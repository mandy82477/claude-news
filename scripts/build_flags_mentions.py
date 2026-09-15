#!/usr/bin/env python3
"""build_flags_mentions.py — 實驗旗標的社群提及對帳：誰在談這個旗標？

給功能記者更新 wiki/topics/claude-code-experimental.md 用。頁上第一、二階的旗標名稱，
逐一到已抓進來的原料（src/gathered_archive/*.json，保留 14 天）與日報（news/*.md）
裡找字串命中，印出每個旗標的提及次數與來源連結。命中＝社群反應的證據；零命中就是零，
記者不得腦補「社群沒興趣」以外的結論。

用法：
    python scripts/build_flags_mentions.py                       # 讀頁上的旗標
    python scripts/build_flags_mentions.py --flags CLAUDE_CODE_X  # 指定旗標
    python scripts/build_flags_mentions.py --days 30

輸出 markdown，直接貼進派工回報或頁面。exit 0 恆定（這是對帳工具，不是閘）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "wiki" / "topics" / "claude-code-experimental.md"
ARCHIVE = ROOT / "src" / "gathered_archive"
NEWS = ROOT / "news"
FLAG_RE = re.compile(r"CLAUDE_CODE_[A-Z0-9_]{3,}")
MAX_LINKS = 3


def flags_on_page(text: str) -> list[str]:
    """表格裡標第 1 或第 2 階的旗標（`` `CLAUDE_CODE_X` `` 在同一列且階欄為 1/2）。"""
    out: list[str] = []
    for line in text.splitlines():
        if not line.startswith("| `CLAUDE_CODE_"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[2] in ("1", "2"):
            m = FLAG_RE.search(cells[0])
            if m and m.group(0) not in out:
                out.append(m.group(0))
    return out


def load_docs(days: int, today: date | None = None) -> list[dict]:
    """原料與日報，各一份 {date, title, url, text}。純檔案讀取，無網路。"""
    today = today or date.today()
    cutoff = (today - timedelta(days=days)).isoformat()
    docs: list[dict] = []
    for f in sorted(ARCHIVE.glob("????-??-??.json")):
        if f.stem < cutoff:
            continue
        try:
            items = json.loads(f.read_text(encoding="utf-8")).get("items") or []
        except (OSError, ValueError):
            continue
        for it in items:
            docs.append({"date": f.stem, "title": it.get("title", ""), "url": it.get("url", ""),
                         "text": f"{it.get('title', '')}\n{it.get('summary', '')}"})
    for f in sorted(NEWS.glob("????-??-??.md")):
        if f.stem < cutoff:
            continue
        try:
            docs.append({"date": f.stem, "title": f"日報 {f.stem}", "url": f"news/{f.stem}.md",
                         "text": f.read_text(encoding="utf-8")})
        except OSError:
            continue
    return docs


def count_mentions(flags: list[str], docs: list[dict]) -> dict[str, dict]:
    """{flag: {"count": n, "links": [(date, title, url)…], "first": date|None}}，純函式。"""
    out: dict[str, dict] = {}
    for flag in flags:
        hits = [d for d in docs if flag in d.get("text", "")]
        hits.sort(key=lambda d: d["date"])
        out[flag] = {
            "count": len(hits),
            "first": hits[0]["date"] if hits else None,
            "links": [(d["date"], d["title"][:60], d["url"]) for d in hits[:MAX_LINKS]],
        }
    return out


def render(result: dict[str, dict], days: int) -> str:
    lines = [f"## 實驗旗標社群提及（近 {days} 天原料＋日報）", "",
             "| 旗標 | 提及 | 首見 | 來源（最多 3 筆） |", "|---|---|---|---|"]
    for flag, r in result.items():
        links = "；".join(f"[{t}]({u})（{d}）" for d, t, u in r["links"]) or "—"
        lines.append(f"| `{flag}` | {r['count']} | {r['first'] or '—'} | {links} |")
    zero = [f for f, r in result.items() if r["count"] == 0]
    lines += ["", f"零提及 {len(zero)} 個；有提及 {len(result) - len(zero)} 個。零提及只代表本站來源沒抓到，不代表沒人談。"]
    return "\n".join(lines)


def _use_utf8_stdout() -> None:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--flags", nargs="*", help="指定旗標；省略則讀頁上第 1／2 階的旗標")
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--page", type=Path, default=PAGE)
    args = ap.parse_args(argv)

    flags = args.flags or (flags_on_page(args.page.read_text(encoding="utf-8")) if args.page.exists() else [])
    if not flags:
        print("沒有要對帳的旗標（頁上無第 1／2 階旗標，或未指定 --flags）")
        return 0
    print(render(count_mentions(flags, load_docs(args.days)), args.days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
