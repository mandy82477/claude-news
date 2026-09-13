"""scripts/registry_relocate.py — registry 路徑搬家。

只改「值恰等於舊路徑」的字串；含舊路徑片段的 pattern／_note 不改，列給人判斷。
"""
import copy
import unittest

from tests._helpers import load_script_module

mod = load_script_module("registry_relocate")

REG = {
    "_doc": "x",
    "path_existence": {"allowlist_patterns": ["^daily/TARGET_DATE\\.md$"]},
    "sync_pairs": [
        {"name": "A", "files": [".claude/commands/foo.md", "scripts/x.py"],
         "patterns": ["foo\\.md", "SOME_CONST"], "_note": "見 .claude/commands/foo.md"},
        {"name": "B", "files": [".claude/commands/bar.md"], "patterns": ["bar"]},
    ],
}


class TestRelocate(unittest.TestCase):
    def test_exact_file_values_replaced_and_patterns_reported(self):
        data = copy.deepcopy(REG)
        n, changed, review = mod.relocate(data, ".claude/commands/foo.md", ".claude/skills/foo/SKILL.md")
        self.assertEqual(n, 1)
        self.assertEqual(data["sync_pairs"][0]["files"][0], ".claude/skills/foo/SKILL.md")
        self.assertEqual(data["sync_pairs"][0]["files"][1], "scripts/x.py")
        # pattern 含檔名片段、_note 含舊路徑 → 不改，列出來
        self.assertEqual(data["sync_pairs"][0]["patterns"][0], "foo\\.md")
        self.assertTrue(any("patterns" in r for r in review))
        self.assertTrue(any("_note" in r for r in review))
        self.assertEqual(data["sync_pairs"][1]["files"][0], ".claude/commands/bar.md")

    def test_backslash_paths_normalised(self):
        data = copy.deepcopy(REG)
        n, _, _ = mod.relocate(data, ".claude\\commands\\bar.md", ".claude/skills/bar/SKILL.md")
        self.assertEqual(n, 1)
        self.assertEqual(data["sync_pairs"][1]["files"][0], ".claude/skills/bar/SKILL.md")

    def test_no_match_changes_nothing(self):
        data = copy.deepcopy(REG)
        n, changed, review = mod.relocate(data, ".claude/commands/none.md", "x.md")
        self.assertEqual((n, changed), (0, []))
        self.assertEqual(data, REG)


if __name__ == "__main__":
    unittest.main()
