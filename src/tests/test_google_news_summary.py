"""Google News RSS description 的可見文字剝離。

description 是一段 HTML（<a href=news.google.com…>標題</a> <font>出版者</font>）。原樣截 200 字元
會留下半截 <a href=…> 標籤：沒有一個字是內容，卻因長度 ≥ enricher 薄摘要門檻而永遠不去抓原文。
2026-09-26 實測：當日 29 則 Google News 經 enricher 後 0 則有可用摘要；改剝標籤後 19 則。
"""
import unittest

from news_aggregator.sources.google_news import _description_summary, _visible_text


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


class TestDescriptionSummary(unittest.TestCase):
    # 真實形狀（2026-09-27 實抓）：<title> 帶「 - 出版者」尾巴，錨文字只有標題，<font> 是出版者
    TITLE = "Anthropic Faces Court Setback on US Supply Chain Risk Label - Bloomberg"
    RAW = ('<a href="https://news.google.com/rss/articles/CBMiabc" target="_blank">'
           'Anthropic Faces Court Setback on US Supply Chain Risk Label</a>&nbsp;&nbsp;<font color="#6f6f6f">Bloomberg</font>')

    def test_title_echo_becomes_empty_so_enricher_fetches_and_shell_gate_still_fires(self):
        self.assertEqual(_description_summary(self.RAW, self.TITLE), "")

    def test_real_description_text_is_kept(self):
        raw = self.RAW + " The appeals court held that the Pentagon's supply-chain designation was within its discretion."
        self.assertTrue(_description_summary(raw, self.TITLE).startswith("Anthropic Faces"))


if __name__ == "__main__":
    unittest.main()
