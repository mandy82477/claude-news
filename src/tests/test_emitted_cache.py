import unittest
from datetime import date, datetime, timedelta, timezone

from news_aggregator.emitted_cache import (
    CACHE_TTL_DAYS, confirm_digest, filter_new_or_reignited, prune_expired,
)
from news_aggregator.sources.base import FeedItem

TODAY = date(2026, 7, 14)


def _item(url="https://example.com/a", score=10, score_unit="分"):
    return FeedItem(
        title="t", url=url, source="Hacker News",
        published=datetime(2026, 7, 14, tzinfo=timezone.utc),
        score=score, summary="", category="community", score_unit=score_unit,
    )


class TestUnconfirmedTreatedAsNew(unittest.TestCase):
    """Regression test for the 2026-07-13 GH Actions blackhole: a gather-only
    run that never reaches a confirmed digest must not permanently suppress
    its items."""

    def test_first_seen_is_kept_and_left_unconfirmed(self):
        kept, cache = filter_new_or_reignited([_item()], {}, today=TODAY)
        self.assertEqual(len(kept), 1)
        self.assertFalse(cache["https://example.com/a"]["digest_confirmed"])

    def test_unconfirmed_entry_is_kept_again_next_run(self):
        # Simulates: gather-only ran once (item cached but never confirmed
        # because the digest build that should have followed never happened).
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        # A later run re-fetches the same unchanged item.
        kept, cache2 = filter_new_or_reignited([_item(score=10)], cache, today=TODAY)
        self.assertEqual(len(kept), 1, "unconfirmed item must not be silently dropped")
        self.assertFalse(cache2["https://example.com/a"]["digest_confirmed"])

    def test_confirmed_entry_without_reignition_is_dropped(self):
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        cache = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        kept, _ = filter_new_or_reignited([_item(score=10)], cache, today=TODAY)
        self.assertEqual(kept, [])

    def test_confirmed_entry_with_reignition_is_kept(self):
        _, cache = filter_new_or_reignited([_item(score=10)], {}, today=TODAY)
        cache = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        kept, cache2 = filter_new_or_reignited([_item(score=30)], cache, today=TODAY)
        self.assertEqual(len(kept), 1)
        # Reignited entries reset to unconfirmed pending the next confirm-digest call.
        self.assertFalse(cache2["https://example.com/a"]["digest_confirmed"])

    def test_zero_score_source_never_reignites_but_stays_recoverable_while_unconfirmed(self):
        # Blogroll items are always score=0, so they can never satisfy the
        # reignite threshold — the only thing that can save them from being
        # a permanent blackhole once confirmed is never re-emitting them
        # again unconfirmed, which is exactly what should NOT happen here
        # (they're never confirmed in this test, so they keep coming back).
        item = _item(url="https://blog.example/post", score=0, score_unit="")
        _, cache = filter_new_or_reignited([item], {}, today=TODAY)
        kept, _ = filter_new_or_reignited([item], cache, today=TODAY)
        self.assertEqual(len(kept), 1)


class TestConfirmDigest(unittest.TestCase):
    def test_confirms_known_entry_preserving_first_emitted(self):
        cache = {"https://example.com/a": {
            "first_emitted": "2026-07-01", "score_at_emit": 5, "digest_confirmed": False,
        }}
        updated = confirm_digest(cache, ["https://example.com/a"], today=TODAY)
        entry = updated["https://example.com/a"]
        self.assertTrue(entry["digest_confirmed"])
        self.assertEqual(entry["first_emitted"], "2026-07-01")

    def test_confirms_unknown_url_by_adding_it_fresh(self):
        updated = confirm_digest({}, ["https://example.com/new"], today=TODAY)
        entry = updated["https://example.com/new"]
        self.assertTrue(entry["digest_confirmed"])
        self.assertEqual(entry["first_emitted"], TODAY.isoformat())


ISSUE = "https://github.com/anthropics/claude-code/issues/6235"


def _issue(content_hash="aaa", score=400, url=ISSUE):
    """A GitHub issue as the source emits it: content key, cumulative comment count."""
    return FeedItem(
        title="Feature Request: Support AGENTS.md.", url=url,
        source="GitHub Issues / claude-code",
        published=datetime(2026, 9, 1, tzinfo=timezone.utc),
        score=score, summary="", category="community", score_unit="留言",
        dedup_key=f"{url}#{content_hash}",
    )


