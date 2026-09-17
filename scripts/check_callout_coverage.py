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

判定：標頭 `**最後新聞更新：**` == TARGET_DATE 的頁，頁首（H1 到第一條 `---`）必須至少有一段首行
`> **標籤**（TARGET_DATE…）` 的 callout。頁首切法與 callout 形狀直接用產生器的 page_head／
dated_callouts，兩端不會各認各的。

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
from build_reader_digest import CALLOUT_RE, WIKI_DIR, dated_callouts, page_head  # noqa: E402

LAST_NEWS_RE = re.compile(r"^\*\*最後新聞更新[：:]\*\*\s*(\d{4}-\d{2}-\d{2})", re.M)

# 機器每日整頁覆寫、沒有記者寫 callout 的頁：「最後新聞更新」天天是當日，但刻意不投影進日報。
# 新增豁免要寫理由——沒有理由的豁免就是把漏洞登記成合法。
EXEMPT = {
    "topics/skill-interest-watch": "scripts/skill_interest_snapshot.py 每日整頁覆寫的機器快照頁",
}


def _norm(slug: str) -> str:
    slug = slug.replace("\\", "/").strip()
    slug = re.sub(r"^wiki/", "", slug)
    return re.sub(r"\.md$", "", slug)


def check(target_date: str, wiki_dir: Path = WIKI_DIR, only: set[str] | None = None) -> tuple[list[str], int]:
    """回傳 (違規訊息, 當日吃進新聞的頁數)。only＝只看這些 slug（entities/x、topics/y）。"""
    problems: list[str] = []
    updated = 0
    for sub in ("entities", "topics"):
        for f in sorted((wiki_dir / sub).glob("*.md")):
            page = f"{sub}/{f.stem}"
            if only is not None and page not in only and f.stem not in only:
                continue
            raw = f.read_text(encoding="utf-8-sig")
            m = LAST_NEWS_RE.search(raw)
            if not m or m.group(1) != target_date or page in EXEMPT:
                continue
            updated += 1
            head = page_head(raw)[1]
            if dated_callouts(head, target_date):
                continue
            seen = [cm.group("date") for l in head.splitlines() if (cm := CALLOUT_RE.match(l))]
            if seen:
                why = f"頁頂 callout 日期是 {'、'.join(seen)}（要寫 TARGET_DATE，不是事件日；今日重點沒覆寫就覆寫）"
            else:
                why = "頁頂沒有 `> **標籤**（YYYY-MM-DD）` 形狀的 callout（自介型「（快照 …）」不算，另加一段當日 callout）"
            problems.append(f"{page}：最後新聞更新＝{target_date}，但{why}——這頁今天不會上讀者版日報")
    return problems, updated


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
