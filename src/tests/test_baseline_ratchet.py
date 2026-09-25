"""存量基線棘輪：基線只准變緊。

看守三份基線（對照 HEAD 版，不是 HEAD~1——雲端有中途 commit，HEAD~1 不一定是前一天）：

- `data/cell-limit-baseline.json`：新基線條目配 HEAD 版條目（同頁同類型同錨點、
  max_len 不增），配不上的＝增長。
- `data/reader-language-baseline.json`：（頁, 指紋）集合差。
- `data/pending-legacy-baseline.json`：`max_legacy` 數值不得調高。

增長必須在 `data/baseline-changes.jsonl` 有**本次未 commit 的新行**登記（file 對得上、
reason 非空、added 列出該條目），否則紅並點名。

為什麼比集合差、不比總數：98a3b59e（928→924）與 8cca5fb0（924→915）兩次都是
「總數下降但新增指紋」——總數測法一次都抓不到。
"""
import json
import subprocess
import unittest
from collections import Counter

from tests._helpers import REPO_ROOT, load_script_module

cl = load_script_module("check_cell_limits")

CELL = "data/cell-limit-baseline.json"
READER = "data/reader-language-baseline.json"
LEGACY = "data/pending-legacy-baseline.json"
LEDGER = "data/baseline-changes.jsonl"


# ── git 讀取 ────────────────────────────────────────────────────────────────

class _NoGit(Exception):
    pass


