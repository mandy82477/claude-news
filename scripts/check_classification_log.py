#!/usr/bin/env python3
"""check_classification_log.py — 主編分類帳本對帳：當日每一則原料都要有著落。

帳本 data/classification-log.jsonl 一行一則，記主編把它分到哪些類別；
categories 為空代表主編判斷不派給任何記者，此時 reason 必填。
帳本 append only：同一 URL 同日多行時**最後一行勝出**，驗證只對勝出的那行做——
先寫錯再 append 一行更正即可通過，不必回頭改舊行。

對帳的等式：gathered_archive/<date>.json 的每個 URL ∈ 帳本當日 URL 集合。
只記「被排除的」對不了帳——「忘了處理」和「判斷排除」在帳上長得一樣
（2026-09-15 使用者稽核：70 則有 13 則從未進任何派工訊息，事後才靠人工比對抓出）。

阻斷（exit 1）只給**會讓漏處理躲過對帳**的問題：原料未進帳本、排除無理由、排除摘要
不可讀、未知類別；排除摘要是剝殼後仍空的純殼層摘要、或排除理由屬記者收錄判斷（重複／
已報導）而非分類判斷，這兩條新規則只對 `ENFORCE_FROM`（見下方常數）起的日期阻斷——
帳本 append only、舊行改不了，生效日前的舊行降為 ⚠️ 警示，`--enforce-all` 可強制全開
做追溯稽核。其餘（帳本 URL 打錯、壞 JSON 行、結構壞行）只印 ⚠️ 不阻斷——它們掩護不了
任何一則原料（被掩護的那則仍會以「未進帳本」阻斷），留著只會製造「append 更正也修不掉」
的死鎖。

exit 0 全數對上｜1 有阻斷級問題｜2 原料已逾 14 天保留窗（逾期 backfill，依 SKILL.md
步驟 2 例外跳過對帳）｜3 原料在窗內卻缺檔或損毀（抓料缺件，先修抓料，不得跳過）。

用法：
    python scripts/check_classification_log.py --date 2026-09-14
    python scripts/check_classification_log.py --date 2026-09-14 --json
    python scripts/check_classification_log.py --date 2026-09-14 --enforce-all
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date as _date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "data" / "classification-log.jsonl"
ARCHIVE = ROOT / "src" / "gathered_archive"
RETENTION_DAYS = 14  # 與 scripts/archive_gathered.py 的保留窗一致

CATEGORIES = {"模型", "功能", "商業", "安全政策", "社群", "人物"}
_DATE_IN_RAW = re.compile(r'"date"\s*:\s*"(\d{4}-\d{2}-\d{2})"')
# 只認原料摘要實際會殘留的標籤形態（HN／Reddit／Google News RSS 的 HTML），不認任意
# 標籤名：摘要正當談到 <canvas>、<div> 是本站題材常態，不能被當成殘留擋掉
_HTML_RESIDUE = re.compile(
    r"<(?:a\s+href|img\s|div\s+class|span\s+class|p>|br\s*/?>|table>|tr>|td>|h[1-6]>|blockquote\s+cite|ul>|li>)",
    re.IGNORECASE,
)
MIN_SUMMARY = 20
HTML_HINT = "（若原文本就在談 HTML 標籤，把尖括號改寫成文字敘述即可）"
# 帳本 append only、舊行不可改：殼層排除與重複理由兩條規則若對生效日前的舊行也阻斷，
# 會把 2026-09-22／09-24 事故當時就已寫死的舊排除行永遠卡紅，逼人去改不可改的舊行。
# 兩條新規則只對 >= 生效日的行阻斷，舊行降級為警示；`--enforce-all` 供追溯稽核強制全開。
ENFORCE_FROM = "2026-09-25"  # 與 scripts/check_log_handoffs.py 的生效日常數同名同語意
# HN 討論串被 dead/flagged 後，抓料只留得下這幾種殼標記，摘要正文全被吃掉——
# 2026-09-24 兩則（Tokenhush、per-step reasoning effort）就是這樣過了 MIN_SUMMARY 字數關，
# 被主編當「無可讀摘要」排除，wiki 全庫零命中。判長度前先剝殼，剝完仍短才算數。
# 💬 是留言貼文一律會有的前綴符號（與標籤無關），拆成獨立於標籤集合之外，
# 這樣「只認某幾種標籤」的測試改動不會被 💬 蓋住——標籤集合變動要能被測試看見。
_SHELL_BULLET = "💬"
_SHELL_TAGS = ("flagged", "dead", "deleted")


def _shell_marker_re() -> re.Pattern[str]:
    tags = "|".join(re.escape(t) for t in _SHELL_TAGS)
    return re.compile(rf"{_SHELL_BULLET}|\[(?:{tags})\]")


# 重複與否是記者的收錄判斷（同一事件昨天報過要不要再收），不是主編的分類判斷——
# 分類表沒有「重複」這一格。`(?<!不)重複` 排除「不重複開列」這種同日單一事故合併敘述
# （2026-09-22 實測：合併敘述會被無腦子串比對誤傷，只有跨日「已報過/昨日」才算違規）。
_DUPLICATE_REASON = re.compile(r"(?<!不)重複|已報導|已報過|昨日|前日|前一日")


def _strip_shell_markers(summary: str) -> str:
    return _shell_marker_re().sub("", summary).strip()


def _is_pure_shell(summary: str) -> bool:
    """整段摘要剝完認得的標記後空無一物，才算「純殼」——只是含有標記但仍有其他
    文字的摘要不算，那種情況該走一般的太短判斷，不冒用殼層訊息。"""
    return summary.strip() != "" and _strip_shell_markers(summary) == ""


def load_log(path: Path) -> list[dict]:
    """壞行保留原文裡的日期，讓只在該日發警示（不讓三個月前的壞行擋今天）。"""
    rows: list[dict] = []
    if not path.exists():
        return rows
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            m = _DATE_IN_RAW.search(line)
            rows.append({"_bad_line": n, "_bad_date": m.group(1) if m else None})
    return rows


def _last_valid_rows(log_rows: list[dict], date: str) -> tuple[dict[str, dict], list[str]]:
    """當日行 → 依 URL 取最後一行。結構壞掉的行不參與勝出，回傳為警示（不阻斷）。

    reconcile 與 summarize 共用同一個篩選，CLI 印的數字才不會與 exit code 說兩套話。
    """
    warnings: list[str] = []
    last: dict[str, dict] = {}
    for r in log_rows:
        if "_bad_line" in r:
            if r.get("_bad_date") in (None, date):
                warnings.append(f"帳本第 {r['_bad_line']} 行不是合法 JSON，已略過")
            continue
        if r.get("date") != date:
            continue
        url = r.get("url")
        if not isinstance(url, str) or not url.startswith("http"):
            warnings.append(f"帳本行 URL 不是 http 開頭，已略過：{str(r.get('title', '?'))[:60]}")
            continue
        if not isinstance(r.get("categories"), list):
            warnings.append(f"帳本行 categories 不是陣列，已略過：{str(r.get('title', '?'))[:60]}")
            continue
        last[url] = r
    return last, warnings


def audit(
    gathered_items: list[dict], log_rows: list[dict], date: str, enforce_all: bool = False,
) -> tuple[list[str], list[str]]:
    """回傳 (阻斷級問題, 警示)。純函式，供測試與 CLI 共用。

    `enforce_all`：殼層排除與重複理由兩條規則預設只對 `date >= ENFORCE_FROM` 阻斷，
    生效日前的行降為警示（帳本 append only，舊行改不了，阻斷等於死鎖）；
    設為 True 時對任何日期都阻斷，供追溯稽核／回放驗證用。
    """
    last, warnings = _last_valid_rows(log_rows, date)
    problems: list[str] = []
    effective_enforce = enforce_all or date >= ENFORCE_FROM

    for r in last.values():
        cats = r["categories"]
        title = str(r.get("title", "?"))[:60]
        bad = [c for c in cats if c not in CATEGORIES]
        if bad:
            problems.append(f"未知類別 {bad}：{title}")
        if not cats:
            if not (r.get("reason") or "").strip():
                problems.append(f"排除但沒寫理由：{title}")
            reason = r.get("reason") or ""
            if _DUPLICATE_REASON.search(reason):
                msg = f"重複與否屬記者收錄判斷，不是分類理由：{title}"
                (problems if effective_enforce else warnings).append(msg)
            summary = str(r.get("summary") or "")
            if _HTML_RESIDUE.search(summary):
                problems.append(f"排除條目的 summary 殘留 HTML，複核記者讀不到內文{HTML_HINT}：{title}")
            elif _is_pure_shell(summary):
                msg = f"殼層摘要不得當排除依據，請以標題與 URL 判類派出：{title}"
                (problems if effective_enforce else warnings).append(msg)
            elif len(summary.strip()) < MIN_SUMMARY:
                problems.append(f"排除條目的 summary 太短（<{MIN_SUMMARY} 字），複核記者無從判斷：{title}")

    gathered_urls: list[str] = []
    for i, it in enumerate(gathered_items, 1):
        u = it.get("url")
        if not isinstance(u, str) or not u.strip():
            problems.append(f"原料第 {i} 則缺 URL，無法對帳：{str(it.get('title', ''))[:60]}")
            continue
        gathered_urls.append(u)

    for u in gathered_urls:
        if u not in last:
            title = next((it.get("title", "") for it in gathered_items if it.get("url") == u), "")
            problems.append(f"原料未進帳本（主編漏處理）：{str(title)[:60]}｜{u}")

    gathered_set = set(gathered_urls)
    for u in last:
        if u not in gathered_set:
            warnings.append(f"帳本有但原料沒有（URL 打錯？append 正確的那行即可，這行不阻斷）：{u}")
    return problems, warnings


def reconcile(gathered_items: list[dict], log_rows: list[dict], date: str, enforce_all: bool = False) -> list[str]:
    """只回阻斷級問題（空＝可派工）。"""
    return audit(gathered_items, log_rows, date, enforce_all)[0]


def summarize(gathered_items: list[dict], log_rows: list[dict], date: str) -> dict:
    last, _ = _last_valid_rows(log_rows, date)
    rows = list(last.values())
    by_cat: dict[str, int] = {c: 0 for c in sorted(CATEGORIES)}
    for r in rows:
        for c in r.get("categories") or []:
            if c in by_cat:
                by_cat[c] += 1
    return {
        "date": date,
        "gathered": len(gathered_items),
        "logged": len(rows),
        "excluded": sum(1 for r in rows if not r.get("categories")),
        "by_category": by_cat,
    }


def beyond_retention(date: str, today: _date | None = None) -> bool:
    """目標日是否已超出原料保留窗——只有這種情況允許跳過對帳。"""
    y, m, d = (int(x) for x in date.split("-"))
    return (today or _date.today()) - _date(y, m, d) > timedelta(days=RETENTION_DAYS)


def _use_utf8_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--log", type=Path, default=LOG)
    ap.add_argument("--archive-dir", type=Path, default=ARCHIVE)
    ap.add_argument("--today", default=None, help="測試用：覆寫今天的日期")
    ap.add_argument("--enforce-all", action="store_true",
                     help=f"殼層排除／重複理由兩條規則預設只對 >= {ENFORCE_FROM} 阻斷，"
                          "此旗標對任何日期都阻斷（追溯稽核用，帳本舊行仍改不了）")
    args = ap.parse_args(argv)

    try:
        _date.fromisoformat(args.date)
        today = _date.fromisoformat(args.today) if args.today else None
    except ValueError:
        print(f"--date 不是有效日期（要 YYYY-MM-DD 且真實存在）：{args.date}")
        print("這是指令參數錯，不是帳本問題——修 TARGET_DATE 再跑，不要去翻帳本。")
        return 3

    archive = args.archive_dir / f"{args.date}.json"
    gathered = None
    if archive.exists():
        try:
            gathered = json.loads(archive.read_text(encoding="utf-8")).get("items") or []
        except ValueError as e:
            print(f"原料不是合法 JSON：{archive}（{e}）")
    if gathered is None:
        if beyond_retention(args.date, today):
            print(f"原料已逾 {RETENTION_DAYS} 天保留窗：{archive}")
            print("逾期 backfill 依 .claude/skills/wiki-ingest/SKILL.md 步驟 2 例外：跳過對帳，"
                  "帳本每行 reason 註明「原料已逾保留窗，未對帳」。")
            return 2
        print(f"原料在保留窗內卻缺檔或損毀：{archive}")
        print("這是抓料缺件（daily-gather 失敗或被 GitHub 丟棄），不是逾窗——先修抓料再 ingest，不得跳過對帳。")
        return 3

    log_rows = load_log(args.log)
    problems, warnings = audit(gathered, log_rows, args.date, args.enforce_all)
    stats = summarize(gathered, log_rows, args.date)

    if args.json:
        print(json.dumps({"ok": not problems, "stats": stats, "problems": problems,
                          "warnings": warnings}, ensure_ascii=False, indent=2))
    else:
        print(f"# 分類帳本對帳 {args.date}")
        print(f"原料 {stats['gathered']} 則｜帳本 {stats['logged']} 則｜排除 {stats['excluded']} 則")
        print("各類別派工數：" + "、".join(f"{k} {v}" for k, v in stats["by_category"].items()))
        for w in warnings:
            print(f"  ⚠️ {w}")
        if problems:
            print(f"\n❌ {len(problems)} 個阻斷級問題：")
            for p in problems:
                print(f"  - {p}")
        else:
            print("\n✅ 全數對上：每則原料都有分類或排除理由")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
