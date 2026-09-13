"""讀者版日報（daily/YYYY-MM-DD.md）契約測試：產生器 → 解析端 → 格式閘 三端同形。

2026-09-12 改版「乙」：讀者版回答「今天 wiki 學到什麼」，六領域分節。
2026-09-13 改版「丙」：讀者版由 scripts/build_reader_digest.py 從各頁頂部當日 callout 產出
（一頁一條：`### [[頁名|頁面標題]]` ＋ callout 原文），不再由 LLM 讀 wiki diff 重寫三段式。
規格端住 `.claude/skills/reader-digest/references/format.md` 的「機械契約字串」表；本檔鎖住：

1. 產生器：只收括號日期＝TARGET_DATE 的頁頂 callout、標籤與內容原樣、按 frontmatter domain 分六節、
   無 domain 的頁 WARN 不收、零命中寫無新知行、`（` 後不緊接日期的（如 ❓ 待查證）不當 callout
2. 解析端：節名順序、一頁一 item（page／name／label／date／body）、部分領域省略不長空殼、
   不認得的節名其下頁面不收、無新知 noNews=True
3. attach_reader_digests：有讀者版的日期掛 reader 欄並改寫 preview；沒有的日期一字不動
4. 搜尋文字：讀者版正文＋仍上站的聚焦與前 5 則重點話題標題（乙-2），其餘新聞區塊不收
5. 格式閘 check_reader_digest.py：節名、頁面小節位置、wikilink 存在、callout 首行日期
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

build_web = load_script_module("build_web")
gen = load_script_module("build_reader_digest")


def _page(domain: str, name: str, callouts: str, inbound: int = 0) -> str:
    return (
        "---\n"
        f'page: "x"\ndomain: "{domain}"\ninbound_links: {inbound}\n'
        "---\n"
        f"# {name}\n\n**類型：** product\n**領域：** {domain}\n\n{callouts}\n---\n\n## 摘要\n\n"
        "> **最新動態**（2020-01-01）\n> 分隔線之後的 callout 不在頁首，不該被收。\n"
    )


def _wiki(tmp: Path) -> Path:
    (tmp / "entities").mkdir()
    (tmp / "topics").mkdir()
    (tmp / "entities" / "claude-code.md").write_text(_page(
        "🛠️ 工具/功能", "Claude Code",
        "> **最新動態**（2026-09-11）\n> - **v2.1.268**：gateway 新增 `pricing:` 設定，見 [[entities/pricing]]。\n> - **服務事故**：錯誤率升高。",
        inbound=88), encoding="utf-8")
    (tmp / "entities" / "managed-agents.md").write_text(_page(
        "🛠️ 工具/功能", "Managed Agents",
        "> **最新動態**（2026-09-11）\n> SDK v1.5.0 加 auto mode。", inbound=10), encoding="utf-8")
    (tmp / "entities" / "old-page.md").write_text(_page(
        "🤖 模型", "舊頁", "> **最新進展**（2026-09-01）\n> 不是今天。"), encoding="utf-8")
    (tmp / "entities" / "pending-only.md").write_text(_page(
        "👤 人物", "只有懸置標記的人",
        "> ❓ **待查證**（標 2026-09-11｜查 X）｜**辭職**（2026-09-11 報導）：括號後不是日期，不算 callout。"),
        encoding="utf-8")
    (tmp / "topics" / "market-signals.md").write_text(_page(
        "💼 商業", "投資訊號判讀",
        "> ⚠️ **教學型事件研究，非投資建議**\n> 免責。\n\n> **最新判讀**（2026-09-11）\n> ⚖️ 兩面：同一頁的第二個 callout。"),
        encoding="utf-8")
    (tmp / "topics" / "no-domain.md").write_text(
        "---\npage: \"x\"\n---\n# 沒有領域的頁\n\n> **本頁是什麼**（2026-09-11 快照）\n> 沒 domain。\n\n---\n",
        encoding="utf-8")
    (tmp / "topics" / "header-domain-only.md").write_text(
        "# 只有標頭領域的頁\n\n**狀態：** ongoing\n**領域：** 🤖 模型\n\n"
        "> **最新進展**（2026-09-11）\n> 沒 frontmatter 也要收。\n\n---\n",
        encoding="utf-8")
    (tmp / "topics" / "internal-ref.md").write_text(_page(
        "🌐 社群", "帶頁內路標的頁",
        "> **最新動態**（2026-09-11）\n> - **⟨G-11⟩ 再添兩款**：詳見下方使用現況表，另見「## 攻防紀錄」與 [[#技術彙整]]。"),
        encoding="utf-8")
    (tmp / "topics" / "tail-in-label.md").write_text(_page(
        "🌐 社群", "尾巴頁",
        "> **本週趨勢觀察**（2026-09-11，補充說明）同行尾巴文字\n> 第二行。"), encoding="utf-8")
    return tmp


def _parse(text: str, date: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / f"{date}.md"
        f.write_text(text, encoding="utf-8")
        return build_web.parse_reader_digest(f)


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.wiki = _wiki(Path(self._td.name))
        self.text, self.count, self.warnings = gen.generate("2026-09-11", self.wiki)
        self.r = _parse(self.text, "2026-09-11")

    def tearDown(self):
        self._td.cleanup()

    def test_only_target_date_callouts_collected(self):
        pages = [it["page"] for sec in self.r["sections"] for it in sec["items"]]
        self.assertEqual(pages, ["entities/claude-code", "entities/managed-agents",
                                 "topics/header-domain-only",
                                 "topics/market-signals", "topics/internal-ref", "topics/tail-in-label"])
        self.assertEqual(self.count, 6)

    def test_page_internal_references_are_warned_but_still_collected(self):
        hits = [w for w in self.warnings if "topics/internal-ref" in w and "頁內路標" in w]
        self.assertTrue(hits, self.warnings)
        self.assertIn("⟨G-11⟩", hits[0])
        clean = [w for w in self.warnings if "topics/tail-in-label" in w and "頁內路標" in w]
        self.assertFalse(clean)
        for bad in ("詳見下方使用現況表", "見「## 攻防紀錄」", "[[#技術彙整]]", "見『## 節』", "參見上方",
                    "（見『IPO 走到哪一格』細節區）", "課程表『押對了嗎』欄才會有值"):
            self.assertTrue(gen.PAGE_INTERNAL_RE.search(bad), bad)
        for ok in ("見 [[topics/x#攻防紀錄]]", "累計 7 款", "下方", "Musk 稱相關警告為「psyop」", "「蒸餾」手法"):
            self.assertFalse(gen.PAGE_INTERNAL_RE.search(ok), ok)

    def test_sections_in_spec_order_and_no_empty_shells(self):
        self.assertEqual([s["key"] for s in self.r["sections"]], ["features", "models", "commercial", "community"])
        self.assertEqual(len(self.r["sections"][3]["items"]), 2)
        for sec in self.r["sections"]:
            self.assertTrue(sec["items"])

    def test_callout_copied_verbatim_with_label_and_date(self):
        it = self.r["sections"][0]["items"][0]
        self.assertEqual(it["name"], "Claude Code")
        self.assertEqual(it["label"], "最新動態")
        self.assertEqual(it["date"], "2026-09-11")
        self.assertIn("- **v2.1.268**：gateway 新增 `pricing:` 設定，見 [[entities/pricing]]。", it["body"])
        self.assertIn("- **服務事故**：錯誤率升高。", it["body"])
        self.assertNotIn("最新動態", it["body"], "首行標籤拆進 label，不重複進 body")

    def test_inbound_links_orders_pages_within_section(self):
        self.assertEqual([it["name"] for it in self.r["sections"][0]["items"]],
                         ["Claude Code", "Managed Agents"])

    def test_second_callout_on_same_page_kept_only_if_dated_today(self):
        it = self.r["sections"][2]["items"][0]
        self.assertEqual(it["label"], "最新判讀")
        self.assertNotIn("免責", it["body"], "沒有日期的 ⚠️ 免責 callout 不算最新動態")

    def test_label_tail_and_same_line_text_survive(self):
        it = self.r["sections"][3]["items"][1]
        self.assertEqual(it["label"], "本週趨勢觀察")
        self.assertEqual(it["date"], "2026-09-11")
        self.assertTrue(it["body"].startswith("同行尾巴文字"))
        self.assertIn("第二行。", it["body"])

    def test_pending_marker_is_not_a_callout(self):
        self.assertNotIn("pending-only", self.text)

    def test_page_without_domain_is_warned_not_silently_dropped(self):
        self.assertNotIn("no-domain", self.text)
        self.assertTrue(any("topics/no-domain" in w and "domain" in w for w in self.warnings))

    def test_no_hit_day_writes_no_news_line(self):
        text, count, _ = gen.generate("2026-09-10", self.wiki)
        self.assertEqual(count, 0)
        self.assertIn("> 今日 wiki 無新知（2026-09-10）", text)
        self.assertTrue(_parse(text, "2026-09-10")["noNews"])

    def test_generated_file_passes_checker(self):
        chk = load_script_module("check_reader_digest")
        valid = {"entities/claude-code", "entities/managed-agents", "topics/market-signals",
                 "topics/tail-in-label", "topics/header-domain-only", "topics/internal-ref"}
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "2026-09-11.md"
            f.write_text(self.text, encoding="utf-8")
            self.assertEqual(chk.check_file(f, valid), [])


PARTIAL = """# 2026-09-13 今天 wiki 學到什麼

