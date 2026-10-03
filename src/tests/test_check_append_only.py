"""`scripts/check_append_only.py`：append-only 檔不得把新紀錄寫在檔頭。

判準是回測出來的（798 組 commit×檔只命中 2026-08-07 cd0f3cf4 那一次），本檔把
回測裡出現過的形狀釘成案例：事故要擋、日常的中段補行與 merge 不擋。
"""
import importlib.util
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("check_append_only", REPO / "scripts" / "check_append_only.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

LOG = ["# Wiki 操作日誌", "", "**角色：** 不會遺忘的過去", "",
       "## 2026-08-05 Ingest", "- a", "", "## 2026-08-06 Ingest", "- b", ""]


class TestHeadGrowth(unittest.TestCase):
    def test_entry_written_at_head_is_flagged(self):
        """08-07 事故形狀：新的 `## ` 紀錄插在第一則既有紀錄之前。"""
        new = LOG[:4] + ["## 2026-08-07 Ingest", "- c", ""] + LOG[4:]
        self.assertTrue(mod.head_growth(LOG, new))

    def test_append_at_tail_ok(self):
        self.assertEqual(mod.head_growth(LOG, LOG + ["## 2026-08-07 Ingest", "- c", ""]), [])

    def test_mid_file_amend_ok(self):
        """同日條目事後補行、merge 帶進對方紀錄落在中段——本專案日常，不擋。"""
        new = LOG[:6] + ["- a2（補）"] + LOG[6:]
        self.assertEqual(mod.head_growth(LOG, new), [])

    def test_inplace_fix_and_delete_ok(self):
        fixed = list(LOG)
        fixed[5] = "- a（日期更正）"
        self.assertEqual(mod.head_growth(LOG, fixed), [])
        self.assertEqual(mod.head_growth(LOG, LOG[:5] + LOG[6:]), [])

    def test_md_preamble_rewrite_ok(self):
        """改寫檔頭說明文字（08bd1a93）不是事故：沒有長出新紀錄。"""
        new = LOG[:3] + ["**契約：** 只能 append", ""] + LOG[3:]
        self.assertEqual(mod.head_growth(LOG, new), [])

    def test_jsonl_head_insert_flagged_and_empty_base_ok(self):
        base = ['{"a": 1}', '{"a": 2}', ""]
        self.assertTrue(mod.head_growth(base, ['{"a": 0}'] + base))
        self.assertEqual(mod.head_growth(base, base[:2] + ['{"a": 3}', ""]), [])
        self.assertEqual(mod.head_growth([""], ['{"a": 1}', ""]), [])


class TestConfig(unittest.TestCase):
    def test_exempt_entries_are_in_append_only_list(self):
        for rel in mod.EXEMPT:
            self.assertIn(rel, mod.APPEND_ONLY)


if __name__ == "__main__":
    unittest.main()
