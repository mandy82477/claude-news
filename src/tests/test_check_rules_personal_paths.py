"""check_rules 檢查 6（個人路徑外洩）必須連「尚未 git add 的新檔」一起掃。

2026-09-27：量測夾具與測試帶著 `C:\\Users\\<帳號>` 進了 repo——commit 前 check_rules 綠、commit 後才紅，
因為舊版只掃 `git ls-files`（追蹤檔），新建檔在 add 之前對閘不可見。閘在 commit 前看不到即將進 repo
的東西，等於沒有閘。
"""
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

mod = load_script_module("check_rules")

CFG = {
    "extensions": [".md", ".jsonl"],
    "patterns": [r"[A-Za-z]:\\+Users\\+"],
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
        (self.repo / "new.jsonl").write_text('{"cmd": "cat C:\\\\Users\\\\someone\\\\x.md"}\n', encoding="utf-8")
        report = self._run()
        self.assertFalse(report.ok)
        self.assertTrue(any("new.jsonl" in d for s in report.sections for d in s["details"]))

    def test_ignored_leak_is_not_scanned(self):
        (self.repo / "ignored").mkdir()
        (self.repo / "ignored" / "scratch.md").write_text("C:\\Users\\someone\\x\n", encoding="utf-8")
        self.assertTrue(self._run().ok)

    def test_clean_repo_is_green(self):
        self.assertTrue(self._run().ok)


if __name__ == "__main__":
    unittest.main()
