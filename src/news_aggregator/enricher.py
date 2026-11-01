"""Enrich FeedItems with actual article/discussion content.

Priority per item type:
  HN link post  → fetch external article via trafilatura
  HN thread     → Firebase API text + top-2 comment texts
  Reddit post   → Reddit JSON API selftext
  Other         → trafilatura on the article URL (only if summary is thin)
"""
import html
import logging
import re
import signal
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as _FutureTimeout, as_completed
from dataclasses import replace
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

MAX_SUMMARY_CHARS = 800
_THIN_THRESHOLD = 120   # existing summary shorter than this → try to enrich（量的是剝掉 HTML 後的可見文字）
_TAG_RE = re.compile(r"<[^>]*>|<[^>]*$")  # 含未閉合的半截標籤（截斷後常見）
_WORKERS = 6
_ARTICLE_TIMEOUT = 8    # per-URL cap for article fetching (trafilatura.fetch_url ignores ours)
# requests 的 timeout 是「單次 socket 等待」上限，慢速滴流（每幾秒吐一小塊）永遠不會觸發它；
# 這是整篇文章從開始讀到讀完的總預算，超過就放棄該篇、保留原摘要。
_READ_DEADLINE_S = _ARTICLE_TIMEOUT * 3
# 整批 enrichment 的牆鐘預算。到期時未完成的條目一律保留原摘要——enrichment 是加值不是必要，
# 任何一篇卡住都不得讓抓料整批失敗（2026-09-26 本機兩次連續失敗即此因：as_completed 的
# TimeoutError 沒被接住，main.py 直接崩潰）。
_ENRICH_BUDGET_S = 60
# 單篇文章 HTML 上限。6 個 worker 並行，所以最壞情況是這個數字的 6 倍常駐；
# 5 MB × 6 = 30 MB，遠低於 runner 記憶體，而正常文章頁只有幾百 KB。
_MAX_ARTICLE_BYTES = 5 * 1024 * 1024
# trafilatura.extract 在子行程裡跑的牆鐘上限。正常文章幾百 ms 就抽完；超時多半是
# lxml 在病態 HTML 上打轉，放棄該篇即可。
_EXTRACT_TIMEOUT_S = _ARTICLE_TIMEOUT
# 子行程程式碼：從 stdin 讀 HTML（UTF-8 bytes），把抽出的正文寫到 stdout。
# 刻意不 import 本專案任何模組，啟動成本只有 trafilatura 本身。
_CHILD_CODE = """\
import sys
import trafilatura
html = sys.stdin.buffer.read().decode('utf-8', 'replace')
text = trafilatura.extract(html, include_comments=False, include_tables=False, no_fallback=False)
sys.stdout.buffer.write((text or '').encode('utf-8'))
"""
_HN_FIREBASE = "https://hacker-news.firebaseio.com/v0/item/{}.json"
_HN_ITEM_RE = re.compile(r"news\.ycombinator\.com/item\?id=(\d+)")

# Domains where article extraction is useless or handled separately
_SKIP_ARTICLE_DOMAINS = frozenset([
    "github.com",
    "news.google.com",
    "reddit.com",
    "twitter.com",
    "x.com",
    "linkedin.com",
])

# Hard-paywalled domains — trafilatura only gets a login wall / teaser, so
# skip fetching entirely (saves time, avoids junk summaries). Original
# summary from the feed is kept as-is.
_PAYWALL_DOMAINS = frozenset([
    "wsj.com",
    "theinformation.com",
    "bloomberg.com",
    "ft.com",
    "nytimes.com",
])

# Shared session with larger connection pool (avoids "pool is full" warnings)
_session = requests.Session()
_adapter = HTTPAdapter(pool_connections=10, pool_maxsize=20)
_session.mount("http://", _adapter)
_session.mount("https://", _adapter)


# ── public API ────────────────────────────────────────────────────────────────

def enrich(items: list[FeedItem]) -> list[FeedItem]:
    """Return items with richer summary fields. Never raises.

    到 `_ENRICH_BUDGET_S` 仍未完成的條目保留原摘要；不用 `with`，因為 `__exit__`
    會等卡死的 worker 收工——改用 shutdown(wait=False) 讓主流程繼續，卡住的執行緒
    自己到 socket／讀取期限後結束。
    """
    result: dict[int, FeedItem] = {}
    pool = ThreadPoolExecutor(max_workers=_WORKERS)
    futures = {pool.submit(_safe_enrich, item): item for item in items}
    try:
        for fut in as_completed(futures, timeout=_ENRICH_BUDGET_S):
            original = futures[fut]
            try:
                result[id(original)] = fut.result()
            except Exception:
                result[id(original)] = original
    except _FutureTimeout:
        unfinished = [it for fut, it in futures.items() if not fut.done()]
        logger.warning("enrichment budget %ss exceeded: %d item(s) kept original summary: %s",
                       _ENRICH_BUDGET_S, len(unfinished),
                       ", ".join(it.url for it in unfinished[:5]))
    finally:
        pool.shutdown(wait=False, cancel_futures=True)
    # preserve original order; anything not finished falls back to the original item
    return [result.get(id(item), item) for item in items]


