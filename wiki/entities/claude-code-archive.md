---
page: "entities/claude-code-archive"
kind: "entity"
status: "resolved（封存頁）"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-01"
last_news_update: "2026-04-30"
status_main: "resolved"
days_since_news: 186
parent: "entities/claude-code"
children: "[]"
page_role: "archive"
days_since_news_subtree: 186
inbound_links: 9
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-21"
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code——原始條目封存

**狀態：** resolved（封存頁）
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**最後更新：** 2026-11-01
**最後新聞更新：** 2026-04-30

> 本頁保存從 [[entities/claude-code]] 與三個子頁移出的原始條目：歷史記錄、發布超過 90 天的版本表列、已解決的 Anthropic Status 事故。條目一字不刪，只是搬離主頁讓主頁讀得動；重點見主頁與 [[entities/claude-code-releases]]。

---

## 2026-04

| 日期 | 事件 |
|------|------|
| 2026-04-30 | GameMaker 宣布整合 Claude Code，為遊戲開發者提供 AI 輔助工作流程 |
| 2026-04-30 | v2.1.124 系統提示更新：新增「File modification detected」預算超出提醒機制（+166 tokens）；v2.1.126 精簡核心身份指令（-87 tokens） |
| 2026-04-30 | Claude Security 公開測試版推出，情境化安全評估直接整合於 Claude Code；見 [[entities/claude-security]] |
| 2026-04-30 | TypeScript SDK v0.92.0：改善 Managed API 相關功能 |
| 2026-04-30 | Anthropic 定位為「agentic AI 的 AWS」：Managed Agents + Persistent Memory 公開測試版 |
| 2026-04-29 | Anthropic 發布官方「Champion Kit」：為推動企業採用 Claude Code 的工程師設計，含 30 天推廣計畫、常見疑慮應對話術與分享素材 |
| 2026-04-29 | 社群工具：Cockpit（Web UI）、Harness（多 worktree 並行 agent）、CodeThis（MCP paste bin）、Claude Exporter（匯出至 PDF/Word/Notion）|
| 2026-04-28 | v2.1.121 發布：MCP `alwaysLoad` 選項（設為 true 跳過 tool-search 延遲）、`claude plugin prune` 清除舊外掛 |
| 2026-04-28 | Runhouse 團隊股權收購：分散式 AI 基礎設施與計算編排專家加入 Anthropic，強化 agentic 工作流底層架構 |
| 2026-04-28 | Auto Compact 失效事件被回報，session 鎖死問題無法通過重啟解決 |
| 2026-04-28 | Anthropic 為 Managed Agents 加入跨會話記憶功能（正式公告） |
| 2026-04-27 | API 金鑰外洩漏洞被媒體報導：可能在自動化流程中洩漏至 npm 等公開倉庫 |
| 2026-04-27 | HERMES.md 計費 bug 引發更廣泛媒體關注，確認損失達 $200，等待修復 |
| 2026-04-27 | 版本從 2.1.120 回滾至 2.1.119；成因為 2.1.120 的 --resume 啟動崩潰，2.1.121 修復（2026-10-24 查證，見 [[entities/claude-code]] 已知問題）|
| 2026-04-27 | 28 個滲透測試子代理人開源工具 pentest-ai-agents 釋出 |
| 2026-04-26 | HERMES.md 計費路由 bug 曝光，Anthropic 確認但拒絕退款 |
| 2026-04-26 | Anthropic 測試 Bugcrawl 漏洞偵測工具，見 [[entities/bugcrawl]] |
| 2026-04-26 | Anthropic 工程部落格詳解 Claude Research 多代理架構設計 |
| 2026-04-26 | 多個社群工具發布：Claude Squad（多人協作）、mux0（多 agent 終端）、agent-order（Codex+Claude PRD 協作） |
| 2026-04-25 | 社群開發 CC-Canary 工具自動偵測效能漂移 |
| 2026-04-24 | Stop hooks 失效問題被回報（Claude 4.7） |
| 2026-04-24 | Anthropic 正式承認效能退步源於工程疏失 |
| 2026-04 | Google 開始秘密開發競品 |

**版本表（發布超過 90 天的列）**

| 版本 | 發布日 | 重點 |
|------|------|------|
| **v2.1.124** | 2026-04-30 | 系統提示新增預算超出提醒機制（+166 tokens）|
| **v2.1.121** | 2026-04-28 | MCP `alwaysLoad` 選項；`claude plugin prune` |

## 2026-05

