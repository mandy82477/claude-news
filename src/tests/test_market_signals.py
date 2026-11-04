"""build_web 端的投資訊號解析契約（wiki/topics/market-signals.md → 日報頁 💰 條目）。

判讀標題 `### 💰 事件名（YYYY-MM-DD）` 是規格（`.claude/reporter-rules/market/daily.md`
「判讀格式（機械契約字串）」表）與程式（`MARKET_SIGNAL_RE`）的共同契約。形狀漂了
不會有任何錯誤訊息——網站上的 💰 條目只是消失，正是 2026-08-14 日報區塊 emoji
的死法。本檔把三件事釘住：

  1. 取的是子樹裡最新一則（各頁最新在上、跨頁比日期）且標題／日期／所在頁解析正確
     （2026-11-02 第 22 波起判讀住四子頁，母頁沒有 `### 💰`；只讀母頁的話 💰 條目會靜默消失）
  2. 日期對得上的那天才注入 marketSignal，其餘日期不動
  3. 頁面不存在或無任何判讀時回 None（無訊號的日子頁面本來就不動）

另加一條真實頁面的煙霧測試：正式頁若有判讀，必須解析得出來。
"""
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module, REPO_ROOT

build_web = load_script_module("build_web")

PAGE = """# 投資訊號判讀

**狀態：** ongoing

## 近期判讀

### 💰 最新事件名（2026-09-04）

**方向**：某公司 ↑。

### 💰 較舊事件名（2026-08-26）

**方向**：某公司 ～。
"""


class TestParseMarketSignal(unittest.TestCase):
    def _write(self, text: str) -> Path:
        d = Path(tempfile.mkdtemp())
        f = d / "market-signals.md"
        f.write_text(text, encoding="utf-8")
        return f

    def test_takes_latest_entry(self):
        sig = build_web.parse_market_signal(self._write(PAGE))
        self.assertEqual(sig, {"title": "最新事件名", "date": "2026-09-04", "page": "market-signals"})

    def test_takes_latest_across_pages(self):
        """子頁的日期比母頁新 → 取子頁那則，並帶出所在頁（網站點擊直達子頁）。"""
        d = Path(tempfile.mkdtemp())
        (d / "market-signals.md").write_text("# 母頁\n\n本頁不放判讀。\n", encoding="utf-8")
        (d / "market-signals-ipo.md").write_text(PAGE, encoding="utf-8")
        (d / "market-signals-legal.md").write_text("### 💰 更新的一則（2026-09-05）\n", encoding="utf-8")
        sig = build_web.parse_market_signal([d / "market-signals.md", d / "market-signals-ipo.md",
                                             d / "market-signals-legal.md"])
        self.assertEqual(sig, {"title": "更新的一則", "date": "2026-09-05", "page": "market-signals-legal"})

    def test_h4_shell_is_not_a_signal(self):
        """母頁的同名指路殼用 h4，不得被當成判讀（只認 ###）。"""
        self.assertIsNone(build_web.parse_market_signal(self._write("#### 💰 殼（2026-09-29）\n")))

    def test_missing_page_returns_none(self):
        self.assertIsNone(build_web.parse_market_signal(Path("no-such-file.md")))

    def test_no_signal_entries_returns_none(self):
        f = self._write("# 投資訊號判讀\n\n## 近期判讀\n\n本週無訊號。\n")
        self.assertIsNone(build_web.parse_market_signal(f))

    def test_heading_shape_must_match(self):
        """缺 💰、缺全形括號日期、或標成 h2 都不算判讀（契約收得夠緊）。"""
        for bad in ("### 事件名（2026-09-04）",
                    "### 💰 事件名 (2026-09-04)",
                    "## 💰 事件名（2026-09-04）"):
            with self.subTest(bad=bad):
                self.assertIsNone(build_web.parse_market_signal(self._write(bad + "\n")))


