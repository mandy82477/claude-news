# 第 18 波 主編官方查證：topics/community-tech-patterns（2026-10-09）

查證範圍：頁面引用官方說法的三節（學術對照 L112–124、誰負責拆分 L125–153、缺口追蹤 L154–182），資料截至欄皆寫 2026-09-06。一手來源：`code.claude.com/docs/en/sub-agents`、`/agent-teams`、`/docs/llms.txt`（2026-10-09 取得）。社群節點（技術彙整）不在本波查證範圍——本波題目是拆頁，不是逐則複核。

## 頁面說法對官方（逐條）

| 頁面句（行） | 官方一手（逐字） | 判定 |
|---|---|---|
| L114「三層階梯：subagent→agent teams（實驗性、預設關閉）→cross-session」 | agent-teams：`Agent teams are experimental and disabled by default. Enable them by setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`；sub-agents 開頭：`Subagents work within a single session… For separate sessions that pass messages to each other, see cross-session messaging. For a coordinated team of sessions Claude spawns and supervises, see agent teams.` | ✅ 一致 |
| L123「官方明載團隊之間不可巢狀、一個 session 只能有一個團隊、lead 不可更換，多層階層只能靠 subagent」 | agent-teams Limitations：`No nested teams: teammates cannot spawn their own teammates`、`One team per session`、`Lead is fixed`。sub-agents：`By default, a subagent can spawn subagents of its own, up to three layers below the main conversation`（`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 可調；v2.1.219 起預設 3，v2.1.217–218 曾預設 1） | ✅ 一致；可補「subagent 預設最多三層」這個數字 |
| L131 表「模型自動委派：Claude 依你的要求、subagent 描述欄與當前脈絡自動決定何時委派」 | sub-agents 本文同義 | ✅ |
| L133「官方未提供『編排者與工人分別指定模型』的預設，但可在 subagent 定義填 model 欄」 | sub-agents Frontmatter：`model … sonnet, opus, haiku, fable, a full model ID… or inherit`；解析順序：呼叫時 `model` 參數→定義 frontmatter→`CLAUDE_CODE_SUBAGENT_MODEL`→主對話模型；`CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`（v2.1.257+）可強制 | ✅ 一致；「全域環境變數」L170 有寫 |
| L134「lead 把工作拆成任務並自動指派；隊友做完會自己認領下一個」 | agent-teams：`Lead assigns… Self-claim: after finishing a task, a teammate picks up the next unassigned, unblocked task on its own`；Tip：`The lead breaks work into tasks and assigns them to teammates automatically` | ✅ |
| L170「官方團隊文件**建議**隊友用 Sonnet」 | agent-teams 只有範例 prompt：`Spawn 4 teammates to refactor these modules in parallel. Use Sonnet for each teammate.`——是示範寫法，不是建議；另 `teammateDefaultModel was removed in v2.1.234` | ⚠️ 過度解讀：改「官方範例以 Sonnet 當隊友」 |
| L171「動態粒度：官方只有工作流大小三檔靜態旋鈕」 | Workflow 工具的 size guideline（medium：10 個 agent 以下）仍是靜態；agent-teams Best practices 只給 `Start with 3-5 teammates`、`5-6 tasks per teammate` 經驗值 | ✅ 仍成立（未補） |
| L173「協調與衝突解決：官方答案是 git worktree 隔離」 | sub-agents：`isolation: worktree… giving it an isolated copy of the repository`；agent-teams：`Avoid file conflicts: Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.` | ✅ 一致，且 teams 這邊連隔離都沒有、只有「自己分好檔」——可補一句 |
| L164「cross-session 傳訊 v2.1.224 起預設開啟」 | 本波未重查版本號（09-20 已對 official-community-gap 對齊） | 不動 |

**沒有一條事實錯；一條措辭過重（L170）、兩處可補數字（subagent 三層、teams 無隔離）。三節「資料截至 2026-09-06」可改 2026-10-09。**

## 給冷讀者四題的官方錨句（設計者寫子頁導言用）

- Q1（多 agent 分工）：官方三條路的分界句——`Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.`；同時併發上限 `By default, when 20 subagents are running in a session, spawning another… fails`（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調，v2.1.217+）。
- Q2（記憶／context）：官方頁 `code.claude.com/docs/en/memory`（How Claude remembers your project）——本波未抓內文，子頁導言只連頁不引句。
- Q3（skill 設計）：官方頁 `/docs/en/skills`；本頁沒有引官方 skill 規範的句子，子頁可只連頁。
- Q4（hooks／plugin／MCP）：官方頁 `/docs/en/hooks-guide`、`/docs/en/plugins/overview`、`/docs/en/mcp`；agent-teams 有三個 hook 事件 `TeammateIdle`／`TaskCreated`／`TaskCompleted`（exit 2 擋下並回饋）——頁面未提，屬「官方補了」的可補項，但是 teams 範圍、放 Agent 群不放自動化群。

## 逾期懸置

本頁懸置標記由健檢卡清點（第 10 條）；主編本波不結案任何一筆。⟨Q-07⟩ 09-20 已查證「未恢復」，10-09 未重查（v2.1.288 後 release notes 本波未抓）。

## 給設計者三句

1. 官方文件自己的分法就是三個入口：sub-agents／agent-teams／worktrees 一組，memory 一組，skills／hooks／plugins／MCP 一組——子頁按讀者問題分群時，這三組有官方頁可當每個子頁的「官方零件」錨。
2. 學術對照與缺口追蹤兩節是「Agent 怎麼組」群的結論層，拆後跟著那個子頁走，母頁只留一行指路；它們的「資料截至」改 2026-10-09 並把 L170 措辭改掉。
3. 本波不要動社群節點的事實（251 則一則不改），拆頁是搬家不是改稿；搬家後錨點 `[[topics/community-tech-patterns#2026-09]]` 這類月份錨會全部斷，設計者要給出新錨規則（子頁內仍保留 `### YYYY-MM` 分組則錨點形狀可延續）。
