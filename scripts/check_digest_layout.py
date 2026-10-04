#!/usr/bin/env python3
"""check_digest_layout.py — 日報（news/YYYY-MM-DD.md）版式與跨區塊重述閘（Step 1b 3a-4）。

2026-10-03 週度 lint 冷讀者對抗輪抓到三件規格寫了、卻沒有任何機械看守的事：

1. 跨區塊重述：10-02 的 Mods 在同一檔出現五處，聚焦句（L9）與技術更新說明句（L30）
   幾乎逐字相同。`selection.md`「聚焦防重複」早就寫了「連續 12 字元相同視為複製」，
   但沒人量——兩句只差一個「現在」、一個分號，肉眼自檢放過了。
2. 版式不穩：常設區塊有時整節消失（讀者分不出「今天沒有」與「改版了」），
   💬 從 8 則膨脹到 19 則（10-01，2.4 倍）。
3. 數字對不攏：標頭「文章數」與檔尾來源表是兩個口徑（候選 vs 原始抓取）。
   檔尾表改由 `scripts/digest_source_table.py` 產生；本閘驗「進候選」欄加總＝標頭。

量法（重述）：說明句只留中日韓統一表意文字（去標點、英數、空白——產品名與數字
是合法的共同元素，不算複製），兩兩比對不同區塊的句子，最長共同子字串 ≥ DUP_MIN_CJK
即判重述。校準（2026-08-01～10-03 共 62 份）：門檻 12 抓得到 10-02 那對（恰 12）；
樣板句（「累積 N 則留言、M 個反應」）只有 8，不會誤擋。

用法：
    python scripts/check_digest_layout.py YYYY-MM-DD [--news-dir DIR]

退出碼：0 通過；1 有違規（逐條印出，修日報後重跑）；2 檔案不存在。
第 2、3 類（常設區塊、篇幅上限、來源表口徑）只對 LAYOUT_SINCE 之後的日期生效，
舊日報凍結不回溯；第 1 類對任何日期都量（規則早已存在）。
"""
from __future__ import annotations

import argparse
import difflib
import io
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "news"

LAYOUT_SINCE = "2026-10-05"
DUP_MIN_CJK = 12
STANDING = ("⭐", "🔧", "💰", "📰", "💬")
# 每區條目上限（規格：.claude/skills/news-digest/references/format.md「版式穩定」）
CAPS = {"📌": 5, "⭐": 5, "🔧": 6, "💰": 4, "📰": 6, "💬": 10}

SECTION_RE = re.compile(r"^###\s+(\S+)")
FOCUS_LINE_RE = re.compile(r"^- \*\*\[[^\]]+\]\*\*\s*(.*)$")
STORY_RE = re.compile(r"^\*\*\[.+\]\(https?://")
ARTICLE_COUNT_RE = re.compile(r"\*\*文章數[：:]\*\*\s*(\d+)")
SOURCE_ROW5_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*[✅❌]\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|")
SOURCE_ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*[✅❌]\s*\|\s*\d+\s*\|")
NON_CJK_RE = re.compile(r"[^一-鿿]")
INLINE_LINK_GROUP_RE = re.compile(r"[（(]\s*\[[^\]]+\]\(https?://.*$")


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def parse_sections(text: str) -> dict[str, dict]:
    """{emoji: {"line": 標題行號, "items": [(行號, 說明句)], "notes": [`>` 行]}}"""
    secs: dict[str, dict] = {}
    cur = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            cur = m.group(1)
            secs.setdefault(cur, {"line": i + 1, "items": [], "notes": []})
            continue
        if cur is None:
            continue
        if line.startswith(">"):
            secs[cur]["notes"].append(line)
        if cur == "📌":
            fm = FOCUS_LINE_RE.match(line)
            if fm:
                secs[cur]["items"].append((i + 1, INLINE_LINK_GROUP_RE.sub("", fm.group(1))))
        elif STORY_RE.match(line):
            desc = lines[i + 1] if i + 1 < len(lines) else ""
            secs[cur]["items"].append((i + 2, desc))
    return secs


