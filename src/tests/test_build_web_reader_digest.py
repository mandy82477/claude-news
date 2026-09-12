"""讀者版日報（daily/YYYY-MM-DD.md）解析契約測試。

2026-09-12 日報改版「乙」：讀者版回答「今天 wiki 學到什麼」，來源是當日 ingest
對 wiki/ 的 diff。規格端住 `.claude/skills/reader-digest/format.md` 的
`Step 2b：讀者版日報`「機械契約字串」表；本檔鎖住三種情況：

1. 完整六領域 —— 節名順序、每條三段（事實／wikilink／判斷句）都解得出來
2. 部分領域省略 —— 沒有內容的領域整節不寫，解析端不得長出空殼節
3. 無新知 —— `> 今日 wiki 無新知（YYYY-MM-DD）` 時 noNews=True 且無任何節

另鎖住 attach_reader_digests 的兩條行為：有讀者版的日期掛 reader 欄並改寫
preview；沒有讀者版的日期（改版日之前）一字不動——歷史頁不可壞。

乙-2（2026-09-12 同日）：讀者版日期的今日聚焦與重點話題仍上站，搜尋索引要跟著收
（reader_search_text 帶 d 時併入 focus 文字與前 5 則重點話題標題，其餘新聞區塊不收）。
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

build_web = load_script_module("build_web")


FULL = """# 2026-09-12 今天 wiki 學到什麼

> 今天最重要的一句總結。

## 🛠️ 功能

- 功能事實一 → [[entities/claude-code]] → 功能判斷一。
- 功能事實二 → [[topics/coding-workflow-guide]] → 功能判斷二。

## 🤖 模型

- 模型事實 → [[entities/opus-5]] → 模型判斷。

## 💼 商業

- 商業事實 → [[entities/pricing]] → 商業判斷。

## 🏛️ 安全政策

- 安全事實 → [[topics/ai-agent-safety]] → 安全判斷。

## 🌐 社群

- 社群事實 → [[topics/community-tech-patterns]] → 社群判斷。

## 👤 人物

- 人物事實 → [[entities/dario-amodei]] → 人物判斷。
"""

PARTIAL = """# 2026-09-13 今天 wiki 學到什麼

> 只有兩個領域有東西。

## 🛠️ 功能

- 功能事實 → [[entities/claude-code]] → 功能判斷。

## 🌐 社群

- 社群事實 → [[topics/community-tech-patterns]] → 社群判斷。
"""

NO_NEWS = """# 2026-09-14 今天 wiki 學到什麼

