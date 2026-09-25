# -*- coding: utf-8 -*-
"""週報讀者面三條（W39 起）：頭條不寫深挖的具體物、本週要動的事、第三節以後不放編輯台的帳。

2026-09-25：W36–W38 頭條與深挖同題，頭條都寫進了深挖的指令名與官方連結；冷讀者讀 W38
說可動作的事散在五處要自己撿，並在「初版誤判…同日更正」「109 → 0 逾期待查證」處跳讀。
"""
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))

import build_web  # noqa: E402
import check_weekly_ledger as cwl  # noqa: E402

ACTIONS = """### 本週要動的事

- **有 proxy 的人**：跳過 v2.1.275（見本週版本）
"""

RECAP = """### 上週的線怎麼了（2026-W38）

上週帳上 1 條，已結案。

| 上週預告 | 判準 | 本週結果 |
|---|---|---|
| **某條線** | 若官方說明 → 寫入 wiki 並更新待查證 | {result} |
"""


def _issue(headline="共用設定檔這週出貨，對多工具團隊是好消息。拆開來是什麼，見本期深挖。",
           actions=ACTIONS, result="✅ 官方已說明，不用再盯", numbers="- **4% 對 15%**——救回率，新手對老手"):
    return f"""# CLAUDE NEWS 週報 · 2026-W39

## 一、頭條敘事：Claude Code 開始讀 `AGENTS.md` 了

{headline}

---

## 二、技術討論與深挖

### 本週版本

v2.1.276 修 proxy 錯誤。

### 討論綜述

- 一條討論。

### 深挖：AGENTS.md 什麼時候會被讀

有 `CLAUDE.md` 就不讀 `AGENTS.md`，設定 `claude-md-or-agents-md`（[官方文件](https://code.claude.com/docs/en/memory)）。

{actions}
---

## 三、下週看什麼

{RECAP.format(result=result)}
---

## 四、本週數字

{numbers}

---

**素材涵蓋窗**：本期取材自 09-20 ~ 09-26 的每日新聞。
"""


class ReaderRules(unittest.TestCase):
    def _run(self, text, stem="2026-W39"):
        d = Path(tempfile.mkdtemp())
        (d / f"{stem}.md").write_text(text, encoding="utf-8")
        report: list[str] = []
        return cwl.check_reader_rules(report, weekly_dir=d), report

    def test_合格的一期通過(self):
        ok, report = self._run(_issue())
        self.assertTrue(ok, report)

    def test_頭條寫進深挖的設定名被擋(self):
        ok, report = self._run(_issue(headline="預設值 `claude-md-or-agents-md` 代表二選一。"))
        self.assertFalse(ok)
        self.assertIn("claude-md-or-agents-md", report[0])

    def test_頭條引用深挖的官方連結被擋(self):
        ok, _ = self._run(_issue(headline="官方寫明預設規則（[官方文件](https://code.claude.com/docs/en/memory)）。"))
        self.assertFalse(ok)

    def test_頭條標題裡的詞不算越界(self):
        ok, report = self._run(_issue(headline="`AGENTS.md` 出貨了，見本期深挖。"))
        self.assertTrue(ok, report)

    def test_缺本週要動的事被擋(self):
        ok, report = self._run(_issue(actions=""))
        self.assertFalse(ok)
        self.assertTrue(any("本週要動的事" in r for r in report))

    def test_沒事可動寫一行即合格(self):
        ok, report = self._run(_issue(actions="### 本週要動的事\n\n本週沒有需要動的事。\n"))
        self.assertTrue(ok, report)

    def test_回收結果欄寫製作過程被擋(self):
        ok, report = self._run(_issue(result="✅ 本列初版誤判，同日更正"))
        self.assertFalse(ok)
        self.assertIn("初版", report[0])

    def test_判準欄是凍結契約不查(self):
        """RECAP 的判準欄含「待查證」，合格那期仍通過。"""
        ok, report = self._run(_issue())
        self.assertTrue(ok, report)

    def test_本週數字放編輯台指標被擋(self):
        ok, _ = self._run(_issue(numbers="- **109 → 0**——本刊 wiki 逾期待查證的條目數"))
        self.assertFalse(ok)

    def test_舊期不回溯(self):
        ok, report = self._run(_issue(actions=""), stem="2026-W38")
        self.assertTrue(ok, report)


class BuildWebActions(unittest.TestCase):
    def test_本週要動的事進_discussion_actions(self):
        p = Path(tempfile.mkdtemp()) / "2026-W39.md"
        p.write_text(_issue(), encoding="utf-8")
        disc = build_web.parse_weekly(p)["sections"]["discussion"]
        self.assertIn("跳過 v2.1.275", disc["actions"])
        self.assertNotIn("本週要動的事", disc["deepDive"]["body"])


if __name__ == "__main__":
    unittest.main()
