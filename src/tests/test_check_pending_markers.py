"""Tests for scripts/check_pending_markers.py — 懸置標記語法檢查器。

回填全庫 388 筆舊字樣為新語法前的驗收工具（規格見
`.claude/reporter-rules/page-templates.md`「懸置標記語法」節）。每個測試用一個假
wiki 目錄（`TemporaryDirectory`），呼叫 `check(report, wiki_dir=..., today=...)`
——`check_pending_markers.check()` 明確接受這兩個參數以支援測試，不需 monkeypatch
模組全域。
"""
import json
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_pending_markers")

TODAY = date(2026, 8, 9)


class _WikiCase(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.wiki_dir = Path(self._tmp.name)
        (self.wiki_dir / "topics").mkdir()
        (self.wiki_dir / "entities").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel_path: str, text: str) -> Path:
        p = self.wiki_dir / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def run_check(self, today: date = TODAY):
        report: list[str] = []
        ok = mod.check(report, wiki_dir=self.wiki_dir, today=today)
        return ok, report


class TestValidMarkers(_WikiCase):
    def test_standard_form_passes(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string）"
            "｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))

    def test_table_variant_with_matched_qid_passes(self):
        self.write(
            "topics/example.md",
            "| 議題 | 狀態 |\n"
            "| --- | --- |\n"
            "| 某議題 | ❓ 待查證 ⟨Q-07⟩ |\n\n"
            "**懸置細節**\n"
            "- ⟨Q-07⟩ ❓ **待查證**（標 2026-08-01｜查 CI-workflow、secrets-leak）：僅標題可用\n",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))

    def test_wikilink_probe_pointing_to_existing_page_passes(self):
        self.write("topics/ai-agent-safety.md", "# ai-agent-safety\n")
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[topics/ai-agent-safety]]）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))


