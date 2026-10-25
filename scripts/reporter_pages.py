#!/usr/bin/env python3
"""reporter_pages.py — 印某類別記者負責的 wiki 頁面（依頁面 frontmatter 的 domain）。

口徑：`wiki/entities/`、`wiki/topics/` 下每頁 frontmatter 的 `domain:`（由
scripts/gen_wiki_frontmatter.py 從頁內 `**領域：**` 行產生；沒有 frontmatter 時直接讀該行）。
子頁不入 index 但有自己的 domain，所以這裡比讀 index 領域欄更完整。
領域文字 → 記者類別沿用 scripts/pending_handoffs.py 的 DOMAIN_TO_CATEGORY，另加 💻 開發實務。
規則檔觸發條件表另列的頁（如 feature-radar）不在這裡，派工 prompt 照舊另附。

唯讀，不寫任何檔。

用法：
    python scripts/reporter_pages.py --category 社群   # 一行一個頁面路徑
    python scripts/reporter_pages.py --all             # 類別 → 頁數，末尾列對不到類別的頁
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
PAGE_DIRS = ("entities", "topics")
UNCLASSIFIED = "未分類"


def _load_domain_map() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location("_ph_for_reporter_pages", ROOT / "scripts" / "pending_handoffs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {**mod.DOMAIN_TO_CATEGORY, "開發實務": "開發實務"}


DOMAIN_TO_CATEGORY = _load_domain_map()
CATEGORIES = tuple(dict.fromkeys(DOMAIN_TO_CATEGORY.values()))

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.DOTALL)
FM_DOMAIN_RE = re.compile(r'^domain:[ \t]*"?([^"\r\n]*?)"?[ \t]*$', re.MULTILINE)
BODY_DOMAIN_RE = re.compile(r"^\*\*領域[：:]\*\*\s*(.+?)\s*$", re.MULTILINE)


def page_domain(text: str) -> str:
    m = FM_RE.match(text)
    if m:
        d = FM_DOMAIN_RE.search(m.group(1))
        if d and d.group(1).strip():
            return d.group(1).strip()
    b = BODY_DOMAIN_RE.search(text)
    return b.group(1).strip() if b else ""


def domain_category(domain: str) -> str:
    for key, cat in DOMAIN_TO_CATEGORY.items():
        if key in domain:
            return cat
    return UNCLASSIFIED


def page_categories(wiki_dir: Path = WIKI_DIR) -> dict[str, str]:
    """回傳 `topics/x`（wikilink 形）→ 記者類別；對不到的歸「未分類」。"""
    out: dict[str, str] = {}
    for sub in PAGE_DIRS:
        base = wiki_dir / sub
        if not base.is_dir():
            continue
        for f in base.rglob("*.md"):
            key = f.relative_to(wiki_dir).with_suffix("").as_posix()
            out[key] = domain_category(page_domain(f.read_text(encoding="utf-8")))
    return dict(sorted(out.items()))


def _stdout() -> None:
    for s in (sys.stdout, sys.stderr):
        try:
            # newline="\n"：Windows 文字模式預設把換行寫成 \r\n；`$(reporter_pages.py …)` 帶進
            # `git diff -- …` 時每個路徑尾巴會多一個 \r，只剩最後一個路徑對得上
            s.reconfigure(encoding="utf-8", errors="replace", newline="\n")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--category", help="類別中文：" + "、".join(CATEGORIES))
    g.add_argument("--all", action="store_true", help="印類別 → 頁數統計")
    ap.add_argument("--wiki-dir", type=Path, default=WIKI_DIR)
    args = ap.parse_args(argv)

    cats = page_categories(args.wiki_dir)
    if args.all:
        for c in (*CATEGORIES, UNCLASSIFIED):
            n = sum(1 for v in cats.values() if v == c)
            if n or c != UNCLASSIFIED:
                print(f"{c}\t{n}")
        print(f"合計\t{len(cats)}")
        for page, c in cats.items():
            if c == UNCLASSIFIED:
                print(f"  未分類：wiki/{page}.md")
        return 0
    if args.category not in CATEGORIES:
        print(f"❌ 不認得的類別「{args.category}」，可用：" + "、".join(CATEGORIES), file=sys.stderr)
        return 2
    for page, c in cats.items():
        if c == args.category:
            print(f"wiki/{page}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
