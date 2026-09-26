"""enrich() 的「絕不拋錯」契約與讀取總預算。

2026-09-26 本機抓料連續兩次失敗：`as_completed(futures, timeout=60)` 只要有一篇
文章卡住就拋 TimeoutError，而 try/except 只包住 `fut.result()`，例外直接穿出
`enrich()` 讓 `main.py` 崩潰。enrichment 是加值不是必要，一篇卡住不得讓整批原料消失。
"""
import time
import unittest
from unittest import mock

from news_aggregator import enricher
from news_aggregator.sources.base import FeedItem


def _item(url: str) -> FeedItem:
    return FeedItem(title=url, url=url, source="test", published=None, score=0, summary="", category="media")


class TestEnrichBudget(unittest.TestCase):
    def test_hung_item_keeps_original_and_does_not_raise(self):
        """一篇卡住：整批在預算內回來，卡住那篇保留原物件，其餘照常加值。"""
        def fake(item):
            if "hang" in item.url:
                time.sleep(5)
                return item
            return enricher.replace(item, summary="enriched")
        items = [_item("https://a/1"), _item("https://a/hang"), _item("https://a/3")]
        with mock.patch.object(enricher, "_safe_enrich", fake), \
             mock.patch.object(enricher, "_ENRICH_BUDGET_S", 1):
            t0 = time.monotonic()
            out = enricher.enrich(items)
            elapsed = time.monotonic() - t0
        self.assertLess(elapsed, 4, "預算到期就該回來，不等卡住的 worker")
        self.assertEqual([o.summary for o in out], ["enriched", "", "enriched"])
        self.assertIs(out[1], items[1])

    def test_all_finish_fast_unchanged_behaviour(self):
        items = [_item("https://a/1"), _item("https://a/2")]
        with mock.patch.object(enricher, "_safe_enrich",
                               lambda it: enricher.replace(it, summary="x")):
            out = enricher.enrich(items)
        self.assertEqual([o.summary for o in out], ["x", "x"])


class _DripResp:
    url = "https://example.com/slow"
    encoding = "utf-8"

    def __init__(self, n_chunks: int, delay: float):
        self._n, self._d = n_chunks, delay

    def iter_content(self, chunk_size=0):
        for _ in range(self._n):
            time.sleep(self._d)
            yield b"<p>x</p>"


class TestReadDeadline(unittest.TestCase):
    def test_slow_drip_is_abandoned(self):
        """每塊都在 socket timeout 內、總時間卻超過預算的滴流頁面：放棄，回空字串。"""
        with mock.patch.object(enricher, "_READ_DEADLINE_S", 0.2):
            self.assertEqual(enricher._read_capped(_DripResp(n_chunks=10, delay=0.1)), "")

    def test_fast_page_unaffected(self):
        with mock.patch.object(enricher, "_READ_DEADLINE_S", 5):
            self.assertEqual(enricher._read_capped(_DripResp(n_chunks=2, delay=0)),
                             "<p>x</p><p>x</p>")


if __name__ == "__main__":
    unittest.main()
