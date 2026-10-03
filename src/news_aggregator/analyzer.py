"""Keyless digest body (no LLM).

History: this module used to call the Anthropic API (claude-haiku) when
ANTHROPIC_API_KEY was set and fall back to a plain list otherwise. The project
never has a key (CLAUDE.md「環境限制」), so the API path never executed; it was
removed on 2026-10-03 by user decision, same as filter.py's LLM scorer on
2026-07-03. The editorial digest is written downstream by the Claude session
(news-digest, Step 1b); this module only produces the plain-list body that the
gather step needs.
"""
from news_aggregator.sources.base import FeedItem


def analyze(items: list[FeedItem]) -> tuple[str, str]:
    """Return (body, method). method starts with "fallback" — digest.py keys on that."""
    if not items:
        return "## 今日無新增資訊\n\n> 所有來源在過去 26 小時內未發現相關新內容。\n", "—"
    return _fallback_body(items), "fallback (純文字列表)"


def _fallback_body(items: list[FeedItem]) -> str:
    lines = []
    for item in items:
        pub_str = item.published.strftime("%m/%d %H:%M UTC")
        score_str = f" — {item.score} {item.score_unit or '分'}" if item.score > 0 else ""
        source_note = f" ✦ 跨 {item.source_count} 來源" if item.source_count > 1 else ""
        lines.append(f"- **[{item.title}]({item.url})**{score_str}{source_note}")
        lines.append(f"  *{item.source} · {pub_str}*")
        if item.summary:
            excerpt = item.summary[:150].replace("\n", " ").strip()
            if excerpt:
                lines.append(f"  > {excerpt}")
        lines.append("")
    return "\n".join(lines)