> 今日 wiki 無新知（2026-09-14）
"""


def _parse(text: str, date: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / f"{date}.md"
        f.write_text(text, encoding="utf-8")
        return build_web.parse_reader_digest(f)


class TestFullSixDomains(unittest.TestCase):
    def setUp(self):
        self.r = _parse(FULL, "2026-09-12")

    def test_summary_and_flags(self):
        self.assertEqual(self.r["date"], "2026-09-12")
        self.assertEqual(self.r["summary"], "今天最重要的一句總結。")
        self.assertFalse(self.r["noNews"])

    def test_all_six_domains_in_spec_order(self):
        self.assertEqual(
            [s["key"] for s in self.r["sections"]],
            ["features", "models", "commercial", "safetyPolicy", "community", "people"],
        )

    def test_item_count(self):
        self.assertEqual(self.r["itemCount"], 7)

    def test_three_segments_per_item(self):
        it = self.r["sections"][0]["items"][0]
        self.assertEqual(it["fact"], "功能事實一")
        self.assertEqual(it["link"], "entities/claude-code")
        self.assertEqual(it["judgment"], "功能判斷一。")

    def test_section_labels_carry_domain_emoji(self):
        # 領域 emoji 是資料值（與 wiki 標頭「領域」欄同源），不是 UI 圖示——
        # 節名整串進 label，前端原樣顯示。
        self.assertEqual(self.r["sections"][1]["label"], "🤖 模型")


class TestPartialDomains(unittest.TestCase):
    def setUp(self):
        self.r = _parse(PARTIAL, "2026-09-13")

    def test_only_written_domains_appear(self):
        self.assertEqual([s["key"] for s in self.r["sections"]], ["features", "community"])

    def test_no_empty_section_shells(self):
        for sec in self.r["sections"]:
            self.assertTrue(sec["items"])

    def test_item_count(self):
        self.assertEqual(self.r["itemCount"], 2)


class TestNoNews(unittest.TestCase):
    def setUp(self):
        self.r = _parse(NO_NEWS, "2026-09-14")

    def test_flagged_and_empty(self):
        self.assertTrue(self.r["noNews"])
        self.assertEqual(self.r["sections"], [])
        self.assertEqual(self.r["itemCount"], 0)

    def test_summary_is_the_no_news_line(self):
        self.assertEqual(self.r["summary"], "今日 wiki 無新知（2026-09-14）")


class TestMalformedItemsAreDropped(unittest.TestCase):
    """少一段箭頭＝「改變了什麼判斷」沒寫，那條就不該上站——那正是過濾。"""

    def test_two_segment_item_not_collected(self):
        r = _parse(
            "# 2026-09-15 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
            "- 只有事實跟連結 → [[entities/claude-code]]\n"
            "- 完整的一條 → [[entities/claude-code]] → 判斷句。\n",
            "2026-09-15",
        )
        self.assertEqual(r["itemCount"], 1)
        self.assertEqual(r["sections"][0]["items"][0]["fact"], "完整的一條")

    def test_unknown_section_items_not_swallowed_by_previous_domain(self):
        r = _parse(
            "# 2026-09-16 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
            "- 功能事實 → [[entities/claude-code]] → 功能判斷。\n\n"
            "## 不是領域的節\n\n- 雜項 → [[entities/pricing]] → 不該被收。\n",
            "2026-09-16",
        )
        self.assertEqual(r["itemCount"], 1)


class TestAttachReaderDigests(unittest.TestCase):
    def test_reader_date_gets_reader_and_preview(self):
        digest_all = {"2026-09-12": build_web.empty_digest("2026-09-12")}
        digest_all["2026-09-12"]["preview"] = "舊的新聞式 preview"
        reader_all = {"2026-09-12": _parse(FULL, "2026-09-12")}
        build_web.attach_reader_digests(digest_all, reader_all)
        d = digest_all["2026-09-12"]
        self.assertIn("reader", d)
        self.assertEqual(d["preview"], "今天最重要的一句總結。")

    def test_legacy_date_untouched(self):
        """改版日之前的日期沒有 daily/ 檔，digest 一字不動——歷史頁不可壞。"""
        legacy = build_web.empty_digest("2026-08-01")
        legacy["preview"] = "舊日報的 preview"
        digest_all = {"2026-08-01": legacy}
        build_web.attach_reader_digests(digest_all, {"2026-09-12": _parse(FULL, "2026-09-12")})
        self.assertNotIn("reader", digest_all["2026-08-01"])
        self.assertEqual(digest_all["2026-08-01"]["preview"], "舊日報的 preview")

    def test_reader_without_raw_material_creates_bare_digest(self):
        digest_all: dict = {}
        build_web.attach_reader_digests(digest_all, {"2026-09-12": _parse(FULL, "2026-09-12")})
        self.assertIn("2026-09-12", digest_all)
        self.assertEqual(digest_all["2026-09-12"]["articleCount"], 0)
        self.assertEqual(digest_all["2026-09-12"]["sourceStatus"], [])


class TestReaderDigestChecker(unittest.TestCase):
    """scripts/check_reader_digest.py 是 Step 2b 第 4 步的格式閘——它抓不到的
    違規，會以「該領域整段在網站上消失」的形式靜默發生。"""

    def setUp(self):
        self.chk = load_script_module("check_reader_digest")
        self.valid = {"entities/claude-code", "claude-code",
                      "topics/community-tech-patterns", "community-tech-patterns"}

    def _check(self, text, name="2026-09-12"):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / f"{name}.md"
            f.write_text(text, encoding="utf-8")
            return self.chk.check_file(f, self.valid)

    def test_good_file_passes(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 事實 → [[entities/claude-code]] → 判斷。\n")
        self.assertEqual(self._check(text), [])

    def test_no_news_file_passes(self):
        text = "# 2026-09-12 今天 wiki 學到什麼\n\n> 今日 wiki 無新知（2026-09-12）\n"
        self.assertEqual(self._check(text), [])

    def test_bad_domain_label_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠 功能\n\n"
                "- 事實 → [[entities/claude-code]] → 判斷。\n")
        self.assertTrue(any("不在六個領域內" in p for p in self._check(text)))

    def test_two_segment_item_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 事實 → [[entities/claude-code]]\n")
        self.assertTrue(any("三段式" in p for p in self._check(text)))

    def test_dead_wikilink_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 事實 → [[entities/does-not-exist]] → 判斷。\n")
        self.assertTrue(any("不存在的 wiki 頁" in p for p in self._check(text)))

    def test_overlong_item_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- " + "長" * 210 + " → [[entities/claude-code]] → 判斷。\n")
        self.assertTrue(any("超過上限" in p for p in self._check(text)))

    def test_housekeeping_fact_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 投資判讀頁拆成兩頁，教材獨立成新頁 → [[entities/claude-code]] → 判斷。\n")
        self.assertTrue(any("事實句含整理語" in p for p in self._check(text)))

    def test_housekeeping_summary_flagged(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 社群模式概覽表首度汰掉五類。\n\n## 🛠️ 功能\n\n"
                "- 事實 → [[entities/claude-code]] → 判斷。\n")
        self.assertTrue(any("總結句含整理語" in p for p in self._check(text)))

    def test_housekeeping_word_in_judgment_is_allowed(self):
        text = ("# 2026-09-12 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 官方發布 X → [[entities/claude-code]] → 本庫判斷這改變了選型。\n")
        self.assertEqual(self._check(text), [])

    def test_title_date_mismatch_flagged(self):
        text = ("# 2026-01-01 今天 wiki 學到什麼\n\n> 總結。\n\n## 🛠️ 功能\n\n"
                "- 事實 → [[entities/claude-code]] → 判斷。\n")
        self.assertTrue(any("與檔名" in p for p in self._check(text)))


if __name__ == "__main__":
    unittest.main()


class TestReaderSearchTextKeepsFocusAndHeadlines(unittest.TestCase):
    """乙-2：讀者版日期仍上站的聚焦與重點話題要能被搜到；不上站的媒體區不索引。"""

    def setUp(self):
        self.r = _parse(PARTIAL, "2026-09-13")
        self.d = {
            "focus": [{"tag": "[重大事件]", "text": "聚焦句甲"}],
            "topStories": [{"title": f"重點 {i}"} for i in range(7)],
            "mediaReports": [{"title": "媒體覆述不該被索引"}],
        }

    def test_without_raw_digest_only_reader_text(self):
        txt = build_web.reader_search_text(self.r)
        self.assertIn("功能事實", txt)
        self.assertNotIn("聚焦句甲", txt)

    def test_focus_and_top_five_headlines_indexed(self):
        txt = build_web.reader_search_text(self.r, self.d)
        self.assertIn("聚焦句甲", txt)
        self.assertIn("重點 4", txt)
        self.assertNotIn("重點 5", txt, "重點話題只上站前 5 則，第 6 則不索引")
        self.assertNotIn("媒體覆述", txt)
