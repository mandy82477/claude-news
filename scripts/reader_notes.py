#!/usr/bin/env python3
"""reader_notes.py — 從 wiki/reader-notes.md 摘出 ⏳ 待處理項的短版，供派工 prompt 直接貼。

收件匣單行可達數千字，記者只需要「有哪幾件、各講什麼」；全文要看時照行號回原檔讀。

類別推斷：該項全文裡的 wikilink 指向的頁，依頁面 domain 對到記者類別
（口徑同 scripts/reporter_pages.py）。一項可屬多類；沒有任何可對到的連結就歸「未分類」，
未分類項不論 --category 為何一律印出（寧可多給一位記者看，不讓它沒人看）。

唯讀，不寫任何檔。

用法：
    python scripts/reader_notes.py --pending                       # 全部 ⏳ 項
    python scripts/reader_notes.py --pending --category 社群        # 該類別＋未分類
    python scripts/reader_notes.py --pending --category 商業 --brief 80
輸出每項一行：`L<行號>｜<日期>｜<類型>｜[類別] <前 N 字>`
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "wiki" / "reader-notes.md"
WIKI_DIR = ROOT / "wiki"
DEFAULT_BRIEF = 150

_spec = importlib.util.spec_from_file_location("_reporter_pages_for_notes", ROOT / "scripts" / "reporter_pages.py")
rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rp)

ITEM_RE = re.compile(r"^- \[⏳\]\s*([^｜]*?)\s*｜\s*([^｜]*?)\s*｜\s*(.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def normalize_link(link: str) -> str:
    p = link.strip()
    if p.startswith("wiki/"):
        p = p[len("wiki/"):]
    if p.endswith(".md"):
        p = p[:-3]
    return p


def brief(text: str, n: int) -> str:
    flat = re.sub(r"\s+", " ", text.replace("**", "")).strip()
    return flat if len(flat) <= n else flat[:n] + "…"


def pending_items(text: str, page_cats: dict[str, str]) -> list[dict]:
    items = []
    for no, line in enumerate(text.splitlines(), 1):
        m = ITEM_RE.match(line)
        if not m:
            continue
        date, kind, content = m.groups()
        cats = []
        for link in WIKILINK_RE.findall(content):
            c = page_cats.get(normalize_link(link))
            if c and c != rp.UNCLASSIFIED and c not in cats:
                cats.append(c)
        items.append({"line": no, "date": date, "kind": kind, "content": content,
                      "categories": cats or [rp.UNCLASSIFIED]})
    return items


def select(items: list[dict], category: str | None) -> list[dict]:
    if category is None:
        return items
    return [it for it in items if category in it["categories"] or rp.UNCLASSIFIED in it["categories"]]


def render(items: list[dict], n: int) -> str:
    return "\n".join(f"L{it['line']}｜{it['date']}｜{it['kind']}｜[{'、'.join(it['categories'])}] "
                     f"{brief(it['content'], n)}" for it in items)


def main(argv: list[str] | None = None) -> int:
    rp._stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pending", action="store_true", required=True, help="印 ⏳ 待處理項（目前唯一模式）")
    ap.add_argument("--category", help="只印該類別＋未分類：" + "、".join(rp.CATEGORIES))
    ap.add_argument("--brief", type=int, default=DEFAULT_BRIEF, metavar="N", help=f"每項內容前 N 字（預設 {DEFAULT_BRIEF}）")
    ap.add_argument("--file", type=Path, default=NOTES)
    ap.add_argument("--wiki-dir", type=Path, default=WIKI_DIR)
    args = ap.parse_args(argv)

    if args.category is not None and args.category not in rp.CATEGORIES:
        print(f"❌ 不認得的類別「{args.category}」，可用：" + "、".join(rp.CATEGORIES), file=sys.stderr)
        return 2
    if args.brief < 1:
        print("❌ --brief 須為正整數", file=sys.stderr)
        return 2
    if not args.file.exists():
        print(f"❌ 找不到 {args.file}", file=sys.stderr)
        return 3
    items = select(pending_items(args.file.read_text(encoding="utf-8"), rp.page_categories(args.wiki_dir)),
                   args.category)
    scope = f"類別：{args.category}＋未分類" if args.category else "全部類別"
    print(f"# reader-notes ⏳ 待處理 {len(items)} 項（{scope}；全文照行號讀 wiki/reader-notes.md）")
    if items:
        print(render(items, args.brief))
    else:
        print("無")
    return 0


if __name__ == "__main__":
    sys.exit(main())