# ── per-item enrichment ───────────────────────────────────────────────────────

def _visible_len(summary: str) -> int:
    return len(re.sub(r"\s+", " ", html.unescape(_TAG_RE.sub(" ", summary or ""))).strip())


def _safe_enrich(item: FeedItem) -> FeedItem:
    try:
        return _enrich_one(item)
    except Exception as e:
        logger.debug("enrich failed for %s: %s", item.url, e)
        return item


def _enrich_one(item: FeedItem) -> FeedItem:
    # ── HN items ──────────────────────────────────────────────────────────────
    hn_id = _extract_hn_id(item.url) or _extract_hn_id(item.summary)
    if hn_id:
        return _enrich_hn(item, hn_id)

    # ── Reddit items ──────────────────────────────────────────────────────────
    if "reddit.com/r/" in item.url and "/comments/" in item.url:
        text = _fetch_reddit(item.url)
        if text:
            return _with_summary(item, text)

    # ── Generic articles (only if existing summary is thin) ───────────────────
    # 量可見文字，不量原始字串：RSS 摘要常是半截 HTML 標籤（Google News 的 <a href=…>），
    # 原始長度過門檻但沒有一個字是內容，會讓整個來源永遠不被加值。
    if _visible_len(item.summary) < _THIN_THRESHOLD and item.url.startswith("http"):
        text = _fetch_article(item.url)
        if text:
            return _with_summary(item, text)

    return item


# ── HN ────────────────────────────────────────────────────────────────────────

def _enrich_hn(item: FeedItem, hn_id: str) -> FeedItem:
    data = _hn_api(hn_id)
    if not data:
        return item

    parts: list[str] = []

    # Ask HN / Show HN / Tell HN — item has a `text` body
    if data.get("text"):
        parts.append(_strip_html(data["text"]))

    # If it's a link post, fetch the external article
    ext_url = data.get("url") or ""
    if ext_url and "ycombinator.com" not in ext_url:
        article = _fetch_article(ext_url)
        if article:
            parts.append(article)

    # Top-2 comments for discussion context — fetch in parallel
    kid_ids = [str(k) for k in (data.get("kids") or [])[:2]]
    if kid_ids:
        with ThreadPoolExecutor(max_workers=len(kid_ids)) as pool:
            for comment in pool.map(_hn_api, kid_ids):
                if comment and comment.get("text"):
                    parts.append("💬 " + _strip_html(comment["text"]))

    combined = "\n\n".join(parts)
    return _with_summary(item, combined) if combined else item


