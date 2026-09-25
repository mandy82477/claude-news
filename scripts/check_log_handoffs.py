#!/usr/bin/env python3
"""check_log_handoffs.py — wiki/log.md 的「轉知」必須對得到轉知帳本單號。

log 沒有腳本讀來派工；派工附件只來自 `data/pending-handoffs.jsonl`
（`scripts/pending_handoffs.py list`）。所以 log 裡寫了「轉知」卻沒登帳的交辦，
下一輪不會有任何記者收到——事實上遺失。本閘讓這種行當場變紅。

規則（逐行，只看當日 `## D Ingest` 區段）：
  含「轉知」的行必須帶帳本單號 `H-xxxxxx`，或明寫「不登帳：<理由>」；
  帶的單號必須真的在帳本裡（打錯號＝對不上帳）。

用法：
    python scripts/check_log_handoffs.py --date 2026-09-24   # 查指定日（不論新舊）
    python scripts/check_log_handoffs.py                     # 查 ENFORCE_FROM 起所有 Ingest 區段

不帶 --date 時只查 ENFORCE_FROM 當天以後的區段：之前的 log 是不可改的過去，
append only 修不掉，全掃只會讓 run_tests 永久紅。

exit 0 全數對上｜1 有行對不上
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "wiki" / "log.md"
LEDGER = ROOT / "data" / "pending-handoffs.jsonl"
ENFORCE_FROM = "2026-09-25"

# 一行算「有交代」：帶帳本單號，或明寫不登帳的理由
HANDOFF_REF = re.compile(r"H-[0-9a-f]{6}|不登帳[：:]\s*\S")
HANDOFF_ID = re.compile(r"H-[0-9a-f]{6}")
INGEST_HEAD = re.compile(r"^## (\d{4}-\d{2}-\d{2}) Ingest\b")


def ingest_sections(text: str) -> list[tuple[str, list[tuple[int, str]]]]:
    """回傳 [(日期, [(檔案行號, 行文字), ...]), ...]，只收 `## D Ingest` 區段。"""
    out: list[tuple[str, list[tuple[int, str]]]] = []
    cur: list[tuple[int, str]] | None = None
    for no, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            m = INGEST_HEAD.match(line)
            if m:
                cur = []
                out.append((m.group(1), cur))
            else:
                cur = None
            continue
        if cur is not None:
            cur.append((no, line))
    return out


def ledger_ids(path: Path = LEDGER) -> set[str]:
    ids: set[str] = set()
    if not path.exists():
        return ids
    for raw in path.read_text(encoding="utf-8").splitlines():
        try:
            hid = json.loads(raw).get("id")
        except (json.JSONDecodeError, AttributeError):
            continue
        if hid:
            ids.add(hid)
    return ids


def check(text: str, ids: set[str], date: str | None) -> tuple[list[str], int, list[str]]:
    """回傳 (問題清單, 檢查過的轉知行數, 涵蓋的日期)。"""
    problems: list[str] = []
    checked = 0
    dates: list[str] = []
    for d, lines in ingest_sections(text):
        if date is not None and d != date:
            continue
        if date is None and d < ENFORCE_FROM:
            continue
        dates.append(d)
        for no, line in lines:
            if "轉知" not in line:
                continue
            checked += 1
            snippet = line.strip()[:120]
            if not HANDOFF_REF.search(line):
                problems.append(f"  ❌ wiki/log.md:{no}（{d}）含「轉知」卻沒帶帳本單號 H-xxxxxx，"
                                f"也沒寫「不登帳：<理由>」：{snippet}")
                continue
            unknown = [h for h in HANDOFF_ID.findall(line) if h not in ids]
            if unknown:
                problems.append(f"  ❌ wiki/log.md:{no}（{d}）單號不在帳本 data/pending-handoffs.jsonl："
                                f"{'、'.join(unknown)}")
    return problems, checked, dates


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="log 轉知 ↔ 轉知帳本對帳")
    ap.add_argument("--date", help="只查這天的 Ingest 區段（YYYY-MM-DD）；省略則查 ENFORCE_FROM 起全部")
    a = ap.parse_args(argv)

    if not LOG.exists():
        print(f"WARN: {LOG} 不存在，跳過")
        return 0
    problems, checked, dates = check(LOG.read_text(encoding="utf-8"), ledger_ids(), a.date)
    scope = a.date or f"{ENFORCE_FROM} 起"
    if a.date and not dates:
        print(f"check_log_handoffs：wiki/log.md 無 {a.date} Ingest 區段，無可查")
        return 0
    if problems:
        print("\n".join(problems))
        print(f"❌ check_log_handoffs（{scope}）：{len(problems)} 行轉知對不上帳本（共查 {checked} 行）"
              "——先 `python scripts/pending_handoffs.py open …` 登帳，把單號補進本輪該行"
              "（本輪 Ingest 紀錄尚未 commit，仍屬撰寫中；已 commit 的舊區段不改）")
        return 1
    print(f"✅ check_log_handoffs（{scope}）：{checked} 行轉知皆對得到帳本單號或註明不登帳")
    return 0


if __name__ == "__main__":
    sys.exit(main())
