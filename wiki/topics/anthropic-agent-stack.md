---
page: "topics/anthropic-agent-stack"
kind: "topic"
status: "ongoing"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-18"
last_news_update: "2026-09-18"
status_main: "ongoing"
days_since_news: 1
parent: null
children: "['entities/managed-agents']"
page_role: "hub"
days_since_news_subtree: 1
inbound_links: 7
attribution_count: 4
attribution_last: "2026-09-10"
top_source: "user-query"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 官方 agent 積木：為什麼有它、讓你多做出什麼

**狀態：** ongoing
**領域：** 🛠️ 工具/功能
**別名：** agent stack, dynamic workflows, agent teams, cross-session messaging, agent view, self-hosted runner
**開始日期：** 2026-09-10
**最後更新：** 2026-09-18
**最後新聞更新：** 2026-09-18

> **這頁在回答什麼**
> 官方把 agent 拆成八塊積木。每一塊這裡答三件事：沒有它之前你卡在哪、官方多給了什麼（附可貼上就跑的最小指令）、它現在還做不到什麼。

> **最近變動**（2026-09-18）
> Claude Code Projects 進入 Beta（六家科技媒體 2026-09-17 同日報導，官方文件索引新增專頁），描述為協調多個 agent 執行緒、關閉筆電後仍持續運作的雲端並行 session；是否構成第九塊積木、與既有 agent view／Managed Agents 的分界，待官方文件內容查證後補卡，詳見 [[entities/claude-code]]「近期平台與文件異動」。

---

## 摘要

官方 agent 積木在 2026 年中補上編排這一塊：dynamic workflows 讓計畫從 Claude 的逐回合判斷變成一支可存檔重跑的 script——先前分身之間只能互傳純文字、訊息不帶依賴語意，排不出誰先誰後。本頁把八塊積木一塊一塊拆開，每塊答「為什麼有它、讓你多做出什麼、還做不到什麼」；八塊怎麼疊、怎麼挑各有一節，原本的五種形態速查表與六層架構收在頁尾附錄。想知道「我現在在開發流程的哪一步、該下哪個」，那是流程視角，見 [[topics/coding-workflow-guide]]；Managed Agents 這個平台產品本身的現況、計費算式與零件成熟度在子頁 [[entities/managed-agents]]。

---

## 八個積木：為什麼出、讓你多做出什麼

按你多半會撞上的順序排。指令與 prompt 都取自官方文件，可以直接貼上改字。社群拿這些積木玩出什麼配置，逐則記錄在 [[topics/community-tech-patterns]]，本頁不重述。

### 一、`/goal`：讓它自己跑到條件成立

- **沒有它之前**：每一回合你都得回來看一眼、再推它一把。官方給 `/goal` 的理由是：設一條完成條件後它自己往下跑，每回合結束由一個小而快的模型檢查條件成不成立——**判定完成的是另一個模型，不是做事的那個**。
- **官方多給了什麼**：四類事現在可以一句話丟出去——把一個模組遷移到所有呼叫點都編得過且測試綠、照設計文件實作到驗收條件全數成立、把大檔案拆到每個都在體積預算內、把某個標籤的 issue backlog 清空。最小指令：

