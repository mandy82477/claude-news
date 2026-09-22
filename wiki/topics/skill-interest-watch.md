# 興趣類別 skill 總覽

**狀態：** ongoing
**開始日期：** 2026-09-02
**領域：** 🌐 社群
**更新頻率：** 🗓️ 每日快照（機器產出；決策表抄自社群工具目錄、最多落後一天；「本週竄升」以七日星數差計）
**最後更新：** 2026-09-22
**最後新聞更新：** 2026-09-22

> **本頁是什麼**（快照 2026-09-22）
> - **該裝哪個**：看「我卡在這裡」決策表——有人判斷過，帶證據等級與判定日。
> - **這一類現在誰大、本週誰在漲**：看 GitHub 每日規模榜（6 類可用 GitHub 辨識）。
> - **星數是規模不是品質**：榜不做推薦，推薦只看決策表；榜上標 🧭 者代表決策表或工具目錄已有判斷。
> - 完整證據、推薦細節、Skills 速查與 113 列工具目錄在 [[topics/community-tech-tools]]。

---

## 我卡在這裡（決策表）

本表每日同步自 [[topics/community-tech-tools]]（判斷與證據的家；改判斷請改那頁），同步日 2026-09-22。

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 帳單爆了，看不到錢花在哪 | ⌨️ [**tare**](https://github.com/kelviq/tare) | 要桌面常駐、不想開終端 → 🖥️ [TokenEater](https://github.com/AThevon/TokenEater)（僅 macOS）；想比較多個 coding agent 的花費 → 🖥️ [Frugal Tokens](https://github.com/dpclark4/frugal-tokens) | 🟡（判 08-27｜查 09-22，287★） |
| 額度快用完，想在斷線前被提醒 | ⌨️ [**Claude-Code-Usage-Monitor**](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 要跨平台、作者還在更新 → ⌨️ [claude-usage-widget](https://github.com/bozdemir/claude-usage-widget)（53★）；用 Windows、想自己設到幾 % 就叫你 → 🖥️ [usage-monitor-for-claude](https://github.com/jens-duttke/usage-monitor-for-claude) | ⚪（判 09-22｜查 09-22，8,713★、07-05 後未更新） |
| context 一直被工具輸出撐爆 | 🔌 [**pxpipe**](https://github.com/teamchong/pxpipe) | 不能接受請求過代理層 → 🧩 [Graft](https://github.com/trailhq/Graft)（數字有爭議，見細節）；還不確定是誰在撐爆 → 先跑 ⌨️ [PrismoDev](https://github.com/shanirsh/prismodev) 診斷 | 🟡（判 08-05｜查 09-22，7,426★） |
| 接手沒碰過的大 repo，agent 讀不懂 | 🧩 [**graphify**](https://github.com/Graphify-Labs/graphify) | 要讓**人**看懂而非 agent → [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)；要把架構畫成圖交付 → [archify](https://github.com/tt-a1i/archify)；改 code 要索引自動同步 → [codegraph](https://github.com/colbymchenry/codegraph) | 🟢（判 05-02 起多來源｜查 09-22，12.0 萬★） |
| 每開新 session 都要重講一遍 | ⌨️ [**brain.md**](https://github.com/mindmuxai/brain.md) | 要團隊共享而非單機 → 🖥️ [OzBrain](https://ozbrain.com)（付費服務）；已在用 Obsidian → VIR | 🟡（判 08-25｜查 09-22，552★） |
| 多個 agent 在同一 repo 互相覆蓋 | 🖥️ [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 已經用 worktree 隔離、只差 commit 落地不打架 → 🧩 [Claude Code Merge Queue](https://github.com/funador/claude-code-merge-queue)；要跨 harness 統一協作邏輯 → [omnigent](https://github.com/omnigent-ai/omnigent) | 🟢（判 04-29 起多來源｜查 09-22，99★） |
| 一堆 agent 在跑，看不到誰卡住 | ⌨️ [**Omar**](https://github.com/omar-os/omar) | 只跑 3–5 個、不想多花一毛 token → [HUD](https://github.com/adrida/hud-mode)（走官方 event stream）；要 GUI 主控台 → 🖥️ [episko](https://github.com/respeak-io/episko)（原名 Cockpit） | 🟡（判 05-02｜查 09-22，48★） |
| 它說做完了，但根本沒做 | 🧩 [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 要留可稽核證據給團隊審 → [Proof Loop](https://github.com/LeoStehlik/proof-loop)（建構者／驗證者分離） | 🟡（判 04-27｜查 09-22，7★） |
| CLAUDE.md 寫了它不聽 | —（答案是機制不是工具，見細節） | 規則多到耗 token → Writ；跨工具設定碎片化 → Caliber | —（這一列沒有工具可評，理由見細節） |
| 不想被單一供應商綁死 | 🔌 [**Workweave Router**](https://github.com/weave-os/router) | 只想改用本地模型、不動主配置 → claudely；想繞過計量計費 → clarp（⚠️ 政策風險，見細節） | 🟡（判 06-27｜查 09-22，4,735★） |

**圖例**——證據：🟢 多來源實測／🟡 單一實測（多為作者自測）／⚪ 僅星數。括號裡兩個日期：**判**＝下這個判斷的那天，**查**＝最近一次確認這個專案還在不在、多大的那天；判很舊而查很新，代表結論是舊的但專案還活著，要拿它做決定前自己再看一眼 repo。安裝：🧩 skill/plugin（一行安裝隨時可拔）／⌨️ CLI／🖥️ 桌面 app（注意平台鎖定）／🔌 proxy·MCP（**流量過第三方層，裝前先評估安全**）。

---

## 各類別：本庫判斷＋規模榜

| 欄 | 意思 |
|---|---|
| 本庫判斷 | 該類別對應的決策表列（同上表，就近重印方便對照） |
| 目前前 5 | 該類別 GitHub 搜尋命中的 repo 依星數排序，星數為快照當日值 |
| 本週竄升 | 七日內星數增量 ≥ 200 者，依增量排序；資料來自本庫每日記錄的星數 |
| 📰 | 本庫日報已報導過 |
| 🧭 | 決策表或工具目錄已有判斷 |

> 榜依 GitHub 描述機械比對，偶有跨類誤收（同一 repo 出現在兩類、或非本類工具混入）；星數與分類皆非推薦。

## A. 開發實務（按流程階段，對應 [[topics/coding-workflow-guide]]）

### 專案設定／CLAUDE.md 生成（對應 [[topics/coding-workflow-guide]] 第 1 段）

**本庫判斷**：標 🧭 者的判斷見 [[topics/community-tech-tools]] Skills 速查或工具目錄

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) 🧭 📰 | 214,625 | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's o… |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) 📰 | 12,738 | All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts… |
| [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | 6,050 | One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workf… |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3,813 | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By… |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 2,638 | Shared starter template configuration and CLAUDE.md memory bank system for Claude Code |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +1,485 | 214,625 |
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | +263 | 1,694 |

### codebase 探索與理解（對應 [[topics/coding-workflow-guide]] 第 2a 段）

**本庫判斷**（同頁首決策表對應列）

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 接手沒碰過的大 repo，agent 讀不懂 | 🧩 [**graphify**](https://github.com/Graphify-Labs/graphify) | 要讓**人**看懂而非 agent → [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)；要把架構畫成圖交付 → [archify](https://github.com/tt-a1i/archify)；改 code 要索引自動同步 → [codegraph](https://github.com/colbymchenry/codegraph) | 🟢（判 05-02 起多來源｜查 09-22，12.0 萬★） |

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) 🧭 📰 | 120,443 | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowle… |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) 🧭 📰 | 83,718 | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge grap… |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) 🧭 📰 | 71,809 | Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gem… |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 44,156 | High-performance code intelligence MCP server. Indexes codebases into a persistent knowle… |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 31,076 | Build Real-Time Knowledge Graphs for AI Agents |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +3,504 | 120,443 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +842 | 71,809 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +816 | 44,156 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +790 | 83,718 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +211 | 15,137 |

### 規劃與拆解（對應 [[topics/coding-workflow-guide]] 第 3 段）

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) 📰 | 138,348 | 💫 Toolkit to help you get started with Spec-Driven Development |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 69,842 | Spec-driven development (SDD) for AI coding assistants. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) 📰 | 64,481 | A light-weight and powerful meta-prompting, context engineering and spec-driven developme… |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | 7,780 | A powerful meta-prompting, context engineering and spec-driven development system that en… |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | 5,438 | Agent OS is a system for injecting your codebase standards and writing better specs for s… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1,489 | 69,842 |
| [github/spec-kit](https://github.com/github/spec-kit) | +1,373 | 138,348 |

### 實作期攔錯（hook／lint／型別）（對應 [[topics/coding-workflow-guide]] 第 4 段）

**本庫判斷**（同頁首決策表對應列）

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| CLAUDE.md 寫了它不聽 | —（答案是機制不是工具，見細節） | 規則多到耗 token → Writ；跨工具設定碎片化 → Caliber | —（這一列沒有工具可評，理由見細節） |

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### Code review（對應 [[topics/coding-workflow-guide]] 第 5 段）

**本庫判斷**：本類本庫不推薦單一工具——官方 `/code-review`、ultra、GitHub App 等六個入口與明價，見 [[topics/coding-workflow-guide]] 第 5 段；社群面做法（Read-Only Reviewer、跨模型互審）見 [[topics/community-tech-patterns]]

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 測試與驗證（含 evidence-gated done）（對應 [[topics/coding-workflow-guide]] 第 6 段）

**本庫判斷**（同頁首決策表對應列）

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 它說做完了，但根本沒做 | 🧩 [**Groundtruth**](https://github.com/vnmoorthy/groundtruth) | 要留可稽核證據給團隊審 → [Proof Loop](https://github.com/LeoStehlik/proof-loop)（建構者／驗證者分離） | 🟡（判 04-27｜查 09-22，7★） |

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 除錯與靜默失敗偵測（對應 [[topics/coding-workflow-guide]] 第 9 段）

**本庫判斷**：「感覺變笨，想先量測歸因」目前沒有成熟到可推薦單一工具，量測起點與訊號群見 [[topics/code-quality-decline]]

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 規則維護不腐爛（CLAUDE.md 跟上改動）（對應 [[topics/coding-workflow-guide]] 第 8 段）

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [steipete/agent-rules](https://github.com/steipete/agent-rules) | 5,682 | Rules and Knowledge to work better with agents such as Claude Code or Cursor |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | 4,761 | AI-Driven Life Cycle (AI-DLC) adaptive workflow steering rules for AI coding agents |
| [dromara/liteflow](https://github.com/dromara/liteflow) | 3,866 | Lightweight, fast, stable, programmable component-based rule engine — where AI Agents orc… |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3,813 | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By… |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | 3,529 | Rules for an AI coding agent to filter out generic AI-generated UI designs, text, and cod… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [shadcn-ui/lint](https://github.com/shadcn-ui/lint) | +978 | 2,517 |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +902 | 3,529 |
| [WorldFlowAI/everything-claude-code](https://github.com/WorldFlowAI/everything-claude-code) | +507 | 3,460 |

## B. 治理（管 agent 的需求）

### multi-agent orchestration

**本庫判斷**（同頁首決策表對應列）

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 多個 agent 在同一 repo 互相覆蓋 | 🖥️ [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 已經用 worktree 隔離、只差 commit 落地不打架 → 🧩 [Claude Code Merge Queue](https://github.com/funador/claude-code-merge-queue)；要跨 harness 統一協作邏輯 → [omnigent](https://github.com/omnigent-ai/omnigent) | 🟢（判 04-29 起多來源｜查 09-22，99★） |
| 一堆 agent 在跑，看不到誰卡住 | ⌨️ [**Omar**](https://github.com/omar-os/omar) | 只跑 3–5 個、不想多花一毛 token → [HUD](https://github.com/adrida/hud-mode)（走官方 event stream）；要 GUI 主控台 → 🖥️ [episko](https://github.com/respeak-io/episko)（原名 Cockpit） | 🟡（判 05-02｜查 09-22，48★） |

> 同名提醒：決策表首選已改名 ness（ness-dev/ness，原名 Harness，多 worktree 並行管理）；榜上的 revfactory/harness（設計 agent team 的 meta-skill）不是同一個專案，裝前認清 owner。

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) 📰 | 75,342 | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with yo… |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | 33,316 | OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much mor… |
| [revfactory/harness](https://github.com/revfactory/harness) | 9,050 | A meta-skill that designs domain-specific agent teams, defines specialized agents, and ge… |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | 8,381 | Project management skill system for Agents that uses GitHub Issues and Git worktrees for… |
| [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | 6,558 | Enterprise-grade, local-first Agent Workbench for people and agent teams. A unified multi… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) | +6,064 | 75,342 |
| [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | +1,291 | 4,403 |
| [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +455 | 6,558 |
| [yetone/cumora](https://github.com/yetone/cumora) | +241 | 3,846 |

### git／commit 衛生自動化

**本庫判斷**（同頁首決策表對應列）

| 我的症狀 | 先裝這個 | 什麼時候改裝別的 | 證據 |
|---|---|---|---|
| 多個 agent 在同一 repo 互相覆蓋 | 🖥️ [**ness**](https://github.com/ness-dev/ness)（原名 Harness） | 已經用 worktree 隔離、只差 commit 落地不打架 → 🧩 [Claude Code Merge Queue](https://github.com/funador/claude-code-merge-queue)；要跨 harness 統一協作邏輯 → [omnigent](https://github.com/omnigent-ai/omnigent) | 🟢（判 04-29 起多來源｜查 09-22，99★） |

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### LLM 知識庫／文件策展／知識傳承

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 27,142 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations,… |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 19,862 | LLM Wiki is a cross-platform desktop application that turns your documents into an organi… |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) 📰 | 15,137 | Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude re… |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 15,017 | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with… |
| [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) 📰 | 4,283 | Beautiful, AI-native markdown IDE and LLM wiki |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +382 | 27,142 |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +307 | 19,862 |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +211 | 15,137 |

---

## 參考來源

- 決策表與判斷：[[topics/community-tech-tools]]（每週整理；本頁每日同步）
- 規模榜：GitHub Search API（依星數排序，每日快照）；「本週竄升」以本庫每日記錄的星數差計算，保留 60 天
- 類別與搜尋條件由維護者校準（每條 query 上線前實測命中；找不到有辨識力 query 的類別只印判斷，不掛空榜）
