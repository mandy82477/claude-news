#!/usr/bin/env python3
"""
check_callout_coverage.py — 讀者版日報涵蓋閘：當日吃進新聞的頁，頁頂必須有當日日期的 callout。

用法：
    python scripts/check_callout_coverage.py YYYY-MM-DD                 # 全庫（Step 2b 產出前）
    python scripts/check_callout_coverage.py YYYY-MM-DD --page <slug>   # 記者收工前自查，可重複 --page
    （slug 寫 entities/x、topics/y 或檔案路徑；只寫檔名時，兩個目錄裡同名的頁都會看）

讀者版（daily/）是各頁頂部當日 callout 的投影（scripts/build_reader_digest.py），挑選鍵是 callout
括號日期。記者把新聞寫進時序、把「最後新聞更新」改成 TARGET_DATE，卻沒覆寫 callout（或把日期寫成
事件日）——這頁當天就從日報上靜默消失，產生器與格式閘都看不見。本閘把這個形狀變成會紅的檢查。

判定（本體是 build_reader_digest.coverage_gaps，豁免表 COVERAGE_EXEMPT 也住那裡）：標頭 `**最後新聞更新：**` == TARGET_DATE 的頁，頁首（H1 到第一條 `---`）必須至少有一段首行
`> **標籤**（TARGET_DATE…）` 的 callout。產生器自己每次產出也會把同一份結果印成 WARN；本腳本是給記者自查與 Step 2b 第 0 步用的、
會回非零結束碼的入口。

只對 TARGET_DATE 當天跑才有意義：頁面隔天再被更新後，「最後新聞更新」就不再是那一天，歷史日期
無法從 wiki 現版重驗，所以本閘不掃全部 daily/、不進 run_tests 的全庫檢查。

規則端：`.claude/reporter-rules/page-templates.md`「頂部 delta-first callout」。
exit 0＝通過；1＝有頁漏了當日 callout（逐頁點名）；2＝用法錯誤。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_reader_digest import coverage_gaps as check  # noqa: E402  判定本體住產生器，兩端同一段程式碼


def _norm(slug: str) -> str:
    slug = slug.replace("\\", "/").strip()
    slug = re.sub(r"^wiki/", "", slug)
    return re.sub(r"\.md$", "", slug)


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = argv[1:]
    only: set[str] = set()
    pos: list[str] = []
    i = 0
    while i < len(args):
        if args[i] == "--page" and i + 1 < len(args):
            only.add(_norm(args[i + 1]))
            i += 2
        elif args[i].startswith("--"):
            pos = []
            break
        else:
            pos.append(args[i])
            i += 1
    if len(pos) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", pos[0]):
        print("用法：python scripts/check_callout_coverage.py YYYY-MM-DD [--page <slug>]…")
        return 2
    target_date = pos[0]
    problems, updated = check(target_date, only=only or None)
    if problems:
        for p in problems:
            print(f"  - {p}")
        print(f"讀者版涵蓋檢查 {target_date}：{len(problems)} 頁漏了當日 callout（當日吃進新聞的頁共 {updated}）")
        return 1
    print(f"讀者版涵蓋檢查 {target_date}：{updated} 頁當日吃進新聞，全數有當日 callout")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
