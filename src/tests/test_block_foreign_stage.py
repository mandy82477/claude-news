"""`block_foreign_stage.py` 看守：commit 不得掃走別的 session 宣告中的路徑。

死因見該檔 docstring（2026-09-13，指名路徑 add 掃走另一 session 的半成品）。
本測試釘住三件事：擋得到、不誤擋、以及**失效方向一律是放行**——宣告過期、
宣告壞掉、不在 git repo 裡，都不可以把使用者卡死。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import importlib.util

HOOK = Path(__file__).resolve().parent.parent.parent / ".claude" / "hooks" / "block_foreign_stage.py"
_spec = importlib.util.spec_from_file_location("block_foreign_stage", HOOK)
hook = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hook)


class _Root:
    """一個帶 tree-claims 的假 repo root。"""

    def __init__(self, tmp: str):
        self.path = Path(tmp)
        (self.path / ".claude" / "tree-claims").mkdir(parents=True)

    def claim(self, session: str, paths: list[str], note: str = "", age_s: int = 0):
        f = self.path / ".claude" / "tree-claims" / f"{session}.json"
        f.write_text(json.dumps({"session": session, "paths": paths, "note": note}),
                     encoding="utf-8")
        if age_s:
            import os
            import time
            old = time.time() - age_s
            os.utime(f, (old, old))
        return f


class ForeignStageTest(unittest.TestCase):
    def _run(self, root: _Root, command: str, session: str = "mine", staged=()):
        payload = {"tool_name": "Bash", "session_id": session,
                   "tool_input": {"command": command}}
        import io as _io
        import types
        buf = _io.StringIO()
        # 不可 patch `hook.sys.stderr`——`hook.sys` 就是全域 sys 模組，改它會污染
        # 整個測試套件（實測：本檔單跑 7 綠，全套跑掛 54 個，logging handler 指到
        # 被換掉的 stream）。改成替換模組自己持有的 sys 參照。
        stub = types.SimpleNamespace(stdin=_io.StringIO(json.dumps(payload)), stderr=buf)
        with patch.object(hook, "_repo_root", return_value=root.path), \
             patch.object(hook, "_touched_paths", return_value=list(staged)), \
             patch.object(hook, "sys", stub):
            code = hook.main()
        return code, buf.getvalue()

    def test_blocks_when_staging_another_sessions_claimed_path(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("peer-62", ["wiki/", "weekly/"], note="跑 /weekly 中")
            code, err = self._run(root, "git add wiki/ && git commit -m x",
                                  staged=["wiki/log.md", "scripts/ok.py"])
            self.assertEqual(code, 2)
            self.assertIn("peer-62", err)
            self.assertIn("wiki/log.md", err)
            self.assertIn("跑 /weekly 中", err, "要說出對方在做什麼，才判斷得了要不要等")
            self.assertNotIn("scripts/ok.py", err, "沒被宣告的檔案不該出現在擋下清單裡")

    def test_my_own_claim_never_blocks_me(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("mine", ["wiki/"])
            code, _ = self._run(root, "git add wiki/", session="mine",
                                staged=["wiki/log.md"])
            self.assertEqual(code, 0)

    def test_disjoint_paths_do_not_block(self):
        """今天實測兩個 session 檔案集重疊為零——那種情況必須零摩擦。"""
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("peer-62", ["wiki/"])
            code, _ = self._run(root, "git add scripts/", staged=["scripts/a.py"])
            self.assertEqual(code, 0)

    def test_stale_claim_expires(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("ghost", ["wiki/"], age_s=(hook.STALE_MINUTES + 10) * 60)
            code, _ = self._run(root, "git add wiki/", staged=["wiki/log.md"])
            self.assertEqual(code, 0, "過期宣告不得把樹卡死")

    def test_corrupt_claim_is_ignored_not_fatal(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            (root.path / ".claude" / "tree-claims" / "bad.json").write_text(
                "{not json", encoding="utf-8")
            code, _ = self._run(root, "git add wiki/", staged=["wiki/log.md"])
            self.assertEqual(code, 0, "宣告檔壞掉要當作不存在，不是擋人")

    def test_dotfile_paths_are_not_mangled(self):
        """`.claude/` 這種點開頭的路徑不得被切成 `claude/`。

        第一版用 `lstrip("./")` 正規化，那是字元集合去除，會把開頭的點一起吃掉——
        dogfood 時印出 `claude/hooks/`，比對也會跟著錯。
        """
        self.assertEqual(hook._norm(".claude/hooks/"), ".claude/hooks/")
        self.assertEqual(hook._norm("./wiki/log.md"), "wiki/log.md")
        self.assertEqual(hook._norm(".github/workflows"), ".github/workflows")

    def test_blocks_dotfile_claim_end_to_end(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("peer", [".claude/hooks/"])
            code, err = self._run(root, "git add .claude/hooks/",
                                  staged=[".claude/hooks/x.py"])
            self.assertEqual(code, 2)
            self.assertIn(".claude/hooks/x.py", err)

    def test_non_git_command_passes(self):
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            root.claim("peer-62", ["wiki/"])
            code, _ = self._run(root, "python scripts/run_tests.py",
                                staged=["wiki/log.md"])
            self.assertEqual(code, 0)

    def test_git_add_argument_counts_even_before_it_runs(self):
        """`git add wiki/ && git commit` 在 add 尚未執行時 staged 是空的，
        仍必須從指令本身認出 wiki/。"""
        with TemporaryDirectory() as tmp:
            root = _Root(tmp)
            with patch.object(hook, "subprocess") as sp:
                sp.run.return_value.returncode = 1
                sp.run.return_value.stdout = ""
                got = hook._touched_paths(root.path, "git add wiki/ weekly/ && git commit -m x")
            self.assertIn("wiki/", got)
            self.assertIn("weekly/", got)


if __name__ == "__main__":
    unittest.main()
