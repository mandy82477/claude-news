"""
PreToolUse hook: 依「誰在呼叫」擋越權動作（H5 news/ 唯讀、H6 閘與基線、H7 不可再委派、H8 派工參數）。

身分判定見 `_identity.py`（main／reporter／pipeline／subagent；雲端另看 CLAUDE_CODE_REMOTE）。

H5 `news/` 唯讀——對象是**子 agent**（pipeline 除外）
    日報由主 session（news-digest）或 pipeline Phase A 用 Write 寫成；爬蟲是 Python 程序寫檔，
    不經工具、本 hook 看不到也不擋。記者與其他子 agent 讀日報、不寫日報
    （wiki/CLAUDE.md、.claude/reporter-rules/shared.md「邊界限制」）。
    主 session 修日報錯字（例：fccb4818、bdaf366b）照常放行。
H6 閘腳本、存量基線、白名單、known-test-gaps——對象是**子 agent 與雲端 session**
    web-publish「修復迴圈」硬性禁止：放行靠改閘＝把閘拆掉。2026-09-25 有 agent 跑全庫
    `check_cell_limits.py --rebuild`，把其他並行 agent 的新超限一起吸進基線（wiki/log.md）。
    本機主 session 開發時合法會改這些檔，hook 分不出「開發」與「修閘紅」，所以只擋
    一定不是開發的兩種身分。棘輪測試 test_baseline_ratchet.py 是另一道（只守基線變鬆）。
H7 不可再委派——子 agent 呼叫 Agent／Task 一律擋（shared.md「不可再委派」、
    page-audit-review「所有 agent：不可再委派」、pipeline 派工 prompt「也不呼叫 Agent tool」）。
    記者另擋 WebFetch／WebSearch：各類 reporter-rules 都寫「記者無 web 工具」，需要官方查證的
    標「⚠️ 需主編查證」交主編。主編層的 web 查證（/wiki-lint 5e、5h）由主 session 做，不受影響。
H8 派工參數——主 session 派記者時必須明寫 `model` 與 `run_in_background: false`；
    派 pipeline agent 必須明寫 `model`（wiki-ingest SKILL 步驟 3：未指定會繼承主 session
    模型，六記者並行足以打穿配額；背景記者的完成通知回不來）。
    2026-10-03 起 Agent 工具「未指定 run_in_background 預設背景」，所以只「沒寫 true」不夠，要明寫 false。

解析錯誤一律放行（fail-open）。
"""
import fnmatch
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmdparse import basename, iter_commands, split_segments  # noqa: E402
from _identity import (  # noqa: E402
    PIPELINE_MARK, REPORTER_MARK, in_shared_tree, is_cloud, rel_to_project, role,
)

try:
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

