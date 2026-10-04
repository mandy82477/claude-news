#!/usr/bin/env python3
"""collect_reporter_reports.py — wiki ingest 主編端收報落帳：記者回報 → 歸因帳、轉知指令、log 骨架。

記者回報照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」的欄位骨架。主編過去逐筆
手抄「來源歸因」成 JSON、手打 pending_handoffs close／open 指令、手拼 log 條目——手抄歸因最容易錯
（slug 打錯、頁面路徑少一段、URL 貼成別則）。本腳本解析回報、驗證、落帳。

做的事：
  - 來源歸因：每行 `slug | 類別 | page | url | title`（半形／全形分隔、表格列皆可）→ 驗 slug 在
    data/source_registry.json、wiki/<page>.md 存在、url 在當日原料（不在只警示）→ append
    data/source_attribution.jsonl（slug／page 驗不過的行警示且不寫；欄非「無」卻解析出 0 行也警示；
    與帳上完全相同的行略過，重跑冪等）
  - 轉知處置「已處理 H-xxxxxx（…）」→ 印出並（--apply 時）執行 pending_handoffs close（同批多份回報
    提到同一單只結一次）
  - 同步自查「⚠️ 需主編轉知[類別]記者：…」→ 每個 ⚠️ 各印一條 pending_handoffs open 指令草稿
    （負責人依 wiki/index.md 推）；沒點名記者的 ⚠️（主編自己的活，如 index 列）原樣帶進 log 骨架。
    草稿不自動執行——轉知要不要登帳是主編判斷
  - 對帳：回報提到的原料 URL 必須 ⊆ 該記者派工包的 URL（否則警示）；包裡的條目在回報中 URL、標題、
    issue 編號都沒出現的，列成「未回應清單」供主編追問
  - 分類回退、新增頁面、index.md 狀態變更、feature-radar 新增彙整成 log 條目骨架印到 stdout

預設 --dry-run（只印不寫）；--apply 才寫。所有驗證在任何寫入之前做完，寫入不會中途停。

exit 0 完成（警示不擋）｜1 有回報解析不出記者類別

用法：
    python scripts/collect_reporter_reports.py --date 2026-09-26 reports/功能.md reports/社群.md
    python scripts/collect_reporter_reports.py --date 2026-09-26 data/ingest-packets/2026-09-26/reports/
    python scripts/collect_reporter_reports.py --date 2026-09-26 data/ingest-packets/2026-09-26/reports/ --apply
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "src" / "gathered_archive"
REGISTRY = ROOT / "data" / "source_registry.json"
ATTRIBUTION = ROOT / "data" / "source_attribution.jsonl"
HANDOFFS = ROOT / "data" / "pending-handoffs.jsonl"
WIKI = ROOT / "wiki"
PACKETS = ROOT / "data" / "ingest-packets"

CATEGORIES = ("模型", "功能", "商業", "安全政策", "社群", "人物")
MARKET = "投資分析"  # 4c 衍生記者：不吃分類路由、沒有派工包、回報少「分類回退」欄，歸因類別寫「投資分析」
DEVPRACTICE = "開發實務"  # 4b 衍生記者：有官方使用指南條目時才有派工包；回報沒有「分類回退」欄
REPORTERS = (*CATEGORIES, MARKET, DEVPRACTICE)
HANDOFF_CATEGORIES = REPORTERS
CORE_FIELDS = ("更新頁面", "feature-radar 新增", "index.md 狀態變更", "新增頁面", "同步自查",
               "待查證命中處置", "轉知處置", "分類回退", "來源歸因")
# 投資分析記者的專屬欄（.claude/reporter-rules/market/daily.md）也要認得，否則會被併進上一欄
FIELDS = (*CORE_FIELDS, "機械自查", "判讀新增", "買得到的標的", "里程碑登記", "回顧結算 ⏳ 新增")


def _load(name: str):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ph = _load("pending_handoffs")

# ── 解析 ─────────────────────────────────────────────────────────────────

_HEADER = re.compile(r"^#{1,3}\s*\[?(" + "|".join(REPORTERS) + r")\]?\s*記者回報")
_FIELD = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?(" + "|".join(re.escape(f) for f in FIELDS)
                    + r")(?:\*\*)?\s*[：:]\s*(.*)$")
# 回報裡不在契約內的「xxx：」段標（如「其他處置說明：」）——遇到就結束當前欄，免得被黏進上一欄
_OTHER_LABEL = re.compile(r"^(?:\*\*)?(?!https?\b|H-[0-9a-f])([^\s|｜：:`#\-*>][^|｜：:`]{0,24}?)(?:\*\*)?[：:]\s*")
_QUALITY = re.compile(r"^\s*\|\s*呈現品質審查\s*\|\s*(.*?)\s*\|?\s*$")
_URL = re.compile(r"https?://[^\s|｜)）\]>」`\"'<，。；]+")
_HID = re.compile(r"H-[0-9a-f]{6}")
_HANDOFF_ASK = re.compile(r"主編轉知\s*\[?(" + "|".join(HANDOFF_CATEGORIES) + r")\]?\s*記者\s*[：:，,]?\s*(.*)", re.S)
_PAGE = re.compile(r"(?:\[\[)?((?:topics|entities|concepts|comparisons|guides)/[A-Za-z0-9_.\-/]+?)"
                   r"(?:\.md)?(?=[\]|#）)（(`\s，,。；、]|$)")


def parse_report(text: str) -> dict | None:
    """回傳 {"category", "fields": {欄名: 全文}, "urls": set, "raw"}；找不到「## [類別] 記者回報」回 None。

    取最後一個表頭：記者常先寫一段敘述性的「## [類別] 記者回報」，再在 code block 裡給正式版。"""
    lines = text.splitlines()
    starts = [i for i, ln in enumerate(lines) if _HEADER.match(ln.strip())]
    if not starts:
        return None
    start = starts[-1]
    category = _HEADER.match(lines[start].strip()).group(1)
    fields: dict[str, str] = {}
    cur: str | None = None
    # 正式版回報本身常包在 code block 裡：表頭之前的 fence 數為奇數＝表頭在 block 內。
    # 這種情況下欄位是一般行，block 的收尾 ``` 才是「進入 fence」的反面，故以奇偶起算。
    opened = sum(1 for ln in lines[:start] if ln.strip().startswith("```")) % 2 == 1
    in_fence = False
    for ln in lines[start + 1:]:
        if opened and ln.strip().startswith("```"):
            opened = False  # 包住整份回報的 block 收尾，不是欄位值的 fence
            cur = None
            continue
        s = ln.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            if not in_fence:
                cur = None  # 欄位值的 block 收尾＝這一欄結束，之後的敘述不得再併進來
            continue
        if in_fence:  # 欄位值包在 code block 裡（歸因列、feature-radar 條目草稿）：原樣收進當前欄
            if cur and s:
                fields[cur] = (fields[cur] + "\n" + s).strip()
            continue
        q = _QUALITY.match(ln)
        if q:
            fields["呈現品質審查"] = q.group(1)
            cur = None
            continue
        m = _FIELD.match(ln)
        if m:
            cur = m.group(1)
            fields[cur] = m.group(2).strip()
            continue
        if not s:
            if cur and fields[cur]:  # 空行結束已有內容的欄；「來源歸因：」後緊接空行再列表不算結束
                cur = None
            continue
        if s.startswith("#") or (not ln[:1].isspace() and _OTHER_LABEL.match(s) and not s.startswith(("-", "*"))):
            cur = None
            continue
        if cur:
            fields[cur] = (fields[cur] + "\n" + s).strip()
    return {"category": category, "fields": fields,
            "urls": {u.rstrip(".,;") for u in _URL.findall(text)}, "raw": text}