def git_show(rev: str, path: str) -> str | None:
    """`git show rev:path`；檔案不在該版 → None；git 不可用或 rev 不存在 → _NoGit。"""
    try:
        r = subprocess.run(["git", "-C", str(REPO_ROOT), "cat-file", "-e", rev],
                           capture_output=True)
    except FileNotFoundError as e:
        raise _NoGit(str(e)) from e
    if r.returncode != 0:
        raise _NoGit(f"rev {rev} 不存在（shallow clone？）")
    r = subprocess.run(["git", "-C", str(REPO_ROOT), "show", f"{rev}:{path}"],
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")


def working(path: str) -> str | None:
    p = REPO_ROOT / path
    return p.read_text(encoding="utf-8") if p.exists() else None


# ── 帳本 ────────────────────────────────────────────────────────────────────

def new_ledger_rows(head_text: str | None, cur_text: str | None) -> list[dict]:
    """帳本裡 HEAD 之後新增的行（append-only；前綴不符時退回多重集合差）。"""
    head = [ln for ln in (head_text or "").splitlines() if ln.strip()]
    cur = [ln for ln in (cur_text or "").splitlines() if ln.strip()]
    if cur[:len(head)] == head:
        fresh = cur[len(head):]
    else:
        fresh = list((Counter(cur) - Counter(head)).elements())
    rows = []
    for ln in fresh:
        try:
            rows.append(json.loads(ln))
        except json.JSONDecodeError:
            continue
    return [r for r in rows if str(r.get("reason", "")).strip()]


def _ledger_added(rows: list[dict], file: str) -> list[dict]:
    return [a for r in rows if r.get("file") == file for a in r.get("added", [])]


# ── 三種基線的增長判定 ──────────────────────────────────────────────────────

def cell_growth(old_pages: dict, new_pages: dict, ledger_rows: list[dict]) -> list[dict]:
    grown = cl.baseline_growth(old_pages, new_pages)
    ok = _ledger_added(ledger_rows, CELL)
    return [g for g in grown if not any(
        a.get("page") == g["page"] and a.get("kind") == g["kind"]
        and a.get("anchor") == g["anchor"] and a.get("max_len", -1) >= g["max_len"]
        for a in ok)]


def set_growth(old_pages: dict, new_pages: dict, ledger_rows: list[dict], file: str) -> list[tuple]:
    old = {(p, fp) for p, fps in old_pages.items() for fp in fps}
    new = {(p, fp) for p, fps in new_pages.items() for fp in fps}
    ok = {(a.get("page"), a.get("fp")) for a in _ledger_added(ledger_rows, file)}
    return sorted(new - old - ok)


def count_growth(old: dict, new: dict, ledger_rows: list[dict]) -> int | None:
    """max_legacy 調高且帳本未登記 → 回傳新值；否則 None。"""
    o, n = old.get("max_legacy", 0), new.get("max_legacy", 0)
    if n <= o:
        return None
    if any(a.get("max_legacy", -1) >= n for a in _ledger_added(ledger_rows, LEGACY)):
        return None
    return n


def _fmt(items) -> str:
    return "\n".join(f"  {i}" for i in items[:20])


# ── 真實倉庫對 HEAD ─────────────────────────────────────────────────────────

class TestRepoAgainstHead(unittest.TestCase):
    def setUp(self):
        try:
            self.ledger = new_ledger_rows(git_show("HEAD", LEDGER), working(LEDGER))
        except _NoGit as e:
            self.skipTest(f"git 不可用：{e}")

    def test_cell_limit_baseline_only_tightens(self):
        head_text = git_show("HEAD", CELL)
        cur = json.loads(working(CELL))
        new_pages = cur["pages"]
        head = json.loads(head_text) if head_text else {"pages": {}}
        if cl.is_legacy_format(head):
            # 過渡期（遷移尚未 commit）：以 HEAD 舊指紋基線配現況命中，推回「HEAD 應遷移出的
            # 錨點基線」當對照。遷移 commit 之後此分支不再走到。
            old_pages, _, _ = cl.migrate_legacy(head, cl.scan(cl.target_files()))
        else:
            old_pages = head["pages"]
        grown = cell_growth(old_pages, new_pages, self.ledger)
        self.assertEqual(grown, [], f"{CELL} 相對 HEAD 新增（或放寬）條目，且 {LEDGER} 未登記理由：\n"
                                    f"{_fmt(grown)}\n基線只准變緊；確屬例外須 --rebuild --allow-grow --reason")

    def test_reader_language_baseline_only_tightens(self):
        head_text = git_show("HEAD", READER)
        old = json.loads(head_text)["pages"] if head_text else {}
        new = json.loads(working(READER))["pages"]
        grown = set_growth(old, new, self.ledger, READER)
        self.assertEqual(grown, [], f"{READER} 相對 HEAD 新增指紋，且 {LEDGER} 未登記理由：\n{_fmt(grown)}")

    def test_pending_legacy_max_only_decreases(self):
        head_text = git_show("HEAD", LEGACY)
        old = json.loads(head_text) if head_text else {"max_legacy": 0}
        new = json.loads(working(LEGACY))
        n = count_growth(old, new, self.ledger)
        self.assertIsNone(n, f"{LEGACY} max_legacy 由 {old.get('max_legacy')} 調高到 {n}，"
                             f"且 {LEDGER} 未登記理由")


# ── 邏輯（fixture） ─────────────────────────────────────────────────────────

def _e(anchor, max_len=250, kind="list_item"):
    return {"kind": kind, "anchor": anchor, "max_len": max_len}


class TestCellGrowthLogic(unittest.TestCase):
    def test_add1_remove2_is_caught_although_total_drops(self):
        """98a3b59e／8cca5fb0 的形狀：總數下降、但混進一個新錨點——必須紅。"""
        old = {"p": [_e("A"), _e("B"), _e("C")]}
        new = {"p": [_e("A"), _e("D")]}
        self.assertLess(sum(map(len, new.values())), sum(map(len, old.values())))
        grown = cell_growth(old, new, [])
        self.assertEqual([g["anchor"] for g in grown], ["D"])

    def test_tightening_is_not_growth(self):
        old = {"p": [_e("A", 300), _e("B")]}
        new = {"p": [_e("A", 280)]}
        self.assertEqual(cell_growth(old, new, []), [])

    def test_loosening_max_len_is_growth(self):
        old = {"p": [_e("A", 250)]}
        new = {"p": [_e("A", 251)]}
        self.assertEqual(len(cell_growth(old, new, [])), 1)

    def test_duplicate_anchor_count_increase_is_growth(self):
        old = {"p": [_e("2026-05-17#c2", 150, "table_cell")]}
        new = {"p": [_e("2026-05-17#c2", 150, "table_cell"), _e("2026-05-17#c2", 140, "table_cell")]}
        self.assertEqual(len(cell_growth(old, new, [])), 1)

    def test_same_anchor_other_page_is_growth(self):
        old = {"p": [_e("A")]}
        new = {"q": [_e("A")]}
        self.assertEqual(len(cell_growth(old, new, [])), 1)

    def test_ledger_with_reason_exempts(self):
        old = {"p": [_e("A")]}
        new = {"p": [_e("A"), _e("D", 230)]}
        row = {"file": CELL, "reason": "x", "added": [{"page": "p", **_e("D", 230)}]}
        self.assertEqual(cell_growth(old, new, [row]), [])

    def test_ledger_row_for_other_file_does_not_exempt(self):
        old = {"p": [_e("A")]}
        new = {"p": [_e("A"), _e("D", 230)]}
        row = {"file": READER, "reason": "x", "added": [{"page": "p", **_e("D", 230)}]}
        self.assertEqual(len(cell_growth(old, new, [row])), 1)

    def test_ledger_rows_without_reason_are_dropped(self):
        rows = new_ledger_rows("", json.dumps({"file": CELL, "reason": " ", "added": []}) + "\n")
        self.assertEqual(rows, [])

    def test_only_uncommitted_ledger_rows_count(self):
        """HEAD 已有的舊帳本行不能再拿來豁免新的增長。"""
        old_row = json.dumps({"file": CELL, "reason": "舊的", "added": [{"page": "p", **_e("D")}]})
        rows = new_ledger_rows(old_row + "\n", old_row + "\n")
        self.assertEqual(rows, [])


class TestSetAndCountLogic(unittest.TestCase):
    def test_reader_language_set_growth(self):
        old = {"p": ["封存:aaa", "封存:bbb"]}
        new = {"p": ["封存:aaa", "收錄標準:ccc"]}
        self.assertEqual(set_growth(old, new, [], READER), [("p", "收錄標準:ccc")])
        row = {"file": READER, "reason": "x", "added": [{"page": "p", "fp": "收錄標準:ccc"}]}
        self.assertEqual(set_growth(old, new, [row], READER), [])

    def test_pending_legacy_count(self):
        self.assertIsNone(count_growth({"max_legacy": 42}, {"max_legacy": 41}, []))
        self.assertEqual(count_growth({"max_legacy": 41}, {"max_legacy": 42}, []), 42)
        row = {"file": LEGACY, "reason": "x", "added": [{"max_legacy": 42}]}
        self.assertIsNone(count_growth({"max_legacy": 41}, {"max_legacy": 42}, [row]))


# ── 歷史事故重放（需要完整 git 歷史；shallow clone 時 skip） ─────────────────

class TestHistoricalReplay(unittest.TestCase):
    def _pair(self, sha, path):
        try:
            before, after = git_show(f"{sha}~1", path), git_show(sha, path)
        except _NoGit as e:
            self.skipTest(str(e))
        if before is None or after is None:
            self.skipTest(f"{sha} 無 {path}")
        return json.loads(before), json.loads(after)

    def test_96217a69_pending_legacy_41_to_42_is_red(self):
        before, after = self._pair("96217a69", LEGACY)
        self.assertEqual((before["max_legacy"], after["max_legacy"]), (41, 42))
        self.assertEqual(count_growth(before, after, []), 42)

    def test_98a3b59e_and_8cca5fb0_total_dropped_but_fingerprints_added(self):
        """兩次事故都是總數下降——比總數必漏，比集合差抓得到（舊指紋格式直接比）。"""
        for sha, n_added in (("98a3b59e", 2), ("8cca5fb0", 3)):
            before, after = self._pair(sha, CELL)
            self.assertLess(after["_hits"], before["_hits"], sha)
            self.assertEqual(len(set_growth(before["pages"], after["pages"], [], CELL)), n_added, sha)


if __name__ == "__main__":
    unittest.main()