| 日期 | 事件 |
|------|------|
| 2026-05-28 | **v2.1.153**：`skipLfs` 選項加入 github/git plugin，clone/update 可跳過 Git LFS 下載；npm 全域安裝版本過期時顯示一次性升級通知；Cisco LLM Security Leaderboard 發布，Anthropic 佔前十名 8 席；Simon Willison 發布 HN 970 分析文（Anthropic/OpenAI 已達 PMF）；Anthropic 宣布開設米蘭辦公室（歐洲第六據點）；企業預算壓力信號：Benzinga/CFO.com 報導 AI 編碼工具成長放緩；ChatGPT-5.5 在 DeepSWE 污染免疫基準超越 Opus 4.7 |
| 2026-05-27 | **v2.1.152**：`/code-review --fix` 可直接將審查結果套用至工作樹；**Coordinator 模式**正式加入，多 worker 代理人協調層支援任務委派、結果合成、lifecycle 管理、跨 session peer 協調與獨立驗證（+4,566 系統提示 tokens）；Uber COO 公開確認 Claude Code + ChatGPT 帶來 25% 生產力提升；富士通與 Anthropic 簽署戰略合作；Platformer 刊出 Boris Cherny 專訪（「軟體工程師的終結」） |
| 2026-05-22 | **v2.1.148**：緊急修復 v2.1.147 回歸問題（Bash 工具 exit code 127）；Managed Agents 自架沙箱完整參考文件發布（涵蓋 worker 輪詢、環境金鑰、webhook 喚醒、監控、客戶安全責任）；Runtime（YC P26）推出讓全團隊安全使用 Claude Code 的基礎設施；DeepSeek 宣布建構自有 Claude Code 競品（整機棧控制戰略）；Qwen3.7-Max 聲稱可持續自主運行 35 小時並支援 Claude Code harness；費用失控輿情升溫（$6,000 徹夜運行廣傳，Karpathy 「最小必要 context」原則成社群共識）；Sky News 專訪 Claude Code 創作者談 AI 與工程師職位；見 [[topics/competitor-landscape]]、[[topics/enterprise-cost-management]] |
| 2026-05-21 | **v2.1.146**：`/simplify` 正式更名為 `/code-review`，新增可選強度等級（`/code-review high`）；auto mode 不再抑制 `AskUserQuestion`，skill 或用戶明確觸發時仍可向使用者提問 |
| 2026-05-21 | Claude Code 沙箱第二個獨立繞過漏洞揭露（null byte 注入繞過 hostname 白名單），PoC 已公開；兩個漏洞均自 2025-10-20 沙箱 GA 起持續存在；Opus 4.6 extended thinking 在 Claude Code 中被靜默移除（桌面版仍可用，未公告）；見 [[topics/ai-agent-safety]] |
| 2026-05-19 | **v2.1.144**：`/resume` 擴展支援背景 session——`claude --bg` 啟動的 session 現可在 `/resume` 列表與互動式 session 並列（標記 `bg`），加入 elapsed duration 計時 |
| 2026-05-19 | Anthropic 收購 Stainless（官方 SDK + MCP 伺服器生成商，傳聞金額逾 $300M）；Microsoft 六個月內部測試全貌揭露（dev.to）：開發者普遍認可但財務層以成本終止；攝影機存取請求隱私疑慮；Claude Code .env 明文 SQLite 安全揭露；見 [[topics/anthropic-business]]、[[topics/ai-agent-safety]]、[[topics/enterprise-cost-management]] |
| 2026-05-19 | 新工具：**Claude Soul**（MCP server + hooks 跨 session 學習引擎，~200 session 後報告出現意外行為）、**cdesktop**（開源整合 Claude Code + Codex + Gemini CLI 等 5 個 coding agent，支援 20+ 第三方模型，`npx` 執行）、**InsForge**（YC P26 開源後端平台，讓 coding agent 直接部署、操作與 debug 後端及基礎設施）|
| 2026-05-17 | 開發者以 Claude Code 完成 Adobe Lightroom CC 在 Linux 的主要移植工作（Phoronix 報導），展現 AI Coding Agent 在複雜跨平台工程任務的實際能力 |
| 2026-05-17 | 社群分享高複雜度持久性自主 agent 系統：語義 + 情節雙重記憶、德英雙語語音對話、情緒狀態追蹤、螢幕感知、自主排程、即時 SaaS 生成，代表社群 agentic 工程複雜度快速提升的里程碑案例 |
| 2026-05-17 | Claude Skills 靜默覆蓋問題浮現：`ask_user_input_v0` 工具存在最多 3 問題 / 4 選項硬性限制，Claude 在不告知用戶的情況下靜默壓縮問題與選項；技術社群對 Skills 機制透明度的系統性質疑升溫；Skills 意外觸發子 agent 派生案例同步出現（見 [[topics/community-tech-discussions]]） |
| 2026-05-17 | Anthropic 官方文件中 4 種 context 管理工具（超越 `/clear` + `/compact` 的二元認知）的使用場景對比在社群廣泛流傳，成為大型 codebase 長工作階段管理的新參考（見 [[topics/community-tech-discussions]]） |
| 2026-05-17 | 多帳號 Claude Code 架構合規邊界明確：兩種多帳號架構中，其中一種已被 Anthropic 明確禁止（ToS 違規），開發者需注意合規邊界；見 [[entities/pricing]] |
| 2026-05-17 | Anthropic API 大規模 500 Internal Server Error（UTC 18:08）：官方狀態頁確認多模型「Elevated error rates」，Claude Code 陸續回報 500 錯誤，為近期少見的跨模型服務中斷事件；見已知問題 |
| 2026-05-17 | 新工具：**shipcheck**（讀取 Claude Code / Cursor session log，輸出費用分解、檔案修改熱圖與安全掃描，不到一秒完成且完全離線；發現 `@anthropic-ai/sdk` 常被誤寫為 `@anthropic/sdk` 的 package hallucination 問題）、**Gonfire**（分析應徵者 Claude Code session log 評估解題思維，面試替代 leetcode 的新工具）|
| 2026-05-16 | **v2.1.143**：Plugin 依賴關係強制執行——`claude plugin disable` 在目標被其他已啟用 plugin 依賴時拒絕執行，提示完整停用鏈建議指令（例：先停用 B 再停用 A），降低複雜 plugin 組合因停用依賴造成工具鏈損壞的風險 |
| 2026-05-16 | GitHub 推出新 Copilot 應用程式，明確將 Claude Code 與 OpenAI Codex 列為競爭目標；Anthropic 據報積極尋找下一個「Claude Code 等級」突破性產品；AI 編程 agent 賽道進入正面搶用戶階段；見 [[topics/competitor-landscape]] |
| 2026-05-16 | 新工具：Code Quest（Web UI 互動模式，6/15 計費調整因應）、CostHawk（公開 token 用量排行榜）、AI 引用資格稽核 MCP（13 工具，無需 API key）、answering machine MCP（Claude Code 用戶間留言） |
| 2026-05-15 | **v2.1.142**：`claude agents` 新增 8 旗標（`--add-dir`、`--settings`、`--mcp-config`、`--plugin-dir`、`--permission-mode`、`--model`、`--effort`、`--dangerously-skip-permissions`），開發者可直接在指令列指定模型版本、MCP 路徑、工作目錄與權限模式 |
| 2026-05-15 | Anthropic 官方發表「Claude Code at Scale」系列首篇，彙整 monorepo、遺留系統、多 repo 分散式架構真實部署成功模式；HN 討論熱度 203，本週最受工程社群關注的技術文章 |
| 2026-05-15 | Microsoft 正陸續取消內部 Claude Code 授權（去年 12 月開放數千名員工使用），改推 GitHub Copilot CLI；見 [[topics/competitor-landscape]] |
| 2026-05-15 | 新工具：PlanBridge（開源，透過 Agent hook 在瀏覽器渲染 Markdown 計劃書並支援行內評論）、my-time-has-come（配額將至時自動收尾任務）、Ungate（Claude Max 訂閱路由至 Cursor，2026-08-10 查證確認 ToS 風險屬實——Anthropic 已於 2026-04-04 明文規定 Pro／Max／Team 訂閱不涵蓋透過第三方 harness 以 OAuth 路由的用量，Ungate 屬此類，使用者恐違反服務條款）|
| 2026-05-14 | 官方文件發布 `/loop`、`/batch`、`/background` 完整自主執行指令套件（搭配 v2.1.139 的 `/goal`），Claude Code 產品定位正式轉向 agent 開發平台；Claude Code 負責人 Cat Wu 指出「AI 下一步是主動性（proactivity）」；6/15 訂閱 programmatic 用量剝離公告引發強烈反彈，`claude-pee` 繞過工具出現；見 [[entities/pricing]] |
| 2026-05-14 | 新工具：Ledger（Rust PR 層級 token 成本追蹤 + macOS 選單欄 + Web dashboard）、Clawdmeter（ESP32-S3 實體 token 監控面板）、Grafana Dashboard（Claude Code 用量 Prometheus 監控）、agent-html-skills（雙向 HTML 工件生成 plugin）、Lanes v0.39（GitHub + Linear 雙向整合） |
| 2026-05-13 | v2.1.141：`terminalSequence` 欄位至 Hook JSON（無控制終端環境桌面通知 + 視窗標題 + 響鈴）；`CLAUDE_CODE_PLUGIN_PRE` 擴展插件系統能力 |
| 2026-05-13 | v2.1.140：改善 Agent 工具的 `subagent_type` 參數匹配邏輯，支援大小寫不敏感及分隔符號不敏感（例如 `"Code Reviewer"` 自動解析為 `code-reviewer`），並更新代理顏色配色方案；代理提示詞更新以確保 context 壓縮後安全指令完整保留；見 [[entities/managed-agents]] |
| 2026-05-13 | Boris Cherny 公開每晚讓數千個 AI 子代理執行「深度工作」的工作流架構，被 Business Insider 與 Let's Data Science 同步報導；研究者掃描 48 個 AI 生成應用發現 90% 存在安全漏洞（44% 驗證缺口、33% 可繞過 RLS 的 Postgres 函式、25% BOLA/IDOR）；見 [[topics/ai-agent-safety]] |
| 2026-05-13 | 新工具：Dragoman（多模型路由 CLI，HN Show HN）、Cocall.ai（外線電話 MCP）、Claudy macOS session 管理版（多 session 並列 + 自動帳號切換）；PullMD v2.4.1 支援 claude.ai 網頁版自訂連接器原生整合 |
| 2026-05-12 | v2.1.139：Agent View（Research Preview，`claude agents` 啟用統一多 session 管理介面）+ `/goal` 指令（fire-and-forget，小型快速模型驗證完成條件，104 項變更）；見 [[entities/managed-agents]] |
| 2026-05-12 | 假冒官方安裝包惡意攻擊（IElevator 機制，Yahoo Tech/CSO Online/The Register 同步報導）；Claude AI 三天內第二次服務中斷；見 [[topics/ai-agent-safety]] |
| 2026-05-12 | UiPath 開放 RPA 平台優先整合 Claude Code + Codex；Signadot 推出 Kubernetes 環境程式碼驗證技能；研究團隊公開 AI 驅動 ESP32 Fault Injection 攻擊（首個公開案例） |
| 2026-05-12 | 新工具：HiveTerm（多 Agent 工作站）、Writ（Neo4j 規則強制執行插件）、Agent FM（聽覺化進度廣播）、Usage4Claude 3.0.0（含 Codex 追蹤）、ltm（跨環境 JSON 記憶協定） |
| 2026-05-11 | Managed Agents 正式發布（從研究預覽升格）；Claude Code Desktop vs Claude Cowork 定位混淆問題浮上，兩款產品功能高度重疊，Anthropic 尚未釐清差異 |
| 2026-05-11 | 新工具：adamsreview（多代理 PR review，宣稱優於官方 /review 與 CodeRabbit）、vibe-log-cli（每日 / 每週開發工作摘要自動生成）、academic-research-skills（蘇格拉底反思模式技能包，社群評價分歧）|
| 2026-05-10 | Claude Code Sandboxing 正式文件發布：透過 OS 層級原語對沙箱化 bash 工具實施檔案系統與網路隔離，在 session 開始時預先定義操作邊界；此為 Anthropic 首次正式記錄 Claude Code 沙箱隔離機制，見 [[topics/ai-agent-safety]] |
| 2026-05-10 | 社群發現 CLAUDE.md 作為 candidate-context 架構：逆向工程 Claude CLI 後發現 CLAUDE.md 被 `<system-reminder>` + 「may or may not be relevant」包裹，直接解釋「指令被忽略」現象；Anthropic 尚未正式回應 |
| 2026-05-09 | v2.1.138：internal fixes only，無功能層面變更 |
| 2026-05-09 | v2.1.136 系統提示大幅更新（+525 tokens）：「操作安全與如實回報」機制新增，不可逆操作須確認、刪除前需檢視目標、必須如實回報跳過步驟與未通過測試；代理規則新增 `hard_deny`（無條件安全邊界封鎖），縮小 `soft_deny` 適用範圍；見 [[topics/ai-agent-safety]] |
| 2026-05-09 | Windows IDE 擴充套件全面無法載入（UTC 00:24）：更新版本將 Linux 路徑硬編碼進套件，官方確認追蹤中，臨時解法降版；繼 2026-05-06 v2.1.131 修復後的第二次 Windows 平台重大相容性事故 |
| 2026-05-08 | v2.1.133：新增 `worktree.baseRef` 設定（`fresh` \| `head`），讓使用者可控制 `--worktree`、`EnterWorktree` 及代理隔離工作樹要從 `origin/<default>` 分支還是本地 `HEAD` 建立，提供更靈活的多工作樹管理策略 |
| 2026-05-08 | CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞公開（symlink 逃逸），v2.1.64 已修補；同日爆出 1-click RCE 信任提示問題，Anthropic 回應被批為責怪使用者；見 [[topics/ai-agent-safety]] |
| 2026-05-08 | 新工具：Claudy（Rust 多供應商設定管理 + MCP 橋接）、DataMoat（AES-256-GCM 工作記錄加密保存）、4-agent Code Review（架構師 + 三模型專家審查，MIT）、awesome-ux-skills（Nielsen 等 UX 原則技能集）|
| 2026-05-08 | Claude Sonnet 4.8 外洩資訊出現（Geeky Gadgets 報導），官方尚未確認下一代 Sonnet 規格 |
| 2026-05-07 | v2.1.132：新增 `CLAUDE_CODE_SESSION_ID` 環境變數至 Bash 工具子行程（hooks 可追蹤當前 session）；新增 `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` 選項，供需要控制終端顯示行為的環境使用 |
| 2026-05-07 | Python SDK v0.100.0 里程碑：新增 Managed Agents 多路並行支援；TypeScript SDK v0.95.0 同步新增 Managed Agents API 支援；兩者同日發布 |
| 2026-05-07 | Managed Agents 重大更新（Code with Claude 大會）：Dreaming 記憶整合、最高 20 路子代理並行、Outcomes 規格驗證，標誌 Agent 框架從無狀態走向有狀態；見 [[entities/managed-agents]] |
| 2026-05-07 | SpaceX 算力合作：Pro/Max 五小時視窗速率上限翻倍、取消尖峰降速；API Tier 4+ 速率限制提升；見 [[entities/pricing]] |
| 2026-05-07 | 新工具：BrowserCode（WebAssembly 瀏覽器 + 行動裝置支援）、/qu /ans 跨 session 通訊插件、Kstack（K8s 監控/除錯/安全審計 skill pack）、recap（AI 對話知識點摘要，主動對抗 skill atrophy） |
| 2026-05-06 | v2.1.131 緊急修復：v2.1.128/129 自動推送後 Windows VS Code extension 完全無法啟動（createRequire polyfill hardcoded build path）+ Mantle endpoint 認證失效；數小時內因 Reddit 大量回報而緊急回應 |
| 2026-05-06 | Python SDK v0.99.0 + TypeScript SDK v0.94.0 同步發布，新增 client 層 workspace 定向功能（同一 SDK 實例可針對指定 workspace 發出請求），雙線同日維持功能同步節奏 |
| 2026-05-06 | Claude Code 累積 121,000 GitHub Stars，分析文章探討為何開發者跳過傳統 IDE 直接使用 CLI 工具 |
| 2026-05-06 | Claude Security 從封閉預覽移至公開 Beta，開發者可在 Claude Code 工作流中直接使用 AI 驅動的安全審查功能，無需另行安裝工具；見 [[entities/claude-security]] |
| 2026-05-06 | 新工具：Claudette（每個 agent 獨立 git worktree + session + 終端機的 speculative parallelism 工作流）、claude-smart（將糾正泛化為跨專案通用規則的自我改進插件）、Dreamer（MCP team memory server，支援任意 coding agent） |
| 2026-05-05 | Amazon 正式向全體企業員工部署 Claude Code 與 OpenAI Codex（雙品牌並行），軟體開發體驗 VP Jim Haughwout 內部公告；AI 編碼工具進入大型企業標配部署階段 |
| 2026-05-05 | v2.1.128：`/color`（無參數）隨機選取 session 顯示顏色；`/mcp` 顯示各伺服器工具數量並標記 0 工具連線伺服器；`--plugin-dir` 行為調整 |
| 2026-05-05 | Boris Cherny（Claude Code 創始人）在 podcast 中宣示：已 100% 用 Claude Code 取代手動編碼；「Loops（迴圈執行）是 AI 編碼的未來」，而非單次對話補全 |
| 2026-05-05 | 新工具：SprintiQ（sprint 規劃）、Claude Relay（多 session 互通）、Memex（本地 RAG 持久記憶，MCP）、Claude-Find（語義 session 搜尋）、Askdiff（diff 介面直問同一 session）、Rudel（9 種 AI 程式設計師原型分析） |
| 2026-05-04 | 原始碼外洩事件持續擴大：Anthropic 已向各平台發出逾 8,100 次 DMCA 下架請求，引發 AI 生成程式碼版權歸屬法律辯論，社群分支「Claw-Code」誕生 |
| 2026-05-04 | Claude Cowork/Desktop 悄悄加入支援任意第三方 LLM 功能（OpenAI、Gemini、本地模型、Bedrock/Vertex/Foundry 企業閘道），無任何官方公告，由社群自行發現 |
| 2026-05-04 | Claude Connectors 透過 MCP 擴展至創意工作軟體：Adobe（After Effects/Photoshop/Illustrator）、Blender、Ableton Live、Affinity、Autodesk Fusion |
| 2026-05-04 | Claude API 全球直接存取正式開放，擴大全球服務覆蓋範圍 |
| 2026-05-04 | 新工具：Semble（code search 比 grep 少 98% token）、Kirikiri（iOS mobile IDE）、JupyterLab 擴充套件、Prism MCP（VS Code LSP 橋接）、claudely（本地 LLM 無痛切換）、Smithy（issue tracker 觸發容器化 session）、Patina（CLAUDE.md 維護 CLI） |
| 2026-05-03 | macOS 電腦使用（computer use）功能上線：Claude Code / Claude Cowork 可直接控制 macOS 桌面滑鼠與鍵盤，升格為全桌面自動化代理 |
| 2026-05-03 | 新工具：TradingAgents Plugin（免額外 API 費的 7 子代理股票分析框架，訂閱內執行）|
| 2026-05-02 | AGENTS.md 規範不支援（GitHub issue #6235）：跨工具（Cursor/Copilot）配置互操作缺口浮現 |
| 2026-05-02 | 新工具：Governor（token 浪費優化插件，成效 🔎 查無官方 ⟨Q-13⟩）、Caliber（888 stars，統一管理 CLAUDE.md/.cursor/rules/AGENTS.md） |
| 2026-05-02 | v2.1.126：`/model` 選擇器現在從 gateway 的 `/v1/models` 端點列出模型（適用於 `ANTHROPIC_BASE_URL` 自訂 gateway 場景）；新增 `claude project purge` 指令 |
| 2026-05-02 | 社群工具：Omar（100 agent TUI 管理）、graphify（知識圖譜插件 450k+ 下載）、NanoBrain（git-backed 知識庫）、Council（多模型並行 CLI）、Destiny（占卜技能）、Mote（Minecraft agent）|
| 2026-05-02 | GameMaker 正式啟用 Claude Code 整合（AI 輔助遊戲開發工作流程），iCapital 金融平台採用 Anthropic 技術 |

**版本表（發布超過 90 天的列）**

| 版本 | 發布日 | 重點 |
|------|------|------|
| **v2.1.158** | 2026-05-30 | **Auto mode 擴展**：Bedrock、Vertex、Foundry 平台現支援 Opus 4.7 & 4.8 的 Auto mode；透過環境變數 `CLAUDE_CODE_ENABLE_AUTO_MODE=1` 啟用 |
| **v2.1.156** | 2026-05-29 | 修復使用 Opus 4.8 時 thinking blocks 被修改導致 API 400 錯誤的問題 |
| **v2.1.153** | 2026-05-28 | ① **`skipLfs` 選項**：加入 github/git plugin 市集來源，clone 與 update 時可跳過 Git LFS 大型檔案下載，降低大型 repo 的頻寬與時間成本；② **npm 版本通知**：偵測到全域安裝版本過期時顯示一次性升級提示，改善版本管理體驗 |
| **v2.1.152** | 2026-05-27 | ① `/code-review --fix`：審查完成後直接將建議套用至工作樹（修正錯誤、優化可重用性與效率，跳過誤報）；② **Coordinator 模式**：全新多 worker 代理人協調層，支援任務委派、結果合成、lifecycle 管理、跨 session peer 協調、獨立驗證委派結果（+4,566 系統提示 tokens）；③ **Worker 代理人指令**：範圍執行、並行分支安全處理、強制回報要求 |
| **v2.1.150** | 2026-05-23 | 內部基礎設施改善，無使用者端可見功能變更；**⚠️ 安全爭議**：社群研究者發現此版啟動時呼叫 `api.anthropic.com/api/claude_cli/bootstrap` 並快取系統提示片段至磁碟，GrowthBook 功能旗標 `tengu_heron_brook` 每 60 秒動態重整，回傳字串直接注入擁有 shell 存取的系統提示（見 [[topics/ai-agent-safety]]） |
| **v2.1.148** | 2026-05-22 | 緊急修復 v2.1.147 引入的回歸問題：Bash 工具對部分用戶每次指令都回傳 exit code 127，導致 shell 命令無法正常執行 |
| **v2.1.146** | 2026-05-21 | `/simplify` 正式更名為 `/code-review`，新增可選強度參數（`/code-review high`）；auto mode 不再抑制 `AskUserQuestion`（skill 或用戶明確觸發時仍可向使用者提問）|
| **v2.1.145** | 2026-05-20 | `claude agents --json` 指令：將目前存活的 Claude session 以 JSON 格式列出，便於與 tmux-resurrect、status bar、session picker 等工具整合；新增 `agent_id` 及 `parent_agent_id` 屬性，支援多 agent 層級識別 |
| **v2.1.144** | 2026-05-19 | `/resume` 擴展支援背景 session：`claude --bg` 啟動的 session 現可在 `/resume` 列表中與互動式 session 並列顯示（標記為 `bg`），加入 elapsed duration 計時顯示 |
| **v2.1.143** | 2026-05-16 | Plugin 依賴關係強制執行：`claude plugin disable` 在目標 plugin 被其他已啟用 plugin 依賴時拒絕執行，並提示完整停用鏈建議指令，防止工具鏈損壞 |
| **v2.1.142** | 2026-05-14 | `claude agents` 新增 8 旗標：`--add-dir`、`--settings`、`--mcp-config`、`--plugin-dir`、`--permission-mode`、`--model`、`--effort`、`--dangerously-skip-permissions`，大幅提升 Agent 啟動時細粒度控制能力 |
| **v2.1.141** | 2026-05-13 | `terminalSequence` 欄位至 Hook JSON（無控制終端環境下桌面通知 + 視窗標題 + 響鈴）；`CLAUDE_CODE_PLUGIN_PRE` 擴展插件系統 |
| **v2.1.140** | 2026-05-13 | `subagent_type` 大小寫／分隔符號不敏感匹配；代理配色更新 |
| **v2.1.139** | 2026-05-12 | ★ Agent View（多 session 統一管理）+ `/goal`（fire-and-forget，104 項變更）|
| **v2.1.136** | 2026-05-09 | 操作安全機制（+525 tokens）；`hard_deny` 無條件安全邊界 |
| **v2.1.133** | 2026-05-08 | `worktree.baseRef` 設定（`fresh` \| `head`）|
| **v2.1.132** | 2026-05-07 | `CLAUDE_CODE_SESSION_ID`；`CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` |
| **v2.1.131** | 2026-05-06 | 緊急修復 Windows VS Code extension 全面無法啟動 |
| **v2.1.128** | 2026-05-05 | `/color` 隨機配色；`/mcp` 顯示各伺服器工具數量 |
| **v2.1.126** | 2026-05-02 | `/model` 從 gateway `/v1/models` 列出；`claude project purge` |

