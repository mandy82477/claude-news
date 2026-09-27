"""wiki ingest 收報落帳：記者回報 → 歸因帳／轉知指令／對帳。

釘住的情境：未註冊 slug 不得落帳、頁面不存在不得落帳、dry-run 不碰帳本、--apply 冪等、
「已處理 H-xxxxxx」轉成 close、回報提到包外 URL 要警示、包裡沒被提到的 URL 要列成未回應。
帳本一律用暫存副本，真帳本只讀。
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "collect_reporter_reports", ROOT / "scripts" / "collect_reporter_reports.py")
mod = importlib.util.module_from_spec(_spec)
sys.modules["collect_reporter_reports"] = mod
_spec.loader.exec_module(mod)

D = "2026-01-02"
U1, U2, U3, OUT = "https://a.test/1", "https://b.test/2", "https://c.test/3", "https://zz.test/9"


def run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main(argv)
    return rc, buf.getvalue()


def sha(p: Path) -> str:
    return hashlib.sha1(p.read_bytes()).hexdigest()


REPORT = f"""前面有一些敘述，主編不讀。

## 功能 記者回報
更新頁面：entities/claude-code
feature-radar 新增：某某標頭
index.md 狀態變更：無
新增頁面：無
同步自查：⚠️ 需主編轉知社群記者：[[topics/community-tech-patterns]] 評估新增一列
待查證命中處置：無命中
轉知處置：已處理 1 筆: H-abc123（補了 wikilink） ／ 不適用 1 筆: H-def456（議題已失效）
分類回退：無
來源歸因：
hacker-news | 功能 | entities/claude-code | {U1} | Alpha
google-news | 功能 | entities/claude-code | {U1} | Alpha
bogus-slug | 功能 | entities/claude-code | {U2} | Bravo
hacker-news | 功能 | entities/no-such-page | {U2} | Bravo
hacker-news | 功能 | entities/claude-code | {OUT} | 包外
| 呈現品質審查 | entities/claude-code：✅ 通過 |
機械自查：python scripts/check_cell_limits.py --page claude-code → OK
"""


MARKET_REPORT = f"""## 投資分析 記者回報
更新頁面：topics/market-signals
判讀新增：1 則（第 5 類：事件）
買得到的標的：無
里程碑登記：無
回顧結算 ⏳ 新增：無
feature-radar 新增：無
index.md 狀態變更：無
新增頁面：無
同步自查：不適用
待查證命中處置：無命中
轉知處置：無待接手
來源歸因：
google-news | 投資分析 | topics/market-signals | {U3} | Charlie
"""


class Case(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        d = self.d = Path(self.tmp.name)
        (d / "archive").mkdir()
        (d / "archive" / f"{D}.json").write_text(json.dumps({"items": [
            {"url": u, "title": u} for u in (U1, U2, U3, OUT)]}), encoding="utf-8")
        (d / "packets").mkdir()
        (d / "packets" / "功能.md").write_text(
            f"## [功能] 條目（共 3 則（3 組））\n\n### Alpha\n- **URL：** {U1}\n\n### Bravo\n- **URL：** {U2}\n\n"
            f"### Charlie\n- **URL：** {U3}\n\nEND 3\n", encoding="utf-8")
        (d / "reports").mkdir()
        (d / "reports" / "功能.md").write_text(REPORT, encoding="utf-8")
        (d / "att.jsonl").write_text("", encoding="utf-8")
        ho = [{"id": "H-abc123", "opened": "2026-01-01", "from": "社群", "to": "功能", "page": "entities/claude-code",
               "note": "n", "status": "open"},
              {"id": "H-def456", "opened": "2026-01-01", "from": "社群", "to": "功能", "page": "entities/claude-code",
               "note": "m", "status": "open"}]
        (d / "ho.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in ho), encoding="utf-8")

    def argv(self, *extra):
        d = self.d
        return ["--date", D, str(d / "reports"), "--packets", str(d / "packets"),
                "--attribution", str(d / "att.jsonl"), "--handoffs", str(d / "ho.jsonl"),
                "--archive-dir", str(d / "archive"), *extra]

    def test_dry_run_is_default_and_touches_nothing(self):
        a, h = sha(self.d / "att.jsonl"), sha(self.d / "ho.jsonl")
        rc, out = run(self.argv())
        self.assertEqual(rc, 0, out)
        self.assertIn("DRY-RUN", out)
        self.assertEqual(a, sha(self.d / "att.jsonl"))
        self.assertEqual(h, sha(self.d / "ho.jsonl"))
        rc, out = run(self.argv("--dry-run"))
        self.assertEqual(a, sha(self.d / "att.jsonl"))

    def test_bad_rows_warned_and_not_written(self):
        rc, out = run(self.argv("--apply"))
        self.assertEqual(rc, 0, out)
        self.assertIn("未註冊 slug「bogus-slug」，不寫入", out)
        self.assertIn("頁面不存在 wiki/entities/no-such-page.md，不寫入", out)
        rows = [json.loads(x) for x in (self.d / "att.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual({(r["source"], r["item_url"]) for r in rows},
                         {("hacker-news", U1), ("google-news", U1), ("hacker-news", OUT)})
        self.assertTrue(all(r["date"] == D and r["category"] == "功能" for r in rows))

    def test_apply_is_idempotent(self):
        run(self.argv("--apply"))
        a = sha(self.d / "att.jsonl")
        rc, out = run(self.argv("--apply"))
        self.assertEqual(a, sha(self.d / "att.jsonl"))
        self.assertIn("0 行待 append", out)

    def test_handoff_close_executed_and_void_left_for_editor(self):
        rc, out = run(self.argv())
        self.assertIn('close H-abc123 --by 功能 --result "補了 wikilink"', out)
        self.assertIn("H-def456", out.split("轉知「不適用」")[1])
        run(self.argv("--apply"))
        state = mod.ph.load(self.d / "ho.jsonl")
        self.assertEqual(state["H-abc123"]["status"], "done")
        self.assertEqual(state["H-def456"]["status"], "open")

    def test_open_draft_uses_index_owner(self):
        rc, out = run(self.argv())
        self.assertIn("open --from 功能 --to 社群 --page topics/community-tech-patterns", out)

    def test_packet_reconciliation(self):
        rc, out = run(self.argv())
        self.assertIn(f"不在該記者包裡（分錯人或貼錯？）：{OUT}", out)
        unanswered = out.split("## 未回應清單")[1].split("##")[0]
        self.assertIn(U3, unanswered)
        self.assertNotIn(U1, unanswered)

    def test_log_skeleton(self):
        rc, out = run(self.argv())
        skel = out.split("## log 條目骨架")[1]
        self.assertIn(f"## {D} Ingest", skel)
        self.assertIn("**功能**：entities/claude-code", skel)
        self.assertIn("feature-radar：[功能] 某某標頭", skel)

    def test_market_reporter_report_is_collected_without_packet(self):
        (self.d / "reports" / "投資分析.md").write_text(
            MARKET_REPORT, encoding="utf-8")
        rc, out = run(self.argv("--apply"))
        self.assertEqual(rc, 0, out)
        self.assertNotIn("[投資分析] 回報缺欄", out)
        self.assertNotIn("[投資分析] 找不到派工包", out)
        self.assertIn("**投資分析**：topics/market-signals", out)
        rows = [json.loads(x) for x in (self.d / "att.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertIn(("投資分析", "topics/market-signals", U3), {(r["category"], r["page"], r["item_url"]) for r in rows})

    def test_duplicate_close_across_reports_applies_once(self):
        dup = REPORT.replace("## 功能 記者回報", "## 模型 記者回報").replace("／ 不適用 1 筆: H-def456（議題已失效）", "")
        (self.d / "reports" / "模型.md").write_text(dup, encoding="utf-8")
        rc, out = run(self.argv("--apply"))
        self.assertEqual(rc, 0, out)
        self.assertIn("H-abc123 同批另一份回報已結", out)
        closes = [json.loads(x) for x in (self.d / "ho.jsonl").read_text(encoding="utf-8").splitlines()
                  if '"closed"' in x]
        self.assertEqual([c["id"] for c in closes], ["H-abc123"])

    def test_report_without_header_fails(self):
        (self.d / "reports" / "壞.md").write_text("只是一段敘述，沒有回報表頭", encoding="utf-8")
        rc, out = run(self.argv())
        self.assertEqual(rc, 1)
        self.assertIn("找不到", out)


if __name__ == "__main__":
    unittest.main()


class TestParsing(unittest.TestCase):
    """真實回報（2026-09-26 七位記者）的格式變體：全形分隔、表格列、code block、段外說明、巢狀括號。"""

    def test_fullwidth_and_table_rows_parse(self):
        val = ("hacker-news｜功能｜entities/claude-code｜https://a/｜T\n"
               "| slug | 類別 | page | url | title |\n|---|---|---|---|---|\n"
               "| github | 功能 | entities/claude-code | https://b/ | B |\n"
               "google-news 功能 entities/x https://c/")
        rows, bad = mod.parse_attribution(val)
        self.assertEqual([r[0] for r in rows], ["hacker-news", "github"])
        self.assertEqual(rows[1][3], "https://b/")
        self.assertEqual(bad, ["google-news 功能 entities/x https://c/"])

    def test_nonempty_attribution_with_zero_rows_warns(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            (d / "r.md").write_text("## 功能 記者回報\n來源歸因：見上方說明，三則都有歸因\n", encoding="utf-8")
            (d / "att.jsonl").write_text("", encoding="utf-8")
            rc, out = run(["--date", D, str(d / "r.md"), "--attribution", str(d / "att.jsonl"),
                           "--packets", str(d)])
        self.assertIn("解析出 0 行", out)

    def test_unknown_label_and_blank_line_end_field(self):
        r = mod.parse_report("## [功能] 記者回報\n分類回退：無\n\n其他處置說明：\n- 48,000 檔案兩則未寫入\n"
                             "來源歸因：無\n")
        self.assertEqual(r["fields"]["分類回退"], "無")
        self.assertEqual(r["fields"]["來源歸因"], "無")
        tight = mod.parse_report("## [功能] 記者回報\n分類回退：無\n其他處置說明：\n- 兩則未寫入\n")
        self.assertEqual(tight["fields"]["分類回退"], "無", "沒有空行隔開時，段外標題也要結束上一欄")

    def test_code_block_value_kept_whole_and_last_header_wins(self):
        # 真實模型記者回報的形狀：先一段敘述性表頭，正式版整份包在 code block 裡
        r = mod.parse_report("## [模型] 記者回報\n敘述段\n\n```\n## 模型 記者回報\nfeature-radar 新增：某標頭\n"
                             "分類回退：無\n```\n之後的敘述\n")
        self.assertEqual(r["fields"]["feature-radar 新增"], "某標頭")
        self.assertEqual(r["fields"]["分類回退"], "無")
        # 未包 block 的回報：欄位值自己是一段 code block，整段收進該欄
        r2 = mod.parse_report("## [功能] 記者回報\nfeature-radar 新增：\n```markdown\n### 某標頭\n"
                              "**發布：** 2026-09-25\n```\n來源歸因：無\n")
        self.assertIn("### 某標頭", r2["fields"]["feature-radar 新增"])
        self.assertIn("**發布：** 2026-09-25", r2["fields"]["feature-radar 新增"])

    def test_nested_parens_result_not_truncated(self):
        val = "已處理 1 筆：H-840cab（加「後續（2026-09-26）」，回補 wikilink，未替使用者代下結論）"
        self.assertEqual(mod.handoff_closes(val),
                         [("H-840cab", "加「後續（2026-09-26）」，回補 wikilink，未替使用者代下結論")])

    def test_page_terminators_and_multiple_warnings(self):
        self.assertEqual(mod._PAGE.search("評估（`topics/ai-agent-safety` 技術彙整").group(1), "topics/ai-agent-safety")
        self.assertEqual(mod._PAGE.search("補 entities/pricing（定價）").group(1), "entities/pricing")
        asks, other = mod.handoff_asks("⚠️ 需主編轉知功能記者：A `topics/x`；⚠️ 需主編轉知商業記者：B entities/pricing"
                                       "\n⚠️ 需主編轉知（登入 wiki/index.md 人物列）")
        self.assertEqual([a[0] for a in asks], ["功能", "商業"])
        self.assertNotIn("商業記者", asks[0][1])
        self.assertEqual(len(other), 1)

    def test_unaddressed_warning_goes_to_log_skeleton(self):
        r = mod.parse_report("## [人物] 記者回報\n更新頁面：無\n同步自查：⚠️ 需主編轉知（登入 wiki/index.md 人物列）\n")
        asks, other = mod.handoff_asks(r["fields"]["同步自查"])
        skel = mod.log_skeleton(D, [r], [], [], [("人物", t) for t in other])
        self.assertIn("主編待辦", skel)
        self.assertIn("登入 wiki/index.md 人物列", skel)

    def test_title_issue_and_short_name_count_as_mentioned(self):
        pk = {"https://aidash.dev/": "Show HN: I couldn't deal with another tab",
              "https://tui2web.com/": "Show HN: Tui2web – use any TUI on the web",
              "https://github.com/anthropics/claude-code/issues/45297": "[BUG] Cowork: Folder does not support UNC",
              "https://news.test/x": "Anthropic Opens Directory Submission Portal - Unite.AI"}
        text = "Tui2web 7 分、aidash 4 分未達門檻；#45297 已記已知問題；anthropic opens directory submission portal 查無原文"
        for u, t in pk.items():
            self.assertTrue(mod.mentioned(u, t, set(), text, pk), u)
        self.assertFalse(mod.mentioned("https://r.test/z", "Need some security advice", set(), text, pk))


class TestContractWithShared(unittest.TestCase):
    """shared.md「回報格式」code block 的欄名＝收報腳本認得的欄名。改一邊這裡紅。"""

    def test_report_field_names_match_contract(self):
        text = (ROOT / ".claude" / "reporter-rules" / "shared.md").read_text(encoding="utf-8")
        block = text.split("## [類別] 記者回報", 1)[1].split("```", 1)[0]
        labels = [ln.split("：", 1)[0].strip() for ln in block.splitlines()
                  if "：" in ln and not ln.startswith("|")]
        self.assertEqual(labels[:9], list(mod.CORE_FIELDS))
        for lab in labels:
            self.assertIn(lab, mod.FIELDS, f"shared.md 回報欄「{lab}」收報腳本不認得")


class TestSecondRoundFixes(unittest.TestCase):
    def test_publisher_domain_and_leading_words_count_as_mentioned(self):
        text = ("New Scientist 反向評論已記；Microsoft 兩則（CNBC＋GeekWire）已處理；Accenture 合作已寫；"
                "Jev 低價新模型（FT）屬競品面；Yahoo Tech（48,000）為第二家報導")
        cases = {
            "https://www.newscientist.com/article/1": "Anthropic’s discovery will be just another tool - New Scientist",
            "https://www.cnbc.com/2026/09/25/microsoft-copilot.html": "Microsoft packages business AI in single app - CNBC",
            "https://finance.yahoo.com/x": "Accenture (ACN) Joins Anthropic’s AI Safety Effort - finance.yahoo.com",
            "https://www.ft.com/content/1": "The cheap new AI model taking aim at OpenAI and Anthropic",
            "https://tech.yahoo.com/ai/48": "48,000 files deleted in 103 seconds - Yahoo Tech",
        }
        for u, t in cases.items():
            self.assertTrue(mod.mentioned(u, t, set(), text, cases), u)
        self.assertFalse(mod.mentioned("https://r.test/z", "Need some security advice", set(), text, cases))

    def test_leading_significant_words_alone_count(self):
        text = "Microsoft 兩則已處理；Accenture 合作已寫"  # 不含出版者與網域，只剩標題顯著詞可對
        self.assertTrue(mod.mentioned("https://www.geekwire.com/x", "Microsoft unveils all-in-one Copilot app - GeekWire",
                                      set(), text, {}))
        self.assertTrue(mod.mentioned("https://finance.example.com/x", "Accenture (ACN) Joins Safety Effort - Example",
                                      set(), text, {}))

    def test_platform_bulk_count(self):
        pk = {f"https://www.reddit.com/r/x/comments/{i}/": f"post {i}" for i in range(4)}
        self.assertEqual(mod.bulk_answered(pk, "Reddit 4 則未達門檻"), set(pk))
        self.assertEqual(mod.bulk_answered(pk, "Reddit 3 則未達門檻"), set())

    def test_self_owned_handoff_has_no_draft(self):
        wiki = ROOT / "wiki"
        self.assertEqual(mod.draft_open("安全政策", "功能", "GitGuardian 研究（`topics/ai-agent-safety` 技術彙整）",
                                        wiki / "index.md", wiki), [])
        self.assertTrue(mod.draft_open("社群", "功能", "評估 `topics/ai-agent-safety` 新列", wiki / "index.md", wiki))

    def test_fence_close_ends_field_and_skeleton_takes_radar_titles(self):
        r = mod.parse_report("## [功能] 記者回報\nfeature-radar 新增：\n```markdown\n### 甲標頭\n**發布：** x\n"
                             "```\n（這段是記者的說明，不是欄位值）\n來源歸因：無\n")
        self.assertNotIn("記者的說明", r["fields"]["feature-radar 新增"])
        skel = mod.log_skeleton(D, [r], [], [], [])
        self.assertIn("- feature-radar：[功能] 甲標頭\n", skel)
