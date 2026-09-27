#!/usr/bin/env python3
"""build_ingest_packets.py — wiki ingest 主編端：由一張 routing 表產出分類帳與六記者派工包。

主編每天的判斷產物只有一張「url → 類別（或排除理由）」表；分類帳、派工節錄、來源 slug、
同事件聚合、「已收錄比對」都是機械搬運，手做最容易錯（手抄 slug、漏則、同一事件 14 家媒體
各佔一則、前一天已歸因的 URL 記者各自 grep 半天）。本腳本把搬運收成一支。

routing 檔（主編唯一要寫的檔，JSON）：
    {"<url>": {"categories": ["功能"], "reason": "", "note": "", "summary_override": ""}}
  - categories 空陣列＝排除，reason 必填
  - note 只准是該則條目的事實性註記（寫進該則 `- **註：**`）；以「請／記得／順手／同步」
    起句的祈使句一律擋下——派工 prompt 不得臨場加寫操作指示的機械版
  - summary_override 選填：原料摘要是殼層（剝 HTML 後空白、只剩 HN 殼標記或過短）時由主編補寫，
    寫進分類帳的 summary 並另存同名欄位留痕；排除條目是殼層卻沒補，對帳會擋
  - 其餘鍵（title、source）只供主編閱讀，腳本忽略；`--init` 產生的骨架就帶這兩鍵

流程（任一步失敗 exit 1，且不寫帳、不產包）：
  1. 驗 routing：原料每個 URL 都在、沒有原料外的 URL、類別合法、排除有理由、note 無祈使句、
     每個來源（含 contributors）都對得到 data/source_registry.json 的 name／aliases
  2. 在記憶體裡模擬 append 後跑 check_classification_log.audit；有阻斷問題就不寫
  3. append 分類帳（與同 URL 最後一行完全相同者跳過，重跑冪等），再跑一次對帳 CLI 當閘
  4. 產包：每類一份 `<類別>.md`（>25K 字元切 `<類別>-k.md`）＋`排除.md`，印路徑與大小

exit 0 產包完成｜1 routing／來源／對帳有阻斷問題｜3 原料或日報缺檔

用法：
    python scripts/build_ingest_packets.py --date 2026-09-26 --init --routing data/ingest-packets/2026-09-26/routing.json
    python scripts/build_ingest_packets.py --date 2026-09-26 --routing data/ingest-packets/2026-09-26/routing.json --out data/ingest-packets/2026-09-26/
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "src" / "gathered_archive"
NEWS = ROOT / "news"
LOG = ROOT / "data" / "classification-log.jsonl"
REGISTRY = ROOT / "data" / "source_registry.json"
ATTRIBUTION = ROOT / "data" / "source_attribution.jsonl"

CATEGORY_ORDER = ("模型", "功能", "商業", "安全政策", "社群", "人物")
EXCLUDED_NAME = "排除"
MAX_CHARS = 25_000
SUMMARY_MAX = 240
PACKET_SUMMARY_MAX = 400


def _load_ccl():
    """check_classification_log 是對帳的單一真相源：殼層定義、類別集合、audit 都借它的。"""
    name = "check_classification_log"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ccl = _load_ccl()

# ── 文字清理 ─────────────────────────────────────────────────────────────

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_TAG = re.compile(r"<[^>]*>")
_OPEN_TAG_TAIL = re.compile(r"<[^>]*$")  # 原料摘要在 240 字處截斷，常留下沒收尾的 `<a href="…`
_TOPIC_BOILERPLATE = re.compile(r"^【專頁定向抓取：[^】]*】[^。]*。\s*")
_WS = re.compile(r"\s+")
_GN_ID = re.compile(r"news\.google\.com/rss/articles/([A-Za-z0-9_-]+)")


def clean_summary(raw: str) -> str:
    s = _COMMENT.sub(" ", raw or "")
    s = _TAG.sub(" ", s)
    s = _OPEN_TAG_TAIL.sub(" ", s)
    s = html.unescape(s)
    s = _TOPIC_BOILERPLATE.sub("", s.strip())
    return _WS.sub(" ", s).strip()


def is_shell(summary: str, title: str = "") -> bool:
    """殼層定義的單一來源是 check_classification_log._is_pure_shell（純殼標記、或剝掉標題後
    只剩出版者的標題回聲）；另加它的 MIN_SUMMARY 太短判斷——兩者都讓複核記者無從判斷。"""
    if ccl._is_pure_shell(summary, title):
        return True
    return len(ccl._strip_shell_markers(summary).strip()) < ccl.MIN_SUMMARY


# 起句祈使：note 開頭，或句號／分號／驚嘆號／換行之後。逗號後不算——
# 「兩家媒體數字不同，請並陳」是 classification.md 明列的合法事實性提示。
_IMPERATIVE = re.compile(r"(?:^|[。；;！!？?\n])\s*(請|記得|順手|同步)")


def imperative_hit(note: str) -> str | None:
    m = _IMPERATIVE.search(note or "")
    return m.group(1) if m else None


# ── 來源 slug ────────────────────────────────────────────────────────────

def load_registry(path: Path = REGISTRY) -> list[tuple[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries: list[tuple[str, str]] = []
    for s in data.get("sources", []):
        slug = s.get("slug")
        if not slug:
            continue
        for name in [s.get("name"), *(s.get("aliases") or [])]:
            if name:
                entries.append((name, slug))
    return entries


def slug_for(label: str, entries: list[tuple[str, str]]) -> str | None:
    """整串相等，或最長的「名稱 / 子來源」前綴：
    「GitHub Issues / claude-code」要對到 github-issues，不能被較短的 GitHub 搶走；
    「GitHub Search」只認 alias，不因字首是 GitHub 就混過去（alias 被拿掉要報未註冊）。"""
    label = (label or "").strip()
    best: tuple[str, str] | None = None
    for name, slug in entries:
        rest = label[len(name):] if label.startswith(name) else None
        if rest is not None and (rest == "" or rest.lstrip().startswith("/")):
            if best is None or len(name) > len(best[0]):
                best = (name, slug)
    return best[1] if best else None


def item_labels(it: dict) -> list[str]:
    labels = [it.get("source") or ""]
    for c in it.get("contributors") or []:
        labels.append(c if isinstance(c, str) else str(c.get("source", "")))
    return labels


def item_slugs(it: dict, entries) -> tuple[list[str], list[str]]:
    """回傳 (slug 清單去重保序, 未註冊的來源標籤)。"""
    slugs: list[str] = []
    missing: list[str] = []
    for lab in item_labels(it):
        s = slug_for(lab, entries)
        if s is None:
            missing.append(lab)
        elif s not in slugs:
            slugs.append(s)
    return slugs, missing


def source_line(it: dict) -> str:
    contrib = [c if isinstance(c, str) else str(c.get("source", "")) for c in it.get("contributors") or []]
    return it.get("source", "?") + (" ＋" + "、".join(contrib) if contrib else "")


# ── 日報段落 ─────────────────────────────────────────────────────────────

_LINK_URL = re.compile(r"\]\((https?://[^)\s]+)\)")


def digest_index(text: str) -> dict[str, dict]:
    """url → {"para": 條目段落原文, "lines": [(區塊名, 行)]}。

    日報兩種形狀：`**[標題](url)**` 起頭的條目段落（到空行為止），與今日聚焦／專頁雷達的
    `- ` 清單行。兩種都照原文擷取，不改寫。"""
    out: dict[str, dict] = {}
    lines = text.splitlines()
    section = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            section = line[4:].strip()
        urls = _LINK_URL.findall(line)
        if urls and line.startswith("**[") and line.rstrip().endswith(")**"):
            block = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip():
                block.append(lines[j])
                j += 1
            out.setdefault(urls[-1], {"para": "", "lines": []})["para"] = "\n".join(block)
            i = j
            continue
        if urls and line.lstrip().startswith("- "):
            for u in urls:
                out.setdefault(u, {"para": "", "lines": []})["lines"].append((section, line.strip()))
        i += 1
    return out


# ── 已收錄比對 ───────────────────────────────────────────────────────────

_TITLE_TAIL = re.compile(r"\s+[-–—|]\s+[^-–—|]{1,60}$")


def norm_title(t: str) -> str:
    t = html.unescape(t or "").strip()
    t = _TITLE_TAIL.sub("", t)
    return _WS.sub(" ", t).lower()


def load_attribution(path: Path = ATTRIBUTION) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return rows


class PriorIndex:
    """查 data/source_attribution.jsonl：同一篇在目標日之前歸因過到哪頁哪天。

    比對鍵三種：URL 原樣、Google News 文章 id（早期歸因存的是 news.google.com 跳轉網址，
    原料摘要裡的 id 被截斷，故用前綴比）、正規化標題（只當弱訊號，另標「同標題」）。"""

    def __init__(self, rows: list[dict], date: str):
        self.by_url: dict[str, list[dict]] = {}
        self.gn: list[tuple[str, dict]] = []
        self.by_title: dict[str, list[dict]] = {}
        for r in rows:
            if str(r.get("date", "")) >= date:
                continue
            u = r.get("item_url") or ""
            self.by_url.setdefault(u, []).append(r)
            m = _GN_ID.search(u)
            if m:
                self.gn.append((m.group(1), r))
            t = norm_title(r.get("item_title", ""))
            if t:
                self.by_title.setdefault(t, []).append(r)

    def lookup(self, it: dict) -> tuple[list[dict], list[dict]]:
        strong = list(self.by_url.get(it.get("url", ""), []))
        ids = _GN_ID.findall((it.get("summary") or "") + " " + (it.get("url") or ""))
        for pid in ids:
            if len(pid) < 24:
                continue
            for aid, r in self.gn:
                if aid.startswith(pid) or pid.startswith(aid):
                    strong.append(r)
        weak = [r for r in self.by_title.get(norm_title(it.get("title", "")), []) if r not in strong]
        return strong, weak


def _fmt_prior(rows: list[dict]) -> list[str]:
    seen: list[str] = []
    for r in sorted(rows, key=lambda r: (r.get("date", ""), r.get("page", ""))):
        s = f"{r.get('date')} 已歸因至 {r.get('page')}"
        if s not in seen:
            seen.append(s)
    return seen


def prior_text(strong: list[dict], weak: list[dict]) -> str:
    parts = _fmt_prior(strong)
    parts += [f"{s}（同標題、URL 不同，未必同一篇）" for s in _fmt_prior(weak)]
    return "；".join(parts[:6]) + ("；…" if len(parts) > 6 else "")


# ── 同事件聚合 ───────────────────────────────────────────────────────────
# 標題相近是保守的補充依據：原料的 dedup_key 多半是變更偵測鍵、contributors 是已被併掉的來源，
# 同一事件十幾家媒體各自成則時兩欄都是空的。但「prompt injection」「Opus 5.5」「cloud session」
# 這種共用詞會把不同事件串在一起，所以只算長度 ≥4、不含數字、不是模型名或新聞泛用詞的
# 顯著詞，且要共用 ≥3 個。寧可漏併（記者多讀幾則），不可誤併（次條目被當成同一件事略過）。

_STOP = set("""
with from that this what when where which while about after over into onto upon than then them they
their there these those your have been will would could should might says said just more most
also only even still very much many some such each both other another here amid among around
make makes made take takes taking give gives come comes goes going gets know need wants want
company companies firm firms year years week today first last next back down away
report reports reported news update updates latest launch launches launched introduce introducing
anthropic claude code openai google microsoft model models agent agents show tell
opus sonnet haiku fable gpt chatgpt gemini llama mistral grok deepseek codex qwen kimi
""".split())
_WORD = re.compile(r"[a-z0-9][a-z0-9.'’&-]*|[一-鿿]{2,}")
TOKEN_MIN_LEN = 4
TITLE_OVERLAP = 3
# 高頻主題詞：算進共用詞數，但兩則之間至少要有一個共用詞不在這張表裡才併——
# 「raises billion funding round」「signs cloud computing deal」「court rules pentagon blacklist」
# 「fixes usage limit」這種詞組在不同事件間反覆出現（不同家融資、不同家雲端交易、地院與上訴兩次裁定、
# 不同版本的修正）。表內放的是 title_tokens 取詞後的形狀（長於 5 字元會剝 s／ed／ing）。
_HIGH_FREQ = set("""
billion million trillion deal deals raise raises round funding fund valuation investor investment
cloud computing comput compute sign signs contract partnership
pentagon court judge ruling rules rule federal blacklist lawsuit government
usage limit limits fixes fix fixed update release version issue
price pricing plan plans user users developer enterprise security
""".split())


def title_tokens(title: str) -> set[str]:
    toks: set[str] = set()
    for w in _WORD.findall(norm_title(title)):
        w = w.replace("’", "'")
        if w.endswith("'s"):
            w = w[:-2]
        w = w.replace(".", "").strip("'-&")
        if any(ch.isdigit() for ch in w):  # 版本號、金額、數字一律不算
            continue
        for suf in ("ing", "ed", "s"):
            if len(w) > 5 and w.endswith(suf):
                w = w[: -len(suf)]
                break
        if len(w) >= TOKEN_MIN_LEN and w not in _STOP:
            toks.add(w)
    return toks


def group_items(items: list[dict]) -> list[list[dict]]:
    """同 dedup_key、或標題顯著詞交集 ≥ TITLE_OVERLAP（互為 contributors 時放寬一個）者
    聯成一組（union-find），保持原料順序。"""
    n = len(items)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    toks = [title_tokens(it.get("title", "")) for it in items]
    for a in range(n):
        for b in range(a + 1, n):
            ia, ib = items[a], items[b]
            dk = ia.get("dedup_key") or ""
            if dk and dk == (ib.get("dedup_key") or ""):
                union(a, b)
                continue
            common = toks[a] & toks[b]
            if not (common - _HIGH_FREQ):
                continue
            mutual = ia.get("source") in item_labels(ib)[1:] or ib.get("source") in item_labels(ia)[1:]
            if len(common) >= TITLE_OVERLAP or (mutual and len(common) >= TITLE_OVERLAP - 1):
                union(a, b)
    groups: dict[int, list[int]] = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    return [[items[i] for i in idxs] for _, idxs in sorted(groups.items())]


def _published_key(it: dict) -> str:
    return str(it.get("published") or "~")  # 「MM/DD HH:MM UTC」同年內字串序即時間序；缺值排最後


def pick_main(group: list[dict]) -> dict:
    """互動數最高者為主，同分取最早發布；與類別、日報收錄與否無關，全日各包一致。"""
    order = {id(it): i for i, it in enumerate(group)}
    return sorted(group, key=lambda it: (-(it.get("score") or 0), _published_key(it), order[id(it)]))[0]

# ── routing 驗證 ─────────────────────────────────────────────────────────

def validate_routing(routing: dict, items: list[dict], entries) -> list[str]:
    problems: list[str] = []
    if not isinstance(routing, dict):
        return ["routing 檔必須是 {url: {...}} 物件"]
    urls = [it.get("url") for it in items]
    for it in items:
        u = it.get("url")
        if u not in routing:
            problems.append(f"routing 漏了原料（主編沒判）：{str(it.get('title', ''))[:60]}｜{u}")
    for u in routing:
        if u not in urls:
            problems.append(f"routing 有但原料沒有（URL 打錯？）：{u}")
    for u, v in routing.items():
        if not isinstance(v, dict):
            problems.append(f"routing 值必須是物件：{u}")
            continue
        cats = v.get("categories")
        if not isinstance(cats, list):
            problems.append(f"categories 必須是陣列：{u}")
            continue
        bad = [c for c in cats if c not in CATEGORY_ORDER]
        if bad:
            problems.append(f"未知類別 {bad}：{u}")
        if not cats and not str(v.get("reason") or "").strip():
            problems.append(f"排除但沒寫理由：{u}")
        hit = imperative_hit(str(v.get("note") or ""))
        if hit:
            problems.append(f"note 以「{hit}」起句＝操作指示，不是事實註記（派工 prompt 不得臨場加寫；"
                            f"下週仍成立的去改規則檔）：{u}")
    for it in items:
        _, missing = item_slugs(it, entries)
        for lab in missing:
            problems.append(f"未註冊來源「{lab}」（data/source_registry.json 無對應 name／aliases）："
                            f"{str(it.get('title', ''))[:60]}")
    return problems


# ── 分類帳 ───────────────────────────────────────────────────────────────

def log_rows_for(date: str, items: list[dict], routing: dict) -> list[dict]:
    rows = []
    for it in items:
        v = routing[it["url"]]
        auto = clean_summary(it.get("summary", ""))[:SUMMARY_MAX]
        override = str(v.get("summary_override") or "").strip()[:SUMMARY_MAX]
        row = {"date": date, "url": it["url"], "title": it.get("title", ""),
               "source": it.get("source", ""), "summary": override or auto,
               "categories": list(v.get("categories") or []), "reason": str(v.get("reason") or "")}
        if override:
            row["summary_override"] = override
        rows.append(row)
    return rows


def pending_appends(existing: list[dict], new_rows: list[dict], date: str) -> list[dict]:
    last: dict[str, dict] = {}
    for r in existing:
        if isinstance(r, dict) and r.get("date") == date and isinstance(r.get("url"), str):
            last[r["url"]] = r
    keys = ("categories", "reason", "summary")
    return [r for r in new_rows
            if not (r["url"] in last and all(last[r["url"]].get(k) == r[k] for k in keys))]


# ── 產包 ─────────────────────────────────────────────────────────────────

def _flag_lines(it: dict, dindex: dict, digest_text: str) -> list[str]:
    out = []
    if it.get("url", "") not in digest_text:
        out.append("- **日報未收錄**（僅原始抓取資料，摘要較簡略）")
    if it.get("topic"):
        out.append(f"- **專頁定向**（目標頁：topics/{it['topic']}；收錄判準為該專頁觸發條件，"
                   "**不套用 Claude/Anthropic 關聯門檻**）")
    return out


def _digest_line_items(d: dict) -> list[str]:
    return [f"- **日報「{section or '清單'}」行：** {ln[2:] if ln.startswith('- ') else ln}"
            for section, ln in d.get("lines", [])]


def _score(it: dict) -> str:
    s = f"{it.get('score', 0)} {it.get('score_unit', '')}".strip()
    if (it.get("source_count") or 1) > 1:
        s += f"（{it['source_count']} 個來源）"
    return s


def _item_summary(it: dict, v: dict) -> str:
    summary = str(v.get("summary_override") or "").strip() or clean_summary(it.get("summary", ""))
    if is_shell(summary, it.get("title", "")):
        summary = (summary + "　" if summary else "") + "（殼層摘要：原料無可讀內文，以標題、URL 與日報段落判讀）"
    return summary[:PACKET_SUMMARY_MAX]


def item_lines(it: dict, cat: str, ctx: dict) -> list[str]:
    """一則條目的完整欄位（不含標題行）。主條目與同組其他則共用同一份、只差縮排——
    次條目少了摘要、日期或「同時派給」，記者就只能憑標題猜它是不是同一件事。"""
    routing, entries, dindex, digest_text, prior = (ctx["routing"], ctx["entries"], ctx["dindex"],
                                                     ctx["digest_text"], ctx["prior"])
    v = routing[it["url"]]
    slugs, _ = item_slugs(it, entries)
    lines = [f"- **來源：** {source_line(it)}（slug：{'、'.join(slugs)}）",
             f"- **URL：** {it['url']}",
             f"- **日期：** {it.get('published', '')}",
             f"- **互動：** {_score(it)}",
             f"- **摘要：** {_item_summary(it, v)}"]
    d = dindex.get(it["url"], {})
    if d.get("para"):
        lines.append("- **日報段落：**")
        lines += ["  > " + ln for ln in d["para"].splitlines()]
    lines += _digest_line_items(d)
    lines += _flag_lines(it, dindex, digest_text)
    others = [c for c in v.get("categories") or [] if c != cat]
    if others:
        lines.append(f"- **同時派給：** {'、'.join(others)}（各記者只寫自己那一面）")
    strong, weak = prior.lookup(it)
    if strong or weak:
        lines.append(f"- **已收錄比對：** {prior_text(strong, weak)}")
    if str(v.get("note") or "").strip():
        lines.append(f"- **註：** {v['note'].strip()}")
    return lines


def render_group(members: list[dict], main: dict, cat: str, ctx: dict) -> str:
    """members＝本包裡屬於這一組的條目；main＝全日共用的主條目（可能不在本包）。
    主條目在本包就完整列出；不在（它只派給別類）就寫一行指路，本包各則全列為同組其他報導——
    同一 URL 在所有包裡角色一致。"""
    rest = [it for it in members if it is not main]
    if main in members:
        block = [f"### {main.get('title', '')}", *item_lines(main, cat, ctx)]
    else:
        where = "、".join(ctx["routing"][main["url"]].get("categories") or [])
        block = [f"### 〔同事件〕{main.get('title', '')}",
                 f"- **主條目不在本包**（派給 {where}：{main['url']}），本包只收同組以下各則"]
    if rest:
        block.append(f"- **同事件其他報導（{len(rest)} 則，依 dedup_key／contributors／標題顯著詞聚合；"
                     "歸因時每則各報一筆）：**")
        for it in rest:
            block.append(f"  - 〔同組〕{it.get('title', '')}")
            block += ["    " + ln for ln in item_lines(it, cat, ctx)]
    return "\n".join(block)


def assemble(cat: str, blocks: list[tuple[str, int]], total_items: int, max_chars: int) -> list[str]:
    """blocks：(組的 markdown, 該組則數)。回傳各份全文；超過 max_chars 依組邊界切份。"""
    n_groups = len(blocks)
    head = f"## [{cat}] 條目（共 {total_items} 則（{n_groups} 組））"
    single = head + "\n\n" + "\n\n".join(b for b, _ in blocks) + f"\n\nEND {total_items}\n"
    if len(single) <= max_chars:
        return [single]
    parts: list[list[tuple[str, int]]] = [[]]
    budget = max_chars - len(head) - 120
    size = 0
    for b, k in blocks:
        if parts[-1] and size + len(b) + 2 > budget:
            parts.append([])
            size = 0
        parts[-1].append((b, k))
        size += len(b) + 2
    out = []
    for idx, p in enumerate(parts, 1):
        k_items = sum(k for _, k in p)
        h = f"{head}｜第 {idx}／{len(parts)} 份：本份 {k_items} 則（{len(p)} 組）"
        out.append(h + "\n\n" + "\n\n".join(b for b, _ in p)
                   + f"\n\nEND {total_items}｜第 {idx}／{len(parts)} 份（本份 {k_items} 則）\n")
    return out


def render_excluded(items: list[dict], ctx: dict) -> str:
    blocks = []
    for it in items:
        v = ctx["routing"][it["url"]]
        slugs, _ = item_slugs(it, ctx["entries"])
        lines = [f"### {it.get('title', '')}",
                 f"- **URL：** {it['url']}",
                 f"- **來源：** {source_line(it)}（slug：{'、'.join(slugs)}）",
                 f"- **互動：** {_score(it)}",
                 f"- **摘要：** {_item_summary(it, v)}"]
        lines += _flag_lines(it, ctx["dindex"], ctx["digest_text"])
        lines.append(f"- **主編排除理由：** {v.get('reason', '').strip()}")
        blocks.append("\n".join(lines))
    return (f"## [{EXCLUDED_NAME}] 條目（共 {len(items)} 則）\n\n" + "\n\n".join(blocks)
            + f"\n\nEND {len(items)}\n")


def build_packets(date: str, items: list[dict], routing: dict, digest_text: str, entries,
                  attribution: list[dict], max_chars: int = MAX_CHARS) -> dict[str, list[str]]:
    """純函式：回傳 {類別或「排除」: [各份全文]}。無條目的類別不出現。

    聚合在全日「有派工」的條目上做一次、主條目全日共用，各包再取自己那幾則——
    同一 URL 不會在一份包當主、另一份當次。"""
    ctx = {"routing": routing, "entries": entries, "dindex": digest_index(digest_text),
           "digest_text": digest_text, "prior": PriorIndex(attribution, date)}
    routed = [it for it in items if routing[it["url"]].get("categories")]
    groups = [(g, pick_main(g)) for g in group_items(routed)]
    out: dict[str, list[str]] = {}
    for cat in CATEGORY_ORDER:
        blocks = []
        n_items = 0
        for g, main in groups:
            members = [it for it in g if cat in (routing[it["url"]].get("categories") or [])]
            if not members:
                continue
            blocks.append((render_group(members, main, cat, ctx), len(members)))
            n_items += len(members)
        if blocks:
            out[cat] = assemble(cat, blocks, n_items, max_chars)
    excluded = [it for it in items if not routing[it["url"]].get("categories")]
    if excluded:
        out[EXCLUDED_NAME] = [render_excluded(excluded, ctx)]
    return out


def packet_filenames(name: str, n_parts: int) -> list[str]:
    return [f"{name}.md"] if n_parts == 1 else [f"{name}-{k}.md" for k in range(1, n_parts + 1)]


def write_packets(out_dir: Path, packets: dict[str, list[str]]) -> list[tuple[Path, int, str]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in (*CATEGORY_ORDER, EXCLUDED_NAME):  # 清掉上一輪同名包，免得切份數變了留下舊份
        for old in [out_dir / f"{name}.md", *out_dir.glob(f"{name}-*.md")]:
            if old.exists():
                old.unlink()
    written = []
    for name, parts in packets.items():
        for fn, text in zip(packet_filenames(name, len(parts)), parts):
            p = out_dir / fn
            p.write_text(text, encoding="utf-8", newline="\n")
            written.append((p, len(text), text.splitlines()[0]))
    return written


# ── CLI ──────────────────────────────────────────────────────────────────

def _use_utf8_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def init_routing(path: Path, items: list[dict]) -> int:
    if path.exists():
        print(f"❌ {path} 已存在，不覆寫（主編的判斷只有這一份）")
        return 1
    path.parent.mkdir(parents=True, exist_ok=True)
    skel = {it["url"]: {"title": it.get("title", ""), "source": it.get("source", ""),
                        "categories": [], "reason": "", "note": ""} for it in items}
    path.write_text(json.dumps(skel, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"已產生 routing 骨架 {path}（{len(items)} 則）：逐則填 categories，排除者填 reason")
    return 0


def main(argv: list[str] | None = None) -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True)
    ap.add_argument("--routing", type=Path, required=True)
    ap.add_argument("--out", type=Path, help="預設 data/ingest-packets/<date>/")
    ap.add_argument("--init", action="store_true", help="只產生 routing 骨架（檔案已存在則拒絕）")
    ap.add_argument("--log", type=Path, default=LOG)
    ap.add_argument("--archive-dir", type=Path, default=ARCHIVE)
    ap.add_argument("--news-dir", type=Path, default=NEWS)
    ap.add_argument("--registry", type=Path, default=REGISTRY)
    ap.add_argument("--attribution", type=Path, default=ATTRIBUTION)
    ap.add_argument("--max-chars", type=int, default=MAX_CHARS)
    args = ap.parse_args(argv)

    archive = args.archive_dir / f"{args.date}.json"
    digest = args.news_dir / f"{args.date}.md"
    if not archive.exists():
        print(f"❌ 原料缺檔：{archive}（先照 check_classification_log 的 exit 2／3 判斷是逾窗還是抓料缺件）")
        return 3
    items = json.loads(archive.read_text(encoding="utf-8")).get("items") or []
    if args.init:
        return init_routing(args.routing, items)
    if not digest.exists():
        print(f"❌ 日報缺檔：{digest}")
        return 3
    digest_text = digest.read_text(encoding="utf-8")
    try:
        routing = json.loads(args.routing.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"❌ routing 讀不到或不是合法 JSON：{args.routing}（{e}）")
        return 1
    entries = load_registry(args.registry)

    problems = validate_routing(routing, items, entries)
    if problems:
        print(f"❌ routing 有 {len(problems)} 個問題，未寫帳、未產包：")
        for p in problems:
            print(f"  - {p}")
        return 1

    existing = ccl.load_log(args.log)
    new_rows = log_rows_for(args.date, items, routing)
    appends = pending_appends(existing, new_rows, args.date)
    pre, _ = ccl.audit(items, existing + appends, args.date)
    if pre:
        print(f"❌ 模擬對帳有 {len(pre)} 個阻斷問題，未寫帳、未產包：")
        for p in pre:
            print(f"  - {p}")
        print("殼層排除條目請在 routing 補 summary_override。")
        return 1
    if appends:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        with args.log.open("a", encoding="utf-8", newline="\n") as f:
            for r in appends:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"分類帳：append {len(appends)} 行（{len(new_rows) - len(appends)} 行與帳上最後一行相同，略過）→ {args.log}")
    rc = ccl.main(["--date", args.date, "--log", str(args.log), "--archive-dir", str(args.archive_dir)])
    if rc != 0:
        print(f"❌ check_classification_log exit {rc}，不產包")
        return 1

    shells = [it for it in items
              if is_shell(str(routing[it["url"]].get("summary_override") or "").strip()
                          or clean_summary(it.get("summary", "")), it.get("title", ""))]
    packets = build_packets(args.date, items, routing, digest_text, entries,
                            load_attribution(args.attribution), args.max_chars)
    out_dir = args.out or (ROOT / "data" / "ingest-packets" / args.date)
    written = write_packets(out_dir, packets)
    print(f"\n# 派工包 {args.date} → {out_dir}")
    for p, size, head in written:
        print(f"  {p}  {size:,} 字元｜{head}")
    missing = [c for c in CATEGORY_ORDER if c not in packets]
    if missing:
        print("無條目、不派工：" + "、".join(missing))
    if EXCLUDED_NAME not in packets:
        print("排除 0 則，未派複核")
    if shells:
        print(f"\n殼層摘要 {len(shells)} 則（包內已標註；需要時在 routing 補 summary_override 後重跑）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
