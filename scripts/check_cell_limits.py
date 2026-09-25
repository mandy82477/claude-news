#!/usr/bin/env python3
"""表格儲存格 / 細節區條列字元上限機械閘 — 「表格放結論，細節下沉」的執行點。

立法依據：`.claude/reporter-rules/page-templates.md`「表格放結論，細節下沉（全站
通用）」與 `.claude/reporter-rules/shared.md`「書寫風格」——查證過程、
演進脈絡、多來源歧異塞進表格儲存格會讓表格失去可掃描性並在網站爆版；下沉
到表格正下方的細節區後，細節區條列本身仍受 200 字元上限拘束，不是換成無
上限的傾倒區。2026-08-27 起這兩條規則只有規則檔明文，沒有偵測器（本庫病史
的標準形狀：承諾有了、執行點沒有）。本檔是那兩條規則的執行點，模型記者
2026-09-05 model-comparison 健檢定稿 §7.2 指定新增。

用法：
    python scripts/check_cell_limits.py                 # 全庫檢查
    python scripts/check_cell_limits.py --page X         # 只看某頁（slug 片段）
    python scripts/check_cell_limits.py --rebuild        # 收緊基線：只移除／縮短條目
    python scripts/check_cell_limits.py --rebuild --allow-grow --reason "…"
                                                         # 例外：基線要加條目（寫帳本）
    python scripts/check_cell_limits.py --migrate-legacy # 一次性：舊指紋格式 → 錨點格式

量測規則：
    - 表格列（以 `|` 開頭的行）：逐格量測，**> 120 字元**算超限
    - 非表格的條列（`- ` / `* ` 開頭，含巢狀縮排）：整行（去除項目符號後）
      **> 200 字元**算超限
    - 量測前先剝掉 markdown 連結的 URL（`[文字](url)` -> `[文字]`），只量渲染
      可見文字
    - 排除純引用來源格（標題＋URL＋日期，去 URL 後仍是短句）——本檔以「剝除
      URL 後仍超限」為準，天然涵蓋此豁免：純引用格的可見文字通常很短
    - 排除 `*-archive.md`（蒐集契約明定 archive 原文一字不刪，不受本閘拘束）
    - frontmatter / code fence / `%% … %%` 註解 / HTML 註解不算（沿用
      check_reader_language.py 的 body_lines() 剝除邏輯）

存量基線：首跑必然命中大量存量，全部 FAIL 只會讓人把檢查關掉。故
`data/cell-limit-baseline.json` 記下每筆存量超限的（頁、類型、錨點、長度上限），
本檔只對**基線外的新增**報 FAIL，基線內的印為 WARN 摘要。

存量判定＝「穩定錨點＋長度不增」：
    同頁、同類型、同錨點，且現長度 ≤ 基線 max_len → 存量（放行）
    錨點不在基線，或長度超過 max_len → 新增（FAIL）
    改寫存量列的內文（例如留言數 40→47）不改錨點、不變長，就仍是存量，不需動基線。

錨點規則（anchor；先「清洗」：剝 wikilink 取顯示文字、剝 markdown 連結取文字、
去 `**`／`__`／反引號、空白壓成單一空格）：
    表格儲存格：該列**第一格**清洗後的文字，取前 24 字，接 `#c<欄序>`（欄序從 1 起算，
        分辨同列多格超限）。例：
          `| **v2.1.152** | 2026-05-20 | 很長的說明… |`         → `v2.1.152#c3`
          `| [Foo 工具](https://x) | 很長的說明… |`             → `Foo 工具#c2`
    細節區條列：清洗後先剝開頭的狀態前綴（`<符號> <≤12 字狀態>（可選括註）｜`，如
        `🔴 **未修復**｜`、`🔎 **查無官方**（標…｜查…｜複…）｜`——狀態會翻、複查日會改，
        不能當身分），再取前 24 字；若這 24 字內有全形冒號「：」且冒號前已 ≥ 10 字，
        在冒號處截斷（標題即身分）。冒號前不足 10 字的是欄位標籤（「核心模式：」
        「功能請求：」），不截，保留冒號後的文字以免全頁同錨。例：
          `- 🔴 **未修復**｜**VSCode 擴充套件 `ide_selection` 缺失…**：…`
                                           → `VSCode 擴充套件 ide_selectio`（前 24 字）
          `- 🔎 **查無官方**（標…｜查…｜複…）｜**功能請求：Linear 整合——指派 issue 給…`
                                           → `功能請求：Linear 整合——指派 issue`
          `- **AWS Continuum（08-05）**：AWS 官方宣布…`  → `AWS Continuum（08-05）`
          `- **核心模式：** 開發者釋出應用程式，讓使用者能從任一則…`
                                           → `核心模式： 開發者釋出應用程式，讓使用者能從任一`
    同頁同錨多筆（例：同日期的多列）：基線以多重集合記錄各自的 max_len，比對時長的
    配長的；筆數或任一長度超出即判新增。
    錨點失效的已知形狀（標題本身前 24 字內含會變的數字；表格首格是會改的數字）
    列在 docs/rules-changelog/reporter-shared.md 2026-09-25 段。

基線只准變緊：
    `--rebuild` 預設只移除消失的條目、把縮短的條目 max_len 收緊；遇到基線外的
    新增超限一律拒絕（exit 1，基線檔不動）。要新增條目必須
    `--allow-grow --reason "…"`，並自動 append 一行到 `data/baseline-changes.jsonl`
    （date、file、added、removed、reason、actor）。
    `src/tests/test_baseline_ratchet.py` 以 HEAD 版基線比對：新增錨點沒有在帳本
    登記理由即紅。記者不得使用 `--rebuild`／`--allow-grow`（`.claude/reporter-rules/shared.md`）。

exit 0 = 無新增超限；1 = 有新增超限（或基線檔損毀／舊格式／rebuild 被拒）。
"""
from __future__ import annotations

