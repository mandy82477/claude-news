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

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
DAILY_DIR = ROOT / "daily"
NEWS_DIR = ROOT / "news"
ATTRIBUTION = ROOT / "data" / "source_attribution.jsonl"   # 記者歸因帳本：{date, page, item_url, …} 一行一筆

# 標題行 `# YYYY-MM-DD 今天 wiki 學到什麼`（build_web.READER_TITLE_RE 的產出端）
TITLE_FMT = "# {date} 今天 wiki 學到什麼"
NO_NEWS_FMT = "> 今日 wiki 無新知（{date}）"
# 頁面小節 `### [[頁名|頁面標題]]`（build_web.READER_PAGE_RE 的產出端）
PAGE_HEADING_FMT = "### [[{page}|{name}]]"
# 頂部兩節：從 news/TARGET_DATE.md 原樣搬來的 📌 今日聚焦，與剔除聚焦已講過事件後的 ⭐ 重點話題（≤5 則）。
# 節名住 format.md 契約表；build_web 對 daily/ 只認六領域，這兩節在網站上的資料仍取自 news/ 解析結果
# （build_web.attach_reader_digests 的 readerTopStories 做同一套剔重），這裡是給 Obsidian 讀者的完整版。
FOCUS_SECTION = "## 📌 今日聚焦"
TOP_SECTION = "## ⭐ 重點話題"
TOP_MAX = 5
NEWS_FOCUS_H3 = "### 📌 今日聚焦"
NEWS_TOP_H3 = "### ⭐ 重點話題"
NEWS_H3_RE = re.compile(r"^###\s")
MD_URL_RE = re.compile(r"\((https?://[^\s()]+)\)")
NEWS_TOP_TITLE_RE = re.compile(r"^\*\*\[(.+?)\]\((https?://[^\s()]+)\)\*\*\s*$")
NEWS_TOP_SOURCE_RE = re.compile(r"^`[^`]+`\s*·")
# 頁內路標：callout 投影到日報後這些指涉沒有東西可指（規則端：page-templates.md「脫離頁面也要讀得懂」）
# ⟨G-11⟩ 這類頁內編號、「見『## 節』」「詳見下方表格」、以及沒有頁名的同頁錨點 [[#節]]
PAGE_INTERNAL_RE = re.compile(
    r"⟨[^⟩\n]{1,16}⟩"
    r"|[詳參]?見\s*[「『]?\s*##"
    r"|[詳參]?見[上下]方"
    r"|[上下]方(?:的)?[^\s，。；]{0,8}(?:表格?|列|節|段)"
    r"|\[\[#[^\]]+\]\]"
    r"|[詳參]?見\s*[「『][^」』\n]{1,24}[」』]"            # 見『IPO 走到哪一格』——引號包頁內小標題，沒有可點的連結
    r"|[「『][^」』\n]{1,24}[」』]\s*(?:細節區|欄|列)"  # 『押對了嗎』欄
)

# 頁頂 callout 首行：`> **標籤**（YYYY-MM-DD…）`——與 scripts/check_hierarchy.py 的
# CALLOUT_DATE_RE 看同一件事（那邊只要日期，這邊還要標籤與同行尾巴）。
# 括號內日期後可接「，補充」或「 重寫」等尾巴，但 `（` 後必須緊接日期——
# `> ❓ **待查證**（標 2026-09-09｜…）` 這類懸置標記因此不會被當成最新動態。
CALLOUT_RE = re.compile(r"^>\s*\*\*(?P<label>[^*\n]+?)\*\*\s*（(?P<date>\d{4}-\d{2}-\d{2})[^）\n]*）(?P<rest>.*)$")
FRONTMATTER_DOMAIN_RE = re.compile(r"^domain:\s*\"?([^\"\n]+?)\"?\s*$", re.M)
# frontmatter 是 gen_wiki_frontmatter.py 事後重算的；機器每日覆寫的頁（如 skill-interest-watch）
# 在重算前沒有 frontmatter，退回讀標頭「領域」欄（兩者本就同源）
HEADER_DOMAIN_RE = re.compile(r"^\*\*領域[：:]\*\*\s*(.+?)\s*$", re.M)
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
    # 頁首止於第一條 `---`；沒有分隔線的頁（少數人物殼頁）止於第一個 `## ` 節，
    # 免得正文裡帶日期的引述被當成頁頂 callout
    parts = re.split(r"^(?:---\s*|##\s.*)$", after, maxsplit=1, flags=re.M)
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
    """頁首有粗體 callout、括號裡沒有任何完整 YYYY-MM-DD——多半是日期寫成「07-10」這種短格式，
    lint 用的 WARN 訊號。括號內有完整日期但不在開頭的（如「（快照 2026-09-12）」）視為刻意不投影，不警告。"""
    bold = [l for l in head.splitlines() if re.match(r"^>\s*\*\*", l)]
    if not bold or any(CALLOUT_RE.match(l) for l in bold):
        return False
    return not any(re.search(r"（[^）]*\d{4}-\d{2}-\d{2}", l) for l in bold)


