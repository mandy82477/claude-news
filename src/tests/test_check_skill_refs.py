"""scripts/check_skill_refs.py — skill 指路完整性閘。

規格端 SKILL-PRINCIPLES.md：description ≤100、目錄只有 references/ scripts/ assets/、
SKILL.md 指到的 reference 要存在、references/ 不得有孤兒、SKILL.md ≤500 行。
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

mod = load_script_module("check_skill_refs")

GOOD = """---
name: demo
description: 示範用 skill
---
# Demo
步驟一：先讀 references/format.md。
"""


class _Case(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.addCleanup(self.td.cleanup)
        self.skill = Path(self.td.name) / "demo"
        (self.skill / "references").mkdir(parents=True)

    def write(self, rel: str, text: str):
        p = self.skill / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")


class TestSkillRefs(_Case):
    def test_good_skill_passes(self):
        self.write("SKILL.md", GOOD)
        self.write("references/format.md", "# f\n")
        self.assertEqual(mod.check_skill(self.skill), [])

    def test_missing_reference_flagged(self):
        self.write("SKILL.md", GOOD)
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("檔不存在" in p for p in probs))

    def test_orphan_reference_flagged(self):
        self.write("SKILL.md", GOOD)
        self.write("references/format.md", "# f\n")
        self.write("references/lonely.md", "# 沒人指我\n")
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("孤兒" in p and "lonely.md" in p for p in probs))

    def test_top_level_stray_file_and_bad_dir_flagged(self):
        self.write("SKILL.md", GOOD)
        self.write("references/format.md", "# f\n")
        self.write("notes.md", "x\n")
        self.write("docs/x.md", "x\n")
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("頂層多了 notes.md" in p for p in probs))
        self.assertTrue(any("docs/" in p for p in probs))

    def test_long_description_flagged(self):
        self.write("SKILL.md", GOOD.replace("示範用 skill", "長" * 101))
        self.write("references/format.md", "# f\n")
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("超過 100" in p for p in probs))

    def test_missing_description_flagged(self):
        self.write("SKILL.md", "---\nname: demo\n---\n# Demo\n")
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("缺 description" in p for p in probs))

    def test_over_500_lines_flagged(self):
        self.write("SKILL.md", GOOD + "行\n" * 500)
        self.write("references/format.md", "# f\n")
        probs = mod.check_skill(self.skill)
        self.assertTrue(any("超過 500" in p for p in probs))


if __name__ == "__main__":
    unittest.main()
