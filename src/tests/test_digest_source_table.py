"""Tests for scripts/digest_source_table.py — 日報檔尾來源表三口徑並列。

守的失敗（2026-10-03 冷讀者對抗輪）：標頭「文章數 59」是候選數，檔尾表「條數」是
原始抓取數（相加 99），同一份檔兩個口徑、沒標明；表上 Reddit 10 條、正文 0 則。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

dst = load_script_module("digest_source_table")
build_web = load_script_module("build_web")

DATA = {
    "date": "2026-10-02",
    "article_count": 4,
    "source_status": {
        "Hacker News": {"ok": True, "count": 14},
        "Reddit": {"ok": True, "count": 10},
        "GitHub": {"ok": True, "count": 10},
        "Blogroll": {"ok": True, "count": 7},
        "Anthropic Blog": {"ok": False, "count": 0},
    },
    "items": [
        {"source": "Hacker News", "url": "https://hn.example/1"},
        {"source": "Reddit / r/ClaudeCode · 週熱門", "url": "https://reddit.example/2"},
        {"source": "GitHub Search", "url": "https://github.example/3"},
        {"source": "Blog / OpenAI News", "url": "https://blog.example/4"},
    ],
}

DIGEST = """# Claude Code & Anthropic 每日新聞摘要

**日期：** 2026-10-02 | **來源：** 4/5 | **文章數：** 4 | **更新時間：** 2026-10-02 17:12 UTC

---

### 💬 技術熱度討論

**[HN 條目](https://hn.example/1)**
說明。
`Hacker News` · 10/02 13:38 UTC

### 📡 來源狀態

> ⚠️ 本日 1 個來源抓取失敗，涵蓋面較平日窄

| 來源 | 狀態 | 條數 |
|------|------|------|
| Hacker News | ✅ | 14 |
| Reddit | ✅ | 10 |
"""


class TestRows(unittest.TestCase):
    def test_candidates_sum_to_article_count(self):
        rows = dst.build_rows(DATA, DIGEST)
        self.assertEqual(sum(r["candidates"] for r in rows), DATA["article_count"])

    def test_prefix_mapping_matches_funnel_rules(self):
        rows = {r["name"]: r for r in dst.build_rows(DATA, DIGEST)}
        self.assertEqual(rows["GitHub"]["candidates"], 1)      # GitHub Search → GitHub
        self.assertEqual(rows["Blogroll"]["candidates"], 1)    # Blog / X → Blogroll
        self.assertEqual(rows["Reddit"]["candidates"], 1)      # Reddit / r/X · 週熱門 → Reddit

    def test_published_counts_only_urls_in_digest(self):
        rows = {r["name"]: r for r in dst.build_rows(DATA, DIGEST)}
        self.assertEqual(rows["Hacker News"]["published"], 1)
        self.assertEqual(rows["Reddit"]["published"], 0)
        self.assertEqual(rows["Reddit"]["gathered"], 10)

    def test_unmapped_source_is_visible_not_dropped(self):
        data = dict(DATA, items=DATA["items"] + [{"source": "Mystery", "url": "u"}], article_count=5)
        rows = dst.build_rows(data, "")
        self.assertEqual(sum(r["candidates"] for r in rows), 5)


class TestRewrite(unittest.TestCase):
    def test_rewrite_keeps_warning_line_and_replaces_table(self):
        table = dst.render_table(dst.build_rows(DATA, DIGEST))
        out = dst.rewrite_digest(DIGEST, table)
        self.assertIn("> ⚠️ 本日 1 個來源抓取失敗", out)
        self.assertIn(dst.TABLE_HEADER, out)
        self.assertNotIn("| 來源 | 狀態 | 條數 |", out)
        self.assertTrue(out.rstrip().endswith(dst.CALIBER_LINE))

    def test_rewrite_is_idempotent(self):
        table = dst.render_table(dst.build_rows(DATA, DIGEST))
        once = dst.rewrite_digest(DIGEST, table)
        self.assertEqual(once, dst.rewrite_digest(once, table))

    def test_rewrite_appends_section_when_missing(self):
        text = DIGEST.split("### 📡")[0]
        out = dst.rewrite_digest(text, dst.render_table(dst.build_rows(DATA, text)))
        self.assertIn(dst.SECTION_HEADING, out)
        self.assertIn(dst.TABLE_HEADER, out)

    def test_build_web_still_reads_raw_gathered_as_count(self):
        """lint 6e 與網站來源列吃第三欄＝原始抓到數；五欄表不得改變它讀到的值。"""
        table = dst.render_table(dst.build_rows(DATA, DIGEST))
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "2026-10-02.md"
            p.write_text(dst.rewrite_digest(DIGEST, table), encoding="utf-8")
            parsed = build_web.parse_digest(p)
        got = {s["name"]: s["count"] for s in parsed["sourceStatus"]}
        self.assertEqual(got["Hacker News"], 14)
        self.assertEqual(got["Reddit"], 10)
        self.assertEqual(parsed["articleCount"], 4)


class TestLoad(unittest.TestCase):
    def test_falls_back_to_archive_when_live_file_is_other_day(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            live = root / "gathered_items.json"
            live.write_text(json.dumps(dict(DATA, date="2026-10-03")), encoding="utf-8")
            arch = root / "archive"
            arch.mkdir()
            (arch / "2026-10-02.json").write_text(json.dumps(DATA), encoding="utf-8")
            self.assertEqual(dst.load_gathered("2026-10-02", live, arch)["date"], "2026-10-02")
            self.assertIsNone(dst.load_gathered("2026-09-01", live, arch))


if __name__ == "__main__":
    unittest.main()
