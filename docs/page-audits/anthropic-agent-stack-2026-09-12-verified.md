# 主編官方查證：topics/anthropic-agent-stack（第 13 波，2026-09-12）

查證者：主 session（claude-news-c1）。一手來源：code.claude.com 官方文件、platform.claude.com、anthropics/claude-code CHANGELOG.md（raw，2026-09-12 抓取）、GitHub issue（`gh issue view`）。行號指 `wiki/topics/anthropic-agent-stack.md` 現行檔（116 行）。

## 一、本波主軸：每個積木「官方為什麼出」的一手錨句

使命句要求每卡答「沒有它之前的痛」「官方多給了什麼」「現在能跑的工作流」。下表是官方自己怎麼說的，設計者寫卡時逐字引或改寫，不得自行補「通用工程常識」。

| 積木 | 官方一句「為什麼」（逐字） | 官方點名的工作流場景（逐字或列點） | 首發版本（changelog） | 現況 |
|---|---|---|---|---|
| `/goal` | "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds." "`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work." | 官方四例：migrate a module until every call site compiles and tests pass；implement a design doc until all acceptance criteria hold；split a large file until each is under a size budget；work through a labeled issue backlog until the queue is empty。最小指令 `/goal all tests in test/auth pass and the lint step is clean`；非互動 `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"` | v2.1.139 "Added `/goal` command: set a completion condition and Claude keeps working across turns until it's met" | 正式發布；**有官方專頁** https://code.claude.com/docs/en/goal |
| 內建 subagent | "Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary." | 官方「用 subagent 當」三條：task produces verbose output you don't need in main context／enforce tool restrictions／work is self-contained and returns a summary。續用範例：先「Use the code-reviewer subagent to review the authentication module」，完成後「Continue that code review and now analyze the authorization logic」 | `--agent` 旗標 v2.0.59 "Added --agent CLI flag to override the agent setting for the current session" | 正式發布 |
| Dynamic workflows | "Reach for a workflow when a task needs more agents than one conversation can coordinate, or when you want the orchestration codified as a script you can read and rerun." "A workflow moves the plan into code. With subagents, skills, and agent teams, Claude is the orchestrator: it decides turn by turn what to spawn or assign next, and every result lands in a context window. A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer." | 官方六個 prompt 範本（可逐字抄）：(1) audit every route handler under src/routes/ for missing authentication checks, and adversarially verify each finding；(2) run `npx tsc --noEmit` and keep fixing until the type check passes or two rounds make no progress；(3) migrate every component from JS to TS, each file in its own isolated copy；(4) review every file changed in this PR then merge into one ranked summary；(5) research how three competitors handle rate limiting in parallel then compare；(6) find flaky tests: run the suite repeatedly, stop once two rounds find nothing new。判斷式："The difference is who holds the plan." | v2.1.154 "Introducing dynamic workflows: ask Claude to create a workflow and it orchestrates work across tens to hundreds of agents in the background"；v2.1.160 觸發字由 `workflow` 改 `ultracode` | 全部付費方案（Pro 在 /config 開）；限制 16 路並行（v2.1.269 起 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 可提到 256）、單次 1,000 agent、`parallel()`/`pipeline()` 單次 4,096 項 |
| Agent teams | "Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own." 官方先勸退："Before you set up a team, check whether a lighter option does the job." | 官方四類：research and review／new modules or features／debugging with competing hypotheses／cross-layer coordination。兩個逐字 prompt：三位 reviewer 各看 security／performance／test coverage 審 PR #142；五位 teammate 各持假說互相反駁（"like a scientific debate"）。建議 3–5 位起步 | v2.1.32 "Added research preview agent teams feature for multi-agent collaboration (token-intensive feature, requires setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)" | 實驗性、預設關閉；限制：`/resume` 不還原 in-process teammate、一 session 一 team、不可巢狀、`-p` 下不 spawn |
| Cross-session messaging | "When a change in one session breaks what another is building on, Claude can warn that session before you notice. When one session settles a question another is blocked on, Claude can send the answer across." | 官方四例：hand over a finding／coordinate parallel worktrees／get status from long-running work／message across machines。逐字 prompt："Ask the session running in my other terminal whether the migration finished"、"Let @api-worker know the schema migration finished"、"Tell me when the migration session finishes what it's working on"（`notify_when_idle`） | v2.1.224 "Added cross-session `SendMessage`: Claude Code sessions can now message each other, on any of your machines, with `ListAgents` to discover them (macOS and Linux)"；v2.1.236 `notify_when_idle` | 原生 Windows v2.1.234 起；訊息只傳純文字不傳歷史；同機走 socket 不經伺服器 |
| Agent view | "Use agent view when you have several independent tasks Claude can work on without you watching every step. Dispatch a bug fix, a pull request review, and a flaky-test investigation as three rows, keep working in another window, and check back when a row shows it needs you or has a result." | `claude agents`；`claude --bg "investigate the flaky SettingsChangeDetector test"`；背景 session 改檔前自動搬進 `.claude/worktrees/` 隔離 | v2.1.139 "Added agent view (Research Preview): a single list of every Claude Code session running, blocked on you, or done" | 研究預覽 |
| Managed Agents | "Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment" | 官方六條 when-to-use：long-running execution（minutes or hours）／cloud sandboxes／self-hosted sandboxes for compliance／minimal infrastructure／stateful sessions（persistent filesystems and history）／scheduled execution（cron） | — | beta（帳號預設可用，須 `managed-agents-2026-04-01` header）；**MCP tunnels 與 dreaming 是「more limited research preview」須申請**（見二-⑤） |
| Self-hosted runner | "Self-hosting is for teams whose network, tooling, or compliance requirements call for keeping session execution on infrastructure they control." 三個換來的東西：network access／custom tooling／compliance | 場景：cloud session 要碰內網 DB、registry；runner image 預裝內部 CLI | v2.1.224 "Added self-hosted environments: `claude self-hosted-runner` turns your own machines or containers into a place Claude Code web, mobile, and desktop sessions can run, on Team and Enterprise plans" | public beta，Team／Enterprise，預設關閉 |

