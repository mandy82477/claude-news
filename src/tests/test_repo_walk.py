"""`scripts/repo_walk.py`：整個 repo 掃描共用的列檔，須排除巢狀 git worktree。"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("repo_walk", REPO / "scripts" / "repo_walk.py")
rw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rw)


def _touch(p: Path, text: str = "x") -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


class TestIterFiles(unittest.TestCase):
    def test_skips_nested_worktree_by_git_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            _touch(root / ".claude" / "rules" / "a.md")
            _touch(root / ".claude" / "worktrees" / "w" / ".git", "gitdir: x")
            _touch(root / ".claude" / "worktrees" / "w" / "CLAUDE.md")
            got = {p.relative_to(root).as_posix() for p in rw.iter_files(root / ".claude", root)}
            self.assertEqual(got, {".claude/rules/a.md"})

    def test_skips_worktrees_dir_without_git_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            _touch(root / ".claude" / "worktrees" / "w" / "CLAUDE.md")
            self.assertEqual(list(rw.iter_files(root / ".claude", root)), [])

    def test_nested_git_dir_elsewhere_skipped_but_root_itself_not(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / ".git").mkdir()
            _touch(root / "a.py")
            _touch(root / "sub" / ".git", "gitdir: x")
            _touch(root / "sub" / "b.py")
            self.assertEqual([p.name for p in rw.iter_files(root)], ["a.py"])

    def test_suffix_filter_and_is_nested_worktree(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            _touch(root / "a.md")
            _touch(root / "b.txt")
            self.assertEqual([p.name for p in rw.iter_files(root, suffixes={".md"})], ["a.md"])
            wt = _touch(root / ".claude" / "worktrees" / "w" / "c.md")
            self.assertTrue(rw.is_nested_worktree(root, wt))
            self.assertFalse(rw.is_nested_worktree(root, root / "a.md"))


if __name__ == "__main__":
    unittest.main()