def _hn_api(item_id: str) -> dict | None:
    try:
        resp = _session.get(
            _HN_FIREBASE.format(item_id),
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logger.debug("HN Firebase API failed for %s: %s", item_id, e)
        return None


def _extract_hn_id(text: str) -> str | None:
    m = _HN_ITEM_RE.search(text or "")
    return m.group(1) if m else None


# ── Reddit ────────────────────────────────────────────────────────────────────

def _fetch_reddit(url: str) -> str:
    """Fetch post selftext via Reddit JSON API."""
    try:
        # Strip trailing slash, append .json
        json_url = url.rstrip("/") + ".json"
        resp = _session.get(
            json_url,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "ClaudeNewsBot/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
        # data[0] = post listing, data[0]["data"]["children"][0]["data"]["selftext"]
        selftext = (
            data[0]["data"]["children"][0]["data"].get("selftext", "").strip()
        )
        return selftext
    except Exception as e:
        logger.debug("Reddit JSON fetch failed for %s: %s", url, e)
        return ""


# ── Generic article ───────────────────────────────────────────────────────────

try:
    import trafilatura as _trafilatura
except ImportError:
    _trafilatura = None  # type: ignore[assignment]


def _read_capped(resp) -> str:
    """Read at most `_MAX_ARTICLE_BYTES` of the response and decode it.

    **這道上限是第一道防線，第二道是 `_extract_isolated` 的子行程隔離。** 底下的
    `trafilatura.extract()` 走 lxml（C 擴充），把幾百 MB 的 HTML 丟給它，
    輕則吃光記憶體、重則在 C 層崩潰——而 C 層的 abort **Python 的 try/except
    攔不住**，整個 process 直接帶著 SIGABRT（exit 134）死掉，`main.py` 的
    per-source 保護完全無效。2026-08-15 GitHub Actions 抓料就是這樣整個失敗，
    當日無原料、雲端 routine 的新鮮度防線正確中止、當天沒有日報。

    正常文章頁 HTML 不會超過幾百 KB；超過上限即視為非文章內容（串流、
    無限捲動、二進位誤標為 HTML），直接放棄擷取並保留原摘要。
    """
    total = 0
    chunks: list[bytes] = []
    deadline = time.monotonic() + _READ_DEADLINE_S
    for chunk in resp.iter_content(chunk_size=65536):
        if time.monotonic() > deadline:
            logger.debug("article read exceeded %ss, skipping: %s", _READ_DEADLINE_S, resp.url)
            return ""
        if not chunk:
            continue
        total += len(chunk)
        if total > _MAX_ARTICLE_BYTES:
            logger.debug("article too large (>%d bytes), skipping: %s",
                         _MAX_ARTICLE_BYTES, resp.url)
            return ""
        chunks.append(chunk)
    raw = b"".join(chunks)
    # 只用 header 宣告的編碼，不呼叫 apparent_encoding——後者會對整份內容跑
    # chardet，在這條熱路徑上既慢又可能再吃一份記憶體。
    return raw.decode(resp.encoding or "utf-8", errors="replace")


def _fetch_article(url: str) -> str:
    """Extract main article text using requests + trafilatura.

    Uses requests (with _ARTICLE_TIMEOUT) instead of trafilatura.fetch_url()
    so that we control the timeout — trafilatura.fetch_url() has its own 30s
    default that ignores REQUEST_TIMEOUT and causes slow pipeline runs.
    """
    if _trafilatura is None:
        logger.debug("trafilatura not installed, skipping article fetch")
        return ""
    try:
        # Skip domains where extraction is useless or handled separately
        domain = urlparse(url).netloc.lstrip("www.")
        if domain in _SKIP_ARTICLE_DOMAINS:
            return ""
        # Skip hard paywalls (apex domain or any subdomain)
        if any(domain == d or domain.endswith("." + d) for d in _PAYWALL_DOMAINS):
            logger.debug("paywall domain, skipping article fetch: %s", url)
            return ""
        resp = _session.get(
            url,
            timeout=_ARTICLE_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ClaudeNewsBot/1.0)"},
            allow_redirects=True,
            stream=True,
        )
        if resp.status_code != 200:
            return ""
        html = _read_capped(resp)
        if not html:
            return ""
        return _extract_isolated(html, url)
    except Exception as e:
        logger.debug("article fetch failed for %s: %s", url, e)
        return ""


def _extract_isolated(html: str, url: str = "") -> str:
    """Run `trafilatura.extract()` in a child process; a C-level crash only kills the child.

    **為什麼要隔離：** `_read_capped` 的大小上限擋得住「幾百 MB 的 HTML」，擋不住
    上限內的病態 HTML——2026-10-31 GitHub Actions 抓料就在 dedup 後 115 筆、
    trafilatura 先報 `empty HTML tree: None`、三秒後整個 process Segmentation
    fault（exit 139）死掉，當日零原料、三班雲端 routine 全部因新鮮度防線中止、
    沒有日報。lxml 是 C 擴充，SIGSEGV／SIGABRT **Python 的 try/except 攔不住**，
    `enrich()` 的 Never-raises 承諾在 C 層面前是空話。放進子行程後，崩潰只帶走那一篇，
    母行程記下 URL（WARNING，讓下次有線索）並保留原摘要繼續。

    成本：每篇一次直譯器啟動（數百 ms），只對摘要過薄才抽正文的條目發生，
    6 個 worker 並行，整批仍在 `_ENRICH_BUDGET_S` 內。
    """
    try:
        proc = subprocess.run(
            [sys.executable, "-c", _CHILD_CODE],
            input=html.encode("utf-8", errors="replace"),
            capture_output=True,
            timeout=_EXTRACT_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        logger.warning("article extraction timed out after %ss, kept original summary: %s",
                       _EXTRACT_TIMEOUT_S, url)
        return ""
    except OSError as e:
        logger.warning("article extraction child failed to start (%s), kept original summary: %s", e, url)
        return ""
    if proc.returncode != 0:
        rc = proc.returncode
        how = f"signal {signal.Signals(-rc).name}" if rc < 0 and -rc in signal.Signals._value2member_map_             else f"exit {rc & 0xFFFFFFFF:#x}" if rc < 0 or rc > 255 else f"exit {rc}"
        logger.warning("article extraction child died (%s), kept original summary: %s", how, url)
        return ""
    return proc.stdout.decode("utf-8", errors="replace").strip()


# ── helpers ───────────────────────────────────────────────────────────────────

def _with_summary(item: FeedItem, text: str) -> FeedItem:
    return replace(item, summary=text.strip()[:MAX_SUMMARY_CHARS])


def _strip_html(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()