def _is_none(val: str) -> bool:
    v = val.strip()
    return v in ("", "無", "無。", "不適用", "無待接手", "無命中") or v.startswith(("無（", "無(", "不適用（"))


def parse_attribution(val: str) -> tuple[list[tuple[str, str, str, str, str]], list[str]]:
    """回傳 (歸因列, 解析不了的行)。分隔符半形 | 或全形 ｜ 皆可；`| a | b | … |` 表格列去頭尾框線，
    表頭列與 `---` 分隔列略過。title 內含分隔符時併回最後一欄。"""
    rows: list[tuple[str, str, str, str, str]] = []
    bad: list[str] = []
    for raw in val.splitlines():
        ln = raw.strip().lstrip("•").strip()
        if ln.startswith(("- ", "* ")):
            ln = ln[2:].strip()
        if _is_none(ln):
            continue
        ln = ln.replace("｜", "|")
        if ln.startswith("|"):
            ln = ln.strip("|").strip()
            if re.fullmatch(r"[\s|:\-]*", ln) or ln.lower().startswith("slug"):
                continue
        parts = [p.strip() for p in ln.split("|")]
        if len(parts) < 5:
            bad.append(raw.strip())
            continue
        rows.append((parts[0], parts[1], parts[2], parts[3], " | ".join(parts[4:]).strip()))
    return rows, bad


