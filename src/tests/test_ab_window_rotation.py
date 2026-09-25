# -*- coding: utf-8 -*-
"""A/B 窗輪替（2026-09-25）：per_page 放大＋「近 14 天抓過就讓位」閘；C 窗 skills scope。

盲點探針（docs/rules-changelog/news-pipeline-steps.md 2026-09-25）：per_page 8 時 A 窗
90 天前 8 名天天同一批、B 窗升冪永遠是剛過 500 星的同一批，星史近 7 天每日 414 個
repo、聯集只有 438——18 個描述明寫 Claude／skills 的中段 repo 本庫從未看過。
"""
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from news_aggregator.sources import github_releases as gr


class TestConstants(unittest.TestCase):
    def test_per_page_wide_enough_to_rotate(self):
        """8 筆會被前幾名占滿；至少 20 才有中段可輪。"""
        self.assertGreaterEqual(gr.AB_SEARCH_PER_PAGE, 20)

    def test_skills_scope_present_in_inventory_only(self):
        """skills in:name 只進 C 窗（≥3000 星有品質過濾），不進 A/B（100 星帶會被內容型 skill 洗版）。"""
        self.assertIn("skills in:name", gr._INVENTORY_SCOPES)
        self.assertNotIn("skills in:name", gr._REPO_SEARCH_SCOPES)

    def test_inventory_per_day_is_three(self):
        self.assertEqual(gr.INVENTORY_PER_DAY, 3)

    def test_recent_gate_matches_archive_retention(self):
        self.assertEqual(gr.RECENTLY_GATHERED_DAYS, 14)


class TestWindowSkipGate(unittest.TestCase):
    def test_emitted_blocks(self):
        self.assertTrue(gr._window_should_skip("https://github.com/a/b", {"https://github.com/a/b"}, set()))

    def test_recently_gathered_blocks_even_if_not_in_digest(self):
        """被日報選材篩掉的 repo 也不能明天再占位——這是本閘存在的理由。"""
        self.assertTrue(gr._window_should_skip("https://github.com/a/b", set(), {"https://github.com/a/b"}))

    def test_fresh_repo_passes(self):
        self.assertFalse(gr._window_should_skip("https://github.com/a/new", {"https://github.com/a/b"}, {"https://github.com/c/d"}))

    def test_emitted_none_falls_back_to_recent_gate_only(self):
        self.assertFalse(gr._window_should_skip("https://github.com/a/b", None, set()))
        self.assertTrue(gr._window_should_skip("https://github.com/a/b", None, {"https://github.com/a/b"}))


class TestRecentlyGatheredReader(unittest.TestCase):
    def _write(self, adir: Path, day: str, urls):
        (adir / f"{day}.json").write_text(
            json.dumps({"date": day, "items": [{"url": u, "title": u} for u in urls]}), encoding="utf-8")

    def test_reads_recent_files_only_lowercased_and_normalized(self):
        now = datetime(2026, 9, 25, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as td:
            adir = Path(td)
            self._write(adir, "2026-09-24", ["https://github.com/Foo/Bar/", "https://example.com/x"])
            self._write(adir, "2026-09-01", ["https://github.com/old/one"])  # 24 天前，超出 14 天
            got = gr._recently_gathered_repo_urls(now, days=14, archive_dir=adir)
        self.assertEqual(got, {"https://github.com/foo/bar"})

    def test_missing_dir_and_bad_file_return_empty_not_none(self):
        """閘的失效模式是「不讓位」，不是「不吐」——回空集合，絕不回 None 或拋錯。"""
        now = datetime(2026, 9, 25, tzinfo=timezone.utc)
        self.assertEqual(gr._recently_gathered_repo_urls(now, archive_dir=Path("/definitely/not/here")), set())
        with tempfile.TemporaryDirectory() as td:
            adir = Path(td)
            (adir / "2026-09-24.json").write_text("{not json", encoding="utf-8")
            self._write(adir, "2026-09-23", ["https://github.com/ok/repo"])
            self.assertEqual(gr._recently_gathered_repo_urls(now, days=14, archive_dir=adir), {"https://github.com/ok/repo"})

    def test_repo_url_regex_ignores_subpaths_beyond_repo(self):
        m = gr._GH_REPO_URL_RE.match("https://github.com/a/b/issues/3")
        self.assertEqual(m.group(0), "https://github.com/a/b")


if __name__ == "__main__":
    unittest.main()