## 2026-06

| 日期 | 事件 |
|------|------|
| 2026-06-30 | **v2.1.197**（初報）：`/model` 選單出現 Sonnet 5 選項（當時無法選用），社群預測正式發布在即；07-01 官方確認正式切換 |
| 2026-06-30 | **Explore subagent 鎖定 Haiku 分析**：社群深入分析內建 subagent 類型，發現 Explore subagent 固定使用 Haiku 模型，除錯場景可能因模型能力不足導致問題（見 [[已知問題]]）|
| 2026-06-30 | **Session 30天自動刪除：Anthropic 拒絕修復**：官方在 GitHub issue #62476 明確表示不修復此行為，社群建議透過 CLAUDE.md + `.claude/changelog` 手動保留記錄 |
| 2026-06-30 | **36Kr 報導背景任務升級**（2026-06-30 指控，至今無後續）：36Kr 報導 Claude Code 下一重大升級方向為讓系統在背景完成所有任務、同時使用者繼續對話互動；官方尚未正式公告 |
| 2026-06-29 | **v2.1.196**：新增 org default model 功能，企業管理員在 org console 設定後，使用者在 `/model` 看到「Org default」或「Role default」選項 |
| 2026-06-25 | **v2.1.191**：新增 `/rewind` 指令，可從 `/clear` 執行前任一對話節點恢復，無需重新輸入指令背景；修正 streaming 捲軸自動跳底部問題（UX 改善）；TypeScript SDK v0.106.0 與 Python SDK v0.112.0 同日發布，新增 `client.system.message` 支援 |
| 2026-06-24 | **v2.1.187**：新增 `sandbox.credentials` 設定，可阻止沙盒指令讀取憑證檔案與機密環境變數（AWS 金鑰、API token 等），防止沙盒內惡意指令竊取敏感資訊；新增組織層級模型限制功能，企業管理員可統一管控可用模型清單 |
| 2026-06-22 | **v2.1.186**：新增 `claude mcp login <name>` 與 `claude mcp logout <name>` CLI 指令，可直接從命令列認證 MCP Server，無需進入 `/mcp` 互動選單；`--no-browser` 旗標支援 headless 環境透過 stdin 完成認證；**Extended Thinking 透明度問題社群揭露**（HN score 312）：工程師 Patrick McCanna 分析 session log 發現 thinking blocks 只含推理摘要，完整思考過程由 Anthropic 加密於 600 字元 signature，用戶端無法自行解密，企業審計追蹤承諾受影響（見「已知問題」）|
| 2026-06-21 | **v2.1.185**：stream-stall 提示文字改為「Waiting for API response · will retry in …」，觸發門檻延長至 20 秒（原 10 秒），reliability 改善；Anthropic 官方博客發布「七種 Claude Code 控制層」決策框架（CLAUDE.md、rules、skills、subagents、hooks、output styles、system prompt append），HN score 4 |

**懸置細節**
- ⟨Q-13⟩ 🔎 **查無官方**（標 2026-08-09｜查 Governor、token 浪費｜複 2026-11-21）：社群工具 Governor 宣稱優化 token 浪費，HN 社群對其實際成效提出疑慮；2026-08-10 查證找到廠商自報數據（compact professional 模式宣稱較基準降低 55.5% output token），惟均為工具作者／推廣部落格自行發布。2026-09-20 複查：本輪另搜尋獨立測試／評測站台，僅找到其他 token 優化工具（非 Governor 本身）的第三方 benchmark，未見任何獨立來源覆核或反駁 Governor 自報的 55.5% 數字；Governor 屬第三方社群工具，非 Anthropic 官方項目，故本題本質上不會有「官方」說法，僅能靠獨立覆核解決，目前仍缺，爭議維持未解。2026-10-24 再複查：重新檢索未見 Anthropic 針對 Governor 的任何說法（僅有官方一般性 token 節省指引，與該工具無關），獨立覆核仍缺。

**版本表（發布超過 90 天的列）**

| 版本 | 發布日 | 重點 |
|------|------|------|
| **v2.1.196** | 2026-06-29 | 新增 **org default model** 功能：企業管理員在 org console 設定預設模型後，使用者在 `/model` 選單可看到「Org default」或「Role default」選項，統一組織內模型使用（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)）|
| **v2.1.195** | 2026-06-26 | 新增 `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` 環境變數：在全螢幕模式下停用滑鼠點擊/拖拉/懸停（保留滾輪），適合需要滑鼠直通終端或避免誤觸的場景；修復 hook matcher 無法匹配帶連字號識別符（如 `c-style-hook`）的 bug |
| **v2.1.193** | 2026-06-25 | 新增 `autoMode.classifyAllShell` 設定：將所有 Bash/PowerShell 指令路由至 auto-mode 分類器（先前僅任意程式碼執行模式才會路由）；auto-mode 相關改進 |
| **v2.1.191** | 2026-06-25 | 新增 `/rewind` 指令：支援從 `/clear` 執行前的任一對話節點恢復，讓使用者在誤清 context 後可無縫回到任意歷史節點繼續對話；修正 streaming 時捲軸自動跳至底部的 UX 問題 |
| **anthropic-sdk-typescript v0.106.0** | 2026-06-25 | `client` 新增 `system.message` 支援，開發者可透過 client 層直接注入系統訊息 |
| **anthropic-sdk-python v0.112.0** | 2026-06-25 | `client` 新增 `system.message` 支援，與 TypeScript SDK v0.106.0 功能對齊 |
| **v2.1.187** | 2026-06-24 | 新增 `sandbox.credentials` 設定：可阻止沙盒指令讀取憑證檔案與機密環境變數，防止沙盒內指令洩漏 AWS 金鑰、API token 等敏感資訊；新增組織層級模型限制功能，企業管理員可統一管控可用模型清單，強化企業安全管控 |
| **v2.1.186** | 2026-06-22 | 新增 `claude mcp login <name>` 與 `claude mcp logout <name>` CLI 指令：可從命令列直接認證 MCP Server，無需進入互動式 `/mcp` 選單；支援 `--no-browser` 旗標，透過 stdin 重導向認證，適合 headless / CI 環境 |
| **v2.1.185** | 2026-06-21 | Stream-stall reliability 改善：等待提示文字從「No response from API · Retrying in …」改為「Waiting for API response · will retry in …」；觸發門檻從 10 秒延長至 20 秒，減少短暫延遲時的干擾提示 |
| **MCP Enterprise Authorization** | 2026-06-19 | **企業 SSO 正式版**（stable）：支援 Okta、Anthropic、VS Code 零設定 SSO 整合，企業可集中管理 Claude Code 授權；見 [[feature-radar]] |
| **v2.1.183** | 2026-06-19 | **Auto mode 安全性強化**：破壞性 Git 指令（`git reset --hard`、`git checkout -- .`、`git clean -fd`、`git stash drop`）在 Auto mode 下若非明確要求，一律自動封鎖，防止非預期資料遺失 |
| **Claude Code Artifacts** | 2026-06-18 | 正式推出 Artifacts 功能：工作階段可將進度即時輸出為可共享互動網頁（PR 摘要、儀表板、系統說明文件、釋出清單），隨 session 進行自動更新，團隊成員可直接瀏覽，無需安裝工具 |
| **anthropic-sdk-python v0.111.0** | 2026-06-18 | helpers 模組新增 refusal-fallback 中間件模式，在模型拒絕回應時可優雅降級處理 |
| **anthropic-sdk-typescript vertex-sdk v0.18.0** | 2026-06-18 | Vertex SDK TypeScript 版本更新，帶來新功能改進 |
| **v2.1.179** | 2026-06-16 | 修復串流中斷時部分回應遺失（改為保留而非顯示原始錯誤）；修復 spinner 卡在「running tool」；修復滑鼠滾輪捲動問題 |
| **v2.1.178** | 2026-06-15 | 新增 `Tool(param:value)` 語法用於 permission rules，可比對工具輸入參數（支援 `*` 萬用字元）；例如 `Agent(model:opus)` 可封鎖使用 Opus 的子 Agent；Skills 在巢狀子 Agent 中可正常運作 |
| **v2.1.177** | 2026-06-13 | Bug fixes and reliability improvements |
| **v2.1.175** | 2026-06-12 | 新增 `enforceAvailableModels` 管理設定：啟用後，`availableModels` 白名單同時限制預設模型的解析，避免管理員設定的模型限制被繞過；針對企業管理場景的重要強化 |
| **v2.1.173** | 2026-06-11 | 修正 Fable 5 模型名稱含 `[1m]` 後綴時無法正規化的問題（Fable 5 預設含 1M context，後綴自動移除）；修正誤報「沙盒限制」錯誤訊息 |
| **v2.1.170** | 2026-06-09 | 引入 Claude Fable 5 支援，Fable 5 發布當日更新，使用者可在 Claude Code terminal 切換至 Fable 5 |
| **v2.1.169** | 2026-06-08 | 新增 `--safe-mode` 旗標（及 `CLAUDE_CODE_SAFE_MODE` 環境變數）：啟動時停用所有客製化設定（CLAUDE.md、plugins、skills、hooks、MCP servers），適合排除問題時隔離干擾來源 |
| **v2.1.168** | 2026-06-07 | Bug fixes and reliability improvements |
| **anthropic-sdk-python v0.107.1** | 2026-06-07 | 修復 foundry 模式下 x-api-key header 未正確送出的問題 |
| **v2.1.167** | 2026-06-06 | Bug fixes and reliability improvements |
| **v2.1.165** | 2026-06-05 | Bug fixes and reliability improvements |
| **v2.1.163** | 2026-06-04（確切發布日期未見於官方 changelog 串流，僅知序於 v2.1.162 與 v2.1.165 之間，2026-08-10 查證） | ⚠️ **安全修復**：修復 **CVE-2026-54316**——GitHub Issue 內容經 prompt injection 於 CI runner 執行任意程式碼、外洩 workflow secrets；受影響版本 **0.2.54–2.1.162**；Novee Security 於 Black Hat USA 2026 揭露（見已知問題「🛡️ 安全與隱私」、[[topics/ai-agent-safety]]）|
| **v2.1.162** | 2026-06-04 | ① `claude agents --json` 新增 `waitingFor` 欄位顯示 agent 被阻塞的原因（如 permission prompt）；② `--tools` 明確列出 Grep/Glob 時提供目錄遍歷能力，無需 Bash 工具 |
| **v2.1.161** | 2026-06-03 | ① `OTEL_RESOURCE_ATTRIBUTES` 值作為 metric datapoints 標籤，支援以 team/repo 等自訂維度切片使用數據；② `claude agents` 列表顯示改善 |
| **v2.1.160** | 2026-06-02 | ① **安全修復**：寫入 shell startup files（`.zshenv`、`.zlogin`、`.bash_login`）及 `~/.config/git/` 前新增提示，防止未預期命令執行；② **⚠️ Breaking Change**：`/effort` 的 `workflow` 觸發詞更名為 `ultracode`，所有硬編碼 `workflow` 的腳本式 prompt 即時失效 |
| **v2.1.159** | 2026-06-01 | 內部基礎設施改善（無使用者端可見功能變更） |

## 2026-07

