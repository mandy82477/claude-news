#!/usr/bin/env python3
"""ingest_metrics.py — 每日 ingest 量測帳本：每位記者這輪花了多少輪、多少 token、讀了什麼。

帳本 data/ingest-metrics.jsonl 一個 agent 一行，append only。要回答的問題是「規則瘦身、
派工包等改動前後，每位記者的輪數／token／讀了什麼有沒有變」——所以只量不評，不設門檻。

資料來源是本機 Claude Code 的 subagent transcript：
    ~/.claude/projects/<專案編碼>/<session-id>/subagents/agent-*.jsonl
挑首則 user 訊息首行帶記者角色前導、且 prompt 內「今日日報日期／今日日期」＝目標日的檔。
同一目錄混有頁面健檢、實作等其他 agent，一律靠角色前導排除，不靠檔名或時間。

計數口徑（與「一筆 assistant 記錄＝一輪」的直覺不同，刻意的）：
transcript 把一次 API 回應按 content block 拆成多筆 assistant 記錄（thinking／text／
每個 tool_use 各一筆），每筆都帶**同一份** usage（cache_read、cache_create 相同，
output_tokens 逐筆累加、最後一筆才是終值）。逐筆加總會把 cache_read 灌大約 1.7 倍，
而且倍數隨「每輪平行叫幾個工具」浮動——正是改動前後要比的東西，會讓比較失真。
所以：`turns`＝不重複的 message.id 數（真實 API 呼叫數），token 以每個 message.id
取一次（output 取最大值）；逐筆記錄數另存 `assistant_records` 供對照。

找不到 transcript（目錄不存在、或當日無記者 transcript；雲端 routine 是否留有 transcript 尚未以探針證實）時印「無 transcript」、
exit 0、**不寫任何行**——零值行會被讀成「那天很省」。

transcript 不完整（檔尾不是 assistant 的純文字結尾，或有壞 JSON 行）時照樣記，但標
`incomplete: true`：數字是下限，不可與正常行並列比較。之後重跑若該檔已完整，會 append
一行新紀錄（同 agent_file 最後一行勝出）；已有完整行則跳過（冪等）。

用法：
    python scripts/ingest_metrics.py --date 2026-09-26
    python scripts/ingest_metrics.py --date 2026-09-26 --dry-run
    python scripts/ingest_metrics.py --date 2026-09-26 --session-dir <session 目錄或其 subagents/>

exit 0 正常（含無 transcript）｜2 參數錯。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import sys
from collections import Counter
from datetime import date as _date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "data" / "ingest-metrics.jsonl"

# 角色前導只認 prompt 首行，日期只認 prompt 內的日期宣告行
_ROLE_PATTERNS = (
    (re.compile(r"你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者"), "devpractice"),
    (re.compile(r"你是 CLAUDE_NEWS wiki 的「投資分析（market）」記者"), "market"),
    (re.compile(r"你是 CLAUDE_NEWS wiki 的分類複核記者"), "分類複核"),
    (re.compile(r"你是 CLAUDE_NEWS wiki 的「(模型|功能|商業|安全政策|社群|人物)」記者"), None),
)
_DATE_DECL = re.compile(r"今日(?:日報)?日期[：:]\s*(\d{4}-\d{2}-\d{2})")
_EDIT_TOOLS = {"Edit", "Write", "MultiEdit"}
_RULE_PATH = re.compile(r"(?:^|/)(\.claude/(?:reporter-rules|agents)/[^\s'\"]+)$")
_SED_RANGE = re.compile(r"^(\d+)(?:,(\d+))?p$")
_HEAD_N = re.compile(r"^-(\d+)$")


# ── 路徑 ────────────────────────────────────────────────────────────────

def default_projects_root(repo_root: Path = ROOT) -> Path:
    """Claude Code 把專案路徑的非英數字元一律換成 '-' 當目錄名。"""
    base = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
    return base / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(repo_root))


def _norm(p: str) -> str:
    return p.replace("\\", "/").strip().strip("'\"")


def rule_path(p: str) -> str | None:
    m = _RULE_PATH.search(_norm(p))
    return m.group(1) if m else None


def wiki_path(p: str, repo_root: Path = ROOT) -> str | None:
    """回傳 repo 相對的 wiki/**.md；絕對路徑須落在 repo 內，相對路徑須以 wiki/ 起頭。"""
    n = _norm(p)
    if not n.endswith(".md"):
        return None
    root = _norm(str(repo_root)).rstrip("/") + "/"
    if n.lower().startswith(root.lower()):
        n = n[len(root):]
    elif n.startswith("./"):
        n = n[2:]
    return n if n.startswith("wiki/") else None


def _line_count(rel: str, repo_root: Path) -> int | None:
    try:
        return len((repo_root / rel).read_text(encoding="utf-8").splitlines())
    except OSError:
        return None


# ── 辨識 ────────────────────────────────────────────────────────────────

def _text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
    return ""


def identify(first_prompt: str) -> tuple[str, str] | None:
    """(role, date) 或 None。角色只看首行、日期看全文的日期宣告。"""
    stripped = first_prompt.strip()
    if not stripped:
        return None
    head = stripped.splitlines()[0]
    role = None
    for pat, name in _ROLE_PATTERNS:
        m = pat.search(head)
        if m:
            role = name or m.group(1)
            break
    d = _DATE_DECL.search(first_prompt)
    if role is None or not d:
        return None
    return role, d.group(1)


def _first_prompt(path: Path) -> str:
    """只讀到第一則非 meta 的 user 記錄（通常就是第一行）。"""
    try:
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("type") == "user" and not r.get("isMeta"):
                    return _text_of((r.get("message") or {}).get("content"))
    except OSError:
        pass
    return ""


def find_transcripts(date: str, search_dirs: list[Path]) -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    for d in search_dirs:
        for p in sorted(d.glob("agent-*.jsonl")):
            ident = identify(_first_prompt(p))
            if ident and ident[1] == date:
                found.append((p, ident[0]))
    return found


def search_dirs_for(session_dir: Path | None, projects_root: Path) -> list[Path]:
    if session_dir is not None:
        if not session_dir.is_dir():
            return []
        sub = session_dir / "subagents"
        return [sub if sub.is_dir() else session_dir]
    if not projects_root.is_dir():
        return []
    return sorted(p for p in projects_root.glob("*/subagents") if p.is_dir())


