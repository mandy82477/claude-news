#!/usr/bin/env python3
"""
check_reader_digest.py — 讀者版日報（daily/YYYY-MM-DD.md）格式閘。

用法：
    python scripts/check_reader_digest.py [YYYY-MM-DD]   # 指定日期
    python scripts/check_reader_digest.py                # 掃全部 daily/*.md

由 `.claude/skills/reader-digest/SKILL.md` 第 2 步呼叫。
規格（標題行、六領域節名、頁面小節、callout 首行、無新知行）住
`.claude/skills/reader-digest/references/format.md` 的「機械契約字串」表，本腳本是它的消費端；
兩端互相指認並登記於 .claude/review-registry.json 的 sync_pairs。

2026-09-13 改版「丙」：daily/ 由 scripts/build_reader_digest.py 從各頁頂部 callout 產出，
本閘看守的是「產出（或手改）的檔案，網站解析端還認得」：

  1. 標題行 `# YYYY-MM-DD 今天 wiki 學到什麼`，日期與檔名一致
  2. h2 節名必須是六個領域之一（拼錯的節名整段會在網站上消失，這是唯一的看守）
  3. 每個頁面小節 `### [[頁名|頁面標題]]` 必須在領域節底下，且頁名存在於 wiki/
  4. 頁面小節底下至少一行 `>` callout；首行 `> **標籤**（YYYY-MM-DD…）` 的日期須等於檔名日期
     （日期對不上＝抄到了別天的 callout，或有人手改了日期）
  5. 領域節底下、頁面小節之外不得有散落的 `>` 行（那些行不會上站）

內容本身（標籤字樣、字數、寫法）不查——那是各頁 callout 自己的事，規則在
`.claude/reporter-rules/wiki-ingest-format.md`「頂部 delta-first callout」。

行為：全過 exit 0；任何違規印出「檔案:行號 問題」後 exit 1。
「今日 wiki 無新知」的空日檔一律視為合法（它是規格要求的寫法，不是失敗）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT / "daily"
WIKI_DIR = ROOT / "wiki"

TITLE_RE = re.compile(r"^#\s+(\d{4}-\d{2}-\d{2})\s+今天 wiki 學到什麼\s*$")
NO_NEWS_RE = re.compile(r"^>\s*今日 wiki 無新知（(\d{4}-\d{2}-\d{2})）\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
# 與 build_web.READER_PAGE_RE／READER_CALLOUT_RE 同形（規格端見 format.md 契約表）
PAGE_RE = re.compile(r"^###\s+\[\[([^\]|]+?)(?:\|([^\]]*))?\]\]\s*$")
CALLOUT_RE = re.compile(r"^>\s*\*\*([^*\n]+?)\*\*\s*（(\d{4}-\d{2}-\d{2})[^）\n]*）(.*)$")

# 與 build_web.READER_DOMAIN_SECTIONS 同一組節名（規格端見 format.md 契約表）
DOMAIN_LABELS = [
    "🛠️ 功能",
    "🤖 模型",
    "💼 商業",
    "🏛️ 安全政策",
    "🌐 社群",
    "👤 人物",
]


def _valid_wiki_targets() -> set[str]:
    targets: set[str] = set()
    for sub, prefix in (("entities", "entities/"), ("topics", "topics/")):
        for f in (WIKI_DIR / sub).glob("*.md"):
            targets.add(f.stem)
            targets.add(prefix + f.stem)
    for f in WIKI_DIR.glob("*.md"):
        targets.add(f.stem)
    return targets


def check_file(f: Path, valid_targets: set[str]) -> list[str]:
    problems: list[str] = []
    try:
        rel = f.relative_to(ROOT)
    except ValueError:
        rel = f.name  # repo 外的檔（測試 tmp 目錄）也要檢查得動
    lines = f.read_text(encoding="utf-8").splitlines()

    title_seen = False
    no_news = False
    any_section = False
    current_label: str | None = None
    page_line: int | None = None      # 目前頁面小節的行號；None＝不在任何頁面小節
    page_quote_lines = 0

    def close_page():
        nonlocal page_line, page_quote_lines
        if page_line is not None and page_quote_lines == 0:
            problems.append(f"{rel}:{page_line} 頁面小節底下沒有任何 `>` callout 行，這頁在網站上會是空的")
        page_line, page_quote_lines = None, 0

    for n, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue

        m = TITLE_RE.match(stripped)
        if m:
            title_seen = True
            if m.group(1) != f.stem:
                problems.append(f"{rel}:{n} 標題日期 {m.group(1)} 與檔名 {f.stem} 不一致")
            continue

        if NO_NEWS_RE.match(stripped):
            no_news = True
            continue

        h = H2_RE.match(stripped)
        if h:
            close_page()
            label = h.group(1).strip()
            if label not in DOMAIN_LABELS:
                problems.append(f"{rel}:{n} 節名「{label}」不在六個領域內，該段在網站上會整段消失")
                current_label = None
            else:
                current_label = label
                any_section = True
            continue

        pm = PAGE_RE.match(stripped)
        if pm:
            close_page()
            if current_label is None:
                problems.append(f"{rel}:{n} 頁面小節不在任何領域節底下，不會上站")
                continue
            target = pm.group(1).split("#")[0].replace("\\", "").strip()
            if target not in valid_targets:
                problems.append(f"{rel}:{n} 頁面小節 [[{target}]] 指向不存在的 wiki 頁")
            page_line = n
            continue

        if stripped.startswith(">"):
            if current_label is None:
                continue  # 第一個領域節之前的總結句（產生器不寫，手寫時容許）
            if page_line is None:
                problems.append(f"{rel}:{n} `>` 行散落在頁面小節之外，不會上站")
                continue
            if page_quote_lines == 0:
                cm = CALLOUT_RE.match(stripped)
                if not cm:
                    problems.append(f"{rel}:{n} callout 首行不是 `> **標籤**（YYYY-MM-DD…）` 形狀，網站上標籤與日期會空白")
                elif cm.group(2) != f.stem:
                    problems.append(f"{rel}:{n} callout 日期 {cm.group(2)} 與檔名 {f.stem} 不一致——抄到了別天的最新動態")
            page_quote_lines += 1
            continue

    close_page()

    if not title_seen:
        problems.append(f"{rel}:1 缺標題行 `# {f.stem} 今天 wiki 學到什麼`")
    if not no_news and not any_section:
        problems.append(f"{rel}:1 既無領域節也無「今日 wiki 無新知」行，內容為空")

    return problems


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    valid = _valid_wiki_targets()
    if len(argv) > 1:
        files = [DAILY_DIR / f"{argv[1]}.md"]
        if not files[0].exists():
            print(f"FAIL: {files[0]} 不存在")
            return 1
    else:
        files = sorted(DAILY_DIR.glob("*.md"))

    problems: list[str] = []
    for f in files:
        problems.extend(check_file(f, valid))

    if problems:
        print(f"讀者版日報格式檢查：{len(problems)} 筆違規")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"讀者版日報格式檢查：{len(files)} 份全過")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
