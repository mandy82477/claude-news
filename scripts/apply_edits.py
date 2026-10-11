"""
apply_edits.py — 一次套用多筆精確字串替換（批次修補，給記者省回合數）。

每個 Edit 工具呼叫是一回合、每回合重算整個 context；同一輪要改多處時，
把修改寫成一個 JSON 檔、用本腳本一次套用，回合數從幾十降到個位數。
步驟與邊界見 `.claude/reporter-rules/batch-edit.md`（試點中）。

用法：
    python scripts/apply_edits.py data/edit-batches/2026-10-11-features.json
    python scripts/apply_edits.py batch.json --dry-run      # 只印命中檔案與行號，不寫
    python scripts/apply_edits.py - < batch.json             # 從 stdin 讀
    python scripts/apply_edits.py batch.json --replace-all   # 允許一筆 old 多次命中、全部替換

JSON 格式：[{"file": "wiki/entities/claude-code.md", "old": "...", "new": "..."}, ...]
    同一檔多筆依序套用（第 2 筆看到的是第 1 筆改完的內容）。

保證：
- 全部預檢再寫入：任一筆 old 找不到或命中多次（未給 --replace-all）→ 整批不寫、exit 2。
- 行尾保留：依原檔偵測 CRLF／LF，JSON 裡的換行一律轉成該檔行尾；UTF-8 BOM 有就保留。
- 路徑白名單：唯一定義在下方常數 ALLOWED_PREFIXES（`--help` 與拒絕訊息都從它組字串）；
  白名單外一律拒絕、exit 3——含 wiki/feature-radar.md、wiki/index.md、wiki/log.md
  （shared.md 邊界限制：記者不可碰，由主編統一處理）。
  hook 看得到 Edit/Write，看不到腳本內部寫檔，這道白名單是補強，不可拿掉。

結束碼：0 成功／2 預檢失敗（未命中、多次命中、JSON 格式錯、檔案不存在）／3 路徑被拒。
不呼叫任何 LLM。
"""
from __future__ import annotations

import argparse
import codecs
import difflib
import json
import os
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent

# 可寫範圍的唯一定義：只准這些目錄底下的檔案。docstring、--help、拒絕訊息都不另抄清單。
ALLOWED_PREFIXES = ("wiki/entities/", "wiki/topics/")
ALLOWED_TEXT = "、".join(ALLOWED_PREFIXES)

EXIT_OK = 0
EXIT_PREFLIGHT = 2
EXIT_PATH = 3


class BatchError(Exception):
    def __init__(self, code: int, msg: str):
        super().__init__(msg)
        self.code = code


def normalize_rel(raw: str) -> str | None:
    """把 JSON 裡的路徑正規化成 repo 相對 POSIX 路徑；逃出 repo（絕對路徑、..）回 None。"""
    s = raw.replace("\\", "/").strip()
    if not s or s.startswith("/") or (len(s) > 1 and s[1] == ":"):
        return None
    parts: list[str] = []
    for p in PurePosixPath(s).parts:
        if p in ("", "."):
            continue
        if p == "..":
            return None
        parts.append(p)
    return "/".join(parts) if parts else None


def path_allowed(rel: str) -> bool:
    return any(rel.startswith(p) and len(rel) > len(p) for p in ALLOWED_PREFIXES)


def reject_reason(rel: str | None, raw: str) -> str:
    if rel is None:
        return f"路徑 {raw!r} 不是 repo 內的相對路徑"
    if rel == "wiki/log.md":
        return f"wiki/log.md 只能 append，不可用批次替換改寫（可寫範圍只有 {ALLOWED_TEXT}）"
    return f"不在可寫範圍（只准 {ALLOWED_TEXT} 底下的檔案）"


def load_edits(text: str) -> list[dict]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise BatchError(EXIT_PREFLIGHT, f"JSON 解析失敗：{e}")
    if not isinstance(data, list) or not data:
        raise BatchError(EXIT_PREFLIGHT, "JSON 頂層必須是非空陣列")
    for i, e in enumerate(data, 1):
        if not isinstance(e, dict):
            raise BatchError(EXIT_PREFLIGHT, f"第 {i} 筆不是物件")
        for k in ("file", "old", "new"):
            if not isinstance(e.get(k), str):
                raise BatchError(EXIT_PREFLIGHT, f"第 {i} 筆缺字串欄位 {k!r}")
        if e["old"] == "":
            raise BatchError(EXIT_PREFLIGHT, f"第 {i} 筆 old 是空字串")
    return data


class FileState:
    def __init__(self, path: Path):
        raw = path.read_bytes()
        self.bom = raw.startswith(codecs.BOM_UTF8)
        if self.bom:
            raw = raw[len(codecs.BOM_UTF8):]
        try:
            self.original = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            raise BatchError(EXIT_PREFLIGHT, f"{path} 不是合法 UTF-8：{e}")
        crlf = self.original.count("\r\n")
        bare_lf = self.original.count("\n") - crlf
        self.eol = "\r\n" if crlf > bare_lf else "\n"
        self.text = self.original

    def convert(self, s: str) -> str:
        s = s.replace("\r\n", "\n")
        return s.replace("\n", self.eol) if self.eol != "\n" else s

    def line_of(self, idx: int) -> int:
        return self.text.count("\n", 0, idx) + 1

    def encoded(self) -> bytes:
        return (codecs.BOM_UTF8 if self.bom else b"") + self.text.encode("utf-8")

    def changed_lines(self) -> list[int]:
        a = self.original.splitlines()
        b = self.text.splitlines()
        lines: set[int] = set()
        for tag, _i1, _i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag == "equal":
                continue
            if j2 > j1:
                lines.update(range(j1 + 1, j2 + 1))
            else:  # 純刪除：標刪除點所在的新行號
                lines.add(max(j1, 1))
        return sorted(lines)


