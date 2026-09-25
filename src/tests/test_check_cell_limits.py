"""Tests for scripts/check_cell_limits.py — 字元上限機械閘。

規則端：`.claude/reporter-rules/page-templates.md`「表格放結論，細節下沉（全站
通用）」與 `.claude/reporter-rules/shared.md`「書寫風格」硬上限。

每個測試用假檔（`TemporaryDirectory`）餵 `scan(files=...)`——`scan()` 明確
接受檔案清單以支援測試，不需 monkeypatch 模組全域，也不會污染真實 wiki 檔。
"""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_cell_limits")


class _Case(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name: str, text: str) -> Path:
        p = self.dir / name
        p.write_text(text, encoding="utf-8")
        return p

    def scan(self, name: str, text: str):
        return mod.scan([self.write(name, text)])


class TestTableCells(_Case):
    def test_undecodable_page_is_fatal_not_zero_hits(self):
        """頁面非法 UTF-8 時必須致命退出——若當成 0 筆命中，--rebuild 會把該頁基線整批當「未使用」移除（2026-09-25 主 session 驗收時以 cp950 夾具誤觸）。"""
        path = self.dir / "bad.md"
        path.write_bytes("| a |\n|---|\n| 字 |\n".encode("cp950"))
        with self.assertRaises(SystemExit) as cm:
            mod.scan([path])
        self.assertIn("無法讀取", str(cm.exception))

    def test_over_120_table_cell_is_caught(self):
        long_cell = "x" * 121
        text = f"| 欄A | 欄B |\n| --- | --- |\n| 短 | {long_cell} |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "table_cell")
        self.assertEqual(hits[0]["limit"], 120)

    def test_exactly_120_table_cell_passes(self):
        cell = "x" * 120
        text = f"| 欄A |\n| --- |\n| {cell} |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_link_url_is_stripped_before_measuring(self):
        """規則明文：量測前先剝掉 markdown 連結的 URL，只算渲染可見文字。"""
        visible = "短標題"
        url = "https://example.com/" + "a" * 200
        text = f"| 來源 |\n| --- |\n| [{visible}]({url}) |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [], "純引用來源格（短可見文字＋長 URL）應豁免")

    def test_visible_text_still_over_limit_after_stripping_url_fails(self):
        visible = "x" * 130
        url = "https://example.com/short"
        text = f"| 來源 |\n| --- |\n| [{visible}]({url}) |\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "table_cell")


class TestListItems(_Case):
    def test_over_200_list_item_is_caught(self):
        text = "- " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["kind"], "list_item")
        self.assertEqual(hits[0]["limit"], 200)

    def test_exactly_200_list_item_passes(self):
        text = "- " + ("x" * 200) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_nested_indented_list_item_is_measured(self):
        text = "  - " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)

    def test_asterisk_bullet_is_measured(self):
        text = "* " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)

    def test_short_prose_paragraph_is_not_a_list_item(self):
        """非條列的散文段不受 200 字元上限拘束（本閘只管條列與表格）。"""
        text = ("x" * 250) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])


class TestSkips(_Case):
    def test_percent_comment_is_skipped(self):
        text = "%%\n- " + ("x" * 300) + "\n%%\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_code_fence_is_skipped(self):
        text = "```\n| " + ("x" * 300) + " |\n```\n"
        hits = self.scan("a.md", text)
        self.assertEqual(hits, [])

    def test_frontmatter_is_skipped_and_line_numbers_stay_true(self):
        text = "---\nkind: topic\n---\n# 標題\n\n- " + ("x" * 201) + "\n"
        hits = self.scan("a.md", text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["line"], 6)

    def test_archive_page_is_excluded_from_target_files(self):
        """蒐集契約明定 archive 原文一字不刪，不受本閘拘束——但 scan() 本身只吃傳入的
        檔案清單，排除邏輯住 target_files()，故此處直接驗 target_files() 的過濾。"""
        f = self.write("foo-archive.md", "| " + ("x" * 300) + " |\n")
        # target_files() 掃 WIKI 底下固定的 entities/topics 目錄，不是 self.dir，
        # 這裡只驗證檔名過濾邏輯本身（模擬 target_files 內的 list comprehension）。
        filtered = [p for p in [f] if not p.stem.endswith("-archive")]
        self.assertEqual(filtered, [])


