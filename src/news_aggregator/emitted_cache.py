"""Cross-run dedup cache — prevents the same story from being emitted twice.

Tracks every item that has already made it into a digest (`gathered_items.json`
output), keyed by normalized URL. Reduces two symptoms:
  - GitHub Issues re-appearing every run while comments keep trickling in
  - Backfill / lookback overlap re-emitting the same story across days

An item is re-emitted only on a genuine "re-ignition": current score is
>= 2x the score recorded at first emit AND the absolute increase is >= 10.
That signals the story picked up meaningfully more traction, worth a
second mention. Otherwise it's filtered out.

Cache entries expire CACHE_TTL_DAYS after the item was last *seen* (offered by a
source at all, kept or dropped), not after it was first emitted. Sources that
re-fetch by activity — GitHub Issues filters on `updated_at`, so an evergreen
issue with daily comments is fetched every single run — would otherwise expire on
day 15 and come back as brand new. Measured 2026-09-25: #6235 reached 11 digests,
#34255 nine, roughly every two weeks since July.

Sources in REFETCHED_SOURCES re-offer unchanged items every run, so for them a
content key ("<url>#<hash>", see `cache_key`) with no entry of its own is matched
against a bare-URL entry for the same URL: that entry predates content hashing
(or was seeded from digest history), so no change can be inferred and the item
counts as already emitted. The 2026-09-15 switch to content keys skipped this and
re-emitted 10 old issues on 09-16 as if new. A different *hash* for the same URL
is a real change and goes through, as change detection intends.

Two-phase commit (digest_confirmed): a `--gather-only` run marks entries it
emits as digest_confirmed=False — "provisionally emitted, not yet known to
have reached a real digest". Only main()'s --confirm-digest step (run after
Step 1b actually writes news/*.md) flips them to True. Until confirmed, an
entry is treated as if it weren't in the cache at all, so it keeps being
re-offered to later runs. This exists because a `--gather-only` run can
succeed (e.g. the GH Actions cron) while the digest that was supposed to
follow it never gets built (e.g. a cloud routine that failed to fire) — the
old single-phase cache would silently blackhole those items forever, since
score_at_emit for a never-rendered item is exactly what it'll be next time,
so the reignite check (delta >= 10) can never fire.
"""
import json
import logging
from datetime import date, timedelta

from news_aggregator.config import SRC_DIR
from news_aggregator.dedup import _normalize_url
from news_aggregator.sources.base import FeedItem

logger = logging.getLogger(__name__)

CACHE_FILE = SRC_DIR / "news_aggregator" / "emitted_items.json"
CACHE_TTL_DAYS = 14
REIGNITE_MULTIPLIER = 2
REIGNITE_MIN_DELTA = 10
# Sources that re-offer an unchanged item every run. Change-detection sources
# (official_docs_watch) only emit on a real change, so they are deliberately absent.
REFETCHED_SOURCES = ("GitHub Issues",)


def cache_key(url: str, dedup_key: str = "") -> str:
    """The emitted-cache identity of an item.

    Normally the normalized URL. Change-detection sources override it with
    "<url>#<content-hash>" so that each change to a stable page is its own entry
    — see `FeedItem.dedup_key` for the failure this prevents. The override is used
    verbatim: normalizing it would strip the fragment that carries the hash.
    """
    return dedup_key or _normalize_url(url)


def load_cache() -> dict:
    try:
        if CACHE_FILE.exists():
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Could not load emitted_items cache: %s", e)
    return {}


def save_cache(cache: dict) -> None:
    try:
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception as e:
        logger.warning("Could not save emitted_items cache: %s", e)


def prune_expired(cache: dict, today: date | None = None) -> dict:
    """Drop entries not seen for CACHE_TTL_DAYS (last_seen, else first_emitted)."""
    today = today or date.today()
    cutoff = today - timedelta(days=CACHE_TTL_DAYS)
    pruned = {}
    for url, entry in cache.items():
        try:
            seen = date.fromisoformat(entry.get("last_seen") or entry["first_emitted"])
        except Exception:
            continue  # drop malformed entries
        if seen >= cutoff:
            pruned[url] = entry
    return pruned


def _bare_entry(cache: dict, key: str, source: str) -> dict | None:
    """Confirmed bare-URL entry standing in for a content key (see module docstring)."""
    if "#" not in key or not source.startswith(REFETCHED_SOURCES):
        return None
    entry = cache.get(key.split("#", 1)[0])
    return entry if entry and entry.get("digest_confirmed", False) else None