# ── 驗證 ─────────────────────────────────────────────────────────────────

def registry_slugs(path: Path = REGISTRY) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {s["slug"] for s in data.get("sources", []) if s.get("slug")}


def archive_urls(date: str, archive_dir: Path = ARCHIVE) -> set[str] | None:
    p = archive_dir / f"{date}.json"
    if not p.exists():
        return None
    return {it.get("url") for it in json.loads(p.read_text(encoding="utf-8")).get("items") or []}


_PACKET_TITLE = re.compile(r"^(?:###\s+(?:〔同事件〕)?|\s+-\s+〔同組〕)(.+)$")
_PACKET_URL = re.compile(r"URL：\**\s*(https?://\S+?)(?=｜|\s|$)")


def packet_entries(packet_dir: Path, category: str) -> dict[str, str] | None:
    """該記者包裡的 url → 標題（含切份）。找不到包回 None。"""
    files = [packet_dir / f"{category}.md", *sorted(packet_dir.glob(f"{category}-*.md"))]
    files = [f for f in files if f.exists()]
    if not files:
        return None
    out: dict[str, str] = {}
    for f in files:
        title = ""
        for ln in f.read_text(encoding="utf-8").splitlines():
            tm = _PACKET_TITLE.match(ln)
            if tm:
                title = tm.group(1).strip()
                continue
            um = _PACKET_URL.search(ln)
            if um:
                out[um.group(1)] = title
    return out


_TITLE_TAIL = re.compile(r"\s+[-–—|]\s+[^-–—|]{1,60}$")
_ISSUE = re.compile(r"/(?:issues|pull)/(\d+)")


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


_SHOW = re.compile(r"^(?:show|ask|tell|launch)\s+hn\s*:\s*", re.I)


def name_keys(url: str, title: str, packet: dict[str, str]) -> list[str]:
    """條目的「短名」：Show HN 標題冒號後、破折號前的產品名；GitHub repo 名；包內唯一的網域名。
    記者在說明段常只寫短名（「Tui2web 7 分未達門檻」），只比全標題會把它們全列成未回應。"""
    keys: list[str] = []
    head = re.split(r"\s[–—-]\s|:|,|｜|\|", _SHOW.sub("", _TITLE_TAIL.sub("", title or "")).strip())[0].strip()
    if 4 <= len(head) and len(head.split()) <= 3:
        keys.append(head)
    gm = re.match(r"https?://github\.com/[^/]+/([^/#?]+)", url)
    if gm and len(gm.group(1)) >= 4:
        keys.append(gm.group(1))
    hm = re.match(r"https?://(?:www\.)?([^/]+)", url)
    if hm and not gm:
        label = hm.group(1).split(".")[-2] if hm.group(1).count(".") >= 1 else hm.group(1)
        if len(label) >= 2 and label not in ("reddit", "google", "youtube"):
            keys.append(label)  # 網域名去點與 TLD：newscientist、ft、makeuseof
    tail = re.search(r"\s[-–—|]\s([^-–—|]{2,60})$", title or "")
    if tail:
        keys.append(tail.group(1).strip())  # 出版者：New Scientist、Yahoo Tech
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9'’.-]*", _SHOW.sub("", _TITLE_TAIL.sub("", title or "")))
             if len(w) >= 4 and w.lower().rstrip("'’s") not in _COMMON]
    keys += words[:3]  # 標題前 3 個顯著詞：Microsoft、Accenture
    return keys


_COMMON = set("""
anthropic claude code openai show with from that this your what have just about into over after says
will more when than they them their been were does into only also here some such very much make
using used uses first could would should asked gave made tried
""".split())



