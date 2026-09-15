"""實驗旗標社群提及對帳：純字串命中，零提及就是零。"""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("build_flags_mentions", ROOT / "scripts" / "build_flags_mentions.py")
mod = importlib.util.module_from_spec(_spec)
sys.modules["build_flags_mentions"] = mod
_spec.loader.exec_module(mod)

PAGE = """# x
| 旗標 | 首見版本 | 階 | 官方態度 | 社群反應 | 最後動靜 |
|---|---|---|---|---|---|
| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | 2.1.261 | 3 | issue | 留言 | 09-09 |
| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 | — | — | 09-14 |
| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 | 2 | — | HN | 09-14 |
- 條列裡的 `CLAUDE_CODE_NOT_A_ROW` 不算
"""
DOCS = [
    {"date": "2026-09-10", "title": "Reddit: tinkering", "url": "https://r/1",
     "text": "I am using CLAUDE_CODE_POST_TURN_MEMORY already"},
    {"date": "2026-09-12", "title": "HN thread", "url": "https://hn/2",
     "text": "CLAUDE_CODE_POST_TURN_MEMORY and CLAUDE_CODE_AUTO_MODE_SERVER"},
    {"date": "2026-09-09", "title": "日報", "url": "news/2026-09-09.md", "text": "nothing here"},
]


class TestMentions(unittest.TestCase):
    def test_flags_on_page_reads_only_stage_1_and_2_rows(self):
        self.assertEqual(mod.flags_on_page(PAGE),
                         ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER"])

    def test_count_mentions_counts_and_links_sorted_by_date(self):
        r = mod.count_mentions(["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER",
                                "CLAUDE_CODE_NOBODY"], DOCS)
        self.assertEqual(r["CLAUDE_CODE_POST_TURN_MEMORY"]["count"], 2)
        self.assertEqual(r["CLAUDE_CODE_POST_TURN_MEMORY"]["first"], "2026-09-10")
        self.assertEqual(r["CLAUDE_CODE_AUTO_MODE_SERVER"]["count"], 1)
        self.assertEqual(r["CLAUDE_CODE_NOBODY"], {"count": 0, "first": None, "links": []})

    def test_render_marks_zero_honestly(self):
        out = mod.render(mod.count_mentions(["CLAUDE_CODE_NOBODY"], DOCS), 14)
        self.assertIn("| `CLAUDE_CODE_NOBODY` | 0 | — | — |", out)
        self.assertIn("零提及只代表本站來源沒抓到", out)


if __name__ == "__main__":
    unittest.main()
