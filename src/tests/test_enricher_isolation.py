"""trafilatura 子行程隔離：C 層崩潰／逾時只帶走那一篇，母行程記 URL 後保留原摘要。

2026-10-31 GitHub Actions 抓料在 lxml 解析某篇文章時 Segmentation fault（exit 139），
整批 115 筆原料陪葬、當日無日報。這裡用 ctypes 製造真實的記憶體存取違規，
不是 mock 一個例外——要證明的正是「Python 攔不住的崩潰」被隔離在子行程裡。
"""
import logging
import pathlib
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from news_aggregator import enricher  # noqa: E402

_CRASH = "import ctypes\nctypes.string_at(0)\n"            # 真實 SIGSEGV／access violation
_HANG = "import time\ntime.sleep(30)\n"
_ECHO = "import sys\nsys.stdout.buffer.write(b'extracted body')\n"


class ExtractIsolationTest(unittest.TestCase):
    def test_child_segfault_returns_empty_and_logs_url(self):
        with mock.patch.object(enricher, "_CHILD_CODE", _CRASH), \
             self.assertLogs(enricher.logger, level=logging.WARNING) as cm:
            self.assertEqual(enricher._extract_isolated("<html>x</html>", "https://example.test/a"), "")
        self.assertTrue(any("child died" in m and "https://example.test/a" in m for m in cm.output), cm.output)

    def test_child_timeout_returns_empty_and_logs_url(self):
        with mock.patch.object(enricher, "_CHILD_CODE", _HANG), \
             mock.patch.object(enricher, "_EXTRACT_TIMEOUT_S", 1), \
             self.assertLogs(enricher.logger, level=logging.WARNING) as cm:
            self.assertEqual(enricher._extract_isolated("<html>x</html>", "https://example.test/b"), "")
        self.assertTrue(any("timed out" in m and "https://example.test/b" in m for m in cm.output), cm.output)

    def test_child_stdout_roundtrip(self):
        with mock.patch.object(enricher, "_CHILD_CODE", _ECHO):
            self.assertEqual(enricher._extract_isolated("<html>x</html>"), "extracted body")

    @unittest.skipIf(enricher._trafilatura is None, "trafilatura not installed")
    def test_real_trafilatura_in_child(self):
        html = ("<html><body><article><h1>T</h1>"
                + "<p>Claude Code shipped a sandbox fix today. </p>" * 8
                + "</article></body></html>")
        text = enricher._extract_isolated(html, "https://example.test/c")
        self.assertIn("sandbox fix", text)

    def test_fetch_article_routes_through_isolation(self):
        class _Resp:
            status_code = 200
            encoding = "utf-8"
            url = "https://example.test/d"

            def iter_content(self, chunk_size):
                yield b"<html><p>hello</p></html>"

        with mock.patch.object(enricher._session, "get", return_value=_Resp()), \
             mock.patch.object(enricher, "_extract_isolated", return_value="hello") as iso:
            self.assertEqual(enricher._fetch_article("https://example.test/d"), "hello")
        iso.assert_called_once()
        self.assertEqual(iso.call_args.args[1], "https://example.test/d")


if __name__ == "__main__":
    unittest.main()
