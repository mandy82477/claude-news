#!/usr/bin/env python3
"""wiki_search.py — wiki 全文檢索（隨需建索引，零落地檔案，零第三方依賴）。

為什麼有這支：查詢分流第 2 路原本靠 `wiki/index.md` 的一句摘要挑頁，但摘要
不含頁面正文的用詞（2026-09-14 教訓：問「agent 視覺化」，答案頁寫的是
「可觀測性／協調地圖」，摘要一個字都沒沾到，關鍵字篩候選直接漏掉）。本腳本
把檢索面換成**全文**——每頁按標題切段，段為文件做 BM25 排序，回傳頁＋最佳段
標題＋行號，可直接 Read offset 跳讀。

查詢改寫橋接「同概念、不同用詞」（視覺化 ↔ 可觀測性）：BM25 只比字面，語意由
呼叫端補——跑這支的永遠是 Claude session，它把原句改寫成幾種說法當額外參數傳入。
每種說法各自排序，分數先除以該說法的最高分（長句不會光靠詞多就壓過短句），
再把同一頁在各說法的得分加總——多種說法都排得上的頁更像答案。本腳本不養同義詞表：表會靜默過期，改寫不會。

`--expand` 圖擴散：把字面／改寫命中的前幾頁當種子，沿 wikilink 圖走一跳，被多個
種子共同指到的頁加回候選（標「圖擴散」＋種子名）。解「相關頁但沒共用任何詞」那類
漏；邊的取捨借 wiki_graph.py：樣板區／階層邊不算、index／log 樞紐排除、鄰居度數
高者壓權。已由字面或改寫找到的頁不再疊加圖分數（兩路取其一，不重複加分）。

斷詞：英數連續段為一詞（保留 `.`/`-`/`_`/`+`，命中 v2.1.211、stream-json）；
CJK 連續段取 bigram（單字段取 unigram）。不裝 jieba——bigram 對繁中檢索
足夠且無依賴，與雲端沙盒／CI 環境無關。

用法：
  python scripts/wiki_search.py "<問題原句>" ["<改寫 1>" "<改寫 2>" …] [--top N] [--expand] [--sections] [--json]
"""
from __future__ import annotations

import argparse
import io
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_web import WIKI_DIR, strip_markdown_to_text  # noqa: E402
from gen_wiki_frontmatter import strip_body  # noqa: E402
from wiki_graph import _neighbor_sets, _parse_page  # noqa: E402

EXCLUDE_PAGES = {"index", "log", "CLAUDE", "metrics", "reader-notes"}

K1 = 1.5
B = 0.75
# 頁分數＝最佳段＋次佳兩段的折扣，不做全段加總：否則數百段的大頁光靠段數就壓過小頁
RUNNER_UP_WEIGHT = 0.25
# 原句實詞 token 的 idf 覆蓋率門檻：低於此值視為只沾到零碎 bigram（「量子」「麵包」），不算命中；
# 但段落命中 ≥ MIN_MATCHED 個相異實詞也算找到——長句的附帶詞（執行狀態、協作）會稀釋分母，不能只看比率
MIN_COVERAGE = 0.3
MIN_MATCHED = 3
# 查詢端剔除含虛字的 CJK bigram（「有哪」「哪些」「相關的」）：它們只是句法，不是要找的概念
STOP_CHARS = set("的有哪些與和是在了嗎呢麼怎可以什會被把及或就都還很請要想找給我你他它們這那個")
# 「用」只在落單時是虛字（「用 hooks 做」）；成對時多半是實詞（費用、用量、使用），剔掉會讓成本類問句只剩 token 一個詞
STOP_UNIGRAMS = STOP_CHARS | {"用"}
# 圖擴散：種子＝覆蓋率達標的前 SEED_TOP 頁；鄰居分數＝Σ(種子相對分數／√鄰居度數)×最高分×EXPAND_WEIGHT
SEED_TOP = 5
EXPAND_WEIGHT = 0.5
# 沒指定 --top 時的候選頁數：帶改寫時放寬，否則每種說法的第一名就把名額佔滿
DEFAULT_TOP = 5
DEFAULT_TOP_WITH_REWRITES = 8
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LATIN_RE = re.compile(r"[a-z0-9][a-z0-9._+\-/]*[a-z0-9]|[a-z0-9]")
CJK_RE = re.compile(r"[㐀-鿿]+")


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens: list[str] = []
    for m in re.finditer(r"[a-z0-9][a-z0-9._+\-/]*|[㐀-鿿]+", text):
        seg = m.group(0)
        if CJK_RE.fullmatch(seg):
            if len(seg) == 1:
                tokens.append(seg)
            else:
                tokens.extend(seg[i:i + 2] for i in range(len(seg) - 1))
        else:
            tokens.append(seg.strip("._+-/"))
    return [t for t in tokens if t]