import argparse
import getpass
import hashlib
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
BASELINE = ROOT / "data" / "cell-limit-baseline.json"
CHANGES = ROOT / "data" / "baseline-changes.jsonl"

TABLE_LIMIT = 120
LIST_LIMIT = 200
ANCHOR_LEN = 24
COLON_MIN = 10
BASELINE_FORMAT = 2

TARGET_GLOBS = ("entities/*.md", "topics/*.md")
TARGET_FILES = ("feature-radar.md", "overview.md", "index.md")

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
INLINE_PCT_RE = re.compile(r"%%.*?%%", re.S)
INLINE_HTML_RE = re.compile(r"<!--.*?-->", re.S)
MD_LINK_RE = re.compile(r"\]\([^)]*\)")
LIST_ITEM_RE = re.compile(r"^(\s*)([-*])\s+(.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")
MD_LINK_FULL_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
STATUS_PREFIX_RE = re.compile(r"^[^\w\s]{0,3}\s*[^｜（\s]{1,12}(?:（[^）]*）)?｜")


class BaselineError(Exception):
    """基線檔損毀或仍是舊格式。"""


def _stdout():
    """Windows 主控台預設 cp950，直接 print 中文與符號會 UnicodeEncodeError。"""
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


def target_files() -> list[Path]:
    files: list[Path] = []
    for g in TARGET_GLOBS:
        files.extend(sorted(WIKI.glob(g)))
    for name in TARGET_FILES:
        f = WIKI / name
        if f.exists():
            files.append(f)
    # archive 頁排除：蒐集契約明定原文一字不刪，不受本閘拘束
    return [f for f in files if not f.stem.endswith("-archive")]


def page_id(f: Path) -> str:
    try:
        return f.relative_to(WIKI).as_posix()[:-3]
    except ValueError:
        return f.stem


