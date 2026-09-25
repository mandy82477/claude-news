# -*- coding: utf-8 -*-
"""scripts/check_focus.py：同一故事不得換家媒體再當一次頭條（2026-09-25）。

事故：09-15～09-24 三十條聚焦裡 9 條是前幾天登過的故事——Suleyman 批評 09-16、09-17
連兩天、Chat 與 Cowork 合併 09-17 登完 09-21 由 extremetech 覆述再登。
"""
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))

import check_focus  # noqa: E402


def _digest(*bullets: str) -> str:
    return "# 摘要\n\n### 📌 今日聚焦\n\n" + "\n".join(bullets) + "\n\n### ⭐ 重點話題\n\n內文\n"


class Synthetic(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        filler = [f"- **[重大事件]** 第{i}則無關事件：編號{i}號的合作案{i}{i}。（[官方](https://e.com/{i})）"
                  for i in range(8)]
        (self.dir / "2026-09-16.md").write_text(_digest(
            "- **[重大事件]** 微軟 AI 執行長 Mustafa Suleyman 批評 Anthropic 類人化論述恐帶來災難性影響。（[BBC](https://b.com/1)）",
            *filler[:4]), encoding="utf-8")
        (self.dir / "2026-09-15.md").write_text(_digest(*filler[4:]), encoding="utf-8")

    def _check(self, *bullets):
        (self.dir / "2026-09-17.md").write_text(_digest(*bullets), encoding="utf-8")
        return check_focus.check("2026-09-17", news_dir=self.dir)

    def test_換家媒體重登被擋(self):
        p = self._check("- **[重大事件]** Suleyman 再度警告 Anthropic 類人化論述會有災難性影響。（[Reuters](https://r.com/2)）")
        self.assertEqual(len(p), 1)
        self.assertIn("2026-09-16", p[0])

    def test_標續報就放行(self):
        p = self._check("- **[持續追蹤]** （續 09-16）Suleyman 再度警告 Anthropic 類人化論述會有災難性影響，微軟董事會跟進表態。（[Reuters](https://r.com/2)）")
        self.assertEqual(p, [])

    def test_續報標記與標籤要一致(self):
        self.assertEqual(len(self._check("- **[重大事件]** （續 09-16）無關的新消息。")), 1)
        self.assertEqual(len(self._check("- **[持續追蹤]** 沒寫接續哪天的新消息。")), 1)

    def test_HN_標籤要連到_HN(self):
        p = self._check("- **[重大事件]** 無關新聞甲乙丙。（[HN](https://code.claude.com/docs/en/changelog)）")
        self.assertEqual(len(p), 1)
        self.assertEqual(self._check("- **[重大事件]** 無關新聞甲乙丙。（[HN](https://news.ycombinator.com/item?id=1)）"), [])

    def test_無關新聞通過(self):
        self.assertEqual(self._check("- **[新工具]** 全新的 IDE 外掛上架，支援多檔重構。（[官方](https://e.com/x)）"), [])


class RealDigests(unittest.TestCase):
    """用 news/ 實檔回放：抓得到的事故要抓，乾淨的一天不能誤報。"""

    def _problems(self, date):
        return check_focus.check(date)

    def test_0917_Suleyman_重登(self):
        self.assertTrue(any("2026-09-16" in p for p in self._problems("2026-09-17")))

    def test_0921_Cowork_合併重登(self):
        self.assertTrue(any("2026-09-17" in p for p in self._problems("2026-09-21")))

    def test_0918_乾淨(self):
        self.assertEqual(self._problems("2026-09-18"), [])


if __name__ == "__main__":
    unittest.main()
