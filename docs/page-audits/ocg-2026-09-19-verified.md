# 第 14 波主編官方查證：topics/official-community-gap

查證日 2026-09-19。工具：`gh issue view`／`gh api`（anthropics/claude-code）、官方 CHANGELOG.md 原檔、code.claude.com 與 platform.claude.com 文件原文。行號＝對象頁檔案原始行號（含 frontmatter）。

## 一、結論（五行）

1. **本頁最承重的一列是錯的**：AGENTS.md 官方已於 **v2.1.277（2026-09-18）原生支援**，頁面 L65／L80 仍寫「❌ 無官方對應」「仍不支援」。
2. **08-17 Boris Cherny 一次關掉五個本頁引用的 issue**（#6235、#24798、#47023、#24316、#29006，另 #28322 於 08-19），每則都附官方文件連結；頁面多處仍當它們是進行中的社群壓力。
3. **兩列的「官方對應」欄漏掉早就存在的官方功能**：通知（手機推播，2026 第 16 週）、個人用量（`/usage` 方案用量條、狀態列 `rate_limits`、VS Code 警示橫幅）。這兩列的「官方僅被動可見性」「個人用戶仍無官方儀表板」撐不起。
4. **Managed Agents「2026-05-11 正式」與官方相反**：官方文件今天仍寫 beta、須帶 beta header（第 2 波已查過一次，本頁沒回掃到）。
5. 記憶列只比 Dreaming，漏了 Claude Code 自己的 **auto memory**（官方文件有專節）；Dreaming 現況＝beta 內更受限的研究預覽，須申請。

## 二、issue 現況（`gh issue view`，2026-09-19）

| issue | 頁面怎麼寫 | 官方現況 | 判定 |
|---|---|---|---|
| #6235 AGENTS.md | L65「335 則留言、5889 個讚（08-14）」、無官方對應 | **CLOSED／COMPLETED 2026-08-17**；405 則留言、👍 5,174 | 頁面過期；讚數口徑不同（頁面疑為全部 reaction） |
| #24798 session 間通訊 | L67「78 則留言、21 👍」 | CLOSED／COMPLETED 2026-08-17；80 則、22 👍 | 過期 |
| #28300 跨機器 A2A | L67 | **OPEN**；45 則、0 👍 | 仍成立 |
| #47023 lifecycle hooks | L135「社群訴求成型」 | CLOSED／COMPLETED 2026-08-17 | 過期：官方答「四個 hook 今天都有」 |
| #14227 session 間持久記憶 | L135 列為既有開放 issue | CLOSED／**NOT_PLANNED** 2026-05-25 | 「開放」不成立 |
| #24316 自訂 agent 當隊友 | L73 下「子項缺口仍未補齊」 | CLOSED／COMPLETED 2026-08-17 | 過期：已出貨 |
| #28322 `/rc` 無法辨識 | L74「官方可能已悄悄鋪路」 | CLOSED／COMPLETED 2026-08-19 | 過期：v2.1.76／v2.1.206 已修 |
| #29006 Desktop 遠端控制 | L74「社群仍在請求」 | CLOSED／COMPLETED 2026-08-17 | 過期：已出貨 |

官方關閉留言逐字（Boris Cherny，COLLABORATOR）：

- #6235（08-17，[連結](https://github.com/anthropics/claude-code/issues/6235#issuecomment-5311479502)）：「Claude Code reads `CLAUDE.md`, but you can share one file with other agents: create a `CLAUDE.md` containing just `@AGENTS.md` (an import), or symlink `CLAUDE.md` to `AGENTS.md`.」——**關閉當下還不是原生支援**，是 import／symlink 做法；原生支援是一個月後的 v2.1.277。
- #24316（[連結](https://github.com/anthropics/claude-code/issues/24316#issuecomment-5311332830)）：「when spawning a teammate you can name a subagent definition from `.claude/agents/` … The teammate honors that definition's `tools` allowlist and `model` … Note that `skills` and `mcpServers` frontmatter aren't applied to teammates.」
- #29006（[連結](https://github.com/anthropics/claude-code/issues/29006#issuecomment-5311302558)）：「Remote Control now works for Claude Code sessions in the Desktop app. Turn it on under **Settings > Claude Code > Enable remote control by default**」
- #24798（[連結](https://github.com/anthropics/claude-code/issues/24798#issuecomment-5311328527)）：「Much of this shipped: as of v2.1.224 your Claude Code sessions can message each other.」
- #47023：「All four of these hook events exist today: `PreCompact` … `PostCompact` … (added in v2.1.76) … `SessionEnd` … `SessionStart` … can return `additionalContext` to inject recalled memory.」
- #28322（08-19）：「version **2.1.76** fixed slash commands showing "Unknown skill", and **2.1.206** additionally made `/remote-control` always resolve」

## 三、考題的官方錨句

