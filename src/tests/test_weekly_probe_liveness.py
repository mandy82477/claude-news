"""Tests for check_weekly_ledger.check_probe_liveness() — 新開預告的探針活性（W39 起生效）。

守的是一個已實際發生的失敗：撰稿者用自己造的詞當探針（W37「週配額、17%、撞上限」），
而日報寫的是另一套詞。那組探針在立案當週就找不到生出它的那則新聞，下期回收於是
把一條實際有 5 則後續的線判成「零命中、續盯」。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

ledger = load_script_module("check_weekly_ledger")

NL = "\n"


def _issue(rows: list[str]) -> str:
    table = NL.join(["| 類型 | 預告 | 判準 |", "|------|------|------|"] + rows)
    return f"# 週報\n\n## 三、下週看什麼\n\n### 下週值得關注：新開 {len(rows)} 條\n\n導言。\n\n{table}\n"


LIVE = "| **修復追蹤型** | **外掛漏洞** | 若出修補 → 結案；若兩週無動作 → 降級｜查證：Plugin4Shell、Copilot |"
DEAD = "| **趨勢確認型** | **配額換軌之後** | 若有實測 → 寫入；若兩週無回報 → 結案｜查證：週配額、weekly limit、17%、撞上限 |"
NEWS = "Max 5x 用戶質疑近期用量縮減幅度不只官方所稱的 25%。另有 Plugin4Shell 零點擊漏洞報導。"


class TestProbeLiveness(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        root = Path(self._tmp.name)
        self.weekly = root / "weekly"
        self.news = root / "news"
        self.weekly.mkdir()
        self.news.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def _run(self, stem: str, rows: list[str], news_date: str | None = "2026-09-23"):
        (self.weekly / f"{stem}.md").write_text(_issue(rows), encoding="utf-8")
        if news_date:
            (self.news / f"{news_date}.md").write_text(NEWS, encoding="utf-8")
        report: list[str] = []
        ok = ledger.check_probe_liveness(report, weekly_dir=self.weekly, news_dir=self.news)
        return ok, NL.join(report)

    def test_dead_probe_set_is_blocked(self):
        """紅燈面：整組探針在當週日報零命中 → 硬擋，且要點名是哪一條、哪些探針。"""
        ok, out = self._run("2026-W39", [LIVE, DEAD])
        self.assertFalse(ok)
        self.assertIn("配額換軌之後", out)
        self.assertIn("週配額", out)
        self.assertNotIn("外掛漏洞", out, "有命中的那條不得被連坐")

    def test_one_live_probe_is_enough(self):
        """一組探針只要有一個命中就放行——要求全中會逼人只寫最寬的詞。"""
        ok, _ = self._run("2026-W39", [LIVE])
        self.assertTrue(ok)

    def test_match_is_case_insensitive(self):
        row = LIVE.replace("Plugin4Shell、Copilot", "plugin4shell")
        ok, _ = self._run("2026-W39", [row])
        self.assertTrue(ok)

    def test_frozen_issues_are_not_retro_checked(self):
        """生效閘：W38 以前已凍結，回溯只會產出永遠不修的 ❌。"""
        ok, out = self._run("2026-W38", [DEAD], news_date="2026-09-16")
        self.assertTrue(ok)
        self.assertNotIn("❌", out)

    def test_missing_news_is_skipped_not_passed_off_as_green(self):
        """找不到當週日報時略過，但要說出來——不得印成「皆有命中」。"""
        ok, out = self._run("2026-W39", [DEAD], news_date=None)
        self.assertTrue(ok)
        self.assertIn("略過", out)
        self.assertNotIn("皆有命中", out)

    def test_window_includes_the_day_before_monday(self):
        """週報常在週日寫、涵蓋上週六起的日報；窗口要含週一的前一天。"""
        ok, _ = self._run("2026-W39", [LIVE], news_date="2026-09-20")  # W39 週一是 09-21
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()