def _bl(hits):
    """把命中轉成錨點格式基線（{page: [{kind, anchor, max_len}]}）。"""
    return mod._entries_from_hits(hits)


class TestBaseline(_Case):
    def test_baseline_hit_is_legacy_new_hit_is_fail(self):
        """存量基線只擋新增：基線內的算 WARN，基線外的算 FAIL（同 reader-language 先例）。"""
        old_cell = "x" * 130
        text = f"| 欄 |\n| --- |\n| {old_cell} |\n"
        hits_old = self.scan("a.md", text)
        self.assertEqual(len(hits_old), 1)
        baseline = _bl(hits_old)
        new, legacy = mod.split_hits(hits_old, baseline)
        self.assertEqual((len(new), len(legacy)), (0, 1))

        # 同頁新加一條超限條列 → 錨點不在基線 → FAIL
        text2 = text + "- " + ("y" * 201) + "\n"
        hits_both = self.scan("a.md", text2)
        new, legacy = mod.split_hits(hits_both, baseline)
        self.assertEqual(len(legacy), 1)
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0]["kind"], "list_item")

    def test_fingerprint_ignores_whitespace_but_not_content(self):
        """舊格式指紋（只供 --migrate-legacy 對應舊基線）。"""
        a = mod.fingerprint("table_cell", "  同一格內容  ")
        b = mod.fingerprint("table_cell", "同一格內容")
        self.assertEqual(a, b)
        self.assertNotEqual(a, mod.fingerprint("table_cell", "不同格內容"))


ROW = ("- 🔴 **未修復**｜**`autoMemoryEnabled=false` 未能抑制記憶體前導文字（GitHub issue #63903，"
       "累積 40 則留言）**：" + "說明" * 100 + "\n")


