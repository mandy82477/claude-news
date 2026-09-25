"""記者間「轉知」帳本 —— 讓跨記者交辦有接手驗收，而不是主編口頭轉達後消失。

背景：記者回報的「同步自查」常出現「⚠️ 需主編轉知功能記者評估產品化矩陣」這類跨記者
交辦。過去主編讀到後靠下一次派工時記得口頭帶上，沒有任何機制保證目標記者真的接手
（`docs/workaround-register.md` 登記為「轉知標記無接手驗收機制」）。本腳本照
`scan_pending_verifications.py` 的同構做法：**主編寫帳本 → 派工時附清單 → 記者回報處置
→ 主編結案**，四步都留痕。

帳本：`data/pending-handoffs.jsonl`（append only，最後一筆勝出）
  開立：{"id","opened","from","to","page","note","status":"open"}
  結案：{"id","closed","status":"done","by":"<類別>","result":"<一句話>"}
  作廢：{"id","closed","status":"void","result":"<為何不需處理>"}

用法：
  python scripts/pending_handoffs.py open  --from 社群 --to 功能 --page topics/official-community-gap --note "評估產品化矩陣新增列：<模式名>"
  python scripts/pending_handoffs.py list                       # 依目標類別分組印出未結案清單（派工附件）
  python scripts/pending_handoffs.py list --to 功能             # 只印該類別（無則印「無」）
  python scripts/pending_handoffs.py close H-a1b2c3 --by 功能 --result "已補矩陣列"
  python scripts/pending_handoffs.py void  H-a1b2c3 --result "議題已失效"
  python scripts/pending_handoffs.py open  ... --dry-run          # 只驗負責人、印單號，不寫帳本

open 會驗 --to 是不是 --page 的負責記者：依 `wiki/index.md` 該頁列的「領域」欄推類別；
頁面不在 index 目錄列（子頁、封存頁）就沿 frontmatter `parent` 往上找。對不上 exit 1 並印出
正確負責人——轉給不負責那頁的記者，他收到也不會動。確有例外用 `--force --reason "…"`，
理由寫進帳本。

設計原則：
1. 只 append 不改寫既有行——結案是新一行，歷史可稽。
2. id 由 (opened, from, to, note) 決定性雜湊而來，同一交辦重複開立不會產生兩筆。
3. 逾 14 天未結案的在 list 中標 ⚠️，讓主編看得到積壓。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEDGER = REPO_ROOT / "data" / "pending-handoffs.jsonl"
CATEGORIES = ("模型", "功能", "商業", "安全政策", "社群", "人物", "投資分析", "開發實務")  # 後兩者為衍生記者（.claude/skills/wiki-ingest/references/classification.md 第四步），2026-09-06 加
STALE_DAYS = 14
INDEX = REPO_ROOT / "wiki" / "index.md"
WIKI_DIR = REPO_ROOT / "wiki"
# index「領域」欄文字 → 記者類別（比對時忽略表情符號）
DOMAIN_TO_CATEGORY = {"模型": "模型", "工具/功能": "功能", "商業": "商業",
                      "政策/安全": "安全政策", "社群": "社群", "人物": "人物"}
# 領域欄推不出真正負責人的頁：market-signals 領域是商業、由投資分析記者維護
# （.claude/reporter-rules/commercial/daily.md）；feature-radar 不在目錄表，歸功能記者
OWNER_OVERRIDES = {"topics/market-signals": "投資分析", "feature-radar": "功能"}
_WIKILINK = re.compile(r"\[\[([^\]|#]+)")
_PARENT = re.compile(r'^parent:[ \t]*"?([^"\r\n]*?)"?[ \t]*$', re.MULTILINE)


def _make_id(opened: str, src: str, dst: str, note: str) -> str:
    h = hashlib.sha1(f"{opened}|{src}|{dst}|{note}".encode("utf-8")).hexdigest()[:6]
    return f"H-{h}"


def load(path: Path = LEDGER) -> dict[str, dict]:
    """回傳 id → 合併後狀態（開立欄位 + 最後一筆結案欄位）。"""
    state: dict[str, dict] = {}
    if not path.exists():
        return state
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError:
            continue
        hid = row.get("id")
        if not hid:
            continue
        cur = state.setdefault(hid, {})
        cur.update(row)
    return state


def _append(row: dict, path: Path = LEDGER) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def normalize_page(page: str) -> str:
    """`[[topics/x]]`、`wiki/topics/x.md`、`topics/x#節` 都正規化成 `topics/x`。"""
    p = page.strip().strip("[]").split("|")[0].split("#")[0].strip()
    if p.startswith("wiki/"):
        p = p[len("wiki/"):]
    if p.endswith(".md"):
        p = p[:-3]
    return p


def index_owners(index_path: Path = INDEX) -> dict[str, str]:
    """讀 wiki/index.md 所有含「領域」表頭的表格，回傳 頁面 → 記者類別。"""
    owners: dict[str, str] = {}
    if not index_path.exists():
        return owners
    col: int | None = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if "領域" in cells:
            col = cells.index("領域")
            continue
        if col is None or col >= len(cells):
            continue
        m = _WIKILINK.match(cells[0])
        if not m:
            continue
        for key, cat in DOMAIN_TO_CATEGORY.items():
            if key in cells[col]:
                owners[normalize_page(m.group(1))] = cat
                break
    return owners


def _parent_of(page: str, wiki_dir: Path) -> str | None:
    f = wiki_dir / f"{page}.md"
    if not f.exists():
        return None
    text = f.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    m = _PARENT.search(text[: end if end != -1 else 2000])
    if not m or m.group(1).strip() in ("", "null", "~"):
        return None
    return normalize_page(m.group(1))


def owner_of(page: str, index_path: Path = INDEX, wiki_dir: Path = WIKI_DIR) -> tuple[str | None, list[str]]:
    """回傳 (負責記者類別或 None, 推導路徑)。先查覆寫表與 index，查不到沿 parent 往上。"""
    owners = index_owners(index_path)
    cur: str | None = normalize_page(page)
    trail: list[str] = []
    while cur and cur not in trail and len(trail) < 6:
        trail.append(cur)
        if cur in OWNER_OVERRIDES:
            return OWNER_OVERRIDES[cur], trail
        if cur in owners:
            return owners[cur], trail
        cur = _parent_of(cur, wiki_dir)
    return None, trail


def open_handoff(src: str, dst: str, page: str, note: str, opened: str | None = None,
                 path: Path = LEDGER, extra: dict | None = None) -> str:
    if src not in CATEGORIES or dst not in CATEGORIES:
        raise SystemExit(f"from/to 必須是下列類別之一：{', '.join(CATEGORIES)}")
    if src == dst:
        raise SystemExit("from 與 to 相同——同記者的待辦不是轉知，寫進頁面或 log 即可")
    opened = opened or date.today().isoformat()
    hid = _make_id(opened, src, dst, note)
    if hid in load(path):
        return hid  # 冪等：同日同交辦重複開立不重複記
    row = {"id": hid, "opened": opened, "from": src, "to": dst, "page": page,
           "note": note, "status": "open"}
    row.update(extra or {})
    _append(row, path)
    return hid


def close_handoff(hid: str, by: str, result: str, status: str = "done",
                  closed: str | None = None, path: Path = LEDGER) -> None:
    state = load(path)
    if hid not in state:
        raise SystemExit(f"找不到 {hid}")
    if state[hid].get("status") != "open":
        raise SystemExit(f"{hid} 已是 {state[hid].get('status')}，不可重複結案")
    _append({"id": hid, "closed": closed or date.today().isoformat(), "status": status,
             "by": by, "result": result}, path)


def open_items(path: Path = LEDGER, to: str | None = None) -> list[dict]:
    rows = [r for r in load(path).values() if r.get("status") == "open"]
    if to:
        rows = [r for r in rows if r.get("to") == to]
    return sorted(rows, key=lambda r: (r.get("to", ""), r.get("opened", "")))


def render(rows: list[dict], today: date | None = None) -> str:
    """派工附件：依目標類別分組；無則印「無」。"""
    today = today or date.today()
    if not rows:
        return "無"
    out: list[str] = []
    by_to: dict[str, list[dict]] = {}
    for r in rows:
        by_to.setdefault(r.get("to", "?"), []).append(r)
    for dst in CATEGORIES:
        group = by_to.get(dst)
        if not group:
            continue
        out.append(f"### 轉知待接手 → {dst} 記者（{len(group)} 筆）")
        for r in group:
            try:
                age = (today - datetime.strptime(r["opened"], "%Y-%m-%d").date()).days
            except Exception:
                age = 0
            flag = " ⚠️ 逾 14 天" if age > STALE_DAYS else ""
            out.append(
                f"- {r['id']}（{r.get('opened','?')} 由 {r.get('from','?')} 記者轉知{flag}）"
                f"｜頁面 `{r.get('page','—')}`｜{r.get('note','')}"
            )
        out.append("")
    return "\n".join(out).rstrip()


def main(argv: list[str] | None = None) -> int:
    # cp950 主控台會讓表情符號與全形字元炸掉 UnicodeEncodeError（2026-09-05 實例）
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_open = sub.add_parser("open"); p_open.add_argument("--from", dest="src", required=True)
    p_open.add_argument("--to", required=True); p_open.add_argument("--page", default="—")
    p_open.add_argument("--note", required=True); p_open.add_argument("--date")
    p_open.add_argument("--force", action="store_true", help="--to 與頁面負責人不符仍開立（須附 --reason）")
    p_open.add_argument("--reason", help="--force 的理由，寫進帳本")
    p_open.add_argument("--dry-run", action="store_true", help="只驗負責人並印單號，不寫帳本")
    p_list = sub.add_parser("list"); p_list.add_argument("--to")
    p_close = sub.add_parser("close"); p_close.add_argument("id"); p_close.add_argument("--by", required=True)
    p_close.add_argument("--result", required=True)
    p_void = sub.add_parser("void"); p_void.add_argument("id"); p_void.add_argument("--result", required=True)
    a = ap.parse_args(argv)

    if a.cmd == "open":
        extra = None
        if a.force:
            if not (a.reason or "").strip():
                print("❌ --force 必須附 --reason「為何轉給非負責記者」", file=sys.stderr)
                return 1
            extra = {"force_reason": a.reason.strip()}
        else:
            owner, trail = owner_of(a.page)
            via = " → ".join(trail)
            if owner is None:
                print(f"❌ 查不到 `{a.page}` 的負責記者（推導路徑：{via or '—'}；wiki/index.md 無此列、"
                      "frontmatter 無 parent）。請改填正確頁面，或 --force --reason 說明", file=sys.stderr)
                return 1
            if owner != a.to:
                print(f"❌ `{a.page}` 的負責記者是「{owner}」，不是「{a.to}」（推導路徑：{via}）。"
                      f"改用 --to {owner}；確有例外用 --force --reason", file=sys.stderr)
                return 1
        if a.dry_run:
            src_ok = a.src in CATEGORIES and a.to in CATEGORIES and a.src != a.to
            if not src_ok:
                print("❌ from/to 不合法或相同", file=sys.stderr)
                return 1
            print(f"（dry-run，未寫帳本）{_make_id(a.date or date.today().isoformat(), a.src, a.to, a.note)}")
            return 0
        print(open_handoff(a.src, a.to, a.page, a.note, a.date, extra=extra))
    elif a.cmd == "list":
        print(render(open_items(to=a.to)))
    elif a.cmd == "close":
        close_handoff(a.id, a.by, a.result); print(f"closed {a.id}")
    elif a.cmd == "void":
        close_handoff(a.id, "主編", a.result, status="void"); print(f"void {a.id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