class TestAttachMarketSignal(unittest.TestCase):
    def setUp(self):
        self.digests = {"2026-09-04": {"date": "2026-09-04"},
                        "2026-09-03": {"date": "2026-09-03"}}

    def test_injects_only_on_matching_date(self):
        sig = {"title": "事件", "date": "2026-09-04"}
        build_web.attach_market_signal(self.digests, sig)
        self.assertEqual(self.digests["2026-09-04"]["marketSignal"], sig)
        self.assertNotIn("marketSignal", self.digests["2026-09-03"])

    def test_no_signal_injects_nothing(self):
        build_web.attach_market_signal(self.digests, None)
        for d in self.digests.values():
            self.assertNotIn("marketSignal", d)

    def test_date_without_digest_is_noop(self):
        build_web.attach_market_signal(self.digests, {"title": "事件", "date": "2026-01-01"})
        for d in self.digests.values():
            self.assertNotIn("marketSignal", d)


CHILDREN = {"market-signals-ipo", "market-signals-legal", "market-signals-compute", "market-signals-customers"}


class TestRealPage(unittest.TestCase):
    def test_subtree_found_by_parent_field(self):
        """子頁清單從標頭「上層」現算：四子頁都要被找到（漏一頁＝那頁的判讀永遠上不了網站）。"""
        page = REPO_ROOT / "wiki" / "topics" / "market-signals.md"
        if not page.exists():
            self.skipTest("market-signals.md 不存在")
        found = {f.stem for f in build_web.market_signal_pages(page)}
        self.assertTrue(CHILDREN <= found, f"上層指向 market-signals 的子頁少了：{CHILDREN - found}")

    def test_live_subtree_parses_if_it_has_entries(self):
        pages = build_web.market_signal_pages()
        texts = [f.read_text(encoding="utf-8") for f in pages if f.exists()]
        if not any("### 💰" in t for t in texts):
            self.skipTest("正式頁目前無判讀條目")
        sig = build_web.parse_market_signal(pages)
        self.assertIsNotNone(sig, "子樹有 ### 💰 標題卻解析不出——標題形狀已漂")
        self.assertRegex(sig["date"], r"^\d{4}-\d{2}-\d{2}$")
        newest = max(m[1] for t in texts for m in build_web.MARKET_SIGNAL_RE.findall(t))
        self.assertEqual(sig["date"], newest, "取到的不是子樹裡最新的一則")

    def test_disclaimer_callout_is_first_callout(self):
        """頁首免責 callout 常駐、不得移除（.claude/reporter-rules/market/daily.md「定位與禁止指令措辭」）。

        2026-10-03 前這條只有文字。禁詞（買進／加碼／布局…）刻意不做機械掃描：規則本身豁免
        「引用他人行為的事實敘述」，當天正式頁 9 處命中全是這類（Nvidia 加碼投資、算力布局），
        掃了只會誤報。
        """
        for name in ["market-signals", *sorted(CHILDREN)]:
            page = REPO_ROOT / "wiki" / "topics" / f"{name}.md"
            if not page.exists():
                continue
            with self.subTest(page=name):
                body = page.read_text(encoding="utf-8").split("\n# ", 1)[-1]
                first_callout = next((ln for ln in body.splitlines() if ln.startswith(">")), "")
                self.assertIn("非投資建議", first_callout)


class TestOwnership(unittest.TestCase):
    """懸置命中與轉知帳都要派給投資分析記者——領域欄是商業，沒有覆寫就會派給商業記者
    （第 22 波查到 data/pending-signals.jsonl 本頁 285 筆命中全記在商業記者名下）。"""

    def test_pending_hits_go_to_market_reporter(self):
        pm = load_script_module("pending_markers")
        spv = load_script_module("scan_pending_verifications")
        for name in ["market-signals", *sorted(CHILDREN)]:
            with self.subTest(page=name):
                r = pm.reporter_of(pm.WIKI_DIR / "topics" / f"{name}.md")
                self.assertEqual(r, "wiki-reporter-market")
                self.assertEqual(spv.REPORTER_LABEL.get(r), "投資分析", "標籤缺了，scan 的分組輸出會整組漏印")

    def test_handoff_owner_is_market(self):
        ph = load_script_module("pending_handoffs")
        for name in ["market-signals", *sorted(CHILDREN)]:
            with self.subTest(page=name):
                self.assertEqual(ph.OWNER_OVERRIDES.get(f"topics/{name}"), "投資分析")


if __name__ == "__main__":
    unittest.main()
