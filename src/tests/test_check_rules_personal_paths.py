"""check_rules 檢查 6（個人路徑外洩）必須連「尚未 git add 的新檔」一起掃。

2026-09-27：量測夾具與測試帶著本機使用者目錄的絕對路徑進了 repo——commit 前 check_rules 綠、
commit 後才紅，因為舊版只掃 `git ls-files`（追蹤檔），新建檔在 add 之前對閘不可見。閘在 commit 前
看不到即將進 repo 的東西，等於沒有閘。
"""
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

mod = load_script_module("check_rules")

BS = chr(92)  # 反斜線；測試用的「個人路徑」以拼接組成，否則本檔自己就會被檢查 6 抓到
LEAK = "C:" + BS + "Users" + BS + "someone"
CFG = {
    "extensions": [".md", ".jsonl"],
    "patterns": ["[A-Za-z]:" + BS * 2 + "+Users" + BS * 2 + "+"],
    "exclude_globs": [],
}


def _git(repo: Path, *args):
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


class TestUntrackedFilesAreScanned(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.repo = Path(self._td.name)
        _git(self.repo, "init", "-q")
        (self.repo / "clean.md").write_text("# fine\n", encoding="utf-8")
        _git(self.repo, "add", "clean.md")
        (self.repo / ".gitignore").write_text("ignored/\n", encoding="utf-8")
        self._orig_root = mod.REPO_ROOT
        mod.REPO_ROOT = self.repo

    def tearDown(self):
        mod.REPO_ROOT = self._orig_root
        self._td.cleanup()

    def _run(self):
        report = mod.Report()
        mod.check_personal_paths(CFG, report)
        return report

    def test_untracked_leak_turns_red(self):
        (self.repo / "new.jsonl").write_text('{"cmd": "cat ' + LEAK.replace(BS, BS * 2) + '"}\n', encoding="utf-8")
        report = self._run()
        self.assertFalse(report.ok)
        self.assertTrue(any("new.jsonl" in d for s in report.sections for d in s["details"]))

    def test_ignored_leak_is_not_scanned(self):
        (self.repo / "ignored").mkdir()
        (self.repo / "ignored" / "scratch.md").write_text(LEAK + "\n", encoding="utf-8")
        self.assertTrue(self._run().ok)

    def test_clean_repo_is_green(self):
        self.assertTrue(self._run().ok)


class TestHomePatternExcludesNumericUrlIds(unittest.TestCase):
    """`/home/` pattern 必須要求使用者名稱片段含至少一個字母，否則撞到新聞原文裡的 URL 路徑。

    2026-11-18：Business Wire 的新聞連結格式為 `.../news/home/<純數字 ID>/en/<slug>`，
    舊版 pattern `/home/[A-Za-z0-9_-]+/` 把這個純數字 ID 誤判成 Unix 家目錄使用者名稱
    （真實使用者名稱幾乎不會是純數字），導致當日抓料檔（`src/gathered_items.json`／
    `src/gathered_archive/<date>.json`）被判外洩，而這兩個檔案本來就不該被要求排除在
    外洩掃描之外（2026-11-09 的 gmail 事故已裁決：不可用 `exclude_globs` 把抓料檔整份
    排除在外，否則真正的外洩也會被放行）。改為要求片段含至少一個字母，真實使用者名稱
    （`someone`、`ubuntu`、`user123`）仍會命中，純數字 URL 路徑段不會。
    """

    CFG = {
        "extensions": [".md", ".jsonl"],
        "patterns": ["/home/(?=[A-Za-z0-9_-]*[A-Za-z])[A-Za-z0-9_-]+/"],
        "exclude_globs": [],
    }

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.repo = Path(self._td.name)
        _git(self.repo, "init", "-q")
        self._orig_root = mod.REPO_ROOT
        mod.REPO_ROOT = self.repo

    def tearDown(self):
        mod.REPO_ROOT = self._orig_root
        self._td.cleanup()

    def _run(self):
        report = mod.Report()
        mod.check_personal_paths(self.CFG, report)
        return report

    def test_numeric_url_path_segment_passes(self):
        (self.repo / "raw.jsonl").write_text(
            '{"url": "https://www.businesswire.com/news/home/20261118974464/en/x"}\n',
            encoding="utf-8",
        )
        self.assertTrue(self._run().ok)

    def test_real_username_home_path_still_turns_red(self):
        leak = "ran from /home/" + "someone" + "/project\n"  # 拼接，避免本檔自己被檢查 6 抓到
        (self.repo / "leak.md").write_text(leak, encoding="utf-8")
        self.assertFalse(self._run().ok)


class TestOwnEmailOnly(unittest.TestCase):
    """信箱只抓使用者自己的（registry 存 sha256）：抓料原文夾帶的第三方信箱不算外洩。

    2026-11-09 起舊版用「任何 @gmail.com」把 HN 原文裡陌生人的信箱當外洩，web build 連續被擋；
    log.md 是 append-only，引述過一次就永遠紅。
    """
    OWN = "owner.example" + "@" + "gmail.com"   # 拼接，避免本檔自己被掃到
    STRANGER = "stranger.example" + "@" + "gmail.com"

    def setUp(self):
        import hashlib
        self._td = tempfile.TemporaryDirectory()
        self.repo = Path(self._td.name)
        _git(self.repo, "init", "-q")
        self._orig_root = mod.REPO_ROOT
        mod.REPO_ROOT = self.repo
        self.cfg = dict(CFG, own_email_sha256=[hashlib.sha256(self.OWN.encode()).hexdigest()])

    def tearDown(self):
        mod.REPO_ROOT = self._orig_root
        self._td.cleanup()

    def _run(self):
        report = mod.Report()
        mod.check_personal_paths(self.cfg, report)
        return report

    def test_third_party_email_passes(self):
        (self.repo / "raw.md").write_text("contact " + self.STRANGER + "\n", encoding="utf-8")
        self.assertTrue(self._run().ok)

    def test_own_email_turns_red(self):
        (self.repo / "leak.md").write_text("mail: " + self.OWN + "\n", encoding="utf-8")
        self.assertFalse(self._run().ok)

    def test_own_email_case_insensitive(self):
        (self.repo / "leak.md").write_text("mail: " + self.OWN.upper() + "\n", encoding="utf-8")
        self.assertFalse(self._run().ok)


if __name__ == "__main__":
    unittest.main()
