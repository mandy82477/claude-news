---
page: "entities/claude-code-archive"
kind: "entity"
status: "resolved（封存頁）"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-27"
last_news_update: "2026-04-30"
status_main: "resolved"
days_since_news: 164
parent: "entities/claude-code"
children: "[]"
page_role: "archive"
days_since_news_subtree: 164
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-18"
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code——原始條目封存

**狀態：** resolved（封存頁）
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**最後更新：** 2026-09-27
**最後新聞更新：** 2026-04-30

> 本頁保存 [[entities/claude-code]] 被搬離主頁的原始「歷史記錄」條目。條目一字不刪，只是搬離主頁讓主頁讀得動；重點層見主頁。

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
| 2026-04-27 | 版本從 2.1.120 回滾至 2.1.119，疑似靜默撤版 |
| 2026-04-27 | 28 個滲透測試子代理人開源工具 pentest-ai-agents 釋出 |
| 2026-04-26 | HERMES.md 計費路由 bug 曝光，Anthropic 確認但拒絕退款 |
| 2026-04-26 | Anthropic 測試 Bugcrawl 漏洞偵測工具，見 [[entities/bugcrawl]] |
| 2026-04-26 | Anthropic 工程部落格詳解 Claude Research 多代理架構設計 |
| 2026-04-26 | 多個社群工具發布：Claude Squad（多人協作）、mux0（多 agent 終端）、agent-order（Codex+Claude PRD 協作） |
| 2026-04-25 | 社群開發 CC-Canary 工具自動偵測效能漂移 |
| 2026-04-24 | Stop hooks 失效問題被回報（Claude 4.7） |
| 2026-04-24 | Anthropic 正式承認效能退步源於工程疏失 |
| 2026-04 | Google 開始秘密開發競品 |

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
- ⟨Q-13⟩ 🔎 **查無官方**（標 2026-08-09｜查 Governor、token 浪費｜複 2026-10-18）：社群工具 Governor 宣稱優化 token 浪費，HN 社群對其實際成效提出疑慮；2026-08-10 查證找到廠商自報數據（compact professional 模式宣稱較基準降低 55.5% output token），惟均為工具作者／推廣部落格自行發布。2026-09-20 複查：本輪另搜尋獨立測試／評測站台，僅找到其他 token 優化工具（非 Governor 本身）的第三方 benchmark，未見任何獨立來源覆核或反駁 Governor 自報的 55.5% 數字；Governor 屬第三方社群工具，非 Anthropic 官方項目，故本題本質上不會有「官方」說法，僅能靠獨立覆核解決，目前仍缺，爭議維持未解。
