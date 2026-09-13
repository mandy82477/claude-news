# 探針記錄：雲端 routine session 有沒有 Workflow 工具（多 agent 編排）（2026-09-13）

> 執行者：CLAUDE_NEWS 一次性雲端探針 agent。全程逐字記錄指令與原始輸出，不推論、不修改探針記錄以外的檔案。

## 步驟 1：環境確認

指令與原始輸出：

```
$ pwd
/home/user/claude-news

$ claude --version 2>&1 || echo no-claude-cli
2.1.270 (Claude Code)

$ echo ENTRYPOINT=$CLAUDE_CODE_ENTRYPOINT REMOTE=$CLAUDE_CODE_REMOTE
ENTRYPOINT=remote_trigger REMOTE=true
```

## 步驟 2：系統提示裡直接可用的工具名稱清單（非 skill）

系統提示最上方直接定義（非 deferred、非 skill）的工具，逐一抄下：

1. Agent
2. Bash
3. Artifact
4. Edit
5. Glob
6. Grep
7. ListAgents
8. PushNotification
9. Read
10. ReadNotifications
11. ReportFindings
12. ScheduleWakeup
13. SendUserFile
14. ShowOnboardingRolePicker
15. Skill
16. SuggestSkills
17. ToolSearch
18. **Workflow**
19. Write

特別記錄：

- `Workflow`：**存在**（見上方第 18 項），直接列在系統提示工具清單中，非 deferred。
- `Agent`（或 `Task`）：**存在**，名稱為 `Agent`；未見到叫做 `Task` 的工具。
- `ToolSearch`：**存在**。

## 步驟 3：ToolSearch 呼叫原文

### 3a. `ToolSearch(query="select:Workflow", max_results=5)`

回傳原文（節錄自 `<functions>` 區塊，完整 description 過長，關鍵欄位逐字抄）：

```
<function>{"description": "Execute a workflow script that orchestrates multiple subagents deterministically. Workflows run in the background — this tool returns immediately with a task ID, and a <task-notification> arrives when the workflow completes. Use /workflows to watch live progress.

ONLY call this tool when the user has explicitly opted into multi-agent orchestration. ...

Every script must begin with `export const meta = {...}`: a PURE LITERAL (no variables, calls or interpolation) giving the workflow's `name`, a one-line `description` ... Pass the script inline via `script` — do not Write it to a file first, and do not also set the tool's `name` input (that selects a saved workflow); it is plain JavaScript, not TypeScript.

The canonical multi-stage pattern — pipeline by default, each dimension verifies as soon as its review completes: ...

Before writing a script, load the `workflow-authoring` skill — the workflow authoring reference: script API and gotchas, resume, the **Ultracode** section, quality patterns, worked examples.

This session has the default workflow size guideline: medium — keep workflows under 15 agents. This is a guideline, not a hard limit — follow it unless the user's prompt calls for a different scale. The user can raise or remove it with \"Dynamic workflow size\" in /config.", "name": "Workflow", "parameters": {"$schema": "https://json-schema.org/draft/2020-12/schema", "additionalProperties": false, "properties": {"args": {...}, "description": {...}, "name": {...}, "resumeFromRunId": {...}, "script": {"description": "Self-contained workflow script. Must begin with `export const meta = { name, description, phases }` (pure literal, no computed values) followed by the script body using agent()/parallel()/pipeline()/phase().", "maxLength": 524288, "type": "string"}, "scriptPath": {...}, "title": {...}}, "type": "object"}}</function>
```

（成功比對到 `Workflow` 工具，schema 完整載入，可直接呼叫。）

### 3b. `ToolSearch(query="workflow orchestration script", max_results=5)`

回傳原文：4 個結果，名稱依序為：

1. `EnterWorktree`（git worktree 建立/切換工具，與多 agent 編排無關）
2. `Monitor`（背景腳本事件監控工具）
3. `TaskUpdate`（任務清單狀態更新工具）
4. `mcp__Claude_Code_Remote__create_session`（建立新 Claude Code Remote session，可用於 fan-out 編排）
5. `mcp__github__actions_get`（GitHub Actions 資源查詢）

