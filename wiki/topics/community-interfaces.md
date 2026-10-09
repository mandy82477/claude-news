---
page: "topics/community-interfaces"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：手機遠端、介面與 agent 可視化

社群從手機控制 Claude Code、換一個更好的終端機或介面、把 agent 正在做什麼畫出來的做法。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-08
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **先畫依賴地圖再開工**：mellos-mapping 先畫分層藍圖，建置時逐一點亮，目前只有這一個實作。
> - **圍繞 hooks 打造的終端機**：10-06 ClaudeTerm 用 hooks 與 statusLine 做出 Windows 終端機；10-04 Mobile-Harness 是免 root 的 Android 版行動端 IDE。

---

## 摘要

從手機控制這件事，先試官方：Claude Desktop 已可遠端控制 Claude Code session，怎麼開見 [[entities/claude-code]]。社群的實作走 bot、MCP、web-app 三條路，各選各的傳輸層，沒有和官方逐項比較過；這條方向怎麼走到今天見 [[topics/community-pattern-trends]] 趨勢八。介面元件多是把終端機或狀態列包裝得更好用；可視化目前只有把工具呼叫畫成遊戲化辦公室的兩個實作，多 agent 看板與儀表板見 [[topics/community-pattern-trends]] 趨勢六。

---

## 目前結論

- **手機遠端**：官方已可遠端控制；社群五個以上實作各走一路，還沒有收斂。**接下來看什麼：** 有沒有人比較官方與社群做法在離線、通知、多 session 上的差別。
- **介面與可視化**：各自單一實作居多，還在試。
- **你的選項：** 要從手機看進度先開官方遠端控制；要多 agent 總覽看 tools 頁「一堆 agent 在跑，看不到誰卡住」那一列。

---

## 技術彙整

### 2026-10

#### GuangminJu/mellos-mapping：由下而上開發用的即時分層依賴地圖，先畫藍圖再隨建置點亮節點（2026-10-07）

- **主線：** —
- **核心模式：** MCP server＋終端機面板，為 Claude Code、Codex CLI 與任何 MCP client 提供即時分層依賴地圖；設計先以「鬼影」畫出完整架構，節點隨實際建置與驗證通過才點亮；GitHub Search 100 星。
- **與既有模式的關係：** 本表既有類別未涵蓋「開發進度對照架構圖」這個切面，與現有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（100★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/GuangminJu/mellos-mapping)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### ClaudeTerm：圍繞 Claude Code hooks 與 statusLine 打造的 Windows 終端機（2026-10-06）

- **主線：** —
- **核心模式：** Windows 終端機，圍繞 Claude Code 的 hooks 與 statusLine 打造圖片面板、context／額度／subagent 狀態列，並支援分頁 session 續接。
- **與既有模式的關係：** 補上「介面元件複用」一個「Windows 原生終端機整合」取向——既有做法多是跨平台前端元件或 TUI，本則專注 Windows、直接消化 hooks／statusLine 輸出；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** Reddit r/ClaudeCode 貼文，互動數未見報導，僅憑作者自述功能清單，未經第三方驗證。
- **來源：** Reddit / r/ClaudeCode；[原文](https://www.reddit.com/r/ClaudeCode/comments/1wz6fvl/claudeterm_a_windows_terminal_built_around_claude/)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### techjarves/Mobile-Harness：免 root 的 Android 版 Claude Code 行動端 IDE（2026-10-04）

- **主線：** —
- **核心模式：** 在 Android 上跑 Claude Code 的行動端 IDE，免 root 即可聊天下指令、執行 Linux 指令、改檔、看 diff 並預覽 web app；GitHub Search 506 星。
- **與既有模式的關係：** 補上「行動裝置遠端控制」既有代表技巧（ccgram、Android Remote Control MCP、Shellular、Orchestrator、CLI-WeChat-Bridge）一個「原生 Android IDE」取向——既有做法多把手機當遠端控制介面橋接回主機，本則讓 Claude Code 直接在手機上執行；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（506★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/techjarves/Mobile-Harness)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### spaceamoeba-t/tapq：用語音與 Claude Code、Codex 等 agent 互動的多模態語音代理（2026-10-04）