def compress(nums: list[int]) -> str:
    out: list[str] = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


def run(edits: list[dict], root: Path, replace_all: bool, dry_run: bool, out=sys.stdout) -> int:
    # 1) 路徑全查一遍：任一筆被拒 → 整批不寫
    rels: list[str] = []
    bad = []
    for i, e in enumerate(edits, 1):
        rel = normalize_rel(e["file"])
        if rel is None or not path_allowed(rel):
            bad.append(f"  第 {i} 筆 {e['file']}：{reject_reason(rel, e['file'])}")
        rels.append(rel or "")
    if bad:
        print("❌ 路徑被拒，整批未寫入：", file=out)
        print("\n".join(bad), file=out)
        return EXIT_PATH

    # 2) 預檢：在記憶體依序套用，任何一筆失敗 → 整批不寫
    states: dict[str, FileState] = {}
    order: list[str] = []
    hits_report: list[str] = []
    errors: list[str] = []
    for i, (e, rel) in enumerate(zip(edits, rels), 1):
        if rel not in states:
            path = root / rel
            if not path.is_file():
                errors.append(f"  第 {i} 筆 {rel}：檔案不存在")
                continue
            try:
                states[rel] = FileState(path)
            except BatchError as be:
                errors.append(f"  第 {i} 筆 {rel}：{be}")
                continue
            order.append(rel)
        st = states[rel]
        old = st.convert(e["old"])
        new = st.convert(e["new"])
        n = st.text.count(old)
        if n == 0:
            errors.append(f"  第 {i} 筆 {rel}：old 找不到（前 60 字：{e['old'][:60]!r}）")
            continue
        if n > 1 and not replace_all:
            first = st.line_of(st.text.find(old))
            errors.append(f"  第 {i} 筆 {rel}：old 命中 {n} 次（首次在第 {first} 行），請加長 old 或用 --replace-all")
            continue
        lines = []
        pos = st.text.find(old)
        while pos != -1:
            lines.append(st.line_of(pos))
            pos = st.text.find(old, pos + len(old))
        hits_report.append(f"  第 {i} 筆 {rel}：第 {compress(sorted(set(lines)))} 行" + (f"（{n} 處）" if n > 1 else ""))
        st.text = st.text.replace(old, new) if replace_all else st.text.replace(old, new, 1)

    if errors:
        print(f"❌ 預檢失敗 {len(errors)} 筆，整批未寫入：", file=out)
        print("\n".join(errors), file=out)
        return EXIT_PREFLIGHT

    if dry_run:
        print(f"🔍 dry-run：{len(edits)} 筆全部命中 / {len(order)} 檔（未寫入）", file=out)
        print("\n".join(hits_report), file=out)
        return EXIT_OK

    # 3) 寫入（先寫暫存檔再 os.replace，單檔不會半寫）
    for rel in order:
        st = states[rel]
        if st.text == st.original:
            continue
        path = root / rel
        tmp = path.with_name(path.name + ".apply_edits.tmp")
        tmp.write_bytes(st.encoded())
        os.replace(tmp, path)

    print(f"✅ {len(edits)} 筆套用 / {len(order)} 檔", file=out)
    for rel in order:
        lines = states[rel].changed_lines()
        print(f"  {rel}：改動行 {compress(lines) if lines else '（內容未變）'}", file=out)
    return EXIT_OK


def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(
        description=f"一次套用多筆精確字串替換（全部預檢通過才寫入）。可寫範圍：只准 {ALLOWED_TEXT} 底下的檔案，其餘 exit 3。")
    ap.add_argument("batch", nargs="?", default="-", help="JSON 檔路徑；省略或 - 表示從 stdin 讀")
    ap.add_argument("--replace-all", action="store_true", help="允許 old 多次命中並全部替換")
    ap.add_argument("--dry-run", action="store_true", help="只印每筆命中的檔案與行號，不寫入")
    ap.add_argument("--root", type=Path, default=ROOT, help="repo 根目錄（測試用）")
    args = ap.parse_args(argv)

    try:
        if args.batch == "-":
            text = sys.stdin.buffer.read().decode("utf-8-sig")
        else:
            text = Path(args.batch).read_text(encoding="utf-8-sig")
        edits = load_edits(text)
    except BatchError as e:
        print(f"❌ {e}")
        return e.code
    except (OSError, UnicodeDecodeError) as e:
        print(f"❌ 讀不到批次檔：{e}")
        return EXIT_PREFLIGHT
    return run(edits, args.root.resolve(), args.replace_all, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
