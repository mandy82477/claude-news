---
page: "entities/managed-agents"
kind: "entity"
type: "feature"
status: "beta（所有 API 帳號預設可用，須帶 beta header）"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-20"
last_news_update: "2026-09-16"
status_main: "beta"
days_since_news: 6
parent: "topics/anthropic-agent-stack"
children: "['entities/managed-agents-archive']"
page_role: "hub+child"
days_since_news_subtree: 6
inbound_links: 31
attribution_count: 6
attribution_last: "2026-09-16"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Managed Agents

**類型：** feature
**狀態：** beta（所有 API 帳號預設可用，須帶 beta header）
**領域：** 🛠️ 工具/功能
**別名：** Anthropic Managed Agents, 受管代理
**上層：** [[topics/anthropic-agent-stack]]
**首次出現：** 2026-04-28
**最後更新：** 2026-09-20
**最後新聞更新：** 2026-09-16

> **最新動態**（2026-09-16）
> anthropic-sdk-python v1.6.0 再次擴充 auto mode 工具權限功能（09-11 v1.5.0 之後第二筆），官方原文於此處截斷，完整範圍與行為仍待官方文件補充。

---

## 現況

Anthropic Managed Agents 是 Claude Platform 上的官方 agent 框架（[概覽文件](https://platform.claude.com/docs/en/managed-agents/overview)）：持久記憶（含 Dreaming 記憶整合）、20 路並行子代理、Outcomes 規格驗證、Proactive Workflows、企業自架沙箱。**狀態為 beta**（自 2026-05-11 起，所有 API 帳號預設可用，須帶 `managed-agents-2026-04-01` beta header）——各零件成熟度不一：只有 `/goal` 已達正式發布，Dreaming 與 Agent View 仍是 research preview（Dreaming 另需申請並帶 `dreaming-2026-04-21` header），Proactive Workflows 與 Capability Curve 自 2026-05-18 公告後逾 100 天無進一步細節公布。Outcomes 讓規格文件成為執行時的強制依據（官方語「Specs become load-bearing」）。

實質新功能停在 2026-05-22；此後多筆為 SDK 版號擴充，多數官方 changelog 未列細節，2026-09-11 的 anthropic-sdk-python v1.5.0 首度列出具體項目——新增 auto mode 工具權限設定；2026-09-15 的 v1.6.0 再擴充同一功能線，原文同樣截斷，行為細節仍待官方文件補充。獨立第三方生產環境回饋至今為零——本頁引用到的兩則使用案例，一則用的是自組架構、一則來自 Claude Code 創始人。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 要跑數小時以上、跨 session 保留狀態的工作流；需要資料不出境（自架沙箱） |
| 不適合 | 單次 30 分鐘內做得完、或不需保留跨 session 狀態的任務——`/goal` 就夠 |

> 跨功能的熱度對比見 [[feature-radar]]；跟其他官方 agent 形態怎麼挑、八塊積木各自為什麼出，見上層 [[topics/anthropic-agent-stack]]。

**為什麼只剩 🔥🔥**：近四週（08-09～09-06）只被提到兩天——一次是 SDK 版號、一次是別人拿它當對照組——沒有任何正向採用回報，實質新功能停在 05-22。
%% 維運備忘：2026-09-05 頁面健檢一次性下修。量測：python scripts/news_mentions.py --since 4w --any "Managed Agents" "受管代理" → 命中 08-20（版號無細節）、09-03（負向對照）。現行「連續 4 週零命中 −1 格」對本頁降 0 格，故為編輯判斷；上限式判準是否成法見 docs/page-audits/ledger.md 待裁決。feature-radar L226 已同步。%%

---

## 怎麼計費

- **依模型 token 牌價**（快取乘數適用；session 內 web search 另計 $10／1,000 次；`inference_geo: "us"` 1.1×）＋ session runtime **$0.08／session-hour**（只計 `running` 狀態，取代 container-hour）。
- **計費例外與算例**：不適用 Batch 折扣與 partner 雲端平台；官方算例 Opus 5 跑 1 小時、50k 輸入／15k 輸出 ≈ **$0.705**（[定價文件](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)，2026-09-06 查證）。

---

## 接下來看什麼

- **等哪個訊號**：Agent View 從研究預覽升格、Proactive Workflows／Capability Curve 補上細節公告、出現第一則獨立生產環境回饋。三者任一發生，本頁的零件表與熱度就會變。
- **你的選項**：(a) 什麼都不做，先用 `/goal` 把單 session 的完成條件立起來；(b) 只在需要資料不出境時評估自架沙箱；(c) 想要跨 session 記憶又不想綁平台，先看社群自組架構——但目前唯一的成本數字未附方法。

---

## 各零件現在到哪

資料截至 2026-09-06（狀態每週複查，以 [[feature-radar]] 為準）。

| 功能 | 說明 | 狀態 |
|------|------|------|
| 持久記憶（Memory） | 跨 session 保留 agent 知識與狀態 | 公開測試 |
| Dreaming | 任務間隙自動整理記憶，類似睡眠記憶鞏固 | 研究預覽 |
| 20 路並行子代理 | 最高 20 個子代理同時執行 | 公開測試 |
| Outcomes 規格驗證 | Agent 自我驗證輸出是否符合規格文件 | 公開測試 |
| Agent View | 統一面板管理所有並行 session 即時狀態（`claude agents`） | 研究預覽 |
| `/goal` 指令 | fire-and-forget 自動化，小型快速模型驗證完成條件 | 正式發布（v2.1.139） |
| Proactive Workflows | Agent 可主動排程並自動觸發任務，不需人工輸入即可啟動 | 公告（細節待確認，公告後逾 100 天無後續） |
| Capability Curve | Agent 能力曲線追蹤，評估不同任務類型能力進展 | 公告（細節待確認，公告後逾 100 天無後續） |
| 自架沙箱（Self-hosted Sandboxes） | 企業在自有基礎設施執行 agent 工作流，資料不出境 | 公開測試 |
| MCP 隧道（MCP Tunnels） | 私有 MCP 伺服器安全連接 Claude Code，無需暴露公網 | 公開測試 |

---

## 相關議題
- [[entities/claude-code]]（Managed Agents 整合於 Claude Code 工作流；SDK 版本流水與已知問題住該頁）
- [[topics/coding-workflow-guide]]（`/goal`、驗證階梯與內建 subagent 的實際用法）
- [[topics/official-community-gap]]（官方對應程度與社群缺口對照）
- [[topics/community-tech-patterns]]（社群工具 Dreamer 採用類似理念，早於官方功能出現）
- [[entities/pricing]]（訂閱配額與 Agent SDK 計費規則）

## 參考來源

- [[news/2026-07-17]]
- [[news/2026-04-28]]
- [[news/2026-04-30]]
- [[news/2026-05-07]]
- [[news/2026-05-11]]
- [[news/2026-05-12]]
- [[news/2026-05-13]]
- [[news/2026-05-19]]
- [[news/2026-05-16]]
- [Ars Technica 報導](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)
- [官方總覽文件](https://platform.claude.com/docs/en/managed-agents/overview)（2026-09-06 查證）
- [官方定價文件](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)（2026-09-06 查證）
- [官方 Dreaming 文件](https://platform.claude.com/docs/en/managed-agents/dreams)（2026-09-06 查證）
- [官方自架沙箱文件](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)（2026-09-06 查證）

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-09-15 | **anthropic-sdk-python v1.6.0** 再擴充 auto mode 工具權限功能，原文截斷、範圍未知（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.6.0)）|
| 2026-09-11 | **anthropic-sdk-python v1.5.0** 新增 Managed Agents auto mode 工具權限設定，changelog 首度列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.5.0)）|
| 2026-09-03 | Reddit 貼文宣稱自建開源 agent 框架以同一模型達同準度、成本低最多 75%，未附測試方法與資料集（[原文](https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/)）|
| 2026-08-19 | **anthropic-sdk-python v0.125.0** 新增 managed agents 的 web search 設定相關功能，官方 changelog 未列出具體項目（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.125.0)）|
| 2026-07-22 | **anthropic-sdk-python v0.118.0** 新增三項 Managed Agents 支援：model effort、初始 session events、threads 增量串流（[Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.118.0)，09-13 查證）|
| 2026-07-16 | **anthropic-sdk-python v0.117.0** 新增「api: add support for dreaming」，即 Dreaming 記憶整合 API（官方 dreams 文件確認，見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0)）|
| 2026-07-01 | **anthropic-sdk-python v0.115.0** 新增 Managed Agents API 支援，開發者可透過官方 SDK 直接操作（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0)）|

### 2026-05 時段總結
- 「Code with Claude」大會宣布重大更新：Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證（05-06）；SDK 雙線原生支援（05-07）；正式發布升格（05-11）；Agent View 與 `/goal` 指令上線（05-12）
- 自架沙箱與 MCP 隧道上線（05-19）；Proactive Workflows／Capability Curve 公告（05-18）；自架沙箱完整參考文件（05-22）；Boris Cherny 公開每晚數千子代理工作流（05-13）
- 原始條目見 [[entities/managed-agents-archive#2026-05]]

### 2026-04 時段總結
- 04-28 首次宣布跨會話記憶功能；04-30 公開測試版推出，定位「agentic AI 的 AWS」
- 原始條目見 [[entities/managed-agents-archive#2026-04]]

**懸置細節**