- **主線：** —
- **核心模式：** 多模態語音代理，讓使用者以語音與 Claude Code、Codex 等 coding agent 互動——用語音回答 agent 的提示、下達指令、詢問 agent 剛才做了什麼，或只需點頭確認；GitHub Search 503 星。
- **與既有模式的關係：** 本表既有類別多在文字或視覺介面上做文章（「介面元件複用」封裝終端機美學、「行動裝置遠端控制」橋接手機傳輸層），本則把互動模態換成語音，與既有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（503★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/spaceamoeba-t/tapq)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### UNLINEARITY/CLI-WeChat-Bridge：把 Codex、Claude Code 等 CLI agent 原生接進微信／企業微信機器人（2026-10-02）

- **主線：** —
- **核心模式：** 將 Codex、Claude Code、OpenCode、Pi Agent 等 CLI 工具原生整合進微信／企業微信機器人，支援本機終端與微信雙向對話、檔案互傳、多 CLI 切換、表情綁定指令與雙向 `/resume` 對話恢復；GitHub Search 522 星。
- **與既有模式的關係：** 補上「行動裝置遠端控制」既有代表技巧（ccgram、Android Remote Control MCP、Shellular、Orchestrator）一個「微信傳輸層」取向——既有做法各自選了不同傳輸層，本則把既有 session 橋接到微信生態；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（522★），無 forks／issues／近期 commit 佐證可查，未另行查證；星數自 09-17 起緩步成長（500→522，約 16 天 +22 星），非短時間暴衝。
- **來源：** GitHub Search；[GitHub](https://github.com/UNLINEARITY/CLI-WeChat-Bridge)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### AgentSystemLabs/agent-office：卡通風 3D 虛擬辦公室，團隊可雇用 Claude Code 員工並追蹤 GitHub issue／PR（2026-10-02）

- **主線：** 並行規模
- **核心模式：** 卡通風格 3D 虛擬辦公室，團隊在其中「雇用」Claude Code 擔任座位上的員工、共享即時終端機、語音對話，並追蹤 GitHub issues 與 PR；GitHub Search 506 星。
- **與既有模式的關係：** 與「Agent 活動可視化」既有代表技巧 claude-office（像素風辦公室模擬）同屬「把 agent 活動搬出終端機」取向，本則走 3D 卡通風格並加入多人共享終端與語音，對應真實團隊多 worker 協作場景；多 agent 共事時的進度可視化是並行規模下的直接痛點，主線填並行規模。
- **可信度註記：** 僅有 GitHub Search 星數（506★），無 forks／issues／近期 commit 佐證可查，未另行查證；本庫星數追蹤今日（2026-10-02）首次收錄此 repo。
- **來源：** GitHub Search；[GitHub](https://github.com/AgentSystemLabs/agent-office)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### Louis-CFM/coucou：macOS 瀏海／Windows 螢幕頂端常駐的 Claude Code session 狀態小工具（2026-10-01）

- **主線：** —
- **核心模式：** 常駐 macOS 瀏海或 Windows 螢幕頂端的輕量小工具，持續顯示 Claude Code session 執行狀態，不必切回終端機確認進度；GitHub Search 2,268 星。
- **與既有模式的關係：** 與「Agent 活動可視化」既有代表技巧 claude-office（像素風辦公室模擬）同屬「把 session 狀態搬出終端機」取向，但 coucou 走極簡狀態列而非空間模擬，機制差異較大，暫不併入既有列，留待第二個同形式實作出現再判斷（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（2,268★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Louis-CFM/coucou)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

### 2026-09

#### alexgreensh/attention-span：ADHD 友善輸出風格外掛（2026-09-30）

- **主線：** —
- **核心模式：** 讓 Claude Code、Codex 等 agent 輸出更「人話」的 ADHD 友善 output-style 外掛；GitHub Search 1,149 星。
- **與既有模式的關係：** 與既有 2026-09-29 snflkd/fluent-korean（語言在地化 output-style 客製）同屬「輸出風格客製」做法，本則鎖定可讀性／專注力面而非語言；屬單一工具、非可複用機制，暫不併入既有代表技巧列；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,149★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/alexgreensh/attention-span)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### Nanako0129/coralline：仿 Powerlevel10k 風格的 Claude Code 狀態列外掛，貼提示詞由 AI 訪談後自動安裝（2026-09-29）

- **主線：** —
- **核心模式：** Powerlevel10k 風格的 Claude Code statusline 外掛，使用者貼一段提示詞即由 AI 訪談使用者需求後自動安裝與設定；GitHub Search 542 星。
- **與既有模式的關係：** 補上「介面元件複用」既有代表技巧（Brainless、statuslin.es、dsh-TUI、better-agent-terminal）一個「AI 訪談式自動安裝設定」取向，既有做法多是預先封裝好的元件庫，本則多了安裝流程本身的 agent 化；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（542★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Nanako0129/coralline)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### snflkd/fluent-korean：讓 Claude Code 講出流暢韓文的 output-style 外掛（2026-09-29）

