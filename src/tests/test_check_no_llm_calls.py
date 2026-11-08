"""`scripts/check_no_llm_calls.py`：程式碼裡的 `claude -p` 與 LLM SDK 匯入。

hook 只看得到 session 當場下的指令；寫進程式碼、以後才跑的呼叫要靠這道靜態閘。
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("check_no_llm_calls", REPO / "scripts" / "check_no_llm_calls.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class TestScanPython(unittest.TestCase):
    def test_flags_calls_and_imports(self):
        for src in (
            "import anthropic\n",
            "from openai import OpenAI\n",
            "import subprocess\nsubprocess.run(['claude', '-p', 'hi'])\n",
            "import os\nos.system('claude --print summarize')\n",
            "CMD = ('claude.exe', '--print')\n",
        ):
            with self.subTest(src=src):
                self.assertTrue(mod.scan_python(src))

    def test_ignores_prose_and_lookalikes(self):
        for src in (
            '"""禁止 `claude -p`：本專案沒有 API key。"""\n',
            "MSG = '🚫 擋下 claude -p'\n",
            "x = ['python', '-p']\n",
            "import anthropic_tools_stub as t\n",
        ):
            with self.subTest(src=src):
                self.assertEqual(mod.scan_python(src), [])


class TestScanShell(unittest.TestCase):
    def test_workflow_run_line(self):
        self.assertTrue(mod.scan_shell("steps:\n  - run: claude -p 'daily'\n"))
        self.assertTrue(mod.scan_shell("echo start\nnpx @anthropic-ai/claude-code -p x\n"))

    def test_comments_and_echo_ignored(self):
        self.assertEqual(mod.scan_shell("# claude -p is banned\necho 'no claude -p'\n"), [])


class TestScanSettings(unittest.TestCase):
    def test_hook_command(self):
        self.assertTrue(mod.scan_settings('{"hooks":{"Stop":[{"hooks":[{"command":"claude -p hi"}]}]}}'))
        self.assertEqual(mod.scan_settings('{"hooks":{"Stop":[{"hooks":[{"command":"python x.py"}]}]}}'), [])


class TestNestedWorktree(unittest.TestCase):
    """Claude Desktop 在 .claude/worktrees/ 開的 git worktree 是 repo 副本，不是本 repo 的程式碼。"""

    def _fake_repo(self, tmp: Path) -> Path:
        wt = tmp / ".claude" / "worktrees" / "x"
        (wt / "scripts").mkdir(parents=True)
        (wt / ".git").write_text("gitdir: /elsewhere/.git/worktrees/x\n", encoding="utf-8")
        (wt / "scripts" / "bad.sh").write_text("claude -p 'hi'\n", encoding="utf-8")
        return tmp

    def test_worktree_copy_not_reported(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(mod.scan(self._fake_repo(Path(d))), [])

    def test_worktree_without_git_file_still_excluded(self):
        """worktree 被 prune 後 .git 檔可能不在，.claude/worktrees/ 路徑本身仍要排除。"""
        with tempfile.TemporaryDirectory() as d:
            root = self._fake_repo(Path(d))
            (root / ".claude" / "worktrees" / "x" / ".git").unlink()
            self.assertEqual(mod.scan(root), [])

    def test_real_hits_next_to_worktree_still_found(self):
        """排除只針對巢狀 worktree，不能把真命中一起吞掉（包括尚未 git add 的新檔）。"""
        with tempfile.TemporaryDirectory() as d:
            root = self._fake_repo(Path(d))
            (root / "scripts").mkdir()
            (root / "scripts" / "real.sh").write_text("claude -p 'hi'\n", encoding="utf-8")
            self.assertEqual([f[0] for f in mod.scan(root)], ["scripts/real.sh"])


class TestRepoClean(unittest.TestCase):
    def test_no_new_hits_in_repo(self):
        """repo 現況除已知存量外零命中；新命中＝有人把 LLM 呼叫寫進程式碼了。"""
        new = [f for f in mod.scan() if f[0] not in mod.ALLOW and f[0] not in mod.KNOWN]
        self.assertEqual(new, [])

    def test_allow_and_known_entries_exist(self):
        """白名單指向已不存在的檔＝殘留豁免，要清掉。"""
        for rel in list(mod.ALLOW) + list(mod.KNOWN):
            with self.subTest(rel=rel):
                self.assertTrue((REPO / rel).is_file())


if __name__ == "__main__":
    unittest.main()
