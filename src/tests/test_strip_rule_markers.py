"""scripts/strip_rule_markers.py — 條文日期標記刪除（2026-09-13 標記制度廢除）。"""
import unittest

from tests._helpers import load_script_module

mod = load_script_module("strip_rule_markers")


class TestStrip(unittest.TestCase):
    def test_heading_and_inline_markers_removed(self):
        text = (
            "## 冪等閘 `[加入: 2026-07-25]`\n"
            "- **測試結果 `[加入: 2026-08-01]`：** 過緊\n"
            "聚焦防重複 `[加入: 2026-09-04]`（適用所有正文區塊）\n"
            "### 頁面拆分原則 `[加入: 2026-07-04，改版: 2026-09-07]`\n"
            "區塊順序固定 `[順序改版: 2026-09-04]`：付費在前\n"
            "週報：判準不上螢幕 `[裁決: 2026-08-30]`\n"
            "網站版面 `[改版: 2026-09-12 乙-2]`：頂部先畫\n"
        )
        new, n = mod.strip_text(text)
        self.assertEqual(n, 7)
        self.assertNotIn("[加入", new)
        self.assertNotIn("[改版", new)
        self.assertNotIn("[順序改版", new)
        self.assertNotIn("[裁決", new)
        self.assertEqual(new.splitlines()[0], "## 冪等閘")
        self.assertEqual(new.splitlines()[1], "- **測試結果：** 過緊")
        self.assertEqual(new.splitlines()[2], "聚焦防重複（適用所有正文區塊）")
        self.assertEqual(new.splitlines()[3], "### 頁面拆分原則")

    def test_untouched_text_and_dates_in_prose_stay(self):
        text = "2026-09-04 冷讀者實測後改版。\n見沿革檔 2026-08-13。\n[[topics/x]] 不動。\n"
        new, n = mod.strip_text(text)
        self.assertEqual(n, 0)
        self.assertEqual(new, text)

    def test_placeholder_form_removed_too(self):
        new, n = mod.strip_text("新增條文標 `[加入: YYYY-MM-DD]`，改寫標 `[改版: YYYY-MM-DD]`。\n")
        self.assertEqual(n, 2)


if __name__ == "__main__":
    unittest.main()
