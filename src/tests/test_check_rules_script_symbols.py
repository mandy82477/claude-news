"""check_rules 檢查 7：規則檔同一行提到腳本與符號時，符號必須存在於那支腳本。

2026-10-08：weekly-report 的契約表指著 check_weekly_ledger.py 已改名的 HEADLINE_SECTION_RE，
registry 的 sync_pairs 沒登記這一組，靠人工 review 才抓到。這一檢查不需登記：掃到就查。
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

mod = load_script_module("check_rules")


class TestScriptSymbols(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        (self.root / "scripts").mkdir()
        (self.root / "rules").mkdir()
        (self.root / "scripts" / "check_x.py").write_text(
            "HEADLINE_DECK_RE = 1\n\ndef deepdive_visible_len(body):\n    return 0\n", encoding="utf-8")
        self._orig = mod.REPO_ROOT
        mod.REPO_ROOT = self.root

    def tearDown(self):
        mod.REPO_ROOT = self._orig
        self._td.cleanup()

    def run_check(self, md: str):
        (self.root / "rules" / "r.md").write_text(md, encoding="utf-8")
        report = mod.Report()
        mod.check_script_symbols(
            {"globs": ["rules/*.md"], "ignore_symbols": ["NOT_A_SYMBOL"], "symbol_homes": ["scripts/*.py"]}, report)
        return report.ok, "\n".join(report.sections[-1]["details"])

    def test_existing_symbols_pass(self):
        ok, _ = self.run_check("| 頭條 | `check_x.py` HEADLINE_DECK_RE、`deepdive_visible_len()` | 擋 |\n")
        self.assertTrue(ok)

    def test_renamed_symbol_fails_with_location(self):
        ok, details = self.run_check("x\n| 節 | `scripts/check_x.py` HEADLINE_SECTION_RE | 跳過 |\n")
        self.assertFalse(ok)
        self.assertIn("rules/r.md:2", details)
        self.assertIn("HEADLINE_SECTION_RE", details)

    def test_symbol_living_in_another_script_is_layout_not_drift(self):
        # 契約表一列只寫一次腳本名、後面幾列只寫符號：符號住在同目錄別支腳本裡不算漂移
        (self.root / "scripts" / "other.py").write_text("ELSEWHERE_RE = 1\n", encoding="utf-8")
        ok, _ = self.run_check("| x | `check_x.py` ELSEWHERE_RE | y |\n")
        self.assertTrue(ok)

    def test_symbols_without_a_script_on_the_line_are_not_checked(self):
        ok, _ = self.run_check("用 SOME_CONST 當門檻（見下表）\n")
        self.assertTrue(ok)

    def test_ignore_list_and_unknown_script(self):
        ok, _ = self.run_check("`check_x.py` NOT_A_SYMBOL\n`nowhere.py` ALSO_MISSING\n")
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()
