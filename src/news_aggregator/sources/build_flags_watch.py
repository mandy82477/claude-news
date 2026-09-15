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

Failure policy (unattended in GitHub Actions): "same version, nothing to do" returns
[]. Everything else — registry down, truncated tarball, corrupt state file, a diff
that does not look like one version's worth — **raises**, so `main.py` records
`ok=false` for this source and the weekly source-health check can see it. Swallowing
errors here would make "npm renamed the package three months ago" look exactly like
"no new version today" (review 2026-09-16, P1-4).

First run (no state file) records a baseline and emits nothing: 600+ flags dumped
into one digest would be noise, not news. A state file that exists but cannot be
parsed is *not* a first run — it raises and leaves the file alone (P1-3).

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
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from news_aggregator.config import REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

PACKAGE = "@anthropic-ai/claude-code-linux-x64"
REGISTRY_URL = f"https://registry.npmjs.org/{PACKAGE}/latest"
PACKAGE_PAGE = f"https://www.npmjs.com/package/{PACKAGE}/v/"
READ_TIMEOUT = 120          # per socket read (requests' timeout is not a total budget)
DOWNLOAD_DEADLINE = 600     # total wall-clock budget for one tarball, seconds
STATE_PATH = Path(__file__).parent / "build_flags_state.json"
LEDGER_PATH = Path(__file__).resolve().parents[3] / "data" / "build_flags_history.jsonl"

FLAG_RE = re.compile(rb"CLAUDE_CODE_[A-Z0-9_]{3,}")
MIN_FLAGS = 50        # a real build has hundreds; fewer means we grabbed the wrong file
MAX_ADDED = 200       # more than this in one step is a bad baseline, not a release
MAX_GLUE = 3          # a name that is another name + ≤3 chars is byte glue, not a flag
# Plumbing: knobs nobody would call a feature. Matched on whole `_`-separated tokens
# of the part after CLAUDE_CODE_, never on substrings — `TEAMS` is not `MS`, `IDLE`
# is not `ID`, `TRANSCRIPT` is not `SCRIPT` (review 2026-09-16, P1-2).
PLUMBING_LAST_TOKEN = {
    "MS", "TIMEOUT", "SECONDS", "MINUTES", "ID", "FD", "TOKEN", "VERSION", "PORT",
    "URL", "PATH", "DIR", "SCRIPT", "FILE", "PID", "SOCKET", "ENV", "UUID",
}
PLUMBING_ANY_TOKEN = {"TIMEOUT"}
PLUMBING_PREFIX = ("INSTALLED_VIA_", "SPAWNED_BY_")
MAX_LISTED = 40  # keep the digest line readable; the ledger has the full diff


def extract_flags(data: bytes) -> set[str]:
    return clean_flags({m.group(0).decode("ascii") for m in FLAG_RE.finditer(data)})


def clean_flags(raw: set[str]) -> set[str]:
    """Drop byte glue. The regex is greedy, so `..._MINUTES` followed by the byte `0`
    comes out as `..._MINUTES0`; `..._SESSION_` is a prefix cut mid-name. Rule: a name
    ending in `_` is not a flag; a name that equals another name + 1..MAX_GLUE chars,
    where the extra part does not start with `_`, is glue (the shorter real name
    survives). `POST_TURN_MEMORY` vs `POST_TURN_MEMORY_SYNC` is kept — the suffix starts
    with `_`, which is how real sub-flags are spelled. (review 2026-09-16, P1-1)
    """
    names = {f for f in raw if not f.endswith("_")}
    glued = set()
    for f in names:
        for cut in range(1, MAX_GLUE + 1):
            base, extra = f[:-cut], f[-cut:]
            if base in names and not extra.startswith("_") and not base.endswith("_"):
                glued.add(f)
                break
    return names - glued


def is_plumbing(flag: str) -> bool:
    tail = flag[len("CLAUDE_CODE_"):]
    if not tail:
        return True
    if tail.startswith(PLUMBING_PREFIX):
        return True
    tokens = tail.split("_")
    if tokens[-1] in PLUMBING_LAST_TOKEN:
        return True
    return any(t in PLUMBING_ANY_TOKEN for t in tokens)


def classify(added: set[str]) -> tuple[list[str], list[str]]:
    """(candidates, plumbing), both sorted."""
    cands = sorted(f for f in added if not is_plumbing(f))
    plumb = sorted(f for f in added if is_plumbing(f))
    return cands, plumb


def _listed(names: list[str]) -> str:
    shown = "、".join(f"`{n}`" for n in names[:MAX_LISTED])
    return shown + (f"（只列前 {MAX_LISTED} 個）" if len(names) > MAX_LISTED else "")


def build_item(prev_version: str, version: str, added: set[str], removed: set[str],
               now: datetime | None = None) -> FeedItem | None:
    """One digest item per new version, or None when nothing worth a line changed."""
    cands, plumb = classify(added)
    gone = sorted(removed)
    if not cands and not gone:
        return None
    parts = []
    if cands:
        parts.append(f"功能候選 {len(cands)} 個：{_listed(cands)}")
    if plumb:
        parts.append(f"另有 {len(plumb)} 個設定類旗標（逾時、識別碼等）未列")
    if gone:
        parts.append(f"消失 {len(gone)} 個：{_listed(gone)}")
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


class StateError(RuntimeError):
    """State file exists but is unusable — never treat as a first run."""


def _load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise StateError(f"state file unreadable ({e}); refusing to treat as first run") from e
    if not isinstance(state, dict) or not isinstance(state.get("flags"), list) or not state.get("version"):
        raise StateError("state file has no version/flags; refusing to treat as first run")
    if len(state["flags"]) < MIN_FLAGS:
        raise StateError(f"state has only {len(state['flags'])} flags; a diff against it would list a whole build")
    return state


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


def _download_flags(tarball_url: str, deadline: float = DOWNLOAD_DEADLINE) -> set[str]:
    start = time.monotonic()
    with tempfile.TemporaryDirectory() as td:
        tgz = Path(td) / "pkg.tgz"
        with requests.get(tarball_url, stream=True, timeout=READ_TIMEOUT,
                          headers={"User-Agent": "ClaudeNewsBot/1.0"}) as resp:
            resp.raise_for_status()
            with tgz.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=1 << 20):
                    if time.monotonic() - start > deadline:
                        raise TimeoutError(f"tarball download exceeded {deadline}s total budget")
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
        state = _load_state()                      # raises on a corrupt file
        version, tarball = _latest()               # raises on registry failure
        if state.get("version") == version:
            return []
        flags = _download_flags(tarball)           # raises on network/tar failure
        if len(flags) < MIN_FLAGS:
            raise ValueError(f"only {len(flags)} flags found in {version}; wrong file, refusing to baseline")
        today = datetime.now(tz=timezone.utc).date().isoformat()
        new_state = {"version": version, "checked": today, "flags": sorted(flags)}
        if not state:
            _save_state(new_state)
            logger.info("BuildFlagsWatch: baseline %s recorded (%d flags), nothing emitted",
                        version, len(flags))
            return []
        prev, prev_flags = state["version"], set(state["flags"])
        added, removed = flags - prev_flags, prev_flags - flags
        if len(added) > MAX_ADDED:
            raise ValueError(f"{len(added)} new flags between {prev} and {version} does not look like a release diff")
        cands, plumb = classify(added)
        _append_ledger({"date": today, "from": prev, "to": version,
                        "added": sorted(added), "removed": sorted(removed),
                        "candidates": cands, "plumbing": plumb})
        _save_state(new_state)
        item = build_item(prev, version, added, removed)
        return [item] if item else []