class TestFailChecks(_WikiCase):
    def test_probe_hits_stoplist(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 Claude）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        joined = "\n".join(report)
        self.assertIn("過寬詞", joined)

    def test_symbol_kind_mismatch(self):
        self.write(
            "topics/example.md",
            "❓ **查無官方**（標 2026-08-01｜查 issue-1234）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("不一致", "\n".join(report))

    def test_bracket_misplaced_inside_bold(self):
        self.write(
            "topics/example.md",
            "❓ **待查證（標 2026-08-01｜查 issue-1234）**｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("括號誤寫在粗體內", "\n".join(report))

    def test_qid_cell_without_definition(self):
        self.write(
            "topics/example.md",
            "| 議題 | 狀態 |\n"
            "| --- | --- |\n"
            "| 某議題 | ❓ 待查證 ⟨Q-09⟩ |\n",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("無對應的懸置細節定義", "\n".join(report))

    def test_qid_definition_without_cell(self):
        self.write(
            "topics/example.md",
            "**懸置細節**\n"
            "- ⟨Q-09⟩ ❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string）：說明\n",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("有懸置細節定義但無表格短標記引用", "\n".join(report))

    def test_wikilink_probe_target_missing(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 [[entities/nonexistent-page]]）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("指向不存在的頁面", "\n".join(report))

    def test_future_marked_date_fails(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-09-01｜查 issue-1234、version-string）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("未來日期", "\n".join(report))

    def test_review_not_after_marked_fails(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 issue-1234、version-string｜複 2026-08-01）"
            "｜**題目**：內文。",
        )
        ok, report = self.run_check()
        self.assertFalse(ok)
        self.assertIn("未晚於標記日", "\n".join(report))


class TestWarnChecks(_WikiCase):
    def test_overdue_marker_is_warn_not_fail(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-07-01｜查 issue-1234、version-string）｜**題目**：內文。",
        )
        ok, report = self.run_check(today=TODAY)
        self.assertTrue(ok, "\n".join(report))
        self.assertIn("已逾期", "\n".join(report))

    def test_single_short_probe_warns(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-08-01｜查 x1）｜**題目**：內文。",
        )
        ok, report = self.run_check()
        # 探針太短同時觸發 check4 FAIL（長度地板），確認 check7 的 WARN 訊息也出現
        self.assertIn("過短", "\n".join(report))


class TestQueueMode(_WikiCase):
    def test_queue_lists_overdue_sorted_and_capped(self):
        self.write(
            "topics/example.md",
            "❓ **待查證**（標 2026-06-01｜查 issue-1234、version-string）｜**題目A**：內文。\n\n"
            "❓ **待查證**（標 2026-07-20｜查 issue-5678、other-string｜訊 2026-08-01）"
            "｜**題目B**：內文。\n",
        )
        entries = mod._overdue_entries(self.wiki_dir, TODAY)
        self.assertEqual(len(entries), 2)
        # 有訊欄者（題目B）應排在前面，即便逾期天數較短
        self.assertTrue(entries[0][0])


class TestMarkerCountGate(_WikiCase):
    """全庫標記數看守閘（`[加入: 2026-09-06]`）——連續四波「砍表列時把懸置標記溶成
    散文」的機械保命條款。基線檔＝`data/pending-marker-count.json`。"""

    def setUp(self):
        super().setUp()
        self._baseline_dir = TemporaryDirectory()
        self.baseline_path = Path(self._baseline_dir.name) / "pending-marker-count.json"

    def tearDown(self):
        self._baseline_dir.cleanup()
        super().tearDown()

    def run_check(self, today: date = TODAY):
        report: list[str] = []
        ok = mod.check(report, wiki_dir=self.wiki_dir, today=today,
                        marker_baseline_path=self.baseline_path)
        return ok, report

    def _write_marker(self, rel_path: str, marked: str = "2026-08-01"):
        self.write(
            rel_path,
            f"❓ **待查證**（標 {marked}｜查 issue-1234、version-string）｜**題目**：內文。",
        )

    def test_below_baseline_fails_and_names_missing_marker(self):
        """基線 2、現況 1：FAIL 且指名少的那筆（探針字串＋頁面定位）。"""
        self._write_marker("topics/alpha.md")
        entries = mod._marker_fingerprints(self.wiki_dir)
        # 現況先建 2 筆基線，再刪掉一頁只剩 1 筆，模擬「標記被溶成散文」。
        self._write_marker("topics/bravo.md", marked="2026-08-02")
        entries = mod._marker_fingerprints(self.wiki_dir)
        self.baseline_path.write_text(
            json.dumps({"count": 2, "updated": "2026-08-09", "note": "test", "fingerprints": entries}),
            encoding="utf-8",
        )
        (self.wiki_dir / "topics" / "bravo.md").write_text("bravo 頁已無懸置標記。\n", encoding="utf-8")

        ok, report = self.run_check()
        self.assertFalse(ok)
        joined = "\n".join(report)
        self.assertIn("低於基線", joined)
        self.assertIn("基線 2", joined)
        self.assertIn("現況 1", joined)
        self.assertIn("topics/bravo", joined)
        self.assertIn("issue-1234", joined)

    def test_equal_to_baseline_passes(self):
        self._write_marker("topics/alpha.md")
        entries = mod._marker_fingerprints(self.wiki_dir)
        self.baseline_path.write_text(
            json.dumps({"count": 1, "updated": "2026-08-09", "note": "test", "fingerprints": entries}),
            encoding="utf-8",
        )
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))
        self.assertIn("基線 1，未低於", "\n".join(report))

    def test_above_baseline_passes_and_baseline_file_unchanged(self):
        self._write_marker("topics/alpha.md")
        entries = mod._marker_fingerprints(self.wiki_dir)
        original = json.dumps(
            {"count": 1, "updated": "2026-08-01", "note": "test", "fingerprints": entries}
        )
        self.baseline_path.write_text(original, encoding="utf-8")

        self._write_marker("topics/bravo.md", marked="2026-08-05")
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))
        self.assertIn("懸置標記 2 筆", "\n".join(report))
        # check() 本身不改基線檔——只有 --rebuild-count 才能動它。
        self.assertEqual(self.baseline_path.read_text(encoding="utf-8"), original)

    def test_no_baseline_file_does_not_fail(self):
        self._write_marker("topics/alpha.md")
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))
        self.assertIn("尚無基線", "\n".join(report))

    def test_rebuild_without_reason_is_rejected(self):
        """`--rebuild-count` 無 `--reason`：main() 的 CLI 解析層必須拒絕。"""
        self.assertIsNone(mod._rebuild_reason(["--rebuild-count"]))
        self.assertIsNone(mod._rebuild_reason(["--rebuild-count", "--reason"]))
        self.assertIsNone(mod._rebuild_reason(["--rebuild-count", "--reason", "  "]))
        self.assertEqual(
            mod._rebuild_reason(["--rebuild-count", "--reason", "首建基線"]), "首建基線"
        )
        with self.assertRaises(ValueError):
            mod._do_rebuild("", self.wiki_dir, self.baseline_path)

    def test_rebuild_with_reason_writes_baseline_with_current_state(self):
        self._write_marker("topics/alpha.md")
        self._write_marker("topics/bravo.md", marked="2026-08-05")
        data = mod._do_rebuild("首建基線 2026-09-06", self.wiki_dir, self.baseline_path,
                                today=date(2026, 9, 6))
        self.assertEqual(data["count"], 2)
        self.assertEqual(data["note"], "首建基線 2026-09-06")
        self.assertEqual(data["updated"], "2026-09-06")
        self.assertTrue(self.baseline_path.exists())

        # 重建後再跑一次 check()：現況等於新基線，應通過。
        ok, report = self.run_check()
        self.assertTrue(ok, "\n".join(report))


if __name__ == "__main__":
    unittest.main()


NL = chr(10)
_SIG = '❓ **待查證**（標 %s｜查 Electron、桌面應用｜訊 2026-08-20）｜**題**：內文'
_NOSIG = '❓ **待查證**（標 %s｜查 Electron、桌面應用）｜**題**：內文'


class QueueLaneSplitTest(_WikiCase):
    """--queue 兩條分流 + 產消對帳（2026-08-29 加入，同日 review 後補強）。

    初版測試把 15 筆標記全寫進同一頁，於是「Lane B 區段含該頁 slug」在
    **原始 bug 原封復活**（Lane B 改印合併排序前 5 筆）時照樣通過——
    review 的突變 M9 實證此漏。現在有訊／無訊分兩頁，斷言 Lane B 區段
    **不含**有訊頁，飢餓語意才真的被釘住。額度切片（M6/M7）、額度不可
    對調（M3）、產能非名目（P1-5）亦一併補上。
    """

    def _queue(self, today=date(2026, 8, 29), history_path=None):
        import io
        buf = io.StringIO()
        mod.print_queue(buf, wiki_dir=self.wiki_dir, today=today, history_path=history_path)
        return buf.getvalue()

    def _lane_sections(self, out):
        a = out.split("## Lane A")[1].split("## Lane B")[0]
        b = out.split("## Lane B")[1].split("總逾期數")[0]
        return a, b

    def _fill(self, n_sig, n_nosig, marked="2026-08-01"):
        if n_sig:
            self.write("topics/alpha.md", NL.join([_SIG % marked] * n_sig))
        if n_nosig:
            self.write("topics/bravo.md", NL.join([_NOSIG % marked] * n_nosig))

    def test_lane_b_is_not_starved_by_lane_a(self):
        """M9 殺手：Lane B 區段不得混入有訊頁。"""
        self._fill(n_sig=8, n_nosig=7)
        lane_a, lane_b = self._lane_sections(self._queue())
        self.assertIn("bravo", lane_b, "Lane B 必須排得進來")
        self.assertNotIn("alpha", lane_b, "Lane B 不得混入有訊筆（原始 bug 的形狀）")
        self.assertIn("alpha", lane_a)
        self.assertNotIn("bravo", lane_a)

    def test_both_lanes_list_every_item_without_truncation(self):
        """清零制殺手：任何截斷都會讓執行者以為「只要做這幾筆」，隊伍就長回來。"""
        self._fill(n_sig=15, n_nosig=15)
        lane_a, lane_b = self._lane_sections(self._queue())
        self.assertEqual(lane_a.count("alpha"), 15, "Lane A 必須全列")
        self.assertEqual(lane_b.count("bravo"), 15, "Lane B 必須全列")

    def test_target_line_states_clear_to_zero_with_backlog_count(self):
        """目標行是執行者唯一照著做的一行：必須講「清到 0」且帶待清總數。"""
        self._fill(n_sig=3, n_nosig=20)
        out = self._queue()
        self.assertIn("清到 0", out)
        self.assertIn("待清 23 筆", out)

    def test_target_line_says_zero_when_queue_empty(self):
        """佇列空時不得印「清到 0（待清 0 筆）」那種怪句，要能看出是已清空。"""
        out = self._queue()
        self.assertIn("逾期 0", out)
        self.assertNotIn("清到 0（待清", out)

    # ---- 趨勢／歷史子系統（2026-08-29 第二輪 review：N8–N12、N15 全存活，此處補洞）----

    def _hist(self):
        return Path(self._tmp.name) / "hist.csv"

    def test_trend_line_reports_signed_delta_against_previous_snapshot(self):
        """N8 殺手：delta 反號會讓惡化印成改善——報表說謊比報錯更危險。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total,lane_a,lane_b,added_7d" + NL + "2026-08-22,3,2,5,4" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        self.assertIn("趨勢", out)
        self.assertIn("2026-08-22 3 筆", out)
        self.assertIn("今日 7 筆", out)
        self.assertIn("+4", out)

    def test_trend_reads_last_row_not_first(self):
        """N11 殺手。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total,lane_a,lane_b,added_7d" + NL
                     + "2026-08-01,99,0,99,0" + NL + "2026-08-22,3,2,5,4" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        trend = [l for l in out.splitlines() if "趨勢" in l][0]
        self.assertIn("2026-08-22 3 筆", trend)
        self.assertNotIn("2026-08-01", trend)

    def test_same_day_rerun_does_not_become_its_own_baseline(self):
        """P0-6 迴歸：同日重跑若拿今天當基準，趨勢永遠印（0），功能自我抵銷。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        self._queue(history_path=h)          # 第一次寫入今日
        out = self._queue(history_path=h)    # 同日重跑
        self.assertIn("尚無上一輪快照", out, "同日重跑不得以今日為基準，且須明說沒有基準")
        self.assertNotIn("今日 7 筆（", out, "不得捏造一個比較")
        rows = [r for r in h.read_text(encoding="utf-8").splitlines() if r.startswith("2026-08-29")]
        self.assertEqual(len(rows), 1, "同日應 upsert 而非 append")

    def test_history_is_appended_with_expected_columns(self):
        """N10／N12 殺手：不寫檔＝序列永遠只有一列；欄序寫錯＝日後讀出來的是別的數字。"""
        self._fill(n_sig=8, n_nosig=7)
        h = self._hist()
        h.write_text("date,total,lane_a,lane_b,added_7d" + NL + "2026-08-22,7,2,5,4" + NL, encoding="utf-8")
        self._queue(history_path=h)
        lines = [r for r in h.read_text(encoding="utf-8").splitlines() if r]
        self.assertEqual(lines[0], "date,total,lane_a,lane_b,added_7d")
        self.assertEqual(lines[-1], "2026-08-29,15,8,7,0")
        # X1 殺手：既有列必須保留。丟掉的話序列永遠只有一列、prev 恆為 None，
        # 趨勢行永遠不印——P0-6 剛修好的功能會靜默死亡。
        self.assertIn("2026-08-22,7,2,5,4", lines)
        self.assertEqual(len(lines), 3)

    def test_corrupt_history_degrades_to_no_trend_not_wrong_trend(self):
        """N15 殺手：讀壞掉的檔要回 None（不印），不可回一個假基準。"""
        self._fill(n_sig=0, n_nosig=7)
        h = self._hist()
        h.write_text("date,total" + NL + "garbage-row" + NL, encoding="utf-8")
        out = self._queue(history_path=h)
        self.assertIn("尚無上一輪快照", out)
        self.assertNotIn("筆 → 今日", out, "壞檔不得產出一個假基準")

    def test_no_history_path_means_no_file_written(self):
        """print_queue 不傳 history_path 時必須是純函式（測試環境不得留檔）。"""
        self._fill(n_sig=0, n_nosig=7)
        self._queue()
        self.assertFalse(self._hist().exists())

    def test_oldest_overdue_ranks_first_within_lane(self):
        """X4 殺手：排序改升序，Lane B 最舊的那批永遠排在額度外——
        形狀就是「某一類工作結構性零曝光」，也就是這整輪要治的病。"""
        self.write("topics/old.md", _NOSIG % "2026-07-01")     # 逾期最久
        self.write("topics/mid.md", NL.join([_NOSIG % "2026-08-01"] * 5))
        _, lane_b = self._lane_sections(self._queue())
        first = [l for l in lane_b.splitlines() if "topics/" in l][0]
        self.assertIn("topics/old", first, "逾期最久者必須排第一")
        # X3 殺手：帳齡是精確值。標 07-01 → 複 07-15 → today 08-29 = 逾期 45 天
        self.assertIn("逾期 45 天", first)

    def test_closing_action_line_demands_clearing_everything(self):
        """X5 殺手：收尾行動行是操作者唯一照著做的一行，必須要求全清、且數字不可對調。"""
        self._fill(n_sig=3, n_nosig=20)
        out = self._queue()
        self.assertIn("Lane A 3 筆 ＋ Lane B 20 筆", out)
        self.assertIn("全部清掉", out)

    # ---- 清零制：不得有截斷、不得有排空預估（2026-09-20 取代額度制）----

    def test_never_truncates_regardless_of_backlog_size(self):
        """N1–N3 的清零制版：舊制靠「另 N 筆未顯示」截斷，那正是隊伍長不完的機制。"""
        self._fill(n_sig=14, n_nosig=12)
        self.assertNotIn("未顯示", self._queue())

    def test_no_drain_estimate_under_clear_to_zero(self):
        """排空預估在清零制下必然是「1 輪」，印出來只會讓人以為還能分期付款。"""
        self._fill(n_sig=3, n_nosig=20)
        out = self._queue()
        self.assertNotIn("排空", out)

    def test_rate_window_boundary_is_exclusive_and_width_matters(self):
        """M4／M8 殺手：窗口寬度與邊界都要釘死。

        today=08-29、窗口 7 天 → cutoff=08-22，條件為 d > cutoff（不含當日）。
        佈局：08-28 兩筆（內）、08-22 一筆（邊界，不含）、08-09 一筆（窗外）。
        期望 added=2；`>` 改 `>=` 會變 3，窗口改 30 會變 4。
        """
        self.write("topics/win.md", NL.join(
            [_NOSIG % "2026-08-28"] * 2 + [_NOSIG % "2026-08-22"] + [_NOSIG % "2026-08-09"]
        ))
        out = self._queue()
        self.assertIn("近 7 天新增 2 筆", out)

    def test_high_intake_warning_fires_above_threshold(self):
        """待清量異常高時要提醒回頭看標記門檻——但仍要求清零，不得改成調額度。"""
        self._fill(n_sig=0, n_nosig=mod.HIGH_INTAKE_WARN + 5)
        out = self._queue()
        self.assertIn("本輪目標", out)
        self.assertIn("標記門檻", out)
        self.assertIn("清零照做", out)

    def test_high_intake_warning_silent_at_normal_volume(self):
        self._fill(n_sig=0, n_nosig=3)
        out = self._queue()
        self.assertIn("本輪目標", out)
        self.assertNotIn("標記門檻", out)