def longest_cjk_overlap(a: str, b: str) -> str:
    x, y = NON_CJK_RE.sub("", a), NON_CJK_RE.sub("", b)
    m = difflib.SequenceMatcher(None, x, y, autojunk=False).find_longest_match(0, len(x), 0, len(y))
    return x[m.a:m.a + m.size]


def check_duplicates(secs: dict[str, dict]) -> list[str]:
    flat = [(emo, ln, d) for emo, s in secs.items() if emo != "📡" for ln, d in s["items"]]
    errs = []
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            (ea, la, da), (eb, lb, db) = flat[i], flat[j]
            if ea == eb:
                continue
            common = longest_cjk_overlap(da, db)
            if len(common) >= DUP_MIN_CJK:
                errs.append(f"  ❌ 跨區塊重述：{ea} L{la} 與 {eb} L{lb} 有 {len(common)} 字相同（「{common}」）"
                            "——後出現的那句只寫前一句沒有的事（數字、版本、誰受影響、下一步），"
                            "寫不出新東西就整則移除（前一句已經講過了）")
    return errs


def check_layout(secs: dict[str, dict], text: str) -> list[str]:
    errs = []
    for emo in STANDING:
        if emo not in secs:
            errs.append(f"  ❌ 常設區塊 {emo} 不見了——區塊固定出現；今天沒有內容就在標題下寫一行 "
                        "`> 本日無……`（讀者語言說明為什麼沒有）")
        elif not secs[emo]["items"] and not secs[emo]["notes"]:
            errs.append(f"  ❌ 常設區塊 {emo} 是空的——寫條目，或一行 `> 本日無……`")
    for emo, cap in CAPS.items():
        n = len(secs.get(emo, {}).get("items", []))
        if n > cap:
            errs.append(f"  ❌ {emo} 有 {n} 則，上限 {cap}——依今日訊號強度留前 {cap} 則，"
                        "其餘不寫（沒寫進日報的條目仍會餵給 wiki ingest，不會消失）")
    m = ARTICLE_COUNT_RE.search(text)
    rows5 = [r for r in (SOURCE_ROW5_RE.match(l) for l in text.splitlines()) if r]
    rows_any = [l for l in text.splitlines() if SOURCE_ROW_RE.match(l)]
    if rows_any and not rows5:
        errs.append("  ❌ 來源狀態表仍是舊三欄——跑 `python scripts/digest_source_table.py DATE --write` 重產")
    elif m and rows5:
        total = sum(int(r.group(3)) for r in rows5)
        if total != int(m.group(1)):
            errs.append(f"  ❌ 標頭文章數 {m.group(1)} ≠ 來源表「進候選」合計 {total}——"
                        "標頭照抄 gathered_items.json 的 article_count，表由 digest_source_table.py 產生，不手改")
    return errs


def run(date: str, news_dir: Path = NEWS_DIR) -> tuple[int, list[str]]:
    path = news_dir / f"{date}.md"
    if not path.exists():
        return 2, [f"  ❌ {path} 不存在"]
    text = path.read_text(encoding="utf-8-sig")
    secs = parse_sections(text)
    errs = check_duplicates(secs)
    if date >= LAYOUT_SINCE:
        errs += check_layout(secs, text)
    return (1 if errs else 0), errs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("date")
    ap.add_argument("--news-dir", type=Path, default=NEWS_DIR)
    args = ap.parse_args(argv)
    code, errs = run(args.date, args.news_dir)
    out = _stdout()
    if errs:
        print("\n".join(errs), file=out)
    print(f"[check_digest_layout] {args.date}："
          + ("✅ 無跨區塊重述" + ("、版式與來源表口徑通過" if args.date >= LAYOUT_SINCE else "") if code == 0
             else f"❌ {len(errs)} 項"), file=out)
    return code


if __name__ == "__main__":
    sys.exit(main())