## 🛠️ 功能

### [[entities/claude-code|Claude Code]]

> **最新動態**（2026-09-13）
> 功能事實。

## 不是領域的節

### [[entities/pricing|定價]]

> **最新動態**（2026-09-13）
> 不該被收。

## 🌐 社群

### [[topics/community-tech-patterns|社群模式]]

> **最新工作流模式**（2026-09-13）
> 社群事實。
"""

NO_NEWS = """# 2026-09-14 今天 wiki 學到什麼

> 今日 wiki 無新知（2026-09-14）
"""


NEWS = """# 日報

**日期：** 2026-09-11

---

### 📌 今日聚焦
- **[重大事件]** 聚焦甲（[官方](https://example.com/a)）
- **[社群趨勢]** 聚焦乙（[GitHub](https://github.com/x/issues/1)）
- **[持續追蹤]** 聚焦丙，來源只在歸因帳本（[媒體](https://example.com/ledger-only)）

### ⭐ 重點話題

**[故事 A 與聚焦甲同源](https://example.com/a)**
內文 A。
`HN / x` · 09/11 14:30 UTC

**[故事 B](https://example.com/b)**
內文 B。
`GitHub Issues / claude-code` · 09/11 09:27 UTC

**[故事 C](https://example.com/c)**
內文 C。
`src` · 09/11 09:00 UTC

### 🔧 技術更新
- 不該被搬。
"""


class TestTopSectionsFromNews(unittest.TestCase):
    """丙-2：daily/ 頂部搬 news/ 的 📌 今日聚焦；⭐ 重點話題剔掉聚焦已講過的 URL，最多 5 則。"""

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        root = Path(self._td.name)
        (root / "wiki").mkdir()
        self.wiki = _wiki(root / "wiki")
        news = root / "news"; news.mkdir()
        (news / "2026-09-11.md").write_text(NEWS, encoding="utf-8")
        # claude-code 頁把聚焦甲的來源 URL 寫進正文 → 不算漏收；聚焦乙的 URL 沒人寫 → WARN
        f = self.wiki / "entities" / "claude-code.md"
        f.write_text(f.read_text(encoding="utf-8") + "\n來源：https://example.com/a\n", encoding="utf-8")
        ledger = root / "attr.jsonl"
        ledger.write_text('{"date": "2026-09-11", "page": "entities/x", "item_url": "https://example.com/ledger-only"}\n'
                          '{"date": "2026-09-10", "page": "entities/x", "item_url": "https://github.com/x/issues/1"}\n',
                          encoding="utf-8")
        self.text, _, self.warnings = gen.generate("2026-09-11", self.wiki, news, ledger)

    def tearDown(self):
        self._td.cleanup()

    def test_focus_copied_verbatim_above_domains(self):
        self.assertIn("## 📌 今日聚焦\n\n- **[重大事件]** 聚焦甲（[官方](https://example.com/a)）\n", self.text)
        self.assertLess(self.text.index("## 📌 今日聚焦"), self.text.index("## 🛠️ 功能"))
        self.assertNotIn("不該被搬", self.text)

    def test_top_stories_dedup_against_focus_and_drop_source_line(self):
        self.assertIn("## ⭐ 重點話題", self.text)
        self.assertNotIn("故事 A 與聚焦甲同源", self.text)
        self.assertIn("**[故事 B](https://example.com/b)**\n內文 B。", self.text)
        self.assertNotIn("GitHub Issues / claude-code", self.text)

    def test_focus_source_missing_from_ledger_and_pages_is_warned(self):
        # 第 1 條：URL 在今日頁正文 → 不警告；第 3 條：URL 在當日歸因帳本 → 不警告；
        # 第 2 條：帳本裡只有前一天的歸因、頁面也沒寫 → 警告
        self.assertTrue(any("聚焦第 2 條" in w for w in self.warnings))
        self.assertFalse(any("聚焦第 1 條" in w for w in self.warnings))
        self.assertFalse(any("聚焦第 3 條" in w for w in self.warnings))

    def test_parser_ignores_top_sections_and_checker_accepts(self):
        r = _parse(self.text, "2026-09-11")
        self.assertEqual(r["itemCount"], 6)
        self.assertNotIn("📌 今日聚焦", [s["label"] for s in r["sections"]])
        chk = load_script_module("check_reader_digest")
        valid = {"entities/claude-code", "entities/managed-agents", "topics/market-signals",
                 "topics/tail-in-label", "topics/header-domain-only", "topics/internal-ref"}
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "2026-09-11.md"
            f.write_text(self.text, encoding="utf-8")
            self.assertEqual(chk.check_file(f, valid), [])

    def test_no_news_file_means_no_top_sections(self):
        text, _, _ = gen.generate("2026-09-11", self.wiki, Path(self._td.name) / "nope", Path(self._td.name) / "nope.jsonl")
        self.assertNotIn("📌", text)


class TestFrozenPagesKeptOnRegenerate(unittest.TestCase):
    """隔天重產昨天的日報：昨天那頁的 callout 已被覆寫成今天的日期，既有檔裡的版本要留住。"""

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.wiki = _wiki(Path(self._td.name))
        self.existing = (
            "# 2026-09-11 今天 wiki 學到什麼\n\n## 🛠️ 功能\n\n"
            "### [[entities/claude-code|Claude Code]]\n\n> **最新動態**（2026-09-11）\n> 舊版內容，頁面已改寫。\n\n"
            "### [[entities/gone-page|已被覆寫的頁]]\n\n> **最新動態**（2026-09-11）\n> 這頁今天的 callout 已是 09-12，重產要留住我。\n\n"
            "## 🤖 模型\n\n### [[entities/old-page|舊頁]]\n\n> **最新動態**（2026-09-11）\n> 也留住。\n"
        )

    def tearDown(self):
        self._td.cleanup()

    def test_default_freezes_existing_pages_and_only_adds_new_ones(self):
        text, _, warnings = gen.generate("2026-09-11", self.wiki, Path(self._td.name) / "nope",
                                         Path(self._td.name) / "nope.jsonl", existing=self.existing)
        self.assertIn("> 舊版內容，頁面已改寫。", text, "既有頁不重讀 wiki——重讀會把隔天補進 callout 的事洩漏進舊日報")
        self.assertNotIn("- **v2.1.268**", text)
        self.assertIn("### [[entities/managed-agents|Managed Agents]]", text, "既有檔沒有的新頁要補進來")
        self.assertIn("### [[entities/gone-page|已被覆寫的頁]]", text)
        self.assertTrue(any("維持原樣未重讀" in w for w in warnings))

    def test_pages_with_moved_on_callouts_are_kept_verbatim(self):
        text, count, warnings = gen.generate("2026-09-11", self.wiki, Path(self._td.name) / "nope",
                                             Path(self._td.name) / "nope.jsonl", existing=self.existing, refresh=True)
        self.assertIn("### [[entities/gone-page|已被覆寫的頁]]", text)
        self.assertIn("> 這頁今天的 callout 已是 09-12，重產要留住我。", text)
        self.assertIn("> 也留住。", text)
        self.assertTrue(any("保留既有檔 2 頁" in w for w in warnings))

    def test_refresh_uses_fresh_wiki_version_for_pages_still_dated_today(self):
        text, _, _ = gen.generate("2026-09-11", self.wiki, Path(self._td.name) / "nope",
                                  Path(self._td.name) / "nope.jsonl", existing=self.existing, refresh=True)
        self.assertNotIn("舊版內容，頁面已改寫", text)
        self.assertIn("- **v2.1.268**", text)
        self.assertEqual(text.count("### [[entities/claude-code|"), 1)

    def test_no_existing_file_no_carry_over(self):
        text, _, warnings = gen.generate("2026-09-11", self.wiki, Path(self._td.name) / "nope",
                                         Path(self._td.name) / "nope.jsonl")
        self.assertNotIn("gone-page", text)
        self.assertFalse(any("保留既有檔" in w for w in warnings))


class TestReaderTopStories(unittest.TestCase):
    def test_web_side_dedup_matches_generator(self):
        d = {"focus": [{"ref_urls": ["https://example.com/a"]}],
             "topStories": [{"title": f"t{i}", "url": f"https://example.com/{c}"} for i, c in enumerate("abcdefg")]}
        tops = build_web.reader_top_stories(d)
        self.assertEqual([t["url"][-1] for t in tops], list("bcdef"))

    def test_attach_sets_reader_top_stories(self):
        d = build_web.empty_digest("2026-09-13")
        d["focus"] = [{"ref_urls": ["https://example.com/a"]}]
        d["topStories"] = [{"title": "A", "url": "https://example.com/a"}, {"title": "B", "url": "https://example.com/b"}]
        digest_all = {"2026-09-13": d}
        build_web.attach_reader_digests(digest_all, {"2026-09-13": _parse(PARTIAL, "2026-09-13")})
        self.assertEqual([t["title"] for t in d["readerTopStories"]], ["B"])


class TestParser(unittest.TestCase):
    def test_unknown_section_pages_not_swallowed(self):
        r = _parse(PARTIAL, "2026-09-13")
        self.assertEqual([s["key"] for s in r["sections"]], ["features", "community"])
        self.assertEqual(r["itemCount"], 2)
        self.assertEqual(r["sections"][1]["label"], "🌐 社群")

    def test_no_news(self):
        r = _parse(NO_NEWS, "2026-09-14")
        self.assertTrue(r["noNews"])
        self.assertEqual(r["sections"], [])
        self.assertEqual(r["summary"], "今日 wiki 無新知（2026-09-14）")

    def test_hand_written_summary_still_recognised(self):
        r = _parse("# 2026-09-13 今天 wiki 學到什麼\n\n> 手寫總結。\n\n" + PARTIAL.split("\n", 2)[2], "2026-09-13")
        self.assertEqual(r["summary"], "手寫總結。")


class TestAttachReaderDigests(unittest.TestCase):
    def test_reader_date_gets_reader_and_preview_from_first_page(self):
        digest_all = {"2026-09-13": build_web.empty_digest("2026-09-13")}
        digest_all["2026-09-13"]["preview"] = "舊的新聞式 preview"
        build_web.attach_reader_digests(digest_all, {"2026-09-13": _parse(PARTIAL, "2026-09-13")})
        d = digest_all["2026-09-13"]
        self.assertIn("reader", d)
        self.assertEqual(d["preview"], "Claude Code：功能事實。")

    def test_legacy_date_untouched(self):
        """改版日之前的日期沒有 daily/ 檔，digest 一字不動——歷史頁不可壞。"""
        legacy = build_web.empty_digest("2026-08-01")
        legacy["preview"] = "舊日報的 preview"
        digest_all = {"2026-08-01": legacy}
        build_web.attach_reader_digests(digest_all, {"2026-09-13": _parse(PARTIAL, "2026-09-13")})
        self.assertNotIn("reader", digest_all["2026-08-01"])
        self.assertEqual(digest_all["2026-08-01"]["preview"], "舊日報的 preview")

    def test_reader_without_raw_material_creates_bare_digest(self):
        digest_all: dict = {}
        build_web.attach_reader_digests(digest_all, {"2026-09-13": _parse(PARTIAL, "2026-09-13")})
        self.assertEqual(digest_all["2026-09-13"]["articleCount"], 0)
        self.assertEqual(digest_all["2026-09-13"]["sourceStatus"], [])


class TestReaderSearchText(unittest.TestCase):
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
        self.assertIn("Claude Code", txt)
        self.assertIn("最新工作流模式", txt)
        self.assertNotIn("聚焦句甲", txt)

    def test_focus_and_top_five_headlines_indexed(self):
        txt = build_web.reader_search_text(self.r, self.d)
        self.assertIn("聚焦句甲", txt)
        self.assertIn("重點 4", txt)
        self.assertNotIn("重點 5", txt, "重點話題只上站前 5 則，第 6 則不索引")
        self.assertNotIn("媒體覆述", txt)

    def test_headlines_already_in_focus_not_indexed_twice(self):
        d = dict(self.d)
        d["focus"] = [{"tag": "[重大事件]", "text": "聚焦句甲", "ref_urls": ["u0"]}]
        d["topStories"] = [{"title": f"重點 {i}", "url": f"u{i}"} for i in range(7)]
        txt = build_web.reader_search_text(self.r, d)
        self.assertNotIn("重點 0", txt)
        self.assertIn("重點 5", txt)


class TestChecker(unittest.TestCase):
    """scripts/check_reader_digest.py 是 Step 2b 的格式閘——它抓不到的違規，
    會以「該領域整段在網站上消失」的形式靜默發生。"""

    def setUp(self):
        self.chk = load_script_module("check_reader_digest")
        self.valid = {"entities/claude-code", "claude-code", "topics/community-tech-patterns"}

    def _check(self, text, name="2026-09-13"):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / f"{name}.md"
            f.write_text(text, encoding="utf-8")
            return self.chk.check_file(f, self.valid)

    HEAD = "# 2026-09-13 今天 wiki 學到什麼\n\n## 🛠️ 功能\n\n"

    def test_good_file_passes(self):
        self.assertEqual(self._check(self.HEAD + "### [[entities/claude-code|Claude Code]]\n\n> **最新動態**（2026-09-13）\n> 事實。\n"), [])

    def test_no_news_file_passes(self):
        self.assertEqual(self._check("# 2026-09-13 今天 wiki 學到什麼\n\n> 今日 wiki 無新知（2026-09-13）\n"), [])

    def test_bad_domain_label_flagged(self):
        text = "# 2026-09-13 今天 wiki 學到什麼\n\n## 🛠 功能\n\n### [[entities/claude-code|Claude Code]]\n\n> **最新動態**（2026-09-13）\n> 事實。\n"
        self.assertTrue(any("不在六個領域內" in p for p in self._check(text)))

    def test_dead_wikilink_flagged(self):
        text = self.HEAD + "### [[entities/does-not-exist|X]]\n\n> **最新動態**（2026-09-13）\n> 事實。\n"
        self.assertTrue(any("不存在的 wiki 頁" in p for p in self._check(text)))

    def test_callout_date_mismatch_flagged(self):
        text = self.HEAD + "### [[entities/claude-code|Claude Code]]\n\n> **最新動態**（2026-09-01）\n> 別天的。\n"
        self.assertTrue(any("與檔名" in p and "callout" in p for p in self._check(text)))

    def test_page_without_callout_flagged(self):
        text = self.HEAD + "### [[entities/claude-code|Claude Code]]\n\n### [[topics/community-tech-patterns|Y]]\n\n> **最新動態**（2026-09-13）\n> 事實。\n"
        self.assertTrue(any("沒有任何 `>` callout 行" in p for p in self._check(text)))

    def test_stray_quote_outside_page_flagged(self):
        text = self.HEAD + "> **最新動態**（2026-09-13）\n> 沒掛在頁面小節下。\n"
        self.assertTrue(any("散落" in p for p in self._check(text)))

    def test_title_date_mismatch_flagged(self):
        text = "# 2026-01-01 今天 wiki 學到什麼\n\n## 🛠️ 功能\n\n### [[entities/claude-code|Claude Code]]\n\n> **最新動態**（2026-09-13）\n> 事實。\n"
        self.assertTrue(any("標題日期" in p for p in self._check(text)))


if __name__ == "__main__":
    unittest.main()
