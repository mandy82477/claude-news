"""
test_callout_coverage.py — scripts/check_callout_coverage.py（讀者版日報涵蓋閘）。

看守的形狀：頁面當日吃進新聞（最後新聞更新＝TARGET_DATE），頁頂卻沒有當日日期的 callout
——這頁會從讀者版日報靜默消失。2026-09-13～09-16 實測每天漏 2–7 頁，全無警訊。
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tests._helpers import load_script_module

cov = load_script_module("check_callout_coverage")

DATE = "2026-09-16"


def _page(last_news: str, callouts: str) -> str:
    return (
        "# 某頁\n\n**狀態：** ongoing\n**領域：** 🌐 社群\n"
        f"**最後更新：** {DATE}\n**最後新聞更新：** {last_news}\n\n{callouts}\n\n---\n\n## 摘要\n\n"
        f"> **最新動態**（{DATE}）\n> 分隔線之後的不算頁首。\n"
    )


class TestCoverage(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.wiki = Path(self._td.name)
        (self.wiki / "entities").mkdir()
        (self.wiki / "topics").mkdir()

    def tearDown(self):
        self._td.cleanup()

    def _write(self, slug: str, text: str):
        (self.wiki / f"{slug}.md").write_text(text, encoding="utf-8")

    def test_updated_page_with_todays_callout_passes(self):
        self._write("entities/ok", _page(DATE, f"> **最新動態**（{DATE}）\n> 今天的事。"))
        problems, updated = cov.check(DATE, self.wiki)
        self.assertEqual((problems, updated), ([], 1))

    def test_callout_dated_by_event_day_is_flagged(self):
        self._write("topics/event-dated", _page(DATE, "> **最新工作流模式**（2026-09-15）\n> 寫成了事件日。"))
        problems, _ = cov.check(DATE, self.wiki)
        self.assertEqual(len(problems), 1)
        self.assertIn("topics/event-dated", problems[0])
        self.assertIn("2026-09-15", problems[0])

    def test_stale_callout_left_untouched_is_flagged(self):
        self._write("entities/stale", _page(DATE, "> **最新進展**（2026-09-01）\n> 兩週前的事。"))
        problems, _ = cov.check(DATE, self.wiki)
        self.assertEqual(len(problems), 1)

    def test_intro_only_snapshot_callout_is_flagged(self):
        self._write("topics/intro", _page(DATE, f"> **本頁是什麼**（快照 {DATE}）\n> 自介，不投影。"))
        problems, _ = cov.check(DATE, self.wiki)
        self.assertEqual(len(problems), 1)
        self.assertIn("自介型", problems[0])

    def test_intro_plus_dated_callout_passes(self):
        self._write("topics/both", _page(
            DATE, f"> **本頁是什麼**（快照 {DATE}）\n> 自介。\n\n> **最新動態**（{DATE}）\n> 新增 3 個旗標。"))
        self.assertEqual(cov.check(DATE, self.wiki)[0], [])

    def test_callout_below_divider_does_not_count(self):
        self._write("entities/below", _page(DATE, "（頁首沒有 callout）"))
        self.assertEqual(len(cov.check(DATE, self.wiki)[0]), 1)

    def test_page_not_updated_today_is_ignored(self):
        self._write("entities/quiet", _page("2026-09-10", "> **最新進展**（2026-09-01）\n> 今天沒動。"))
        self.assertEqual(cov.check(DATE, self.wiki), ([], 0))

    def test_exempt_machine_page_is_ignored(self):
        self._write("topics/skill-interest-watch", _page(DATE, f"> **本頁是什麼**（快照 {DATE}）\n> 機器頁。"))
        self.assertEqual(cov.check(DATE, self.wiki), ([], 0))

    def test_page_filter_accepts_path_slug_and_stem(self):
        self._write("entities/a", _page(DATE, "> **最新進展**（2026-09-01）\n> 舊。"))
        self._write("entities/b", _page(DATE, "> **最新進展**（2026-09-01）\n> 舊。"))
        for given in ("wiki/entities/a.md", "entities/a", "a"):
            problems, _ = cov.check(DATE, self.wiki, only={cov._norm(given)})
            self.assertEqual(len(problems), 1, given)
            self.assertIn("entities/a", problems[0])

    def test_main_usage_error_exits_2(self):
        self.assertEqual(cov.main(["x"]), 2)
        self.assertEqual(cov.main(["x", DATE, "--help"]), 2)
        self.assertEqual(cov.main(["x", "09-16"]), 2)


if __name__ == "__main__":
    unittest.main()