@dataclass
class Section:
    page: str
    heading: str
    line: int
    text: str
    tokens: list[str] = field(default_factory=list)


def split_sections(page: str, raw: str) -> list[Section]:
    body = strip_body(raw)
    offset = raw.count("\n") - body.count("\n")
    sections: list[Section] = []
    heading, start, buf = "（頁首）", 1, []
    for i, line in enumerate(body.splitlines(), start=1):
        m = HEADING_RE.match(line)
        if m:
            if buf:
                sections.append(Section(page, heading, start + offset, "\n".join(buf)))
            heading, start, buf = m.group(2), i, [line]
        else:
            buf.append(line)
    if buf:
        sections.append(Section(page, heading, start + offset, "\n".join(buf)))
    for s in sections:
        s.tokens = tokenize(strip_markdown_to_text(s.text))
    return [s for s in sections if s.tokens]


def iter_wiki_files(wiki_dir: Path = WIKI_DIR):
    for p in sorted(wiki_dir.rglob("*.md")):
        if p.stem in EXCLUDE_PAGES:
            continue
        yield p


def page_slug(path: Path, wiki_dir: Path = WIKI_DIR) -> str:
    return path.relative_to(wiki_dir).with_suffix("").as_posix()


def build_adjacency(files, wiki_dir: Path = WIKI_DIR) -> dict[str, set[str]]:
    """正文 wikilink 的無向鄰居表；解析與取捨規則全借 wiki_graph（樣板／階層邊不算、樞紐排除）。"""
    pages = {page_slug(p, wiki_dir): p for p in files}
    links = []
    for slug, f in pages.items():
        _, ls = _parse_page(slug, f)
        links.extend(l for l in ls if l.dst in pages)
    adj, _ = _neighbor_sets(links, pages)
    return adj


class Index:
    def __init__(self, sections: list[Section], adjacency: dict[str, set[str]] | None = None):
        self.sections = sections
        self.adjacency = adjacency or {}
        self.df: Counter = Counter()
        for s in sections:
            self.df.update(set(s.tokens))
        self.n = len(sections)
        self.avgdl = sum(len(s.tokens) for s in sections) / max(self.n, 1)
        self.tf = [Counter(s.tokens) for s in sections]

    @classmethod
    def from_files(cls, files, wiki_dir: Path = WIKI_DIR) -> "Index":
        sections: list[Section] = []
        files = list(files)
        for p in files:
            sections.extend(split_sections(page_slug(p, wiki_dir), p.read_text(encoding="utf-8")))
        return cls(sections, build_adjacency(files, wiki_dir))

    def idf(self, term: str) -> float:
        n_t = self.df.get(term, 0)
        return math.log(1 + (self.n - n_t + 0.5) / (n_t + 0.5))

    def score(self, weighted_terms: dict[str, float]) -> list[tuple[float, int]]:
        out = []
        for i, s in enumerate(self.sections):
            tf, dl = self.tf[i], len(s.tokens)
            sc = 0.0
            for term, w in weighted_terms.items():
                f = tf.get(term)
                if not f:
                    continue
                sc += w * self.idf(term) * f * (K1 + 1) / (f + K1 * (1 - B + B * dl / self.avgdl))
            if sc > 0:
                out.append((sc, i))
        out.sort(key=lambda x: -x[0])
        return out


def content_tokens(tokens: list[str]) -> list[str]:
    kept = [t for t in tokens
            if not (CJK_RE.fullmatch(t) and (t in STOP_UNIGRAMS if len(t) == 1 else set(t) & STOP_CHARS))]
    return kept or tokens


def query_weights(query: str) -> dict[str, float]:
    """查詢句的實詞 token，權重一律 1。"""
    return {t: 1.0 for t in content_tokens(tokenize(query))}