# ── Bash 指令解析 ─────────────────────────────────────────────────────────

def _split_pipelines(command: str) -> list[list[list[str]]]:
    """指令 → [pipeline[simple-command[token]]]。解析失敗的行退回空白切分。"""
    out: list[list[list[str]]] = []
    for raw in command.splitlines():
        try:
            lex = shlex.shlex(raw, posix=True, punctuation_chars=True)
            lex.whitespace_split = True
            toks = list(lex)
        except ValueError:
            toks = raw.split()
        pipeline: list[list[str]] = []
        cur: list[str] = []
        for t in toks:
            if t == "|":
                pipeline.append(cur)
                cur = []
            elif t in ("&&", "||", ";", "&", ";;"):
                pipeline.append(cur)
                out.append(pipeline)
                pipeline, cur = [], []
            else:
                cur.append(t)
        pipeline.append(cur)
        out.append(pipeline)
    return out


def bash_reads(command: str) -> list[dict]:
    """抽出 cat／sed -n／head／tail／grep 讀到的檔。

    回傳 {"path", "method", "range"?, "piped"}；piped＝輸出又被管線接走，內容沒有整份進 context。
    """
    reads: list[dict] = []
    for pipeline in _split_pipelines(command):
        for i, cmd in enumerate(pipeline):
            while cmd and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", cmd[0]):
                cmd = cmd[1:]
            if not cmd:
                continue
            name = cmd[0].rsplit("/", 1)[-1]
            args = cmd[1:]
            piped = i < len(pipeline) - 1
            files = [a for a in args if not a.startswith("-") and a not in (">", ">>", "<", "2>")]
            if name == "cat":
                reads += [{"path": f, "method": "Bash-cat", "piped": piped} for f in files]
            elif name == "sed" and "-n" in args:
                rest = [a for a in args if a != "-n"]
                rng = None
                for j, a in enumerate(rest):
                    m = _SED_RANGE.match(a)
                    if m:
                        rng = [int(m.group(1)), int(m.group(2) or m.group(1))]
                        rest = rest[j + 1:]
                        break
                reads += [{"path": f, "method": "Bash-sed", "range": rng, "piped": piped}
                          for f in rest if not f.startswith("-")]
            elif name in ("head", "tail"):
                n, fl, skip = 10, [], False
                for j, a in enumerate(args):
                    if skip:
                        skip = False
                        continue
                    if a == "-n" and j + 1 < len(args) and args[j + 1].lstrip("+").isdigit():
                        n, skip = int(args[j + 1].lstrip("+")), True
                    elif _HEAD_N.match(a):
                        n = int(a[1:])
                    elif not a.startswith("-"):
                        fl.append(a)
                reads += [{"path": f, "method": f"Bash-{name}",
                           "range": [1, n] if name == "head" else None, "piped": piped}
                          for f in fl]
            elif name == "grep":
                # grep 的第一個非選項參數是 pattern，其後才是檔
                pos = [a for a in args if not a.startswith("-")]
                reads += [{"path": f, "method": "Bash-grep", "piped": piped} for f in pos[1:]]
    return reads