def mentioned(url: str, title: str, report_urls: set[str], report_text: str,
              packet: dict[str, str] | None = None) -> bool:
    """回報裡出現該則的 URL、標題（去出版者尾巴取前 40 字，至少 12 字）、issue／PR 編號或短名
    （產品名、repo 名、網域名、出版者、標題前 3 個顯著詞），任一命中都算回應。短名去空白與標點後
    比對，「New Scientist」對得上 newscientist；只有英數字邊界，「（FT）」對得上 ft。"""
    if url in report_urls:
        return True
    t = _norm(_TITLE_TAIL.sub("", title or ""))[:40]
    text = _norm(report_text)
    if len(t) >= 12 and t in text:
        return True
    m = _ISSUE.search(url)
    if m and re.search(rf"(?<!\d){m.group(1)}(?!\d)", report_text):
        return True
    for k in name_keys(url, title, packet or {}):
        parts = [p for p in re.split(r"[\s.\-_'’]+", k.lower()) if p]
        if not parts or len("".join(parts)) < 2:
            continue
        pat = r"[\s.\-_'’]*".join(re.escape(p) for p in parts)
        if re.search(rf"(?<![a-z0-9]){pat}(?![a-z0-9])", text):
            return True
    return False


_BULK = {"reddit": "reddit.com/"}  # 記者常以「Reddit 4 則未達門檻」整批帶過


def bulk_answered(packet: dict[str, str], report_text: str) -> set[str]:
    """回報寫「<平台> N 則」且 N 等於包裡該平台的則數 → 這批整批算已回應。"""
    out: set[str] = set()
    for name, frag in _BULK.items():
        urls = [u for u in packet if frag in u]
        for m in re.finditer(name + r"\s*(\d+)\s*則", report_text, re.I):
            if urls and int(m.group(1)) == len(urls):
                out.update(urls)
    return out


def load_ledger_keys(path: Path) -> set[tuple]:
    keys = set()
    if not path.exists():
        return keys
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        keys.add((r.get("date"), r.get("source"), r.get("category"), r.get("page"), r.get("item_url")))
    return keys


def check_attribution(rows, category: str, date: str, slugs: set[str], wiki_dir: Path,
                      day_urls: set[str] | None) -> tuple[list[dict], list[str]]:
    good: list[dict] = []
    warns: list[str] = []
    for slug, cat, page, url, title in rows:
        tag = f"[{category}] {slug} | {page} | {url[:70]}"
        page_n = ph.normalize_page(page.strip("`"))
        bad = False
        if slug not in slugs:
            warns.append(f"未註冊 slug「{slug}」，不寫入：{tag}")
            bad = True
        if not (wiki_dir / f"{page_n}.md").exists():
            warns.append(f"頁面不存在 wiki/{page_n}.md，不寫入：{tag}")
            bad = True
        if cat not in REPORTERS:
            warns.append(f"未知類別「{cat}」，不寫入：{tag}")
            bad = True
        elif cat != category:
            warns.append(f"歸因類別「{cat}」與記者類別「{category}」不同（照記者寫的落帳）：{tag}")
        if not bad and day_urls is not None and url not in day_urls:
            warns.append(f"URL 不在 {date} 原料（仍寫入，請核對是否貼錯）：{tag}")
        if not bad:
            good.append({"date": date, "source": slug, "category": cat, "page": page_n,
                         "item_url": url, "item_title": title})
    return good, warns


# ── 轉知 ─────────────────────────────────────────────────────────────────

_OPEN_P, _CLOSE_P = "（(", "）)"


def _balanced(s: str) -> str | None:
    """s 以（或 ( 開頭時取到對應的收括號（容許巢狀、全半形混用）；沒收尾就取到行尾。"""
    if not s or s[0] not in _OPEN_P:
        return None
    depth = 0
    for i, ch in enumerate(s):
        if ch in _OPEN_P:
            depth += 1
        elif ch in _CLOSE_P:
            depth -= 1
            if depth == 0:
                return s[1:i].strip()
    return s[1:].split("\n")[0].strip()


def handoff_closes(val: str) -> list[tuple[str, str]]:
    """「已處理 N 筆: H-a, H-b（補了 X）」→ [(id, result)]。只取「已處理」段，「不適用」段留給主編判斷。"""
    if _is_none(val):
        return []
    m = re.search(r"已處理(.*?)(?:／\s*不適用|/\s*不適用|\n\s*不適用|$)", val, re.S)
    if not m:
        return []
    seg = m.group(1)
    out = []
    for hm in _HID.finditer(seg):
        result = _balanced(seg[hm.end():].lstrip()) or ""
        out.append((hm.group(0), result))
    return out


