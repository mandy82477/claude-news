"""Google News RSS description 的可見文字剝離。

description 是一段 HTML（<a href=news.google.com…>標題</a> <font>出版者</font>）。原樣截 200 字元
會留下半截 <a href=…> 標籤：沒有一個字是內容，卻因長度 ≥ enricher 薄摘要門檻而永遠不去抓原文。
2026-09-26 實測：當日 29 則 Google News 經 enricher 後 0 則有可用摘要；改剝標籤後 19 則。
"""
import unittest

from news_aggregator.sources.google_news import _visible_text


class TestVisibleText(unittest.TestCase):
    def test_anchor_and_font_are_stripped_to_headline_and_publisher(self):
        raw = ('<a href="https://news.google.com/rss/articles/CBMiabc?oc=5" target="_blank">'
               'Court rules Pentagon can blacklist Anthropic - Ars Technica</a>&nbsp;&nbsp;'
               '<font color="#6f6f6f">Ars Technica</font>')
        self.assertEqual(_visible_text(raw), "Court rules Pentagon can blacklist Anthropic - Ars Technica Ars Technica")

    def test_unclosed_truncated_tag_yields_nothing(self):
        """截斷後的半截標籤不算內容——這正是舊行為漏掉的形狀。"""
        self.assertEqual(_visible_text('<a href="https://news.google.com/rss/articles/CBMiqAJBVV95cUxN'), "")

    def test_plain_text_passes_through(self):
        self.assertEqual(_visible_text("  plain   text "), "plain text")


if __name__ == "__main__":
    unittest.main()
