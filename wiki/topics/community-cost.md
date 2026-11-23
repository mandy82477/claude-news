---
page: "topics/community-cost"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-11-22"
last_news_update: "2026-11-17"
status_main: "ongoing"
days_since_news: 6
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 6
inbound_links: 8
attribution_count: 18
attribution_last: "2026-11-17"
top_source: "github"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：token、成本與模型路由

社群在 Claude Code 上省 token、看見花費、把任務分派給不同模型的做法。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-03
**最後更新：** 2026-11-22
**最後新聞更新：** 2026-11-17

> **模型使用策略再添兩款：便宜模型配測試把關、跨廠商 CLI 橋接**（2026-11-17）
> - **cheap-ag**：便宜模型寫程式、測試結果決定上不上，宣稱讓訂閱用量延長 50 倍。
> - **antigravity-for-claude-code**：把 Google Antigravity CLI（Gemini）接成 Claude Code 的協作子 agent，跨模型路由任務。

---

## 摘要

省 token 的做法分三路：少送（精簡輸出、清掉 AI 留下的註解、工具結果轉 Markdown）、晚送（工具改用程式碼呼叫，不把定義全塞進 context）、送便宜的（純 I/O 工作路由給便宜模型）。看見花費這一路，現有工具只顯示帳號額度與重置時間，還沒有一款給出每批並行 subagent 花了多少。多 agent 到底比較省還是比較貴，同一個問題有兩個相反答案，見 [[topics/community-tech-patterns]]「現在收斂到哪」。

模型路由這條方向怎麼走到今天見 [[topics/community-pattern-trends]] 趨勢四；企業規模的成本結構與因應見 [[topics/enterprise-cost-management]]。

---

## 目前結論

- **費用可觀測性從選配變必備**：2026-06 計費切割風波（該政策已於 2026-06-16 暫停）之後，帳單看得見成了工具的基本要求；工具清單見 [[topics/community-tech-tools]]。
- **11 月中旬新冒出一批用量觀測品**：Model-share、Wake、Faros Desktop 等，見 [[topics/community-tech-tools]]「用量／token 觀測工具」。
- **並行成本歸因是缺口**：額度監控工具都有，「這一批 subagent 花了多少、做出了什麼」沒有人答得出來（見下方機制細節）。
- **省 token 的工具開始合體**：2026-11-12 Downshift 把指令輸出壓縮與 subagent 模型路由放進同一個工具（beta、單一作者，尚無量化節省）；11-02 的 Reddit「20 招」清單把零散做法收成對照表，11-04 一則公開帳單稱 17 個 bot 一個月只用一個 100 美元 Max 方案（單一案例、非第三方審計）。
- **你的選項：** 先量再省——用額度監控工具看清楚是哪一類工作在燒；再挑上面三路之一，路由給便宜模型的降幅目前最高，但只有單一團隊的數字。合體工具等有人量出省多少再裝。

### 用量去向歸因