# ── 單檔量測 ─────────────────────────────────────────────────────────────

def _ts(s) -> datetime | None:
    if not isinstance(s, str):
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _normal_end(last: dict | None) -> bool:
    """正常收尾＝最後一筆是 assistant、只含 text、沒有 tool_use，stop_reason 不是 tool_use。"""
    if not last or last.get("type") != "assistant":
        return False
    m = last.get("message") or {}
    kinds = {c.get("type") for c in m.get("content") or [] if isinstance(c, dict)}
    return kinds == {"text"} and m.get("stop_reason") in (None, "end_turn", "stop_sequence")


def measure(path: Path, role: str, date: str, repo_root: Path = ROOT) -> dict:
    records: list[dict] = []
    bad_lines = 0
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except ValueError:
                bad_lines += 1

    usage_by_msg: dict[str, dict] = {}
    out_by_msg: dict[str, int] = {}
    assistant_records = 0
    tools: Counter = Counter()
    seen_tool_ids: set[str] = set()
    hooks = 0
    rule_reads: list[dict] = []
    wiki_full: list[dict] = []
    stamps = [t for t in (_ts(r.get("timestamp")) for r in records) if t]

    for r in records:
        att = r.get("attachment")
        if isinstance(att, dict) and att.get("type") == "hook_success":
            hooks += 1
        if r.get("type") != "assistant":
            continue
        assistant_records += 1
        m = r.get("message") or {}
        key = m.get("id") or r.get("requestId") or r.get("uuid") or f"rec{assistant_records}"
        u = m.get("usage") or {}
        usage_by_msg[key] = u
        out_by_msg[key] = max(out_by_msg.get(key, 0), int(u.get("output_tokens") or 0))
        for c in m.get("content") or []:
            if not isinstance(c, dict) or c.get("type") != "tool_use":
                continue
            tid = c.get("id")
            if tid in seen_tool_ids:
                continue
            if tid:
                seen_tool_ids.add(tid)
            name = c.get("name") or "?"
            tools[name] += 1
            inp = c.get("input") or {}
            if name == "Read":
                fp = str(inp.get("file_path") or "")
                rp = rule_path(fp)
                if rp:
                    e = {"file": rp, "method": "Read"}
                    if inp.get("offset") is not None:
                        e["offset"] = inp["offset"]
                    if inp.get("limit") is not None:
                        e["limit"] = inp["limit"]
                    rule_reads.append(e)
                wp = wiki_path(fp, repo_root)
                if wp and inp.get("offset") is None and inp.get("limit") is None:
                    wiki_full.append({"file": wp, "method": "Read",
                                      "lines": _line_count(wp, repo_root)})
            elif name == "Grep":
                rp = rule_path(str(inp.get("path") or ""))
                if rp:
                    rule_reads.append({"file": rp, "method": "Grep"})
            elif name == "Bash":
                for br in bash_reads(str(inp.get("command") or "")):
                    rp = rule_path(br["path"])
                    if rp:
                        e = {"file": rp, "method": br["method"]}
                        if br.get("range"):
                            e["range"] = br["range"]
                        if br["piped"]:
                            e["piped"] = True
                        rule_reads.append(e)
                    wp = wiki_path(br["path"], repo_root)
                    if wp and br["method"] == "Bash-cat" and not br["piped"]:
                        wiki_full.append({"file": wp, "method": "Bash-cat",
                                          "lines": _line_count(wp, repo_root)})

    return {
        "date": date,
        "role": role,
        "session_id": path.parent.parent.name if path.parent.name == "subagents" else path.parent.name,
        "agent_file": path.name,
        "turns": len(usage_by_msg),
        "assistant_records": assistant_records,
        "tool_uses": {"total": sum(tools.values()), "by_tool": dict(sorted(tools.items()))},
        "edits": sum(v for k, v in tools.items() if k in _EDIT_TOOLS),
        "cache_read": sum(int(u.get("cache_read_input_tokens") or 0) for u in usage_by_msg.values()),
        "cache_create": sum(int(u.get("cache_creation_input_tokens") or 0) for u in usage_by_msg.values()),
        "output_tokens": sum(out_by_msg.values()),
        "duration_s": round((max(stamps) - min(stamps)).total_seconds()) if len(stamps) >= 2 else None,
        "hook_feedback": hooks,
        "rule_reads": rule_reads,
        "wiki_full_reads": wiki_full,
        "incomplete": bad_lines > 0 or not _normal_end(records[-1] if records else None),
        "_start": min(stamps).isoformat() if stamps else "",
    }