def _run(item, cache, day):
    """One daily gather + confirmed digest, pruned the way main() does."""
    cache = prune_expired(cache, today=day)
    kept, cache = filter_new_or_reignited([item], cache, today=day)
    if kept:
        cache = confirm_digest(cache, [{"url": item.url, "dedup_key": item.dedup_key}], today=day)
    return kept, cache


class TestEvergreenIssueDoesNotResurface(unittest.TestCase):
    """2026-09-25 事故：TTL 依 first_emitted 算，天天被 updated_at 抓回的老 issue
    第 15 天過期、被當新條目重登——#6235 七月以來上了 11 次日報、約兩週一次。"""

    def test_issue_fetched_daily_is_emitted_once_across_a_month(self):
        cache, shown = {}, []
        for d in range(30):
            day = date(2026, 9, 1) + timedelta(days=d)
            kept, cache = _run(_issue(score=400 + d), cache, day)
            shown += [day] * len(kept)
        self.assertEqual(shown, [date(2026, 9, 1)])

    def test_issue_that_stops_being_fetched_still_expires(self):
        _, cache = _run(_issue(), {}, date(2026, 9, 1))
        cache = prune_expired(cache, today=date(2026, 9, 1) + timedelta(days=CACHE_TTL_DAYS + 1))
        self.assertEqual(cache, {})

    def test_confirm_digest_keeps_last_seen(self):
        _, cache = filter_new_or_reignited([_issue()], {}, today=TODAY)
        cache = confirm_digest(cache, [{"url": ISSUE, "dedup_key": f"{ISSUE}#aaa"}], today=TODAY)
        self.assertEqual(cache[f"{ISSUE}#aaa"]["last_seen"], TODAY.isoformat())


class TestBareUrlEntryStandsInForContentKey(unittest.TestCase):
    """2026-09-15 改為內容雜湊鍵時，舊裸 URL 條目對不上新鍵，09-16 一天重登 10 個老 issue。"""

    def _bare(self, score_at_emit=394):
        return {ISSUE: {"first_emitted": "2026-09-13", "score_at_emit": score_at_emit,
                        "digest_confirmed": True}}

    def test_issue_with_only_a_bare_entry_is_not_re_emitted(self):
        kept, cache = filter_new_or_reignited([_issue(score=396)], self._bare(), today=TODAY)
        self.assertEqual(kept, [])
        self.assertTrue(cache[f"{ISSUE}#aaa"]["digest_confirmed"], "content key adopted as the same item")

    def test_bare_entry_still_allows_a_real_reignition(self):
        kept, _ = filter_new_or_reignited([_issue(score=800)], self._bare(), today=TODAY)
        self.assertEqual(len(kept), 1)

    def test_seeded_entry_without_score_never_reignites_and_learns_the_score(self):
        kept, cache = filter_new_or_reignited([_issue(score=5000)], self._bare(None), today=TODAY)
        self.assertEqual(kept, [])
        self.assertEqual(cache[f"{ISSUE}#aaa"]["score_at_emit"], 5000)

    def test_changed_content_hash_still_goes_through(self):
        _, cache = _run(_issue("aaa"), {}, TODAY)
        kept, _ = filter_new_or_reignited([_issue("bbb")], cache, today=TODAY)
        self.assertEqual(len(kept), 1, "an OP rewrite is news (fb0c3e1b) and must not be blocked")

    def test_non_refetched_sources_ignore_bare_entries(self):
        """官方文件變更偵測只在內容真的變了才送來，裸 URL 舊條目不得擋下。"""
        docs = FeedItem(title="官方文件更新", url=ISSUE, source="Official Docs",
                        published=datetime(2026, 9, 1, tzinfo=timezone.utc), score=0,
                        summary="", category="official", score_unit="", dedup_key=f"{ISSUE}#ccc")
        kept, _ = filter_new_or_reignited([docs], self._bare(), today=TODAY)
        self.assertEqual(len(kept), 1)


if __name__ == "__main__":
    unittest.main()
