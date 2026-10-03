#!/usr/bin/env python3
"""
check_append_only.py — append-only 檔不得把新內容寫在檔頭。

為什麼（2026-10-03）：`wiki/log.md` 是「不可改的過去」，新紀錄一律 append，但這條只寫在
規則裡；2026-08-07 的 Ingest 條目就被寫在檔案最上方（wiki/log.md 2026-08-08 lint 的「結構性發現」）。
寫錯位置不會有任何錯誤——直到下一次 rebase 的 union 合併把順序攪亂。

判準（回測過才定的，見 head_growth）：比對「基準版」與工作樹，**淨增長的 hunk（新增行數 >
刪除行數）不得落在第一則既有紀錄之前**——也就是不准把新紀錄寫在檔頭。中段的就地更正、
同日條目補行、merge 帶進來的對方紀錄都放行：那是本專案的日常，不是事故。
基準版＝`git merge-base HEAD origin/master`（本機未推送的 commit 一起驗；雲端在 commit 後、
push 前跑也有效），沒有 origin/master 時退回 HEAD。

檔案清單：`scripts/resolve_append_only.py` 的 APPEND_ONLY（單一來源），但排除
`data/source_attribution.jsonl`——`scripts/enrich_attribution_publisher.py` 會回填舊行的
publisher 欄位，屬設計內的改寫（例：45339ed0）。

用法：python scripts/check_append_only.py [--base <rev>]
    無違規 → exit 0；有 → 列出檔名與行號、exit 1。
"""
from __future__ import annotations

import argparse
import difflib
import io
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from resolve_append_only import APPEND_ONLY  # noqa: E402

EXEMPT = {
    "data/source_attribution.jsonl": "enrich_attribution_publisher.py 回填 publisher 欄位，設計內改寫",
}


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                             text=True, encoding="utf-8", errors="replace", timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout if out.returncode == 0 else None


def default_base() -> str:
    mb = _git("merge-base", "HEAD", "origin/master")
    return mb.strip() if mb and mb.strip() else "HEAD"


def head_growth(base: list[str], new: list[str]) -> list[int]:
    """淨增長、且落在基準版「第一則紀錄之前」（檔頭）的 hunk，回傳其在新版的起始行號（1-based）。

    紀錄邊界：markdown 以第一個 `## ` 標題為準；jsonl／log 以第一個非空行為準。
    只看檔頭是回測後的取捨：「淨增長只能在檔尾」在 2026-08-01～10-03 的 798 組
    commit×檔裡誤報 27 組（merge 時對方紀錄落在中段、同日條目事後補行）；本判準回測只命中
    08-07 那一次（cd0f3cf4）——那才是要擋的病。markdown 檔頭說明文字的改寫不算（08bd1a93）。
    """
    if not any(ln.strip() for ln in base):
        return []  # 空檔的第一次寫入
    md_head = next((i for i, ln in enumerate(base) if ln.startswith("## ")), None)
    head = md_head if md_head is not None else next(i for i, ln in enumerate(base) if ln.strip())
    sm = difflib.SequenceMatcher(a=base, b=new, autojunk=False)
    hits = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag not in ("insert", "replace") or (j2 - j1) <= (i2 - i1) or i1 > head:
            continue
        added = new[j1:j2]
        # markdown 檔頭的說明文字可以改（08bd1a93 統一檔頭契約）；長出新的 `## ` 紀錄才算事故
        if md_head is not None and not any(ln.startswith("## ") for ln in added):
            continue
        hits.append(j1 + 1)
    return hits


def _lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").split("\n")


def check(base_rev: str) -> list[tuple[str, list[int]]]:
    out = []
    for rel in sorted(APPEND_ONLY):
        if rel in EXEMPT:
            continue
        base_text = _git("show", f"{base_rev}:{rel}")
        path = ROOT / rel
        if base_text is None:
            continue  # 基準版沒有這個檔：新檔，無從比較
        if not path.is_file():
            out.append((rel, [0]))
            continue
        hits = head_growth(_lines(base_text), _lines(path.read_text(encoding="utf-8", errors="replace")))
        if hits:
            out.append((rel, hits))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="append-only 檔不得把新內容寫在檔頭")
    ap.add_argument("--base", help="基準版（預設 merge-base HEAD origin/master）")
    args = ap.parse_args(argv)
    stream = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace") if hasattr(sys.stdout, "buffer") else sys.stdout
    base = args.base or default_base()
    bad = check(base)
    if bad:
        stream.write("❌ append-only 檔把新紀錄寫在檔頭（第一則既有紀錄之前），或整檔被刪：\n")
        for rel, hits in bad:
            where = "檔案不見了" if hits == [0] else "新版第 " + "、".join(map(str, hits[:5])) + " 行起"
            stream.write(f"  {rel}：{where}\n")
        stream.write("修法：把新紀錄移到檔尾。"
                     "規則：wiki/CLAUDE.md「log 只能 append」。\n")
        stream.write(f"FAIL: check_append_only — {len(bad)} 檔違規（基準 {base[:10]}）\n")
        stream.flush()
        return 1
    stream.write(f"OK: check_append_only — {len(APPEND_ONLY) - len(EXEMPT)} 檔無檔頭插入（基準 {base[:10]}）\n")
    stream.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