# ── 帳本 ────────────────────────────────────────────────────────────────

def load_ledger(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return rows


def collect(date: str, search_dirs: list[Path], repo_root: Path = ROOT) -> list[dict]:
    rows = [measure(p, role, date, repo_root) for p, role in find_transcripts(date, search_dirs)]
    rows.sort(key=lambda r: (r["role"], r["_start"], r["agent_file"]))
    counts: Counter = Counter()
    for r in rows:
        counts[r["role"]] += 1
        r["run_index"] = counts[r["role"]]
        del r["_start"]
    return rows


def new_rows(rows: list[dict], ledger_rows: list[dict]) -> list[dict]:
    """冪等：同 (date, session, agent_file) 已有完整行就跳過；舊行不完整而新量測也不完整時同樣跳過。"""
    last: dict[tuple, dict] = {}
    for r in ledger_rows:
        last[(r.get("date"), r.get("session_id"), r.get("agent_file"))] = r
    out = []
    for r in rows:
        prev = last.get((r["date"], r["session_id"], r["agent_file"]))
        if prev is None or (prev.get("incomplete") and not r["incomplete"]):
            out.append(r)
    return out


def summary_table(rows: list[dict]) -> str:
    lines = ["角色｜run｜turns｜tool_uses｜edits｜cache_read M｜output K｜wiki全讀｜狀態"]
    for r in rows:
        lines.append(
            f"{r['role']}｜{r['run_index']}｜{r['turns']}｜{r['tool_uses']['total']}｜{r['edits']}｜"
            f"{r['cache_read'] / 1e6:.2f}｜{r['output_tokens'] / 1e3:.1f}｜{len(r['wiki_full_reads'])}｜"
            f"{'⚠️ 不完整（數字是下限）' if r['incomplete'] else 'ok'}")
    return "\n".join(lines)


def _use_utf8_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _use_utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True, help="YYYY-MM-DD（日報日期）")
    ap.add_argument("--session-dir", type=Path, default=None,
                    help="只看這個 session（session 目錄或其 subagents/）")
    ap.add_argument("--projects-root", type=Path, default=None,
                    help="預設 ~/.claude/projects/<本專案編碼>")
    ap.add_argument("--ledger", type=Path, default=LEDGER)
    ap.add_argument("--repo-root", type=Path, default=ROOT, help="算 wiki 檔行數用（測試覆寫）")
    ap.add_argument("--dry-run", action="store_true", help="只印不寫")
    args = ap.parse_args(argv)
    try:
        _date.fromisoformat(args.date)
    except ValueError:
        print(f"--date 不是有效日期（要 YYYY-MM-DD）：{args.date}")
        return 2

    dirs = search_dirs_for(args.session_dir, args.projects_root or default_projects_root(args.repo_root))
    rows = collect(args.date, dirs, args.repo_root)
    if not rows:
        print(f"無 transcript：{args.date} 找不到記者 subagent transcript"
              "（雲端 routine 或已清除），未寫帳本。")
        return 0

    fresh = new_rows(rows, load_ledger(args.ledger))
    print(f"# ingest 量測 {args.date}：{len(rows)} 個 agent，新寫入 {len(fresh)} 行"
          f"{'（dry-run 未寫）' if args.dry_run else ''}")
    print(summary_table(rows))
    if args.dry_run:
        for r in fresh:
            print(json.dumps(r, ensure_ascii=False))
    elif fresh:
        args.ledger.parent.mkdir(parents=True, exist_ok=True)
        with args.ledger.open("a", encoding="utf-8", newline="\n") as fh:
            for r in fresh:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