官方總覽頁（https://code.claude.com/docs/en/agents）給的三問決策樹，可直接當卡片後的「怎麼挑」：**Who coordinates the work?**（Claude 在一個對話內派收→subagent；你丟出去晚點回來看→agent view；Claude 規劃分派監督→agent teams；script 持有計畫→workflows）／**Do the workers need to talk to each other?**／**Do the tasks touch the same files?**（worktrees）。

## 二、頁面現有數字對官方（逐條判定）

| # | 行 | 頁面原句 | 官方 | 判定 |
|---|---|---|---|---|
| ① | L61 | 「官方文件站沒有 `/goal` 的專頁，以 changelog 為據」 | https://code.claude.com/docs/en/goal 存在，含條件寫法、4,000 字元上限、評估機制、`/goal clear`、resume 行為 | **錯，須改**：改指官方專頁；4,000 字元、"or stop after 20 turns" 兩點官方頁逐字可證 |
| ② | L62 | Explore「跳過 CLAUDE.md」「以 Opus 為上限（v2.1.198 起）」 | sub-agents 頁：Explore "Model: Inherits from main conversation (capped at Opus on Claude API)"，未標版本；v2.1.198 官方寫的是 subagent 繼承 extended thinking 設定。「跳過 CLAUDE.md」本次未在官方頁查得 | **部分**：Opus 上限成立但版本號對錯事實；「跳過 CLAUDE.md」標待查證或刪 |
| ③ | L64 | `--agent` 引入版本「第三方 ClaudeLog 稱 v2.0.59，官方 changelog 未直接查得」 | changelog v2.0.59 "Added --agent CLI flag to override the agent setting for the current session" | **可升級**：官方 changelog 已查得，刪「未直接查得」 |
| ④ | L68 | 「上限 16 路並行、單次 1,000 agent」 | 官方限制表同；v2.1.269 新增 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`（1–256）可提高 | 對；可補一句 |
| ⑤ | L83 | 「MCP 隧道（公開測試）」 | Managed Agents overview："Within the beta, MCP tunnels and dreaming are in a more limited research preview. Request access" | **錯，須改**：研究預覽須申請，非公開測試 |
| ⑥ | L81 | 「issue #24798，75 則留言」「原始需求…如今由第三層的 workflows 以 script 承接」 | `gh issue view 24798`：**CLOSED**，84 則留言；原文三項需求＝inter-session messaging／shared project scratchpad／event bus | **更新**：標已關閉、84 則；官方對應是 cross-session messaging（第 1 項）＋`notify_when_idle`（第 3 項部分）；第 2 項 shared scratchpad 官方無對應。「由 workflows 承接」是本頁推論，issue 原文沒提編排 |
| ⑦ | L83 | A2A「issue #28300 未回應」 | `gh issue view 28300`：OPEN | 對 |
| ⑧ | L81 | 跨 session 傳訊「macOS／Linux v2.1.224、原生 Windows v2.1.234」「閒置通知 v2.1.236」 | 官方頁與 changelog 皆同 | 對 |
| ⑨ | L81 | agent teams「實驗性、預設關閉」 | 官方 Warning 逐字同 | 對；可補首發 v2.1.32 |
| ⑩ | L77 | agent view「研究預覽」 | 官方同；首發 v2.1.139 | 對 |
| ⑪ | L79 | dynamic workflows「全部付費方案」 | 官方 Note："available on all paid plans… On Pro, turn them on from the Dynamic workflows row in /config" | 對；首發 v2.1.154 可補 |
| ⑫ | L52 | `/goal`「✅ 正式發布（v2.1.139）」 | changelog v2.1.139 同 | 對 |
| ⑬ | L85 | Dreaming「研究預覽，須申請並帶 header」 | 同 ⑤ 來源 | 對 |
| ⑭ | L66 | 「`ultracode` 關鍵字或直說 use a workflow」 | 官方同；另有 `/effort ultracode` 讓 Claude 自行決定每個實質任務是否開 workflow（頁面未寫） | 對；可補 `/effort ultracode` 一句 |

Managed Agents 計費（L69–70）沿用第 2 波 2026-09-06 查證，本波未重查。

## 三、逾期懸置

`check_pending_markers.py` 對本頁：pending_count 0。無懸置需處置。

## 四、給設計者三句

1. 每張卡的「官方為什麼出」欄只准用第一節表格的逐字句或其忠實改寫；工作流欄優先抄官方自己給的 prompt 範本（workflows 六條、teams 兩條、cross-session 三條、/goal 四例），社群案例放第二位。
2. 二-①（/goal 專頁）與二-⑤（MCP 隧道狀態）是硬錯，實作單必含；二-⑥ issue #24798 改「已關閉、84 則」並把「由 workflows 承接」降為本頁推論或刪。
3. 官方 agents 總覽頁的三問決策樹（誰協調／要不要互講／碰不碰同檔）比本頁六層架構更貼讀者視角，可考慮以它取代六層作為「怎麼挑」節的骨架，六層降為附錄。

## 五、健檢卡「需官方查證表」五項回覆（主 session，2026-09-12 補查）

| # | 項 | 官方 | 處置 |
|---|---|---|---|
| 1 | Agent SDK 列版本下限與計費切割句 | 未上網重查。v0.100.0／v0.95.0 出自本庫 2026-05-07 條目（`entities/claude-code.md` L769、`entities/managed-agents.md` L133）；計費切割暫停句的家在 `entities/pricing.md` L151 與 L613 節 | 本頁該列改一句「計入訂閱配額，細節見 [[entities/pricing]]」，不再抄事實；09-14 pricing 換軌只需改 pricing 一處 |
| 2 | **組合題：subagent 加 workflows 能不能疊** | sub-agents 頁："By default, a subagent can spawn subagents of its own, up to three layers below the main conversation"（`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`）；同頁 Available tools：`Workflow` 一律從 subagent 工具池移除；agent-teams 頁：teammate 不可巢狀、`-p` 與 SDK session 不 spawn teammate；workflows 頁限制表："No mid-run user input"；goal 頁："If a subagent or a background shell command is still running when a turn ends, Claude Code skips the evaluation for that turn" | 可疊的組合（官方可證）：**workflow 的 agent 可再派 subagent（≤3 層）**；**`/goal` 的 session 可以啟 workflow**（評估會等背景工作完）。不可疊：subagent 裡不能開 workflow；workflow 裡不能開 agent teams；workflow 中途不能等你輸入。設計者拿這四句寫「怎麼疊」一節 |
| 3 | L62「Explore 跳過 CLAUDE.md」 | sub-agents 頁逐字："Explore and Plan skip your CLAUDE.md files and the parent session's git status to keep research fast and inexpensive." "Explore and Plan are the only subagents that omit CLAUDE.md and git status." | **對，保留**；二-② 改判：只有版本號 v2.1.198 對錯事實（該版是 extended thinking 繼承） |
| 4 | Managed Agents 持久記憶狀態 | memory 頁：memory store 走 `agent-memory-2026-07-22` beta header，無需申請；dreaming 為研究預覽須申請（overview 頁） | 「持久記憶（公開測試）」可保留為 beta；Dreaming 維持研究預覽 |
| 5 | dynamic workflows 兩頁狀態不一致 | 官方現況：all paid plans（Pro 在 /config 開）。Research Preview 是 v2.1.154 首發時狀態 | `feature-radar` L227 狀態欄過期，實作單列一格修正並互指；退款爭議（UltraCode 1.7M token）是獨立事實，留 radar，本頁只 wikilink 不重述 |
