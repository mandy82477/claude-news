"""
PreToolUse hook 共用：判斷這次工具呼叫是誰發的（不是 hook，本身不掛 settings）。

角色：
    main      主 session（payload 無 `agent_id`）
    reporter  記者子 agent：派工 prompt 含 `.claude/agents/wiki-reporter-`（六記者、
              devpractice、market、分類複核的派工模板都有這句，見 wiki-ingest/references/dispatch.md）
    pipeline  /news-pipeline 的 Phase A／C 背景 agent：prompt 以「你是 Claude News Pipeline Agent」開頭
              （news-pipeline/references/dispatch.md）——它們照規則會 commit、push、還原 replay 檔
    subagent  其他子 agent

證據（2026-10-03 實測）：子 agent 內的 PreToolUse 輸入多 `agent_id`／`agent_type` 兩欄，主 session
沒有；子 agent 的派工 prompt 是 `<transcript_path 去副檔名>/subagents/agent-<agent_id>.jsonl`
第一行的 message.content。這個檔案配置不是官方契約：找不到或讀不了時一律回 `subagent`
——對子 agent 寧可嚴（最壞情況是 pipeline 備用 agent 被擋，它會回報、主 session 接手）。

另：`is_cloud()` 看 `CLAUDE_CODE_REMOTE`。官方文件沒寫這個變數（2026-10-03 查）；證據是
雲端 routine 探針實測 `REMOTE=true`（docs/cloud-runbooks/probe-workflow-tool-2026-09-13.md）。
"""
from __future__ import annotations

import json
import os
from pathlib import Path

REPORTER_MARK = ".claude/agents/wiki-reporter-"
PIPELINE_MARK = "你是 Claude News Pipeline Agent"


def _first_prompt(payload: dict) -> str | None:
    tp = payload.get("transcript_path")
    aid = payload.get("agent_id")
    if not tp or not aid:
        return None
    try:
        base = Path(tp)
        cand = base.with_suffix("") / "subagents" / f"agent-{aid}.jsonl"
        if not cand.is_file():
            return None
        with open(cand, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                msg = rec.get("message") or {}
                if msg.get("role") != "user":
                    continue
                content = msg.get("content")
                if isinstance(content, list):
                    content = "\n".join(
                        c.get("text", "") for c in content if isinstance(c, dict)
                    )
                return content if isinstance(content, str) else None
    except (OSError, ValueError):
        return None
    return None


def role_from_prompt(prompt: str | None, agent_type: str = "") -> str:
    if agent_type.startswith("wiki-reporter-"):
        return "reporter"
    if not prompt:
        return "subagent"
    if REPORTER_MARK in prompt:
        return "reporter"
    if prompt.lstrip().startswith(PIPELINE_MARK):
        return "pipeline"
    return "subagent"


def role(payload: dict) -> str:
    if not payload.get("agent_id"):
        return "main"
    return role_from_prompt(_first_prompt(payload), str(payload.get("agent_type") or ""))


def in_shared_tree(payload: dict) -> bool:
    """cwd 是否為專案根（共用工作樹）。`isolation: worktree` 的子 agent cwd 在別處。"""
    root = os.environ.get("CLAUDE_PROJECT_DIR")
    cwd = payload.get("cwd")
    if not root or not cwd:
        return True
    try:
        return Path(cwd).resolve() == Path(root).resolve()
    except (OSError, ValueError):
        return True


def is_cloud() -> bool:
    return os.environ.get("CLAUDE_CODE_REMOTE", "").lower() == "true"


def rel_to_project(path: str, cwd: str | None = None) -> str | None:
    """工具輸入的檔案路徑 → 專案相對、正斜線；專案外回 None。"""
    root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd
    if not root or not path:
        return None
    try:
        p = Path(path)
        if not p.is_absolute():
            p = Path(cwd or root) / p
        return p.resolve().relative_to(Path(root).resolve()).as_posix()
    except (OSError, ValueError):
        return None
