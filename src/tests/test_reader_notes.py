"""reader_notes.py：派工 prompt 只貼 ⏳ 項的短版，不讓記者整讀 30 KB 收件匣。

釘的情境：只挑 ⏳（✅ 📌 ❌ 與說明區的 ⏳ 字樣不算）、行號對得回原檔、
類別由 wikilink 指向頁的 domain 推、推不出的「未分類」在任何 --category 都印、截字正確。
夾具不含絕對路徑，故不需 `__REPO_ROOT__` 佔位符；wiki 與收件匣都在暫存目錄生成。
"""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from tests._helpers import REPO_ROOT, load_script_module

rn = load_script_module("reader_notes")

LONG = "很長的內容" * 100

NOTES = f"""# 讀者筆記收件匣

**狀態：** ⏳ 待處理 / ✅ 已納入
- `/wiki-weekly-review`（每週）掃描 ⏳ 項目

---

- [✅] 2026-10-07｜🔍 興趣主題｜已處理的 [[topics/community-a]]

- [⏳] 2026-10-01｜🔍 興趣主題｜**社群題** 見 [[topics/community-a|社群頁]] 與 [[entities/biz-b#節]]

- [⏳] 2026-09-30｜🎨 版面｜沒有任何連結的版面建議 {LONG}

- [⏳] 2026-09-29 裁決｜📝 內容修正｜只連到 [[log]] 與 [[topics/not-exist]]
- [📌] 2026-09-28｜📓 雜記｜[[topics/community-a]]
- [⏳] 2026-09-27｜🔍 興趣主題｜商業題 [[wiki/entities/biz-b.md]]
"""


def write(root: Path, rel: str, text: str) -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


class TestReaderNotes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.wiki = root / "wiki"
        write(self.wiki, "topics/community-a.md", '---\ndomain: "🌐 社群"\n---\n')
        write(self.wiki, "entities/biz-b.md", '---\ndomain: "💼 商業"\n---\n')
        self.notes = write(self.wiki, "reader-notes.md", NOTES)

    def run_cli(self, *extra):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = rn.main(["--pending", "--file", str(self.notes), "--wiki-dir", str(self.wiki), *extra])
        return rc, out.getvalue().splitlines(), err.getvalue()

    def test_all_pending_with_line_numbers(self):
        rc, lines, _ = self.run_cli()
        self.assertEqual(rc, 0)
        self.assertIn("⏳ 待處理 4 項", lines[0])
        body = lines[1:]
        self.assertEqual([l.split("｜")[0] for l in body], ["L10", "L12", "L14", "L16"])
        src = self.notes.read_text(encoding="utf-8").splitlines()
        for l in body:
            n = int(l.split("｜")[0][1:])
            self.assertTrue(src[n - 1].startswith("- [⏳]"), l)

    def test_categories_from_wikilinks(self):
        _, lines, _ = self.run_cli()
        self.assertIn("L10｜2026-10-01｜🔍 興趣主題｜[社群、商業] 社群題 見", lines[1])
        self.assertIn("｜[未分類]", lines[2])
        self.assertIn("L14｜2026-09-29 裁決｜📝 內容修正｜[未分類]", lines[3])
        self.assertIn("｜[商業] 商業題", lines[4])

    def test_category_filter_keeps_unclassified(self):
        _, lines, _ = self.run_cli("--category", "商業")
        self.assertEqual([l.split("｜")[0] for l in lines[1:]], ["L10", "L12", "L14", "L16"])
        _, lines, _ = self.run_cli("--category", "社群")
        self.assertEqual([l.split("｜")[0] for l in lines[1:]], ["L10", "L12", "L14"])
        _, lines, _ = self.run_cli("--category", "人物")
        self.assertEqual([l.split("｜")[0] for l in lines[1:]], ["L12", "L14"])
        self.assertIn("人物＋未分類", lines[0])

    def test_brief_truncates_and_strips_bold(self):
        _, lines, _ = self.run_cli("--brief", "20")
        long_line = lines[2]
        content = long_line.split("] ", 1)[1]
        self.assertEqual(len(content), 21)
        self.assertTrue(content.endswith("…"))
        self.assertNotIn("**", lines[1])
        _, lines, _ = self.run_cli()
        self.assertEqual(len(lines[2].split("] ", 1)[1]), rn.DEFAULT_BRIEF + 1)

    def test_bad_inputs(self):
        rc, _, err = self.run_cli("--category", "八卦")
        self.assertEqual(rc, 2)
        rc, _, _ = self.run_cli("--brief", "0")
        self.assertEqual(rc, 2)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            rn.main([])

    def test_no_pending_prints_none(self):
        self.notes.write_text("# 空\n- [✅] 2026-01-01｜🔍｜x\n", encoding="utf-8")
        rc, lines, _ = self.run_cli()
        self.assertEqual(rc, 0)
        self.assertEqual(lines[1:], ["無"])

    def test_real_inbox_parses(self):
        real = REPO_ROOT / "wiki" / "reader-notes.md"
        if not real.exists():
            self.skipTest("無 reader-notes.md")
        text = real.read_text(encoding="utf-8")
        items = rn.pending_items(text, rn.rp.page_categories(REPO_ROOT / "wiki"))
        expected = sum(1 for l in text.splitlines() if l.startswith("- [⏳]"))
        self.assertEqual(len(items), expected)


if __name__ == "__main__":
    unittest.main()
