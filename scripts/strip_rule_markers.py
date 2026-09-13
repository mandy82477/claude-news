#!/usr/bin/env python3
"""
strip_rule_markers.py — 刪掉規則檔裡的條文日期標記 `[加入: YYYY-MM-DD]`／`[改版: …]` 等。

用法：
    python scripts/strip_rule_markers.py            # dry-run：只印每檔會刪幾個、抽樣三行
    python scripts/strip_rule_markers.py --write    # 真的寫回

範圍：.claude/**/*.md、CLAUDE.md、wiki/CLAUDE.md（不碰 docs/rules-changelog/、wiki/log.md 等歷史紀錄）。

刪什麼：`[加入: 2026-08-28]`、`[改版: 2026-09-04]`、`[加入: 2026-06-20，改名: 2026-08-01]`、
`[順序改版: …]`、`[裁決: …]`、`[移入: …]`、`[加入: 2026-09-13 乙-2]` 這類方括號日期戳，
連同包住它的反引號與前後多餘的一個空白。不刪 `[加入: YYYY-MM-DD]` 這種說明用的佔位字樣以外的東西
（佔位字樣本身也刪——標記制度廢除後說明它的句子由人另外改）。

為什麼（2026-09-13 使用者裁決）：283 個標記是人手維護的版本戳，漏標、標錯沒有機制抓；
規則年齡 git blame 就有，考古鏈在沿革檔 grep 關鍵字就找得到。標記只讓執行的 agent 每條多跳一截尾巴。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [ROOT / "CLAUDE.md", ROOT / "wiki" / "CLAUDE.md", *sorted((ROOT / ".claude").rglob("*.md"))]

# 方括號內：以「加入／改版／順序改版／改名／裁決／移入／擴充／使用者指示」開頭、含日期或 YYYY 佔位，可多段以全形逗號連接
_KIND = r"(?:加入|改版|順序改版|改名|裁決|移入|擴充|使用者指示)"
_DATE = r"(?:\d{4}-\d{2}-\d{2}|YYYY-MM-DD)"
MARK_RE = re.compile(
    r"[ 　]?`?\[" + _KIND + r":\s*" + _DATE + r"[^\]\n]*\]`?"
)


def strip_text(text: str) -> tuple[str, int]:
    out_lines: list[str] = []
    n = 0
    for line in text.splitlines(keepends=True):
        new, k = MARK_RE.subn("", line)
        if k:
            n += k
            # 標題／粗體尾端可能剩下「 `」或雙空白，順手收乾淨
            new = re.sub(r"[ 　]{2,}", " ", new)
            new = re.sub(r" +(\r?\n)$", r"\1", new)
            new = re.sub(r"\*\* +：", "**：", new)
        out_lines.append(new)
    return "".join(out_lines), n


def main(argv: list[str]) -> int:
    write = "--write" in argv
    total = 0
    for f in TARGETS:
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        new, n = strip_text(text)
        if not n:
            continue
        total += n
        rel = f.relative_to(ROOT).as_posix()
        print(f"{rel}: {n}")
        if not write:
            for a, b in zip(text.splitlines(), new.splitlines()):
                if a != b:
                    print(f"    - {a.strip()[:100]}")
                    print(f"    + {b.strip()[:100]}")
                    break
        else:
            f.write_text(new, encoding="utf-8", newline="")
    print(f"{'已刪' if write else '將刪'} {total} 個標記" + ("" if write else "（dry-run，加 --write 才寫）"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
