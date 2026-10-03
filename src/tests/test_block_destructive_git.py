"""`.claude/hooks/block_destructive_git.py`：共用工作樹的破壞性 git 指令。

兩條邊界都要守：
- 該擋的：2026-09-05 記者 `git stash` 捲走三頁、2026-09-29 雲端 `push HEAD:master`。
- 不該擋的：管線本身會用的指令（web-publish 的 replay 還原、push 重試的
  `pull --rebase`、`rebase --abort`）。誤擋這些等於讓每日管線推不上去。
"""
import importlib.util
import io
import json
import os
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
HOOK = REPO / ".claude" / "hooks" / "block_destructive_git.py"
_spec = importlib.util.spec_from_file_location("block_destructive_git", HOOK)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class TestAllSessions(unittest.TestCase):
    def test_blocks_whole_tree_and_history_rewrites(self):
        for cmd in (
            "git stash", "git stash push -m x", "git stash pop", "git stash drop", "git stash -u",
            "git pull --rebase --autostash", "git -c rebase.autostash=true pull --rebase",
            "git -c rebase.autoStash=true rebase origin/master",
            "git reset --hard", "git reset --hard HEAD~1", "git reset --merge",
            "git clean -fd", "git clean -fdx", "git clean -f -- wiki/",
            "git checkout -- .", "git checkout .", "git checkout HEAD -- :/",
            "git restore .", "git restore --worktree --staged .",
            "git checkout -f master", "git switch --discard-changes master", "git switch -f x",
            "git push --force", "git push -f origin master", "git push --force-with-lease",
            "git push --mirror", "git push origin +master",
            "git push origin HEAD:master", "git push origin HEAD:refs/heads/master",
            "git checkout -B master", "git switch -C master",
            'git -C "C:/repo" stash', "cd x && git stash && git pull",
            'bash -c "git reset --hard"',
        ):
            with self.subTest(cmd=cmd):
                self.assertIsNotNone(mod.violation(cmd))

    def test_allows_pipeline_and_readonly_commands(self):
        for cmd in (
            "git checkout -- src/gathered_items.json",
            "git -C REPO_ROOT checkout -- src/gathered_items.json",
            "git pull --rebase origin master", "git pull --ff-only", "git fetch origin",
            "git rebase --abort", "git -c core.editor=true rebase --continue",
            "git reset", "git reset HEAD wiki/x.md", "git reset --soft HEAD~1",
            "git restore --staged .", "git restore wiki/a.md",
            "git stash list", "git stash show -p",
            "git clean -n", "git clean --dry-run -d",
            "git push", "git push origin master", "git push -u origin cloud-daily-2026-10-03-unmerged",
            "git push origin master:master", "git checkout -b feature", "git switch master",
            "git pull --no-autostash",
            "git commit -m 'never git stash; never git reset --hard'",
            "echo git push --force", "grep 'git clean -fd' docs/x.md",
        ):
            with self.subTest(cmd=cmd):
                self.assertIsNone(mod.violation(cmd))


class TestSharedTreeSubagent(unittest.TestCase):
    def test_blocks_rule_list(self):
        for cmd in (
            "git checkout -- wiki/a.md", "git restore wiki/a.md", "git reset HEAD x",
            "git pull", "git pull --ff-only", "git rebase origin/master", "git merge origin/master",
            "git switch master", "git cherry-pick abc", "git clean -f wiki/x.md",
        ):
            with self.subTest(cmd=cmd):
                self.assertIsNotNone(mod.violation(cmd, is_shared_subagent=True))

    def test_allows_readonly(self):
        for cmd in ("git status", "git diff", "git log --oneline -5", "git stash list",
                    "git clean -n", "git show HEAD:wiki/a.md"):
            with self.subTest(cmd=cmd):
                self.assertIsNone(mod.violation(cmd, is_shared_subagent=True))


class TestMainPayload(unittest.TestCase):
    def setUp(self):
        self._env = os.environ.get("CLAUDE_PROJECT_DIR")
        os.environ["CLAUDE_PROJECT_DIR"] = str(REPO)

    def tearDown(self):
        if self._env is None:
            os.environ.pop("CLAUDE_PROJECT_DIR", None)
        else:
            os.environ["CLAUDE_PROJECT_DIR"] = self._env

    def run_hook(self, cmd, **extra):
        payload = {"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": str(REPO), **extra}
        old = sys.stdin, sys.stderr
        sys.stdin, sys.stderr = io.StringIO(json.dumps(payload)), io.StringIO()
        try:
            return mod.main()
        finally:
            sys.stdin, sys.stderr = old

    def test_identity_from_agent_id(self):
        """子 agent 身分取自 PreToolUse 輸入的 agent_id（2026-10-03 實測：主 session 無此欄）。"""
        cmd = "git checkout -- wiki/a.md"
        self.assertEqual(self.run_hook(cmd), 0)
        self.assertEqual(self.run_hook(cmd, agent_id="a1", agent_type="general-purpose"), 2)

    def test_worktree_isolated_subagent_not_restricted(self):
        """`isolation: worktree` 的子 agent 在自己的樹裡，不受共用樹限制。"""
        cwd = str(REPO / ".claude" / "worktrees" / "agent-x")
        self.assertEqual(self.run_hook("git checkout -- wiki/a.md", agent_id="a1", cwd=cwd), 0)
        self.assertEqual(self.run_hook("git stash", agent_id="a1", cwd=cwd), 2)

    def test_non_shell_tools_pass(self):
        payload = {"tool_name": "Read", "tool_input": {"command": "git stash"}}
        old = sys.stdin
        sys.stdin = io.StringIO(json.dumps(payload))
        try:
            self.assertEqual(mod.main(), 0)
        finally:
            sys.stdin = old


if __name__ == "__main__":
    unittest.main()
