---
page: "entities/managed-agents-archive"
kind: "entity"
status: "resolved（封存頁）"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-20"
last_news_update: "2026-05-22"
status_main: "resolved"
days_since_news: 122
parent: "entities/managed-agents"
children: "[]"
page_role: "archive"
days_since_news_subtree: 122
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Managed Agents——原始條目封存

**狀態：** resolved（封存頁）
**領域：** 🛠️ 工具/功能
**上層：** [[entities/managed-agents]]
**最後更新：** 2026-09-20
**最後新聞更新：** 2026-05-22

> 本頁保存 [[entities/managed-agents]] 被搬離主頁的原始「歷史記錄」條目（含對應歷史細節）。條目一字不刪，只是搬離主頁讓主頁讀得動；重點層見主頁。

---

## 2026-05

| 日期 | 事件 |
|------|------|
| 2026-05-22 | **自架沙箱完整參考文件發布**（via Reddit r/ClaudeAI 報告 v2.1.145 新增）：企業可在完全自有基礎設施部署受管代理（文件範圍見歷史細節）|
| 2026-05-19 | 新增**自架沙箱（self-hosted sandboxes）**與 **MCP 隧道（MCP tunnels）**：企業可於自有基礎設施執行 agent 工作流，私有 MCP 伺服器無需公開即可連接（the-decoder.com）|
| 2026-05-18 | InfoQ：Anthropic 於 Code With Claude 正式公告 **Proactive Workflows** 與 **Capability Curve** 兩項新能力（各自解什麼見歷史細節）|
| 2026-05-16 | dev.to 深度解析 Dreaming——Agent 於非活躍期間透過 Outcomes 與 Orchestration 自我優化，副標「How Agents Self-Improve While You Sleep」（見歷史細節）|
| 2026-05-13 | v2.1.140 的 `subagent_type` 改為大小寫與分隔符號不敏感（`"Code Reviewer"` → `code-reviewer`），降低配置摩擦；同期 Boris Cherny 公開每晚數千子代理工作流（見歷史細節）|
| 2026-05-12 | v2.1.139 新增 Agent View（Research Preview，多 session 管理面板，`claude agents`）與 `/goal` 指令，是邁向非同步工作流的里程碑 |
| 2026-05-11 | 正式發布（從研究預覽升格）；社群自建 70 天多代理架構開發者分享實戰：Opus 決策層 + OpenCode 工程師層 + 並行研究代理，核心結論是任務簡報品質決定系統成敗；官方 vs 社群自組方案的比較進入主流討論 |
| 2026-05-07 | Python SDK v0.100.0 + TypeScript SDK v0.95.0 新增 Managed Agents 原生支援，雙線同日發布 |
| 2026-05-06 | 「Code with Claude」大會宣布重大更新：Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證 |

**歷史細節**
- **自架沙箱參考文件（2026-05-22）**：文件涵蓋 worker 輪詢機制、環境金鑰管理、webhook 喚醒設定、監控方案及客戶自管安全責任，標誌企業化部署從「支援」走向「完整文件化」。
- **Proactive Workflows 與 Capability Curve（2026-05-18）**：前者讓 Agent 可主動（而非被動等待觸發）排程並執行任務，與 Cat Wu「AI 的下一步是主動性（proactivity）」論述一致；後者提供能力曲線追蹤，協助評估 Agent 在不同任務類型的能力進展。
- **dev.to 技術解析（2026-05-16）**：Code with Claude 大會功能的首篇深度技術解析，對關注 agent 長期自主執行行為的開發者有參考價值。
- **Boris Cherny 的數千子代理工作流（2026-05-13）**：由 Business Insider 等主流媒體報導，是 Managed Agents 大規模並行能力的極端現實應用案例（見 [[entities/boris-cherny]]）。

## 2026-04

| 日期 | 事件 |
|------|------|
| 2026-04-30 | 公開測試版推出，Anthropic 定位為「agentic AI 的 AWS」，Managed Agents + Persistent Memory 同步開放 |
| 2026-04-28 | 首次正式宣布加入跨會話記憶功能 |