- **主線：** —
- **核心模式：** Claude Code output-style 外掛，讓輸出使用更清晰道地的韓文；GitHub Search 1,349 星。
- **與既有模式的關係：** 現有 21 類聚焦工作流／記憶／協作／介面等面向，皆非本則核心；本則是單一語言在地化 output-style 客製，屬單一工具、非可複用機制，暫不併入既有代表技巧列；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,349★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/snflkd/fluent-korean)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### paulrobello/claude-office：即時像素風辦公室模擬視覺化 Claude Code 操作（新類別：Agent 活動可視化）（2026-09-27）

- **主線：** —
- **核心模式：** 即時像素風格辦公室模擬遊戲畫面，把 Claude Code 操作視覺化呈現；GitHub Search 530 星。
  - 同日 Hacker News 貼文「The City」提出把 Claude Code 視覺化成機器人城市的相近構想，惟該貼文已被下架（flagged），僅存標題與 repo 連結，內容細節與完成度均未見報導。
- **與既有模式的關係：** 現有 20 類皆無「把 agent 操作映射成空間遊戲視覺化」這個取向，claude-office 本身即可用一句機制成立（把工具呼叫映射成遊戲化空間視覺化），開立新類別「Agent 活動可視化」；The City 僅供參考，不作為判準所需的第二個具名實作；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** claude-office 僅有 GitHub Search 星數（530★），無 forks／issues／近期 commit 佐證可查，未另行查證；The City 僅 HN 標題可讀（貼文已下架），實際功能未經驗證，本節僅記錄其存在。
- **來源：** GitHub Search；[claude-office](https://github.com/paulrobello/claude-office)（530★）；Hacker News（已下架）；[The City](https://github.com/Slaymish/theCity)
- **成熟度：** ⏳ 新興（本庫首次收錄，兩者皆單一團隊／個人專案，尚無社群採用回饋數據）

#### Show HN: Whiteboard（YC W26）——人類與 agent 共用畫布討論架構，整合既有 CLI coding agent（2026-09-25）

- **主線：** —
- **核心模式：** 開源桌面應用，讓人類與 agent 共用一塊畫布討論系統架構；直接整合 Claude Code、Codex 等既有 CLI agent，並提供 SDK 讓 agent 把工作畫到畫布上；原型曾用 HTML artifact，因規格圖與程式碼難連動而改建在 CodeOSS 之上；團隊 Sid、Alex、Ketan、Milan；HN 358 分，2 個來源同日報導。
- **與既有模式的關係：** 現有代表技巧聚焦 agent 之間或 agent 與工具鏈協作，本則是「人類與 agent 共用視覺化畫布」取向，機制不重疊，暫不併入既有列；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** HN 358 分、2 個來源同日報導，訊號扎實；GitHub repo 可查，YC W26 團隊具名，未見獨立第三方復現或採用回饋數據。
- **來源：** Hacker News；[GitHub](https://github.com/devdotfast/whiteboard)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊產品發表，尚無社群採用回饋數據）

#### markusbug/Orchestrator：手機遠端生成、下指令、終止並管理多個 Claude Code 實例，關閉 App 後任務仍在背景執行（2026-09-10）

- **主線：** —
- **核心模式：** 開源工具，可從手機遠端生成、下指令、終止並管理多個 Claude Code 實例；關閉 App 後任務仍在背景持續執行，之後可回來查看進度；支援 Android（GitHub 下載 build）與 iOS（TestFlight）
- **與既有模式的關係：** 補上「行動裝置遠端控制」類別一個聚焦「多實例生命週期管理」的具體案例，與既有代表技巧（ccgram、Android Remote Control MCP、Shellular）同屬手機當 agent 控制介面取向，差異在本則強調背景持續執行與多實例並管
- **可信度註記：** 未提供互動分數；未見 forks／issues／近期 commit 佐證
- **來源：** 「Show HN: Orchestrator, spawn and manage Claude Code instances remotely」— Hacker News；[GitHub](https://github.com/markusbug/Orchestrator)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### ccch1mneyyy/dsh-TUI：中國社群「DSH」官方收錄的 TUI 補位插件，Claude Code 風格介面元件（鯨魚頂欄、串流思考顯示、雙擊 Esc 回滾、含 TPS 的 context 進度條）（2026-09-10）

- **主線：** —
- **核心模式：** TUI 補位插件，提供 Claude Code 風格介面元件：鯨魚頂欄、即時狀態列、串流思考顯示、雙擊 Esc 回滾、含 TPS 的 context 進度條，npm 一鍵安裝；中國社群「DSH」官方公眾號收錄
- **與既有模式的關係：** 補上「介面元件複用」類別一個聚焦 Claude Code 風格 TUI 元件的具體案例，與既有代表技巧（Brainless、statuslin.es）同屬把 agent 互動封裝成可安裝前端元件的取向
- **可信度註記：** GitHub Search 星數 2,933，僅取得星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（2,933★）；[GitHub](https://github.com/ccch1mneyyy/dsh-TUI)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### tony1223/better-agent-terminal：多工作區終端機聚合工具，整合 Claude Code 的 AI 協作功能（2026-09-10）

- **主線：** —
- **核心模式：** 多工作區終端機聚合工具，整合 Claude Code 的 AI 協作功能
- **與既有模式的關係：** 補上「介面元件複用」類別另一個終端機介面案例，與 dsh-TUI 同日收錄、同屬把 agent 互動封裝成可安裝前端元件的取向，差異在鎖定多工作區聚合而非單一 session 風格化
- **可信度註記：** GitHub Search 星數 502，僅取得星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（502★）；[GitHub](https://github.com/tony1223/better-agent-terminal)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### shlokkhemani/rabbithole：MCP 驅動的無限畫布學習工具，選取文字提問後以文件形式延伸分支（2026-09-07）

- **主線：** —
- **核心模式：** MCP 驅動的無限畫布學習工具，選取文字提問後答案以文件形式延伸分支，支援 Claude Code、Codex 等 agent；GitHub Search 累積 310 星
- **與既有模式的關係：** 與「介面元件複用」既有代表技巧（Brainless、statuslin.es）同屬把 agent 互動封裝成特定介面形態的取向，本則鎖定學習用的分支式文件畫布；與 coding workflow 關聯薄弱
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（310★）；[GitHub](https://github.com/shlokkhemani/rabbithole)
- **成熟度：** ⏳ 新興（本庫首次收錄，與 coding workflow 的關聯僅為支援 Claude Code 作為 agent 後端）

### 2026-08

#### Show HN：statuslin.es——社群策展的 Claude Code status line 樣式展示網站，每則附真實 sandbox 容器截圖（2026-08-17）

- **主線：** —
- **核心模式：** 開發者釋出 statuslin.es，蒐集社群提交、經人工審核的 Claude Code status line 樣式展示，每則皆附上真實 sandbox 容器截圖以佐證樣式實際運作效果（而非僅程式碼片段）
- **與既有模式的關係：** 為 Claude Code 客製化／UI 展示補上策展型社群索引，性質類似「介面元件複用」類別的 Brainless，聚焦 status line 這個更細分面向，以「真實截圖佐證」為收錄依據；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Show HN: A community library for Claude Code status lines」— Hacker News（score 12）＋跨 2 來源；[statuslin.es](https://statuslin.es)
- **成熟度：** ⏳ 新興（今日首見，尚待觀察後續提交量與社群採用度）

### 2026-07

#### Agenta：開源、可自架模型的 Claude Cowork 替代品，支援任意 harness（2026-07-28）

- **主線：** —
- **核心模式：** 開源專案 Agenta 提供與 Claude Cowork 相似的協作體驗，但可搭配自架（self-hosted）模型與任意 harness，不綁定單一廠商模型
- **與既有模式的關係：** 呼應本頁「介面元件複用」「模型使用策略」等類別中「降低廠商鎖定」的既有關注，是社群對官方 Cowork 產品提出開源平替方向的首個具體實作
- **來源：** 「Agenta: an open-source Claude Cowork alternative where you can use self-hosted models (and any harness)」— Reddit r/LocalLLaMA · 週熱門
- **成熟度：** ⏳ 新興

#### 開源手寫畫布：Claude 回應顯示於使用者手寫筆記旁（2026-07-17，補記技術做法）

- **主線：** —
- **核心模式：** 開發者釋出開源畫布工具，讓 Claude 的回應直接顯示在使用者手寫筆記旁，將 AI 輔助思考與紙本手寫筆記工作流結合，而非侷限於純聊天視窗介面
- **與既有模式的關係：** 與 [[topics/community-tech-discussions]] 07-15 記錄的「r/ClaudeAI 週熱門三則大型個人專案展示」為同一專案（手寫畫布），本頁首次以「模式」角度補記其技術做法；概念上與「介面元件複用」類別（Brainless）同屬 AI coding 工具介面美學探索，但本模式聚焦「手寫 + AI 回應並置」的新互動形式，而非既有元件封裝
- **來源：** 「I built an open-source canvas where Claude responds beside your handwritings」— Reddit r/ClaudeAI（週熱門，已達標；原貼 2026-07-17）
- **成熟度：** ⏳ 新興（單一開源專案展示，尚無其他採用案例佐證）

#### Brainless：模仿 Claude Code / Codex / Grok 介面風格的 shadcn 元件庫（2026-07-15）

- **主線：** —
- **核心模式：** 開發者釋出 shadcn 元件庫 Brainless，收錄模仿 Claude Code、Codex、Grok 等 AI coding 工具介面外觀風格的可安裝 UI 元件（如 pricing block），透過 `bunx shadcn add brainless/pricing` 等單一指令即可加入專案；把「AI coding 工具介面美學」封裝為可直接複用的前端元件
- **與既有模式的關係：** 本頁尚未有「前端 UI 元件複用」類別，屬新出現的類型，與既有 Skills/Plugin 的「封裝可複用單元」思路相通，差異在於封裝對象是視覺元件而非邏輯/流程
- **來源：** 「Brainless: Shadcn components that look like Claude Code, Codex and Grok」— Hacker News（score 124，本日社群條目最高分）
- **成熟度：** ⏳ 新興（今日首見，HN 124 分，顯示高度社群興趣，尚待後續採用回饋）

#### Devthropology：GitHub Repo 貢獻者互動與程式碼健康度視覺化（2026-07-10）

- **核心模式：** Show HN 工具 Devthropology 分析 GitHub PR 資料，提供貢獻者互動關係與程式碼健康度的視覺化洞察，供團隊了解協作模式與潛在瓶頸
- **與 Claude Code 生態的關係：** 非 Claude Code 專屬工具，但屬於「AI 輔助開發團隊如何觀察協作健康度」的鄰接工具類別，可作為 agent 大量產出 PR 後的團隊層可觀測性補充（推論）
- **來源：** [Show HN: Devthropology – Better Insights for GitHub Repos](https://devthropology.com/demo)（原文已失效）（Hacker News Show HN，34 分）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；HN≥30分）

#### AI 思考表徵編輯器：視覺化並編輯模型回答前的內部推理（2026-07-10）

- **核心模式：** 開發者受 Anthropic 論文《Verbalizable Representations Form a Global Workspace in Language Models》啟發，做出可視覺化並編輯開源模型內部推理表徵（thinking representation）的網頁工具，讓使用者在模型正式作答前介入調整其「思考」內容
- **與既有模式的關係：** 呼應既有「Extended Thinking 為摘要而非真實推理」討論（見 [[topics/community-tech-discussions]]）對「thinking blocks 究竟代表什麼」的持續關注；此工具提供社群一個實驗性介面直接操作內部表徵，而非僅停留在文本層辯論
- **來源：** [Show HN: I built a web tool to see and edit what an AI thinks before it answers](https://lucid.earthpilot.ai)（Hacker News Show HN，31 分）；相關論文亦見於同日 MIT Technology Review 報導「Anthropic found a hidden space where Claude puzzles over concepts」
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；HN≥30分）

#### Shellular：從手機遠端操作本機 Claude Code / Codex Session（2026-07-08）

- **核心模式：** 開發者發布 Shellular，讓使用者從手機遠端連線至自有機器，操作正在執行的 Claude Code、Codex 等 coding agent 與終端機、開發伺服器
- **與既有模式的關係：** 與 ccgram（2026-06-28，透過 Telegram 遠端控制 Claude Code）、Android Remote Control MCP（Plugin 設計模式一節）同屬「行動裝置遠端操作 agent session」模式家族的第三個獨立實作；三者共同顯示「手機作為 agent 控制介面」是社群反覆出現的需求，各自選擇不同傳輸層（Telegram bot、MCP、專屬 web app）
- **來源：** [Show HN: Shellular – run Claude Code, Codex, Pi from your phone](https://shellular.dev/)（Hacker News Show HN，32 分，跨 2 來源報導）
- **成熟度：** ⏳ 新興（單一 Show HN 專案，尚無採用數據；但屬第三個獨立佐證同一需求的實作，模式本身已具跨案例重複出現的訊號）

