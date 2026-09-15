"""GitHub Issues 的快取鍵必須跟著「日報會顯示的內容」走，不能只跟 URL。

2026-09-09 事故：#91870 的 OP 被改寫成「Community Update：數週內出貨、更名 Claude Mods」，
標題也改了。快取只認 URL＋留言數翻倍（107→214），內容質變沒有留言暴增，於是每天重抓、
每天被丟，沒有任何 LLM 看過那段更新，最後靠使用者提問人工補進 wiki。
2026-08 官方文件頁死於同一型（FeedItem.dedup_key 註解），當時只修 score=0 的來源。
"""
import importlib
import sys
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

gi = importlib.import_module("news_aggregator.sources.github_issues")
from news_aggregator.emitted_cache import cache_key, filter_new_or_reignited  # noqa: E402

URL = "https://github.com/anthropics/claude-code/issues/91870"
OLD_TITLE = "Function Hooks - make plugins 10x more powerful"
OLD_BODY = "### Hi folks! ✨\n\n> **AI;DR**: Function Hooks let you modify " + "x" * 400
NEW_TITLE = "Mods - make Claude 10x more extensible"
NEW_BODY = ("# Community Update: Sep 9, 2026\n\n> **AI;DR**: We're shipping in N weeks.\n\n"
            "We're now committed to shipping function hooks ... calling this functionality "
            "\"Claude Mods\"" + OLD_BODY)


class TestContentKey(unittest.TestCase):
    def test_op_rewrite_is_a_new_key(self):
        self.assertNotEqual(gi.content_key(URL, OLD_TITLE, OLD_BODY),
                            gi.content_key(URL, NEW_TITLE, NEW_BODY))

    def test_retitle_alone_is_a_new_key(self):
        self.assertNotEqual(gi.content_key(URL, OLD_TITLE, OLD_BODY),
                            gi.content_key(URL, NEW_TITLE, OLD_BODY))

    def test_edit_past_the_shown_prefix_is_not_a_change(self):
        deep_edit = OLD_BODY[:-5] + "yyyyy"  # 本文尾端，遠在折疊後的 200 字視窗之外
        self.assertEqual(gi.content_key(URL, OLD_TITLE, OLD_BODY),
                         gi.content_key(URL, OLD_TITLE, deep_edit))

    def test_whitespace_reflow_is_not_a_change(self):
        reflowed = OLD_BODY.replace("\n\n", " \n ").replace("  ", " ")
        self.assertEqual(gi.content_key(URL, OLD_TITLE, OLD_BODY),
                         gi.content_key(URL, " " + OLD_TITLE + " ", reflowed))

    def test_key_keeps_url_and_fragment_survives_cache_normalization(self):
        k = gi.content_key(URL, OLD_TITLE, OLD_BODY)
        self.assertTrue(k.startswith(URL + "#"))
        self.assertEqual(cache_key(URL, k), k)

    def test_none_title_and_body_do_not_crash(self):
        self.assertTrue(gi.content_key(URL, None, None).startswith(URL + "#"))


class TestFetchSetsDedupKey(unittest.TestCase):
    def _issue(self, title, body, comments=107):
        now = datetime.now(tz=timezone.utc)
        return {"title": title, "body": body, "html_url": URL, "comments": comments,
                "created_at": (now - timedelta(days=12)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "reactions": {"total_count": 3}}

    def _fetch(self, issue):
        resp = mock.Mock()
        resp.json.return_value = [issue]
        resp.raise_for_status.return_value = None
        with mock.patch.object(gi.requests, "get", return_value=resp):
            return gi.GitHubIssues().fetch()

    def test_fetch_populates_dedup_key_from_shown_content(self):
        items = self._fetch(self._issue(OLD_TITLE, OLD_BODY))
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].dedup_key, gi.content_key(URL, OLD_TITLE, OLD_BODY))

    def test_op_rewrite_survives_the_emitted_cache_without_a_comment_surge(self):
        """事故重演：09-05 已收錄且確認（107 則），09-09 OP 改寫、留言只到 150——必須再進日報。"""
        before = self._fetch(self._issue(OLD_TITLE, OLD_BODY, comments=107))[0]
        kept, cache = filter_new_or_reignited([before], {}, today=date(2026, 9, 5))
        self.assertEqual(len(kept), 1)
        for v in cache.values():
            v["digest_confirmed"] = True

        after = self._fetch(self._issue(NEW_TITLE, NEW_BODY, comments=150))[0]
        kept2, _ = filter_new_or_reignited([after], cache, today=date(2026, 9, 10))
        self.assertEqual([i.title for i in kept2], [NEW_TITLE])

    def test_unchanged_op_is_still_dropped_until_comments_double(self):
        """反向：內容沒變、留言 107→150，仍照 reignite 規則丟掉——修法不能變成每天重發。"""
        before = self._fetch(self._issue(OLD_TITLE, OLD_BODY, comments=107))[0]
        _, cache = filter_new_or_reignited([before], {}, today=date(2026, 9, 5))
        for v in cache.values():
            v["digest_confirmed"] = True
        again = self._fetch(self._issue(OLD_TITLE, OLD_BODY, comments=150))[0]
        kept, _ = filter_new_or_reignited([again], cache, today=date(2026, 9, 10))
        self.assertEqual(kept, [])


if __name__ == "__main__":
    unittest.main()
