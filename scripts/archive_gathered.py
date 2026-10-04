#!/usr/bin/env python3
"""archive_gathered.py — 把 src/gathered_items.json 存一份按日期分檔的副本。

為什麼需要：`gathered_items.json` 沒有按日分檔，每次抓料都直接覆寫它。若某天的
日報沒產出（雲端 routine 失敗、中止、push 失敗），那天「已經抓到手」的原料會在
隔天抓料時被蓋掉；之後想補跑只能回頭重抓，但來源多是近期視窗的 RSS/API，幾天前
的內容早已滾出視窗——那天的新聞就永久漏失。

有了副本，補跑可以直接 replay 當天的真實原料，產出與原本該有的日報一致
（見 `.claude/skills/news-gather/SKILL.md` 的「補跑（backfill）注意事項」）。

檔名取 `gathered_items.json` 內的 `date` 欄位，不取系統當下日期——這樣 backfill
產生的原料也會歸檔到它真正對應的那一天。

保留天數與 emitted-cache 的 TTL 一致（14 天）。

副本含「全部抓到的條目」而不只是通過管線的那批（2026-10-04 起）：
- `items`        通過 dedup／relevance filter／emitted-cache 的條目，也就是送進主編分類的
                 那批（與舊格式完全相同，既有讀者照舊只讀它）；每筆補 `emitted: true`、
                 `blocked_by: null`。
- `blocked_items` 抓到卻被擋下的條目（舊檔沒有這個 key），每筆帶 `emitted: false`、
                 `blocked_by`（層名，見 news_aggregator.main.BLOCKED_LAYERS）、
                 `blocked_detail`（留下那筆的 URL／首次刊出日）。
- `archive_schema: 2` 標記此檔有記錄被擋條目；缺這個 key 的舊檔無從得知被擋了什麼，
  與「沒有條目被擋」要分開看。
此處的 emitted 指「通過抓料管線」，不是「被日報選入」——後者是主編／記者的編輯判斷。

用法：
    python scripts/archive_gathered.py            # 歸檔 + 清理過期
    python scripts/archive_gathered.py --prune-only
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GATHERED = REPO_ROOT / "src" / "gathered_items.json"
ARCHIVE_DIR = REPO_ROOT / "src" / "gathered_archive"
NEWS_DIR = REPO_ROOT / "news"
RETENTION_DAYS = 14


ARCHIVE_SCHEMA = 2


def annotate(data: dict) -> dict:
    """為副本補上「是否通過管線」與「被擋理由」欄位（只加欄位，不刪不改既有欄位）。
    items 內若不是 dict（舊測試夾具）就原樣保留。"""
    for it in data.get("items") or []:
        if isinstance(it, dict):
            it.setdefault("emitted", True)
            it.setdefault("blocked_by", None)
    if "blocked_items" in data:
        for it in data.get("blocked_items") or []:
            if isinstance(it, dict):
                it["emitted"] = False
                it.setdefault("blocked_by", None)  # 管線沒記到理由時為 null
                it.setdefault("blocked_detail", "")
        data["archive_schema"] = ARCHIVE_SCHEMA
        data["gathered_total"] = len(data.get("items") or []) + len(data.get("blocked_items") or [])
    return data


def prune(archive_dir: Path = ARCHIVE_DIR, today: date | None = None) -> list[str]:
    """刪除超過保留天數的副本，回傳被刪檔名。以檔名日期判斷，不看 mtime
    （git checkout 會把 mtime 全部重設為 checkout 當下，mtime 在 CI 不可信）。"""
    today = today or date.today()
    cutoff = today - timedelta(days=RETENTION_DAYS)
    removed = []
    if not archive_dir.exists():
        return removed
    for f in sorted(archive_dir.glob("*.json")):
        try:
            stamp = date.fromisoformat(f.stem)
        except ValueError:
            continue  # 檔名不是日期就別亂刪
        if stamp < cutoff:
            f.unlink()
            removed.append(f.name)
    return removed


def archive(gathered: Path = GATHERED, archive_dir: Path = ARCHIVE_DIR,
            news_dir: Path = NEWS_DIR) -> Path | None:
    if not gathered.exists():
        print(f"跳過歸檔：{gathered} 不存在")
        return None
    try:
        data = json.loads(gathered.read_text(encoding="utf-8"))
        stamp = data["date"]
        date.fromisoformat(stamp)  # 驗證格式
    except Exception as e:
        print(f"跳過歸檔：無法從 {gathered.name} 讀出合法的 date 欄位（{e}）")
        return None
    archive_dir.mkdir(parents=True, exist_ok=True)
    target = archive_dir / f"{stamp}.json"
    # 當天日報已產出、副本也已存在時，不覆寫：副本是「那天日報與分類帳的原料」，
    # 之後同日再抓（本機提早跑完後 GitHub Actions 10:23 UTC 再跑、或 watchdog 重跑）
    # 拿到的是不同視窗、已去掉 emitted-cache 的另一批條目，覆寫會讓
    # data/classification-log.jsonl 對該日永遠對不上帳（check_classification_log 紅）。
    # 這批較晚的條目沒進 emitted-cache，會在次日的抓料視窗再被看見，不會遺失。
    if target.exists() and (news_dir / f"{stamp}.md").exists():
        print(f"跳過歸檔：{target.relative_to(target.parent.parent)} 已存在且 news/{stamp}.md 已產出，"
              "不以同日較晚的抓料覆寫日報原料")
        return None
    target.write_text(json.dumps(annotate(data), ensure_ascii=False, indent=2), encoding="utf-8")
    return target


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prune-only", action="store_true")
    args = p.parse_args()

    if not args.prune_only:
        target = archive()
        if target:
            print(f"已歸檔：{target.relative_to(REPO_ROOT)}")
    removed = prune()
    if removed:
        print(f"已清理過期副本（保留 {RETENTION_DAYS} 天）：{', '.join(removed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
