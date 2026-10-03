"""`.claude/hooks/gate_wiki_commit.py`（H9）：內容閘紅時不准把 wiki/ commit 進 master。

使用者 2026-10-03 裁決。兩條邊界：紅燈內容進不了 master；但停泊分支一定 commit 得進去——
否則雲端修不好的那天，wiki 成果會隨容器消失。
"""
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent.parent / ".claude" / "hooks" / "gate_wiki_commit.py"
_spec = importlib.util.spec_from_file_location("gate_wiki_commit", HOOK)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class TestParsing(unittest.TestCase):
    def test_touches_wiki(self):
        self.assertTrue(mod.touches_wiki("git commit -m x", ["wiki/log.md"]))
        self.assertTrue(mod.touches_wiki("git add wiki/ data/x.jsonl && git commit -m x", []))
        self.assertTrue(mod.touches_wiki('git -C "D:/r" add D:/r/wiki/index.md && git commit -m x', []))
        self.assertFalse(mod.touches_wiki("git add news/2026-10-03.md && git commit -m x", ["data/a.json"]))
        self.assertFalse(mod.touches_wiki("git commit -m x", [".claude/skills/wiki-ingest/SKILL.md"]))

    def test_has_commit(self):
        self.assertTrue(mod.has_commit("git add wiki/ && git commit -m 'x'"))
        self.assertFalse(mod.has_commit("git log --oneline"))
        self.assertFalse(mod.has_commit("echo git commit"))


class TestAgainstRealRepo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        g = lambda *a: subprocess.run(["git", "-C", str(self.root), *a], capture_output=True, check=True)
        self.g = g
        g("init", "-q", "-b", "master")
        g("config", "user.email", "t@example.com")
        g("config", "user.name", "t")
        (self.root / "wiki").mkdir()
        (self.root / "wiki" / "a.md").write_text("a\n", encoding="utf-8")
        (self.root / "scripts").mkdir()
        self.set_gate(0)
        g("add", "-A")
        g("commit", "-q", "-m", "init")
        (self.root / "wiki" / "a.md").write_text("b\n", encoding="utf-8")
        self._env = os.environ.get("CLAUDE_PROJECT_DIR")
        os.environ["CLAUDE_PROJECT_DIR"] = str(self.root)

    def tearDown(self):
        if self._env is None:
            os.environ.pop("CLAUDE_PROJECT_DIR", None)
        else:
            os.environ["CLAUDE_PROJECT_DIR"] = self._env
        self.tmp.cleanup()

    def set_gate(self, code):
        (self.root / "scripts" / "ingest_gate.py").write_text(
            f"import sys\nprint('❌ check_x 紅')\nsys.exit({code})\n", encoding="utf-8")

    def run_hook(self, cmd):
        payload = {"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": str(self.root)}
        old = sys.stdin, sys.stderr
        sys.stdin, sys.stderr = io.StringIO(json.dumps(payload)), io.StringIO()
        try:
            return mod.main()
        finally:
            sys.stdin, sys.stderr = old

    def test_red_gate_blocks_master_commit(self):
        self.set_gate(1)
        self.assertEqual(self.run_hook("git add wiki/ && git commit -m 'wiki: x'"), 2)

    def test_green_gate_allows(self):
        self.set_gate(0)
        self.assertEqual(self.run_hook("git add wiki/ && git commit -m 'wiki: x'"), 0)

    def test_parking_branch_allowed_when_red(self):
        self.set_gate(1)
        self.g("switch", "-q", "-c", "cloud-daily-2026-10-03-unmerged")
        self.assertEqual(self.run_hook("git add wiki/ && git commit -m 'wiki: x'"), 0)

    def test_non_wiki_commit_not_gated(self):
        self.set_gate(1)
        self.assertEqual(self.run_hook("git add news/x.md && git commit -m 'news: x'"), 0)

    def test_gate_crash_fails_open(self):
        (self.root / "scripts" / "ingest_gate.py").unlink()
        self.assertEqual(self.run_hook("git add wiki/ && git commit -m x"), 0)


if __name__ == "__main__":
    unittest.main()
