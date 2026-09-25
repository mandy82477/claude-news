"""Tests for scripts/check_log_handoffs.py — log 的「轉知」必須對得到帳本單號。

守的是：沒單號也沒寫不登帳理由的轉知行要紅並點名行號；單號打錯（不在帳本）要紅；
只看指定日的 Ingest 區段；不帶日期時舊區段不追溯。
"""
import unittest

from tests._helpers import load_script_module

clh = load_script_module("check_log_handoffs")

LOG = """# log

## 2026-09-24 Ingest

- 來源日報：[[news/2026-09-24]]
   - **模型**：GPT-6 評測轉知功能記者改投 model-task-leaderboard，主編登記 log 待下輪處理
- 轉知帳本：新開 1（H-694685 商業→安全政策）

## 2026-09-24 Query：別的區段

- 這行轉知不在 Ingest 區段，不查

## 2026-09-26 Ingest

- 轉知帳本：新開 1（H-aaaaaa 模型→功能）
- 模型記者另一項轉知已由商業記者同輪處理，不登帳：同輪已派
"""


class TestCheck(unittest.TestCase):
    def test_missing_ref_is_red_with_line_number(self):
        problems, checked, dates = clh.check(LOG, {"H-694685"}, "2026-09-24")
        self.assertEqual(dates, ["2026-09-24"])
        self.assertEqual(checked, 2)
        self.assertEqual(len(problems), 1)
        self.assertIn("wiki/log.md:6（", problems[0])

    def test_ref_or_explicit_skip_passes(self):
        problems, checked, _ = clh.check(LOG, {"H-aaaaaa"}, "2026-09-26")
        self.assertEqual((problems, checked), ([], 2))

    def test_unknown_id_is_red(self):
        problems, _, _ = clh.check(LOG, set(), "2026-09-26")
        self.assertEqual(len(problems), 1)
        self.assertIn("H-aaaaaa", problems[0])

    def test_bare_skip_word_without_reason_is_red(self):
        text = "## 2026-09-26 Ingest\n- 轉知功能記者，不登帳\n"
        problems, _, _ = clh.check(text, set(), "2026-09-26")
        self.assertEqual(len(problems), 1)

    def test_default_scope_skips_sections_before_enforce_from(self):
        problems, _, dates = clh.check(LOG, {"H-aaaaaa"}, None)
        self.assertEqual(dates, ["2026-09-26"])
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
