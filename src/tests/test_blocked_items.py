"""被擋條目記錄：dedup／filter／emitted-cache 各層丟條目時要留下 (item, 層, 細節)。

2026-10-04：gathered_archive 只存通過管線的條目，被擋的 40 筆（2026-10-02 funnel
99→59）完全不可考，缺席偵測做不到逐條判斷。各層加 optional `dropped` 出參；
不傳時行為與回傳值不變（既有呼叫端與測試不受影響）。
"""
import unittest
from datetime import date, datetime, timezone

from news_aggregator.dedup import deduplicate
from news_aggregator.emitted_cache import filter_new_or_reignited
from news_aggregator.filter import filter_relevant
from news_aggregator.main import BLOCKED_LAYERS, blocked_record
from news_aggregator.sources.base import FeedItem


def _item(url, title="Some title", source="Hacker News", score=0, category="community"):
    return FeedItem(title=title, url=url, source=source,
                    published=datetime(2026, 10, 2, tzinfo=timezone.utc),
                    score=score, summary="s" * 800, category=category)


class TestDedupDrops(unittest.TestCase):
    def test_url_duplicate_records_loser_and_survivor(self):
        low = _item("https://a.com/x", source="Reddit", score=1)
        high = _item("https://a.com/x/", source="Hacker News", score=9)
        dropped = []
        out = deduplicate([low, high], dropped=dropped)
        self.assertEqual(out, [high])
        self.assertEqual(dropped, [(low, "dedup_url", high.url)])

    def test_title_duplicate_records_layer(self):
        a = _item("https://a.com/1", title="Anthropic ships a new thing today", score=5)
        b = _item("https://b.com/2", title="Anthropic ships a new thing today!", score=1)
        dropped = []
        out = deduplicate([a, b], dropped=dropped)
        self.assertEqual(len(out), 1)
        self.assertEqual([(d[0], d[1]) for d in dropped], [(b, "dedup_title")])

    def test_without_out_param_unchanged(self):
        self.assertEqual(len(deduplicate([_item("https://a.com/x"), _item("https://a.com/x")])), 1)


class TestFilterDrops(unittest.TestCase):
    def test_pr_wire_and_gnews_off_topic(self):
        pr = _item("https://www.prnewswire.com/x", title="Claude thing")
        off = _item("https://news.example/y", title="Generic AI roundup", source="Google News / X")
        ok = _item("https://news.example/z", title="Claude thing", source="Google News / X")
        dropped = []
        out = filter_relevant([pr, off, ok], dropped_out=dropped)
        self.assertEqual(out, [ok])
        self.assertEqual([(d[0], d[1]) for d in dropped], [(pr, "pr_wire"), (off, "gnews_off_topic")])


class TestEmittedCacheDrops(unittest.TestCase):
    def test_confirmed_item_dropped_with_first_emitted(self):
        it = _item("https://a.com/x", score=3)
        cache = {"https://a.com/x": {"first_emitted": "2026-09-30", "last_seen": "2026-10-01",
                                     "score_at_emit": 3, "digest_confirmed": True}}
        dropped = []
        kept, _ = filter_new_or_reignited([it], cache, today=date(2026, 10, 2), dropped=dropped)
        self.assertEqual(kept, [])
        self.assertEqual(dropped, [(it, "emitted_cache", "2026-09-30")])

    def test_new_item_not_recorded(self):
        dropped = []
        kept, _ = filter_new_or_reignited([_item("https://a.com/new")], {}, today=date(2026, 10, 2),
                                          dropped=dropped)
        self.assertEqual(len(kept), 1)
        self.assertEqual(dropped, [])


class TestBlockedRecord(unittest.TestCase):
    def test_record_shape_and_summary_cap(self):
        rec = blocked_record(_item("https://a.com/x"), "emitted_cache", "2026-09-30")
        self.assertEqual(rec["blocked_by"], "emitted_cache")
        self.assertEqual(rec["blocked_detail"], "2026-09-30")
        self.assertEqual(len(rec["summary"]), 500)
        self.assertIn(rec["blocked_by"], BLOCKED_LAYERS)

    def test_every_layer_emitted_by_modules_is_declared(self):
        for layer in ("dedup_url", "dedup_title", "pr_wire", "gnews_off_topic", "emitted_cache", "after_window"):
            self.assertIn(layer, BLOCKED_LAYERS)


if __name__ == "__main__":
    unittest.main()
