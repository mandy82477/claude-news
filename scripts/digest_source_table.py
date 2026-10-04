#!/usr/bin/env python3
"""digest_source_table.py — 產生日報檔尾 📡 來源狀態表（三種口徑並列、加總對得上標頭）。

為什麼有這支（2026-10-04）：日報標頭「文章數 N」是去重＋相關性篩選後交給 Step 1b
的候選數（gathered_items.json 的 article_count），檔尾來源表的「條數」卻是各來源
原始抓到數（source_status.count，含重複與不相關）——兩個口徑擺在同一份檔、沒標明，
10-02 標頭 59、表格相加 99，冷讀者讀成「數字對不攏」；表上寫 Reddit 10 條、正文
卻 0 則，又被讀成漏刊。表的第三欄仍須是原始抓到數（`/wiki-lint` 6e 靠它判斷來源
是否壞掉、`build_web.py` SOURCE_TABLE_RE 只取第三欄），所以不換欄義，改成三欄並列：

    | 來源 | 狀態 | 抓到 | 進候選 | 刊出 |

- 抓到   ＝source_status.count（原始抓取，含重複與不相關）
- 進候選 ＝gathered_items.json items 中以該來源為勝出來源的條數；全表加總＝標頭文章數
- 刊出   ＝其中 URL 有出現在日報正文的條數（日報檔不存在時為 0）

口徑說明行（CALIBER_LINE）固定寫在表格正下方，是檔案最後一行。

用法：
    python scripts/digest_source_table.py YYYY-MM-DD            # 印出 📡 區塊
    python scripts/digest_source_table.py YYYY-MM-DD --write    # 就地改寫 news/YYYY-MM-DD.md 的表

資料來源：`src/gathered_items.json`（date 須等於目標日），否則退回
`src/gathered_archive/YYYY-MM-DD.json`；兩者皆無 → exit 2。
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GATHERED = REPO_ROOT / "src" / "gathered_items.json"
ARCHIVE_DIR = REPO_ROOT / "src" / "gathered_archive"
NEWS_DIR = REPO_ROOT / "news"

SECTION_HEADING = "### 📡 來源狀態"
TABLE_HEADER = "| 來源 | 狀態 | 抓到 | 進候選 | 刊出 |"
TABLE_SEP = "|------|------|------|------|------|"
CALIBER_LINE = ("> 抓到＝各來源原始抓取數（含重複與不相關）；進候選＝去重與相關性篩選後"
                "交給編輯的條數，加總即標頭文章數；刊出＝實際寫進本日報的條數。")
URL_RE = re.compile(r"\]\((https?://[^)\s]+)\)")


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def label_prefix(label: str) -> str:
    """與 src/news_aggregator/main.py `_label_prefix` 同規則：取 ` / `、` · ` 之前。"""
    return (label or "").split(" / ")[0].split(" · ")[0].strip()


def map_to_registered(prefix: str, registered: list[str]) -> str | None:
    """與 main.py `_map_prefix_to_registered` 同規則：先全等，再前綴互含。"""
    if not prefix:
        return None
    if prefix in registered:
        return prefix
    for name in registered:
        if prefix.startswith(name) or name.startswith(prefix):
            return name
    return None


def load_gathered(date: str, gathered: Path = GATHERED,
                  archive_dir: Path = ARCHIVE_DIR) -> dict | None:
    for path in (gathered, archive_dir / f"{date}.json"):
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            if data.get("date") == date:
                return data
    return None


def build_rows(data: dict, digest_text: str = "") -> list[dict]:
    status = data.get("source_status") or {}
    registered = list(status.keys())
    rows = {name: {"name": name, "ok": bool(s.get("ok")), "gathered": int(s.get("count", 0)),
                   "candidates": 0, "published": 0}
            for name, s in status.items()}
    published_urls = set(URL_RE.findall(digest_text))
    for it in data.get("items") or []:
        name = map_to_registered(label_prefix(it.get("source", "")), registered)
        if name is None:
            name = "（未對應來源）"
            rows.setdefault(name, {"name": name, "ok": True, "gathered": 0,
                                   "candidates": 0, "published": 0})
        rows[name]["candidates"] += 1
        if it.get("url") in published_urls:
            rows[name]["published"] += 1
    return list(rows.values())


def render_table(rows: list[dict]) -> list[str]:
    out = [TABLE_HEADER, TABLE_SEP]
    for r in rows:
        icon = "✅" if r["ok"] else "❌"
        out.append(f"| {r['name']} | {icon} | {r['gathered']} | {r['candidates']} | {r['published']} |")
    out += ["", CALIBER_LINE]
    return out


def rewrite_digest(text: str, table_lines: list[str]) -> str:
    """把 📡 區塊的表格（含舊口徑行）換成新表；表上方的 `>` 說明行原樣保留。

    區塊不存在就補在檔尾。"""
    lines = text.rstrip("\n").splitlines()
    idx = next((i for i, l in enumerate(lines) if l.strip().startswith(SECTION_HEADING)), None)
    if idx is None:
        return "\n".join(lines + ["", SECTION_HEADING, ""] + table_lines) + "\n"
    head = lines[: idx + 1]
    keep: list[str] = []
    for l in lines[idx + 1:]:
        s = l.strip()
        if s.startswith("|") or s == CALIBER_LINE or s.startswith("> 抓到＝"):
            continue
        if s.startswith("#"):
            break  # 不吞後面意外存在的其他區塊——但規格上 📡 是最後一區
        keep.append(l)
    while keep and not keep[-1].strip():
        keep.pop()
    while keep and not keep[0].strip():
        keep.pop(0)
    body = [""] + keep + ([""] if keep else []) + table_lines
    return "\n".join(head + body) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("date")
    ap.add_argument("--write", action="store_true", help="就地改寫 news/DATE.md 的 📡 表")
    args = ap.parse_args(argv)
    out = _stdout()

    data = load_gathered(args.date)
    if data is None:
        print(f"❌ 找不到 {args.date} 的 gathered_items（src/gathered_items.json 日期不符、"
              f"archive 也沒有）", file=out)
        return 2
    digest = NEWS_DIR / f"{args.date}.md"
    text = digest.read_text(encoding="utf-8-sig") if digest.exists() else ""
    rows = build_rows(data, text)
    table = render_table(rows)
    total = sum(r["candidates"] for r in rows)
    n = data.get("article_count", len(data.get("items") or []))
    if args.write:
        if not digest.exists():
            print(f"❌ {digest} 不存在；先寫日報正文再跑 --write", file=out)
            return 2
        digest.write_text(rewrite_digest(text, table), encoding="utf-8")
        print(f"✅ 已改寫 {digest.name} 的來源狀態表（進候選合計 {total}＝標頭文章數 {n}）", file=out)
    else:
        print("\n".join([SECTION_HEADING, ""] + table), file=out)
    if total != n:
        print(f"⚠️ 進候選合計 {total} ≠ article_count {n}——gathered_items.json 自相矛盾，查抓料端", file=out)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
