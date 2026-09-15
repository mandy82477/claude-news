"""GitHub Issues source — first-hand bug signals from the claude-code repo.

Fetches issues (not PRs) with recent activity, keeping only those with real
traction so the digest isn't flooded by every drive-by report:
  - comments >= 5 (heated discussion), or
  - created within the lookback window AND comments >= 2 (new hot bug)

Unauthenticated GitHub API allows 60 req/hr — one request per run is fine.
GITHUB_TOKEN from config is used when available for a higher limit.

Issues are living documents, not one-shot news: maintainers rewrite the OP to post
roadmap decisions (2026-09-09, #91870 got "Community Update: shipping in N weeks,
renamed Claude Mods" prepended to its body and a new title). Keyed by URL alone the
emitted cache drops every re-fetch unless comments double (the reignite escape hatch
models a heat surge, not a content change), so that update never reached a digest.
`dedup_key` therefore hashes what the digest shows — title + body[:200] — so an OP
rewrite is a new cache entry while a typo fix deep in the body is not. Same cure
as `official_docs_watch.py`; see `FeedItem.dedup_key`.
"""
import hashlib
import logging
from datetime import datetime, timedelta, timezone

import requests

import news_aggregator.config as _cfg
from news_aggregator.config import GITHUB_TOKEN, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

REPO = "anthropics/claude-code"
MAX_ITEMS = 15
MIN_COMMENTS_HOT = 5      # older issue, heavy recent discussion
MIN_COMMENTS_NEW = 2      # brand-new issue with early traction
SUMMARY_CHARS = 200       # what the digest shows — and therefore what the cache key hashes


def content_key(url: str, title: str | None, body: str | None) -> str:
    """Emitted-cache key: URL + hash of the part of the issue the digest displays.

    Title and body[:SUMMARY_CHARS] only. An OP rewrite or retitle changes the key
    (re-emitted as a new item); comments, reactions, and edits past the prefix do not
    (score-based reignition still applies within the same key). Whitespace is
    collapsed so a reflow of the same words is not a "change".
    """
    # Collapse whitespace *before* slicing: a reflow must not shift which words fall
    # inside the window, or a paragraph re-wrap would masquerade as an OP rewrite.
    body_norm = " ".join((body or "").split())[:SUMMARY_CHARS]
    title_norm = " ".join((title or "").split())
    digest = hashlib.sha256(f"{title_norm}\n{body_norm}".encode("utf-8")).hexdigest()[:16]
    return f"{url}#{digest}"


class GitHubIssues(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=_cfg.LOOKBACK_HOURS)
            headers = {"Accept": "application/vnd.github+json",
                       "User-Agent": "ClaudeNewsBot/1.0"}
            if GITHUB_TOKEN:
                headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

            resp = requests.get(
                f"https://api.github.com/repos/{REPO}/issues",
                params={
                    "since": cutoff.strftime("%Y-%m-%dT%H:%M:%SZ"),  # filters by updated_at
                    "sort": "comments", "direction": "desc",
                    "state": "all", "per_page": 50,
                },
                headers=headers, timeout=REQUEST_TIMEOUT,
            )
            resp.raise_for_status()

            items = []
            for issue in resp.json():
                if "pull_request" in issue:
                    continue
                comments = issue.get("comments", 0)
                created = datetime.strptime(
                    issue["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                is_new = created >= cutoff
                if not (comments >= MIN_COMMENTS_HOT or (is_new and comments >= MIN_COMMENTS_NEW)):
                    continue
                reactions = issue.get("reactions", {}).get("total_count", 0)
                url = issue.get("html_url", "")
                items.append(FeedItem(
                    title=issue.get("title", "(no title)"),
                    url=url,
                    dedup_key=content_key(url, issue.get("title"), issue.get("body")),
                    # use created time for new issues so the digest shows when the bug appeared;
                    # updated time would churn on every comment
                    published=created if is_new else datetime.strptime(
                        issue["updated_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc),
                    source=f"GitHub Issues / {REPO.split('/')[1]}",
                    score=comments,
                    score_unit="留言",
                    summary=(issue.get("body") or "")[:200]
                            + (f"（👍 {reactions} reactions）" if reactions else ""),
                    category="community",
                ))
                if len(items) >= MAX_ITEMS:
                    break
            return items
        except Exception as e:
            logger.warning("GitHubIssues.fetch failed: %s", e)
            return []
