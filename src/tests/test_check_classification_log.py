"""分類帳本對帳：每則原料都要有分類或排除理由，缺一則就該 FAIL。

2026-09-15 事故：主編分類時默默漏掉 13 則（其中 2 則是誤判），沒有任何紀錄。
只記「排除」對不了帳——忘了處理和判斷排除在帳上一樣是「沒出現」。
同日兩輪 review 再抓到：逐行驗證與 append-only 互斥（寫錯一次永遠卡死）、URL 打錯
append 也修不掉、exit 2 把逾窗與抓料缺件混為一談、HTML 偵測誤判正當提到標籤的摘要、
真實資料測試從帳本出發抓不到「有原料沒寫帳本」。每一項各釘一個測試。
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "check_classification_log", ROOT / "scripts" / "check_classification_log.py")
mod = importlib.util.module_from_spec(_spec)
sys.modules["check_classification_log"] = mod
_spec.loader.exec_module(mod)

D = "2026-09-14"
A, B, C = "https://a/", "https://b/", "https://c/"
GATHERED = [{"url": A, "title": "A"}, {"url": B, "title": "B"}, {"url": C, "title": "C"}]
OK_SUMMARY = "這是一段足夠長的原文摘要，讓複核記者有內容可以判斷分類是否正確。"
LEDGER_START = "2026-09-14"  # 機制上線前一天的回填；之前的原料檔沒有帳本，不納入真實資料測試


def row(url, cats, reason="", date=D, title="t", summary=OK_SUMMARY):
    return {"date": date, "url": url, "title": title, "summary": summary,
            "categories": cats, "reason": reason}


def good_log():
    return [row(A, ["功能"]), row(B, ["商業", "安全政策"]), row(C, [], "與 Claude 無關")]


class TestBlocking(unittest.TestCase):
    """會讓漏處理躲過對帳的問題才阻斷。"""

    def test_all_accounted_for_passes(self):
        self.assertEqual(mod.reconcile(GATHERED, good_log(), D), [])

    def test_missing_item_is_flagged_as_editor_omission(self):
        log = [row(A, ["功能"]), row(B, ["商業"])]
        problems = mod.reconcile(GATHERED, log, D)
        self.assertEqual(len(problems), 1)
        self.assertIn("主編漏處理", problems[0])
        self.assertIn(C, problems[0])

    def test_excluded_without_reason_fails(self):
        log = [row(A, ["功能"]), row(B, ["商業"]), row(C, [], "")]
        self.assertTrue(any("沒寫理由" in p for p in mod.reconcile(GATHERED, log, D)))

    def test_unknown_category_fails(self):
        log = [row(A, ["功能"]), row(B, ["市場"]), row(C, [], "x")]
        problems = mod.reconcile(GATHERED, log, D)
        self.assertTrue(any("未知類別" in p and "市場" in p for p in problems))

    def test_gathered_item_without_url_is_reported_not_dropped(self):
        gathered = GATHERED + [{"url": "", "title": "空"}, {"title": "沒鍵"}]
        problems = mod.reconcile(gathered, good_log(), D)
        self.assertEqual(sum("缺 URL，無法對帳" in p for p in problems), 2)
        self.assertEqual(mod.summarize(gathered, good_log(), D)["gathered"], 5)


class TestAppendOnlyNeverDeadlocks(unittest.TestCase):
    """任何寫錯都能靠 append 一行修到 exit 0，不必回頭改舊行。"""

    def test_reason_and_category_mistakes_fixed_by_append(self):
        log = [row(A, [], ""), row(B, ["市場"]), row(C, [], "x"),
               row(A, [], "補上理由"), row(B, ["商業"])]
        self.assertEqual(mod.reconcile(GATHERED, log, D), [])

    def test_url_typo_fixed_by_appending_correct_row(self):
        """N-1 B1：URL 貼錯再 append 正確行——打錯那行只警示，不阻斷。"""
        log = [row("https://a-typo/", ["功能"]), row(B, ["商業"]), row(C, [], "x"), row(A, ["功能"])]
        problems, warnings = mod.audit(GATHERED, log, D)
        self.assertEqual(problems, [])
        self.assertTrue(any("a-typo" in w and "不阻斷" in w for w in warnings))

    def test_structurally_broken_rows_are_warnings_not_blockers(self):
        """N-1 A3/A4：非 http URL、categories 非陣列、壞 JSON 行——略過並警示，後行補上即可。"""
        log = [row("htp://a/", ["功能"]), {"date": D, "url": B, "categories": "商業"},
               {"_bad_line": 9, "_bad_date": D},
               row(A, ["功能"]), row(B, ["商業"]), row(C, [], "x")]
        problems, warnings = mod.audit(GATHERED, log, D)
        self.assertEqual(problems, [])
        self.assertEqual(len(warnings), 3)

    def test_later_row_for_same_url_wins_in_stats_too(self):
        log = [row(A, [], "先排除"), row(B, ["商業"]), row(C, [], "x"), row(A, ["功能"], "分類回退自複核")]
        self.assertEqual(mod.reconcile(GATHERED, log, D), [])
        stats = mod.summarize(GATHERED, log, D)
        self.assertEqual((stats["excluded"], stats["by_category"]["功能"], stats["logged"]), (1, 1, 3))


class TestFiltering(unittest.TestCase):
    def test_other_dates_are_ignored(self):
        log = good_log() + [row("https://old/", [], "", date="2026-01-01")]
        self.assertEqual(mod.audit(GATHERED, log, D), ([], []))

    def test_bad_json_line_warns_only_for_its_own_date(self):
        _, w = mod.audit(GATHERED, good_log() + [{"_bad_line": 7, "_bad_date": "2026-01-01"}], D)
        self.assertEqual(w, [])
        _, w = mod.audit(GATHERED, good_log() + [{"_bad_line": 8, "_bad_date": D}], D)
        self.assertTrue(any("第 8 行" in x for x in w))
        _, w = mod.audit(GATHERED, good_log() + [{"_bad_line": 9, "_bad_date": None}], D)
        self.assertTrue(any("第 9 行" in x for x in w))

    def test_load_log_extracts_date_from_broken_line(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "l.jsonl"
            f.write_text('{"date": "2026-01-01", "url": "https://x/", "categories": [\n'
                         + json.dumps(row(A, ["功能"]), ensure_ascii=False) + "\n", encoding="utf-8")
            rows = mod.load_log(f)
        self.assertEqual(rows[0], {"_bad_line": 1, "_bad_date": "2026-01-01"})
        self.assertEqual(rows[1]["url"], A)

    def test_summarize_and_audit_share_filter(self):
        log = good_log() + [row("ftp://x", [], "x"), {"date": D, "url": "https://d/", "categories": "功能"}]
        stats = mod.summarize(GATHERED, log, D)
        self.assertEqual((stats["logged"], stats["excluded"]), (3, 1))
        problems, warnings = mod.audit(GATHERED, log, D)
        self.assertEqual(problems, [])
        self.assertEqual(len(warnings), 2)


class TestExcludedSummaryReadability(unittest.TestCase):
    def test_residue_html_blocks_only_on_excluded_rows(self):
        truncated = '<img alt="Built a cool way to visualize your Claude Code / Codex history" src="https://external-preview.redd.it/eW96'
        log = [row(A, ["功能"], summary=truncated), row(B, ["商業"]),
               row(C, [], "x", summary='<a href="https://news.google.com/rss/..."')]
        problems = mod.reconcile(GATHERED, log, D)
        self.assertEqual(sum("殘留 HTML" in p for p in problems), 1, "只查排除行，已派工的不查")
        log = [row(A, ["功能"]), row(B, ["商業"]), row(C, [], "x", summary=truncated)]
        self.assertTrue(any("殘留 HTML" in p for p in mod.reconcile(GATHERED, log, D)))

    def test_legit_mention_of_tags_is_not_residue(self):
        """N-4：摘要正當談到 <canvas>／<div>，或以 x<y 結尾，不是殘留。"""
        for s in ("作者說要用 <div> 包起來才會生效，否則 <canvas> 不會重繪，這是常見坑。",
                  "Show HN：一個把 <canvas> 動畫錄成 GIF 的工具，效能比 threshold<y 的舊法好。"):
            log = [row(A, ["功能"]), row(B, ["商業"]), row(C, [], "x", summary=s)]
            self.assertEqual(mod.reconcile(GATHERED, log, D), [], s)

    def test_too_short_summary_blocks(self):
        log = [row(A, ["功能"]), row(B, ["商業"]), row(C, [], "x", summary="短")]
        self.assertTrue(any("太短" in p for p in mod.reconcile(GATHERED, log, D)))


class TestCLI(unittest.TestCase):
    def _setup(self, td: Path):
        (td / "arch").mkdir()
        (td / "arch" / f"{D}.json").write_text(json.dumps({"items": GATHERED}), encoding="utf-8")
        log = td / "log.jsonl"
        log.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in good_log()) + "\n",
                       encoding="utf-8")
        return log

    def test_exit_0_and_1(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td); log = self._setup(td)
            args = ["--log", str(log), "--archive-dir", str(td / "arch")]
            self.assertEqual(mod.main(["--date", D, *args]), 0)
            log.write_text(json.dumps(row(A, ["功能"])) + "\n", encoding="utf-8")
            self.assertEqual(mod.main(["--date", D, *args]), 1)

    def test_exit_2_only_when_beyond_retention_window(self):
        """N-2：窗內缺檔＝抓料缺件（3，不得跳過）；逾窗才是 2（可跳過對帳）。"""
        with tempfile.TemporaryDirectory() as td:
            td = Path(td); log = self._setup(td)
            args = ["--log", str(log), "--archive-dir", str(td / "arch")]
            self.assertEqual(mod.main(["--date", "2026-09-13", "--today", "2026-09-15", *args]), 3)
            self.assertEqual(mod.main(["--date", "2026-08-01", "--today", "2026-09-15", *args]), 2)
            (td / "arch" / "2026-09-13.json").write_text("{not json", encoding="utf-8")
            self.assertEqual(mod.main(["--date", "2026-09-13", "--today", "2026-09-15", *args]), 3)
            self.assertEqual(mod.main(["--date", "2026-9-13", *args]), 3)
            # F-2：合格式但不存在的日期不能 traceback 落到 exit 1（那會把人導去翻帳本）
            self.assertEqual(mod.main(["--date", "2026-02-30", *args]), 3)
            self.assertEqual(mod.main(["--date", "2026-13-01", *args]), 3)

    def test_beyond_retention_boundary(self):
        from datetime import date
        today = date(2026, 9, 15)
        self.assertFalse(mod.beyond_retention("2026-09-01", today))  # 剛好 14 天，仍在窗內
        self.assertTrue(mod.beyond_retention("2026-08-31", today))


class TestRealLedger(unittest.TestCase):
    def test_every_ingested_archive_since_ledger_start_reconciles(self):
        """N-5／F-3：從原料出發——保留窗內每個 ≥ 帳本起始日、且 ingest **已完成**的原料檔，
        帳本都必須有該日期且對帳乾淨。從帳本出發掃日期抓不到「有原料卻沒寫帳本」的回歸。

        「已完成」的訊號是 wiki/log.md 有 `## <date> Ingest` 標題——那是 ingest 收尾寫的產物。
        不用 news/<date>.md：日報是 ingest 的輸入，Phase A 就存在，拿它當訊號會在
        日報已產、ingest 未跑完的空窗期把整個套件弄紅、擋住無關 session 收工。"""
        rows = mod.load_log(ROOT / "data" / "classification-log.jsonl")
        dates_in_ledger = {r.get("date") for r in rows}
        log_text = (ROOT / "wiki" / "log.md").read_text(encoding="utf-8")
        candidates = sorted(
            p.stem for p in (ROOT / "src" / "gathered_archive").glob("????-??-??.json")
            if p.stem >= LEDGER_START and f"## {p.stem} Ingest" in log_text)
        if not candidates:
            self.skipTest("保留窗內沒有已完成 ingest 的原料檔可對帳")
        for d in candidates:
            self.assertIn(d, dates_in_ledger, f"{d} 有原料也有日報，但帳本沒有這一天——ingest 沒寫分類紀錄")
            gathered = json.loads((ROOT / "src" / "gathered_archive" / f"{d}.json").read_text(encoding="utf-8")).get("items") or []
            problems = mod.reconcile(gathered, rows, d)
            self.assertEqual(problems, [], f"{d}:\n" + "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