def handoff_voids(val: str) -> list[str]:
    m = re.search(r"不適用(.*)$", val or "", re.S)
    return _HID.findall(m.group(1)) if m else []


def split_warnings(val: str) -> list[str]:
    """同步自查欄每個 ⚠️ 各成一段（同一行以「；⚠️」連寫、或分行列出都拆開）。"""
    return [p.strip().rstrip("；;") for p in re.split(r"(?=⚠️)", val or "") if p.strip().startswith("⚠️")]


def handoff_asks(val: str) -> tuple[list[tuple[str, str]], list[str]]:
    """回傳 (點名記者的轉知 [(目標類別, 要做什麼)], 沒點名記者的 ⚠️ 原文)。"""
    asks, other = [], []
    for seg in split_warnings(val):
        m = _HANDOFF_ASK.search(seg)
        if m:
            asks.append((m.group(1), m.group(2).strip()))
        else:
            other.append(seg)
    return asks, other


def draft_open(src: str, dst: str, note: str, index_path: Path, wiki_dir: Path) -> list[str]:
    pm = _PAGE.search(note)
    page = ph.normalize_page(pm.group(1)) if pm else None
    safe = note.replace('"', "'").replace("\n", " ")
    if not page:
        return [f'python scripts/pending_handoffs.py open --from {src} --to {dst} --page <待填> --note "{safe}"']
    owner, _ = ph.owner_of(page, index_path, wiki_dir)
    if owner == src:
        return []  # 推出的負責人就是回報者自己：開單會變成自己轉給自己，交主編判斷（呼叫端列進主編待辦）
    cmd = f'python scripts/pending_handoffs.py open --from {src} --to {{to}} --page {page} --note "{safe}"'
    if owner and owner != dst:
        return [cmd.format(to=owner) + f"   # index 推負責人＝{owner}（記者點名 {dst}）",
                cmd.format(to=dst) + " --force --reason \"<為何轉給非負責記者>\""]
    if owner is None:
        return [cmd.format(to=dst) + "   # index 查不到負責人，確屬例外才加 --force --reason"]
    return [cmd.format(to=dst)]


# ── log 骨架 ─────────────────────────────────────────────────────────────

def radar_titles(val: str) -> str:
    """feature-radar 欄常貼整段條目草稿：骨架只取 ### 標題行；沒有標題行就取第一行。"""
    heads = [ln.lstrip("#").strip() for ln in val.splitlines() if ln.startswith("###")]
    return "、".join(heads) if heads else val.splitlines()[0].strip()


def log_skeleton(date: str, reports: list[dict], closes, opens, editor_todos) -> str:
    def collect(field):
        return [(r["category"], r["fields"].get(field, "")) for r in reports
                if not _is_none(r["fields"].get(field, ""))]
    out = [f"## {date} Ingest", "", f"- 來源日報：[[news/{date}]]", "- 更新頁面："]
    for r in reports:
        out.append(f"  - **{r['category']}**：{r['fields'].get('更新頁面', '（回報缺欄）') or '無'}")
    new_pages = collect("新增頁面")
    out.append("- 新增頁面：" + ("；".join(v for _, v in new_pages) if new_pages else "無"))
    fr = [(c, radar_titles(v)) for c, v in collect("feature-radar 新增")]
    out.append("- feature-radar：" + ("；".join(f"[{c}] {v}" for c, v in fr) if fr else "本日無新功能"))
    idx = collect("index.md 狀態變更")
    out.append("- index：" + ("；".join(v for _, v in idx) if idx else "無"))
    out.append("- 摘要：（主編補寫一句）")
    q = [(r["category"], r["fields"].get("呈現品質審查", "")) for r in reports]
    bad_q = [f"[{c}] {v}" for c, v in q if v and ("⚠️" in v or "📋" in v)]
    out.append("- 呈現品質：" + ("；".join(bad_q) if bad_q else "全部通過"))
    back = collect("分類回退")
    out.append("- 分類回退：" + ("；".join(f"[{c}] {v}" for c, v in back) if back else "無")
               + ("（待主編依 SKILL.md 步驟 3b 處理）" if back else ""))
    ho = []
    if closes:
        ho.append("結案 " + "、".join(f"{h}（{c}）" for c, h, _ in closes))
    if opens:
        ho.append("新開（草稿，登帳後補單號）" + "；".join(f"{s}→{d}：{n[:40]}" for s, d, n in opens))
    out.append("- 轉知帳本：" + ("；".join(ho) if ho else "無"))
    if editor_todos:
        out.append("- 主編待辦（同步自查 ⚠️ 未點名記者，原文）：")
        out += [f"  - [{c}] {t}" for c, t in editor_todos]
    return "\n".join(out)