| 日期 | 事件 |
|------|------|
| 2026-07-31 | 已知問題互動數更新（今日聚焦 GitHub Issues 三則）：送出前檢視/編輯「已貼上文字」功能請求（issue #3412）留言增至 82、讚數增至 305；多 Claude session 直接通訊功能請求（issue #24798）留言增至 60、讚數增至 20；Remote Control 自動重連失效（issue #34255）留言增至 59、讚數增至 100；新增已知問題：Linear 整合觸發雲端 agent session 功能請求（issue #12925，39 則留言、131 個讚）、Post/PreToolUse Hooks 未如預期觸發（issue #6305，38 則留言、16 個讚）。 |
| 2026-07-30 | Anthropic Status 通報 Opus 4.7／Opus 4.5 錯誤率升高事件（10:03 UTC 進入監控、10:48 UTC 確認解決）；已知問題互動數更新：主控台新增文字時畫面滾回歷史頂端（issue #826，留言增至 354，全站已知問題本日互動量最高）、Desktop app 多帳號管理與快速切換（issue #18435，154 則留言、769 個讚）、GitHub Connector 已連結卻未被識別（issue #32479，76 則留言、130 個讚）、Desktop 多視窗支援（issue #30154，61 則留言、215 個讚）、Windows 執行工具時主控台視窗閃爍（issue #14828，47 則留言、35 個讚）、VS Code 擴充套件停用自動附加設定（issue #24726，63 則留言、197 個讚）；新增已知問題：Claude Code 未遵循 XDG Base Directory 規範（issue #1455）、功能請求串接 Claude.ai Projects 知識庫（issue #2511）。 |
| 2026-07-29 | anthropic-sdk-python 發布 **v0.120.2**（Bug Fixes：mcp 支援 MCP SDK v2 與 v1 並存），純相容性修正，僅記版本表。新增已知問題 3 則：Cowork 工作區啟動失敗「Failed to start Claude's workspace」、VM service not running，重開機後問題依然存在（issue #27801，71 則留言、40 個讚）、Linux（Ubuntu）無法從剪貼簿貼上圖片（issue #8324，43 則留言、41 個讚）、claude.exe 列出目錄時（`NtQueryDirectoryFileEx`）疑似透過 Wof.sys 觸發 Windows 藍屏（issue #32870，36 則留言）；既有已知問題互動數更新：跨平台多帳號連結訴求（issue #27302，212→222 則留言、452→454 個讚，本日全站互動量最高）、印度地區專屬定價功能請求（issue #17432，205→210 則留言、598→613 個讚）、Windows 11 Pro 缺少 HCS 服務 vfpext 導致 Cowork 無法運作（issue #74649，留言數增至 84）、`autoMemoryEnabled=false` 未抑制記憶體前導文字（issue #63903，32→35 則留言）。The Information（經 Google News 轉載）報導 Claude Code 採用黏著度領先 Codex／開源模型討論熱度，屬市場競爭層面觀察，與 [[topics/competitor-landscape]] 相關，非本頁功能異動範圍，暫不記錄細節。 |
| 2026-07-28 | Anthropic Status 通報 Opus 5／Haiku 4.5 錯誤率升高（07-27 13:42–約 14:34 UTC，約 52 分鐘後恢復基準值）；已知問題互動數更新：跨平台多帳號連結訴求（issue #27302，419→452 個讚，本日全站互動量最高）、常駐顯示 thinking 功能請求（issue #8477，348→351 個讚）；新增已知問題 3 則：Claude Code 部分場景卡住/凍結 5–20 分鐘以上（issue #26224，149 個讚）、Windows 11 Pro 缺少 HCS 服務 vfpext 導致 Cowork 無法使用（issue #74649，6 個讚）、Cowork VM 在 Windows ARM64（Snapdragon）無法啟動（issue #40198，13 個讚）；Hacker News 討論官方資料使用政策文件（`code.claude.com/docs/en/data-usage`），釐清消費版（Free/Pro/Max）與商用版（Team/Enterprise/API/第三方平台/Claude Gov）訓練資料使用差異，已補充於「Session 歷史 30 天自動刪除」條目。 |
| 2026-07-26 | Anthropic 官方部落格正式證實 Claude 5 世代模型（含 Opus 5）已移除逾 80% 的 Claude Code 系統提示詞、改採新版 context engineering 原則（HN 393 分，前日僅為低互動傳聞，今日轉為官方正式敘述，仍非具體可設定功能；同日 Hacker News 另有討論指出二進位中含僅針對 Opus 5 的兩行硬編碼限制（非經請求不得用 AgentTool／workflows／deep-research），未經官方證實。Opus 5 全平台正式上線首日，Anthropic Status 接連出現 4 起模型錯誤率事件（Opus 5／Fable 5／Sonnet 5／Sonnet 4.6／Haiku 4.5 等組合），均於 10 分鐘至約 1 小時內排除。新增已知問題 5 則：API 連線頻繁中途中斷（issue #69415）、經常誤判所在工作目錄（issue #1669）、Microsoft 365 Connector 僅限 Team／Enterprise 方案（issue #20469，60 則留言、105 個讚）、訊息佇列模式功能請求（issue #50246，40 則留言、182 個讚）、Dispatch 主對話持續顯示離線（issue #45937，37 則留言）；互動數更新：AGENTS.md 支援訴求（issue #6235）攀升至 5760 個讚，居全站已知問題讚數之冠。 |
| 2026-07-25 | **v2.1.220** 為純 bug fix / reliability 版本；新增已知問題 3 則：自陳分析缺口未真正阻擋輸出（issue #60226，47 則留言）、Fable 5 於 Max 方案持續要求 usage credits（issue #79337，42 則留言、15 個讚）、context compaction 間缺乏持久記憶（issue #34556，61 則留言、5 個讚）；Reddit 單一來源回報 Opus 5 於 Claude Code Desktop 的 xhigh 推理強度因思考功能被強制關閉而失效（上線當天新增問題，待更多佐證）；Hacker News 轉述一則低互動（16 分）推文稱 Anthropic 為 Opus 5／Fable 5 移除逾 80% 系統提示詞；此傳聞已於次日（07-26）由 Anthropic 官方部落格（member of technical staff Thariq Shihipar，07-24 發文）正式證實，見下方 07-26 條目。 |
| 2026-07-24 | SDK 新增 API stop reason `model_continue`（anthropic-sdk-python v0.119.0、anthropic-sdk-typescript sdk-v0.114.0，皆 2026-07-23）。The Verge、TechCrunch、9to5Mac、Engadget、the-decoder.com、SQ Magazine 六家媒體同步報導 **Claude 語音模式（Voice Mode）全面開放 Opus／Sonnet 模型選擇**，昨日 TestingCatalog 的預告獲跨媒體確認。Tech Times 確認 v2.1.216（07-20）已修復 Auto Mode 長會話持續累積的二次方效能衰退。Anthropic Status：Opus 4.8 錯誤率升高（09:09 UTC 調查中，10:22 UTC 解決）。新增已知問題 1 則：Windows 11 Pro CoworkVMService 簽章驗證初始化失敗無法啟動（#29941，39 則留言）；互動數更新：RTL 排版請求（#38005，34→40 則留言、93→105 讚）、API Connection closed mid-response（#69415，32→33 則留言）、macOS Filesystem extension tools/call 未派發（#80002，59→61 則留言）。Reddit 使用者反映 Claude Security 外掛（Beta）無 Workflow tool 存取權限；查證確認為既有 opt-in 設計（Pro 方案須於 `/config` 手動開啟「dynamic workflows」，Max／Team／Enterprise／API 預設已開啟），非缺陷，已結案（2026-09-20，見 [[entities/claude-security]]）。IT Brief Australia 報導「Agent Island」讓 Claude Code 狀態資訊保留在本機；2026-08-10 查證確認它是第三方開源工具（MIT 授權，非官方產物），提供 Claude Code／Codex 本機 session 監控面板，不涉及資料外傳。 |
| 2026-07-22 | **v2.1.217**：新增 prompt input 表情符號 shortcode 自動完成（`:heart:` 插入 ❤️、`:hea` 顯示建議清單），可透過 `emojiCompletionEnabled` 關閉；官方 changelog 另提及新增警告訊息，原文截斷。同日 anthropic-sdk-python v0.117.1（修復 AWS 憑證處理邏輯）、anthropic-sdk-typescript sdk-v0.112.5（Chores，原文截斷）發布，皆為純修正／內部維護。**v2.1.218**（同日發布，07-23 補記）：`/code-review` 改為以背景 subagent 執行，不再佔用對話內容，維持 stacked slash commands 為審查對象；另有螢幕報讀軟體無障礙改善，原文於「Added screen-reade[r]…」處截斷。同日 anthropic-sdk-python v0.118.0 新增 Managed Agents 相關 API 支援（見 [[entities/managed-agents]]）、anthropic-sdk-typescript sdk-v0.113.0 新增 API 支援但原文於「add support」處截斷。互動數更新：Remote Control 自動重連失效（#34255，56→57 則留言、97→99 讚）、Thinking summaries 於 Opus 4.7 消失（#49268，補上 49 則留言，讚數持平 78）、`--screen-reader` 無障礙模式功能請求（#11002，58→63 則留言，讚數持平 38）。9to5Mac／MacRumors 與 07-23 的 Startup Fortune／Cult of Mac 四家媒體同步報導 Claude Code Mac app 可於 Apple 模擬器即時建置／測試 iOS App，惟當時無官方 release 或 blog 佐證版本與發布管道；2026-08-10 查證官方文件 [desktop-ios-simulator](https://code.claude.com/docs/en/desktop-ios-simulator) 已載明：Pro／Max／Team 可於 Desktop 內建 iOS Simulator 面板即時建置、執行、除錯 iPhone App（公開 Beta，僅限 macOS 本機 session，需已安裝 Xcode iOS 平台）。infoq.com 報導 Anthropic 說明如何在 Web、Code、Cowork 三介面圍欄化（contain）Claude 行為；2026-08-10 查證為官方自述其架構——以檔案系統／網路／執行環境的確定性邊界取代單純仰賴權限提示或模型層安全機制，屬架構說明而非新功能。 |
| 2026-07-23 | MarkTechPost 報導 Anthropic 發布 Claude Security 終端機內多代理漏洞掃描外掛 Beta 版；2026-08-10 查證確認此為對所有 Claude Code 使用者開放的終端機內 Beta 外掛（需付費方案 + v2.1.154 以上、`/config` 啟用 dynamic workflows），指令 `/claude-security` 提供掃描全庫／掃描異動／建議修補三項工作，與既有 Enterprise 版 Claude Security（企業管理主控台開關）屬互補而非重疊定位，見 [[entities/claude-security]]；TestingCatalog 報導 Claude 語音模式（Voice Mode）將新增 Opus／Sonnet 模型選項；2026-08-10 查證確認模型選擇器先前掛在介面上約 3 週但選誰都固定跑 Haiku（純裝飾），該日起選 Opus／Sonnet 才真正生效路由；Augment Code 報導回顧 v2.1.215（已於 07-19 記錄）聚焦「誰能掌控 agent 檢查清單」討論，無新增事實。本日新增 7 則已知問題：macOS Filesystem extension `tools/call` 未派發（issue #80002，59 則留言、27 個讚）、排程 routine 對 custom connector 呼叫 MCP 工具遭要求 approval（issue #61015，40 則留言、52 個讚，約 05-20 回歸）、無法複製 Claude Code 輸出文字（issue #62699，34 則留言、51 個讚）、`bypassPermissions` 模式未真正跳過權限檢查 META 彙整（issue #39523，33 則留言、18 個讚）、`autoMemoryEnabled=false` 未抑制記憶體前導文字（issue #63903，32 則留言）、API 連線中途關閉頻繁發生（issue #69415，32 則留言、69 個讚）、VS Code 擴充套件請求支援 `/btw` 指令（issue #37323，31 則留言、196 個讚）；既有已知問題更新：Session 額度續行請求（issue #13354，71 則留言、182 個讚，本日互動量最高）、VS Code 停用自動附加設定請求（issue #24726，61 則留言、189 個讚）。 |
| 2026-07-21 | **Anthropic Status**：Haiku 4.5 錯誤率升高（08:53 UTC，已解決）；Fable 5 錯誤率升高（11:47 UTC，仍在監控中，尚未見「已解決」時間戳）。Tech Times 報導稱 Claude Code 已修補 agentic 權限層中的 Bash 與 Unicode 繞過漏洞；2026-08-10 查證確認為 v2.1.216（07-20）修補的兩類繞過（Bash 複合語句重導向、PowerShell 隱形 Unicode 注入），另 v2.1.223（08-06）再修補 4 項相關權限邊界，詳見「已知問題」🛡️ 安全與隱私。GitHub Issues 高互動更新：Console 捲動回頂端（issue #826，353 則留言、821 個讚，本日互動量最高）、Rate limit reached 儘管訂閱 Max 且僅用 16%（issue #29579，新增，153 則留言、94 個讚）、`--screen-reader` 無障礙模式功能請求（issue #11002，新增，58 則留言、38 個讚）、記憶體洩漏 120GB+ OOM（issue #4953，97 則留言）、READ 工具檔案指示功能請求（issue #21151，133 則留言）、常駐顯示 thinking 功能請求（issue #8477，91 則留言、348 個讚）、OAuth 登入逾時（issue #33238，153 則留言）皆為既有已知問題的互動數更新。 |
| 2026-07-20 | **v2.1.216**：新增 `sandbox.filesystem.disabled` 設定（維持網路出口控管同時跳過檔案系統隔離）；同版修復長會話訊息正規化造成的效能退化。同日 anthropic-sdk-typescript v0.112.4（Bug Fixes：修復 AWS 相關欄位保留邏輯）發布，純修正未進 feature-radar。Anthropic Status 同日發生兩起服務事件：Opus 4.5 錯誤率升高（07:57–約 UTC 全日，已解決）、Fable 5 於 Max 方案誤判需耗用點數（07:35–15:35 UTC，已解決）、Opus 4.8 錯誤率升高（16:16 UTC，已解決），三起皆確認同日修復。 |
| 2026-07-17 | **v2.1.212**：⚠️ Breaking change——`/fork` 改為複製對話至新背景 session（`claude agents` 自成一列），原同 session 子 agent 功能更名 `/subtask`，無過渡期即刻生效。同日 TypeScript SDK v0.112.1（無 changelog 說明）、Python SDK v0.117.0（新增 dreaming API 支援，細節未知，疑似對應 [[entities/managed-agents]]）發布。The Verge、Engadget、SiliconANGLE、Help Net Security 同步報導 Claude 新增 1Password 整合，可用已存憑證登入網站且密碼不外流至 Claude/Anthropic。本日新增已知問題 4 條：`In-progress Call` 導致畫面閃爍（issue #769，335 個讚，全站互動最高）、VS Code 擴充套件請求新增停用自動附加開啟檔案/選取範圍設定（issue #24726，185 個讚）、Cowork 網路對外連線白名單失效（issue #30112，49 個讚）、Opus 4.7 thinking summaries 因 harness 未設定 `display: "summarized"` 而消失（issue #49268，78 個讚，見 [[entities/opus-4-7]]）；既有已知問題更新：終端機複製夾帶縮排/行尾空白（issue #18170，271→275 個讚）、Session 額度上限續行請求（統一併入 issue #13354，158→175 個讚，此前重複列為兩則條目已合併）、Cowork Edit/Write 緩衝區截斷檔案（補上 issue #53940 連結與確定性重現細節） |
| 2026-07-14 | **v2.1.210**：已折疊工具摘要行新增即時經過時間計數器；新增 `Write(path)` 相關啟動警告；原文摘要被截斷，內容有限，不進 [[feature-radar]]；claude.ai container creation 於 21:56–22:16 UTC 部分中斷，同日已解決；本日新增 6 則已知問題（Remote Control 自動重連失效 issue #34255、跨機器多 agent 協作功能請求 issue #28300、GitLab 整合功能請求 issue #12346、Environment Contributions 警告重複出現 issue #3301、VS Code LaTeX 渲染功能請求 issue #16446、VS Code diff 審閱 UI 功能請求 issue #33932），另更新 OAuth 登入逾時（issue #33238）與 GitHub Connector 未被識別（issue #32479）既有已知問題數據 |
| 2026-07-09 | **Reflect with Claude 測試版推出**：Settings 內新增使用模式儀表板，TechCrunch、Mashable、CNET、Axios、The Verge 多家媒體同步報導，多類比「AI 版 Spotify Wrapped」，TechCrunch 提出「悄悄推銷 AI」質疑角度；HN 29 分（見 [[feature-radar]]）|
| 2026-07-08 | **Claude Cowork 擴展至行動裝置與網頁版**：首波開放 Max 訂閱用戶，任務可在雲端持續執行，闔上筆電/關閉裝置也不中斷，此次擴展亦涵蓋政府機構客戶；官方表示「完整體驗」仍限桌面版；The Verge、TechCrunch、WIRED、NBC News、The New Stack、Let's Data Science 等多家媒體同步報導；Cowork 既有平台相容性已知問題是否延伸至新平台尚待觀察（見「已知問題」）|
| 2026-07-01 | **v2.1.197 Sonnet 5 正式成為預設模型**：Claude Code 預設切換至 Claude Sonnet 5，原生支援 1M token context window，促銷定價至 2026-08-31（後續：該到期日已於 2026-08-10 取消，$2/$10 永久化）；使用者升版後無需手動切換即享受完整 1M context（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.197)）|
| 2026-07-01 | **Enterprise Gateway 發布**：Anthropic 新增 Enterprise Gateway，簡化企業在 AWS 和 Google Cloud 上接入 Claude Code 的流程，降低大型組織的部署門檻（見 [DevOps.com 報導](https://devops.com/anthropic-adds-enterprise-gateway-to-simplify-claude-code-access-on-aws-and-google-cloud/)）|
| 2026-07-01 | **anthropic-sdk-python v0.115.0**：新增 Managed Agents API 支援，Python 開發者可透過 SDK 直接操作 Managed Agents 框架（見 [[entities/managed-agents]]）|

**版本表（發布超過 90 天的列）**

| 版本 | 發布日 | 重點 |
|------|------|------|
| **anthropic-sdk-python v0.120.2** | 2026-07-28 | Bug Fixes：**mcp** 支援 MCP SDK v2 與 v1 並存，純相容性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.120.2)）|
| **v2.1.220** | 2026-07-25 | Bug fixes and reliability improvements，官方 changelog 未列具體項目，純可靠性修正，無使用者端功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.220)）|
| **anthropic-sdk-python v0.119.0** | 2026-07-23 | Features：新增 API stop reason **`model_continue`**（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.119.0)）|
| **anthropic-sdk-typescript sdk-v0.114.0** | 2026-07-23 | Features：新增 API 支援，changelog 於「add new sto[p reason]」處截斷，研判與同日 Python SDK 的 `model_continue` stop reason 為同一異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.114.0)）|
| **v2.1.218** | 2026-07-22 | 將 `/code-review` 改為以**背景 subagent** 執行，審查工作不再佔用對話內容，維持 stacked slash commands 作為審查對象；新增螢幕報讀軟體相關無障礙改善，官方 changelog 於「Added screen-reade[r]…」處截斷，具體對應範圍未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.218)）|
| **anthropic-sdk-python v0.118.0** | 2026-07-22 | Features：新增 **Managed Agents** 相關 API 支援（見 [[entities/managed-agents]]，見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.118.0)）|
| **anthropic-sdk-typescript sdk-v0.113.0** | 2026-07-22 | Features：新增 API 支援，changelog 於「add support」處截斷，具體項目未知（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.113.0)）|
| **v2.1.217** | 2026-07-21 | 新增 prompt input 表情符號 shortcode 自動完成：輸入 `:heart:` 插入 ❤️，或輸入 `:hea` 顯示建議清單，可透過 `emojiCompletionEnabled` 設定關閉；官方 changelog 另提及新增警告訊息，原文於此處截斷，具體內容未知（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.217)）|
| **anthropic-sdk-python v0.117.1** | 2026-07-21 | Bug Fixes：修復 AWS 憑證處理邏輯（handle credentials correctly），純修正無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.1)）|
| **anthropic-sdk-typescript sdk-v0.112.5** | 2026-07-21 | Chores：新增 API 支援項目，原文於此處截斷，屬內部維護性更新（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.112.5)）|
| **v2.1.216** | 2026-07-20 | 新增 `sandbox.filesystem.disabled` 設定：可在維持網路出口控管（network egress control）的同時跳過檔案系統隔離；修復長會話中訊息正規化（message normalization）造成的效能退化問題；Tech Times（2026-07-23）報導確認此修復解決了 Auto Mode 最長工作階段中持續累積的二次方（quadratic）效能衰退問題（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.216)）|
| **anthropic-sdk-typescript v0.112.4** | 2026-07-20 | Bug Fixes：修復 AWS 相關欄位保留邏輯（preserve AWS...），純修正無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.112.4)）|
| **v2.1.215** | 2026-07-19 | ⚠️ **行為變更**：Claude 不再自動執行 `/verify` 與 `/code-review` 兩項技能，須由使用者手動呼叫 `/verify` 或 `/code-review` 才會觸發；依賴自動驗證/審查的既有工作流需改用顯式呼叫，無過渡期即刻生效（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.215)）|
| **v2.1.214** | 2026-07-18 | 修復 single-segment `dir/**` allow 規則（如 `Edit(src/**)`）誤自動核准樹狀結構中任意層級 `dir/` 目錄寫入的問題（原本應僅限 `<cwd>/dir`），並修復另一項相關權限問題（原文於此處被截斷，細節未知）；純安全性修正，無新指令/旗標（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.214)）|
| **anthropic-sdk-typescript google-cloud-sdk v0.0.6** | 2026-07-17 | Changelog 僅提供與前版的完整比較連結，未列出具體異動項目，純版本號更新，暫記版本表（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.0.6)）|
| **anthropic-sdk-typescript v0.112.3** | 2026-07-17 | Chores：docs 小幅調整，無使用者端功能異動（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.112.3)）|
| **v2.1.212** | 2026-07-17 | ⚠️ **Breaking change**：`/fork` 不再於同一 session 內啟動子 agent，改為將目前對話複製進一個新的**背景 session**（在 `claude agents` 中自成一列），使用者可同時繼續原本工作；原本 `/fork` 的同 session 子 agent 行為更名為 **`/subtask`**；依賴舊版 `/fork` 語意的腳本/工作流需改用 `/subtask`，無過渡期即刻生效（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.212)）|
| **anthropic-sdk-typescript v0.112.1** | 2026-07-16 | Changelog 未列出具體異動說明，純版本號更新，暫記版本表（見 [Release](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.112.1)）|
| **anthropic-sdk-python v0.117.0** | 2026-07-16 | 新增「api: add support for dreaming」；查證確認官方 changelog 全文即止於此句，未進一步說明技術細節（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0)，查證日 2026-09-20）|
| **v2.1.211** | 2026-07-15 | 新增 `--forward-subagent-text` 旗標與 `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` 環境變數：`stream-json` 輸出可包含 subagent 的文字與思考內容；修復一項權限相關問題（原文於此處被截斷，細節未知）（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.211)）|
| **v2.1.210** | 2026-07-14 | 已折疊工具摘要行新增即時經過時間計數器（長時間執行的工具呼叫不再看似卡住）；新增 `Write(path)` 相關啟動警告；來源原文於此處被截斷，僅此兩項變更可確認，暫無法判斷是否有其他異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.210)）|
| **v2.1.209** | 2026-07-14 | Bug fix：修復 `claude agents` 背景 session 中 `/model` 等對話框被過度廣泛的防護機制阻擋的問題（回退先前過寬的防護邏輯），純可靠性修正，無新功能異動（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.209)）|
| **v2.1.207** | 2026-07-11 | **Auto mode 在 Bedrock/Vertex AI/Foundry 三平台預設開啟**：不再需要 `CLAUDE_CODE_ENABLE_AUTO_MODE` 環境變數 opt-in，可透過設定中的 `disableAutoMode` 關閉；同版修復終端機凍結問題（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.207)）|
| **v2.1.206** | 2026-07-10 | `/cd` 新增目錄路徑建議（比照 `/add-dir` 的自動完成體驗）；`/doctor` 新增檢查項目，會建議精簡已 checked-in 的 CLAUDE.md 內容（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.206)）|
| **v2.1.204** | 2026-07-08 | Bug fix：修復 headless session 中 SessionStart hook 事件無法即時串流的問題；此問題先前可能導致遠端 worker 在 hook 執行中途被系統誤判為閒置而回收（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.204)）|
| **v2.1.202** | 2026-07-07 | `/config` 新增 **Dynamic workflow size** 設定：可調整動態工作流（Dynamic Workflows / `ultracode`，見 [[feature-radar]]）的 agent 數量規模（小/中/大），屬建議性引導值（非硬上限）（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.202)）|
| **v2.1.201** | 2026-07-03 | Claude Sonnet 5 session 不再使用對話中途的 system role 插入 harness 提醒訊息（改變 reminder 注入機制的行為調整）；其餘為一般性小幅修正（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.201)）|
| **anthropic-sdk-python v0.115.0** | 2026-07-01 | 新增對 Managed Agents 的 API 支援（見 [[entities/managed-agents]]）|
| **anthropic-sdk-typescript vertex-sdk v0.19.0** | 2026-07-01 | Vertex SDK TypeScript 版本更新 |
| **v2.1.197** | 2026-07-01 | **Claude Sonnet 5 成為新預設模型**，原生支援 **1M token context window**，促銷定價至 2026-08-31（後續：該到期日已於 2026-08-10 取消，$2/$10 永久化）；使用者無需手動切換，所有新 session 即享 1M context（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.197)）|

