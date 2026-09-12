"""Blogroll RSS source — authoritative independent blogs curated in blogroll.json.

Unlike the aggregator sources (HN/Reddit/GitHub), a personal blog's RSS feed is
mostly off-topic (the author writes about many things, not just Claude/Anthropic).
We therefore apply a keyword pre-filter on top of the normal LOOKBACK_HOURS window
so an author's unrelated posts don't flood the daily digest.

The blog list itself starts empty — curation happens out-of-band via
/source-review + user confirmation, which edits blogroll.json directly. This
module ships the mechanism; it works correctly (returns []) with an empty or
absent list.

Vendor feeds (2026-09-12): a blog entry may carry ``"topic": "<wiki slug>"``.
Such feeds are official blogs/changelogs of other AI vendors fetched *for a
specific wiki page* (competitor-landscape); their posts never mention Claude,
so the keyword pre-filter is skipped and every recent post is emitted with
``topic`` set -- exactly like sources/topic_watch.py. The digest step then
judges each one on "does this release change anything for a Claude user" and
drops the rest (see news-pipeline-steps.md 專頁雷達). ``max_items`` (default
``TOPIC_MAX_ITEMS``) caps how many such posts one feed may emit per run, so a
busy vendor newsroom cannot dilute the radar.
"""
import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests

import news_aggregator.config as _cfg
from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem, parse_feed_time

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent / "blogroll.json"

# Keyword pre-filter: a personal blog's feed is mostly off-topic, so only posts
# whose title/summary mention Claude/Anthropic (or the broader LLM-agent space
# this project also tracks per CLAUDE.md 蒐集範圍) are admitted. Lowercase,
# matched case-insensitively against "title summary".
KEYWORDS = [
    "claude",
    "anthropic",
    "mcp",
    "claude code",
    "llm",
    "ai agent",
]

# Per-run cap for a topic-mode (vendor) feed; overridable per blog via "max_items".
TOPIC_MAX_ITEMS = 3


class Blogroll(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            blogs = _load_blogs()
        except Exception as e:
            logger.warning("Blogroll config load failed: %s", e)
            return []

        if not blogs:
            return []

        lookback = _cfg.LOOKBACK_HOURS
        cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=lookback)

        items: list[FeedItem] = []
        for blog in blogs:
            if blog.get("status") == "retired":
                continue
            try:
                items.extend(_fetch_blog(blog, cutoff))
            except Exception as e:
                logger.warning(
                    "Blogroll blog '%s' failed: %s", blog.get("slug", "?"), e
                )

        return items


def _load_blogs() -> list[dict]:
    if not CONFIG_PATH.exists():
        logger.warning("Blogroll config not found: %s", CONFIG_PATH)
        return []
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Blogroll config is invalid JSON (%s): %s", CONFIG_PATH, e)
        return []
    return data.get("blogs", []) or []


def _matches_keywords(title: str, summary: str) -> bool:
    haystack = f"{title} {summary}".lower()
    return any(kw in haystack for kw in KEYWORDS)


def _fetch_blog(blog: dict, cutoff: datetime) -> list[FeedItem]:
    name = blog.get("name") or blog.get("slug") or "(未命名部落格)"
    rss_url = blog.get("rss_url")
    if not rss_url:
        logger.warning("Blogroll blog '%s' missing rss_url", name)
        return []

    resp = requests.get(
        rss_url,
        headers={"User-Agent": "ClaudeNewsBot/1.0"},
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    feed = feedparser.parse(resp.content)
    if feed.bozo and not feed.entries:
        raise ValueError(f"bozo feed: {feed.bozo_exception}")

    topic = (blog.get("topic") or "").strip()
    max_items = int(blog.get("max_items") or TOPIC_MAX_ITEMS) if topic else None

    items: list[FeedItem] = []
    for entry in feed.entries:
        pub = parse_feed_time(entry)
        if pub and pub < cutoff:
            continue

        title = entry.get("title", "(no title)")
        summary = entry.get("summary", "") or ""
        # Vendor feeds carry a topic: skip the keyword gate (their posts never
        # mention Claude) and let the digest step judge impact instead.
        if not topic and not _matches_keywords(title, summary):
            continue

        items.append(FeedItem(
            title=title,
            url=entry.get("link", ""),
            source=f"Blog / {name}",
            published=pub or datetime.now(tz=timezone.utc),
            score=0,
            score_unit="",
            summary=summary[:200],
            category="media" if topic else "community",
            topic=topic,
        ))
        if max_items is not None and len(items) >= max_items:
            break

    return items
