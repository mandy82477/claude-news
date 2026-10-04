"""程式開發實戰手冊交給開發實務記者之後，會讓料漏掉的五個環節各釘一條。

1. 官方使用指南只有手冊一個家——分類要能直接派給開發實務，包要產得出來。
2. 他每日看 wiki 新增行——自己寫的手冊不能被自己再撿一次。
3. 候選用游標讀、不用日期窗——跳一週不漏。
4. 手冊領域欄仍是工具/功能——轉知的負責人要推得出開發實務。
5. 狀態檔是 data 檔——收尾 commit 漏帶要紅。
"""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module
from tests.test_build_ingest_packets import Sandbox, item, run as run_packets
from tests.test_check_classification_log import D, GATHERED, A, B, C, row

packets = load_script_module("build_ingest_packets")
ccl = load_script_module("check_classification_log")
collect = load_script_module("collect_reporter_reports")
ph = load_script_module("pending_handoffs")
diff = load_script_module("devpractice_diff")
gate = load_script_module("check_devpractice_state")
pm = load_script_module("pending_markers")
spv = load_script_module("scan_pending_verifications")

GUIDE_URL = "https://docs.test/usage-guide"


class TestRoutedToDevpractice(unittest.TestCase):
    def test_usage_guide_gets_its_own_packet(self):
        sb = Sandbox([item(GUIDE_URL, "Official guide: managing long sessions", source="Official Docs")],
                     {GUIDE_URL: {"categories": ["開發實務"], "reason": "", "note": ""}})
        self.addCleanup(sb.close)
        rc, out = run_packets(sb.argv())
        self.assertEqual(rc, 0, out)
        self.assertIn("## [開發實務] 條目（共 1 則", sb.packet("開發實務"))
        self.assertNotIn("未知類別", out)

    def test_classification_log_accepts_devpractice_and_still_rejects_typos(self):
        log = [row(A, ["開發實務"]), row(B, ["開發實物"]), row(C, [], "與 Claude 無關")]
        problems = ccl.reconcile(GATHERED, log, D)
        self.assertEqual([p for p in problems if "未知類別" in p and "開發實務" in p and "開發實物" not in p], [])
        self.assertTrue(any("開發實物" in p for p in problems))

    def test_devpractice_report_is_parsed_and_needs_no_reroute_field(self):
        r = collect.parse_report("## 開發實務 記者回報\n更新頁面：topics/coding-workflow-guide\n來源歸因：無\n")
        self.assertEqual(r["category"], "開發實務")
        self.assertIn("開發實務", collect.REPORTERS)


class TestDiffAndCursor(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        d = Path(self.tmp.name)
        self._orig = (diff.STATE, diff.LEDGER)
        diff.STATE, diff.LEDGER = d / "state.json", d / "ledger.jsonl"
        self.addCleanup(lambda: setattr(diff, "STATE", self._orig[0]) or setattr(diff, "LEDGER", self._orig[1]))

    def _ledger(self, n):
        diff.LEDGER.write_text("".join(json.dumps({"n": i}) + "\n" for i in range(n)), encoding="utf-8")

    def test_own_page_is_excluded_from_diff(self):
        self.assertTrue(any("CLAUDE_NEWS/wiki/topics/coding-workflow-guide.md".endswith(e) for e in diff.EXCLUDE))

    def test_cursor_survives_a_skipped_week(self):
        self._ledger(3)
        diff.consume()
        self._ledger(8)  # 兩週份的新候選一次進來
        state = json.loads(diff.STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["consumed_lines"], 3)
        self.assertEqual(len(diff._ledger_lines()[state["consumed_lines"]:]), 5)

    def test_mark_keeps_the_cursor(self):
        self._ledger(4)
        diff.consume()
        diff.mark()
        state = json.loads(diff.STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["consumed_lines"], 4)
        self.assertTrue(state["last_sha"])

    def test_truncated_ledger_rereads_everything(self):
        self._ledger(5)
        diff.consume()
        self._ledger(2)
        self.assertEqual(diff.pending(), 0)  # 不炸；游標大於行數時從頭讀


class TestOwner(unittest.TestCase):
    def test_guide_owner_is_devpractice_despite_domain_column(self):
        self.assertEqual(ph.OWNER_OVERRIDES.get("topics/coding-workflow-guide"), "開發實務")
        self.assertEqual(ph.owner_of("topics/coding-workflow-guide")[0], "開發實務")

    def test_pending_hits_on_guide_go_to_devpractice(self):
        guide = pm.WIKI_DIR / "topics" / "coding-workflow-guide.md"
        self.assertEqual(pm.reporter_of(guide), "wiki-reporter-devpractice")
        self.assertEqual(spv.REPORTER_LABEL[pm.reporter_of(guide)], "開發實務")
        self.assertEqual(pm.reporter_of(pm.WIKI_DIR / "entities" / "claude-code.md"), "wiki-reporter-features")


def _git(repo, *args):
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   cwd=repo, check=True, capture_output=True)


class TestStateCommitted(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = r = Path(self.tmp.name)
        _git(r, "init", "-q")
        (r / "wiki").mkdir()
        (r / "data").mkdir()
        (r / "wiki" / "log.md").write_text("# log\n", encoding="utf-8")
        (r / "data" / "devpractice_state.json").write_text("{}\n", encoding="utf-8")
        _git(r, "add", ".")
        _git(r, "commit", "-q", "-m", "init")

    def _ingest(self, date, with_state):
        r = self.repo
        with (r / "wiki" / "log.md").open("a", encoding="utf-8") as f:
            f.write(f"\n## {date} Ingest\n\n- x\n")
        _git(r, "add", "wiki/log.md")
        if with_state:
            (r / "data" / "devpractice_state.json").write_text(json.dumps({"d": date}) + "\n", encoding="utf-8")
            _git(r, "add", "data/devpractice_state.json")
        _git(r, "commit", "-q", "-m", f"ingest {date}")

    def test_state_in_ingest_commit_is_green(self):
        self._ingest("2026-11-01", with_state=True)
        self.assertTrue(gate.check(self.repo, enforce_from="2026-10-05")[0])

    def test_ingest_commit_without_state_is_red(self):
        self._ingest("2026-11-01", with_state=True)
        self._ingest("2026-11-02", with_state=False)
        ok, msg = gate.check(self.repo, enforce_from="2026-10-05")
        self.assertFalse(ok)
        self.assertIn("2026-11-02", msg)

    def test_follow_up_commit_heals_it(self):
        self._ingest("2026-11-02", with_state=False)
        (self.repo / "data" / "devpractice_state.json").write_text('{"late": 1}\n', encoding="utf-8")
        _git(self.repo, "add", "data/devpractice_state.json")
        _git(self.repo, "commit", "-q", "-m", "補 commit 狀態檔")
        self.assertTrue(gate.check(self.repo, enforce_from="2026-10-05")[0])

    def test_before_enforce_date_is_not_checked(self):
        self._ingest("2026-10-01", with_state=False)
        self.assertTrue(gate.check(self.repo, enforce_from="2026-10-05")[0])


if __name__ == "__main__":
    unittest.main()
