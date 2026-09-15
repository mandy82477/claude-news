"""已沉澱徽章：只認 source_attribution 帳本，不認字串比對。

2026-09-14 事故：徽章原本用「wiki 頁名出現在條目標題/內文」判定，當天 8 個徽章
有 5 個錯——「Claude Code」這個頁名幾乎出現在每一則條目裡，於是沒進 wiki 的條目
被標成已沉澱，進了別頁的條目被指到 claude-code。讀者點下去會落在找不到那條新聞
的頁面。這批測試釘住新判準，防止退回字串比對。
"""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

_spec = importlib.util.spec_from_file_location("build_web", ROOT / "scripts" / "build_web.py")
build_web = importlib.util.module_from_spec(_spec)
sys.modules["build_web"] = build_web
_spec.loader.exec_module(build_web)

DATE = "2026-09-14"
RCE_URL = "https://www.reddit.com/r/artificial/comments/1wfr3vz/x/"
XDA_URL = "https://news.google.com/rss/articles/xda?oc=5"
GENOFFICE_URL = "https://github.com/genspark-ai/genoffice"

PAGES_E = [
    {"id": "claude-code", "name": "Claude Code", "pageType": "entity",
     "lastNewsUpdate": DATE},
]
PAGES_T = [
    {"id": "ai-agent-safety", "name": "AI Agent 安全與可靠性", "pageType": "topic",
     "lastNewsUpdate": DATE},
    {"id": "community-tech-patterns", "name": "Claude Code 社群工作流模式",
     "pageType": "topic", "lastNewsUpdate": DATE},
]


def digest():
    """三則條目都含「Claude Code」字樣——舊的字串比對會把三則全標 claude-code。"""
    return {DATE: {"date": DATE, "topStories": [
        {"title": "GitHub Actions RCE in Claude Code", "url": RCE_URL, "body": ""},
        {"title": "Anthropic analyzed 400,000 Claude Code sessions", "url": XDA_URL,
         "body": "Claude Code 使用 session 分析"},
        {"title": "genspark-ai/genoffice", "url": GENOFFICE_URL,
         "body": "讓 Claude Code 讀寫本機檔案"},
    ]}}


def run(idx):
    d = digest()
    build_web.attach_sedimented_badges(d, PAGES_E, PAGES_T, sediment_idx=idx)
    return {s["title"]: s.get("sedimented") for s in d[DATE]["topStories"]}


class TestSedimentIndex(unittest.TestCase):
    def test_builds_date_url_to_pages(self):
        f = ROOT / "data" / "source_attribution.jsonl"
        idx = build_web.load_sediment_index(f)
        self.assertTrue(idx, "帳本存在時不該建出空索引")
        for key, pages in idx.items():
            self.assertEqual(len(key), 2)
            self.assertIsInstance(pages, list)
            self.assertEqual(len(pages), len(set(pages)), "同一頁不可重複")

    def test_missing_file_gives_empty_index(self):
        self.assertEqual(build_web.load_sediment_index(ROOT / "data" / "nope.jsonl"), {})

    def test_bad_lines_and_non_http_urls_skipped(self, ):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "a.jsonl"
            f.write_text(
                "not json\n"
                '{"date":"D","item_url":"(未附連結)","page":"topics/x"}\n'
                '{"date":"D","page":"topics/y"}\n'
                '{"date":"D","item_url":"https://ok/","page":"topics/z"}\n',
                encoding="utf-8")
            idx = build_web.load_sediment_index(f)
        self.assertEqual(idx, {("D", "https://ok/"): ["topics/z"]})


class TestBadges(unittest.TestCase):
    def test_only_ledger_entries_get_badges(self):
        got = run({(DATE, RCE_URL): ["entities/claude-code"]})
        self.assertEqual(got["GitHub Actions RCE in Claude Code"],
                         [{"id": "claude-code", "pageType": "entity"}])
        # 沒進帳本 → 沒徽章，即使標題含「Claude Code」
        self.assertIsNone(got["Anthropic analyzed 400,000 Claude Code sessions"])
        self.assertIsNone(got["genspark-ai/genoffice"])

    def test_badge_points_at_the_page_that_actually_took_it(self):
        got = run({(DATE, GENOFFICE_URL): ["topics/community-tech-patterns"]})
        self.assertEqual(got["genspark-ai/genoffice"],
                         [{"id": "community-tech-patterns", "pageType": "topic"}])

    def test_one_item_can_have_several_homes(self):
        got = run({(DATE, RCE_URL): ["entities/claude-code", "topics/ai-agent-safety"]})
        self.assertEqual([r["id"] for r in got["GitHub Actions RCE in Claude Code"]],
                         ["claude-code", "ai-agent-safety"])

    def test_no_ledger_for_that_date_means_no_badges(self):
        other = {("2026-01-01", RCE_URL): ["entities/claude-code"]}
        self.assertEqual(set(run(other).values()), {None})

    def test_unknown_page_path_is_dropped_not_crashed(self):
        got = run({(DATE, RCE_URL): ["topics/does-not-exist"]})
        self.assertIsNone(got["GitHub Actions RCE in Claude Code"])

    def test_sedimented_today_still_from_last_news_update(self):
        d = digest()
        build_web.attach_sedimented_badges(d, PAGES_E, PAGES_T, sediment_idx={})
        self.assertEqual({p["id"] for p in d[DATE]["sedimentedToday"]},
                         {"claude-code", "ai-agent-safety", "community-tech-patterns"})


class TestNoStringMatching(unittest.TestCase):
    def test_source_has_no_page_name_substring_match(self):
        src = (ROOT / "scripts" / "build_web.py").read_text(encoding="utf-8")
        start = src.index("def attach_sedimented_badges")
        body = src[start:src.index("\ndef ", start + 10)]
        self.assertNotIn('p["name"] in text', body,
                         "徽章不可退回用頁名做字串比對（2026-09-14 事故）")


if __name__ == "__main__":
    unittest.main()