def _reignited(score: int, entry: dict) -> bool:
    prev = entry.get("score_at_emit")
    if prev is None:  # seeded from digest history: shown before, score unknown
        return False
    return score >= prev * REIGNITE_MULTIPLIER and score - prev >= REIGNITE_MIN_DELTA


def filter_new_or_reignited(
    items: list[FeedItem], cache: dict, today: date | None = None
) -> tuple[list[FeedItem], dict]:
    """Return (items to keep, updated cache — not yet saved).

    - Item not in cache, or in cache but not yet digest_confirmed -> kept,
      (re-)added to cache with digest_confirmed=False. An unconfirmed entry
      means an earlier --gather-only run offered this item but no digest
      was ever confirmed built from it, so it's treated as if never emitted.
    - Item in cache and digest_confirmed, current score < reignite threshold
      -> dropped.
    - Item in cache and digest_confirmed, current score >= 2x recorded score
      and delta >= 10 -> kept (reignited), cache entry updated and reset to
      digest_confirmed=False pending the next confirm-digest call.
    - Content-keyed item from REFETCHED_SOURCES with no entry of its own but a
      confirmed bare-URL entry -> judged against that entry (module docstring).
    Every item seen refreshes last_seen on its entry, kept or dropped.
    """
    today = today or date.today()
    today_str = today.isoformat()
    updated_cache = dict(cache)
    kept: list[FeedItem] = []

    def emit(key: str, item: FeedItem, existing: dict | None) -> None:
        kept.append(item)
        updated_cache[key] = {
            **(existing or {}),
            "first_emitted": (existing or {}).get("first_emitted", today_str),
            "last_emitted": today_str,
            "last_seen": today_str,
            "score_at_emit": item.score,
            "digest_confirmed": False,
        }

    for item in items:
        norm = cache_key(item.url, getattr(item, "dedup_key", ""))
        existing = updated_cache.get(norm)

        if existing is not None and existing.get("digest_confirmed", False):
            if _reignited(item.score, existing):
                emit(norm, item, existing)
            else:
                seen = {**existing, "last_seen": today_str}
                if seen.get("score_at_emit") is None:
                    seen["score_at_emit"] = item.score
                updated_cache[norm] = seen
            continue

        bare = _bare_entry(updated_cache, norm, item.source) if existing is None else None
        if bare is None:
            emit(norm, item, existing)
            continue

        updated_cache[norm.split("#", 1)[0]] = {**bare, "last_seen": today_str}
        if _reignited(item.score, bare):
            emit(norm, item, bare)
        else:
            # Adopt the content key as the same, already-emitted item.
            updated_cache[norm] = {
                "first_emitted": bare["first_emitted"],
                "last_emitted": bare.get("last_emitted") or bare["first_emitted"],
                "last_seen": today_str,
                "score_at_emit": item.score if bare.get("score_at_emit") is None else bare["score_at_emit"],
                "digest_confirmed": True,
            }

    return kept, updated_cache


def confirm_digest(cache: dict, urls: list, today: date | None = None) -> dict:
    """Mark the given items as digest_confirmed=True — call this only after a
    real digest (news/*.md) has actually been written from these items.

    Each entry is either a plain URL string, or a mapping with "url" and an
    optional "dedup_key" (as persisted in gathered_items.json). The mapping form
    matters for change-detection sources: confirming them under the bare URL
    while `filter_new_or_reignited` stored them under "<url>#<hash>" would leave
    the real entry unconfirmed forever and re-offer it every run.

    Unknown entries (not already in cache, e.g. because filtering happened in a
    process that never called save_cache) are added fresh and confirmed.
    """
    today = today or date.today()
    today_str = today.isoformat()
    updated_cache = dict(cache)

    for entry in urls:
        if isinstance(entry, dict):
            norm = cache_key(entry.get("url", ""), entry.get("dedup_key", ""))
        else:
            norm = cache_key(entry)
        existing = updated_cache.get(norm, {})
        updated_cache[norm] = {
            **existing,
            "first_emitted": existing.get("first_emitted", today_str),
            "last_seen": existing.get("last_seen", today_str),
            "score_at_emit": existing.get("score_at_emit", 0),
            "digest_confirmed": True,
        }

    return updated_cache
