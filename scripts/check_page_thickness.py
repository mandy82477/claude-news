#!/usr/bin/env python3
"""check_page_thickness.py — 厚頁清單：正文逾 600 行的 wiki 頁，以及它們有沒有交代切法。

**為什麼需要：** `page-lifecycle.md`「一頁一故事」規定正文逾 600 行就必須交代切法（拆子頁，
或寫出不拆的理由）。2026-09 到 10 月的 17 波頁面審查沒拆過任何一頁，`community-tech-patterns`
從 1,135 行長到 2,486 行，中間沒有任何機械訊號——厚度只在審查波開健檢卡時才被看到。
本腳本每週在 `/wiki-lint` 5o 跑，只回報不擋：拆頁不是 ingest 能做的事，擋了只會讓日更紅燈。

**量什麼：**
  - 正文行數＝檔案行數 − frontmatter − `%% … %%` 維運備忘；archive 頁、log、CLAUDE.md 不算
  - 事件流佔比＝`## 技術彙整`／`## 時序`／`## 歷史記錄` 這類 `### YYYY-MM` 分組節的行數比例
  - 交代＝頁面 `%%` 備忘裡的一行 `拆頁評估 YYYY-MM-DD：…`（拆／不拆都寫；不拆的理由只有三種）
    逾 `STALE_DAYS` 天沒交代的標 ⚠️

exit 恆 0（報告型）。`--json` 給機器讀。

用法：
    python scripts/check_page_thickness.py [--threshold 600] [--stale-days 60] [--json]
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO / "wiki"
THRESHOLD = 600
STALE_DAYS = 60
EVENT_FLOW_HEADINGS = ("技術彙整", "時序", "歷史記錄", "事件流", "編年")
ASSESS_RE = re.compile(r"拆頁評估\s*(\d{4}-\d{2}-\d{2})\s*[：:]\s*(.+)")


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def content_pages(wiki_dir: Path = WIKI_DIR) -> list[Path]:
    """只看會長大的內容頁：topics／entities，排除 archive、轉址殼（已併回）、index／log／規則。"""
    out = []
    for sub in ("topics", "entities"):
        for p in sorted((wiki_dir / sub).glob("*.md")):
            if p.stem.endswith("-archive"):
                continue
            out.append(p)
    return out


def body_lines(text: str) -> list[str]:
    """去 frontmatter、去 `%% … %%` 區塊後的行。"""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
    out: list[str] = []
    in_memo = False
    for line in lines:
        s = line.strip()
        if not in_memo and s.startswith("%%") and not (s.endswith("%%") and len(s) > 2):
            in_memo = True
            continue
        if in_memo:
            if "%%" in s:
                in_memo = False
            continue
        if s.startswith("%%") and s.endswith("%%"):
            continue
        out.append(line)
    return out


def event_flow_share(lines: list[str]) -> float:
    """`## 技術彙整` 這類節底下 `### YYYY-MM` 分組的行數佔正文比例。"""
    total = len(lines) or 1
    counted = 0
    in_section = False
    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            in_section = any(k in title for k in EVENT_FLOW_HEADINGS)
            continue
        if in_section:
            counted += 1
    return counted / total


def assessment(text: str, today: date) -> tuple[date | None, str, bool]:
    """最近一筆 `拆頁評估 YYYY-MM-DD：…`；回 (日期, 內容, 是否過期)。"""
    found = [(datetime.strptime(m.group(1), "%Y-%m-%d").date(), m.group(2).strip()) for m in ASSESS_RE.finditer(text)]
    if not found:
        return None, "", True
    d, note = max(found)
    return d, note, (today - d).days > STALE_DAYS


def rows(wiki_dir: Path = WIKI_DIR, threshold: int = THRESHOLD, today: date | None = None) -> list[dict]:
    today = today or date.today()
    out = []
    for p in content_pages(wiki_dir):
        text = p.read_text(encoding="utf-8-sig")
        lines = body_lines(text)
        n = len(lines)
        if n <= threshold:
            continue
        d, note, stale = assessment(text, today)
        out.append({
            "page": f"{p.parent.name}/{p.stem}",
            "lines": n,
            "event_flow_share": round(event_flow_share(lines), 2),
            "assessed": d.isoformat() if d else None,
            "assessment": note,
            "stale": stale,
        })
    return sorted(out, key=lambda r: -r["lines"])


def render(result: list[dict], threshold: int) -> str:
    if not result:
        return f"厚頁清單（5o）：0 頁逾 {threshold} 行"
    overdue = sum(1 for r in result if r["stale"])
    head = f"厚頁清單（5o）：{len(result)} 頁逾 {threshold} 行／{overdue} 頁逾 {STALE_DAYS} 天未交代切法"
    body = []
    for r in result:
        flag = "⚠️" if r["stale"] else "✅"
        when = f"評估 {r['assessed']}：{r['assessment'][:60]}" if r["assessed"] else "從未評估"
        body.append(f"  {flag} {r['page']}：{r['lines']} 行（事件流 {int(r['event_flow_share'] * 100)}%）｜{when}")
    return head + "\n" + "\n".join(body)


def main(argv: list[str] | None = None) -> int:
    global STALE_DAYS
    ap = argparse.ArgumentParser(description="厚頁清單（報告型，exit 恆 0）")
    ap.add_argument("--threshold", type=int, default=THRESHOLD)
    ap.add_argument("--stale-days", type=int, default=STALE_DAYS)
    ap.add_argument("--json", action="store_true")
    ns = ap.parse_args(argv)
    STALE_DAYS = ns.stale_days
    out = _stdout()
    result = rows(threshold=ns.threshold)
    out.write((json.dumps(result, ensure_ascii=False, indent=1) if ns.json else render(result, ns.threshold)) + "\n")
    out.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