# ── CLI ──────────────────────────────────────────────────────────────────

def _use_utf8_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def _expand(paths: list[Path]) -> list[Path]:
    out = []
    for p in paths:
        out += sorted(p.glob("*.md")) if p.is_dir() else [p]
    return out


def main(argv: list[str] | None = None) -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True)
    ap.add_argument("reports", nargs="+", type=Path, help="回報檔或存放回報檔的目錄")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="預設：只印不寫")
    mode.add_argument("--apply", action="store_true", help="append 歸因帳並執行 close")
    ap.add_argument("--packets", type=Path, help="派工包目錄，預設 data/ingest-packets/<date>/")
    ap.add_argument("--attribution", type=Path, default=ATTRIBUTION)
    ap.add_argument("--handoffs", type=Path, default=HANDOFFS)
    ap.add_argument("--registry", type=Path, default=REGISTRY)
    ap.add_argument("--archive-dir", type=Path, default=ARCHIVE)
    ap.add_argument("--wiki-dir", type=Path, default=WIKI)
    args = ap.parse_args(argv)

    index_path = args.wiki_dir / "index.md"
    packet_dir = args.packets or (PACKETS / args.date)
    slugs = registry_slugs(args.registry)
    day_urls = archive_urls(args.date, args.archive_dir)
    warns: list[str] = []
    if day_urls is None:
        warns.append(f"找不到 {args.date} 原料，URL 在不在當日原料無法驗")

    reports: list[dict] = []
    for f in _expand(args.reports):
        r = parse_report(f.read_text(encoding="utf-8"))
        if r is None:
            print(f"❌ {f} 找不到「## [類別] 記者回報」表頭，無法判定是哪位記者")
            return 1
        r["file"] = f
        reports.append(r)

    # ── 第一階段：只讀、只驗，不寫任何東西 ──
    ledger_keys = load_ledger_keys(args.attribution)
    to_write: list[dict] = []
    closes: list[tuple[str, str, str]] = []
    closing: set[str] = set()
    opens: list[tuple[str, str, str]] = []
    open_cmds: list[str] = []
    voids: list[tuple[str, str]] = []
    editor_todos: list[tuple[str, str]] = []
    unanswered: dict[str, list[tuple[str, str]]] = {}
    state = ph.load(args.handoffs)

    for r in reports:
        cat, fields = r["category"], r["fields"]
        required = [f for f in CORE_FIELDS if not (cat in (MARKET, DEVPRACTICE) and f == "分類回退")]
        missing = [f for f in required if f not in fields]
        if missing:
            warns.append(f"[{cat}] 回報缺欄：{'、'.join(missing)}（{r['file'].name}）")
        attr_val = fields.get("來源歸因", "")
        rows, bad_lines = parse_attribution(attr_val)
        for bl in bad_lines:
            warns.append(f"[{cat}] 來源歸因行解析不了（要 5 欄 slug | 類別 | page | url | title）：{bl[:90]}")
        if not _is_none(attr_val) and not rows:
            warns.append(f"[{cat}] 來源歸因欄不是「無」，卻解析出 0 行——格式跑掉了，回頭看回報原文")
        good, w = check_attribution(rows, cat, args.date, slugs, args.wiki_dir, day_urls)
        warns += w
        for row in good:
            key = (row["date"], row["source"], row["category"], row["page"], row["item_url"])
            if key in ledger_keys:
                continue
            ledger_keys.add(key)
            to_write.append(row)
        for hid, result in handoff_closes(fields.get("轉知處置", "")):
            if hid in closing:
                warns.append(f"[{cat}] {hid} 同批另一份回報已結，這份不重複結案")
                continue
            if hid not in state:
                warns.append(f"[{cat}] 回報已處理 {hid}，但帳本查無此單")
                continue
            if state[hid].get("status") != "open":
                warns.append(f"[{cat}] {hid} 帳上已是 {state[hid].get('status')}，不重複結案")
                continue
            if state[hid].get("to") != cat:
                warns.append(f"[{cat}] {hid} 帳上目標是 {state[hid].get('to')}，不是回報者")
            closing.add(hid)
            closes.append((cat, hid, result or f"{cat}記者 {args.date} ingest 回報已處理"))
        voids += [(cat, h) for h in handoff_voids(fields.get("轉知處置", ""))]
        asks, others = handoff_asks(fields.get("同步自查", ""))
        editor_todos += [(cat, t) for t in others]
        for dst, note in asks:
            if dst == cat:
                continue
            cmds = draft_open(cat, dst, note, index_path, args.wiki_dir)
            if not cmds:
                editor_todos.append((cat, f"⚠️ 轉知{dst}記者：{note}（頁面負責人依 index 推是回報者本人，未產開單草稿）"))
                continue
            opens.append((cat, dst, note))
            open_cmds += cmds
        if cat == MARKET:
            continue  # 投資分析記者吃整份日報、沒有派工包，不做 URL 對帳
        pk = packet_entries(packet_dir, cat)
        if pk is None and cat == DEVPRACTICE:
            continue  # 當日沒有官方使用指南條目就沒有包，不是缺包
        if pk is None:
            warns.append(f"[{cat}] 找不到派工包 {packet_dir}/{cat}.md，URL 對帳略過")
            continue
        extra = sorted(u for u in r["urls"] if u not in pk and (day_urls is None or u in day_urls))
        for u in extra:
            warns.append(f"[{cat}] 回報提到的原料 URL 不在該記者包裡（分錯人或貼錯？）：{u}")
        bulk = bulk_answered(pk, r["raw"])
        unanswered[cat] = sorted((u, t) for u, t in pk.items()
                                 if u not in bulk and not mentioned(u, t, r["urls"], r["raw"], pk))

    print(f"# 收報落帳 {args.date}｜{len(reports)} 份回報｜{'APPLY' if args.apply else 'DRY-RUN（加 --apply 才寫）'}")
    print(f"\n## 來源歸因：{len(to_write)} 行待 append → {args.attribution}")
    for row in to_write:
        print("  " + json.dumps(row, ensure_ascii=False))
    print(f"\n## 轉知結案（{len(closes)}）")
    for cat, hid, result in closes:
        print(f'  python scripts/pending_handoffs.py close {hid} --by {cat} --result "{result.replace(chr(34), chr(39))}"')
    if voids:
        print(f"\n## 轉知「不適用」（{len(voids)}，主編判斷：理由成立 void；不屬我則改派）")
        for cat, hid in voids:
            print(f"  [{cat}] {hid}")
    print(f"\n## 轉知開立草稿（{len(open_cmds)}，不自動執行）")
    for c in open_cmds:
        print("  " + c)
    print("\n## 未回應清單（包裡有、回報 URL／標題／issue 編號都沒提到；供主編追問）")
    any_un = False
    for cat, pairs in unanswered.items():
        if pairs:
            any_un = True
            print(f"  [{cat}] {len(pairs)} 則")
            for u, t in pairs:
                print(f"    - {t[:70]}｜{u}")
    if not any_un:
        print("  無")
    if warns:
        print(f"\n## ⚠️ 警示（{len(warns)}）")
        for w in warns:
            print(f"  - {w}")
    print("\n## log 條目骨架\n")
    print(log_skeleton(args.date, reports, closes, opens, editor_todos))

    # ── 第二階段：寫入。前面已去重、已驗 open，close 不會半途拋錯 ──
    if args.apply:
        if to_write:
            with args.attribution.open("a", encoding="utf-8", newline="\n") as f:
                for row in to_write:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
        for cat, hid, result in closes:
            ph.close_handoff(hid, by=cat, result=result, closed=None, path=args.handoffs)
        print(f"\n已 append {len(to_write)} 行歸因、結案 {len(closes)} 筆轉知。"
              "publisher 欄照舊由 scripts/enrich_attribution_publisher.py 補。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