### AGENTS.md（冷讀者 Q1）
- CHANGELOG **2.1.277**（GitHub release 2026-09-18T18:06Z）：「Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in `/config` (not yet on Bedrock, Vertex or Foundry)」
- 官方文件 [memory#agents-md](https://code.claude.com/docs/en/memory#agents-md)：「Claude Code can read `AGENTS.md` as your project instructions, so a repository already set up for other coding agents works without adding a `CLAUDE.md`, an import, or a setting.」「By default, Claude reads `AGENTS.md` only when you have no `CLAUDE.md` in your working directory or above it.」「Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later. In some sessions, such as those on Amazon Bedrock or with telemetry disabled, Claude can't read `AGENTS.md`」
- 三個讀者會踩的邊界（同文件）：有 `CLAUDE.md` 或 `CLAUDE.local.md` 就只讀 CLAUDE.md；要兩者並讀把 **Project instructions** 設 `claude-md-and-agents-md`；Bedrock／Vertex／Foundry 或關掉 telemetry 的 session 讀不到，改用 `@AGENTS.md` import。
- 社群當日回報（#6235 留言，2026-09-19，二手）：設了 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` 時 `/config` 看不到該選項——與官方「telemetry disabled」句一致。

### 額度快用完的提醒（Q2）
- 官方 [costs](https://code.claude.com/docs/en/costs)：「Subscribers see plan usage bars, activity stats, and a usage breakdown」「On a Pro, Max, Team, or Enterprise plan, `/usage` also shows a breakdown of what counts against your plan limits」
- 官方 [statusline](https://code.claude.com/docs/en/statusline)：`rate_limits.five_hour.used_percentage`、`rate_limits.seven_day.used_percentage`、`resets_at`——可自己寫狀態列顯示 5 小時／7 天窗用掉幾 %。
- CHANGELOG：「[VSCode] Added rate limit warning banner with usage percentage and reset time」；「Fixed rate limit warning appearing at low usage after weekly reset (now requires 70% usage)」——**官方有內建警示，門檻 70%**。
- 判定：L61「個人用戶仍無官方儀表板/告警 UI」、L79「個人重度使用者缺口依舊」不成立。還成立的缺口較窄：**沒有主動推到手機／桌面的額度告警、門檻不可自訂**（推論：官方文件未見此設定，非官方明示沒有）。

### 需要輸入時的通知（Q3 的一列）
- [2026 第 16 週 What's new](https://code.claude.com/docs/en/whats-new/2026-w16)：「With Remote Control connected, Claude can send a push notification to your phone when a long task finishes or it needs a decision to keep going.」；文件 [remote-control#mobile-push-notifications](https://code.claude.com/docs/en/remote-control#mobile-push-notifications)。
- CHANGELOG 另有桌面 idle notification、`Notification` hook。
- 判定：L56「官方僅被動可見性」、L75「官方尚未涉足」不成立；該列應屬已產品化或部分產品化，社群補的是終端機標籤變色、實體燈這類形式。

### 記憶（Q4）
- platform 文件 [managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)：「Claude Managed Agents is in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header.」「Within the beta, MCP tunnels and dreaming are in a more limited research preview. Request access to enable them.」
- Claude Code [memory](https://code.claude.com/docs/en/memory)：「**Auto memory**: notes Claude writes itself based on your corrections and preferences」「Subagents can also maintain their own auto memory.」；CHANGELOG「Claude automatically saves useful context to auto-memory. Manage with /memory」「Project configs & auto memory now shared across git worktrees」
- 判定：Dreaming 是 Managed Agents（API 產品）的功能，須申請；Claude Code 使用者的官方記憶是 auto memory，本頁 L58／L77／L103／L133 完全沒提——「跨 session 記憶歸零 ⏳ 正在做但遠未解決」比的對象錯了。

## 四、逾期懸置

| 標記 | 行 | 到期 | 處置建議 |
|---|---|---|---|
| ⟨Q-02⟩ internet-court-skill | L92 | 2026-09-18 | 本輪未查（GitHub Search 單一來源）；交設計者判斷該列去留時一併處理，不得靜默刪 |
| 其餘 1 筆逾期 | 由健檢卡盤點 | | 待健檢卡交件後補查 |

## 五、給設計者三句

1. 這頁的病不是版面，是**「官方對應」欄沒有人定期對官方一手**——14 列裡至少 5 列今天是錯的，而且錯的方向一致（低估官方）；任何新設計都要先回答「這一欄誰、多久、拿什麼對一次」，lint 步驟要能直接跑 `gh issue view` 與 CHANGELOG grep。
2. issue 數字（留言數、讚數）是快變事實又沒有看守，關閉狀態比數字重要十倍；建議狀態欄寫 OPEN／CLOSED（日期＋官方怎麼答），數字退場或只留量級。
3. AGENTS.md 列從「全站讚數之最的未解缺口」變成「已解，附三個邊界」，這會連動 index 鉤子、claude-code 已知問題、community-tech-tools 等至少 10 頁（`grep -l AGENTS.md wiki/`）——屬事實更正必回掃，跨維護者的走轉知帳本。