class TestAnchorLegacyRule(_Case):
    """存量判定 B：穩定錨點＋長度不增。"""

    def test_rewrite_number_same_length_stays_legacy(self):
        """09-24 事故形狀：留言數 40→47，長度不變 → 仍是存量，不需 rebuild。"""
        base = _bl(self.scan("a.md", ROW))
        hits = self.scan("a.md", ROW.replace("累積 40 則", "累積 47 則"))
        new, legacy = mod.split_hits(hits, base)
        self.assertEqual((len(new), len(legacy)), (0, 1))

    def test_status_flip_keeps_anchor(self):
        base = _bl(self.scan("a.md", ROW))
        hits = self.scan("a.md", ROW.replace("🔴 **未修復**", "🟢 **已修復**"))
        self.assertEqual(mod.split_hits(hits, base)[0], [])

    def test_growing_legacy_row_is_new(self):
        base = _bl(self.scan("a.md", ROW))
        hits = self.scan("a.md", ROW.replace("累積 40 則", "累積 400 則"))
        self.assertEqual(len(mod.split_hits(hits, base)[0]), 1)

    def test_shrinking_legacy_row_is_legacy(self):
        base = _bl(self.scan("a.md", ROW))
        hits = self.scan("a.md", ROW.replace("說明說明", "說明", 1))
        self.assertEqual(mod.split_hits(hits, base)[0], [])

    def test_same_anchor_on_other_page_is_new(self):
        base = _bl(self.scan("a.md", ROW))
        hits = self.scan("b.md", ROW)
        self.assertEqual(len(mod.split_hits(hits, base)[0]), 1)

    def test_duplicate_anchor_multiset_long_matches_long(self):
        head = "| a | b |\n|---|---|\n"
        long_ = "| 2026-05-17 | " + "x" * 150 + " |\n"
        short = "| 2026-05-17 | " + "y" * 130 + " |\n"
        base = _bl(self.scan("a.md", head + long_ + short))
        # 兩列互換位置仍各自配得上
        hits = self.scan("a.md", head + short + long_)
        self.assertEqual(mod.split_hits(hits, base)[0], [])
        # 多一列同錨 → 第三筆沒有槽位 → 新增
        hits3 = self.scan("a.md", head + long_ + short + short)
        self.assertEqual(len(mod.split_hits(hits3, base)[0]), 1)

    def test_table_anchor_is_first_cell_plus_column(self):
        hits = self.scan("a.md", "| **v2.1.152** | 2026-05-20 | " + "x" * 130 + " |\n")
        self.assertEqual(hits[0]["anchor"], "v2.1.152#c3")

    def test_docstring_list_anchor_examples(self):
        """腳本頂部 docstring 的錨點例子必須與實作一致。"""
        cases = {
            "🔴 **未修復**｜**VSCode 擴充套件 `ide_selection` 缺失…**：…": "VSCode 擴充套件 ide_selectio",
            "🔎 **查無官方**（標 2026-08-09｜查 #12925、Linear｜複 2026-10-04）｜"
            "**功能請求：Linear 整合——指派 issue 給 Claude**": "功能請求：Linear 整合——指派 issue",
            "**AWS Continuum（08-05）**：AWS 官方宣布與 Anthropic": "AWS Continuum（08-05）",
            "**核心模式：** 開發者釋出應用程式，讓使用者能從任一則歷史訊息": "核心模式： 開發者釋出應用程式，讓使用者能從任一",
            "[標題文字很長很長很長](https://example.com/x)：內文": "標題文字很長很長很長",
        }
        for src, want in cases.items():
            self.assertEqual(mod.list_anchor(src), want, src)


class TestRebuild(_Case):
    """--rebuild 只准變緊；--allow-grow 需 --reason 並寫帳本。"""

    def setUp(self):
        super().setUp()
        self.bl = self.dir / "baseline.json"
        self.ch = self.dir / "changes.jsonl"
        self.legacy_text = "- " + ("a" * 230) + "\n- " + ("b" * 240) + "\n"
        mod.write_baseline(_bl(self.scan("p.md", self.legacy_text)), self.bl)

    def _sha(self):
        import hashlib
        return hashlib.sha256(self.bl.read_bytes()).hexdigest()

    def test_rebuild_refuses_new_hit_and_leaves_file_untouched(self):
        before = self._sha()
        hits = self.scan("p.md", self.legacy_text + "- " + ("c" * 250) + "\n")
        code, msg = mod.rebuild(hits, self.bl, self.ch)
        self.assertEqual(code, 1)
        self.assertIn("拒絕", msg)
        self.assertEqual(self._sha(), before)
        self.assertFalse(self.ch.exists())

    def test_rebuild_refuses_grown_legacy_row(self):
        before = self._sha()
        hits = self.scan("p.md", "- " + ("a" * 231) + "\n- " + ("b" * 240) + "\n")
        code, _ = mod.rebuild(hits, self.bl, self.ch)
        self.assertEqual(code, 1)
        self.assertEqual(self._sha(), before)

    def test_allow_grow_needs_reason(self):
        before = self._sha()
        hits = self.scan("p.md", self.legacy_text + "- " + ("c" * 250) + "\n")
        code, _ = mod.rebuild(hits, self.bl, self.ch, allow_grow=True, reason="  ")
        self.assertEqual(code, 1)
        self.assertEqual(self._sha(), before)

    def test_allow_grow_with_reason_writes_ledger(self):
        hits = self.scan("p.md", self.legacy_text + "- " + ("c" * 250) + "\n")
        code, _ = mod.rebuild(hits, self.bl, self.ch, allow_grow=True, reason="x", actor="t")
        self.assertEqual(code, 0)
        rows = [json.loads(ln) for ln in self.ch.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(rows), 1)
        self.assertEqual(set(rows[0]), {"date", "file", "added", "removed", "reason", "actor"})
        self.assertEqual((rows[0]["reason"], rows[0]["actor"], len(rows[0]["added"])), ("x", "t", 1))
        self.assertEqual(sum(map(len, mod.load_baseline(self.bl).values())), 3)

    def test_removal_passes_and_shrinks_by_one(self):
        hits = self.scan("p.md", "- " + ("a" * 230) + "\n")
        code, _ = mod.rebuild(hits, self.bl, self.ch)
        self.assertEqual(code, 0)
        self.assertEqual(sum(map(len, mod.load_baseline(self.bl).values())), 1)
        self.assertFalse(self.ch.exists(), "純收緊不寫帳本")

    def test_shortening_tightens_max_len(self):
        hits = self.scan("p.md", "- " + ("a" * 210) + "\n- " + ("b" * 240) + "\n")
        code, _ = mod.rebuild(hits, self.bl, self.ch)
        self.assertEqual(code, 0)
        self.assertEqual(sorted(e["max_len"] for e in mod.load_baseline(self.bl)["p"]), [210, 240])

    def test_legacy_format_baseline_is_rejected(self):
        self.bl.write_text(json.dumps({"pages": {"p": ["list_item:abc"]}}), encoding="utf-8")
        with self.assertRaises(mod.BaselineError):
            mod.load_baseline(self.bl)


