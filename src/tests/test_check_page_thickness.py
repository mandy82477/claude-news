"""check_page_thickness：厚頁清單量的是正文、認得交代、不擋。

2026-10-09：17 波頁面審查零拆頁、patterns 1,135→2,486 行中間沒有任何機械訊號。
守三件事：frontmatter 與 %% 備忘不算行、事件流佔比算得出、沒交代／交代過期才 ⚠️。
"""
import tempfile
import unittest
from datetime import date
from pathlib import Path

from tests._helpers import load_script_module

mod = load_script_module("check_page_thickness")
TODAY = date(2026, 10, 9)


def page(body_lines: int, flow_lines: int = 0, memo: str = "", front: int = 5) -> str:
    fm = "---\n" + "\n".join(f"k{i}: v" for i in range(front)) + "\n---\n"
    body = "# 標題\n\n## 摘要\n" + "\n".join(f"正文 {i}" for i in range(body_lines))
    flow = ("\n## 技術彙整\n### 2026-09\n" + "\n".join(f"- 節點 {i}" for i in range(flow_lines))) if flow_lines else ""
    return fm + body + flow + ("\n%%\n" + memo + "\n%%\n" if memo else "")


class ThicknessTest(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.wiki = Path(self._td.name)
        (self.wiki / "topics").mkdir()
        (self.wiki / "entities").mkdir()

    def tearDown(self):
        self._td.cleanup()

    def write(self, rel: str, text: str):
        (self.wiki / rel).write_text(text, encoding="utf-8")

    def test_counts_body_only_and_skips_archive(self):
        self.write("topics/thin.md", page(100, memo="\n".join(["備忘"] * 600)))   # 備忘 600 行不算
        self.write("topics/thick.md", page(300, flow_lines=400))
        self.write("topics/thick-archive.md", page(2000))
        r = mod.rows(self.wiki, threshold=600, today=TODAY)
        self.assertEqual([x["page"] for x in r], ["topics/thick"])
        self.assertGreater(r[0]["event_flow_share"], 0.5)
        self.assertTrue(r[0]["stale"])
        self.assertIsNone(r[0]["assessed"])

    def test_recent_assessment_clears_flag_and_old_one_does_not(self):
        self.write("topics/a.md", page(700, memo="拆頁評估 2026-09-20：不拆，分不出群"))
        self.write("topics/b.md", page(700, memo="拆頁評估 2026-07-01：不拆，等官方事件"))
        r = {x["page"]: x for x in mod.rows(self.wiki, threshold=600, today=TODAY)}
        self.assertFalse(r["topics/a"]["stale"])
        self.assertEqual(r["topics/a"]["assessment"], "不拆，分不出群")
        self.assertTrue(r["topics/b"]["stale"])

    def test_render_and_exit_zero(self):
        self.write("topics/a.md", page(700))
        text = mod.render(mod.rows(self.wiki, threshold=600, today=TODAY), 600)
        self.assertIn("厚頁清單（5o）：1 頁逾 600 行／1 頁逾 60 天未交代切法", text)
        self.assertIn("⚠️ topics/a", text)
        self.assertEqual(mod.render([], 600), "厚頁清單（5o）：0 頁逾 600 行")


if __name__ == "__main__":
    unittest.main()
