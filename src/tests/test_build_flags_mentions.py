"""實驗旗標社群提及對帳：純字串命中，零提及就是零；表格靠表頭欄名解析，不靠欄序。"""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("build_flags_mentions", ROOT / "scripts" / "build_flags_mentions.py")
mod = importlib.util.module_from_spec(_spec)
sys.modules["build_flags_mentions"] = mod
_spec.loader.exec_module(mod)

PAGE = """# x
| 旗標 | 首見 | 階 | 官方態度 | 社群反應 | 最後動靜 |
|---|---|---|---|---|---|
| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | 2.1.261 | 3 | issue | 留言 | 09-09 |
| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 | — | — | 09-14 |
| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 | 2 | — | HN | 09-14 |

## 代號旗標
| 旗標 | 動靜 |
|---|---|
| `CLAUDE_CODE_POLISHED_DEWDROP` | 出現 |
- 條列裡的 `CLAUDE_CODE_NOT_A_ROW` 不算
"""
DOCS = [
    {"date": "2026-09-10", "title": "Reddit: tinkering", "url": "https://r/1",
     "text": "I am using CLAUDE_CODE_POST_TURN_MEMORY already"},
    {"date": "2026-09-12", "title": "HN thread", "url": "https://hn/2",
     "text": "CLAUDE_CODE_POST_TURN_MEMORY and CLAUDE_CODE_AUTO_MODE_SERVER"},
    {"date": "2026-09-09", "title": "日報", "url": "news/2026-09-09.md", "text": "nothing here"},
]


class TestFlagsOnPage(unittest.TestCase):
    def test_reads_only_stage_1_and_2_rows_of_the_tracking_table(self):
        self.assertEqual(mod.flags_on_page(PAGE),
                         ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER"])

    def test_reporter_may_add_or_reorder_columns(self):
        """P1-5：欄序改了、多了備註欄，靠表頭仍解析得到。"""
        reordered = PAGE.replace(
            "| 旗標 | 首見 | 階 | 官方態度 | 社群反應 | 最後動靜 |",
            "| 階 | 備註 | 旗標 | 首見 | 官方態度 | 社群反應 | 最後動靜 |").replace(
            "|---|---|---|---|---|---|", "|---|---|---|---|---|---|---|")
        for old, new in (("| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | 2.1.261 | 3 |", "| 3 | x | `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | 2.1.261 |"),
                         ("| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 |", "| 1 | y | `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 |"),
                         ("| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 | 2 |", "| 2 | z | `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 |")):
            reordered = reordered.replace(old, new)
        self.assertEqual(mod.flags_on_page(reordered),
                         ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER"])

    def test_blank_line_inside_table_does_not_truncate(self):
        """P2-A：記者分節手滑插空行，不能只對帳到空行前。"""
        split = PAGE.replace("| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 |",
                             "\n| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 |")
        self.assertEqual(mod.flags_on_page(split),
                         ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER"])

    def test_non_numeric_stage_is_an_error_not_silence(self):
        """P2-A：階欄寫成「1（新）」「1→2」不可靜默跳過，要點名。"""
        for bad in ("1（新）", "1→2", "第 1 階"):
            page = PAGE.replace("| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | 1 |",
                                f"| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.272 | {bad} |")
            with self.assertRaises(mod.PageFormatError) as cm:
                mod.flags_on_page(page)
            self.assertIn("CLAUDE_CODE_POST_TURN_MEMORY", str(cm.exception))

    def test_empty_first_cell_is_not_a_separator(self):
        """P2-C：首欄留空的資料列不是分隔列——要被點名，不能靜默吞掉且列數不變。"""
        page = PAGE.replace("| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 | 2 | — | HN | 09-14 |",
                            "| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.272 | 2 | — | HN | 09-14 |\n"
                            "|  | 2.1.262 | 1 | — | — | 備註列 |")
        with self.assertRaises(mod.PageFormatError) as cm:
            mod.flags_on_page(page)
        self.assertIn("2.1.262", str(cm.exception))
        self.assertEqual(len(mod.parse_table(PAGE)), 3)  # 真分隔列 `---` 仍照常跳過

    def test_missing_stage_column_is_an_error_not_silence(self):
        broken = PAGE.replace("| 旗標 | 首見 | 階 |", "| 旗標 | 首見 | 狀態 |")
        with self.assertRaises(mod.PageFormatError):
            mod.flags_on_page(broken)

    def test_no_table_is_an_error(self):
        with self.assertRaises(mod.PageFormatError):
            mod.flags_on_page("# 只有標題\n\n沒有表格。\n")


class TestCLI(unittest.TestCase):
    def _page(self, text):
        d = Path(tempfile.mkdtemp()); p = d / "page.md"; p.write_text(text, encoding="utf-8"); return p

    def test_format_error_exits_2_but_genuinely_empty_exits_0(self):
        broken = self._page(PAGE.replace("| 旗標 | 首見 | 階 |", "| 旗標 | 首見 | 狀態 |"))
        self.assertEqual(mod.main(["--page", str(broken)]), 2)
        empty = self._page(PAGE.replace("| 1 |", "| 3 |").replace("| 2 |", "| 4 |"))
        self.assertEqual(mod.main(["--page", str(empty)]), 0)
        self.assertEqual(mod.main(["--page", str(Path(tempfile.mkdtemp()) / "nope.md")]), 2)


class TestMentions(unittest.TestCase):
    def test_count_mentions_counts_and_links_sorted_by_date(self):
        r = mod.count_mentions(["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_AUTO_MODE_SERVER",
                                "CLAUDE_CODE_NOBODY"], DOCS)
        self.assertEqual((r["CLAUDE_CODE_POST_TURN_MEMORY"]["count"], r["CLAUDE_CODE_POST_TURN_MEMORY"]["first"]),
                         (2, "2026-09-10"))
        self.assertEqual(r["CLAUDE_CODE_AUTO_MODE_SERVER"]["count"], 1)
        self.assertEqual(r["CLAUDE_CODE_NOBODY"], {"count": 0, "first": None, "links": []})

    def test_render_marks_zero_honestly(self):
        out = mod.render(mod.count_mentions(["CLAUDE_CODE_NOBODY"], DOCS), 14)
        self.assertIn("| `CLAUDE_CODE_NOBODY` | 0 | — | — |", out)
        self.assertIn("零提及只代表本站來源沒抓到", out)


if __name__ == "__main__":
    unittest.main()