- ⏳ **量測方法：** aidiveyt 翻 `~/.claude/projects/` 逐 session 拆帳，把「額度被誰吃掉」從感覺變成可重算的比例（見下方〈aidiveyt〉條目）；現有額度監控工具做不到這個顆粒度。
- ⏳ **context 與 subagent 的取捨：** 何時把工作移出主對話，見 [[topics/community-memory]] 10-06〈Context Is Like a Fridge〉；但 subagent 本身可能是最大用量來源（上列 48.1%），移出去不等於省（推論）。
- ⏳ **計價端的分段門檻：** Haiku 5.5 的 prompt 超過 10 萬 token 後單價跳五倍（$0.10／$0.50 → $0.50／$2.50），見 [[entities/haiku-5-5#實付成本]]。
- ⏳ **事前試算：** 送出前先估成本——mcptoon（10-04）壓縮 MCP schema 的 context 佔用，條目見本頁〈activeing123/mcptoon〉；Haiku 價格閘門見本頁〈Claude Haiku 5.5 Is Cheap Until 100k Tokens〉。
- **證據強度：** 單人一月樣本，尚無覆核；各節點細節以所在頁為準，此處只彙整歸因脈絡。
- 本節答的是「額度掉得快，花在哪」；官方認了沒、事故現在還在不在，見 [[entities/pricing#事故現在還在發生嗎]]。

### 用量窗口與配額守門

訂閱方案的 5 小時與 7 天用量窗口被燒完時，社群的補救分六類。下表分類，逐則證據仍在下方〈技術彙整〉原條目，表下各條只指路。

| 類別 | 解決什麼 | 代表節點 | 成熟度 |
|---|---|---|---|
| 事前攔截 hook | 窗口被燒完前先擋下 | agent-usage-guard | ⏳ 作者自報 |
| 選單列／儀表板 | 看見剩餘額度與重置時間 | syrtis、Pulse 等 | ⏳ 最多一族 |
| 暫停與恢復 | 撞限速後不丟進度 | resume-on-ratelimit | ⏳ 單人腳本 |
| 預算圍欄 | 到門檻自動停手 | agent-usage-guard；官方 Spend Controls | ⏳／官方有警示無暫停 |
| 中轉與 gateway 比價 | 換便宜管道或多帳號 | Folkbench、OmniRoute、teamclaude | ⏳ 星數待證 |
| 成本拆解實測 | 找出額度被誰吃掉 | aidiveyt | ⏳ 單一樣本 |

- **事前攔截 hook**：[[topics/community-cost#rbartoli/agent-usage-guard：Claude Code hook 防用量窗口被幾分鐘內燒完（2026-10-23）|agent-usage-guard]] 在快取過期、內容過大時提示先壓縮，用量逾 80% 時擋下新子 agent；單次爆量 365 降到 27 是作者 75 天自述。
- **選單列與儀表板**
  - [[topics/community-cost#Nanako0129/syrtis：macOS 選單列原生 Swift 用量監控，本地追蹤 25 種以上 agent（2026-10-24）|syrtis]]（10-24）
  - [[topics/community-cost#qunqin24/Pulse：macOS 邊緣常駐監視器，顯示 Claude Code、Codex、Cursor、Copilot 等 70 餘款 AI 工具剩餘額度（2026-10-03）|Pulse]]（10-03）
  - [[topics/community-cost#yakuikai/tokentab：本機優先、免 API key 讀取三款 CLI session 算用量與成本（2026-10-13）|tokentab]]（10-13）
  - [[topics/community-cost#同日三款 Claude Code／Codex 用量監控工具：codenotch（macOS 選單列釘選）、Armada（跨帳號側欄）、token-tracker（狀態列＋熱力圖＋成本分析）（2026-09-25）|同日三款]]（09-25）；全是單一作者工具，彼此不比較準不準。
- **暫停與恢復**
  - [[topics/community-tech-patterns-archive#resume-on-ratelimit.sh：以 PROGRESS.md + 20 行 shell script 自動恢復被限速中斷的 Claude Code Session（2026-08-04）|resume-on-ratelimit.sh]] 用 PROGRESS.md 加 20 行 shell 重試
  - [[topics/community-tech-patterns-archive#額度監控與自動恢復工具生態（2026-07-03）|07-03 自動恢復與監控兩類工具]]，是最早的同類
- **預算圍欄**：社群端只有上列 agent-usage-guard 的 80% 門檻；官方 Spend Controls 屬 Enterprise 方案，有 75%／90% 警示、無自動暫停，見 [[topics/enterprise-cost-management]]。
- **中轉與 gateway 比價**
  - [[topics/community-cost#Folkbench/folkbench：評測各家 AI API 中轉站可用率、延遲與價格並支援一鍵切換（2026-10-18）|Folkbench]] 量中轉站可用率與價格
  - [[topics/community-cost#cheaper-inference/OmniRoute：單一端點整合 375 家供應商、1,400+ 模型的免費 AI gateway，配額感知備援＋壓縮省 token（2026-10-22）|OmniRoute]] 的 79,703 星異常高，不當採用證據。
  - [[topics/community-cost#KarpelesLab/teamclaude：多帳號代理集中 Claude Max、Codex、API key 帳號池，額度用完自動輪替（2026-11-16）|teamclaude]] 多帳號額度池自動輪替
- **成本拆解實測**
  - [[topics/community-cost#aidiveyt：逐 session 拆帳一個月用量，量出 subagent 佔全部 token 48.1%、寫了 64% 的輸出（2026-10-08）|aidiveyt]] 一個月 455 個 session 拆帳，subagent 佔 48.1%
  - [[topics/community-tech-patterns-archive#MCP Server 設計對每輪對話隱藏 token 成本的實測比較（2026-07-21）|MCP 隱藏成本]]：單一作者實測各設計每輪注入的 token
  - [[topics/community-tech-patterns-archive#headless Claude Code（`claude -p`）冷啟動實測：未加 `--bare` 約載入 15 萬 token（2026-08-07）|headless 冷啟動]]：未加 `--bare` 約載入 15 萬 token
- **證據強度：** 六類全部是單一作者工具或自報數字，沒有一款有第二方重現；官方端只有 Enterprise 警示。

**機制細節**
- **模型使用策略**：Dragoman / Workweave 自動路由，嵌入 Claude Code / Codex / Cursor 的成本感知路由；InstantVideos 將分工路由思路延伸至內容生成（文字/圖像/影音各交專門模型）
- **Token / 成本優化**：極簡輸出模式（穴居人）企業採用獲 404 Media 確認；claude-thermos 保活請求維持快取不過期，引發成本轉嫁爭議；pxpipe 把文字渲染成圖片降 token；`claude -p` 未加 `--bare` 冷啟動約耗 15 萬 token；no-agent-summary.js 停用背景 agent 面板每 30 秒重傳逐字稿的隱藏成本
- **並行用量與成本歸因（缺口）**：Pulse、Offrun、[Usage Updates](https://usageupdates.com/)（Show HN，10-01）只顯示帳號額度與重置，不給每批並行 subagent 的成本；r/ClaudeAI 10-03 [提問](https://www.reddit.com/r/ClaudeAI/comments/1wwlwys/how_do_you_track_cost_and_outcome_across_parallel/)庫內無解答；遞迴失控見 [#68619](https://github.com/anthropics/claude-code/issues/68619)

---

## 技術彙整

> ⟨Q-nn⟩ 標的是這一則還沒查實的地方，完整說明在該月份分組最後的「懸置細節」。

### 2026-11

#### muaaz9329/cheap-ag：便宜模型寫程式、測試結果決定能不能上，MCP server 宣稱讓訂閱用量延長 50 倍（2026-11-17）

- **主線：** —
- **核心模式：** MCP server，讓便宜模型負責寫每一行程式碼，再用測試結果決定哪些變更真正送出（ship），作者宣稱可讓 Opus／Astra 等方案的 $20 訂閱不再頻繁撞到用量上限，號稱提升 50 倍可用量；供 Claude Code 與 Codex 使用。
- **與既有模式的關係：** 補上「模型使用策略」既有代表技巧（自製 harness 搭配 DeepSeek／GLM Flash 等便宜模型追平設計品質，[[topics/community-cost#2026-10]]）一個「測試結果當上線關卡」取向——既有做法只宣稱便宜模型能追平設計品質，本則額外用測試結果把關，不是單靠模型本身判斷對錯；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（335★），無 forks／issues／近期 commit 佐證可查，未另行查證；50 倍用量與品質把關的具體量測方法未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/muaaz9329/cheap-ag)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，宣稱倍數未經第三方驗證）

#### yuting0624/antigravity-for-claude-code：把 Google Antigravity CLI（Gemini）接成 Claude Code 的協作子 agent，依任務跨模型路由（2026-11-17）

- **主線：** —
- **核心模式：** Claude Code plugin，讓使用者把 Google 的 Antigravity CLI（底層為 Gemini）當成協作子 agent 呼叫，在軟體開發生命週期各階段依任務智慧選用模型；專案聲明與 Google／Anthropic 無關，為社群專案。
- **與既有模式的關係：** 補上「模型使用策略」既有代表技巧（多模型路由、jev-router 等，[[topics/community-cost#2026-10]]）一個「跨廠商 CLI 橋接」取向——既有路由多在 Claude 家內部模型或換供應商端點，本則直接把另一家廠商的官方 CLI 接成子 agent 參與編排；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證；「智慧選用模型」的具體路由規則未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/yuting0624/antigravity-for-claude-code)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### KarpelesLab/teamclaude：多帳號代理集中 Claude Max、Codex、API key 帳號池，額度用完自動輪替（2026-11-16）

- **主線：** —
- **核心模式：** Claude Code 與 Codex 用的多帳號代理，把 Claude Max、ChatGPT／Codex、API 金鑰與第三方後端帳號集中成一個帳號池，單一帳號額度用完時自動輪替到下一個。
- **與既有模式的關係：** 本表既有類別聚焦 agent 工作流本身（Skills、Hooks、MCP、記憶、模型路由等），本則是帳號層級的代理與輪替機制，與既有代表技巧不重疊，判為帳號橋接取向歸入本頁（同類先例：ardeyouxipianyi/workbuddy2api-hub，[[topics/community-cost#2026-09]]）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（503★），無 forks／issues／近期 commit 佐證可查，未另行查證；多帳號輪替用途未載明是否涉及規避官方帳號政策，本庫不評論其合規性。
- **來源：** GitHub Search；[GitHub](https://github.com/KarpelesLab/teamclaude)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### tiagovilasboas/downshift-ai：Go 開源工具壓縮指令輸出並依政策路由 subagent 模型（2026-11-12）

- **主線：** —
- **核心模式：** 作者在 Pro 方案幾天就用完週額度，做出 Go 開源工具 Downshift：Compactor 在 AI 讀到指令結果前先縮短、保留錯誤與結束碼，Computer Use 時也壓縮螢幕描述並只送兩次讀取間的變化；Model-routing 依政策為 subagent 選模型與推理力度；另有 Agents 角色檔與 Telemetry。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧（MCP Code Execution、mcptoon 等，[[topics/community-cost#2026-10]]）一個「指令輸出壓縮加 subagent 模型路由」合一的實作，與 jev-router 的任務路由同方向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** dev.to 第一手實作，7 讚；GitHub 查證日 2026-11-14：4 星、1 fork、最近 push 2026-11-12；作者自述已有特定情境結果，但延長 Pro 額度多少尚未量測。
- **來源：** dev.to / #claudecode；[原文](https://dev.to/tiagovilasboas/como-economizar-tokens-no-claude-code-conheca-o-downshift-4f0m)、[GitHub](https://github.com/tiagovilasboas/downshift-ai)
- **成熟度：** ⏳ 新興（beta、單一作者，無量化節省數字）

#### 韓國 B2B 流通公司：17 個 Claude Code bot 每月帳單僅 100 美元，零額外 API 支出（2026-11-04）

- **主線：** —
- **核心模式：** 非工程背景的運營人員公開實際帳單：17 個 Claude Code bot 自 2026 年起每天處理客訴比對等真實營運工作，全靠一個 100 美元 Claude Max 方案，零額外 API 支出。
- **與既有模式的關係：** 補上「Token / 成本優化」一則「單一訂閱方案撐多 bot 規模」的具名公開帳單案例，與既有省 token 清單、MCP 工具成本實測（[[topics/community-cost#2026-10]]）並列參照；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** Hacker News 單一貼文（13 分），作者公開具體帳單數字但非第三方審計，細節未見其他來源佐證。
- **來源：** Hacker News；[原文](https://botsinproduction.com/blog/what-10-claude-code-bots-cost-per-month/)
- **成熟度：** ⏳ 新興（單一公開案例，尚無其他團隊複現報告）

#### Reddit：給 coding agent 的「少浪費 token 20 招」清單，從基礎到進階（2026-11-02）

- **主線：** —
- **核心模式：** 整理一份從基礎到進階的 20 項省 token 檢查清單，指出 prompt 本身只是一部分花費，檔案內容讀取、修復回合、subagent 與背景模型呼叫都會疊加消耗，逐項提供可執行的縮減做法。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧（MCP Code Execution、穴居人模式等，[[topics/community-cost#2026-10]]）一份彙整式檢查清單，把既有零散做法收成一份可對照的清單；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** Reddit r/ClaudeCode 貼文，score 不可信（RSS 抓取恆為 0）；內容為清單彙整非單一量測，20 項具體條目未逐一轉述，依標題與摘要判讀收錄。
- **來源：** Reddit / r/ClaudeCode；[原文](https://www.reddit.com/r/ClaudeCode/comments/1xm8403/20_ways_to_waste_fewer_tokens_with_coding_agents/)
- **成熟度：** ⏳ 新興（單篇彙整，尚無第三方驗證清單有效性）

### 2026-10

#### MCP tool cost 實測：Apify 20 個求職 Actor 的 tools/list 耗 2.1K–32.7K token（2026-10-30）

- **主線：** —
- **核心模式：** 作者對 mcp.apify.com 上 20 個求職相關 Actor 呼叫 `tools/list`，實測每個工具定義耗用的 token：中位數 3.8K，最高一個達 32.7K，其中 98% 是伺服器自動推論出來的輸出 schema。
- **與既有模式的關係：** 補充既有「Token / 成本優化」MCP context bloat 量化系列（MCP Code Execution、MCP Server 信任邊界審查、MCP Server 設計隱藏成本比較）一筆新數據點，聚焦單一 MCP 服務內工具數量 × schema 大小的加總效應；非大型 codebase 特有痛點，主線填 —。
- **來源：** dev.to（12 讚；依規則以第一手量化實測內容判斷，非讚數）；[原文](https://dev.to/kevinhall/mcp-tool-cost-20-job-actors-on-apify-21k-to-327k-tokens-each-1hm4)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者實測，無第三方覆核）

#### Claude Code 用量優化工具推出 VS Code 延伸套件：30 天內 890 萬 token 浪費在已過期快取上（2026-10-30）

- **主線：** —
- **核心模式：** 作者將自製的 Claude Code 用量優化工具做成 VS Code 延伸套件，統計過去 30 天內有 890 萬個 token 浪費在已過期的 prompt cache 上。
- **與既有模式的關係：** 補上「用量去向歸因」一筆快取過期浪費的量化數字；方向與同日另一則「session token cache 更快失效」回報一致，詳見 [[topics/code-quality-decline#2026-10]]；主線填 —。
- **可信度註記：** 單一作者工具與自報數字，0 留言、無第三方覆核，未另行查證。
- **來源：** Reddit r/ClaudeCode（0 留言）；[原文](https://www.reddit.com/r/ClaudeCode/comments/1xjiyk0/my_claude_code_optimizer_is_now_a_vscode/)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，作者自報數字、無第三方覆核）

#### Research：自製 harness 搭配 DeepSeek／GLM Flash 等便宜模型，宣稱追平 Claude Code + Sonnet 5.5 的設計品質（2026-10-30）

- **主線：** —
- **核心模式：** 作者發布研究，自製 agent harness 搭配 DeepSeek、GLM Flash 等較便宜的模型，宣稱可在設計品質上追平 Claude Code 搭配 Sonnet 5.5 的輸出；本則只記 harness 設計本身，模型能力對比面見 [[entities/sonnet-5-5]]。
- **與既有模式的關係：** 補上「模型使用策略」一個「自製 harness 換用便宜模型」取向——既有做法多在同一 agent 內依任務路由模型，本則整套自建 harness 搭配非 Claude 模型重現設計產出；主線填 —。
- **可信度註記：** 僅有 Reddit 單一貼文、0 留言，無第三方覆核；測試方法與樣本量未見於摘要，未另行查證。
- **來源：** Reddit r/LocalLLaMA（0 留言）；[原文](https://www.reddit.com/r/LocalLLaMA/comments/1xit9g8/research_matching_claude_code_sonnet_55_design/)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者研究，無第三方覆核）

#### Claude Code 背景 agent 面板每 30 秒重傳完整逐字稿給模型：no-agent-summary.js 停用此行為（2026-10-29）

- **主線：** 並行規模
- **核心模式：** 社群分析發現 Claude Code 每隔約 30 秒把每個背景 agent 的完整對話記錄重新送給模型，只為更新 agents 面板的狀態列；作者發布 `no-agent-summary.js`（Bun `--preload`）可停用此計時器，不修改 Claude Code 本體二進位檔，於 2.1.257–2.1.312（Linux）測試過，據稱 macOS 亦可行。
- **與既有模式的關係：** Token / 成本優化——既有做法多在「送得少」（穴居人）或「送得晚」（MCP Code Execution），本則揭露的是官方 agents 面板本身的隱藏重傳成本；同時跑的背景 agent 數越多，影響越大，主線填並行規模。
- **可信度註記：** 單一作者分析＋腳本，於 2.1.257–2.1.312（Linux）實測，macOS 可行性為他人回報、未附對照數字，無第三方獨立覆核；HN 累積 527 分，為今日討論度最高條目。
- **來源：** Hacker News；[Gist](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者腳本，無第三方覆核）

#### Nanako0129/syrtis：macOS 選單列原生 Swift 用量監控，本地追蹤 25 種以上 agent（2026-10-24）

- **主線：** —
- **核心模式：** macOS 選單列 AI token 用量／配額監控工具，原生 Swift 打造（Liquid Glass 介面），本地追蹤 Claude Code、Codex、Cursor、OpenCode 等 25 種以上 agent 的用量，另附 3D 累積貢獻圖；GitHub Search 501 星。
- **與既有模式的關係：** 此類用量監控工具持續每隔數天出現新實作（如 10-13 tokentab、09-25 同日三款、09-20 Usage-Monitor），模式概覽表無對應類別收留；差異在本則單一工具同時覆蓋 25 種以上 agent，既有做法多鎖定 1–3 款；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（501★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Nanako0129/syrtis)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### rbartoli/agent-usage-guard：Claude Code hook 防用量窗口被幾分鐘內燒完（2026-10-23）

- **主線：** —
- **核心模式：** 以 hooks 實作的 Claude Code mod：快取過期、內容過大時提前提示「先壓縮再送出」，用量超過 80% 門檻時防止繼續生出子 agent，控制權交還使用者；MIT 授權，作者自述實測 75 天後單次爆量的 agent 數從 365 降到 27。
- **與既有模式的關係：** 補上「Agent 預算控制」一個以 hooks 實作的用量窗口防護取向（上一代表技巧 AgentWatch 已逾 60 天移出概覽表，本則重新激活此類別），呼應「Hooks 與自動化」；非大型 codebase 特有痛點，主線填 —。
- **來源：** Hacker News（24 分，2 個來源）；[GitHub](https://github.com/rbartoli/agent-usage-guard)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，作者自述量測、無第三方覆核）

#### cheaper-inference/OmniRoute：單一端點整合 375 家供應商、1,400+ 模型的免費 AI gateway，配額感知備援＋壓縮省 token（2026-10-22）

- **主線：** —
- **核心模式：** 免費 MIT 授權 AI gateway，單一端點整合 375 家供應商（150+ 免費）、逾 1,400 款模型，相容 Claude Code、Codex、Cursor 等；配額感知自動備援，稱 RTK+Caveman 壓縮省 token 15–95%。
- **與既有模式的關係：** 補上「模型使用策略」既有代表技巧（多模型路由、jev-router 等）一個「單一端點整合 375 家供應商」的規模取向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 2026-02 建 repo、8 個月內星數暴增至 79,703，遠高於本頁同類節點常見的數百至數萬星，無 forks／issues／近期 commit 佐證可查，不排除灌星可能，本庫僅陳列星數、不代表採用規模或品質背書。
- **來源：** GitHub Search；[GitHub](https://github.com/cheaper-inference/OmniRoute)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，星數異常未經驗證，尚無社群採用回饋數據）

#### Folkbench/folkbench：評測各家 AI API 中轉站可用率、延遲與價格並支援一鍵切換（2026-10-18）

- **主線：** —
- **核心模式：** 開源工具實測第三方 AI API 中轉站（relay／resale 服務）的可用率、延遲與價格並排行，供 Claude Code、Codex 使用者在多家中轉商之間切換；GitHub Search 累積 1,639 星。
- **與既有模式的關係：** 補上「模型使用策略」既有代表技巧（分層模型、多模型路由、Workweave Router 等）一個「第三方中轉商選擇」取向——既有做法多在官方模型之間路由任務，本則是在同一模型的多個非官方轉售管道之間，依可用率／延遲／價格切換；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,639★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Folkbench/folkbench)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### yakuikai/tokentab：本機優先、免 API key 讀取三款 CLI session 算用量與成本（2026-10-13）

- **主線：** —
- **核心模式：** 本機 CLI＋網頁儀表板，直接讀取 Claude Code、Codex、Gemini CLI 的 session log，依模型、專案、日期與活動類型拆算 token 用量與成本；免帳號、免 API key，資料不離開使用者機器；GitHub Search 530 星。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧（MCP Code Execution、穴居人模式、pxpipe、headless 冷啟動、I-have-ADHD、Pulse、mcptoon、Haiku 5.5 價格閘門）一個「跨三款 CLI 統一讀取、全本機無需任何帳號或金鑰」取向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（530★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[tokentab](https://github.com/yakuikai/tokentab)（原文已失效，2026-10-16 連結檢查）
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### SaarthurR/atticus-mac：按住說話的 macOS 語音助理，簡單操作本機處理、複雜任務靠 `claude -p` 吃既有訂閱（2026-10-12）

- **主線：** —
- **核心模式：** macOS 語音助理，按住快捷鍵說話；簡單操作（開啟 App、播放音樂）本機 0.08 秒內處理完畢不碰 AI，複雜任務才透過 `claude -p` 轉給 Claude，吃既有 Claude Pro／Max 訂閱額度、不需另外申請 API key；作者自述為國中生（9th grade）。
- **與既有模式的關係：** 補上「模型使用策略」既有代表技巧（分層模型、多模型路由等）一個「本機啟發式優先、只在必要時才吃訂閱額度」取向——既有做法多在多個雲端模型間路由，本則先用本機規則擋掉大多數請求，只有真正複雜的任務才送一次 `claude -p`；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** Hacker News 36 分（2 個討論串同日出現），作者第一手專案發布，無第三方量測覆核本機 0.08 秒處理的數字。
- **來源：** Hacker News；[GitHub](https://github.com/SaarthurR/atticus-mac)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### Headless Claude Code asks, exits, then resumes on the answer：用 `claude -p --resume` 讓 agent 等人決定時結束當前回合，不佔用程序輪詢（2026-10-05）

- **主線：** —
- **核心模式：** 當 headless Claude Code 需要人類決定時，把問題寫進 ticket 並直接結束當前回合（不留 process 輪詢等待），待人類回覆後用 `claude -p --resume` 接續執行，取代「開一個進程空等答案」的做法。
- **與既有模式的關係：** 補上「Token / 成本優化」既有做法在「長任務中斷後怎麼接續」面向的另一種實作——既有 resume-on-ratelimit.sh（2026-08-04）解決限速中斷自動重試，本篇解決「需要人類決策」的非故障性中斷，兩者皆「不留程序空等、靠外部事件觸發 resume」；非大型 codebase 特有痛點，主線填 —。
- **來源：** dev.to（4 讚；依 dev.to 內容判斷原則收錄：第一手 headless 自動化流程設計，非讚數）；[原文](https://dev.to/panthpatel/headless-claude-code-asks-exits-then-resumes-on-the-answer-54j3)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者實作心得，尚無第三方複現）

#### aidiveyt：逐 session 拆帳一個月用量，量出 subagent 佔全部 token 48.1%、寫了 64% 的輸出（2026-10-08）

- **主線：** —
- **核心模式：** 週額度 150→125（約減 17%，官方換軌見 [[entities/pricing]]）後，作者翻 `~/.claude/projects/` 一個月紀錄逐 session 拆帳（455 個 session、2,631 次 subagent 執行），量出 **subagent 佔全部 token 的 48.1%、寫了 64% 的輸出**。
- **與既有模式的關係：** 回應「並行成本歸因是缺口」既有機制細節——既有監控工具只顯示帳號額度與重置時間，答不出「這一批 subagent 花了多少」；本則是量測方法論而非工具，首次把個人用量拆到這個顆粒度，但僅一人一月樣本，未見覆核；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** dev.to 讚數待核，但屬第一手量化實測，附具體 session／request 數字與計費陷阱說明，非 SEO 農場文；單一作者樣本，無第三方覆核或對照組。
- **來源：** dev.to / #claudecode；[原文](https://dev.to/aidiveyt/the-september-cut-took-17-of-my-claude-code-week-subagents-were-taking-48-98n)
- **成熟度：** ⏳ 新興（本庫首次收錄這類量測方法論，單一樣本，尚無覆核）

#### Claude Haiku 5.5 Is Cheap Until 100k Tokens：送出前用 TypeScript 價格閘門先算計價級距（2026-10-08）

- **主線：** —
- **核心模式：** 針對 Haiku 5.5 官方已確認「逾 10 萬 token 請求適用更高價格」的分級計價機制（見 [[entities/haiku-5-5]]），作者寫一段小型 TypeScript 函式，在送出前依 prompt 長度先判斷會落在哪個計價級距，不需 API key 即可試算。
- **與既有模式的關係：** 補上「Token / 成本優化」既有做法一個「送出前價格試算」取向——既有做法多在輸出內容本身省 token，本則針對 Haiku 5.5 特有的 token 級距定價規則做前置判斷；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** dev.to 讚數低（1 讚）但屬第一手可執行程式碼範例，非行銷稿；僅單一作者樣本，未見第三方採用。
- **來源：** dev.to / #anthropic；[原文](https://dev.to/bobbyhalljr/claude-haiku-55-is-cheap-until-100k-tokens-build-a-tiny-price-gate-in-typescript-3k4)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### Armin Ronacher〈What is Codemode〉：重申別把工具塞進 context，改用程式碼呼叫工具（2026-10-06）

- **主線：** —
- **核心模式：** 部落格文章，重申作者一年多前「別把自訂工具或 MCP server 定義直接塞進模型 context」的主張，並說明「Codemode」——讓模型寫程式碼去呼叫工具，取代逐次把工具定義塞進提示詞——這個替代做法的設計理由。
- **與既有模式的關係：** 與「Token / 成本優化」既有代表技巧「MCP Code Execution」同屬同一機制，本則是具名部落客對該機制一年多來立場的重申與補充說明，未提出新機制；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 具名部落客個人論述，無第三方實測數據，屬立場闢述而非量化結果。
- **來源：** Blog / Armin Ronacher；[原文](https://lucumr.pocoo.org/2026/10/6/codemode/)
- **成熟度：** ⚡ 活躍（沿用「Token / 成本優化」既有活躍分類，本則為既有機制的立場重申，非新工具）

#### activeing123/mcptoon：零依賴 CLI 把 MCP 工具發現與 schema 成本壓到最低（2026-10-04）

- **主線：** —
- **核心模式：** 零依賴 CLI，整合管理所有 MCP 伺服器與 agent skill，宣稱可把工具發現成本從 71,929 token 壓到 581 token（降 99.2%，作者自測），schema 不進 context；單一設定檔適用 Claude Code、Codex、Cursor 等各家 agent；341KB、純 Python；GitHub Search 207 星。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧（MCP Code Execution、Pulse 等）一個「MCP 工具發現壓縮」取向——既有做法多壓縮對話或輸出內容，本則鎖定 MCP schema 本身的 context 佔用；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 99.2% 降幅為作者自測數字，無第三方覆核；僅有 GitHub Search 星數（207★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/activeing123/mcptoon)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### qunqin24/Pulse：macOS 邊緣常駐監視器，顯示 Claude Code、Codex、Cursor、Copilot 等 70 餘款 AI 工具剩餘額度（2026-10-03）

- **主線：** —
- **核心模式：** 免費開源 macOS 監視器，貼在螢幕邊緣，彙整 Claude Code、Codex、Cursor、Copilot 等 70 餘款 AI coding 工具的剩餘額度；GitHub Search 501 星。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧一個「額度可見」取向——既有做法多在降低用量，本則讓用量先看得見；與 Offrun 的帳號額度顯示同屬一個需求（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** GitHub API 查得 501★、54 forks、2 open issues、最近 commit 2026-10-03，建立於 2026-08-30（2026-10-03 查）；forks 約星數 11%，屬正常。
- **來源：** GitHub Search；[GitHub](https://github.com/qunqin24/Pulse)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### elidickinson/pi-claude-bridge：讓 pi.dev 用 Claude Code Pro／Max 訂閱當推論來源（2026-10-01）

- **主線：** —
- **核心模式：** Pi 平台的 inference provider，讓 Claude Code 的 Pro／Max 訂閱額度可供 pi.dev 平台取用；GitHub Search 509 星。
- **與既有模式的關係：** 本表既有類別聚焦 agent 工作流本身（Skills、Hooks、MCP、記憶、模型路由等），本則是訂閱額度跨平台接入的帳號層級橋接，不是工作流機制，不進模式概覽表；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（509★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始社群情緒標記為中性（😐），非一致正面評價。
- **來源：** GitHub Search；[GitHub](https://github.com/elidickinson/pi-claude-bridge)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

### 2026-09

#### ardeyouxipianyi/workbuddy2api-hub：多帳號反向代理閘道（2026-09-30）

- **主線：** —
- **核心模式：** 國際／國內多帳號反向代理閘道，支援 Codex、Claude Code、DSH 與標準 OpenAI 客戶端；GitHub Search 505 星。
- **與既有模式的關係：** 本表既有類別聚焦 agent 工作流本身（Skills、Hooks、MCP、記憶、模型路由等），本則是帳號層級的網路代理閘道，機制與既有代表技巧不重疊，暫不併入既有列；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（505★），無 forks／issues／近期 commit 佐證可查，未另行查證；「多帳號反代」用途未載明是否涉及規避官方帳號政策，本庫不評論其合規性。
- **來源：** GitHub Search；[GitHub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### gargpratyush/jev-router：Claude Code 中依任務路由到最便宜模型（2026-09-30）

- **主線：** —
- **核心模式：** 在 Claude Code 中依任務自動路由到最便宜可用模型的小工具；GitHub Search 500 星。
- **與既有模式的關係：** 補上既有「模型使用策略」代表技巧（分層模型、多模型路由、Workweave Router、Fable 5 編排、MaskShift、magpie）一個「成本優先路由」取向，既有做法涵蓋複雜度路由與手動切換，本則鎖定單一目標——選最便宜可用模型；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/gargpratyush/jev-router)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### Paritok-official/paritok-4b-v1：自研 4B 模型驅動的 non-destructive token 壓縮閘道（2026-09-29）

- **主線：** Context 管理
- **核心模式：** 非破壞性壓縮閘道，宣稱可為 coding agent 省下最多 85% token 費用（長時或飽和 session）、讓同一 context window 容納約 3 倍回合數，以自研 4B 模型驅動；可接上 Claude Code、Cursor、Codex、OpenHands；GitHub Search 1,453 星。
- **與既有模式的關係：** 補上「Token / 成本優化」既有代表技巧一個「模型驅動的 context 壓縮閘道」取向，與既有 pxpipe（圖片化 context）方向不同、走專用小模型重寫路線；長時 session 的 context window 飽和正是大型 codebase 常見痛點，主線填 Context 管理。
- **可信度註記：** 僅有 GitHub Search 星數（1,453★），無 forks／issues／近期 commit 佐證可查，未另行查證；「省 85% token」為自述數字，未見第三方獨立複現。
- **來源：** GitHub Search；[GitHub](https://github.com/Paritok-official/paritok-4b-v1)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### yetone/magpie：選單列一鍵切換底層模型（2026-09-28）

- **主線：** —
- **核心模式：** 選單列小工具，讓使用者在同一介面切換不同底層模型，例：Claude Code 搭配 Kimi、Codex 搭配 DeepSeek；GitHub Search 1,571 星。
- **與既有模式的關係：** 補上既有「模型使用策略」代表技巧一個「選單列快速切換底層供應商模型」取向，既有做法多聚焦依任務複雜度自動路由（Workweave Router、Fable 5 編排），本則走使用者手動一鍵切換；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,571★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/yetone/magpie)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### 同日三款 Claude Code／Codex 用量監控工具：codenotch（macOS 選單列釘選）、Armada（跨帳號側欄）、token-tracker（狀態列＋熱力圖＋成本分析）（2026-09-25）

- **主線：** —
- **核心模式：** codenotch（macOS app 釘選 Claude Code／Cursor／Codex／Antigravity 用量上限於螢幕邊緣，2,487★）、Armada（macOS 選單列顯示多帳號 session 狀態與配額，HN 1 分）、token-tracker（Claude Code／Codex 本地 token 追蹤，狀態列＋熱力圖＋成本分析，523★）。
- **與既有模式的關係：** 此類用量監控工具持續每隔數天出現新實作（如 07-03 額度監控工具生態、09-20 Usage-Monitor、09-16 TokenEater），模式概覽表無對應類別收留；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** codenotch 與 token-tracker 有 GitHub Search 星數但無 forks／issues／近期 commit 佐證；Armada 僅 HN 1 分、單一來源，訊號薄弱，僅記錄其存在。
- **來源：** GitHub Search；[codenotch](https://github.com/vinzdg/codenotch)（2,487★）、[token-tracker](https://github.com/stormzhang/token-tracker)（523★）；Hacker News；[Armada](https://armada.mgcrea.io/)（1 分）
- **成熟度：** ⏳ 新興（三款皆為本庫近期收錄的同類工具之一，尚無社群採用回饋數據）

#### simonw/llm-keys-ui 0.1：管理多組 LLM API 金鑰的圖形介面外掛（2026-09-21）

- **主線：** —
- **核心模式：** Simon Willison 發布 `llm` CLI 外掛 llm-keys-ui 0.1，針對「管理多組 LLM API 金鑰」這個具體問題提供圖形介面；Blogroll 策展來源。
- **與既有模式的關係：** 現有代表技巧皆聚焦 Claude Code／agent 工作流本身，本則是通用 `llm` CLI（非 Claude Code 專屬）的金鑰管理外掛，與既有類別核心機制不重疊，暫不併入既有代表技巧列；單一小型工具，無可複用機制描述。非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 來源為 Blogroll 策展名單（Simon Willison 本人部落格），非星數／留言數可比對，內容以官方發布說明為準。
- **來源：** Blog；[原文](https://simonwillison.net/2026/Sep/20/llm-keys-ui/)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一小型工具，尚無社群採用回饋數據）

#### CodeZeno/Claude-Code-Usage-Monitor：Windows 工作列小工具追蹤 Claude Code／Codex／Cursor 用量上限與重置時間（2026-09-20）

- **主線：** —
- **核心模式：** Windows 工作列小工具，追蹤 Claude Code、Codex、Cursor 等工具的用量上限與重置時間；免費開源；GitHub Search 累積 500 星。
- **與既有模式的關係：** 與 09-16 收錄的 AThevon/TokenEater（macOS 原生 App 監控用量並即時觀看 session）同屬額度監控可視化取向，本則為 Windows 平台版本；也與 07-03「額度監控與自動恢復工具生態」（CCLimitPing、LimitBar）同屬回應額度焦慮系列痛點的輔助工具；非大型 codebase 特有痛點，暫填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/CodeZeno/Claude-Code-Usage-Monitor)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### Show HN：Die With Me——以 AIM 好友清單介面查看朋友 Claude／Codex 額度剩餘（2026-09-17）

- **主線：** —
- **核心模式：** 補上 07-03「額度監控與自動恢復工具生態」第三例——仿 AIM 好友清單介面，讓使用者查看朋友的 Claude／Codex 用量還剩多少，額度低於 20% 時進聊天室互動；HN 11 分，跨 2 來源
- **與既有模式的關係：** 與既有 CCLimitPing（自動恢復型）、LimitBar（單人選單列監控型）同屬回應「額度焦慮系列」痛點的輔助工具，差異在本則把額度監控做成社交／好友清單形式，而非單人視覺化或自動化操作；額度用量提示與 codebase 規模無關，暫填 —。
- **可信度註記：** HN 11 分，跨 2 個來源同日報導，跨平台驗證強於單純單一貼文
- **來源：** Hacker News；[加入](https://diewithme.co/join)
- **成熟度：** ⏳ 新興（Show HN 當日，尚無採用數據，社交化額度監控此前未見）

#### ruvnet/open-claude-code：逆向工程還原重建的 Claude Code CLI 每夜反編譯專案（2026-09-16）

- **主線：** —
- **核心模式：** 每夜自動反編譯官方 Claude Code CLI 二進位檔並還原重建原始碼，屬逆向工程專案，非官方授權的原始碼重現。
- **與既有模式的關係：** 本表既有類別皆未鎖定「對閉源 CLI 逆向工程還原」這個做法，暫不併入既有列，留待第二個同類實作出現再判斷是否需要新類別（推論）；非大型 codebase 特有痛點。
- **可信度註記：** 僅有 GitHub Search 星數（501★），無 forks／issues／近期 commit 佐證可查，未另行查證；反編譯還原的正確性與授權疑慮未經查證。
- **來源：** GitHub Search；[GitHub](https://github.com/ruvnet/open-claude-code)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### I-have-ADHD：鎖定「Claudism」冗語——阻止 coding agent 完成任務後反覆交代哪些沒做的 Skill（2026-09-08）

- **主線：** —
- **核心模式：** 開源 skill，鎖定「Claudism」冗語風格——模型完成任務後仍反覆交代哪些檔案沒改、哪些事沒做（如「我改了 this.py 和 that.py，但沒改 README.md、也沒 commit」），或在程式碼註解中重複描述自己在做什麼
- **與既有模式的關係：** 與「Token / 成本優化」既有代表技巧穴居人模式（CaveMan Skill，單次回覆 Token 從 70 降至 20）同屬壓縮輸出取向，差異在本則鎖定的是「交代未做之事」這種特定冗語模式，而非泛用輸出長度
- **可信度註記：** Hacker News，499 分，另有一家獨立來源同步報導，屬本頁近期收錄中互動最高者之一；惟尚無具體實測數據佐證縮減幅度，亦無 forks／issues 佐證可查
- **來源：** 「I-have-ADHD: A skill to stop coding agents from burying the answer」— Hacker News（499 分，另有一家獨立來源報導）；[GitHub](https://github.com/ayghri/i-have-adhd)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### nafeeur/MaskShift：零 npm 依賴的本地優先 coding agent harness，可支援無原生 tool-calling API 的模型（2026-09-06）

- **主線：** —
- **核心模式：** 本地優先的 coding agent harness，訴求零 npm runtime 依賴，並可支援沒有原生 tool-calling API 的模型——做法是透過系統提示渲染工具 schema，讓模型以文字輸出間接完成工具呼叫
- **與既有模式的關係：** 與「模型使用策略」既有代表技巧（分層模型、多模型路由）不同層次——既有技巧解決「該用哪個模型」，本則解決「該模型能不能被納入工具呼叫框架」，補上模型相容性這一層
- **可信度註記：** Hacker News 單則僅 1 分，但同日另有一則獨立來源提及，屬多家報導；尚無具體實測數據或第三方回饋
- **來源：** 「Show HN: MaskShift – a maximalist coding agent with zero NPM dependencies」— Hacker News（1 分，同日另有一則獨立來源提及）；[GitHub](https://github.com/nafeeur/MaskShift)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋）

#### magnitudedev/magnitude：開源本地推論伺服器，可接掛 Claude Code 等既有 agent CLI（2026-09-06）

- **主線：** —
- **核心模式：** 在使用者自有硬體上運行本地模型的開源推論伺服器，可作為既有 agent CLI（Pi、OpenCode、Hermes、OpenClaw、Codex、Claude Code、Oh My Pi、Cline）的後端，不綁死單一 agent 工具；GitHub Search 累積 3,465 星
- **與既有模式的關係：** 屬推論基礎設施層，非 Claude Code 特有的工作流模式——與本頁「模型使用策略」類別的路由工具不同層次（那些路由既有雲端模型，本則替換整個推論後端）；Claude Code 僅為其支援的 8 種 harness 之一，關聯薄弱
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（3,465★）；[GitHub](https://github.com/magnitudedev/magnitude)
- **成熟度：** ⏳ 新興（本庫首次收錄，與 Claude Code 的關聯僅為其中一種可接掛 harness）

#### Spotify Portal：依任務型態把「純 I/O」工作路由給便宜模型，Token 用量降 90%（2026-09-04）

- **主線：** —
- **核心模式：** Spotify 內部工具 Portal 依任務型態分派——判斷為「純 I/O」（無需深度推理）的工作路由給便宜模型執行，使 Claude Code 整體 token 用量降低 90%
- **與既有模式的關係：** 為本頁「模型使用策略」類別既有「分層模型／多模型路由」補上一個具名大型企業（Spotify）的生產環境實證案例，且量化效果（90%）具體可查；成本面事實見 [[topics/enterprise-cost-management]]，本頁只記路由模式本身
- **可信度註記：** 官方工程部落格一手發布，附具體量化數字（90%），具名大型企業（Spotify）實證
- **來源：** 「Portal by Spotify cut my Claude Code token usage by 90%」— Spotify Engineering；[原文](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
- **成熟度：** ⚡ 活躍（具名大型企業生產環境實證，量化效果具體）

### 2026-08

- **兩則可量的成本機制：** headless `claude -p`（08-07）未加 `--bare` 冷啟動約載入 15 萬 token，是每次呼叫的固定成本，文章給出何時該加 `--bare` 的判準；Graft hooks（08-15）宣稱削減 grep 輸出 token 42%，但 benchmark 段落遭質疑 AI 代寫。
- 限速恢復：resume-on-ratelimit.sh（08-04）以 PROGRESS.md 加 20 行 shell，在撞上 5 小時或 7 天限額後自動重試並接續進度。
- 其他省 token 做法：pxpipe（08-05）把文字 context 轉成圖片，與「轉成更精簡文字」的既有做法方向相反；CCN（08-02）只清除 AI 遺留註解，作者稱經 2,700 次迭代測試。
- 用量與提示詞可視化：Frugal Tokens（08-19）依模型與快取狀態拆解各 session 花費；phistory（08-08）自動保存各 agent CLI 的 system prompt 版本快照；x1xhlol/system-prompts-and-models-of-ai-tools（08-29）彙整數十款工具的系統提示詞，GitHub 累積 14.3 萬星。
- Simon Willison 轉介 softwaredoug「假設性分類」（08-14）：部分分類任務直接讓 LLM 生成分類結果，取代傳統分類器或 embedding pipeline。
- 皆為單一作者工具或自報數字，無第二方重現。
- 原始條目見 [[topics/community-tech-patterns-archive#2026-08]]

### 2026-07

- **分層模型路由是本月主軸。** 「Fable 5 orchestrates, cheap models execute」（07-14，Reddit 轉載）宣稱 46% 成本達 96% 效能；07-12 與 07-26 兩則作者實務主張相同：只在需要頂尖判斷力的任務用 Fable 5，其餘交給便宜 subagent。
- 隱藏成本實測：MCP server 設計對每輪對話注入的 token 量（07-21，單一作者第一手量測）；Local Reverse Proxy（07-10）因 Claude Code 不遵守 HTTP_PROXY，自建 loopback 代理攔截完整 prompt、token 與花費。
- 快取：claude-thermos（07-23）定期保活 prompt cache，HN 討論帶出 Pro/Max 快取到期現為 1 小時、曾短暫退到 5 分鐘，並引發「成本轉嫁」爭議。
- 額度工具：07-03 出現自動恢復（限制解除即自動 continue）與監控可視化兩類工具，是同類工具最早的一批。
- 省 token 做法：CaveMan Skill（07-06，單次回覆約 70 降到 20 token，作者自稱）；本地 Ollama task router 分流程式碼探索（07-05）。
- AWS Bedrock 單日 $8.43（07-12）是 Bedrock 路徑的第一手計費參考。
- 其餘：作者翻自己的 JSONL 發現官方文件未載的 `<ip_reminder>` 標籤（07-29，原文已查證，查證說明見原文）；InstantVideos 多模型短影音 pipeline（07-07）；Anyclaude-SDK（07-28）與依任務分工選用 Claude 產品線（07-23）僅標題可考。
- 原始條目見 [[topics/community-tech-patterns-archive#2026-07]]
