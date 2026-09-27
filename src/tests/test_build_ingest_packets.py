"""wiki ingest 派工包產生器：主編只寫 routing，其餘機械搬運必須對得上帳、擋得住壞輸入。

每條測試釘一個會讓派工悄悄出錯的情境：漏判一則、note 夾帶操作指示、來源對不到 slug、
包太大被截、同一事件十幾家媒體各佔一則、前一天已歸因的 URL 沒標出來。
所有寫檔都在暫存目錄——真帳本 data/classification-log.jsonl 只讀不寫。
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("build_ingest_packets", ROOT / "scripts" / "build_ingest_packets.py")
mod = importlib.util.module_from_spec(_spec)
sys.modules["build_ingest_packets"] = mod
_spec.loader.exec_module(mod)

REAL_DATE = "2026-09-26"
REAL_ARCHIVE = ROOT / "src" / "gathered_archive" / f"{REAL_DATE}.json"
REAL_LOG = ROOT / "data" / "classification-log.jsonl"
REAL_REGISTRY = ROOT / "data" / "source_registry.json"

LONG = "這是一段足夠長的原文摘要，讓複核記者有內容可以判斷分類是否正確，也讓派工包有東西可讀。"


def run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main(argv)
    return rc, buf.getvalue()


def sha(p: Path) -> str:
    return hashlib.sha1(p.read_bytes()).hexdigest()


class Sandbox:
    """暫存目錄裡的一整套輸入：原料、日報、registry、歸因帳、分類帳、routing。"""

    def __init__(self, items, routing, digest="# 日報\n", registry=None, date="2026-01-02",
                 attribution=None, log_rows=None):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.date = date
        (self.dir / "archive").mkdir()
        (self.dir / "news").mkdir()
        (self.dir / "archive" / f"{date}.json").write_text(
            json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8")
        (self.dir / "news" / f"{date}.md").write_text(digest, encoding="utf-8")
        reg = registry if registry is not None else json.loads(REAL_REGISTRY.read_text(encoding="utf-8"))
        (self.dir / "registry.json").write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")
        (self.dir / "att.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in attribution or []), encoding="utf-8")
        (self.dir / "log.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in log_rows or []), encoding="utf-8")
        self.write_routing(routing)

    def write_routing(self, routing):
        (self.dir / "routing.json").write_text(json.dumps(routing, ensure_ascii=False), encoding="utf-8")

    def argv(self, *extra):
        d = self.dir
        return ["--date", self.date, "--routing", str(d / "routing.json"), "--out", str(d / "out"),
                "--log", str(d / "log.jsonl"), "--archive-dir", str(d / "archive"),
                "--news-dir", str(d / "news"), "--registry", str(d / "registry.json"),
                "--attribution", str(d / "att.jsonl"), *extra]

    def packet(self, name):
        return (self.dir / "out" / f"{name}.md").read_text(encoding="utf-8")

    def close(self):
        self.tmp.cleanup()


def item(url, title, source="Hacker News", summary=LONG, **kw):
    base = {"title": title, "url": url, "source": source, "published": "01/01 00:00 UTC", "score": 10,
            "score_unit": "分", "source_count": 1, "summary": summary, "category": "", "topic": "",
            "dedup_key": "", "contributors": []}
    base.update(kw)
    return base


def small_case():
    items = [item("https://a.test/1", "Alpha launches widget"),
             item("https://b.test/2", "GitHub issue about bravo", source="GitHub Issues / claude-code"),
             item("https://c.test/3", "Unrelated charlie story")]
    routing = {"https://a.test/1": {"categories": ["功能"], "reason": "", "note": ""},
               "https://b.test/2": {"categories": ["功能", "社群"], "reason": "", "note": ""},
               "https://c.test/3": {"categories": [], "reason": "與 Claude 無關", "note": ""}}
    return items, routing


class TestRoutingGate(unittest.TestCase):
    def setUp(self):
        items, routing = small_case()
        self.sb = Sandbox(items, routing)
        self.addCleanup(self.sb.close)

    def test_happy_path_writes_ledger_and_packets(self):
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 0, out)
        self.assertIn("## [功能] 條目（共 2 則（2 組））", self.sb.packet("功能"))
        self.assertTrue(self.sb.packet("功能").rstrip().endswith("END 2"))
        self.assertIn("（slug：github-issues）", self.sb.packet("功能"))
        self.assertIn("主編排除理由：** 與 Claude 無關", self.sb.packet("排除"))
        rows = (self.sb.dir / "log.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(rows), 3)

    def test_rerun_is_idempotent(self):
        run(self.sb.argv())
        before = sha(self.sb.dir / "log.jsonl")
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 0)
        self.assertIn("append 0 行", out)
        self.assertEqual(before, sha(self.sb.dir / "log.jsonl"))

    def test_missing_url_fails_and_names_it(self):
        items, routing = small_case()
        del routing["https://c.test/3"]
        self.sb.write_routing(routing)
        before = sha(self.sb.dir / "log.jsonl")
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 1)
        self.assertIn("https://c.test/3", out)
        self.assertIn("routing 漏了原料", out)
        self.assertEqual(before, sha(self.sb.dir / "log.jsonl"), "驗證失敗不得寫帳")
        self.assertFalse((self.sb.dir / "out").exists(), "驗證失敗不得產包")

    def test_imperative_note_fails(self):
        items, routing = small_case()
        routing["https://a.test/1"]["note"] = "請記得同步 X 頁"
        self.sb.write_routing(routing)
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 1)
        self.assertIn("操作指示", out)

    def test_imperative_after_full_stop_fails(self):
        self.assertEqual(mod.imperative_hit("數字不同。順手補 pricing 頁"), "順手")

    def test_factual_note_passes_and_lands_on_item(self):
        items, routing = small_case()
        routing["https://a.test/1"]["note"] = "兩家媒體數字不同，請並陳"
        self.sb.write_routing(routing)
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 0, out)
        self.assertIn("- **註：** 兩家媒體數字不同，請並陳", self.sb.packet("功能"))

    def test_excluded_shell_without_override_blocks_before_writing(self):
        items, routing = small_case()
        items[2]["summary"] = '<a href="https://news.google.com/rss/articles/CBMabc'
        sb = Sandbox(items, routing)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 1)
        self.assertIn("殼層", out)
        self.assertEqual((sb.dir / "log.jsonl").read_text(encoding="utf-8"), "")
        routing["https://c.test/3"]["summary_override"] = "一則與 Claude 無關的新聞，標題提到 charlie 的故事內容"
        sb.write_routing(routing)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        row = json.loads((sb.dir / "log.jsonl").read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(row["summary"], row["summary_override"])


class TestSlugs(unittest.TestCase):
    def test_longest_prefix_wins(self):
        entries = mod.load_registry(REAL_REGISTRY)
        self.assertEqual(mod.slug_for("GitHub Issues / claude-code", entries), "github-issues")
        self.assertEqual(mod.slug_for("GitHub / anthropics/claude-code", entries), "github")
        self.assertEqual(mod.slug_for("GitHub Search", entries), "github")
        self.assertEqual(mod.slug_for("Blog / Simon Willison", entries), "blog")
        self.assertIsNone(mod.slug_for("GitHubby", entries))
        nested = [("GitHub", "github"), ("GitHub / anthropics", "gh-official")]
        self.assertEqual(mod.slug_for("GitHub / anthropics/claude-code", nested), "gh-official")

    def test_contributors_each_get_a_slug(self):
        entries = mod.load_registry(REAL_REGISTRY)
        it = item("https://x.test/", "t", contributors=["Google News / Anthropic", "HN Repo Bridge"])
        self.assertEqual(mod.item_slugs(it, entries)[0], ["hacker-news", "google-news", "hn-repo-bridge"])

    def test_unregistered_source_fails(self):
        reg = json.loads(REAL_REGISTRY.read_text(encoding="utf-8"))
        for s in reg["sources"]:
            if s["slug"] == "github":
                s["aliases"] = [a for a in s.get("aliases", []) if a != "GitHub Search"]
        items, routing = small_case()
        items.append(item("https://d.test/4", "some/repo", source="GitHub Search"))
        routing["https://d.test/4"] = {"categories": ["社群"], "reason": "", "note": ""}
        sb = Sandbox(items, routing, registry=reg)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 1)
        self.assertIn("未註冊來源「GitHub Search」", out)


class TestPacketShape(unittest.TestCase):
    def test_oversize_packet_splits_with_end_on_each_part(self):
        items, routing = [], {}
        for i in range(75):  # 75 則 × 400 字摘要 ≈ 30K 字元的摘要
            u = f"https://s.test/{i}"
            items.append(item(u, f"uniq{i}word zz{i}", summary="字" * 400))
            routing[u] = {"categories": ["社群"], "reason": "", "note": ""}
        sb = Sandbox(items, routing)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        parts = sorted((sb.dir / "out").glob("社群-*.md"))
        self.assertEqual(len(parts), 2, out)
        self.assertFalse((sb.dir / "out" / "社群.md").exists())
        total = 0
        for k, p in enumerate(parts, 1):
            text = p.read_text(encoding="utf-8")
            self.assertLessEqual(len(text), mod.MAX_CHARS)
            self.assertIn(f"第 {k}／2 份", text.splitlines()[0])
            self.assertTrue(text.rstrip().splitlines()[-1].startswith("END 75"))
            total += text.count("\n### ")
        self.assertEqual(total, 75, "切份不得掉則")

    def test_same_event_grouped_and_digest_paragraph_attached(self):
        digest = ("### 📌 今日聚焦\n\n- **[重大事件]** 法院維持認定。（[R](https://r.test/1)）\n\n"
                  "### 📰 媒體報導\n\n**[Other](https://o.test/9)**\n段落第一行\n`Google News / O` · 01/01\n\n")
        items = [item("https://r.test/1", "Appeals court upholds Pentagon blacklist of Anthropic - Reuters",
                      source="Google News / Reuters"),
                 item("https://w.test/2", "Federal appeals court rules Pentagon can blacklist Anthropic - WaPo",
                      source="Google News / WaPo"),
                 item("https://o.test/9", "Totally different story about pricing", source="Google News / O")]
        routing = {it["url"]: {"categories": ["安全政策"], "reason": "", "note": ""} for it in items}
        sb = Sandbox(items, routing, digest=digest)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        text = sb.packet("安全政策")
        self.assertIn("共 3 則（2 組）", text)
        self.assertIn("同事件其他報導（1 則", text)
        self.assertIn("**URL：** https://w.test/2", text)
        self.assertIn("**[重大事件]** 法院維持認定", text)
        self.assertIn("  > 段落第一行", text)
        self.assertIn("日報未收錄", text)

    def test_prior_attribution_marked_by_url_and_google_news_id(self):
        gid = "CBMif0FVX3lxTFBCWU40OGxGYUZKQTZvcFNhWTVyemFm"
        att = [{"date": "2026-01-01", "source": "google-news", "category": "人物", "page": "entities/x",
                "item_url": f"https://news.google.com/rss/articles/{gid}MoreTail?oc=5", "item_title": "t"},
               {"date": "2026-01-01", "source": "hacker-news", "category": "功能", "page": "entities/y",
                "item_url": "https://a.test/1", "item_title": "Alpha launches widget"}]
        items, routing = small_case()
        items[1]["summary"] = f'<a href="https://news.google.com/rss/articles/{gid}'
        sb = Sandbox(items, routing, attribution=att)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        text = sb.packet("功能")
        self.assertIn("2026-01-01 已歸因至 entities/y", text)
        self.assertIn("2026-01-01 已歸因至 entities/x", text)


_MAIN_URL = __import__("re").compile(r"^- \*\*URL：\*\* (\S+)", __import__("re").M)
_SEC_URL = __import__("re").compile(r"^    - \*\*URL：\*\* (\S+)", __import__("re").M)


def roles_conflicts(out_dir: Path) -> list[str]:
    """同一 URL 在某份包當主條目（行首 URL）、另一份包當同組其他則（縮排 URL）→ 列出。"""
    main, sec = set(), set()
    for p in out_dir.glob("*.md"):
        if p.stem == "排除":
            continue
        text = p.read_text(encoding="utf-8")
        main |= set(_MAIN_URL.findall(text))
        sec |= set(_SEC_URL.findall(text))
    return sorted(main & sec)


class TestGroupingIsConservative(unittest.TestCase):
    """09-24／09-25 回測抓到的誤併：共用詞（prompt injection、Opus 5.5、companies make、
    cloud session）不得把不同事件併成一組。"""

    def assert_apart(self, a, b):
        groups = mod.group_items([item("https://x.test/a", a), item("https://x.test/b", b)])
        self.assertEqual(len(groups), 2, f"不該併組：{a} ／ {b}")

    def assert_together(self, a, b):
        groups = mod.group_items([item("https://x.test/a", a), item("https://x.test/b", b)])
        self.assertEqual(len(groups), 1, f"應併組：{a} ／ {b}")

    def test_known_false_merges_stay_apart(self):
        self.assert_apart("Claude treating Anthropic's internal instructions as prompt injection",
                          "Salesforce Agentforce Flaw Lets Attackers Steal CRM Data With Zero-Click Prompt Injection")
        self.assert_apart("Anthropic Says Opus 5.5 Costs 40% Less to Run. Claude Subscribers Get About 25% More Room",
                          "If opus 5.5 is basically fable level, what are you still using fable for?")
        self.assert_apart("An 'AI freeze' could make big AI companies bigger and hurt smaller firms",
                          "AI could make more companies worth hacking, Anthropic report suggests - Fortune")
        self.assert_apart("Linear Integration: Assign issues to Claude Code to trigger cloud agent sessions",
                          "Anthropic launches Claude Code cloud sessions and hands out up to $250 in credit")

    def test_same_topic_different_events_stay_apart(self):
        """共用詞全是高頻主題詞（金額、融資、雲端交易、法院裁定、用量上限修正）時不併。"""
        self.assert_apart("Anthropic raises $13 billion in Series F funding round",
                          "OpenAI raises $40 billion in new funding round")
        self.assert_apart("Anthropic signs $11.6 billion cloud computing deal with Akamai",
                          "Microsoft signs $10 billion cloud computing deal with Oracle")
        self.assert_apart("Federal judge rules Pentagon blacklist of Anthropic unlawful",
                          "Federal appeals court rules Pentagon can blacklist Anthropic")
        self.assert_apart("Claude Code 2.1.281 fixes usage limit reset bug",
                          "Claude Code 2.1.283 fixes usage limit display bug")

    def test_same_story_still_merges(self):
        self.assert_together("Federal appeals court rules Pentagon can blacklist Anthropic - The Washington Post",
                             "US appeals court upholds Pentagon's blacklisting of Anthropic - Reuters")
        self.assert_together("Salesforce Agentforce Flaw Lets Attackers Steal CRM Data With Zero-Click Prompt Injection",
                             "Salesforce Agentforce Flaw Enables 0-Click Data Exfiltration via Prompt Injection")

    def test_numbers_and_model_names_are_not_tokens(self):
        self.assertEqual(mod.title_tokens("Opus 5.5 vs GPT-6 Sol: $250 credit, 48,000 files"),
                         {"credit", "files"})

    def test_main_is_highest_score_then_earliest(self):
        g = [item("https://x.test/1", "a", score=0, published="09/25 10:00 UTC"),
             item("https://x.test/2", "b", score=0, published="09/25 08:00 UTC"),
             item("https://x.test/3", "c", score=5, published="09/25 12:00 UTC")]
        self.assertEqual(mod.pick_main(g)["url"], "https://x.test/3")
        self.assertEqual(mod.pick_main(g[:2])["url"], "https://x.test/2")


class TestSecondaryAndCrossPacket(unittest.TestCase):
    TITLES = ("Federal appeals court rules Pentagon can blacklist Anthropic - WaPo",
              "US appeals court upholds Pentagon's blacklisting of Anthropic - Reuters",
              "Appeals court upholds Pentagon blacklist decision against Anthropic - AP")

    def setUp(self):
        items = [item("https://m.test/main", self.TITLES[0], score=100, summary="主條目摘要" + LONG),
                 item("https://s.test/sec", self.TITLES[1], score=0, summary="次條目自己的摘要" + LONG,
                      published="09/25 09:00 UTC"),
                 item("https://p.test/only", self.TITLES[2], score=0, summary="只派商業的那則" + LONG)]
        routing = {"https://m.test/main": {"categories": ["安全政策", "商業"], "reason": "", "note": ""},
                   "https://s.test/sec": {"categories": ["安全政策", "人物"], "reason": "", "note": ""},
                   "https://p.test/only": {"categories": ["人物"], "reason": "", "note": ""}}
        self.sb = Sandbox(items, routing)
        self.addCleanup(self.sb.close)
        rc, out = run(self.sb.argv())
        self.assertEqual(rc, 0, out)

    def test_secondary_has_summary_date_and_also_sent_to(self):
        text = self.sb.packet("安全政策")
        sec = text.split("〔同組〕")[1]
        self.assertIn("**摘要：** 次條目自己的摘要", sec)
        self.assertIn("**日期：** 09/25 09:00 UTC", sec)
        self.assertIn("**同時派給：** 人物", sec)

    def test_main_role_is_global(self):
        people = self.sb.packet("人物")  # 人物包沒有主條目：主條目只派安全政策＋商業
        self.assertIn("主條目不在本包", people)
        self.assertNotIn("\n- **URL：** https://s.test/sec", people)
        self.assertEqual(roles_conflicts(self.sb.dir / "out"), [])


class TestShellTitleEcho(unittest.TestCase):
    def test_summary_that_only_echoes_title_is_shell(self):
        title = "Anthropic Opens Directory Submission Portal for Claude Plugins - Unite.AI"
        echo = "Anthropic Opens Directory Submission Portal for Claude Plugins - Unite.AI Unite.AI"
        self.assertTrue(mod.is_shell(echo, title))
        self.assertFalse(mod.is_shell(LONG + LONG, title))
        items, routing = small_case()
        items[0]["title"], items[0]["summary"] = title, echo
        sb = Sandbox(items, routing)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        self.assertIn("殼層摘要：原料無可讀內文", sb.packet("功能"))


class TestPacketCollectorRoundTrip(unittest.TestCase):
    """收報腳本從包檔取 URL 與標題做對帳：產包端的 URL 行形狀改了，這裡要紅。"""

    def test_collector_reads_every_url_and_title(self):
        spec = importlib.util.spec_from_file_location(
            "collect_reporter_reports", ROOT / "scripts" / "collect_reporter_reports.py")
        col = importlib.util.module_from_spec(spec)
        sys.modules.setdefault("collect_reporter_reports", col)
        spec.loader.exec_module(col)
        items = [item("https://m.test/main", TestSecondaryAndCrossPacket.TITLES[0], score=9),
                 item("https://s.test/sec", TestSecondaryAndCrossPacket.TITLES[1]),
                 item("https://o.test/solo", "Totally unrelated pricing story")]
        routing = {it["url"]: {"categories": ["安全政策"], "reason": "", "note": ""} for it in items}
        sb = Sandbox(items, routing)
        self.addCleanup(sb.close)
        rc, out = run(sb.argv())
        self.assertEqual(rc, 0, out)
        got = col.packet_entries(sb.dir / "out", "安全政策")
        self.assertEqual(got, {"https://m.test/main": TestSecondaryAndCrossPacket.TITLES[0],
                               "https://s.test/sec": TestSecondaryAndCrossPacket.TITLES[1],
                               "https://o.test/solo": "Totally unrelated pricing story"})


BACKTEST_DATES = ("2026-09-24", "2026-09-25", "2026-09-26")
# 2026-09-27 人工逐組確認皆為同一事件的回測結果（組大小，依原料順序）；改聚合規則時這裡要重新人工確認
BACKTEST_EXPECTED = {"2026-09-24": [6], "2026-09-25": [3, 2], "2026-09-26": [12, 2, 3]}


@unittest.skipUnless(all((ROOT / "src" / "gathered_archive" / f"{d}.json").exists() for d in BACKTEST_DATES),
                     "回測原料已逾保留窗")
class TestBacktestThreeDays(unittest.TestCase):
    def test_multi_item_groups_match_audited_result(self):
        last_by_date: dict[str, dict] = {d: {} for d in BACKTEST_DATES}
        for ln in REAL_LOG.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                r = json.loads(ln)
                if r.get("date") in last_by_date:
                    last_by_date[r["date"]][r["url"]] = r
        for d in BACKTEST_DATES:
            items = json.loads((ROOT / "src" / "gathered_archive" / f"{d}.json").read_text(encoding="utf-8"))["items"]
            last = last_by_date[d]
            routed = [it for it in items if it["url"] in last and last[it["url"]]["categories"]]
            sizes = [len(g) for g in mod.group_items(routed) if len(g) > 1]
            self.assertEqual(sizes, BACKTEST_EXPECTED[d], d)


@unittest.skipUnless(REAL_ARCHIVE.exists(), f"{REAL_DATE} 原料已逾保留窗")
class TestRealData0926(unittest.TestCase):
    """以 2026-09-26 真實原料重跑：routing 由當日分類帳最後一行勝出版反推。"""

    @classmethod
    def setUpClass(cls):
        items = json.loads(REAL_ARCHIVE.read_text(encoding="utf-8"))["items"]
        last = {}
        for ln in REAL_LOG.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                r = json.loads(ln)
                if r.get("date") == REAL_DATE:
                    last[r["url"]] = r
        routing = {}
        for it in items:
            r = last[it["url"]]
            v = {"categories": r["categories"], "reason": r["reason"], "note": ""}
            if not r["categories"] and mod.is_shell(mod.clean_summary(it["summary"]), it["title"]):
                v["summary_override"] = r["summary"]
            routing[it["url"]] = v
        cls.tmp = tempfile.TemporaryDirectory()
        d = Path(cls.tmp.name)
        shutil.copy(REAL_LOG, d / "log.jsonl")
        (d / "routing.json").write_text(json.dumps(routing, ensure_ascii=False), encoding="utf-8")
        cls.real_sha = sha(REAL_LOG)
        cls.rc, cls.out = run(["--date", REAL_DATE, "--routing", str(d / "routing.json"),
                               "--out", str(d / "out"), "--log", str(d / "log.jsonl")])
        cls.dir = d / "out"

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exit_zero_and_real_ledger_untouched(self):
        self.assertEqual(self.rc, 0, self.out)
        self.assertEqual(sha(REAL_LOG), self.real_sha)

    def test_category_counts(self):
        expected = {"功能": 10, "社群": 22, "安全政策": 23, "商業": 15, "模型": 4, "人物": 2, "排除": 3}
        for name, n in expected.items():
            head = (self.dir / f"{name}.md").read_text(encoding="utf-8").splitlines()[0]
            self.assertIn(f"共 {n} 則", head, name)

    def test_dc_circuit_event_is_one_group(self):
        text = (self.dir / "安全政策.md").read_text(encoding="utf-8")
        blocks = text.split("\n### ")
        dc = [b for b in blocks if "reuters.com/world/us-appeals-court-declines-block" in b]
        self.assertEqual(len(dc), 1)
        # Ars Technica 那則與其他則只共用高頻詞（court、rules、blacklist），保守規則下獨立成則
        self.assertGreaterEqual(dc[0].count("\n  - 〔同組〕") + 1, 12)

    def test_no_url_is_main_in_one_packet_and_secondary_in_another(self):
        self.assertEqual(roles_conflicts(self.dir), [])

    def test_prior_attribution_flags_known_repeats(self):
        people = (self.dir / "人物.md").read_text(encoding="utf-8")
        axios = next(b for b in people.split("\n### ") if "axios.com" in b)
        self.assertIn("已歸因至 entities/dario-amodei", axios)
        safety = (self.dir / "安全政策.md").read_text(encoding="utf-8")
        tr = next(b for b in safety.split("\n### ") if "techradar.com" in b)
        self.assertIn("2026-09-25 已歸因至 topics/ai-agent-safety", tr)
        biz = (self.dir / "商業.md").read_text(encoding="utf-8")
        self.assertIn("2026-09-25 已歸因至 topics/competitor-landscape", biz)
        feat = (self.dir / "功能.md").read_text(encoding="utf-8")
        ns = next(b for b in feat.split("\n### ") if "newscientist.com" in b)
        self.assertIn("2026-09-25 已歸因至 entities/claude-science", ns)


if __name__ == "__main__":
    unittest.main()