def news_sections(news_md: str) -> tuple[list[str], list[str]]:
    """news/ 日報 → (📌 今日聚焦的條列行, ⭐ 重點話題的原始行)。找不到的節回空 list。"""
    def block(h3: str) -> list[str]:
        lines = news_md.splitlines()
        try:
            i = next(k for k, l in enumerate(lines) if l.strip() == h3)
        except StopIteration:
            return []
        out = []
        for l in lines[i + 1:]:
            if NEWS_H3_RE.match(l):
                break
            out.append(l.rstrip())
        return out
    focus = [l for l in block(NEWS_FOCUS_H3) if l.startswith("- ")]
    return focus, block(NEWS_TOP_H3)


def top_stories_minus_focus(top_lines: list[str], focus_urls: set[str], limit: int = TOP_MAX) -> list[list[str]]:
    """⭐ 原始行 → 每則 [標題行, 內文行…]，剔掉 URL 已在聚焦裡的、剔掉來源行，最多 limit 則。"""
    stories: list[list[str]] = []
    cur: list[str] | None = None
    for l in top_lines:
        m = NEWS_TOP_TITLE_RE.match(l.strip())
        if m:
            cur = [l.strip()] if m.group(2) not in focus_urls else None
            if cur is not None:
                stories.append(cur)
            continue
        if cur is None or not l.strip() or NEWS_TOP_SOURCE_RE.match(l.strip()):
            continue
        cur.append(l.strip())
    return stories[:limit]


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
            dm = FRONTMATTER_DOMAIN_RE.search(raw) or HEADER_DOMAIN_RE.search(raw)
            domain = dm.group(1).strip() if dm else ""
            section = DOMAIN_TO_SECTION.get(domain)
            if not section:
                warnings.append(f"{page}：frontmatter domain={domain!r} 不在六領域內，當日 callout 未收")
                continue
            for b in hits:
                hit_txt = "\n".join(b)
                pm = PAGE_INTERNAL_RE.search(hit_txt)
                if pm:
                    warnings.append(f"{page}：callout 含頁內路標「{pm.group(0)}」，投影進日報後讀者無處可指——改成 [[頁#節]] 完整連結或白話說明")
            im = FRONTMATTER_INBOUND_RE.search(raw)
            sections[section].append({
                "page": page,
                "name": name or f.stem,
                "lines": [l for b in hits for l in (b + [""])][:-1],
                "inbound": int(im.group(1)) if im else 0,
                "raw": raw,
            })
    for items in sections.values():
        items.sort(key=lambda it: (-it["inbound"], it["page"]))
    return sections, warnings


def render(target_date: str, sections: dict[str, list[dict]],
           focus_lines: list[str] | None = None, top_stories: list[list[str]] | None = None) -> str:
    out = [TITLE_FMT.format(date=target_date), ""]
    if focus_lines:
        out += [FOCUS_SECTION, "", *focus_lines, ""]
    if top_stories:
        out += [TOP_SECTION, ""]
        for st in top_stories:
            out += [*st, ""]
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


