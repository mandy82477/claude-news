#!/usr/bin/env python3
"""build_flags_mentions.py — 實驗旗標的社群提及對帳：誰在談這個旗標？

給功能記者更新 wiki/topics/claude-code-experimental.md 用。頁上第一、二階的旗標名稱，
逐一到已抓進來的原料（src/gathered_archive/*.json，保留 14 天）與日報（news/*.md）
裡找字串命中，印出每個旗標的提及次數與來源連結。命中＝社群反應的證據；零命中就是零，
記者不得腦補「社群沒興趣」以外的結論。

表格解析靠**表頭欄名**（「旗標」與「階」兩欄），不靠欄序——記者加欄、換序都不會
靜默失效；找不到表或找不到這兩欄時 exit 2 並明說，和「頁上真的沒有第 1／2 階旗標」
（exit 0）分開講。（review 2026-09-16，P1-5）

用法：
    python scripts/build_flags_mentions.py                       # 讀頁上的旗標
    python scripts/build_flags_mentions.py --flags CLAUDE_CODE_X  # 指定旗標
    python scripts/build_flags_mentions.py --days 30

exit 0 對帳完成（含零旗標）｜exit 2 頁面表格解析失敗（格式改了，先修頁或修本腳本）。
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
STAGES_TO_CHECK = ("1", "2")


class PageFormatError(ValueError):
    """追蹤表找不到，或缺「旗標」／「階」欄。"""


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


VALID_STAGES = ("1", "2", "3", "4")


def parse_table(text: str) -> list[tuple[str, str]]:
    """追蹤表所有列 → [(旗標, 階)]。以表頭定位欄位；空行不結束表（記者分節手滑常見），
    第一個非空、非 `|` 的行才結束。階欄必須是 1–4 單一數字（`features/pages.md` 契約）；
    任何一列不是 → PageFormatError 並點名，不靜默跳過（review 2026-09-16 round 2，P2-A）。"""
    lines = text.splitlines()
    header_i = flag_col = stage_col = None
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = _cells(line)
        if "旗標" in cells and any(c == "階" for c in cells):
            header_i, flag_col, stage_col = i, cells.index("旗標"), cells.index("階")
            break
    if header_i is None:
        raise PageFormatError("追蹤表找不到：沒有同時含「旗標」與「階」兩欄的表頭")
    rows: list[tuple[str, str]] = []
    bad: list[str] = []
    for line in lines[header_i + 1:]:
        if not line.strip():
            continue                      # 空行不結束表
        if not line.startswith("|"):
            break                         # 表結束
        cells = _cells(line)
        if set(cells[0]) <= {"-", ":"}:
            continue                      # 分隔列
        if len(cells) <= max(flag_col, stage_col):
            bad.append(line.strip()[:60]); continue
        m = FLAG_RE.search(cells[flag_col])
        stage = cells[stage_col]
        if not m:
            bad.append(line.strip()[:60]); continue
        if stage not in VALID_STAGES:
            bad.append(f"{m.group(0)}：階欄「{stage}」不是 1–4 單一數字"); continue
        rows.append((m.group(0), stage))
    if bad:
        raise PageFormatError("有列無法辨識（階欄要 1–4 單一數字，備註寫別欄）：" + "；".join(bad[:5])
                              + (f"…共 {len(bad)} 列" if len(bad) > 5 else ""))
    return rows


def flags_on_page(text: str) -> list[str]:
    """追蹤表裡階欄為 1／2 的旗標（去重、保序）。"""
    out: list[str] = []
    for flag, stage in parse_table(text):
        if stage in STAGES_TO_CHECK and flag not in out:
            out.append(flag)
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
        hits = sorted((d for d in docs if flag in d.get("text", "")), key=lambda d: d["date"])
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

    if args.flags:
        flags = args.flags
    else:
        if not args.page.exists():
            print(f"頁面不存在：{args.page}")
            return 2
        try:
            rows = parse_table(args.page.read_text(encoding="utf-8"))
        except PageFormatError as e:
            print(f"表格解析失敗：{e}。頁面格式變了——修頁（表頭需含「旗標」「階」兩欄，階欄 1–4 單一數字）或修本腳本，不要當成「沒有旗標」。")
            return 2
        flags = []
        for flag, stage in rows:
            if stage in STAGES_TO_CHECK and flag not in flags:
                flags.append(flag)
        print(f"追蹤表 {len(rows)} 列，第 1／2 階 {len(flags)} 個")
        if not flags:
            print("頁上沒有第 1／2 階的旗標（表格解析正常），本輪無需對帳。")
            return 0
    print(f"對帳 {len(flags)} 個旗標")
    print(render(count_mentions(flags, load_docs(args.days)), args.days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