WRITE_TOOLS = {"Edit", "Write", "NotebookEdit", "MultiEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}
AGENT_TOOLS = {"Agent", "Task"}
WEB_TOOLS = {"WebFetch", "WebSearch"}

GATE_FILES = (
    "scripts/check_*.py", "scripts/run_tests.py", "scripts/gate_web_build.py",
    "scripts/ingest_gate.py", "data/*baseline*.json", "data/*-allow.json",
    "data/baseline-changes.jsonl", "docs/known-test-gaps.json",
)
BASELINE_FLAGS = ("--rebuild", "--allow-grow", "--write-baseline")

WHY_H6 = (
    "修閘紅時不可改閘腳本、基線、白名單或 known-test-gaps，也不可跑 --rebuild／--allow-grow／"
    "--write-baseline——靠改閘放行等於把閘拆掉，基線只准人工變緊。只能修失敗訊息指名的內容本身；"
    "修不了就照舊擋下並回報。規則：.claude/skills/web-publish/SKILL.md「硬性禁止」。"
)
WHY_H5 = (
    "news/ 是唯讀原料：記者與其他子 agent 只讀日報、不寫日報。日報有錯，在回報裡寫明交主 session 處理。"
    "規則：wiki/CLAUDE.md、.claude/reporter-rules/shared.md「邊界限制」。"
)


WHY_WEB = (
    "記者無 web 工具：需要官方查證的事實，在回報寫「⚠️ 需主編查證：[議題＋建議查證頁]」交主編，"
    "不得自行上網補。規則：.claude/reporter-rules/commercial/daily.md 等各類 daily.md「無 web 工具」。"
)


def _is_gate_file(rel: str) -> bool:
    return any(fnmatch.fnmatchcase(rel, pat) for pat in GATE_FILES)


def _restricted_for_gates(who: str) -> bool:
    return who != "main" or is_cloud()


def check_write(path_rel: str | None, who: str) -> str | None:
    if not path_rel:
        return None
    if who in ("reporter", "subagent") and (path_rel == "news" or path_rel.startswith("news/")):
        return WHY_H5
    if _restricted_for_gates(who) and _is_gate_file(path_rel):
        return WHY_H6
    return None


def _shell_targets(command: str):
    """shell 指令會寫到的路徑（盡力而為）：重導向 `>`/`>>`、tee、sed -i、cp/mv 目的地、Set-Content 等。"""
    for seg in split_segments(command):
        s = seg.replace(">>", " > ")
        parts = s.split(">")
        for tail in parts[1:]:
            toks = tail.strip().split()
            if toks:
                yield toks[0].strip("'\"")
    for toks in iter_commands(command):
        prog = basename(toks[0])
        args = [t for t in toks[1:] if not t.startswith("-")]
        if prog in ("tee", "sed", "perl") and args:
            if prog == "tee" or any(t.startswith("-i") for t in toks[1:]):
                yield from args[-1:] if prog != "tee" else args
        elif prog in ("cp", "mv", "copy", "move", "copy-item", "move-item") and len(args) >= 2:
            yield args[-1]
        elif prog in ("set-content", "add-content", "out-file", "new-item", "remove-item", "rm", "del"):
            yield from args


def check_shell(command: str, who: str, cwd: str | None) -> str | None:
    if _restricted_for_gates(who):
        for toks in iter_commands(command):
            if any(t in BASELINE_FLAGS or t.split("=", 1)[0] in BASELINE_FLAGS for t in toks[1:]):
                return WHY_H6
    if who in ("reporter", "subagent") or _restricted_for_gates(who):
        for target in _shell_targets(command):
            why = check_write(rel_to_project(target, cwd), who)
            if why:
                return why
    return None


def _log_agent_payload(tool_input: dict) -> None:
    """暫時的證據收集：記下記者派工時 hook 實際收到的欄位（不含 prompt 全文）。"""
    try:
        import tempfile
        rec = {k: (v if k != "prompt" else str(v)[:40]) for k, v in tool_input.items()}
        with open(os.path.join(tempfile.gettempdir(), "claude-news-agent-payloads.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def check_agent(tool_input: dict, who: str) -> str | None:
    if who != "main":
        return (
            "子 agent 不可再委派（呼叫 Agent tool）：完成通知會迷路、品質無人驗收。所有工作親自完成，"
            "做不完就在回報說明交主 session。規則：.claude/reporter-rules/shared.md「不可再委派」。"
        )
    prompt = str(tool_input.get("prompt") or "")
    stype = str(tool_input.get("subagent_type") or "")
    is_reporter = REPORTER_MARK in prompt or stype.startswith("wiki-reporter-")
    is_pipeline = prompt.lstrip().startswith(PIPELINE_MARK)
    if (is_reporter or is_pipeline) and not tool_input.get("model"):
        return (
            "派工未指定 model：會繼承主 session 模型，六記者並行足以打穿訂閱配額。記者與 pipeline agent 一律明寫 "
            "`model: \"sonnet\"`。規則：.claude/skills/wiki-ingest/SKILL.md 步驟 3。"
        )
    if is_reporter:
        _log_agent_payload(tool_input)
    # 只擋「明確設成 true」。2026-10-03 事故：2.1.288 的派工明寫 false，hook 卻沒收到 False，
    # 「is not False」把 pipeline 的七位記者全擋掉；欄位缺席時放行（fail-open），查證中。
    if is_reporter and tool_input.get("run_in_background") is True:
        return (
            "記者必須 foreground 派工：明寫 `run_in_background: false`（Agent 工具未指定時預設背景）。"
            "背景記者的完成通知回不到派工 agent，會永久等待。規則：.claude/skills/wiki-ingest/SKILL.md 步驟 3。"
        )
    return None


def decide(payload: dict) -> str | None:
    tool = payload.get("tool_name")
    ti = payload.get("tool_input") or {}
    if tool not in WRITE_TOOLS | SHELL_TOOLS | AGENT_TOOLS | WEB_TOOLS:
        return None
    who = role(payload)
    if tool in WEB_TOOLS:
        return WHY_WEB if who == "reporter" else None
    if who in ("reporter", "subagent") and not in_shared_tree(payload) and tool in WRITE_TOOLS:
        # worktree 隔離的子 agent：不碰共用樹的 news/，只受 H6（它不是開發身分）
        rel = rel_to_project(ti.get("file_path") or ti.get("notebook_path") or "", payload.get("cwd"))
        return WHY_H6 if rel and _is_gate_file(rel) else None
    if tool in WRITE_TOOLS:
        path = ti.get("file_path") or ti.get("notebook_path") or ""
        return check_write(rel_to_project(path, payload.get("cwd")), who)
    if tool in SHELL_TOOLS:
        cmd = ti.get("command")
        return check_shell(cmd, who, payload.get("cwd")) if isinstance(cmd, str) else None
    return check_agent(ti, who)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    try:
        why = decide(payload)
    except Exception:
        return 0
    if not why:
        return 0
    sys.stderr.write("🚫 " + why + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
