#!/usr/bin/env python3
"""
build_reader_digest.py — 讀者版日報（daily/YYYY-MM-DD.md）產生器。

用法：
    python scripts/build_reader_digest.py YYYY-MM-DD            # 寫 daily/YYYY-MM-DD.md
    python scripts/build_reader_digest.py YYYY-MM-DD --stdout   # 只印不寫

由 `.claude/skills/reader-digest/SKILL.md`（Step 2b）呼叫。

做法（2026-09-13 改版「丙」）：讀者版不再由 LLM 讀 wiki diff 重新消化，而是把各頁頂部
「最新動態」callout 原樣搬出來——記者當天覆寫過的 callout（括號日期＝TARGET_DATE）就是
該頁的最新動態，日報只是它們按六領域排好的投影。每個事實只有一個家（頁頂 callout），
日報不再是第二份消化。

挑選規則（規格端：`.claude/skills/reader-digest/references/format.md`）：
  - 只掃 wiki/entities/ 與 wiki/topics/ 的頁首（H1 到第一條 `---` 之間）
  - 一段 `>` 引述區塊，首行形如 `> **標籤**（YYYY-MM-DD…）`，且日期 == TARGET_DATE 才收；
    標籤自由（最新動態／最新判讀／本週衝擊…都算），內容自由——本腳本不改一字
  - 沒有 frontmatter `domain` 或值不在六領域者跳過並 WARN（不會靜默消失）
  - 一頁可有多個當日 callout（如 market-signals 的 ⚠️ 免責＋最新判讀），全部照抄
  - 零命中 → 只寫標題加 `> 今日 wiki 無新知（TARGET_DATE）`

輸出形狀（`build_web.parse_reader_digest` 與 `check_reader_digest.py` 的消費契約）：
    # YYYY-MM-DD 今天 wiki 學到什麼
    ## 🛠️ 功能
    ### [[entities/claude-code|Claude Code]]
    > **最新動態**（YYYY-MM-DD）
    > - …（callout 原文）
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
DAILY_DIR = ROOT / "daily"

# 標題行 `# YYYY-MM-DD 今天 wiki 學到什麼`（build_web.READER_TITLE_RE 的產出端）
TITLE_FMT = "# {date} 今天 wiki 學到什麼"
NO_NEWS_FMT = "> 今日 wiki 無新知（{date}）"
# 頁面小節 `### [[頁名|頁面標題]]`（build_web.READER_PAGE_RE 的產出端）
PAGE_HEADING_FMT = "### [[{page}|{name}]]"

# 頁頂 callout 首行：`> **標籤**（YYYY-MM-DD…）`——與 scripts/check_hierarchy.py 的
# CALLOUT_DATE_RE 看同一件事（那邊只要日期，這邊還要標籤與同行尾巴）。
# 括號內日期後可接「，補充」或「 重寫」等尾巴，但 `（` 後必須緊接日期——
# `> ❓ **待查證**（標 2026-09-09｜…）` 這類懸置標記因此不會被當成最新動態。
CALLOUT_RE = re.compile(r"^>\s*\*\*(?P<label>[^*\n]+?)\*\*\s*（(?P<date>\d{4}-\d{2}-\d{2})[^）\n]*）(?P<rest>.*)$")
FRONTMATTER_DOMAIN_RE = re.compile(r"^domain:\s*\"?([^\"\n]+?)\"?\s*$", re.M)
FRONTMATTER_INBOUND_RE = re.compile(r"^inbound_links:\s*(\d+)\s*$", re.M)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)

# wiki 標頭「領域」欄的六個值 → 讀者版六個節名（節名的家：format.md 契約表；
# build_web.READER_DOMAIN_SECTIONS／check_reader_digest.DOMAIN_LABELS 同源）
DOMAIN_TO_SECTION = {
    "🛠️ 工具/功能": "🛠️ 功能",
    "🤖 模型":      "🤖 模型",
    "💼 商業":      "💼 商業",
    "🏛️ 政策/安全": "🏛️ 安全政策",
    "🌐 社群":      "🌐 社群",
    "👤 人物":      "👤 人物",
}
SECTION_ORDER = ["🛠️ 功能", "🤖 模型", "💼 商業", "🏛️ 安全政策", "🌐 社群", "👤 人物"]


def page_head(raw: str) -> tuple[str, str]:
    """回傳 (H1 標題, 頁首區塊文字)。頁首 = H1 之後到第一條 `---` 分隔線之前。"""
    m = H1_RE.search(raw)
    if not m:
        return "", ""
    after = raw[m.end():]
    parts = re.split(r"^---\s*$", after, maxsplit=1, flags=re.M)
    return m.group(1).strip(), parts[0]


def dated_callouts(head: str, target_date: str) -> list[list[str]]:
    """頁首裡首行帶 target_date 的 `>` 區塊，每塊回傳原始行（含 `>` 前綴）。"""
    blocks: list[list[str]] = []
    cur: list[str] = []
    for line in head.splitlines():
        if line.startswith(">"):
            cur.append(line.rstrip())
        else:
            if cur:
                blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    hits = []
    for b in blocks:
        m = CALLOUT_RE.match(b[0])
        if m and m.group("date") == target_date:
            hits.append(b)
    return hits


def has_undated_callout(head: str) -> bool:
    """頁首有粗體 callout 但沒有一個帶可解析日期——lint 用的 WARN 訊號。"""
    bold = [l for l in head.splitlines() if re.match(r"^>\s*\*\*", l)]
    return bool(bold) and not any(CALLOUT_RE.match(l) for l in bold)


def collect(target_date: str, wiki_dir: Path = WIKI_DIR) -> tuple[dict[str, list[dict]], list[str]]:
    """回傳 ({節名: [item…]}, warnings)。item = {page, name, lines, inbound}。"""
    sections: dict[str, list[dict]] = {s: [] for s in SECTION_ORDER}
    warnings: list[str] = []
    for sub in ("entities", "topics"):
        for f in sorted((wiki_dir / sub).glob("*.md")):
            raw = f.read_text(encoding="utf-8")
            name, head = page_head(raw)
            page = f"{sub}/{f.stem}"
            hits = dated_callouts(head, target_date)
            if not hits:
                if has_undated_callout(head):
                    warnings.append(f"{page}：頁首 callout 沒有可解析的（YYYY-MM-DD）日期，永遠不會進讀者版")
                continue
            dm = FRONTMATTER_DOMAIN_RE.search(raw)
            domain = dm.group(1).strip() if dm else ""
            section = DOMAIN_TO_SECTION.get(domain)
            if not section:
                warnings.append(f"{page}：frontmatter domain={domain!r} 不在六領域內，當日 callout 未收")
                continue
            im = FRONTMATTER_INBOUND_RE.search(raw)
            sections[section].append({
                "page": page,
                "name": name or f.stem,
                "lines": [l for b in hits for l in (b + [""])][:-1],
                "inbound": int(im.group(1)) if im else 0,
            })
    for items in sections.values():
        items.sort(key=lambda it: (-it["inbound"], it["page"]))
    return sections, warnings


def render(target_date: str, sections: dict[str, list[dict]]) -> str:
    out = [TITLE_FMT.format(date=target_date), ""]
    total = sum(len(v) for v in sections.values())
    if total == 0:
        out.append(NO_NEWS_FMT.format(date=target_date))
        return "\n".join(out) + "\n"
    for label in SECTION_ORDER:
        items = sections[label]
        if not items:
            continue
        out.append(f"## {label}")
        out.append("")
        for it in items:
            out.append(PAGE_HEADING_FMT.format(page=it["page"], name=it["name"]))
            out.append("")
            out.extend(it["lines"])
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def generate(target_date: str, wiki_dir: Path = WIKI_DIR) -> tuple[str, int, list[str]]:
    sections, warnings = collect(target_date, wiki_dir)
    return render(target_date, sections), sum(len(v) for v in sections.values()), warnings


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows cp950 主控台印 emoji 會炸
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        print("用法：python scripts/build_reader_digest.py YYYY-MM-DD [--stdout]")
        return 2
    target_date = args[0]
    text, count, warnings = generate(target_date)
    for w in warnings:
        print(f"  WARN: {w}")
    if "--stdout" in argv:
        print(text)
    else:
        DAILY_DIR.mkdir(exist_ok=True)
        out = DAILY_DIR / f"{target_date}.md"
        out.write_text(text, encoding="utf-8")
        print(f"讀者版日報 {out.relative_to(ROOT)}：{count} 頁當日最新動態（WARN {len(warnings)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