def body_lines(text: str) -> list[tuple[int, str]]:
    """回傳 (行號, 可檢查的正文) — frontmatter / code fence / %% 註解 / HTML 註解已剝除。

    邏輯與 check_reader_language.py 的同名函式一致（單一演算法，兩處各自維護
    是可接受的重複——兩支腳本各自獨立、互不 import，複製比抽共用模組簡單）。
    """
    fm = FRONTMATTER_RE.match(text)
    offset = text[: fm.end()].count("\n") if fm else 0
    body = text[fm.end():] if fm else text

    out: list[tuple[int, str]] = []
    in_fence = False
    in_pct = False
    in_html = False
    for i, raw in enumerate(body.splitlines(), 1):
        lineno = i + offset
        line = raw
        if in_pct:
            if "%%" in line:
                in_pct = False
                line = line.split("%%", 1)[1]
            else:
                continue
        if in_html:
            if "-->" in line:
                in_html = False
                line = line.split("-->", 1)[1]
            else:
                continue
        if re.match(r"\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = INLINE_PCT_RE.sub("", line)
        line = INLINE_HTML_RE.sub("", line)
        if "%%" in line:
            in_pct = True
            line = line.split("%%", 1)[0]
        if "<!--" in line:
            in_html = True
            line = line.split("<!--", 1)[0]
        if line.strip():
            out.append((lineno, line))
    return out


def _strip_link_urls(text: str) -> str:
    """剝掉 markdown 連結的 URL，只留可見文字——規則檔明文的量測前置步驟。"""
    return MD_LINK_RE.sub("]", text)


CHILDREN_PROJECTION_RE = re.compile(r"\s*↳ 子故事：.*$")


def _table_cells(line: str) -> list[str]:
    """表格列的儲存格（去頭尾空格），不含開頭/結尾的空字串。

    `↳ 子故事：` 那一段不計入字數：它是 `gen_wiki_frontmatter.py` 每次重生的**機器投影**
    （家在各子頁的「上層」欄），不是撰稿者寫的摘要。本閘管的是讀者讀得動的鉤子長度，
    把機器附加的片段算進人寫的預算，會變成「某頁多了一個 archive 子頁，就要求另一個人
    去砍他的鉤子」——那是叫人修一個他沒寫、也不該由他修的東西。
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    parts = stripped.split("|")
    # split 會在開頭/結尾產生空字串（因為列以 | 開頭與結尾）
    cells = [p.strip() for p in parts[1:-1]] if len(parts) > 2 else []
    return [CHILDREN_PROJECTION_RE.sub("", c).strip() for c in cells]


def fingerprint(kind: str, content: str) -> str:
    """舊格式（format 1）指紋 = 類型 + 正規化內容雜湊。只供 --migrate-legacy 對應舊基線用。"""
    norm = re.sub(r"\s+", "", content.strip())
    return f"{kind}:{hashlib.sha1(norm.encode('utf-8')).hexdigest()[:12]}"


def _clean(text: str) -> str:
    """錨點清洗：wikilink 取顯示文字、markdown 連結取文字、去強調與反引號、壓空白。"""
    text = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = MD_LINK_FULL_RE.sub(r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def table_anchor(first_cell: str, col: int) -> str:
    """表格儲存格錨點：第一格清洗後前 24 字 + `#c<欄序>`（欄序 1 起算）。"""
    return f"{_clean(first_cell)[:ANCHOR_LEN]}#c{col}"


def list_anchor(content: str) -> str:
    """細節區條列錨點：清洗 → 剝狀態前綴 → 前 24 字，冒號前 ≥10 字則截在冒號。"""
    text = _clean(content)
    text = STATUS_PREFIX_RE.sub("", text, count=1).strip()
    head = text[:ANCHOR_LEN]
    idx = head.find("：")
    if idx >= COLON_MIN:
        head = head[:idx]
    return head.strip()


def scan(files: list[Path] | None = None) -> list[dict]:
    """回傳所有超限命中：{page, line, kind, limit, length, snippet, anchor, fp}。"""
    hits: list[dict] = []
    for f in files if files is not None else target_files():
        pid = page_id(f)
        try:
            text = f.read_text(encoding="utf-8-sig")
        except Exception as exc:  # 解碼失敗不得當成 0 筆命中——否則 --rebuild 會把該頁基線整批當「未使用」移除
            raise SystemExit(f"❌ 無法讀取 {pid}：{exc}（頁面編碼損毀，先修檔再跑；不得視為無超限）")
        for lineno, raw_line in body_lines(text):
            stripped = raw_line.strip()
            if stripped.startswith("|"):
                cells = _table_cells(raw_line)
                for col, cell in enumerate(cells, 1):
                    visible = _strip_link_urls(cell)
                    if len(visible) > TABLE_LIMIT:
                        hits.append({
                            "page": pid, "line": lineno, "kind": "table_cell",
                            "limit": TABLE_LIMIT, "length": len(visible),
                            "snippet": visible[:100],
                            "anchor": table_anchor(cells[0], col),
                            "fp": fingerprint("table_cell", cell),
                        })
                continue
            m = LIST_ITEM_RE.match(raw_line)
            if m:
                content = m.group(3)
                visible = _strip_link_urls(content)
                if len(visible) > LIST_LIMIT:
                    hits.append({
                        "page": pid, "line": lineno, "kind": "list_item",
                        "limit": LIST_LIMIT, "length": len(visible),
                        "snippet": visible[:100],
                        "anchor": list_anchor(content),
                        "fp": fingerprint("list_item", content),
                    })
    return hits


# ── 基線讀寫 ────────────────────────────────────────────────────────────────

def is_legacy_format(data: dict) -> bool:
    pages = data.get("pages", {})
    return any(v and isinstance(v[0], str) for v in pages.values())


def load_baseline(path: Path | None = None) -> dict[str, list[dict]]:
    """{page: [{kind, anchor, max_len}, ...]}。舊格式或損毀 → BaselineError。"""
    path = path or BASELINE
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        raise BaselineError(f"基線檔無法解析：{e}") from e
    if is_legacy_format(data):
        raise BaselineError("基線檔仍是舊指紋格式，需先跑 --migrate-legacy（一次性）")
    pages = data.get("pages", {})
    for p, entries in pages.items():
        for e in entries:
            if not {"kind", "anchor", "max_len"} <= set(e):
                raise BaselineError(f"基線條目缺欄位：{p} {e}")
    return pages


def _entries_from_hits(hits: list[dict]) -> dict[str, list[dict]]:
    pages: dict[str, list[dict]] = {}
    for h in hits:
        pages.setdefault(h["page"], []).append(
            {"kind": h["kind"], "anchor": h["anchor"], "max_len": h["length"]})
    for v in pages.values():
        v.sort(key=lambda e: (e["kind"], e["anchor"], -e["max_len"]))
    return dict(sorted(pages.items()))


def write_baseline(pages: dict[str, list[dict]], path: Path | None = None,
                   extra: dict | None = None) -> None:
    path = path or BASELINE
    payload = {
        "_note": (
            "字元上限機械閘的存量基線（頁 → [{kind, anchor, max_len}]）。check_cell_limits.py "
            "以「同頁同類型同錨點且長度 ≤ max_len」判存量，其餘判新增 FAIL。只准變緊：--rebuild "
            "只能移除或收緊條目；要新增必須 --allow-grow --reason 並寫入 data/baseline-changes.jsonl，"
            "src/tests/test_baseline_ratchet.py 以 HEAD 版比對看守。記者不得 rebuild。"
        ),
        "_format": BASELINE_FORMAT,
        "_baseline_set": "2026-09-05",
        "_pages": len(pages),
        "_hits": sum(len(v) for v in pages.values()),
    }
    if extra:
        payload.update(extra)
    payload["pages"] = dict(sorted(pages.items()))
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _group(items, key):
    out: dict = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out


def match(hits: list[dict], baseline: dict[str, list[dict]]):
    """把命中配到基線槽位（同頁同類型同錨點的多重集合，長配長）。

    回傳 (new, legacy_pairs, unused_slots)：legacy_pairs 為 [(hit, slot)]，
    unused_slots 為 [(page, slot)]（基線有、現況已無或已縮到上限內的條目）。
    貪婪法：命中由長到短，各取剩餘最大槽位；最大槽位都放不下 → 新增。
    """
    new: list[dict] = []
    pairs: list[tuple[dict, dict]] = []
    unused: list[tuple[str, dict]] = []
    hit_groups = _group(hits, lambda h: (h["page"], h["kind"], h["anchor"]))
    slot_groups: dict = {}
    for page, entries in baseline.items():
        for e in entries:
            slot_groups.setdefault((page, e["kind"], e["anchor"]), []).append(e)
    for key in set(hit_groups) | set(slot_groups):
        hs = sorted(hit_groups.get(key, []), key=lambda h: -h["length"])
        ss = sorted(slot_groups.get(key, []), key=lambda e: -e["max_len"])
        for h in hs:
            if ss and h["length"] <= ss[0]["max_len"]:
                pairs.append((h, ss.pop(0)))
            else:
                new.append(h)
        unused.extend((key[0], s) for s in ss)
    new.sort(key=lambda h: (h["page"], h["line"]))
    return new, pairs, unused


def split_hits(hits: list[dict], baseline: dict[str, list[dict]]) -> tuple[list[dict], list[dict]]:
    """(基線外新增, 基線內存量)。"""
    new, pairs, _ = match(hits, baseline)
    return new, [h for h, _ in pairs]


def baseline_growth(old: dict[str, list[dict]], new: dict[str, list[dict]]) -> list[dict]:
    """新基線相對舊基線「變鬆」的條目：錨點新增、同錨筆數增加、或 max_len 變大。

    把新基線條目當成命中、拿去配舊基線——配不上的就是增長。棘輪測試與 --rebuild 共用。
    """
    as_hits = [
        {"page": p, "kind": e["kind"], "anchor": e["anchor"], "length": e["max_len"], "line": 0}
        for p, entries in new.items() for e in entries
    ]
    grown, _, _ = match(as_hits, old)
    return [{"page": h["page"], "kind": h["kind"], "anchor": h["anchor"], "max_len": h["length"]}
            for h in grown]


# ── 一次性遷移 ──────────────────────────────────────────────────────────────

def migrate_legacy(legacy: dict, hits: list[dict]) -> tuple[dict[str, list[dict]], list[dict], list[tuple[str, str]]]:
    """舊指紋基線 → 錨點基線。

    只收「現況命中且指紋在舊基線」的條目（max_len = 現長度），不借遷移放進任何新命中。
    回傳 (新基線 pages, 現況命中但不在舊基線的 hits, 舊基線有但現況找不到的 (page, fp))。
    """
    old_pages = legacy.get("pages", {})
    kept, outside = [], []
    seen: set[tuple[str, str]] = set()
    for h in hits:
        if h["fp"] in old_pages.get(h["page"], []):
            kept.append(h)
            seen.add((h["page"], h["fp"]))
        else:
            outside.append(h)
    stale = [(p, fp) for p, fps in old_pages.items() for fp in fps if (p, fp) not in seen]
    return _entries_from_hits(kept), outside, stale


# ── 帳本 ────────────────────────────────────────────────────────────────────

def append_change(changes_path: Path, file: str, added: list[dict], removed: list[dict],
                  reason: str, actor: str, today: date | None = None) -> dict:
    row = {
        "date": (today or date.today()).isoformat(),
        "file": file,
        "added": added,
        "removed": removed,
        "reason": reason,
        "actor": actor,
    }
    changes_path.parent.mkdir(parents=True, exist_ok=True)
    with changes_path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def rebuild(hits: list[dict], baseline_path: Path, changes_path: Path, *,
            allow_grow: bool = False, reason: str | None = None, actor: str = "unknown",
            today: date | None = None) -> tuple[int, str]:
    """收緊（預設）或在帳本登記下擴張基線。回傳 (exit code, 訊息)。拒絕時不寫任何檔。"""
    old = load_baseline(baseline_path)
    new_hits, pairs, unused = match(hits, old)
    if allow_grow and not (reason and reason.strip()):
        return 1, "拒絕：--allow-grow 必須附非空的 --reason \"…\""
    if new_hits and not allow_grow:
        lines = [f"拒絕：{len(new_hits)} 筆基線外的新增超限，--rebuild 只准移除／收緊條目，基線檔未動"]
        for h in new_hits[:20]:
            lines.append(f"  {h['page']}.md:{h['line']}  [{h['kind']}｜錨點「{h['anchor']}」｜{h['length']} 字元]")
        lines.append("修法：把這些列縮到上限內或下沉；確屬必要的例外由主 session 人工以 "
                     "--allow-grow --reason 登記（記者不得使用）")
        return 1, "\n".join(lines)
    kept = [h for h, _ in pairs] + (new_hits if allow_grow else [])
    pages = _entries_from_hits(kept)
    added = baseline_growth(old, pages)
    removed = baseline_growth(pages, old)  # 舊有、新無或被收緊的條目
    try:
        raw = json.loads(baseline_path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        raw = {}
    keep_meta = {k: v for k, v in raw.items() if k.startswith("_migrated")}
    write_baseline(pages, baseline_path, extra=keep_meta)
    msg = (f"已重建基線：{len(kept)} 筆（移除／收緊 {len(removed)}，新增 {len(added)}；"
           f"未使用槽位 {len(unused)}）")
    if added:
        try:
            rel = baseline_path.relative_to(ROOT).as_posix()
        except ValueError:
            rel = baseline_path.name
        append_change(changes_path, rel, added, removed, reason or "", actor, today)
        msg += f"\n已登記帳本：{changes_path.name} +1 行"
    return 0, msg


def _default_actor() -> str:
    try:
        return getpass.getuser()
    except Exception:  # noqa: BLE001
        return "unknown"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="字元上限機械閘")
    ap.add_argument("--page", help="只掃某頁（slug 片段）")
    ap.add_argument("--rebuild", action="store_true", help="收緊存量基線（只移除／縮短條目）")
    ap.add_argument("--allow-grow", action="store_true", help="與 --rebuild 併用：允許新增條目（需 --reason）")
    ap.add_argument("--reason", help="--allow-grow 的理由（寫入 data/baseline-changes.jsonl）")
    ap.add_argument("--actor", default=None, help="帳本 actor 欄（預設為系統使用者名）")
    ap.add_argument("--migrate-legacy", action="store_true", help="一次性：舊指紋基線轉錨點格式")
    args = ap.parse_args(argv)
    out = _stdout()

    files = target_files()
    if args.page:
        files = [f for f in files if args.page in page_id(f)]

    hits = scan(files)

    if args.migrate_legacy:
        if args.page:
            out.write("拒絕：--migrate-legacy 必須掃全庫\n")
            out.flush()
            return 1
        data = json.loads(BASELINE.read_text(encoding="utf-8"))
        if not is_legacy_format(data):
            out.write("拒絕：基線已是錨點格式，不需遷移\n")
            out.flush()
            return 1
        pages, outside, stale = migrate_legacy(data, hits)
        n = sum(len(v) for v in pages.values())
        write_baseline(pages, extra={"_migrated": date.today().isoformat(),
                                     "_migrated_from_hits": data.get("_hits")})
        out.write(f"已遷移：舊指紋 {data.get('_hits')} 筆 → 錨點條目 {n} 筆\n")
        for p, fp in stale:
            out.write(f"  舊基線有、現況無（丟棄）：{p} {fp}\n")
        for h in outside:
            out.write(f"  現況超限但不在舊基線（不收，仍會 FAIL）：{h['page']}.md:{h['line']} {h['anchor']}\n")
        out.flush()
        return 0

    if args.allow_grow and not args.rebuild:
        out.write("拒絕：--allow-grow 只能與 --rebuild 併用\n")
        out.flush()
        return 1

    if args.rebuild:
        if args.page:
            out.write("拒絕：--rebuild 必須掃全庫，不可只憑單頁重建基線\n")
            out.flush()
            return 1
        try:
            code, msg = rebuild(hits, BASELINE, CHANGES, allow_grow=args.allow_grow,
                                reason=args.reason, actor=args.actor or _default_actor())
        except BaselineError as e:
            out.write(f"FAIL: {e}\n")
            out.flush()
            return 1
        out.write(msg + "\n")
        out.flush()
        return code

    try:
        baseline = load_baseline()
    except BaselineError as e:
        out.write(f"FAIL: 字元上限機械閘 — {e}\n")
        out.flush()
        return 1
    new, legacy = split_hits(hits, baseline)

    if new:
        out.write(f"FAIL: 字元上限機械閘 — {len(new)} 筆新增的超限儲存格／條列\n\n")
        for h in new:
            what = "表格儲存格（>120）" if h["kind"] == "table_cell" else "細節區條列（>200）"
            out.write(f"  {h['page']}.md:{h['line']}  [{what}，實測 {h['length']} 字元｜錨點「{h['anchor']}」]\n")
            out.write(f"    {h['snippet']}...\n\n")
        out.write("修法：查證過程／原文比對／多來源歧異一律下沉到表格正下方的細節區；細節區"
                  "條列本身仍受 200 字元上限拘束，超過就拆成兩條或改用 wikilink 指回事實的家\n")
        out.write("判定方式：存量列改寫不變長即放行（同錨點＝表格首格／條列開頭；長度不超過基線）；"
                  "被點名代表錨點不在基線或比基線長。確屬新內容請縮短或下沉；不得 rebuild\n")

    # 存量 WARN 摘要（供 /wiki-lint 抄進回報）
    by_page: dict[str, int] = {}
    for h in legacy:
        by_page[h["page"]] = by_page.get(h["page"], 0) + 1
    top = sorted(by_page.items(), key=lambda kv: -kv[1])[:5]
    out.write(f"\nWARN: 存量基線內 {len(legacy)} 筆／{len(by_page)} 頁"
              f"（前 5 頁：{'、'.join(f'{p}({n})' for p, n in top) or '無'}）\n")
    if not new:
        out.write("OK: 字元上限機械閘 — 無新增超限\n")
    out.flush()
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