def attributed_urls(target_date: str, ledger: Path = ATTRIBUTION) -> set[str]:
    """記者當日歸因帳本裡的 item_url——某則來源被任一記者收進任一頁的證據。"""
    urls: set[str] = set()
    if not ledger.exists():
        return urls
    for line in ledger.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("date") == target_date and rec.get("item_url"):
            urls.add(rec["item_url"])
    return urls


PAGE_HEADING_RE = re.compile(r"^###\s+\[\[([^\]|]+?)(?:\|([^\]]*))?\]\]\s*$")


def frozen_pages(existing: str) -> dict[str, tuple[str, str, list[str]]]:
    """既有 daily 檔 → {頁路徑: (節名, 頁面標題, 該頁的 callout 行)}。
    callout 每天覆寫，昨天的日報若隔天重產，昨天那頁的 callout 已經是今天的日期、收不到——
    日報是不可改的過去，所以重產時把既有檔裡這些頁原樣留住（`wiki/CLAUDE.md`：log 是不可改的過去）。"""
    out: dict[str, tuple[str, str, list[str]]] = {}
    section = ""
    cur: str | None = None
    for line in existing.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            section = h.group(1).strip(); cur = None
            continue
        pm = PAGE_HEADING_RE.match(line)
        if pm and section in SECTION_ORDER:
            cur = pm.group(1).strip()
            out[cur] = (section, (pm.group(2) or "").strip(), [])
            continue
        if cur and line.startswith(">"):
            out[cur][2].append(line.rstrip())
    return {k: v for k, v in out.items() if v[2]}


def generate(target_date: str, wiki_dir: Path = WIKI_DIR, news_dir: Path = NEWS_DIR,
             ledger: Path = ATTRIBUTION, existing: str | None = None) -> tuple[str, int, list[str]]:
    sections, warnings = collect(target_date, wiki_dir)
    if existing:
        have = {it["page"] for items in sections.values() for it in items}
        kept = 0
        for page, (section, name, lines) in frozen_pages(existing).items():
            if page in have or section not in sections:
                continue
            sections[section].append({"page": page, "name": name, "lines": lines, "inbound": -1, "raw": ""})
            kept += 1
        if kept:
            warnings.append(f"保留既有檔 {kept} 頁（其 callout 已被後一天覆寫，日報是不可改的過去）")
        for items in sections.values():
            items.sort(key=lambda it: (-it["inbound"], it["page"]))
    focus_lines: list[str] = []
    top_stories: list[list[str]] = []
    news_f = news_dir / f"{target_date}.md"
    if news_f.exists():
        focus_lines, top_raw = news_sections(news_f.read_text(encoding="utf-8"))
        focus_urls = {u for l in focus_lines for u in MD_URL_RE.findall(l)}
        top_stories = top_stories_minus_focus(top_raw, focus_urls)
        # 乙版放棄的那層保險，機械撿回：聚焦每條的來源 URL，既不在記者當日歸因帳本、
        # 也沒被任何今日覆寫 callout 的頁寫進正文 → 多半是記者漏收，點名出來給人判斷
        today_raw = "\n".join(it["raw"] for items in sections.values() for it in items)
        attributed = attributed_urls(target_date, ledger)
        for n, l in enumerate(focus_lines, 1):
            urls = MD_URL_RE.findall(l)
            if urls and not any(u in attributed or u in today_raw for u in urls):
                warnings.append(f"聚焦第 {n} 條的來源既不在當日歸因帳本、也未出現在今日更新的頁——記者可能漏收：{l[:60]}…")
    text = render(target_date, sections, focus_lines, top_stories)
    return text, sum(len(v) for v in sections.values()), warnings


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows cp950 主控台印 emoji 會炸
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        print("用法：python scripts/build_reader_digest.py YYYY-MM-DD [--stdout]")
        return 2
    target_date = args[0]
    out_path = DAILY_DIR / f"{target_date}.md"
    existing = out_path.read_text(encoding="utf-8") if out_path.exists() and "--stdout" not in argv else None
    text, count, warnings = generate(target_date, existing=existing)
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
