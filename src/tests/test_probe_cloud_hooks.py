"""`.claude/hooks/probe_cloud_hooks.py`：雲端被動探針只在雲端寫、每 session 一次、不擾亂看門狗。

最後一條最要緊：探針行若被 daily_health_check 算成上一班的「結果」，一個中途死掉的班次
會看起來正常結束——探針本身就成了新的盲點。
"""
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("probe_cloud_hooks", REPO / ".claude" / "hooks" / "probe_cloud_hooks.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)
_hspec = importlib.util.spec_from_file_location("daily_health_check", REPO / "scripts" / "daily_health_check.py")
health = importlib.util.module_from_spec(_hspec)
_hspec.loader.exec_module(health)


class TestProbe(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "src" / "logs").mkdir(parents=True)
        self.log = self.root / "src" / "logs" / "task_scheduler.log"
        self.log.write_text("[cloud daily-news-pipeline-cloud STARTED 2026-10-03T12:08:00Z]\n", encoding="utf-8")
        self.sid = "probe-test-" + os.urandom(4).hex()

    def tearDown(self):
        marker = Path(tempfile.gettempdir()) / f"claude-news-hooks-probe-{self.sid}"
        marker.unlink(missing_ok=True)
        self.tmp.cleanup()

    def run_hook(self, remote, tool="Bash"):
        env = {"CLAUDE_CODE_REMOTE": "true" if remote else "", "CLAUDE_PROJECT_DIR": str(self.root)}
        payload = {"tool_name": tool, "tool_input": {"command": "ls"}, "session_id": self.sid}
        with mock.patch.dict(os.environ, env):
            old = sys.stdin
            sys.stdin = io.StringIO(json.dumps(payload))
            try:
                return mod.main()
            finally:
                sys.stdin = old

    def probe_lines(self):
        return [ln for ln in self.log.read_text(encoding="utf-8").splitlines() if "hooks-probe" in ln]

    def test_local_writes_nothing(self):
        self.assertEqual(self.run_hook(remote=False), 0)
        self.assertEqual(self.probe_lines(), [])

    def test_cloud_writes_once_per_session(self):
        self.assertEqual(self.run_hook(remote=True), 0)
        self.assertEqual(self.run_hook(remote=True), 0)
        lines = self.probe_lines()
        self.assertEqual(len(lines), 1)
        self.assertRegex(lines[0], r"^\[cloud hooks-probe ACTIVE \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\]")

    def test_non_shell_tool_ignored(self):
        self.run_hook(remote=True, tool="Read")
        self.assertEqual(self.probe_lines(), [])

    def test_probe_line_does_not_mask_a_dead_shift(self):
        """上一班 STARTED 後就死了；探針行接在後面（下一班第一個 Bash 前）不可讓它看起來有結果。"""
        self.run_hook(remote=True)
        now = datetime(2026, 10, 3, 20, 0, tzinfo=timezone.utc)
        orphans = health.orphan_starts(date(2026, 10, 3), repo=self.root, now=now)
        self.assertEqual([o["routine"] for o in orphans], ["daily-news-pipeline-cloud"])

    def test_probe_before_started_keeps_finished_shift_finished(self):
        """探針寫在新班 STARTED 之前；新班之後的結果行仍歸新班。"""
        self.run_hook(remote=True)
        with open(self.log, "a", encoding="utf-8") as f:
            f.write("[cloud daily-news-pipeline-cloud STARTED 2026-10-03T17:08:00Z]\n")
            f.write("[週五 2026/10/03 18:03:37.00] === Pipeline complete (agent) ===\n")
        now = datetime(2026, 10, 3, 23, 0, tzinfo=timezone.utc)
        starts = [o["started"] for o in health.orphan_starts(date(2026, 10, 3), repo=self.root, now=now)]
        self.assertNotIn("17:08", starts)


if __name__ == "__main__":
    unittest.main()