備註：此關鍵字查詢**沒有**再次命中 `Workflow` 本體（已透過 3a 精確命中並載入），命中的是語意相近但不同的工具（worktree、任務更新、遠端 session 建立、GitHub Actions）。

## 步驟 4：實際呼叫 Workflow 工具

呼叫時使用的 script（逐字，與指示相同）：

```js
export const meta = { name: 'cloud-probe', description: '雲端 Workflow 可用性探針', phases: [{ title: 'Probe' }] }
phase('Probe')
const r = await parallel([1,2].map(i => () => agent(`只回傳字串 ok-${i}，不做其他事`, {label: `probe-${i}`, effort: 'low'})))
return { results: r }
```

### 4a. 工具呼叫的立即回傳（原文）

```
Workflow launched in background. Task ID: wbezk6pcw
Summary: 雲端 Workflow 可用性探針
Transcript dir: /root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/subagents/workflows/wf_a84a13d7-702
Script file: /root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/workflows/scripts/cloud-probe-wf_a84a13d7-702.js
(Edit this file with Write/Edit and re-invoke Workflow with {scriptPath: "/root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/workflows/scripts/cloud-probe-wf_a84a13d7-702.js"} to iterate without resending the script.)
Run ID: wf_a84a13d7-702
To resume after editing the script: Workflow({scriptPath: "/root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/workflows/scripts/cloud-probe-wf_a84a13d7-702.js", resumeFromRunId: "wf_a84a13d7-702"}) — completed agents return cached results (cached results may themselves be empty — inspect journal.jsonl before assuming there is something to recover).

You will be notified when it completes. Use /workflows to watch live progress.
```

### 4b. 完成通知（`<task-notification>`，原文）

```
<task-id>wbezk6pcw</task-id>
<tool-use-id>toolu_01EWyKRN1dLYQMJgkN7K1F78</tool-use-id>
<output-file>/tmp/claude-0/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/tasks/wbezk6pcw.output</output-file>
<status>completed</status>
<summary>Dynamic workflow "雲端 Workflow 可用性探針" completed</summary>
<result>{"results":["ok-1","ok-2"]}</result>
<diagnostics>Per-agent results: /root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/subagents/workflows/wf_a84a13d7-702/journal.jsonl — one {"type":"result",...} line per completed agent with its full return value.
If the result above is empty or unexpected, Read this file BEFORE diagnosing — do not assume agents returned non-empty results.
To re-run with edited post-processing: Workflow({scriptPath: '/root/.claude/projects/-home-user-claude-news/cb41a5e5-790e-5c14-a563-97595f0d548c/workflows/scripts/cloud-probe-wf_a84a13d7-702.js', resumeFromRunId: 'wf_a84a13d7-702'}) — agents whose (prompt, opts) are unchanged replay from cache.</diagnostics>
<usage><agent_count>2</agent_count><agents_done>2</agents_done><agents_error>0</agents_error><agents_skipped>0</agents_skipped><agents_empty_result>0</agents_empty_result><subagent_tokens>106842</subagent_tokens><tool_uses>0</tool_uses><duration_ms>3098</duration_ms></usage>
```

兩個 `parallel()` 分支（`probe-1`、`probe-2`）皆回傳預期字串 `ok-1`、`ok-2`，`agents_error` 為 0，`status` 為 `completed`。

## 步驟 5：對照組（Agent tool）

呼叫參數：`Agent({description: "Control group ok test", subagent_type: "general-purpose", prompt: "回答 ok 即可", run_in_background: false})`。

回傳原文：

```
ok
```

```
agentId: a936483cf7e41db1b (use SendMessage with to: 'a936483cf7e41db1b', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 53647
tool_uses: 0
duration_ms: 1589</usage>
```

## 結論

- **Workflow 工具**：存在，且**可執行**——直接呼叫成功，背景啟動後正常完成，兩個 `parallel()` 子 agent 均正確回傳指定字串，`agents_error: 0`。
- **Agent 對照組**：**成功**——`general-purpose` subagent 正確回傳 `ok`。
