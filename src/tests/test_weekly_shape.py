# -*- coding: utf-8 -*-
"""週報篇幅形狀（W41 起）：官方段必有；官方 6／綜述 4／要動的事 4 條上限；回收結果欄 80 字。

2026-10-11：W41 第一版把當週 8 項功能更新只寫進 2 項，討論綜述卻有 8 條——四段裡沒有一段
的題目是「官方出了什麼」，其餘各段只有下限沒有上限。舊期（W40 以前）凍結不回溯。
"""
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))

import build_web  # noqa: E402
import check_weekly_ledger as cwl  # noqa: E402


def _issue(week="2026-W41", official="### 本週官方出了什麼\n\n- **新模型**：所有方案可用。\n\n升版：可升。\n",
           roundup=1, actions=1, result="⏳ **還要盯** → 續盯至 W42。官方仍未回覆"):
    bullets = lambda n, word: "".join(f"- **{word} {i}**：一句。\n" for i in range(n))
    return f"""# CLAUDE NEWS 週報 · {week}

## 一、頭條敘事：一句話

正文。

---

## 二、技術討論與深挖

{official}
### 討論綜述

{bullets(roundup, "討論")}
### 深挖：一題

#### 開發實務｜標題

內文。

### 本週要動的事

{bullets(actions, "誰")}
---

## 三、下週看什麼

### 上週的線怎麼了（2026-W40）

上週 1 條。

| 上週預告 | 判準 | 本週結果 |
|---|---|---|
| **某條線** | 若官方回覆 → 補上說明<!-- 查證：某線 --> | {result} |

---

## 四、本週數字

- **1**——一個數字
- **2**——兩個數字
"""


class TestShape(unittest.TestCase):
    def run_check(self, text, name="2026-W41.md"):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / name).write_text(text, encoding="utf-8")
            report = []
            return cwl.check_shape(report, Path(d)), "\n".join(report)

    def test_within_limits_passes(self):
        ok, rep = self.run_check(_issue(roundup=4, actions=4))
        self.assertTrue(ok, rep)

    def test_missing_official_section_fails(self):
        ok, rep = self.run_check(_issue(official="### 本週版本\n\n可升。\n"))
        self.assertFalse(ok)
        self.assertIn("本週官方出了什麼", rep)

    def test_roundup_over_cap_fails(self):
        ok, rep = self.run_check(_issue(roundup=5))
        self.assertFalse(ok)
        self.assertIn("討論綜述", rep)

    def test_actions_over_cap_fails(self):
        ok, rep = self.run_check(_issue(actions=5))
        self.assertFalse(ok)
        self.assertIn("本週要動的事", rep)

    def test_official_over_cap_fails(self):
        many = "### 本週官方出了什麼\n\n" + "".join(f"- **功能 {i}**：一句。\n" for i in range(7)) + "\n升版：可升。\n"
        ok, rep = self.run_check(_issue(official=many))
        self.assertFalse(ok)

    def test_long_recap_result_fails_and_links_do_not_count(self):
        ok, _ = self.run_check(_issue(result="⏳ **還要盯** → 續盯至 W42。" + "查了很多關鍵字都沒有命中" * 8))
        self.assertFalse(ok)
        linked = "⏳ **還要盯** → 續盯至 W42。見[官方](https://example.com/" + "x" * 200 + ")"
        ok, rep = self.run_check(_issue(result=linked))
        self.assertTrue(ok, rep)

    def test_frozen_issues_not_checked(self):
        """W40 以前用 `### 本週版本`、沒有上限，凍結不回溯。"""
        ok, rep = self.run_check(_issue(week="2026-W40", official="### 本週版本\n\n可升。\n", roundup=8, actions=7),
                                 name="2026-W40.md")
        self.assertTrue(ok, rep)

    def test_build_web_parses_official_and_keeps_old_version_note(self):
        with tempfile.TemporaryDirectory() as d:
            new = Path(d) / "2026-W41.md"
            new.write_text(_issue(), encoding="utf-8")
            old = Path(d) / "2026-W40.md"
            old.write_text(_issue(week="2026-W40", official="### 本週版本\n\n舊期可升。\n"), encoding="utf-8")
            dn = build_web.parse_weekly(new)["sections"]["discussion"]
            do = build_web.parse_weekly(old)["sections"]["discussion"]
        self.assertIn("新模型", dn["official"])
        self.assertIsNone(dn["versionNote"])
        self.assertIn("舊期可升", do["versionNote"])
        self.assertIsNone(do["official"])
        self.assertIn("討論 0", dn["roundup"])


if __name__ == "__main__":
    unittest.main()
