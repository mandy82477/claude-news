"""週報判準欄的讀者語言：查證線索藏進 HTML 註解、新立判準不寫 wiki 頁名（W41 起）。

守的失敗（2026-10-03 冷讀者對抗輪）：第三節「判準」欄的「→ 寫進 ai-agent-safety」與
「｜查證：…」關鍵字清單是全刊最大的內部語言外洩。線索仍是腳本契約，只是讀者看不到。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from tests._helpers import load_script_module

ledger = load_script_module("check_weekly_ledger")
scan = load_script_module("scan_open_forecasts")


def _issue(criterion: str) -> str:
    return (
        "# 週報\n\n## 二、技術討論與深挖\n\n### 本週要動的事\n\n本週沒有需要動的事。\n\n"
        "## 三、下週看什麼\n\n### 下週值得關注：新開 1 條\n\n導言。\n\n"
        "| 類型 | 預告 | 判準 |\n|------|------|------|\n"
        f"| **修復追蹤型** | **外掛漏洞** | {criterion} |\n"
    )


SLUGGED = "若出修補 → 寫入 ai-agent-safety 並改寫自保建議；若兩週無事 → 結案<!-- 查證：Plugin4Shell -->"
CLEAN = "若出修補 → 本刊改寫自保建議；若兩週無事 → 結案<!-- 查證：Plugin4Shell、gemini-cli -->"


class TestDispatchWords(unittest.TestCase):
    def _run(self, stem, criterion):
        with TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / f"{stem}.md").write_text(_issue(criterion), encoding="utf-8")
            report: list[str] = []
            ok = ledger.check_reader_rules(report, weekly_dir=d)
            return ok, "\n".join(report)

    def test_slug_in_new_criterion_is_blocked(self):
        ok, out = self._run("2026-W41", SLUGGED)
        self.assertFalse(ok)
        self.assertIn("ai-agent-safety", out)

    def test_wikilink_in_new_criterion_is_blocked(self):
        ok, out = self._run("2026-W41", "若出修補 → 更新 [[entities/pricing]]；若兩週無事 → 結案<!-- 查證：x -->")
        self.assertFalse(ok)

    def test_slug_inside_probe_comment_is_allowed(self):
        """探針本來就要用日報原文的詞，含連字號的產品名（gemini-cli）合法。"""
        ok, out = self._run("2026-W41", CLEAN)
        self.assertTrue(ok, out)

    def test_frozen_issues_not_retro_checked(self):
        ok, out = self._run("2026-W40", SLUGGED.replace("<!-- 查證：Plugin4Shell -->", "｜查證：Plugin4Shell"))
        self.assertTrue(ok, out)


class TestScanReadsBothForms(unittest.TestCase):
    def test_open_forecasts_reads_comment_and_legacy_forms(self):
        text = _issue(CLEAN) + (
            "\n### 上週的線怎麼了（2026-W40）\n\n導言。\n\n"
            "| 上週預告 | 判準 | 本週結果 |\n|---|---|---|\n"
            "| **舊線** | 若 A → B；若兩週無事 → 結案｜查證：舊詞、old | ⏳ **還要盯** → 續盯至 W42 |\n"
        )
        with TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "2026-W41.md").write_text(text, encoding="utf-8")
            with mock.patch.object(scan, "WEEKLY_DIR", d):
                _, items = scan.open_forecasts()
        probes = {it["forecast"]: it["probes"] for it in items}
        self.assertEqual(probes["外掛漏洞"], ["Plugin4Shell", "gemini-cli"])
        self.assertEqual(probes["舊線"], ["舊詞", "old"])


if __name__ == "__main__":
    unittest.main()
