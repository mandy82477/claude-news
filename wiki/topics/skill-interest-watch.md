---
page: "topics/skill-interest-watch"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-04"
last_news_update: "2026-10-04"
update_freq: "🗓️ 每日快照（機器產出；「本週竄升」以七日星數差計）"
status_main: "ongoing"
days_since_news: 1
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 1
inbound_links: 9
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群工具規模榜

**狀態：** ongoing
**開始日期：** 2026-09-02
**領域：** 🌐 社群
**更新頻率：** 🗓️ 每日快照（機器產出；「本週竄升」以七日星數差計）
**最後更新：** 2026-10-04
**最後新聞更新：** 2026-10-04

> **本頁是什麼**（快照 2026-10-04）
> - **這頁是什麼**：各類社群工具在 GitHub 上現在誰最大、本週誰在漲（6 類可用 GitHub 辨識，每日快照）。
> - **該裝哪個**：看 [[topics/community-tech-tools]]「我卡在這裡」決策表——有人判斷過，帶證據等級與判定日；那頁另有 126 列工具目錄。
> - **星數是規模不是品質**：本頁不做推薦；每類底下的「本庫判斷 →」直接連到那頁對應的症狀列。
> - **🧭**：該 repo 在社群工具目錄已有判斷，點過去看結論。

---

## 各類別：本庫判斷＋規模榜

| 欄 | 意思 |
|---|---|
| 本庫判斷 | 該類別對應的 tools 決策表症狀列，連過去看首選 |
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
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) 🧭 📰 | 216,815 | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's o… |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) 📰 | 12,826 | All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts… |
| [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | 6,074 | One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workf… |
| [gadievron/raptor](https://github.com/gadievron/raptor) | 3,858 | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By… |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 2,654 | Shared starter template configuration and CLAUDE.md memory bank system for Claude Code |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +1,323 | 216,815 |

### codebase 探索與理解（對應 [[topics/coding-workflow-guide]] 第 2a 段）

**本庫判斷 →** 見 [[topics/community-tech-tools]]「接手沒碰過的大 repo，agent 讀不懂」列

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) 🧭 📰 | 123,706 | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowle… |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) 🧭 📰 | 85,247 | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge grap… |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) 🧭 📰 | 73,175 | Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gem… |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 45,786 | High-performance code intelligence MCP server. Indexes codebases into a persistent knowle… |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 31,429 | Build Real-Time Knowledge Graphs for AI Agents |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +1,903 | 123,706 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1,007 | 73,175 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +931 | 85,247 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +762 | 45,786 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | +591 | 6,913 |

### 規劃與拆解（對應 [[topics/coding-workflow-guide]] 第 3 段）

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 71,032 | Spec-driven development (SDD) for AI coding assistants. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) 📰 | 64,384 | A light-weight and powerful meta-prompting, context engineering and spec-driven developme… |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | 7,778 | A powerful meta-prompting, context engineering and spec-driven development system that en… |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | 5,466 | Agent OS is a system for injecting your codebase standards and writing better specs for s… |
| [Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | 4,302 | A Model Context Protocol (MCP) server that provides structured spec-driven development wo… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +556 | 71,032 |

### 實作期攔錯（hook／lint／型別）（對應 [[topics/coding-workflow-guide]] 第 4 段）

**本庫判斷 →** 見 [[topics/community-tech-tools]]「CLAUDE.md 寫了它不聽」列

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### Code review（對應 [[topics/coding-workflow-guide]] 第 5 段）

**本庫判斷**：本類本庫不推薦單一工具——官方 `/code-review`、ultra、GitHub App 等六個入口與明價，見 [[topics/coding-workflow-guide]] 第 5 段；社群面做法（Read-Only Reviewer、跨模型互審）見 [[topics/community-tech-patterns]]

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 測試與驗證（含 evidence-gated done）（對應 [[topics/coding-workflow-guide]] 第 6 段）

**本庫判斷 →** 見 [[topics/community-tech-tools]]「它說做完了，但根本沒做」列

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 除錯與靜默失敗偵測（對應 [[topics/coding-workflow-guide]] 第 9 段）

**本庫判斷**：「感覺變笨，想先量測歸因」目前沒有成熟到可推薦單一工具，量測起點與訊號群見 [[topics/code-quality-decline]]

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### 規則維護不腐爛（CLAUDE.md 跟上改動）（對應 [[topics/coding-workflow-guide]] 第 8 段）

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [steipete/agent-rules](https://github.com/steipete/agent-rules) | 5,682 | Rules and Knowledge to work better with agents such as Claude Code or Cursor |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | 4,980 | AI-Driven Life Cycle (AI-DLC) adaptive workflow steering rules for AI coding agents |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | 4,408 | Rules for an AI coding agent to filter out generic AI-generated UI designs, text, and cod… |
| [WorldFlowAI/everything-claude-code](https://github.com/WorldFlowAI/everything-claude-code) | 4,005 | Claude Code toolkit - agents, commands, skills, rules, and hooks for productive AI-assist… |
| [dromara/liteflow](https://github.com/dromara/liteflow) | 3,877 | Lightweight, fast, stable, programmable component-based rule engine — where AI Agents orc… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | +1,224 | 3,479 |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +552 | 4,408 |
| [WorldFlowAI/everything-claude-code](https://github.com/WorldFlowAI/everything-claude-code) | +358 | 4,005 |

## B. 治理（管 agent 的需求）

### multi-agent orchestration

**本庫判斷 →** 見 [[topics/community-tech-tools]]「多個 agent 在同一 repo 互相覆蓋」；「一堆 agent 在跑，看不到誰卡住」列

> 同名提醒：決策表首選已改名 ness（ness-dev/ness，原名 Harness，多 worktree 並行管理）；榜上的 revfactory/harness（設計 agent team 的 meta-skill）不是同一個專案，裝前認清 owner。

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) 📰 | 84,769 | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with yo… |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | 33,449 | OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much mor… |
| [revfactory/harness](https://github.com/revfactory/harness) | 9,118 | A meta-skill that designs domain-specific agent teams, defines specialized agents, and ge… |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | 8,399 | Project management skill system for Agents that uses GitHub Issues and Git worktrees for… |
| [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | 6,627 | Enterprise-grade, local-first Agent Workbench for people and agent teams. A unified multi… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) | +5,438 | 84,769 |
| [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | +454 | 5,092 |

### git／commit 衛生自動化

**本庫判斷 →** 見 [[topics/community-tech-tools]]「多個 agent 在同一 repo 互相覆蓋」列

規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。

### LLM 知識庫／文件策展／知識傳承

**本庫判斷**：本庫尚無判斷（榜上無 🧭 條目）——星數不是推薦，裝前自行查證

| 目前前 5 | ★ | 一句話 |
|---|---|---|
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 31,986 | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomou… |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 27,685 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations,… |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,194 | LLM Wiki is a cross-platform desktop application that turns your documents into an organi… |
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) 📰 | 15,344 | Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude re… |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 15,097 | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with… |

| 本週竄升 | 七日增量 | ★ 現值 |
|---|---|---|
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | +1,476 | 31,986 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +376 | 27,685 |

---

## 參考來源

- 該裝哪個（決策表與判斷）：[[topics/community-tech-tools]]（每週整理）
- 規模榜：GitHub Search API（依星數排序，每日快照）；「本週竄升」以本庫每日記錄的星數差計算，保留 60 天
- 類別與搜尋條件由維護者校準（每條 query 上線前實測命中；找不到有辨識力 query 的類別只印判斷，不掛空榜）
