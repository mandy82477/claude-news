"""Build Flags — feature flags that appear in the shipped Claude Code binary before
anyone announces them.

Why this source exists: `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` was in the 2.1.261 build on
2026-09-04. The maintainer's public commitment ("shipping in N weeks, renamed Claude
Mods") landed in the GitHub issue on 09-09, and as of 2.1.272 (09-14) the CHANGELOG
still says nothing. The binary is the earliest place an experimental feature shows up;
changelog and docs are, by definition, late for anything experimental.

What it watches: the npm package `@anthropic-ai/claude-code-linux-x64` (the real
binary — `@anthropic-ai/claude-code` is a 27 KB wrapper). One version per day is
normal. On a new version it downloads the tarball (~100 MB, once), pulls every
`CLAUDE_CODE_*` string out of the binary, and diffs against the last recorded set.

What it emits: **at most one item per new version**, listing the flags that look like
features. Plumbing (timeouts, fds, session ids) is counted but not listed. The rest is
noise-prone on purpose — a flag in a binary is not a promise — so the digest gets one
line and the judgement lives on `wiki/topics/claude-code-experimental.md`, where a
flag climbs from "seen in build" only when there is evidence (issue, docs, changelog,
community mentions). See `.claude/reporter-rules/features/pages.md`.

First run (no state) records a baseline and emits nothing: 600+ flags dumped into one
digest would be noise, not news.

State: `build_flags_state.json` next to this file (committed by daily-gather like the
other watch states). Ledger: `data/build_flags_history.jsonl`, one line per version
diff, consumed by the wiki page and `scripts/build_flags_mentions.py`.
"""
from __future__ import annotations

import json
import logging
import re
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import requests

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

PACKAGE = "@anthropic-ai/claude-code-linux-x64"
REGISTRY_URL = f"https://registry.npmjs.org/{PACKAGE}/latest"
PACKAGE_PAGE = f"https://www.npmjs.com/package/{PACKAGE}/v/"
DOWNLOAD_TIMEOUT = 300  # ~100 MB; REQUEST_TIMEOUT is sized for HTML pages
STATE_PATH = Path(__file__).parent / "build_flags_state.json"
LEDGER_PATH = Path(__file__).resolve().parents[3] / "data" / "build_flags_history.jsonl"

FLAG_RE = re.compile(rb"CLAUDE_CODE_[A-Z0-9_]{3,}")
# Plumbing: knobs nobody would call a feature. Suffix/fragment match on the part
# after CLAUDE_CODE_. Everything else is a *candidate* — the reporter decides.
PLUMBING = (
    "_MS", "_TIMEOUT", "_SECONDS", "_MINUTES", "_ID", "_FD", "_TOKEN", "_VERSION",
    "_PORT", "_URL", "_PATH", "_DIR", "_SCRIPT", "_FILE", "INSTALLED_VIA", "SPAWNED_BY",
    "_PID", "_SOCKET", "_HOST_", "_ENV",
)
MAX_LISTED = 40  # keep the digest line readable; the ledger has the full diff


def extract_flags(data: bytes) -> set[str]:
    return {m.group(0).decode("ascii") for m in FLAG_RE.finditer(data)}


def is_plumbing(flag: str) -> bool:
    tail = flag[len("CLAUDE_CODE_"):]
    return any(p in tail or tail.endswith(p.strip("_")) for p in PLUMBING) if tail else True


def classify(added: set[str]) -> tuple[list[str], list[str]]:
    """(candidates, plumbing), both sorted."""
    cands = sorted(f for f in added if not is_plumbing(f))
    plumb = sorted(f for f in added if is_plumbing(f))
    return cands, plumb


def build_item(prev_version: str, version: str, added: set[str], removed: set[str],
               now: datetime | None = None) -> FeedItem | None:
    """One digest item per new version, or None when nothing worth a line changed."""
    cands, plumb = classify(added)
    gone = sorted(removed)
    if not cands and not gone:
        return None
    parts = []
    if cands:
        shown = "、".join(f"`{c}`" for c in cands[:MAX_LISTED])
        more = f" 等 {len(cands)} 個" if len(cands) > MAX_LISTED else ""
        parts.append(f"功能候選 {len(cands)} 個：{shown}{more}")
    if plumb:
        parts.append(f"另有 {len(plumb)} 個設定類旗標（逾時、識別碼等）未列")
    if gone:
        parts.append("消失：" + "、".join(f"`{g}`" for g in gone[:MAX_LISTED]))
    parts.append("build 裡出現的旗標不等於會上線；官方態度與社群反應見 wiki 的 Claude Code 實驗功能頁")
    url = f"{PACKAGE_PAGE}{version}"
    return FeedItem(
        title=f"Claude Code {version} build 新增 {len(cands)} 個功能候選旗標（自 {prev_version} 起）",
        url=url,
        dedup_key=f"{url}#{version}",
        source="Build Flags",
        published=now or datetime.now(tz=timezone.utc),
        score=0,
        summary="；".join(parts),
        category="official",
        score_unit="",
    )


def _load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _append_ledger(entry: dict) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER_PATH.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _latest() -> tuple[str, str]:
    resp = requests.get(REGISTRY_URL, timeout=REQUEST_TIMEOUT,
                        headers={"User-Agent": "ClaudeNewsBot/1.0"})
    resp.raise_for_status()
    meta = resp.json()
    return meta["version"], meta["dist"]["tarball"]


def _download_flags(tarball_url: str) -> set[str]:
    with tempfile.TemporaryDirectory() as td:
        tgz = Path(td) / "pkg.tgz"
        with requests.get(tarball_url, stream=True, timeout=DOWNLOAD_TIMEOUT,
                          headers={"User-Agent": "ClaudeNewsBot/1.0"}) as resp:
            resp.raise_for_status()
            with tgz.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=1 << 20):
                    if chunk:
                        f.write(chunk)
        with tarfile.open(tgz) as t:
            files = [m for m in t.getmembers() if m.isfile()]
            if not files:
                raise ValueError("tarball has no files")
            binary = max(files, key=lambda m: m.size)
            data = t.extractfile(binary).read()
    return extract_flags(data)


class BuildFlagsWatch(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            version, tarball = _latest()
            state = _load_state()
            if state.get("version") == version:
                return []
            flags = _download_flags(tarball)
            if len(flags) < 50:  # a real build has hundreds; fewer means we grabbed the wrong file
                raise ValueError(f"only {len(flags)} flags found in {version}, refusing to baseline")
            today = datetime.now(tz=timezone.utc).date().isoformat()
            prev = state.get("version")
            prev_flags = set(state.get("flags", []))
            new_state = {"version": version, "checked": today, "flags": sorted(flags)}
            if not prev:
                _save_state(new_state)
                logger.info("BuildFlagsWatch: baseline %s recorded (%d flags), nothing emitted",
                            version, len(flags))
                return []
            added, removed = flags - prev_flags, prev_flags - flags
            cands, plumb = classify(added)
            _append_ledger({"date": today, "from": prev, "to": version,
                            "added": sorted(added), "removed": sorted(removed),
                            "candidates": cands, "plumbing": plumb})
            _save_state(new_state)
            item = build_item(prev, version, added, removed)
            return [item] if item else []
        except Exception as e:  # noqa: BLE001 — one flaky download must not sink the gather
            logger.warning("BuildFlagsWatch.fetch failed: %s", e)
            return []