```
/goal all tests in test/auth pass and the lint step is clean
claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"
```

  條件上限 4,000 字元，可加 `or stop after 20 turns` 設界，`/goal clear` 取消（[官方文件](https://code.claude.com/docs/en/goal)，2026-09-12 查證）。

- **還做不到什麼**：跨 session 只帶條件不帶進度：resume 會還原未完成的 goal，但回合數、計時與 token 基線歸零。回合結束時若還有 subagent 或背景 shell 在跑，那一回合的檢查會被跳過，等下一回合再判。

### 二、內建 subagent：把吵雜的活丟進另一個 context

- **沒有它之前**：一件旁支工作會把搜尋結果、log、你不會再看第二眼的檔案內容全倒進主對話。官方的說法是讓 subagent 在自己的 context 裡做完，只把摘要交回來。
- **官方多給了什麼**：三種情況官方點名用它——輸出很囉嗦但主對話用不到、要限制它只能碰哪些工具、工作自成一段只需回一份摘要。它也可以續用（下面第二、三行就是官方的續用範例，照抄改字即可），角色檔還能當整個 session 的身分：

```
claude --agent code-reviewer --name reviewer-1
Use the code-reviewer subagent to review the authentication module
Continue that code review and now analyze the authorization logic
```

（`--name` 自取）

  `--agent`（v2.0.59 起）讓角色檔 body 整段取代預設 system prompt、resume 後身分保留；搭 `--name` 就成了一位長駐領域專家——別的 session 用傳訊丟任務給他、隔天 `--continue` 接續，context 不歸零（[官方 sub-agents 文件](https://code.claude.com/docs/en/sub-agents)，2026-09-12 查證）。

- **還做不到什麼**：Explore 與 Plan 唯讀、一次性不能追問，且會跳過 CLAUDE.md 與上層 session 的 git status（官方明說只有這兩個省略）；Explore 的模型繼承主對話、在 Claude API 上以 Opus 為上限，要來回追問改用 `general-purpose`。**subagent 裡開不了 workflow**。

### 三、Dynamic workflows：把編排寫成一支可重跑的 script

- **沒有它之前**：用 subagent、skills、agent teams 時，計畫握在 Claude 手上——它逐回合決定下一個派誰，而且每一份結果都落進 context 視窗。官方那句判斷式是「**計畫握在誰手上**」：workflow 把迴圈、分支與中間結果都收進 script 自己，主對話只拿到最終答案。
- **官方多給了什麼**：六個可以逐字抄的 prompt——

```
use a workflow to audit every route handler under src/routes/ for missing authentication checks, and adversarially verify each finding
use a workflow to run npx tsc --noEmit and keep fixing the reported errors until the type check passes or two rounds in a row make no progress
use a workflow to migrate every component from JS to TS, each file in its own isolated copy
use a workflow to review every file changed in this PR then merge into one ranked summary
use a workflow to research how three competitors handle rate limiting in parallel then compare
use a workflow to find flaky tests: run the suite repeatedly, stop once two rounds find nothing new
```

  怎麼叫它：prompt 帶 `ultracode`（觸發關鍵字，v2.1.160 起取代原本的 `workflow`）或直說 use a workflow；`/effort ultracode` 讓 Claude 自己決定每個實質任務要不要開；內建範例 `/deep-research`。

- **一支最小 script**：存成專案的 `.claude/workflows/audit-routes.js`（只給自己用就放 `~/.claude/workflows/`），`meta.name` 就是指令名，用 `/audit-routes` 叫它跑、`/workflows` 看進度。形狀取自官方 `audit-routes` 範例：

```js
export const meta = {
  name: 'audit-routes',
  description: 'Audit every route handler for missing auth checks',
}

const found = await agent('List every .ts file under src/routes/.', {
  schema: { type: 'object', required: ['files'], properties: { files: { type: 'array', items: { type: 'string' } } } },
})

const audits = await pipeline(found.files, file =>
  agent(`Audit ${file} for missing authentication checks.`, { label: file }),
)

return audits.filter(Boolean)
```

  `agent()` 派一個，`pipeline()` 逐項流水，`parallel()` 齊發等全收，`phase()` 在進度畫面分組；四者是 script 裡直接可用的全域函式，不用 import。被停掉或 API 錯的 agent 回 `null`，所以最後 `.filter(Boolean)`。（官方 workflows 頁「What the saved script looks like」節，2026-09-12 查證）

- **還做不到什麼**：上限 16 路並行（v2.1.269 起可用 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 提到 256）、單次 1,000 agent、`parallel()`／`pipeline()` 單次 4,096 項；**跑到一半不能等你輸入**，裡面也開不了 agent teams。

### 四、Agent teams：讓分身互相質疑

- **沒有它之前**：subagent 是派出去、回報、結束，分身之間沒有通道。官方的分界句是：需要快速、聚焦、做完就回報的工人用 subagent；需要隊友之間交換發現、互相質疑、自己協調時才用 agent teams。官方同時先勸退一句——**開團隊之前先確認輕一點的做法是不是就夠了**。
- **官方多給了什麼**：四類場景（研究與審查／新模組或新功能／有競爭假說的除錯／跨層協調），建議 3–5 位起步。兩個可以逐字抄的 prompt：

```
Spawn three teammates to review PR #142:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```
```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific debate.
Update the findings doc with whatever consensus emerges.
```

  怎麼打開：環境變數 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`（v2.1.32 起的研究預覽，官方註明很吃 token）。

- **還做不到什麼**：實驗性、預設關閉；`/resume` 不還原行程內的 teammate、一個 session 只能有一個 team、不可巢狀、`-p` 之下不會派出 teammate。

### 五、跨 session 傳訊：讓另一個終端機的 session 回你話

- **沒有它之前**：官方的說法是——一個 session 改的東西弄壞了另一個 session 正在蓋的，你不會馬上知道；一個 session 已經解掉的問題，另一個還卡在那裡。
- **官方多給了什麼**：四類用法（交接一項發現／協調平行 worktree／問長時間工作跑到哪／跨機器傳話）。三個可以逐字抄的 prompt：

```
Ask the session running in my other terminal whether the migration finished
Let @api-worker know the schema migration finished
Tell me when the migration session finishes what it's working on
```

  `ListAgents` 找得到誰在線、`SendMessage` 點名傳（macOS／Linux v2.1.224 起、原生 Windows v2.1.234 起）；第三句是閒置通知 `notify_when_idle`（v2.1.236 起）。同機走本機 socket，跨機器經 Anthropic 伺服器轉送。

- **還做不到什麼**：只傳純文字，不傳對話歷史與檔案，訊息也不帶依賴語意——要排誰先誰後得靠 workflow。
- **跟 agent teams 怎麼分**：官方寫得很直接——隊友是 Claude 派出並監督的，用 agent teams；兩個都是你自己開、自己指揮的 session，才用跨 session 傳訊。
- **當初的需求工單對上多少**：那張工單（[issue #24798](https://github.com/anthropics/claude-code/issues/24798)，已關閉、84 則留言）要的三件事裡，官方對上的是跨 session 傳訊與閒置通知，「共用專案暫存區」至今沒有對應品；協定級的 agent 互通（A2A）仍是未回應的功能請求（[issue #28300](https://github.com/anthropics/claude-code/issues/28300)）。

### 六、Agent view：把幾件互不相干的事丟出去，回頭再看

- **沒有它之前**：官方的說法是——手上有好幾件彼此獨立、不需要你盯著每一步的事時，你只能一個一個開視窗顧。
- **官方多給了什麼**：派出去之後，一個畫面看所有 session 是在跑、卡著等你、還是有結果了。官方舉的例子是把一個 bug 修復、一次 PR 審查、一樁 flaky test 調查當成三列丟出去，回頭再看：

```
claude --bg "investigate the flaky SettingsChangeDetector test"
claude agents
```

  背景 session 要改檔前會自動搬進 `.claude/worktrees/` 隔離，不會踩到你正在編輯的工作目錄。

- **還做不到什麼**：仍是研究預覽（v2.1.139 起）。官方文件給它的定位是丟工作出去與看板，沒有寫它自己能排先後或彙整結果——那兩件事在 workflow 那一塊。

### 七、Managed Agents：不必自己蓋 agent 迴圈

- **沒有它之前**：要把 Claude 當自主 agent 跑在自己的服務裡，你得自己蓋 agent 迴圈、工具執行與執行環境。官方給 Managed Agents 的理由就是這一句的反面：這些由平台代管，你拿到的是一套完整託管的執行環境。
- **官方多給了什麼**：六條官方點名的時機——一跑就是數分鐘到數小時、要雲端沙箱、為法遵要自架沙箱、不想維運基礎設施、要有持久檔案系統與歷史的有狀態 session、排程（cron）執行。它不是 CLI 指令而是平台 API：帳號預設可用，請求帶 `managed-agents-2026-04-01` beta header 即可開始。
- **還做不到什麼**：整包仍是 beta，十個零件裡只有 `/goal` 到正式發布，MCP 隧道與 Dreaming 是須另外申請的研究預覽。計費算式、各零件成熟度與第三方使用回饋都在子頁 [[entities/managed-agents]]。

### 八、Self-hosted runner：把執行搬回自己控制的機器

- **沒有它之前**：官方的說法是——網路、工具或法遵要求讓你必須把 session 的執行留在自己控制的基礎設施上時，雲端執行這條路走不通。
- **官方多給了什麼**：三件事——連得到內網（雲端 session 要碰內部資料庫、私有 registry）、帶得動自己的工具（runner image 預裝內部 CLI）、滿足法遵。一行指令把自己的機器或容器變成 Claude Code 網頁版、行動版與桌面版 session 的執行地：

```
claude self-hosted-runner
```

- **還做不到什麼**：public beta、預設關閉，只有 Team 與 Enterprise 方案開得了（v2.1.224 起）。

---

## 這八塊怎麼疊

「subagent 加 workflows」這個「加」字的答案在這裡。官方文件說得出口的只有這四條（2026-09-12 查證），其餘組合（含 agent teams 能不能搭跨 session 傳訊合用）官方沒寫，本頁不猜：

- **workflow 裡的 agent 可以再派 subagent**：主對話以下最多三層，層數由 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 控制。
- **`/goal` 的 session 可以啟 workflow**：回合結束時若背景工作還在跑，那一回合的完成檢查會被跳過，不會誤判成沒達標。
- **subagent 裡開不了 workflow**：`Workflow` 這個工具一律從 subagent 的工具池移除。
- **workflow 裡開不了 agent teams**：teammate 不可巢狀，`-p` 與 SDK session 也不會派出 teammate；workflow 跑到一半也不能等你輸入。

---

## 你該用哪個

官方總覽頁用三個問題分流，照順序問自己：

1. **誰來協調？** 在同一個對話裡派出去、收回來 → 內建 subagent；丟出去、晚點回來看 → agent view；要 Claude 規劃、分派、盯著跑 → agent teams；計畫握在一支 script 手上 → dynamic workflows。
2. **這些工人需不需要互相講話？** 不需要 → subagent 就夠；需要交換發現、互相質疑 → agent teams；只是要問另一個 session 一句話 → 跨 session 傳訊。
3. **它們會不會碰到同一批檔案？** 會 → 用 worktree 隔離（背景 session 會自動搬進 `.claude/worktrees/`）。

要跑數小時以上、跨 session 保留狀態，或資料不出境，那是另一條分支：[[entities/managed-agents]]（平台代管）或 self-hosted runner（你自己的機器）。逐欄對照見下方附錄（[官方 agents 總覽](https://code.claude.com/docs/en/agents)，2026-09-12 查證）。

---

## 附錄：五種形態速查表

上面三個問題答不出來時，用這張表逐欄對號。

| 選項 | 選它的分界（可自我對號） | 跨 session 記憶／執行位置 | 計費走哪條 | 現在拿得到嗎 |
|------|------|------|------|------|
| `/goal`（Claude Code 內建） | 單一 session 內跑得完，且完成條件寫得成一條可執行檢查（如 `npm test` exits 0） | 無／你自己的機器 | 計入訂閱配額 | ✅ 正式發布（v2.1.139） |
| 內建 subagent（Explore／Plan／general-purpose） | 只是要把大量讀檔丟進獨立 context；Explore 唯讀、一次性、不能追問 | 無／你自己的機器 | 計入訂閱配額 | ✅ 正式發布 |
| **Dynamic workflows** | 一件事要幾十個 agent（全庫掃描、大規模遷移、交叉查證），或要把編排寫成可重跑的 script | 同一 session 內可續跑（已完成 agent 吃快取）／你自己的機器，背景執行 | 計入訂閱配額（多 agent 倍增） | ✅ 全部付費方案（Pro 需在 `/config` 開啟） |
| **Managed Agents** | 要跑數小時以上並跨 session 保留狀態，或需 20 路並行、資料不出境 | 有（持久記憶）／Claude Platform，企業可自架沙箱 | token 牌價另計 session 執行時數，算式見 [[entities/managed-agents]] | ⚠️ beta；十個零件只有 `/goal` 正式發布 |
| Agent SDK | 要把 agent 包進自己的產品或 CI，自己控制迴圈 | 由你自己實作／你自己的基礎設施 | 計入訂閱配額，細節見 [[entities/pricing]] | ✅ 正式發布；版本下限見 [[entities/claude-code]] |

- **成本對照的唯一第三方數字，本庫未採信**：2026-09-03 一則 Reddit 貼文宣稱以同一模型跑自建開源框架，準確度與 Managed Agents 打平、成本低最多 75%，但未附測試方法與資料集，屬單一未驗證宣稱，不列入上表（[原文](https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/)）。
- **社群自組替代**：Opus 決策層＋OpenCode 執行層的自組架構（Reddit 開發者 70 天實戰，2026-05-11）仍是可行選擇，核心結論是任務簡報品質決定成敗；與官方框架的對照見 [[topics/official-community-gap]]。

---

## 附錄：六層架構怎麼疊起來

上面八塊是一塊一塊看，這一節換個角度：按架構層級排，一層比一層外——你多半從第一層開始，撞到牆才往下一層走。層是可疊加的能力，同一套系統可以同時用好幾層；每層的官方細節在上面對應的積木卡，這裡只留位置與互動模式。社群在各層玩出的具體配置（147 個 subagent 的移植、殭屍 agent 偵測、Concord、cumora、brain.md、OzBrain、meta-harness），逐則記錄在 [[topics/community-tech-patterns]]。

1. **一個 agent 把事做完**（`/goal`）——沒有 agent 之間的互動可言，只有你和它。社群在這一層玩的是自主度邊界，不是架構。
2. **開分身，但分身彼此不講話**（內建 subagent、Managed Agents 的 20 路並行子代理、agent view）——**單向扇出**：主 agent 分配、收回結果，分身之間沒有通道，所以不會協調也不會互相覆蓋，代價是重複工作。
3. **把編排寫成程式**（dynamic workflows）——**依 script 排定的依賴順序流動**：上游 agent 的輸出直接成為下游的輸入，也能讓獨立 agent 對抗式互審彼此的發現再回報。判斷式：**這個編排下週還會照原樣再跑一次嗎？** 會就寫成 workflow 存起來，不會就讓 Claude 臨場派 subagent。
4. **分身開始互相講話**（`ListAgents`＋`SendMessage`、agent teams）——**點對點傳訊**：只傳純文字，**傳訊層自身仍無編排**，要排先後仍得回到第三層。
5. **跨機器與跨工具**（self-hosted runner、MCP 隧道〔研究預覽，須申請〕、經 Remote Control 對另一台機器或網頁版 session 開話，v2.1.225 起）——跨機器的協定級互通（A2A）仍缺席。
6. **跨時間：狀態不隨 session 消失**（Managed Agents 的持久記憶〔beta〕與 Dreaming〔研究預覽，須申請〕；本機側的 `claude --resume` 與 subagent 續用）——**agent 與過去的自己互動**。

**穿過所有層的一件事：hooks。** `PreModelSwitch`／`PostModelSwitch`（v2.1.251）這類事件讓你在既有架構的接縫上插手——攔截、確認或標註，它本身不是新的一層。判斷式：**你要的是多一個 agent，還是要在現有 agent 的某個動作前後插一句話？** 後者用 hook，別開分身。

---

## 子頁怎麼分

| 頁 | 答什麼 | 最後動態 |
|------|------|------|
| 本頁 | 八塊官方積木各自為什麼出、讓你多做出什麼、怎麼疊、怎麼挑 | 2026-09-12 |
| [[entities/managed-agents]] | 代管平台這個產品本身：現況、計費算式、各零件成熟度、歷史 | 2026-09-11 |

---

## 相關實體

- [[entities/managed-agents]] — 代管平台產品（子頁）
- [[entities/claude-code]] — 各積木的版本與指令細節
- [[entities/pricing]] — 訂閱配額與各條計費規則
- [[feature-radar]] — 單則功能的熱度與試用價值
- [[topics/official-community-gap]] — 官方積木 vs 社群痛點的缺口矩陣
- [[topics/coding-workflow-guide]] — 「我在做這件事該用哪個」的流程視角
- [[topics/community-tech-patterns]] — 社群 multi-agent 做法的逐則記錄
- [[topics/community-large-codebase-workflow]] — 同一批積木被社群拿去跑大型 codebase 時的工作流主線（本頁講官方給了什麼零件，那頁講社群怎麼組）

---

## 時序

- 2026-09-10：建頁，選型表與積木架構自 [[entities/managed-agents]] 移入並增補；查證來源：[workflows](https://code.claude.com/docs/en/workflows)、[cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)、[agents 總覽](https://code.claude.com/docs/en/agents)。
- 2026-09-10：查證重點——dynamic workflows 全付費方案開放；跨 session 傳訊原生 Windows v2.1.234 起支援、閒置通知 v2.1.236 起；agent teams 仍為實驗性、預設關閉。
- 2026-09-11：anthropic-sdk-python v1.5.0 為 Managed Agents 新增 auto mode 工具權限設定，積木層級無變動（細節見 [[entities/managed-agents]]）。
- 2026-09-12：改以「一塊積木一張卡」重寫，補上八塊的官方存在理由與可貼上的指令、新增「怎麼疊」與官方三問決策樹；更正 `/goal` 官方專頁、MCP 隧道狀態（研究預覽須申請）與 issue #24798 現況（已關閉、84 則留言）。查證來源：[goal](https://code.claude.com/docs/en/goal)、[sub-agents](https://code.claude.com/docs/en/sub-agents)、[agent teams](https://code.claude.com/docs/en/agent-teams)、[managed agents](https://platform.claude.com/docs/en/managed-agents/overview)。