## 2026-08

| 日期 | 事件 |
|------|------|
| 2026-08-30 | 新增已知問題 5 則——Claude Desktop（Windows）反覆當機需「進階選項→修復」（issue #85199，40 則留言）；功能請求 `--quiet` 旗標抑制互動模式工具呼叫輸出（issue #9340，32 則留言、47 個讚）；context window 狀態列對 Sonnet 4.6 僅顯示 200k、實際支援 1M（issue #61734，24 則留言）；已付費 Max 帳號登入後仍被導向新帳號 onboarding，第 10 次公開通報、首度捕捉封包層級觸發機制（#83633，22 則留言）；The Register 揭露僅需請 Claude Code 摘要一個網址，即可誘發它信任 llms.txt 內容而產生非預期行為（產品層攻擊面，已列入「🛡️ 安全與隱私」）。互動數更新：GitHub connector 帳號全域讀不到內容（#71542，48→60 則留言，今日全站聚焦頭條）；Opus 5 Auto Mode 繞過事件補上 Cybernews 後續——在野案例中 Claude 曾嘗試修復被植入的惡意程式碼但遭拒絕執行。Anthropic 宣布標準週配額自 2026-09-14 起永久調高 25%（Pro／Max／Team／座位制 Enterprise），同時取消目前暫行的 +50% 加成，相較「目前」水位實為減少約 17%（見 [[feature-radar]]「⏰ 倒數中」與 [[entities/pricing]]）。 |
| 2026-08-29 | （涵蓋 08-28～08-29，08-28 未抓到料）**v2.1.250** 發布，純可靠性修正，無使用者端功能異動。anthropic-sdk-typescript sdk-v0.122.0、anthropic-sdk-python v1.2.0 同步將 beta 版 files／skills 命名空間改用正式版（GA）介面形狀。Claude Help Center release notes 補述 8/6 更新：Enterprise 方案新增 Skill／外掛安全掃描（beta），屬背景自動機制。互動數更新 3 則：Max 方案額度自 3 月起異常快速耗盡（#38335，807→837 則留言）、AGENTS.md 規範不支援（#6235，384→385 則留言、6496→6525 讚）、社群請願恢復 `/buddy`（#45596，265→268 則留言、2068→2076 讚）。Anthropic 部落格發布「Model Hardware Standard」研究預覽（統一介面供 Claude 代理人操作機器人與科學實驗室儀器），該階段尚無使用者可實際取用的操作。**同日後續：** **v2.1.251** 發布，新增 PreModelSwitch／PostModelSwitch hook 事件與 SessionStart resume hook 新鮮度回傳。官方桌面版文件再新增 3 段：adaptive reasoning 模型上 `MAX_THINKING_TOKENS` 非預設值時的行為、跨 session 傳訊卡片標示傳送方、extended thinking 現為預設啟用。Anthropic Status 通報 Claude Cowork 與 Claude Code on the web 錯誤率升高，已解決。新增已知問題 3 則：session 端無法得知 auto-memory 索引是否完整載入、遭截斷或未載入（#82056，47 則留言、1 讚）；Claude Desktop（Windows 11）主視窗持續蓋在其他應用程式最上層且無設定可關（#85891，41 則留言、92 讚）；功能請求——Claude Code Web 支援從非預設分支啟動 session（#10018，59 則留言、162 讚，今日全站互動量最高功能請求）。互動數更新 2 則：Windows 11 Pro 缺少 HCS 服務 vfpext 導致 Cowork 無法運作（#74649，6→7 讚，今日 GitHub Issues 討論度最高）、GitLab 整合功能請求（#12346，47→50 則留言、131→135 讚）。XDA（經 Google News 轉載）報導使用者實測發現輸入第一個提示前即耗用約 51,000 token 並自行排查修正，僅標題可用。 |
| 2026-08-27 | **v2.1.247** 發布，新增 `SendFeedback` 工具（session 出錯時 Claude 可草擬回報供使用者於 `/feedback` 檢視後送出，`feedbackDisabled` 可關閉）。新增已標記懸置的已知問題 1 則：Reddit 使用者觀察到 "fork" subagent 每次工具呼叫皆重送整段對話歷史，四個平行子代理耗用約 200 萬 tokens，未經官方證實。互動數更新 2 則：AGENTS.md 規範不支援（#6235，335→384 則留言、5889→6496 讚，今日全站互動數最高的 GitHub Issue）、API Error: Connection closed mid-response（#69415，44→55 則留言、82→91 讚）。 |
| 2026-08-25 | **v2.1.245** 發布，修復搭載 glibc 2.44 的 Linux 發行版（例如 Arch Linux、CachyOS、Fedora Rawhide）上啟動時發生的當機問題，純 bug fix，無新指令/旗標。互動數更新 3 則：模型行為模式回報——`/goal` stop-hook 指令被引用作未授權動作依據、搜尋不到即視為不存在、質疑下用結構取代實質內容（issue #60705，107→137 則留言，今日全站互動量最高之 GitHub Issue，依懸置標記語法加註 `｜訊 2026-08-25`）；功能請求——訊息佇列模式，排入佇列而非中斷進行中任務（issue #50246，40→67 則留言、218→236 個讚，今日互動量次高）；Linux 上持續產生 Windows 換行 CRLF 檔案（issue #2805，47→52 則留言、33→35 個讚）。 |
| 2026-08-24 | 新增已知問題 1 則：Windows/MSIX 1.28929.0 跨 session 訊息會送進目標 session 輸入框卻不會自動送出，該 session 從此無回應（issue #86069，8 個讚）。互動數更新 4 則：Desktop 多視窗支援功能請求（issue #30154，215→238 個讚）、CLI TUI 無法捲動回看對話歷史（issue #28077，75→80 個讚）、跨機器多 agent 協作 A2A 協定功能請求（issue #28300，補上 41 個讚）、關閉啟動歡迎畫面功能請求（issue #2254，126→138 個讚）；提示卡住/凍結 5–20 分鐘以上（issue #26224）今日日報再度標為全站互動量最高之 GitHub Issue，惟讚數維持 150 未變，不構成新互動數更新。 |
| 2026-08-23 | **v2.1.241** 發布，release notes 僅載明「Bug fixes and reliability improvements」，純可靠性修正。Hacker News 討論串（191 分）回報 Opus 5 在簡單任務上耗時異常長（43 分鐘 vs 4.6 版 < 2 分鐘）；Anthropic Claude Code 團隊 Thariq 具名回應：正測試一項 API serving 設定、改變 effort 數值的顯示方式，使用者實際選到的 effort 等級未變，與標題「reduced effort levels」的框架不完全一致。同日 Reddit 另有使用者反映「新分類器」讓表現變差（單一低分來源，僅作背景參考）。新增已知問題 1 則：功能請求——允許自訂 `.claude/agents/` 定義加入 agent team 作為隊友（#24316，41 則留言、43 讚）。互動數更新 4 則：CVP 核准組織仍遭資安防護誤擋（#84352，69→141 則留言、9→22 讚，今日全站已知問題互動量最高）、貼上文字自動收合功能請求（#23134，補上 47 則留言、137→151 讚）、VS Code LaTeX 渲染功能請求（#16446，35→42 則留言、122→138 讚）、Post/PreToolUse Hooks 未如預期觸發（#6305，38→40 則留言）。官方文件索引（`code.claude.com/docs/llms.txt`）新增 2 頁「本週新功能」（Week 33：8/10–14、Week 34：8/17–21），實際內容待查。官方第三度更新 Claude Code Desktop 說明頁，內容仍為既有功能清單（並行 session／Git 隔離、拖放式面板配置、內建終端機與檔案編輯器、side chat、電腦操作、行動端 Dispatch session、視覺化 diff 審查、app 預覽、PR 監控、connectors、企業設定），未見新指令／旗標。 |
| 2026-08-22 | **v2.1.239** 發布，Cost estimates（`/cost`、狀態列、`--max-budget-usd`）現會計入資料常駐（data-residency）工作區的 1.1 倍純美國推理附加費，屬既有成本顯示機制的計算口徑調整；同版另有一項全螢幕渲染器相關設定調整，官方 changelog 原文於此處截斷，細節未知。新增已知問題 2 則：一般開發操作（讀檔、編輯程式碼、執行 git 指令）在數分鐘內即異常耗盡 token／配額（issue #42249，44 則留言、17 個讚）；Claude 在應優先使用 Read／Grep 等內建工具的情境下仍頻繁改用 Bash 指令如 sed/grep，屬既有行為模式而非單一事件（issue #19649，45 則留言、101 個讚）；同步新增 1 則平台相容性已知問題：Claude Desktop 1.1.3189 於 Windows 上出現嚴重 UI 延遲與滑鼠卡頓，為更新後效能退化（issue #26302，44 則留言、44 個讚）。互動數更新 2 則：Max 訂閱方案立即觸及用量上限（issue #16157，1483→1488 則留言、722→724 個讚，2026-08-22 再度列入今日聚焦［持續追蹤］）、要求幾乎每天重新網頁驗證登入（issue #1757，補上留言數 79 則、74→69 個讚）。官方文件索引（`code.claude.com/docs/llms.txt`）新增 3 頁：Deploy managed settings、Example settings files、Claude Code settings reference，屬頁面增減偵測，實際內容尚未查證，暫不建立對應條目。Claude Mythos 5 整合進 Claude Security 事件（企業團隊免直接存取模型即取得前沿等級漏洞掃描能力）已記入 [[entities/claude-security]]，非本頁範圍。 |
| 2026-08-21 | **v2.1.238** 發布，新增 `keybindingFlavor` 設定：設為 `"readline"` 時可讓提示列中的 Ctrl+W 依 Bash 慣例刪除到前一個空白字元，預設值 `"classic"` 行為不變。同日 anthropic-sdk-python 正式發布 **v1.0.0**，⚠️ **Breaking change**：client 升級至 httpx2，官方未提供明確遷移時程，僅建議升級前查閱完整 changelog。已知問題互動數更新 1 則：Cowork VM 於 Windows ARM64（Snapdragon）無法啟動（issue #40198，13 個讚 → 68 則留言／反應）；新增已知問題 1 則：多起 API 連線錯誤彙整回報（issue #4297，48 則留言／反應，Windows 11、Anthropic API 平台）。Official Docs 再次更新 Claude Code Desktop 說明頁（`code.claude.com/docs/en/desktop.md`），內容涵蓋既有已追蹤功能（並行 session／Git 隔離、拖放式面板配置、內建終端機與檔案編輯器、side chat、電腦操作、行動端 Dispatch session、視覺化 diff 審查、app 預覽、PR 監控、connectors、企業設定），與 08-18 該頁首次記錄時同屬既有功能彙整、未見新指令/旗標。Anthropic Status 通報 2 起同日已解決事故：多模型請求錯誤升高（08-20 19:16–19:42 UTC）、Google connectors（Sheets/Docs/Slides/Chat）錯誤升高（08-20 18:32–19:01 UTC），皆同日修復，重要性低未列入已知問題。 |
| 2026-08-20 | **v2.1.237** 發布，修復使用 LLM gateway 或自訂 base URL 的 session 中 prompt caching 失效問題，並新增內建「Concise」輸出風格（Claude 直接給結果、省去前言與敘述性文字）。同日 anthropic-sdk-python v0.125.0 新增 managed agents 的 web search 設定相關功能，已同步更新 [[entities/managed-agents]] 並提報 [[feature-radar]]；anthropic-sdk-typescript vertex-sdk v0.19.5／google-cloud-sdk v0.0.10（Chores，無使用者端功能異動）暫記版本表。新增已知問題 2 則：修改 thinking block 觸發 API Error 400（issue #10199，100 則留言、65 個讚）；v2.1.113 起原生二進位改依賴 glibc、無 JS fallback，Termux（Android）環境完全無法使用，屬破壞性回歸（issue #50270，67 則留言、60 個讚）。互動數更新 3 則：Cowork 建立 10GB VM bundle 效能退化（issue #22543，補上 259 個讚）、進程記憶體洩漏 120GB+ OOM（issue #4953，73→75 個讚）、Cowork「Failed to start Claude's workspace」VM service not running（issue #27801，71→73 則留言、40→41 個讚）。Reddit r/ClaudeAI 週熱門貼文回報 Claude Code 已新增「額度重置後自動繼續」功能，與既有功能請求 issue #13354 同主題，已於該條註記社群回報但未見官方 changelog 確認，暫不改列已修復。 |
| 2026-08-19 | **v2.1.235** 發布，新增可選 `spellcheck` 設定（透過本機 aspell／hunspell／ispell 即時在輸入框標出拼字錯誤），並修復一項與整段提示詞（whole-prompt）相關的問題（官方 changelog 原文截斷，細節未知）。Anthropic Status 通報二度效能異常：8/18 16:11–18:23 UTC 多款模型效能下降，19:01 UTC 確認解決；8/19 09:42 UTC 起 Opus 5、Haiku 4.5 再度效能異常，10:33 UTC 已實施修復方案並監控中，尚未標記已解決；Startup Fortune、SQ Magazine、GV Wire、Asbury Park Press 等多家媒體同步報導用戶端「容量已滿」錯誤與 Downdetector 回報量大增。官方文件索引（`code.claude.com/docs/llms.txt`）移除 1 頁「Slash Commands in the SDK」，屬頁面增減偵測，是否代表功能實際移除仍為懸置，已標於「現況」。官方 Skills 清冊今日核對：昨日新增的 `claude-academy-guide` 已改名為 `academy-guide`（`discernment-nudge` 不變），詳見 [[entities/claude-skills]]。已知問題新增 1 則：Windows 桌面版開啟內建瀏覽器分頁發生致命 GPU 當機（錯誤碼 0x060C201E），MSIX 應用崩潰後卡在 appxState=2 需 Repair（issue #80444，5 個 reactions、43 則留言）；互動數更新 2 則：工作目錄追蹤暫存檔未清理（issue #8856，70 個 reactions、新增 111 則留言）、Linux 剪貼簿貼圖失敗（issue #8324，41→42 個 reactions、43→44 則留言）。新增懸置標記 1 則（現況）：9to5Mac 報導 Claude Cowork 現已於所有付費方案行動版上線，僅標題可用、未見官方公告佐證。 |
| 2026-08-18 | **v2.1.234**（報導日；發布日 08-17 見版本表）發布，新增可選環境變數 `CLAUDE_CODE_PROJECT_DIR_NAME`，讓每個 session 有獨立設定目錄的主機（如 CI／多租戶執行環境）可為專案 transcript 目錄自訂短名稱，官方 changelog 原文截斷。Anthropic Status 通報 Opus 5、Sonnet 5 短暫效能降級（8/17 14:25 UTC 起 → 15:29 UTC 確認解決）。官方 Skills 清冊新增 2 項：`claude-academy-guide`、`discernment-nudge`，詳見 [[entities/claude-skills]]。已知問題互動數更新 3 則：Windows Desktop 孤兒程序檔案鎖無法 Relaunch（issue #42776，116→122 則留言、39→59 個讚）、Remote Control 自動重連失效（issue #34255，63→65 則留言、103→104 個讚）、Windows 主控台視窗閃爍（issue #14828，47→62 則留言、35→36 個讚）；新增功能請求 2 則：OAuth／第三方流程外部 URL 白名單設定（issue #27263，52 則留言、131 個讚）、刪除 Claude Code session（issue #13514，47 則留言、110 個讚）。新增懸置標記 2 則（現況）：the-decoder.com 報導 Claude Code 新增 `/design` 指令可於終端機建立 UI mockup（同步標記於 [[entities/claude-design]]）；Tech Times 報導 Anthropic 已下線 Claude Workbench，既有已儲存 prompt 消失、API pipeline 隨之中斷；兩則皆單一媒體來源，未見官方公告佐證。Official Docs 更新 Claude Code Desktop 說明頁（三分頁 Chat／Cowork／Code），內容涵蓋既有已追蹤功能（Git 隔離並行 session、電腦操作、Dispatch session、PR 監控、connectors 等），未見新指令/旗標。ALM Corp 報導 Auto 模式預設化，屬既有已於 08-10 官方確認事實（見 08-14 生效條目）的媒體重複報導，非新訊號，未另行記錄。 |
| 2026-08-17 | Anthropic Status 通報 8/16 晚間服務中斷，影響 claude.ai、platform.claude.com、Claude API、Claude Code、Claude Cowork，22:34 UTC 確認修復；BleepingComputer 等多家媒體同步報導同一事件。已知問題互動數更新 3 則：常駐顯示思考過程功能請求（issue #8477，91→93 則留言、351→356 個讚）、送出前編輯「已貼上文字」功能請求（issue #3412，82→83 則留言、305→307 個讚）、印度盧比定價功能請求（issue #17432，210→212 則留言）。新增懸置標記 2 則（現況）：TestingCatalog AI News 報導 Anthropic 據傳為 Claude Desktop 開發類 Slack 功能、為 Cowork 新增內建網頁瀏覽器（「超級應用」方向），皆未經官方證實。Reddit 貼文指稱排程任務（scheduled tasks）遭自動切換至 Fable 5 並消耗大量額度，惟 sort=new 且 score=0、無跨來源佐證，暫不列入已知問題。 |
| 2026-08-14 | **v2.1.232** 發布，Subagent forking 預設開啟——帶 `subagent_type: "fork"` 的 subagent 現在預設繼承完整對話與 prompt cache，互動 session 中非 teammate 的 agent 任務指派行為亦有相應調整（官方 changelog 原文於此處截斷，細節未知）。同日 anthropic-sdk-typescript vertex-sdk v0.19.4（Chores，無具體功能異動說明）、anthropic-sdk-python v0.122.0（Features，新增 API `output_behavior` 欄位支援於 dream creation，2026-09-20 查證確認官方 changelog 原文完整、非截斷，詳見版本表 ⟨Q-14⟩）發布，暫記版本表。Anthropic Status 通報 2 起事件：Claude Code on the web 與相關服務效能下降（08-13 23:42 UTC 起 → 08-14 00:51 UTC 確認解決）；status.claude.com 網站本身一度無法連線（08-14 07:58–10:53 UTC，屬狀態頁自身存取問題，非 Claude 服務本身故障，重要性極低，未列入已知問題）。已知問題互動數更新 4 則：AGENTS.md 規範不支援（issue #6235，5760→5889 個讚，今日全站已知問題讚數最高）、Desktop app 多帳號管理與快速切換（issue #18435，769→819 個讚）、Max 方案額度自 3 月起異常快速耗盡（issue #38335，538→543 個讚）、GitHub Connector 已連結卻未被識別（issue #32479，130→138 個讚）。新增已知問題 1 則（懸置標記，詳見「現況」）：The Register 報導 Claude Code 回傳空白思考區塊但推理 token 仍照常計費，僅標題可用、無正文佐證，計費爭議面另見 [[entities/pricing]]。InfoWorld 報導 VS Code 1.133 為 Claude 相關工作階段帶來更彈性操作方式，Google News RSS 僅提供標題與連結片段，無正文說明具體改動內容，答不出使用者可執行的具體操作，暫不收錄 feature-radar。 |
| 2026-08-13 | **v2.1.231** 修復 MCP OAuth 登入失敗問題——使用預先註冊 OAuth client 的伺服器（如 Slack）先前因 redirect URI 不符而登入失敗；純 bug 修復。新增已知問題 2 則：Claude in Chrome 瀏覽器擴充功能無法連接本機 Claude Code CLI（issue #20298，51 則留言、41 個讚，環境 Claude Code v2.1.17）、獨立 macOS 介面缺乏關閉自動建立 worktree 選項功能請求（issue #12513，47 則留言、80 個讚）；既有已知問題互動數更新 4 則：內建 Slack MCP connector 多帳號連結訴求（issue #27302，222→227 則留言、454→480 個讚）、Skills 支援子目錄結構功能請求（issue #10238，補上 50 則留言、165→167 個讚）、Environment Contributions 警告重複出現（issue #3301，43→45 則留言、81→83 個讚）、官方 Linux Desktop build 功能請求（issue #65697，累積反應 651→655）。Engadget（經 Google News 轉載）報導 Claude Cowork 現可於 Chrome 側邊欄執行，僅有標題可用、無正文佐證，已標記懸置（見上方「現況」）。 |
| 2026-08-12 | 新增已知問題 1 則：已通過 CVP 審核的組織在 Claude Code 中再度被資安防護機制誤擋（issue #84352，69 則留言、9 個讚）；標記懸置 1 則：Claude Code 經 curl 送出的 User-Agent 字串疑似洩漏使用者真實 email（issue #78431，經 Hacker News 轉發 38 分，2026-08-11 報導）。 |
| 2026-08-11 | Auto Mode 8/14 預設化持續獲多家媒體接力報導（含 Mashable），確認官方 8/10 宣布內容在社群媒體圈持續擴散；官方文件索引（code.claude.com/docs/llms.txt）新增兩頁「本週新功能」記錄（Week 30：7/20–24、Week 32：8/3–7），屬頁面增減偵測，實際內容待後續查看確認是否含未公開異動。v2.1.227（2026-08-10）修復 bug：session 以過期登入 token 啟動時，feature flag 未依訂閱層級正確評估，曾導致 Max 方案使用者被誤導提示啟用相關功能，純 bug 修復。 |
| 2026-08-10 | Anthropic 官方部落格（claude.com/blog/auto-mode-default-in-claude-code，經 Hacker News 轉發 227 分）正式宣布 **2026-08-14** 起 auto 模式成為 Pro／Max／Team 方案新 session 的預設權限模式（已自行設定過個人預設或釘選預設者不受影響，會收到一次性提示詢問是否切換；Enterprise 與 API／雲端平台不在本次範圍），並宣布即日起不再對 auto 分類器產生的額外 token 用量收費；Reddit 週熱門貼文引述對 1,053 名付費測試者的對照研究，指 auto 模式攔下 89% 危險指令、人工逐一審核僅攔下 13.6%，為官方訪談單方陳述補上量化佐證，已同步更新 [[feature-radar]]。已知問題新增 1 則：Max 20 方案升級至 v2.1.198 後額度重置僅約 70 分鐘即 100% 用盡，此前版本未曾發生（issue #41788，60 則留言）；互動數更新 5 則（詳見「已知問題」對應條目）。 |
| 2026-08-09 | Claude Code 跨 session 訊息互通功能經官方文件（code.claude.com/docs/en/cross-session-messaging，經 Hacker News 連結揭露）正式確認，需 v2.1.224 以上版本、限 macOS／Linux，工具為 `ListAgents`＋`SendMessage`，同機制涵蓋 subagent／team 內部訊息；解除 08-08 媒體報導階段的不確定狀態，已知問題 #24798 狀態轉為 ✅ 已修復 v2.1.224，並同步更新 [[topics/official-community-gap]]「Agent 間直接通訊協定」列。Anthropic 產品負責人 Cat Wu 就 2026-08-14 Auto Mode 預設化受訪表示（The New Stack）：已大致緩解主要風險類別攻擊、近期將發布評測數據，並稱 Anthropic 內部幾乎人人使用 Auto Mode；the-decoder.com 同步報導，生效範圍不變，已同步 [[feature-radar]]。新增已知問題功能請求 1 則：跨 session 持久記憶（issue #14227，34 則留言、11 個讚，與既有跨 compaction 持久記憶 issue #34556 合計 96 則留言）；另收錄 1 則未經證實的問題：GitHub Issue 處理時 prompt 過長（issue #23377，43 則留言、38 個讚，僅標題可判斷）；既有已知問題互動數更新 4 則：VS Code `/btw` 指令支援請求（issue #37323，31→35 則留言、196→216 個讚，今日日報互動量最高）、Desktop App 遠端控制請求（issue #29006，補上互動數 36 則留言、158 個讚）、圖片處理失敗浪費額度（issue #60334，補上互動數 72 則留言、19 個讚）、跨 compaction 持久記憶（issue #34556，61→62 則留言、5→6 個讚）。 |
| 2026-08-08 | **v2.1.226** 為純 bug fix／穩定性改進版本；anthropic-sdk-python v0.121.0（Features，新增 `mid-conversation-tool-changes-2026-07-01` beta，2026-08-10 查證確認為對話中途異動工具而不使 prompt cache 失效的 API）、anthropic-sdk-typescript google-cloud-sdk v0.0.7（2026-08-10 查證確認為 Bug Fixes，User-Agent 固定字串修正）、vertex-sdk v0.19.1（Bug Fixes）三則 SDK 更新（皆 2026-08-07）暫記版本表。Anthropic 宣布 2026-08-14 起將 auto 模式設為 Claude Code 預設權限模式（HN 轉引 @ClaudeDevs 推文／9to5Mac PSA 同步報導）；MacRumors、The Mac Observer、biggo.com、Inshorts、9to5Mac 五家媒體同步報導 Claude Code 新增跨 session 訊息互通功能（macOS/Linux），GitHub release 無對應 changelog 佐證，已同步更新 [[topics/official-community-gap]] 並提報 feature-radar。新增已知問題功能請求 1 則：跨分支 diff 比較（issue #23626，38 則留言、120 個讚，今日互動最高功能請求）；既有已知問題互動數更新 4 則：API 連線中途中斷（issue #69415，33→44 則留言、69→82 個讚，本日全站互動量最高）、`autoMemoryEnabled=false` 未抑制記憶體前導文字（issue #63903，35→40 則留言）、跨機器多 agent 協作 A2A 協定（issue #28300，35→36 則留言）、內建 Slack MCP connector 多 workspace 功能請求（補上 issue #44243 編號，33→36 則留言、69→78 個讚）。 |
| 2026-08-07 | **v2.1.224** 新增 `claude self-hosted-runner` 指令，可將自有機器或容器轉為 Claude Code web／mobile／desktop session 執行環境，開放 Team／Enterprise 方案（Google News／Unite.AI 同步轉載）。Claude API Release Notes（2026-08-05）新增 **Inference Hooks**，進入 Enterprise 組織 beta，受管治 prompt 可導向企業自有 AI 安全伺服器。Anthropic Status 通報 Claude Opus 5 請求錯誤率升高（08-05 13:51 UTC 確認原因並著手修復，14:34 UTC 標記已解決）。新增已知問題 1 則：上傳過大圖片導致對話永久卡死、無法在不開新對話情況下復原（issue #13480，111 則留言、90 個讚）；既有已知問題互動數更新 2 則：終端機複製夾帶多餘縮排/行尾空白（issue #18170，131→134 則留言、275→283 個讚）、Fable 5 於 Max 方案持續要求 usage credits（issue #79337，42→67 則留言、15→25 個讚）。另有低知名度媒體（techtimes.com）以「164th outage」聳動標題報導穩定性問題，惟官方 Status 頁僅顯示 2 起獨立事件且皆已解決，其框架與事實不符，暫不收錄、不引用其說法。 |
| 2026-08-05 | **v2.1.222**（報導日；發布日 08-04 見版本表）修復 worktree-isolated session 與其 subagent 可對主 checkout 執行破壞性 git 指令的隔離漏洞，隔離範圍擴大至每個 session 的檔案編輯與 Bash 執行。Anthropic Status 新增 2 起事件：08-04 21:04–21:59 UTC 帳號登入失敗，已解決；08-05 07:05 UTC 起 Claude Mythos 5、Fable 5 等多模型效能降級，09:13 UTC 彙整時仍在處理中，尚未確認解決（另有 Benzinga 等媒體同步報導使用者反映服務異常）。新增已知問題 1 則：社群提案呼籲開放 compact／session 生命週期 hook 供外部記憶層串接，彙整既有 5 個持久化記憶相關 issue（#14227、#32627、#34192、#34556、#46138）（issue #47023，41 則留言、4 個讚）；既有已知問題互動數更新 1 則：RTL（希伯來/阿拉伯文）排版支援請求（issue #38005，40→41 則留言、105→111 個讚）。 |
| 2026-08-04 | v2.1.221 為 VSCode 擴充新增 Focus view（`Ctrl+Alt+F` 切換）。已知問題新增 1 則：使用者反映幾乎每天都須重新透過網頁驗證登入（issue #1757，74 個讚）。互動數更新 6 則：Max 訂閱瞬間觸及用量上限（issue #16157，1480→1483 則留言，今日聚焦頭條）；提示卡住 5–20 分鐘以上（issue #26224，149→150 個讚，新補 128 則留言，今日聚焦頭條）；Session 額度上限自動續行功能請求（issue #13354，182→193 個讚）；claude.ai visualize 功能故障（issue #34820，94→96 則留言）；Cowork 網路白名單失效（issue #30112，49→51 個讚，新補 54 則留言）；GitHub connector 帳號全域讀不到內容的迴歸問題確認為 issue #71542（37→48 則留言、33→43 個讚）；Linux 上持續產生 Windows 換行檔案（issue #2805，39→47 則留言、32→33 個讚）。另 Anthropic Status 於 08-03～08-04 出現 3 起短暫錯誤率事件，均同日確認解決，未列個別條目。 |
| 2026-08-02 | 新增已知問題 4 則：Max 5x 升級至 Max 20x 失敗「Unable to update subscription」，回報者稱與 #10832／#50710／#43118 同屬相同模式（issue #55266，39 則留言、1 個讚）、Cowork 無法加入私有 GitHub marketplace（issue #28125，35 個讚）、MCP OAuth `resource` 參數多加尾端斜線導致 Microsoft Entra ID 驗證失敗 AADSTS9010010（issue #52871，26 個讚）、功能請求：提供選項關閉啟動歡迎畫面（issue #2254，126 個讚）；已知問題互動數更新 2 則：Advisor 觸發「No response from API」錯誤（issue #69238，69→96 個讚）、主題模式不隨系統自動切換明暗（issue #2990，新補讚數 242，本日已知問題讚數最高）。Google News（經 Startup Fortune 轉載）報導稱 Anthropic 已承認自身 bug 為先前 Claude Code 故障成因、此前曾「否認數週」；惟該報導僅有標題可讀、無具體時間線或官方聲明原文佐證，且屬單一低知名度媒體來源，暫不列入已知問題，待更多來源確認。 |
| 2026-08-01 | 已知問題互動數更新 2 則：macOS 持續性 ECONNRESET 連線錯誤（issue #5674，47→51 則留言，今日全站互動最高）、CLI TUI 無法捲動回看對話歷史（issue #28077，留言增至 37、讚數增至 75）；新增已知問題 6 則：v2.1.150 起滑鼠滾輪失效、滾動動作誤判為方向鍵（issue #65833，35 則留言，今日互動次高）、多帳號設定檔支援功能請求（issue #20131，39 則留言）、Bedrock Opus 4.7 回傳 permission_error 儘管 AUTHORIZED（issue #51183，37 則留言）、Session 重新命名後第二次退出即消失（issue #25090，32 則留言）、Cowork Global instructions 儲存後靜默還原（issue #40175，30 則留言）、CLI 與 Desktop app 同步對話歷史功能請求（issue #28791，30 則留言）。 |

