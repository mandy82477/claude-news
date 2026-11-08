"""build_web.py 在 Windows 預設主控台編碼（cp950）下不可因 print 失敗而誤報「頁面解析失敗」。

根因（2026-11-08 實測）：build() 的 try 區塊把「解析對照表」和「print 警告」包在一起，
警告文字含 emoji（🛠️）時，print 到 cp950 stdout 拋 UnicodeEncodeError，被 `except Exception`
當成「product matrix 解析失敗」整頁致命——解析器本身沒有任何問題。
同類缺陷：build() 內所有把 wiki 內容印到主控台的 print（WARN 行等）都有同樣風險。

釘的情境：以 PYTHONUTF8=0、PYTHONIOENCODING=cp950 在子程序跑 build()（暫存夾具，警告含 emoji），
必須 exit 0、不得出現「解析失敗」；且從 wiki 內容來的 emoji 以替代字元顯示、不中斷。
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests._helpers import SCRIPTS_DIR
from tests.test_build_web_product_matrix import page

CHILD = r'''
import sys, importlib.util
from pathlib import Path
root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("bw", sys.argv[2])
bw = importlib.util.module_from_spec(spec); sys.modules["bw"] = bw; spec.loader.exec_module(bw)
for k, v in {"ROOT": root, "WIKI_DIR": root / "wiki", "WIKI_ENTITIES": root / "wiki" / "entities",
             "WIKI_TOPICS": root / "wiki" / "topics", "WIKI_RADAR": root / "wiki" / "feature-radar.md",
             "NEWS_DIR": root / "news", "DAILY_DIR": root / "daily", "WEEKLY_DIR": root / "weekly",
             "OUT_JS": root / "web_reader" / "data" / "data.js",
             "OUT_WIKI_DIR": root / "web_reader" / "data" / "wiki",
             "OUT_DIGEST_DIR": root / "web_reader" / "data" / "digest",
             "OUT_WEEKLY_DIR": root / "web_reader" / "data" / "weekly",
             "OUT_SEARCH_INDEX": root / "web_reader" / "data" / "search-index.json"}.items():
    setattr(bw, k, v)
orig = bw.build_matrix_tracking
bw.build_matrix_tracking = lambda *a, **k: ([], ["含 emoji 的警告 \U0001f6e0️ 測試"])
bw.build()
'''


class TestBuildUnderCp950(unittest.TestCase):
    def test_emoji_warning_does_not_become_parse_failure(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for sub in ("wiki/entities", "wiki/topics", "news", "web_reader/data"):
                (root / sub).mkdir(parents=True)
            (root / "wiki" / "index.md").write_text(
                "| [[topics/anthropic-product-matrix]] | 🛠️ 工具/功能 | ongoing | 對照表 |\n", encoding="utf-8")
            (root / "wiki" / "topics" / "anthropic-product-matrix.md").write_text(page(), encoding="utf-8")
            env = {k: v for k, v in os.environ.items() if k not in ("PYTHONUTF8", "PYTHONIOENCODING")}
            env.update({"PYTHONUTF8": "0", "PYTHONIOENCODING": "cp950"})
            r = subprocess.run([sys.executable, "-c", CHILD, str(root), str(SCRIPTS_DIR / "build_web.py")],
                               env=env, capture_output=True, cwd=d)
            out = (r.stdout + r.stderr).decode("cp950", errors="replace")
            self.assertNotIn("解析失敗", out, out[-800:])
            self.assertEqual(r.returncode, 0, out[-800:])


if __name__ == "__main__":
    unittest.main()