def snippet(text: str, weights: dict[str, float], width: int = 90) -> str:
    plain = re.sub(r"\s+", " ", strip_markdown_to_text(text))
    low = plain.lower()
    best = None
    for term, w in sorted(weights.items(), key=lambda kv: -kv[1]):
        pos = low.find(term)
        if pos >= 0 and (best is None or w > best[0]):
            best = (w, pos)
    if best is None:
        return plain[:width]
    start = max(0, best[1] - width // 3)
    return ("…" if start else "") + plain[start:start + width] + ("…" if start + width < len(plain) else "")


def coverage(index: Index, tokens: set[str], original: dict[str, float]) -> tuple[float, int]:
    """回傳 (查詢句實詞的 idf 加權覆蓋率, 命中的相異實詞數)。"""
    total = sum(index.idf(t) for t in original)
    if total <= 0:
        return 0.0, 0
    got, n = 0.0, 0
    for t in original:
        if t in tokens:
            got += index.idf(t)
            n += 1
    return got / total, n


def is_found(cov: float, matched: int) -> bool:
    return cov >= MIN_COVERAGE or matched >= MIN_MATCHED


def expand_by_graph(pages: list[dict], adjacency: dict[str, set[str]], top: int) -> list[dict]:
    """種子＝覆蓋率達標的前 SEED_TOP 頁。回傳擴散進來的新頁（原本沒被字面／改寫找到的），至多 top//2。"""
    seeds = [e for e in pages if e["found"]][:SEED_TOP]
    if not seeds:
        return []
    top_score = seeds[0]["score"] or 1.0
    boost: dict[str, float] = {}
    via: dict[str, list[str]] = {}
    for seed in seeds:
        for n in adjacency.get(seed["page"], ()):
            deg = max(1, len(adjacency.get(n, ())))
            boost[n] = boost.get(n, 0.0) + seed["rel"] / math.sqrt(deg)
            via.setdefault(n, []).append(seed["page"])
    already = {e["page"] for e in pages if e["found"]}
    out = []
    for n, b in sorted(boost.items(), key=lambda kv: -kv[1]):
        if n in already:
            continue
        out.append({"page": n, "score": round(EXPAND_WEIGHT * top_score * b, 2), "rel": EXPAND_WEIGHT * b,
                    "coverage": 0.0, "found": True, "matched": 0, "source": "圖擴散", "via": via[n],
                    "variant": "", "sections": []})
    return out[: max(1, top // 2)]


def rank_one(query: str, index: Index) -> list[dict]:
    """單一說法的頁排序。`rel`＝分數÷該說法最高分，跨說法融合時加總它，不加總原始 BM25 分數。"""
    weights = query_weights(query)
    by_page: dict[str, dict] = {}
    for sc, i in index.score(weights):
        s = index.sections[i]
        entry = by_page.setdefault(s.page, {"page": s.page, "sections": []})
        cov, matched = coverage(index, set(s.tokens), weights)
        entry["sections"].append({"heading": s.heading, "line": s.line, "score": round(sc, 2),
                                  "coverage": round(cov, 2), "matched": matched, "found": is_found(cov, matched),
                                  "snippet": snippet(s.text, weights)})
    pages = []
    for e in by_page.values():
        e["sections"].sort(key=lambda x: -x["score"])
        top_secs = e["sections"][:3]
        e["score"] = round(top_secs[0]["score"] + RUNNER_UP_WEIGHT * sum(x["score"] for x in top_secs[1:]), 2)
        e["coverage"] = max(x["coverage"] for x in top_secs)
        e["found"] = any(x["found"] for x in top_secs)
        e["matched"] = max(x["matched"] for x in top_secs)
        e["via"] = []
        pages.append(e)
    pages.sort(key=lambda e: -e["score"])
    best = pages[0]["score"] if pages and pages[0]["score"] else 1.0
    for e in pages:
        e["rel"] = e["score"] / best
    return pages


def search(queries: str | list[str], index: Index, top: int = DEFAULT_TOP, expand: bool = False):
    """`queries` 第一句是使用者原句，其餘是呼叫端的改寫。每種說法各自排序，頁的融合分數＝
    它在各說法「找到」時的 rel 加總——多種說法都排得上的頁，比只在一種說法裡第一名的頁更像答案。
    顯示用的段落與來源取該頁最好的那一次（平手歸原句）。"""
    if isinstance(queries, str):
        queries = [queries]
    queries = list(dict.fromkeys(q for q in queries if q.strip()))
    best: dict[str, dict] = {}
    fused: dict[str, float] = {}
    for order, q in enumerate(queries):
        for e in rank_one(q, index):
            e["variant"] = q
            e["source"] = "字面命中" if order == 0 else "改寫命中"
            if e["found"]:
                fused[e["page"]] = fused.get(e["page"], 0.0) + e["rel"]
            old = best.get(e["page"])
            if old is None or (e["found"], e["rel"]) > (old["found"], old["rel"]):
                best[e["page"]] = e
    peak = max(fused.values(), default=0.0) or 1.0
    for page, e in best.items():
        e["rel"] = fused[page] / peak if e["found"] else 0.0
    found_pages = sorted((e for e in best.values() if e["found"]), key=lambda e: -e["rel"])
    expanded = expand_by_graph(found_pages, index.adjacency, top) if expand else []
    # 擴散頁一律以「圖擴散」身分進榜；字面／改寫已找到的頁不疊加圖分數（兩路取其一）
    expanded_slugs = {x["page"] for x in expanded}
    weak_pages = sorted((e for e in best.values() if not e["found"] and e["page"] not in expanded_slugs),
                        key=lambda e: -e["score"])
    ranked = (sorted(found_pages + expanded, key=lambda e: -e["rel"]) + weak_pages)[:top]
    variant_hits = {q: sum(1 for e in ranked if e["found"] and e["variant"] == q) for q in queries}
    return {"query": queries[0], "variants": queries[1:], "variant_hits": variant_hits, "pages": ranked,
            "found": any(e["found"] for e in ranked), "expanded": expand}


def render(result: dict, show_sections: bool) -> str:
    lines = [f"查詢：{result['query']}"]
    if result["variants"]:
        hits = result["variant_hits"]
        lines.append("改寫：" + "｜".join(f"{v}（{hits.get(v, 0)} 頁）" for v in result["variants"]))
    if not result["found"]:
        steps = []
        if not result["variants"]:
            steps.append("把原句改寫成幾種說法（中英對譯、wiki 可能的用詞、上下位詞）當額外參數再查")
        if not result["expanded"]:
            steps.append("加 --expand 沿 wikilink 圖擴散")
        steps.append("換路（專有名詞走 Grep、近況走 log.md）")
        lines.append(f"零命中（沒有任何候選段的實詞覆蓋率達 {MIN_COVERAGE} 或命中 ≥{MIN_MATCHED} 個實詞）。下一步：{'；'.join(steps)}。")
        return "\n".join(lines)
    lines.append(f"候選頁（{len(result['pages'])} 頁，全部要開，不憑摘要跳過）：")
    for r, e in enumerate(result["pages"], start=1):
        if e["source"] == "圖擴散":
            lines.append(f"{r}. [[{e['page']}]]  分數 {e['score']}  來源 圖擴散（種子 {', '.join(e['via'])} 都指到它）")
            continue
        best = e["sections"][0]
        flag = "" if e["found"] else "  ⚠ 低覆蓋"
        source = e["source"] if e["source"] == "字面命中" else f"改寫命中「{e['variant']}」"
        lines.append(f"{r}. [[{e['page']}]]  分數 {e['score']}  覆蓋 {e['coverage']}（{best['matched']} 實詞）{flag}  來源 {source}  最佳段 § {best['heading']}  行 {best['line']}")
        lines.append(f"   {best['snippet']}")
        if show_sections:
            for x in e["sections"][1:4]:
                lines.append(f"   · § {x['heading']}  行 {x['line']}  分數 {x['score']}")
    if not result["expanded"] and (len(result["pages"]) < 3 or not all(e["found"] for e in result["pages"])):
        lines.append("候選少或有低覆蓋 → 建議再跑一次加 --expand。")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="wiki 全文檢索")
    ap.add_argument("queries", nargs="+", metavar="query", help="第一句是問題原句，其餘是改寫")
    ap.add_argument("--top", type=int, default=None)
    ap.add_argument("--expand", action="store_true", help="以命中頁為種子沿 wikilink 圖擴散一跳")
    ap.add_argument("--sections", action="store_true", help="每頁多列前幾個命中段")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    index = Index.from_files(iter_wiki_files())
    top = args.top or (DEFAULT_TOP if len(args.queries) == 1 else DEFAULT_TOP_WITH_REWRITES)
    result = search(args.queries, index, top=top, expand=args.expand)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    else:
        print(render(result, args.sections))
    return 0 if result["found"] else 1


if __name__ == "__main__":
    sys.exit(main())