**懸置細節**
- ⟨Q-14⟩ anthropic-sdk-python v0.122.0（2026-08-13）Features 區塊新增 API `output_behavior` 欄位支援：查證官方完整 changelog（[Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.122.0)，查證日 2026-09-20）確認原句為「add output_behavior to dream creation (create a new memory store or update the input store in place)」——先前因摘錄擷取不完整誤判為「於『dream cr』處截斷」，實際上官方原文完整、非截斷；`output_behavior` 用於控制 dream（記憶）建立時是否新建記憶庫或原地更新既有輸入庫，與 [[entities/managed-agents]] 的 Dreaming 記憶整合功能同屬一組 API。
- ⟨Q-15⟩ anthropic-sdk-python v0.117.0（2026-07-16）新增「api: add support for dreaming」：查證官方完整 changelog（[Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0)，查證日 2026-09-20）確認全文僅此一句，未進一步說明技術細節；命名對應 [[entities/managed-agents]] 既有 Dreaming 記憶整合功能的 API 化，與 v0.122.0（見 ⟨Q-14⟩）的 `output_behavior` 欄位屬同一組 dream/記憶 API 的先後兩次擴充。

## 服務穩定性：已解決的 Status 事故

自 [[entities/claude-code-known-issues]]「🌐 服務穩定性」組移入的已解決事故，原文照搬、最新在上；最後一條原住母頁現況。

