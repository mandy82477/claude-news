"""reporter_pages.py：記者認領清單改讀頁面 domain，不再整讀 index。

釘的情境：子頁不入 index 也要被認領、沒有 frontmatter 的頁退回讀 `**領域：**`、
領域文字含表情符號變體、對不到類別的頁要被點名而不是悄悄消失、真庫與 index 領域欄口徑一致。
"""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from tests._helpers import REPO_ROOT, load_script_module

rp = load_script_module("reporter_pages")
ph = load_script_module("pending_handoffs")


def write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="")


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = rp.main(argv)
    return rc, out.getvalue(), err.getvalue()


class TestReporterPages(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        w = self.wiki = Path(self.tmp.name)
        write(w, "topics/community-a.md", '---\r\ntype: "topic"\r\ndomain: "🌐 社群"\r\n---\r\n# A\r\n')
        write(w, "topics/community-a/child.md", '---\ndomain: "🌐 社群"\nparent: "topics/community-a"\n---\n# child\n')
        write(w, "entities/anthropic-x.md", '---\ndomain: "🏛️ 政策/安全"\n---\n# X\n')
        write(w, "entities/tool-y.md", "# Y\n\n**領域：** 🛠️ 工具/功能\n")
        write(w, "topics/guide.md", '---\ndomain: "💻 開發實務"\n---\n')
        write(w, "topics/odd.md", '---\ndomain: "🧪 實驗"\n---\n')
        write(w, "log.md", "# log\n**領域：** 🌐 社群\n")  # 根目錄頁不在認領範圍

    def test_category_lists_subpages_and_crlf_pages(self):
        rc, out, _ = run(["--category", "社群", "--wiki-dir", str(self.wiki)])
        self.assertEqual(rc, 0)
        self.assertEqual(out.splitlines(), ["wiki/topics/community-a.md", "wiki/topics/community-a/child.md"])

    def test_body_domain_fallback_and_variation_selector(self):
        cats = rp.page_categories(self.wiki)
        self.assertEqual(cats["entities/tool-y"], "功能")
        self.assertEqual(cats["entities/anthropic-x"], "安全政策")
        self.assertEqual(cats["topics/guide"], "開發實務")
        self.assertNotIn("log", cats)

    def test_all_counts_and_names_unclassified(self):
        rc, out, _ = run(["--all", "--wiki-dir", str(self.wiki)])
        self.assertEqual(rc, 0)
        lines = out.splitlines()
        self.assertIn("社群\t2", lines)
        self.assertIn("模型\t0", lines)
        self.assertIn("未分類\t1", lines)
        self.assertIn("合計\t6", lines)
        self.assertIn("  未分類：wiki/topics/odd.md", lines)

    def test_stdout_has_no_carriage_return(self):
        # Windows 文字模式會寫出 CRLF；shell 的 $(...) 只去掉最後的換行，其餘路徑尾巴留下 \r
        import subprocess
        import sys
        r = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "reporter_pages.py"), "--category", "安全政策"],
            capture_output=True, cwd=REPO_ROOT)
        self.assertEqual(r.returncode, 0)
        self.assertTrue(r.stdout.strip())
        self.assertNotIn(b"\r", r.stdout)

    def test_unknown_category_exit_2(self):
        rc, out, err = run(["--category", "八卦", "--wiki-dir", str(self.wiki)])
        self.assertEqual(rc, 2)
        self.assertEqual(out, "")
        self.assertIn("社群", err)

    def test_requires_a_mode(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            rp.main([])


class TestRealWikiAgreesWithIndex(unittest.TestCase):
    """frontmatter 口徑必須和 index 領域欄一致，否則改用本腳本會讓記者認領的頁變了。"""

    def test_every_index_row_same_category(self):
        idx = ph.index_owners(REPO_ROOT / "wiki" / "index.md")
        cats = rp.page_categories(REPO_ROOT / "wiki")
        if not idx:
            self.skipTest("wiki/index.md 無領域表")
        diffs = {p: (c, cats.get(p)) for p, c in idx.items() if cats.get(p) != c}
        self.assertEqual(diffs, {}, "index 領域欄 vs 頁面 domain 不一致（index, frontmatter）")


if __name__ == "__main__":
    unittest.main()
