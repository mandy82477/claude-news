"""Tests for check_weekly_ledger.check_headline() — 只看頭條標題（網站副標的來源）。

寫法規則（日期位置、粗體、句型、角色詞）2026-10-08 起不再機械檢查。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

ledger = load_script_module("check_weekly_ledger")


class TestHeadlineDeck(unittest.TestCase):
    """頭條標題（`## 一、頭條敘事：<一句話>`），W36 起硬擋。

    這條檢查存在的唯一理由是「上一次它是靠沒人注意而死的」：W30–W34 五期都寫了
    這句、渲染層 weeklyHeadlineDeck() 一直支援，但規格從未寫下它——W35 一漏無人
    察覺，還誤把另立「本週一句話」callout 當成修法（2026-09-06 兩者合併）。
    """

    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def _run(self, stem: str, heading: str):
        (self.dir / f"{stem}.md").write_text(
            f"# 本週深挖\n\n{heading}\n\n一段正常的頭條正文。\n\n## 二、技術討論與深挖\n\n內容\n",
            encoding="utf-8",
        )
        report: list[str] = []
        ok = ledger.check_headline(report, weekly_dir=self.dir)
        return ok, "\n".join(report)

    def test_missing_deck_is_blocked(self):
        ok, out = self._run("2026-W36", "## 一、頭條敘事")
        self.assertFalse(ok)
        self.assertIn("缺頭條標題", out)

    def test_deck_present_passes(self):
        ok, out = self._run(
            "2026-W36", "## 一、頭條敘事：讓 Claude Code 讀一個網頁，就可能有人在你電腦上跑程式"
        )
        self.assertTrue(ok)
        self.assertNotIn("缺頭條標題", out)

    def test_overlong_deck_is_blocked(self):
        ok, out = self._run("2026-W36", "## 一、頭條敘事：" + "字" * (ledger.HEADLINE_DECK_MAX + 1))
        self.assertFalse(ok)
        self.assertIn("上限", out)

    def test_pre_w36_issues_are_not_retrofitted(self):
        """W35 以前已凍結——回溯只會產出永遠不修的 ❌，把真訊號淹掉。"""
        ok, out = self._run("2026-W35", "## 一、頭條敘事")
        self.assertNotIn("缺頭條標題", out)

if __name__ == "__main__":
    unittest.main()