- ✅ **已修復（約 35 分鐘後解決）**｜**Anthropic Status：Claude Sonnet 5.5 錯誤率升高，波及 claude.ai、Claude API、Claude Code 與 Claude Cowork（2026-10-27 14:42–15:17 UTC，15:50 UTC 確認解決）**：官方通報四項產品同受影響，15:50 UTC 確認已解決。[來源](https://status.claude.com/incidents/lqhknfdjrcst)
- ✅ **已修復（約 35 分鐘後解決）**｜**Anthropic Status：Claude Fable 5、Fable 5.1 錯誤率升高（2026-10-24 05:00–05:35 UTC，05:53 UTC 確認解決）**：官方通報兩款模型請求錯誤率升高，05:53 UTC 確認已解決。[來源](https://status.claude.com/incidents/0ns5clsk8p2x)
- ✅ **已修復（約 11 分鐘後解決）**｜**Anthropic Status：Claude Opus 5.5 錯誤率升高（2026-10-24 00:23–00:34 UTC，00:37 UTC 確認解決）**：官方通報 Opus 5.5 請求錯誤率升高，00:37 UTC 確認已解決。[來源](https://status.claude.com/incidents/3cqf3pmlnr96)
- ✅ **已修復（約 31 分鐘後解決）**｜**Anthropic Status：Claude Fable 5.1、Sonnet 5.5、Haiku 5.5 錯誤率升高（2026-10-23 23:28–23:59 UTC，2026-10-24 00:11 UTC 確認解決）**：官方通報三款模型請求錯誤率升高，00:11 UTC 確認已解決。[來源](https://status.claude.com/incidents/h101vcmhnfky)
- ✅ **已修復（約 1 小時 40 分後解決）**｜**Anthropic Status：platform.claude.com 用量資料讀取錯誤升高（2026-10-06 17:00–18:40 PT，10-07 02:33 UTC 確認解決）**：Usage 頁面讀取出現大量錯誤，僅影響用量儀表板顯示，不影響 Claude 本身使用。[來源](https://status.claude.com/incidents/wf2v8ms031sx)
- ✅ **已修復**｜**Anthropic Status：Claude 全面中斷，波及 claude.ai、App、Claude Code、Cowork、API（2026-09-29 14:00–14:59 UTC，16:27 UTC 通報恢復）**：全站中斷約 1 小時，14:59 UTC 恢復正常，觸發數十家美國媒體報導「Is Claude down」。[來源](https://status.claude.com/incidents/4xvtc2gnq73l)
  - 10-03 補：Anthropic 表示 14:00–14:59 UTC 間送出的部分訊息可能沒有被儲存；那段時間的對話或 Claude Code session 若有缺漏，要自己重送（[mixed-news.com](https://mixed-news.com/en/anthropic-claude-september-29-outage-messages-may-not-have-been-saved/)）
- ✅ **已修復**｜**Anthropic Status：Opus 5、Mythos 5.1、Fable 5.1 錯誤率升高（2026-09-22 00:50–02:10 UTC，02:35 UTC 監控確認恢復）**：三款模型請求錯誤率升高，官方分批修復後確認恢復正常。[來源](https://status.claude.com/incidents/7g1qpkyz5gxh)
- ✅ **已修復（約 24 分鐘後解決）**｜**Anthropic Status：Claude Mythos 5.1、Fable 5.1 錯誤率間歇升高（2026-09-15 10:50 UTC 進入監控 → 11:14 UTC 確認解決）**：與 09-11 同款模型錯誤率事件（見下）為不同起單獨通報事故，暫分列追蹤。[來源](https://status.claude.com/incidents/6304r9jjhj34)
- ✅ **已修復（約 1 小時 41 分後解決）**｜**Anthropic Status：Claude API 延遲升高（2026-09-10 21:43 UTC 識別 → 23:24 UTC 確認已緩解）**：官方通報部分使用者遇到 Claude API 回應速度低於正常水準，23:24 UTC 確認已緩解（mitigated）。[來源](https://status.claude.com/incidents/2pt83vlkk7x7)
- ✅ **已修復（約 2 小時後解決）**｜**Anthropic Status：claude.ai 與 Claude Code 降級（2026-08-31 16:55–19:16 UTC，20:36 UTC 確認解決）**：官方通報 claude.ai 與 Claude Code 出現服務降級，影響期間 16:55–19:16 UTC，20:36 UTC 確認已解決。[來源](https://status.claude.com/incidents/r82kdk0m7vqh)
- ✅ **已修復（同日解決）**｜**Anthropic Status：claude.ai 降級（2026-08-31，17:52 UTC 確認解決）**：官方通報 claude.ai 出現服務降級，17:52 UTC 確認已解決，與同日另一起 16:55–19:16 UTC 的 claude.ai／Claude Code 降級事件（見上）為不同起單獨通報事故，暫分列追蹤。[來源](https://status.claude.com/incidents/9jrp5rtyzrf6)
- ✅ **已修復**｜**Anthropic Status：Claude Cowork 與 Claude Code 網頁版錯誤率升高（2026-08-28，已採取緩解措施並確認解決）**：官方通報 Claude Cowork 與 Claude Code on the web 一度出現錯誤率升高，採取緩解措施後確認解決（Resolved）。[來源](https://status.claude.com/incidents/vr9tpk8w7zr8)
- ✅ **已修復（約 2 小時後解決）**｜**Anthropic Status：多款模型效能下降（2026-08-18 16:11–18:23 UTC，19:01 UTC 確認解決）**：官方通報多款模型出現效能下降，影響期間 16:11–18:23 UTC，19:01 UTC 確認已解決，官方訊息明確標註「The issue affecting Claude Opus 5 has been resolved」。[來源](https://status.claude.com/incidents/q7txxvbsftgq)
- ✅ **已修復（約 1 小時後解決）**｜**Anthropic Status：Claude Opus 5、Claude Sonnet 5 效能降級（2026-08-17 14:25 UTC 起 → 14:39 UTC 監控中 → 15:29 UTC 確認解決）**：官方通報 Claude Opus 5、Claude Sonnet 5 出現效能降級（degraded performance），14:39 UTC 進入監控階段，15:29 UTC 確認已解決。[來源](https://status.claude.com/incidents/zhk4v3yv1lsf)
- ✅ **已修復**｜**Anthropic Status：Claude 服務中斷，影響 claude.ai、platform.claude.com、Claude API、Claude Code 與 Claude Cowork（2026-08-16，22:34 UTC 確認修復）**：官方通報服務中斷，影響範圍涵蓋 claude.ai、platform.claude.com、Claude API、Claude Code 與 Claude Cowork，22:34 UTC 確認已解決（起始時間未載於摘要來源）；BleepingComputer 等多家媒體同步報導此次中斷事件。

> 2026-07-15～07-17 為近月密度最高的一段：Anthropic Status 三天內累計 9 起獨立事件（下方第 4～12 條），密度明顯高於近月平均；07-19 彙整時對照 07-18 日報確認全數已同日解決，07-17 那起（原 07-17 彙整時仍標記「修復實施中」）實際已於 12:21 UTC 解決。GV Wire 報導曾引用 Downdetector 錯誤回報數上升作為外部佐證，顯示使用者端在修復完成前確實感受到服務品質下降。2026-07-20～07-21 又出現一波獨立事件（下方前 5 條），多數已同日或次日解決，唯 07-21 的 Fable 5 事件截至彙整時仍在監控中；2026-07-24 再度出現 Opus 4.8 錯誤率升高事件，同日解決。**2026-07-25～07-26：** Opus 5 全平台正式上線首日，Anthropic Status 密集出現 4 起模型錯誤率事件，皆於 10 分鐘至約 1 小時內排除，屬新模型上線常見的短暫陣痛，非長期性問題。**2026-07-27：** Opus 5 上線後再度出現錯誤率升高事件，稍後 Haiku 4.5 亦開始回報錯誤，約 52 分鐘後恢復基準值。**2026-07-30：** Opus 4.7／Opus 4.5 錯誤率升高，約 45 分鐘後解決。**2026-08-03～08-04：** 再出現 3 起短暫錯誤率事件（Sonnet 5 兩起、跨多模型一起），最長約 85 分鐘、最短約 7 分鐘即套用修復並確認解決，屬短暫陣痛未列個別條目。**2026-08-04～08-05：** 08-04 21:04–21:59 UTC 出現帳號登入失敗事件，約 55 分鐘後解決；08-05 07:05 UTC 起 Claude Mythos 5、Fable 5 等多模型效能降級，09:13 UTC 彙整時仍在處理中，尚未確認解決，屬近期少見跨越彙整時間點仍未解決的事件。
- ✅ **已修復（24 分鐘後解決）**｜**Anthropic Status：Claude 服務中斷，影響 Claude API、Claude Code 與 Claude Cowork（2026-08-14 20:14–20:38 UTC）**：官方通報 Claude 服務中斷，影響範圍涵蓋 Claude API、Claude Code 與 Claude Cowork，20:38 UTC 確認已解決。[來源](https://status.claude.com/incidents/005ym4vzrq2w)
- ✅ **已修復（約 1 小時後解決）**｜**Anthropic Status：Claude Code on the web 與相關服務效能下降（2026-08-13 23:42 UTC 起 → 2026-08-14 00:51 UTC 確認解決）**：官方通報 Claude Code on the web 與相關服務出現效能下降（degraded performance），影響期間約 23:42–00:50 UTC，00:51 UTC 確認已解決。
- ✅ **已修復（約 55 分鐘後解決）**｜**Anthropic Status：帳號登入失敗（2026-08-04 21:04 UTC 識別 → 21:59 UTC 確認解決）**：官方通報部分使用者嘗試登入 Anthropic 帳號時遇到問題，21:59 UTC 確認已解決。[來源](https://status.claude.com/incidents/bdr3fq2rkchr)
- ✅ **已修復（約 45 分鐘後解決）**｜**Anthropic Status：多模型錯誤率升高，含 Opus 4.7／Opus 4.5（2026-07-30 10:03 UTC 進入監控，10:23 UTC 更新調查範圍納入 Opus 4.7／Opus 4.5，10:48 UTC 確認解決）**：官方通報多個模型錯誤率上升，10:23 UTC 更新確認調查範圍包含 Opus 4.7 與 Opus 4.5。[來源](https://status.claude.com/incidents/fsh2zzzl2c4l)
- ✅ **已修復（約 52 分鐘後解決）**｜**Anthropic Status：Opus 5 與 Haiku 4.5 錯誤率升高（2026-07-27 13:42 UTC 通報，Haiku 4.5 稍後開始回報錯誤，14:34 UTC 恢復基準值後解決）**：Opus 5 全平台上線後第二起錯誤率事件（首起見 07-26 10:44 UTC），本次同時波及 Haiku 4.5。[來源](https://status.claude.com/incidents/rkk5x44tndw9)
- ✅ **已修復（16 分鐘後解決）**｜**Anthropic Status：Opus 5 錯誤率升高（2026-07-26 10:44 UTC 通報並確認解決）**：Opus 5 全平台上線後首起錯誤率事件。[來源](https://status.claude.com/incidents/zftg3gqkmv18)
- ✅ **已修復（34 分鐘後解決）**｜**Anthropic Status：Fable 5／Sonnet 5／Haiku 4.5 等多模型錯誤率升高（2026-07-25 22:08 UTC 通報並確認解決）**。[來源](https://status.claude.com/incidents/j6gv862066n7)
- ✅ **已修復（約 1 小時後解決）**｜**Anthropic Status：Mythos 5／Fable 5／Opus 5／Haiku 4.5 錯誤率升高（2026-07-25 19:44 UTC 通報並確認解決）**：涵蓋範圍最廣的一起，同批含 Mythos 5。[來源](https://status.claude.com/incidents/f1q2wvw4qj4j)
- ✅ **已修復（約 10 分鐘後解決）**｜**Anthropic Status：Sonnet 4.6／Sonnet 5 錯誤率升高（2026-07-25 18:13 UTC 通報並確認解決）**。[來源](https://status.claude.com/incidents/1019wwb67615)
- ✅ **已修復（同日解決）**｜**Anthropic Status：Opus 4.8 錯誤率升高（2026-07-24 09:09 UTC 調查中 → 09:35 UTC 監控中 → 10:22 UTC 確認解決）**：與先前 07-17、07-20 的 Opus 4.8 錯誤率事件為不同批次的獨立事故。[來源](https://status.claude.com/incidents/0lbk5m7mbqk5)
- ✅ **已修復（跨日解決）**｜**Anthropic Status：Microsoft Office 附加元件安裝異常（2026-07-22 17:56 UTC 首次識別 → 2026-07-24 15:36 UTC 確認解決）**：Office 版 Claude 附加元件安裝流程出現異常，非 Claude Code CLI 本身問題，屬 Anthropic Status 頁面涵蓋的生態系其他用戶端事故，補記於此供跨產品穩定性對照。[來源](https://status.claude.com/incidents/yc7mr2gvl914)
- ✅ **已修復（同日解決）**｜**Anthropic Status：Haiku 4.5 錯誤率升高（2026-07-21 08:53 UTC 通報並確認解決）**。[來源](https://status.claude.com/incidents/v35b71rthzhp)
- ✅ **已修復（同日解決）**｜**Anthropic Status：Opus 4.8 錯誤率升高（2026-07-20 16:16 UTC 通報並確認解決）**：與同日稍早的 Opus 4.5 錯誤率事件（見下）為不同批次的獨立事故。[來源](https://status.claude.com/incidents/4n0mmv2v41rf)
- ✅ **已修復（同日解決）**｜**Anthropic Status：Opus 4.5 錯誤率升高（2026-07-20 07:57 UTC 起，07:57 標記已定位、10:57 套用修復進入監控）**：07-21 彙整時對照狀態頁確認已於同日完全解決。[來源](https://status.claude.com/incidents/hlt0yqp4lkww)
- ✅ **已修復（同日解決）**｜**Anthropic Status：Fable 5 於 Max 方案被誤判需消耗使用點數（2026-07-20 07:35–15:35 UTC）**：部分 Claude Code Max 方案用戶一度被系統誤判須使用點數才能存取 Fable 5（該存取權限實屬 Max 方案內建、不應額外扣點）；07-21 彙整時對照狀態頁確認已於同日 15:35 UTC 完全解決。與 [[entities/pricing]] 現行方案內容相關，另見 [[entities/fable-5]]。[來源](https://status.claude.com/incidents/tnypgb2jbqnq)
- ✅ **已修復（同日解決）**｜**Anthropic Status：多模型錯誤率升高（2026-07-15 15:11 UTC 確認解決）**。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Sonnet 5 錯誤率升高（2026-07-16 08:53 UTC 通報並同時確認解決）**。
- ✅ **已修復（同日解決）**｜**Anthropic Status：企業 SSO 登入失敗（2026-07-16 10:27 UTC 確認解決）**。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Opus 4.7 錯誤率升高（約 2026-07-16 08:58 UTC 通報，13:30 UTC 確認解決）**。
- ✅ **已修復（同日解決）**｜**Anthropic Status：多模型錯誤率升高第二起（2026-07-16 18:30–22:15 UTC 期間，22:53 UTC 確認解決）**。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Sonnet 5 與 Haiku 4.5 錯誤率升高（2026-07-17 07:03–12:21 UTC）**：兩模型同時出現錯誤率升高，07:03 UTC 進入監控、07:10 UTC 標記問題已定位，12:21 UTC 確認解決。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Claude Opus 4.8 錯誤率升高（2026-07-17 14:57–15:33 UTC）**：14:57 UTC 標記問題已定位，15:27 UTC 套用修復進入監控，15:33 UTC 確認解決。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Sonnet 5 錯誤率升高（2026-07-17 18:22–18:27 UTC）**：18:22 UTC 套用修復進入監控，18:27 UTC 確認解決。
- ✅ **已修復（同日解決）**｜**Anthropic Status：Fable 5 錯誤率升高（2026-07-17 18:48–19:43 UTC）**：18:48 UTC 套用修復進入監控，19:43 UTC 確認解決，官方確認 Fable 5 仍如預期維持「不消耗用量額度」的存取狀態。見 [[entities/fable-5]]。
- ✅ **已修復（同日解決）**｜**claude.ai container creation 部分中斷（2026-07-14 21:56–22:16 UTC）**：Anthropic Status 頁面顯示 claude.ai 的 container creation 功能發生部分中斷，約 20 分鐘後修復完成並經監控確認恢復正常；狀態頁未進一步說明確切成因與影響範圍，可能涉及 Claude Code on the web／Cowork 的沙箱建立流程。
- **Anthropic Status**（2026-10-06）：Claude Opus 5.5 錯誤率升高（12:37–12:43 UTC），6 分鐘內已解決，重要性低未列入已知問題。