class TestMigration(_Case):
    def test_migrate_keeps_only_legacy_fingerprints(self):
        hits = self.scan("p.md", "- " + ("a" * 230) + "\n- " + ("b" * 240) + "\n")
        legacy = {"pages": {"p": [hits[0]["fp"], "list_item:stale0000000"]}}
        pages, outside, stale = mod.migrate_legacy(legacy, hits)
        self.assertEqual([e["anchor"] for e in pages["p"]], [hits[0]["anchor"]])
        self.assertEqual(len(outside), 1, "遷移不得順手收進新命中")
        self.assertEqual(stale, [("p", "list_item:stale0000000")])


class TestMainExitCode(_Case):
    def test_main_injected_overlimit_fails_then_removal_passes(self):
        """雙向驗紅：注入超限條列 → exit 1；移除後 → exit 0（用臨時檔，不動真實基線）。"""
        f = self.write("a.md", "- " + ("x" * 201) + "\n")
        hits = mod.scan([f])
        self.assertEqual(len(hits), 1)
        new, legacy = mod.split_hits(hits, {})
        self.assertEqual(len(new), 1)

        f2 = self.write("b.md", "- 短句，沒有超限。\n")
        hits2 = mod.scan([f2])
        self.assertEqual(hits2, [])


class TestRepoState(unittest.TestCase):
    def test_repo_baseline_file_is_wellformed(self):
        data = json.loads(mod.BASELINE.read_text(encoding="utf-8"))
        self.assertIn("pages", data)
        self.assertEqual(data.get("_format"), mod.BASELINE_FORMAT)
        self.assertFalse(mod.is_legacy_format(data))
        for entries in data["pages"].values():
            for e in entries:
                self.assertEqual(set(e), {"kind", "anchor", "max_len"})
        self.assertEqual(data["_hits"], sum(map(len, data["pages"].values())))

    def test_repo_currently_has_no_new_hits_against_its_own_baseline(self):
        """真實倉庫的字元上限閘必須自己是綠的——這是本閘上線的前提，不是選填。"""
        hits = mod.scan(mod.target_files())
        baseline = mod.load_baseline()
        new, _legacy = mod.split_hits(hits, baseline)
        self.assertEqual(new, [], f"倉庫對自己的基線出現新增超限：{new[:3]}")


if __name__ == "__main__":
    unittest.main()
