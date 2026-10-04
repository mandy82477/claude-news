"""Tests for scripts/check_digest_layout.py — 日報跨區塊重述與版式閘。

守的失敗（2026-10-03 冷讀者對抗輪）：10-02 聚焦句與技術更新說明句幾乎逐字相同
（Mods 同檔五處）；常設區塊時有時無；💬 一天 8 則、隔天 19 則；標頭與來源表兩個口徑。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

lay = load_script_module("check_digest_layout")

HEADER = "**日期：** {d} | **來源：** 2/2 | **文章數：** {n} | **更新時間：** x\n\n---\n"


def story(title, desc):
    return f"**[{title}](https://e.example/{abs(hash(title))})**\n{desc}\n`HN` · 10/02 13:38 UTC\n"


def digest(date="2026-10-06", n=2, focus=None, sections=None, table5=True, total=None):
    focus = focus or ["- **[重大事件]** Claude Code 新版推出外掛機制，可修改深層行為。（[官方](https://o.example)）"]
    sections = sections if sections is not None else {
        "⭐ 重點話題": [story("A", "追蹤串累積 233 則留言。")],
        "🔧 技術更新": [story("B", "同版新增 10 頁文件。")],
        "💰 付費方案動態": ["> 本日無定價或配額異動。\n"],
        "📰 媒體報導": ["> 本日無媒體報導。\n"],
        "💬 技術熱度討論": ["> 本日無社群討論。\n"],
    }
    out = ["# t\n", HEADER.format(d=date, n=n), "### 📌 今日聚焦\n", "\n".join(focus) + "\n"]
    for name, parts in sections.items():
        out.append(f"### {name}\n")
        out += parts
    out.append("### 📡 來源狀態\n")
    if table5:
        t = total if total is not None else n
        out.append(f"| 來源 | 狀態 | 抓到 | 進候選 | 刊出 |\n|---|---|---|---|---|\n| HN | ✅ | 9 | {t} | 2 |\n")
    else:
        out.append("| 來源 | 狀態 | 條數 |\n|---|---|---|\n| HN | ✅ | 9 |\n")
    return "\n".join(out)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def run_on(self, text, date="2026-10-06"):
        (self.dir / f"{date}.md").write_text(text, encoding="utf-8")
        return lay.run(date, self.dir)


class TestDuplicates(Base):
    def test_clean_digest_passes(self):
        code, errs = self.run_on(digest())
        self.assertEqual(code, 0, errs)

    def test_the_10_02_pair_is_caught(self):
        """實例：聚焦句與 🔧 說明句只差「現在」與一個分號。"""
        f = ["- **[重大事件]** Claude Code v2.1.287 正式發布，推出「Mods」功能，外掛可修改更深層的行為，"
             "並內建旁觀 agent「You should know」。（[官方](https://o.example)）"]
        s = {"🔧 技術更新": [story("v2.1.287", "本次更新新增「Claude Mods」：外掛現在可修改更深層的行為；"
                                         "並內建名為「You should know」的 mod。")]}
        code, errs = self.run_on(digest(date="2026-10-02", focus=f, sections=s), "2026-10-02")
        self.assertEqual(code, 1)
        self.assertIn("跨區塊重述", errs[0])

    def test_boilerplate_counts_do_not_trip(self):
        """「累積 N 則留言、M 個反應」只有 8 個漢字共同，不算重述。"""
        s = {
            "⭐ 重點話題": [story("A", "某功能請求累積 120 則留言、30 個反應。")],
            "💬 技術熱度討論": [story("B", "另一個錯誤回報累積 80 則留言、12 個反應。")],
            "🔧 技術更新": ["> 本日無官方發布。\n"], "💰 付費方案動態": ["> 本日無。\n"],
            "📰 媒體報導": ["> 本日無。\n"],
        }
        code, errs = self.run_on(digest(sections=s))
        self.assertEqual(code, 0, errs)

    def test_same_block_entries_are_not_compared(self):
        long = "這是一段相當長而且完全一樣的中文說明句子用來測試"
        s = {"⭐ 重點話題": [story("A", long), story("B", long)],
             "🔧 技術更新": ["> 無。\n"], "💰 付費方案動態": ["> 無。\n"],
             "📰 媒體報導": ["> 無。\n"], "💬 技術熱度討論": ["> 無。\n"]}
        code, errs = self.run_on(digest(sections=s))
        self.assertEqual(code, 0, errs)


class TestLayout(Base):
    def test_missing_standing_section_fails(self):
        s = {"⭐ 重點話題": [story("A", "x")]}
        code, errs = self.run_on(digest(sections=s))
        self.assertEqual(code, 1)
        self.assertTrue(any("常設區塊 🔧" in e for e in errs))

    def test_empty_section_without_note_fails(self):
        s = {"⭐ 重點話題": [story("A", "x")], "🔧 技術更新": [], "💰 付費方案動態": ["> 無。\n"],
             "📰 媒體報導": ["> 無。\n"], "💬 技術熱度討論": ["> 無。\n"]}
        code, errs = self.run_on(digest(sections=s))
        self.assertTrue(any("🔧 是空的" in e for e in errs))

    def test_over_cap_fails(self):
        many = [story(f"T{i}", f"第{i}則") for i in range(lay.CAPS["💬"] + 1)]
        s = {"⭐ 重點話題": ["> 無。\n"], "🔧 技術更新": ["> 無。\n"], "💰 付費方案動態": ["> 無。\n"],
             "📰 媒體報導": ["> 無。\n"], "💬 技術熱度討論": many}
        code, errs = self.run_on(digest(sections=s))
        self.assertTrue(any("💬 有" in e for e in errs))

    def test_header_vs_table_caliber(self):
        code, errs = self.run_on(digest(n=59, total=99))
        self.assertTrue(any("≠" in e for e in errs))

    def test_old_three_column_table_fails_after_since(self):
        code, errs = self.run_on(digest(table5=False))
        self.assertTrue(any("舊三欄" in e for e in errs))

    def test_layout_rules_not_retroactive(self):
        s = {"⭐ 重點話題": [story("A", "x")]}
        code, errs = self.run_on(digest(date="2026-10-01", sections=s, table5=False), "2026-10-01")
        self.assertEqual(code, 0, errs)


if __name__ == "__main__":
    unittest.main()
