"""gathered 原料副本歸檔與保留測試。

副本存在的理由：`gathered_items.json` 不按日分檔、每次抓料直接覆寫，某天日報沒
產出時，那天已經抓到手的原料會在隔天被蓋掉，補跑只能回頭重抓，但來源視窗早已
滾過去 → 該日永久漏失。歸檔讓補跑可以 replay 當天真實原料。
"""
import json
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))

from archive_gathered import archive, prune, annotate  # noqa: E402


class TestArchive(unittest.TestCase):
    def _setup(self, d, stamp="2026-09-26", with_digest=True, with_existing=True):
        src = Path(d) / "gathered_items.json"
        src.write_text(json.dumps({"date": stamp, "items": ["late-1"]}), encoding="utf-8")
        out = Path(d) / "archive"; out.mkdir()
        news = Path(d) / "news"; news.mkdir()
        if with_existing:
            (out / f"{stamp}.json").write_text(json.dumps({"date": stamp, "items": ["morning-1", "morning-2"]}),
                                               encoding="utf-8")
        if with_digest:
            (news / f"{stamp}.md").write_text("# digest", encoding="utf-8")
        return src, out, news

    def test_same_day_regather_after_digest_does_not_overwrite(self):
        """日報已產出、副本已存在：同日較晚的抓料不得覆寫——副本是那天分類帳的原料，
        覆寫後 check_classification_log 對該日永遠對不上（2026-09-26 本機提早跑完、
        GitHub Actions 10:23 UTC 再抓即此情境）。"""
        with TemporaryDirectory() as d:
            src, out, news = self._setup(d)
            self.assertIsNone(archive(src, out, news))
            kept = json.loads((out / "2026-09-26.json").read_text(encoding="utf-8"))["items"]
            self.assertEqual(kept, ["morning-1", "morning-2"])

    def test_digest_exists_but_no_copy_yet_still_archives(self):
        with TemporaryDirectory() as d:
            src, out, news = self._setup(d, with_existing=False)
            self.assertIsNotNone(archive(src, out, news))

    def test_no_digest_yet_overwrites_as_before(self):
        """日報還沒產出時，後一次抓料就是更完整的原料，照舊覆寫。"""
        with TemporaryDirectory() as d:
            src, out, news = self._setup(d, with_digest=False)
            self.assertIsNotNone(archive(src, out, news))
            self.assertEqual(json.loads((out / "2026-09-26.json").read_text(encoding="utf-8"))["items"], ["late-1"])

    def test_archives_under_the_date_inside_the_file(self):
        """檔名取檔案內的 date 欄位，不取系統當下日期——backfill 產生的原料才會
        歸檔到它真正對應的那一天。"""
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text(json.dumps({"date": "2026-07-20", "items": [1, 2]}), encoding="utf-8")
            out = Path(d) / "archive"
            target = archive(src, out)
            self.assertEqual(target.name, "2026-07-20.json")
            self.assertEqual(json.loads(target.read_text(encoding="utf-8"))["items"], [1, 2])

    def test_missing_source_is_not_an_error(self):
        with TemporaryDirectory() as d:
            self.assertIsNone(archive(Path(d) / "nope.json", Path(d) / "archive"))

    def test_malformed_source_is_not_an_error(self):
        """抓料失敗留下半截檔案時，歸檔只能跳過，不能讓整條 pipeline 掛掉。"""
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text("{ this is not json", encoding="utf-8")
            self.assertIsNone(archive(src, Path(d) / "archive"))

    def test_source_without_date_field_is_skipped(self):
        with TemporaryDirectory() as d:
            src = Path(d) / "gathered_items.json"
            src.write_text(json.dumps({"items": []}), encoding="utf-8")
            self.assertIsNone(archive(src, Path(d) / "archive"))


class TestBlockedItems(unittest.TestCase):
    """2026-10-04：副本要含被擋條目與理由，Q2 缺席偵測才能逐條判斷「擋得對嗎」。
    2026-10-02 實測 funnel gathered 99／emitted 59，舊副本正好 59 筆。"""

    def _archive(self, d, payload):
        src = Path(d) / "gathered_items.json"
        src.write_text(json.dumps(payload), encoding="utf-8")
        target = archive(src, Path(d) / "archive")
        return json.loads(target.read_text(encoding="utf-8"))

    def test_blocked_items_kept_with_reason_and_flags(self):
        with TemporaryDirectory() as d:
            out = self._archive(d, {
                "date": "2026-10-02", "article_count": 1,
                "items": [{"url": "u1", "title": "a"}],
                "blocked_items": [
                    {"url": "u2", "title": "b", "blocked_by": "emitted_cache", "blocked_detail": "2026-09-30"},
                    {"url": "u3", "title": "c", "blocked_by": "pr_wire"},
                ],
            })
            self.assertEqual(out["archive_schema"], 2)
            self.assertEqual(out["gathered_total"], 3)
            self.assertEqual([i["url"] for i in out["items"]], ["u1"])
            self.assertTrue(out["items"][0]["emitted"])
            self.assertIsNone(out["items"][0]["blocked_by"])
            self.assertEqual([(b["emitted"], b["blocked_by"]) for b in out["blocked_items"]],
                             [(False, "emitted_cache"), (False, "pr_wire")])
            self.assertEqual(out["blocked_items"][1]["blocked_detail"], "")

    def test_old_format_stays_readable_and_unmarked(self):
        """沒有 blocked_items 的舊格式：items 不變、不偽稱 schema 2（無從得知被擋什麼）。"""
        with TemporaryDirectory() as d:
            out = self._archive(d, {"date": "2026-10-02", "items": [{"url": "u1"}]})
            self.assertNotIn("archive_schema", out)
            self.assertNotIn("blocked_items", out)
            self.assertEqual(out["items"][0]["url"], "u1")

    def test_annotate_does_not_touch_existing_fields(self):
        data = {"date": "x", "items": [{"url": "u", "emitted": True, "score": 5}]}
        self.assertEqual(annotate(data)["items"][0]["score"], 5)

    def test_unreasoned_blocked_item_gets_null_reason(self):
        out = annotate({"items": [], "blocked_items": [{"url": "u"}]})
        self.assertIsNone(out["blocked_items"][0]["blocked_by"])


class TestPrune(unittest.TestCase):
    def test_removes_only_expired_and_ignores_non_date_names(self):
        with TemporaryDirectory() as d:
            p = Path(d)
            # 07-10 與 07-11 是保留天數的兩側邊界：14 天時 cutoff 為 07-11，
            # 所以 07-10 該刪、07-11 該留。少了這一對，RETENTION_DAYS 被改成 15
            # 也不會有人發現（2026-08-29 突變測試實測）。
            for name in ("2026-07-01.json", "2026-07-10.json", "2026-07-11.json",
                         "2026-07-24.json", "readme.json"):
                (p / name).write_text("{}", encoding="utf-8")
            removed = prune(p, today=date(2026, 7, 25))
            self.assertEqual(removed, ["2026-07-01.json", "2026-07-10.json"])
            self.assertTrue((p / "readme.json").exists(), "檔名不是日期就不該被刪")

    def test_missing_dir_is_not_an_error(self):
        with TemporaryDirectory() as d:
            self.assertEqual(prune(Path(d) / "nope", today=date(2026, 7, 25)), [])


if __name__ == "__main__":
    unittest.main()
