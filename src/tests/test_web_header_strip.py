"""wiki 詳頁標頭欄位剝除 — app.js `stripHeaderFields()` 的行為契約。

死因（2026-10-23）：模板允許 H1 下先寫一句「這是什麼」再接 `**狀態：**` 等欄位，
舊的剝除 regex 只處理「緊接 H1 的一串欄位行」，那一句一出現，後面全部欄位都
印進正文；當時 10 頁中招（fable-5、anthropic-product-matrix、community-* 子頁）。

做法：從 app.js 抽出該函式原始碼交給 node 跑，測的是真的程式碼而不是抄一份 regex。
沒有 node 的環境跳過（本套件其餘案例不依賴 node）。
"""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_JS = ROOT / "web_reader" / "assets" / "app.js"

HEAD_WITH_SENTENCE = (
    "# Claude Fable 5\n\n"
    "Anthropic 的旗艦模型系列，2026-06-09 發布。\n\n"
    "**類型：** model\n**狀態：** active（現行）\n**領域：** 🤖 模型\n"
    "**別名：** Fable 5, Fable 5.1\n**最後更新：** 2026-10-18\n\n"
    "> **下代傳聞**（2026-10-18）\n> 單一來源稱下週發布。\n\n---\n\n"
    "## 現況\n\n**粗體開頭：** 正文裡這種行不是標頭欄位，要留著。\n"
)
HEAD_PLAIN = (
    "# Claude Code\n\n**類型：** product\n**狀態：** active\n\n---\n\n## 現況\n\n正文。\n"
)


def _extract_fn(js: str) -> str:
    m = re.search(r"\n  function stripHeaderFields\(md\) \{\n.*?\n  \}\n", js, re.S)
    assert m, "app.js 缺 stripHeaderFields()——改名就必須同步本測試"
    return m.group(0)


@unittest.skipUnless(shutil.which("node"), "需要 node 才能執行 app.js 片段")
class TestStripHeaderFields(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fn = _extract_fn(APP_JS.read_text(encoding="utf-8"))

    def run_js(self, md: str) -> str:
        body = md.split("\n", 1)[1]  # renderMarkdownBody 先去掉 H1 行
        script = self.fn + "\nprocess.stdout.write(JSON.stringify(stripHeaderFields(" + json.dumps(body) + ")));"
        out = subprocess.run(["node", "-e", script], capture_output=True, text=True,
                             encoding="utf-8", timeout=20)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def test_sentence_before_fields_keeps_sentence_drops_fields(self):
        got = self.run_js(HEAD_WITH_SENTENCE)
        self.assertTrue(got.startswith("Anthropic 的旗艦模型系列"), got[:80])
        for field in ("**類型：**", "**狀態：**", "**領域：**", "**別名：**", "**最後更新：**"):
            self.assertNotIn(field, got, f"標頭欄位 {field} 漏進正文")
        self.assertIn("> **下代傳聞**", got, "callout 必須保留")
        self.assertIn("## 現況", got)

    def test_bold_colon_line_in_body_is_untouched(self):
        got = self.run_js(HEAD_WITH_SENTENCE)
        self.assertIn("**粗體開頭：** 正文裡這種行不是標頭欄位", got, "標頭區之外的粗體冒號行不得被剝")

    def test_plain_header_still_stripped(self):
        got = self.run_js(HEAD_PLAIN)
        self.assertTrue(got.startswith("---"), got[:40])
        self.assertNotIn("**類型：**", got)

    def test_render_path_uses_the_function(self):
        js = APP_JS.read_text(encoding="utf-8")
        self.assertRegex(js, r"md = stripHeaderFields\(md\);",
                         "renderMarkdownBody 必須經由 stripHeaderFields 剝標頭")


if __name__ == "__main__":
    unittest.main()
