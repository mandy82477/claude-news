---
page: "topics/community-integrations"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-10-09"
last_news_update: "2026-10-07"
status_main: "ongoing"
days_since_news: 4
parent: "topics/community-tech-patterns"
children: "[]"
page_role: "child"
days_since_news_subtree: 4
inbound_links: 1
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-10-20"
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：MCP、plugin 與外部工具整合

社群把 Claude Code 接上外部服務、工具與創作軟體的做法，以及 MCP 長時間連線怎麼不斷。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-15
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **國產模型補連網、求職流程 MCP 化**：huashu-doubao-search 用豆包搜索補連網能力；swissdevjobs-cli 讓 agent 搜尋並應徵瑞士等 7 國的職缺。
> - **接上實體機器人**：ros-mcp-server（1,488★）透過 MCP 串接 ROS，目前只有這一個實作。

---

## 摘要

這是十月新做法最多的一群：每週都有新的 MCP server 或 plugin 進來，多數是單一作者工具（推論），還沒有人篩過哪個值得裝——該裝哪個看 [[topics/community-tech-tools]]。共同的設計原則是避免不必要的 context 載入；MCP 長時間連線的三種失效（連線中斷、工具逾時、上下文失憶）對應心跳、重試、快照三種防護。官方怎麼裝 plugin、怎麼接 MCP，見 [官方 plugins 文件](https://code.claude.com/docs/en/plugins/overview) 與 [官方 MCP 文件](https://code.claude.com/docs/en/mcp)；官方新出的 plugin 與 MCP 功能見 [[feature-radar]]。

---

## 目前結論

- **整合面一直往外擴**：從程式碼工具鏈擴到創作工具（影片、遊戲引擎、ComfyUI），十月起也接上實體機器人。
- **MCP 長 session 穩健化**：最後一則做法停在 2026-08-14，心跳、重試、快照三種防護還沒有新的實測。
- **你的選項：** 先查 tools 頁有沒有對應症狀的首選；裝單一作者的 MCP server 前，先確認它會載入多少工具定義進 context。

---

## 技術彙整

> ⟨Q-nn⟩ 標的是這一則還沒查實的地方，完整說明在該月份分組最後的「懸置細節」。

### 2026-10

#### robotmcp/ros-mcp-server：MCP server 串接 Claude、GPT 與 ROS 機器人（2026-10-07）

- **主線：** —
- **核心模式：** MCP server 讓 Claude、GPT 等模型透過 MCP 協定與 ROS（Robot Operating System）串接，操控實體機器人；GitHub Search 1,488 星。
- **與既有模式的關係：** 本表既有類別皆聚焦軟體開發或創作工具鏈，本則首次把 agent 整合延伸到實體機器人控制，與現有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,488★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/robotmcp/ros-mcp-server)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### alchaincyf/huashu-doubao-search：用豆包搜索補上國產模型版 Claude Code 缺少的連網能力（2026-10-07）

- **主線：** —
- **核心模式：** MCP server 以豆包搜索（字節系信源）替國產模型版 Claude Code 補上連網搜尋能力，每月 500 次免費額度；GitHub Search 105 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧一個「特定供應商連網能力補位」取向——針對換成國產模型後遺失的官方連網功能，用第三方搜尋 MCP 補回；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（105★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/alchaincyf/huashu-doubao-search)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### Stupidoodle/swissdevjobs-cli：零依賴 Python CLI＋MCP server＋Claude Code 外掛，供 agent 搜尋並應徵跨 7 國的透明薪資職缺（2026-10-07）

- **主線：** —
- **核心模式：** 零依賴 Python CLI，搭配 MCP server 與 Claude Code 外掛，讓終端機或 AI agent 搜尋並應徵約 4,700 個跨 7 國（瑞士、德國、英國、美國、加拿大、荷蘭、法國）的薪資透明技術職缺；GitHub Search 102 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧一個「垂直應用三件套（CLI＋MCP＋plugin）」取向——把特定領域（求職）包成可讓 agent 直接操作的完整工具鏈，而非開發流程本身的輔助；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（102★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Stupidoodle/swissdevjobs-cli)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### 〈How I Made My Autonomous Coding Agent Survive API Rate Limits and Outages〉：錯誤分類器＋抖動重試預算＋跨 agent 斷路器＋存檔暫停，取代直接崩潰（2026-10-06）

- **主線：** —
- **核心模式：** 作者記錄讓 24/7 執行的自動化編碼 agent 系統挺過 API 429 與過載錯誤的做法：錯誤分類器區分可重試與不可重試錯誤、帶隨機抖動的重試預算、跨平行 agent 共用的斷路器，以及「存檔後暫停」取代直接崩潰。
- **與既有模式的關係：** 本表既有類別中雖有處理長時間執行穩健性的做法，但鎖定協定層的連線與工具呼叫；本則處理的是模型 API 本身的限流與過載，機制（斷路器、重試預算、跨 agent 共享狀態）不同，與現有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 作者第一手實作心得，無量化數據或第三方驗證，屬方法論而非工具。
- **來源：** dev.to / #claudecode；[原文](https://dev.to/yureki_lab/how-i-made-my-autonomous-coding-agent-survive-api-rate-limits-and-outages-3912)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者方法論，尚無社群採用回饋數據）

#### pipeboard-co/meta-ads-mcp：Meta 廣告 MCP server，Pipeboard 五平台家族的 Meta 節點（2026-10-06）

- **主線：** —
- **核心模式：** Meta 廣告 MCP server，支援 Claude、ChatGPT、Perplexity、Cursor；屬 Pipeboard 五平台 MCP 家族（另含 Google、TikTok、Snap、Reddit）的 Meta 節點，託管免自架、免費方案；GitHub Search 1,293 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧（atlassian-mcp-server 等官方自建 remote MCP）之外一個「第三方託管、多平台家族、免自架」取向——既有做法是供應商自建或本機工具橋接，本則是獨立公司把同一套託管模式複製到五個廣告平台；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,293★），無 forks／issues／近期 commit 佐證可查，未另行查證；Meta Business Partner 標章為自述。
- **來源：** GitHub Search；[GitHub](https://github.com/pipeboard-co/meta-ads-mcp)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一公司產品家族，尚無社群採用回饋數據）

#### nykooi1/vibe-wise：陪使用者一起學系統設計的 Claude Code 外掛（2026-10-05）

- **主線：** —
- **核心模式：** Claude Code 外掛，在 AI 寫程式的同時向使用者解釋設計決策，目標是讓委託 AI 寫程式的人同步學會怎麼建構系統；GitHub Search 1,599 星。
- **與既有模式的關係：** 本表既有類別多聚焦「讓 agent 做得更好」，本則是少見的「讓人在旁邊跟著學」取向，與現有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,599★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/nykooi1/vibe-wise)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### zhitongblog/solomd：本地優先 markdown 編輯器，內建 MCP 橋接 Claude Code／Codex／Cursor（2026-10-05）

- **主線：** —
- **核心模式：** 本地優先、MIT 授權 markdown 編輯器（約 15MB），內建 MCP server 讓 Claude Code、Codex、Cursor 直接操作筆記庫，支援 14 家 LLM 供應商自帶金鑰；GitHub Search 1,167 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧（docsagent 等）一個「筆記應用本身即 MCP 橋接」取向——把既有編輯器變成 agent 可直接操作的資料層，而非另建獨立記憶服務。
- **可信度註記：** 僅有 GitHub Search 星數（1,167★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/zhitongblog/solomd)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### atlassian/atlassian-mcp-server：Atlassian 官方 remote MCP server，串 Jira／Confluence／Bitbucket（2026-10-05）

- **主線：** —
- **核心模式：** Atlassian 官方推出的 remote MCP server，讓 Claude、ChatGPT、Cursor、VS Code 等工具以 OAuth 2.1 或 API token 直接存取 Jira、Confluence、Jira Service Management、Bitbucket、Compass；GitHub Search 1,084 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧一個「供應商官方自建 remote MCP」取向——不是社群拼裝，是廠商自己發布的正式整合層。
- **可信度註記：** 僅有 GitHub Search 星數（1,084★），無 forks／issues／近期 commit 佐證可查，未另行查證；官方供應商發布，造假誘因低於個人開發者項目（推論）。
- **來源：** GitHub Search；[GitHub](https://github.com/atlassian/atlassian-mcp-server)
- **成熟度：** ⏳ 新興（本庫首次收錄，官方供應商發布，尚無社群採用回饋數據）

#### sadjow/claude-code-nix：隨 Anthropic 原生發布每小時自動更新的 Claude Code Nix 套件（2026-10-05）

- **主線：** —
- **核心模式：** Nix 套件，每小時輪詢 Anthropic 原生發布並自動同步最新版本，免去手動包裝 Claude Code 版本落後的問題；GitHub Search 500 星。
- **與既有模式的關係：** 本表既有類別未涵蓋「套件分發自動化」這個切面，與現有類別重疊不足半數，暫不併入既有列；目前僅此一個實作，留待第二個同形式實作出現再判斷是否另立類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/sadjow/claude-code-nix)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### desktop-commander/remote-desktop-commander：Desktop Commander 官方 remote MCP server，OAuth 連回自己的電腦（2026-10-05）

- **主線：** —
- **核心模式：** Desktop Commander 官方 remote MCP server，讓 claude.ai、ChatGPT、Cursor 等用戶端透過 OAuth 連回使用者自己的電腦執行操作；GitHub Search 137 星。
- **與既有模式的關係：** 與本則同批的 atlassian-mcp-server 同屬「供應商官方自建 remote MCP」取向，併入「Plugin / MCP 整合」既有代表技巧。
- **可信度註記：** 僅有 GitHub Search 星數（137★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/desktop-commander/remote-desktop-commander)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### RandallLiuXin/GodotMaker：由 Claude Code、Codex、Opencode 驅動的 Godot 自動文字轉遊戲產線（2026-10-04）

- **主線：** —
- **核心模式：** 自主文字轉遊戲產線，由 Claude Code、Codex、Opencode 共同驅動，依文字描述自動產出 Godot 遊戲雛型；GitHub Search 549 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（universal-modder 等）一個「從零產生新遊戲」取向——universal-modder 改裝既有遊戲，本則從文字描述直接產出新 Godot 專案；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（549★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/RandallLiuXin/GodotMaker)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### edenfunf/reelmimic：給一支喜歡的影片、由 Claude Code 或 Codex 團隊規劃並產出同風格新影片（2026-10-03）

- **主線：** —
- **核心模式：** 輸入一支喜歡的影片，AI 團隊（Claude Code 或 Codex）與使用者一起規劃、製作並審查出風格相同的新影片；GitHub Search 1,023 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、video-talkcraft 等）一個「以參考影片定風格」取向，並含規劃、製作、審查三段分工；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** GitHub API 查得 1,026★、132 forks、26 open issues、最近 commit 2026-10-02，建立於 2026-09-28——五天內衝到千星但 forks 與 issues 都有真實往來（2026-10-03 查）。
- **來源：** GitHub Search；[GitHub](https://github.com/edenfunf/reelmimic)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### artokun/comfyui-mcp：ComfyUI 的本機優先 MCP server＋側欄 agent，以自然語言產圖影音並編輯 workflow（2026-10-03）

- **主線：** —
- **核心模式：** 本機優先的 ComfyUI 控制層，MCP server 加側欄 agent，以自然語言生成圖像、影片、音訊，撰寫並執行 workflow、編輯即時節點圖；不綁模型（Claude、ChatGPT、Gemini、離線 Ollama 皆可）；專案自述 178 個工具、36 個 AI skills；GitHub Search 780 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、universal-modder 等）一個「節點式生成工具」取向，與 Plugin / MCP 整合同屬「以 MCP 接外部專業軟體」；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** GitHub API 查得 780★、134 forks、76 open issues、最近 commit 2026-10-02，2026-02 建立（2026-10-03 查）；forks 與 issues 往來充足，採信度高。
- **來源：** GitHub Search；[GitHub](https://github.com/artokun/comfyui-mcp)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具；工具與 skills 數量為專案自述）

#### Coolver/home-assistant-vibecode-agent：Home Assistant 的 MCP server agent，讓 IDE 用自然語言管理智慧家庭（2026-10-02）

- **主線：** —
- **核心模式：** Home Assistant 專用 MCP server agent，讓 Claude Code、Cursor、VS Code 等支援 MCP 的 IDE 用自然語言建立與除錯自動化、設計儀表板、調整主題與設定並部署變更；GitHub Search 630 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧（docsagent、google-ads-meta-ads-mcp 等）一個「智慧家庭控制」取向的垂直 MCP 整合；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（630★），無 forks／issues／近期 commit 佐證可查，未另行查證；星數自 09-17 起已近兩週持平（629→630），非短時間暴衝。
- **來源：** GitHub Search；[GitHub](https://github.com/Coolver/home-assistant-vibecode-agent)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### rehan-remade/universal-modder：讓 Claude Code 改裝任意 PC 遊戲的 skills／工具組合（2026-10-01）

- **主線：** —
- **核心模式：** 整合 skills、工具與 fal MCP，讓 Claude Code 對任意 PC 遊戲進行偵查、反組譯分析、fal 生成美術／3D／音效、遊戲內測試與成果影片產出；GitHub Search 1,388 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、anything2explainer、chess-postmortem-skills、video-talkcraft）一個「遊戲改裝」取向，既有做法多聚焦單一風格影片或棋局分析，本則把反組譯分析與素材生成整進同一改裝流程；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,388★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/rehan-remade/universal-modder)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

### 2026-09

#### irinabuht12-oss/google-ads-meta-ads-mcp：Google Ads、Meta Ads、GA4、Search Console 整進單一託管 MCP（2026-09-30）

- **主線：** —
- **核心模式：** 託管遠端 MCP 伺服器，整合 Google Ads MCP、Meta Ads MCP、GA4、Search Console，供 Claude、ChatGPT 等多款 agent 使用；號稱 250+ 工具、OAuth 免 API 金鑰、寫入需人工核准、免費；GitHub Search 3,223 星，近 4 天 +588 星（約 147 星／日）。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧（Plugin 反模式整理、Claude Code 作為 MCP 協調中心、XActions、docsagent、agenvoy）一個「多廣告／分析數據源整進單一託管 MCP」取向，既有做法多聚焦單一資料源或任務類型，本則把四種廣告與分析資料源整進同一免費託管遠端 MCP；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 星速偵測收錄（近 4 天 +588 星，約 147 星／日），未見 forks／issues／近期 commit 佐證可查，未另行查證；核准層審核寫入動作（approval-gated writes）為專案自述設計，未經第三方驗證。
- **來源：** GitHub Search；[GitHub](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### Vincentwei1021/video-talkcraft：配音驅動動態設計工作室 agent skill（2026-09-30）

- **主線：** —
- **核心模式：** Agent skill，把 Claude Code／Codex 變成動態設計工作室，產出配音驅動的解說影片；含逐字稿配音同步、109 套運鏡範本卡、反投影片式運鏡系統，以 Remotion 算圖；GitHub Search 1,314 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、anything2explainer、chess-postmortem-skills、lemo-opuscar）一個「配音驅動動態設計」取向，既有做法多聚焦單一風格化影片或棋局分析，本則另附大量運鏡範本卡與逐字稿同步機制；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,314★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Vincentwei1021/video-talkcraft)（原文已失效）
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### AMAP-ML/LongHorizon-Harness：跨桌面應用與 CLI 的長時任務可恢復 harness（2026-09-28）

- **主線：** —
- **核心模式：** 長時任務 computer-use harness，讓 agent 跨桌面應用與 CLI 長時間執行並維持任務狀態；核心機制為 fresh-context execution（重置對話避免累積漂移）、可稽核的持久驗證狀態、獨立稽核與可恢復進度，原生支援 Claude；GitHub Search 1,638 星。
- **與既有模式的關係：** 現有 21 類聚焦 agent 協作、記憶、工具鏈整合等面向，皆非本則核心；概念上與既有「長 Session 穩健化」（原聚焦 MCP 協定失效模式：心跳、重試、快照）相近，皆處理長時任務的可恢復進度與稽核，但本則橫跨任意桌面應用與 CLI、不限 MCP，是否併類或另立新類留待週更判斷；單一 agent 長時延續而非跨 agent 並行痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,638★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/AMAP-ML/LongHorizon-Harness)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### 同日三款 Skills／創意工具新實作：lemo-opuscar（Opus 5.5 導演影片風格）、geo-sleuth（照片地理定位 skill）、3dicon（3D 動態 icon 生成 skill）（2026-09-28）

- **主線：** —
- **核心模式：**
  - lemo-opuscar：39 種影片風格，各附可重用風格提示詞，由 Claude Opus 5.5 純程式碼產出樣片，使用者選風格帶入自己的故事讓 agent 導演；GitHub Search 505 星
  - geo-sleuth：agent skill，綜合 OpenStreetMap 幾何、海拔天際線、衛星影像與街景判斷照片拍攝地並展示推理過程；相容 Claude Code、Codex、Cursor、Gemini CLI、OpenCode、GitHub Copilot；GitHub Search 502 星
  - 3dicon：Claude Code skill，輸入一段提示即輸出具真實透明度的循環動畫 3D icon；GitHub Search 500 星
- **與既有模式的關係：** lemo-opuscar 補上「創意工具 Agent 整合」一個「風格化影片導演」取向；geo-sleuth、3dicon 補上「Skills 設計」兩個新取向——跨來源地理定位判讀、3D 動態資產生成；三者皆非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 三者皆僅有 GitHub Search 星數（505★／502★／500★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)（505★）、[geo-sleuth](https://github.com/Oldcircle/geo-sleuth)（502★）、[3dicon](https://github.com/samyost1/3dicon)（500★）
- **成熟度：** ⏳ 新興（三者皆本庫首次收錄，尚無社群採用回饋數據）

#### agenvoy/Agenvoy：自我修復工具的自架 agent harness（2026-09-27）

- **主線：** —
- **核心模式：** 單一 Go 二進位檔的自架 AI agent harness，自己寫工具、在沙盒測試並修復，讓 Claude Code、Codex 與任何 MCP client 都能建立並共享這些工具；GitHub Search 537 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」既有代表技巧一個「agent 自寫並跨 client 共享 MCP 工具」取向實作，既有做法聚焦既有工具鏈整合，本則多了工具自我修復一步；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（537★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/agenvoy/Agenvoy)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### 同日兩款創意工具 Agent 整合：anything2explainer（主題轉解說影片）、chess-postmortem-skills（棋局賽後分析影片）（2026-09-27）

- **主線：** —
- **核心模式：**
  - anything2explainer：輸入一個主題，輸出附 TTS 旁白、字幕與章節進度條的黑底動態圖形解說影片，中英文皆可，每一格畫面用 Remotion 以程式碼繪製；Claude Code／Codex skill（2,108★）
  - chess-postmortem-skills：讓 Claude 用視覺（非棋譜記號）看棋局並結合 Stockfish 解說，再把使用者的語音筆記轉成附講解的棋局影片；作者估算分析一局約耗費 15 美元 API 額度；Hacker News 74 分，2 個來源同日報導
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧兩個新取向——泛用主題轉解說影片（anything2explainer）與棋局賽後分析影片（chess-postmortem-skills），皆延續既有 Palmier Pro／oh-story-claudecode 把 agent 整合擴到影片創作工具鏈的方向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** anything2explainer 僅有 GitHub Search 星數（2,108★），無 forks／issues／近期 commit 佐證可查，未另行查證；chess-postmortem-skills 來自 Hacker News，74 分且 2 個來源同日報導，訊號較扎實。
- **來源：** GitHub Search；[anything2explainer](https://github.com/Vincentwei1021/anything2explainer)（原文已失效）（2,108★）；Hacker News；[chess-postmortem-skills](https://github.com/brumar/chess-postmortem-skills)（74 分，2 來源）
- **成熟度：** ⏳ 新興（兩者皆本庫首次收錄，單一團隊／個人專案，尚無社群採用回饋數據）

#### bangtutorial/bang-motion：瀏覽器動態圖形 agent skill，五種解說風格單一 HTML 輸出（2026-09-24）

- **主線：** —
- **核心模式：** 瀏覽器端動態圖形 agent skill，可產出片頭、宣傳片、動態字卡等五種解說風格，單一 index.html 輸出，相容 Claude Code、Codex、Gemini CLI、Cursor；GitHub Search 509 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、oh-story-claudecode）一個「動態圖形／短片生成」取向的代表技巧，跨 harness 相容是既有兩例沒有的取向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（509★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/bangtutorial/bang-motion)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### docsagent/docsagent：原生 C++ 搜尋核心 MCP，讓 Claude 等 agent 存取個人知識庫（先支援 Zotero）（2026-09-21）

- **主線：** —
- **核心模式：** MCP 伺服器讓 Claude、Cursor、Cline 等 agent 即時、私有存取個人知識庫，先支援 Zotero，Obsidian／Apple Notes 開發中；採原生 C++ 搜尋核心（BM25＋段落排序），查詢約 15ms；GitHub Search 616 星。
- **與既有模式的關係：** 補上「Plugin / MCP 整合」類別一個「私有知識庫存取」取向的代表技巧——既有代表技巧（Claude Code 作為 MCP 協調中心、XActions、stagehand）多聚焦工具鏈調度或網頁互動，本則鎖定本機個人知識庫的低延遲檢索；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（616★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/docsagent/docsagent)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### GitHub Search 存量盤點：browserbase/stagehand——網頁資料擷取與互動 SDK，相容 Claude Code／Codex／Eve／Mastra（2026-09-17）

- **主線：** —
- **核心模式：** 開源網頁資料擷取與互動 SDK，讓 coding agent 以程式化方式操作瀏覽器完成資料擷取與網頁互動；可搭配 Claude Code、Codex、Eve、Mastra 等工具使用；GitHub Search 累積 24,318 星
- **與既有模式的關係：** 補上本頁「Plugin/MCP 整合」類別另一個瀏覽器互動案例——與 2026-09-05 收錄的 feder-cr/AIHawk（完整瀏覽器自動化 agent 再外掛 MCP 介面）取向不同，stagehand 定位是供 agent 呼叫的資料擷取 SDK 本身，非完整自動化 agent；非大型 codebase 特有痛點
- **可信度註記：** 存量盤點條目，2024-03 出生、本庫今日首次收錄，累積時間跨度逾 2 年；僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（24,318★，存量盤點｜2024-03 出生、本庫今日首次收錄）；[GitHub](https://github.com/browserbase/stagehand)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### genspark-ai/genoffice：開源 AI Office 套件，CLI 與 agent skill 讓 Claude Code／Codex／Cursor 直接讀寫本機 .docx/.xlsx/.pptx（2026-09-14）

- **主線：** —
- **核心模式：** 開源 AI Office 套件，內建 Docs、Sheets、Slides、PDF、Markdown／HTML 編輯器與 AI agent；另提供 `genoffice` CLI 與 agent skill，讓 Claude Code、Codex、Cursor 直接讀寫本機 .docx/.xlsx/.pptx，支援三大作業系統
- **與既有模式的關係：** 本表既有類別皆未鎖定「本機辦公文件格式讀寫」這個具體應用面——與「創意工具 Agent 整合」（Palmier Pro、oh-story-claudecode）相近但服務對象不同（辦公文件 vs 創作內容），暫不併入既有列，留待第二個同類實作出現再判斷是否需要新類別（推論）；辦公文件讀寫與 codebase 規模無關，暫填 —。
- **可信度註記：** 星速偵測收錄（6,774 星、forks 899，約星數 13%，符合防刷門檻），近日仍有 commit（2026-09-14），跨 2 來源；功能清單為專案自述
- **來源：** GitHub Search；[GitHub](https://github.com/genspark-ai/genoffice)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### zenstory-ai/oh-story-claudecode：中文網路小說寫作 agent skills 合集，涵蓋掃榜、拆文、寫作、去 AI 味、封面全流程，本庫存量盤點今日首次收錄（2026-04-22 出生、6,824 星）（2026-09-13）

- **主線：** —
- **核心模式：** 13 個 skill 組成的中文網路小說（网文）寫作流程，涵蓋掃榜選題、拆文分析、正文寫作、去 AI 味潤稿、封面生成，長篇短篇皆支援，具檔案式跨 session 連續性追蹤
- **與既有模式的關係：** 補上「創意工具 Agent 整合」類別一種「垂直領域全流程 skill 化」取向的做法——既有代表技巧（Palmier Pro）聚焦把 agent 整合擴到創作工具鏈，本則把單一垂直領域（中文網文寫作）的完整生產流程拆成 13 個可組合 skill；創作領域 skill 與 codebase 規模無關，暫填 —。
- **可信度註記：** 本庫存量盤點通道首次收錄（已成名但本庫未報導過的 repo，2026-04-22 出生），未見 forks／issues／近期 commit 佐證，功能敘述為專案自述；6,824 星屬本庫近期收錄中同類最高，星數真實性未經第三方驗證
- **來源：** GitHub Search（存量盤點）；[GitHub](https://github.com/zenstory-ai/oh-story-claudecode)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### nirholas/XActions：X/Twitter 自動化工具組，內建供 AI agent 使用的 MCP 伺服器與 CLI（2026-09-07）

- **主線：** —
- **核心模式：** X/Twitter 自動化工具組，內建供 Claude、GPT 等 AI agent 使用的 MCP 伺服器、CLI 與瀏覽器腳本；GitHub Search 累積 513 星
- **與既有模式的關係：** 補上「Plugin / MCP 整合」類別一個社群媒體自動化的具體案例，與 figwright（設計稿↔程式碼）同屬「既有 MCP 客戶端串接特定領域工作」的取向，差異在鎖定 X/Twitter 而非設計工具
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（513★）；[GitHub](https://github.com/nirholas/XActions)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### aqm857886159/Nomi：開源 AI 影片工作台，透過 MCP 讓 Claude Code／Codex／Cursor 指揮生成與剪輯（2026-09-07）

- **主線：** —
- **核心模式：** 開源 AI 影片工作台，local-first 設計，可讓 Claude Code、Codex、Cursor 透過 MCP 指揮影片生成與剪輯流程；GitHub Search 累積 500 星
- **與既有模式的關係：** 與 XActions 同屬「既有 coding agent 透過 MCP 跨足非程式碼領域工作」的取向，本則鎖定影片生產而非社群媒體
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（500★）；[GitHub](https://github.com/aqm857886159/Nomi)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### awdr74100/figwright：雙向 Figma MCP，設計稿轉框架感知程式碼、程式碼變更可推回畫布（2026-09-06）

- **主線：** —
- **核心模式：** 免費雙向 Figma MCP 伺服器，可把 Figma 設計稿轉為框架感知的程式碼，也能把程式碼變更推回 Figma 畫布；支援 Claude Code、Cursor、Codex 等 MCP 客戶端；GitHub Search 累積 684 星
- **與既有模式的關係：** 補上「Plugin / MCP 整合」類別一個設計稿↔程式碼雙向同步的具體案例，此前該類多聚焦工具鏈協調與 context 載入，本則是設計工具整合的新取向
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（684★）；[GitHub](https://github.com/awdr74100/figwright)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### GitHub Search 存量盤點：feder-cr/AIHawk——開源瀏覽器自動化與電腦操作 agent，含 Claude Code／Gemini CLI 適用 Browser MCP（2026-09-05）

- **主線：** —
- **核心模式：** 開源 AI 瀏覽器自動化 agent，以自然語言操作網頁瀏覽與電腦操作（web browsing agent + computer-use agent），另提供可供 Claude Code 與 Gemini CLI 使用的 Browser MCP；GitHub Search 累積 30,311 星
- **與既有模式的關係：** 補上本頁「Plugin/MCP 整合」類別一個具體案例——不同於既有 Playwright／Chrome DevTools 類瀏覽器 MCP，AIHawk 本身是完整瀏覽器自動化 agent 再外掛 MCP 介面；非大型 codebase 特有痛點，暫不歸入 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 存量盤點條目，2024-08-04 出生、本庫今日首次收錄，累積時間跨度逾 1 年；僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（3.03 萬★，存量盤點｜2024-08-04 出生、本庫今日首次收錄）；[GitHub](https://github.com/feder-cr/AIHawk)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### internet-court/internet-court-skill：agent 對 agent 商業往來的信任層——自然語言協議＋ERC-7710 委任權限＋x402 支付＋履約爭議仲裁（2026-09-02）

- **主線：** —
- **核心模式：** 定位為「agent 對 agent 商業往來的信任層」，以自然語言協議、ERC-7710 委任權限、x402 支付機制與履約爭議仲裁機制，組成一個開放、通用的 Claude Code plugin／Agent Skill；GitHub Search 累積 5,317 星
- **與既有模式的關係：** 為本頁補上「agent 間商業／支付基礎設施」這個此前未見的類別——既有 Plugin/MCP 整合類目前聚焦工具鏈協作（context 共享、避免不必要載入），本則處理的是 agent 之間**經濟往來**的信任與爭議解決，屬不同層次的協作問題；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（5,317），惟僅取得 GitHub Search 星數，**無出生日期標記**、無 forks／issues／近期 commit 佐證可查，未另行查證，成長軌跡是否正常無法判斷；內容涉及加密貨幣支付軌道（x402、ERC-7710），此類題材過往較常見星數異常案例，本庫持保留態度收錄，讀者宜自行核實其實際採用程度
- **來源：** GitHub Search（5,317★，新發現，無出生日期標記）；[GitHub](https://github.com/internet-court/internet-court-skill)
- **成熟度：** ⏳ 新興（本庫首次收錄，星數來源與成長軌跡未經驗證，尚無其他社群採用回饋）

### 2026-08

#### Looker 原生 MCP Server：免安裝本機 292MB Toolbox 二進位檔，Claude Code 直接連線查詢 BI 資料（2026-08-14）

- **主線：** —
- **核心模式：** dev.to 文章說明 Looker（含 Google Cloud core 與原版）現已在每個執行個體自帶專屬 base URL 的 MCP 端點，Claude Code 等 agent 可直接連線查詢，不再需要先在本機下載安裝約 292MB 的 MCP Toolbox 二進位檔；文中同時誠實列出目前 Looker MCP 工具集的既知限制
- **與既有模式的關係：** 呼應本頁「Plugin / MCP 整合」類別既有「Claude Code 作為 MCP 協調中心」的取向，補上「BI／資料平台原生託管 MCP 端點、取代本機二進位安裝」這個此前未見於既有節點的整合形態——省去的是安裝與版本維護成本，而非 token 或 context 成本，與同類別「避免不必要 context 載入」的既有訊號互補而非重疊；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「Looker's Native MCP Server with Claude Code」— dev.to / #claudecode（依 dev.to 內容判斷原則收錄：具體描述架構變化並誠實列出限制，非純新聞轉述或行銷稿）
- **成熟度：** ⏳ 新興（單一文章描述官方新能力，尚無社群第一手串接實測或量化數據佐證）

#### 全部 26 個 MCP 工具以相同方式失敗：用排除測試鎖定 token 是根因（2026-08-14）

- **主線：** —
- **核心模式：** 作者記錄一次除錯過程：手上全部 26 個 MCP 工具皆以完全相同的方式失敗；透過設計測試排除其他變因（而非逐一檢查每個工具設定），確認問題根源出在 token 上，而非個別工具或伺服器設定
- **與既有模式的關係：** 呼應本頁「MCP 長 Session 穩健化」類別既有的三大失效模式防護（連線中斷、工具超時、上下文失憶），補上第四種此前未記錄的失效模式——token 設定錯誤導致「全部工具同時、同型態失敗」；也呼應本頁 08-08「先測量、再究責」方法論（生產環境 memory leak 除錯節點）在 MCP 除錯場景的對應版本：先用排除測試鎖定變因範圍，而非直覺猜測或逐一檢查
- **來源：** 「All 26 of My MCP Tools Failed the Same Way. My Test to Rule Out the Token Proved It Was the Problem.」— dev.to / #anthropic（3 讚；依規則以第一手除錯內容判斷，非讚數）
- **成熟度：** ⏳ 新興（單一作者第一手除錯記錄，具體 token 問題成因與修復方式未見於摘要，暫記觀察）

### 2026-07

#### Simon Willison：Stateless MCP 設計啟發打造 mcp-explorer 與 datasette-mcp 兩個小工具（2026-07-31）

- **主線：** —
- **核心模式：** Simon Willison 討論 MCP 2.0 推行的 Stateless MCP 設計方向，並分享受此啟發打造的 mcp-explorer 與 datasette-mcp 兩個小工具，聚焦「MCP server/tool 本身設計為無狀態」這個協定層設計面向
- **與既有模式的關係：** 呼應本頁「Plugin / MCP 整合」類別既有「避免不必要 context 載入」「Claude Code 主導 MCP 工具鏈協作」的關注，本篇補上更底層的協定設計面向——伺服器端無狀態化與 Claude Code 常用的 MCP 生態直接相關
- **來源：** 「Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)」— Simon Willison Blog（具名知名開發者第一手實作記錄）
- **成熟度：** ⏳ 新興（單一開發者早期工具，尚待社群採用驗證）

#### 自製 agent 失敗自動復原（auto-undo）機制，處理多工具連續呼叫中途失敗留下的混亂狀態（2026-07-31）

- **主線：** —
- **核心模式：** 作者針對 agent 連續呼叫多個工具的工作流中途失敗、遺留部分完成狀態導致環境混亂的問題，打造自動偵測並復原（undo）到失敗前狀態的機制
- **與既有模式的關係：** 呼應本頁「MCP 長 Session 穩健化」「破壞性操作安全閘門工具（GrapeRoot Pro）」類別對「失敗後如何收拾」面向的既有關注，本篇聚焦「失敗發生後自動回滾」而非「失敗前攔截」或「失敗中重試」，是本頁首次出現的自動復原（rollback）具體實作
- **來源：** 「I built a way to auto-undo the mess when an AI agent fails mid-task」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，尚無跨平台佐證，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興（單一開發者工具）；🔎 查無官方 ⟨Q-02⟩

#### nightshift：夜間遭遇跨模型 API 500 錯誤時自動等待錯誤解除並接續原對話（2026-07-31）

- **主線：** —
- **核心模式：** 作者本週遭遇跨模型錯誤率升高的情況，打造夜間排程工具 nightshift，遇到 `API Error: 500` 時不中斷任務，而是等待錯誤解除後自動 resume 回同一對話繼續執行，取代人工守夜重試
- **與既有模式的關係：** 延伸本頁「MCP 長 Session 穩健化」類別「心跳檢查、超時重試、session 狀態快照」等因應長 session 失效模式的既有做法，補上「API 層級錯誤等待 + 自動 resume」這個更貼近 Claude Code 本身（而非 MCP）錯誤處理的具體實作
- **來源：** 「Claude Code hits "API Error: 500" at 3 AM? nightshift now waits it out and resumes the same conversation」— Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，訊號強度較弱，依內容判斷收錄）
- **成熟度：** ⏳ 新興

#### Palmier Pro：開源 macOS 影片編輯器，內建 AI 生成與本機 MCP server（2026-07-23）

- **主線：** —
- **核心模式：** Palmier 團隊釋出開源 macOS 影片編輯器 Palmier Pro，內建 AI 影片生成能力，並提供本機 MCP server 供使用者連接自己的 agent，讓 agent 可直接操作編輯流程，而非侷限於程式碼協作場景
- **與既有模式的關係：** 屬本頁新出現的「創意工具 Agent 整合」類別——過往 Skills/MCP 整合案例多聚焦程式碼、雲端資源或知識管理，此案例將 agent 整合延伸至影片創作工具鏈本身，顯示 MCP 協定的應用場景正從開發者工具擴及一般創作軟體
- **來源：** 「Show HN: Palmier Pro – Open-source macOS video editor built for AI」— Hacker News（score 171，本輪最高分）
- **成熟度：** ⏳ 新興（今日首見，單一團隊產品，尚待社群採用回饋）

#### Agentty：以 C++26 撰寫的 Claude Code Drop-in 替代品，11MB 二進位檔（2026-07-15）

- **主線：** —
- **核心模式：** 開發者釋出 Agentty，一款以 C++26 撰寫、作為 Claude Code drop-in 替代方案的工具，編譯後二進位檔僅 11.0 MB；HN 討論中作者強調重點在於「harness 設計本身」而非單純呼叫底層模型 API，呼應本頁既有「確定性 Agent 框架」「Agentic Orchestrator」等強調 harness 架構設計的思路（推論：harness 設計價值獨立於底層模型選擇，可能是驅動此類替代實作出現的共同動機）
- **與既有模式的關係：** 屬「終端 Agent 工具」新實作；HN 討論中亦有人質疑以此方式使用 Claude OAuth 是否有帳號被封風險，屬未解疑慮，採用前需留意
- **來源：** 「Agentty – A drop-in alternative to claude-code, written in C++26. 11.0 MB binary」— Hacker News（score 38）
- **成熟度：** ⏳ 新興（今日首見，OAuth 使用風險尚待社群後續驗證）

**懸置細節**
- ⟨Q-02⟩ 🔎 **查無官方**（標 2026-08-10｜查 auto-undo、rollback｜複 2026-10-20）：複查（2026-09-20）原始 Reddit 貼文仍未能取得（reddit.com 網域對本工具封鎖擷取）。
  - 補充查得官方確有自動快照機制：[Checkpointing 文件](https://code.claude.com/docs/en/checkpointing)載明每次送出提示前自動快照檔案、`/rewind` 可還原至任一檢查點。
  - 但無法比對原貼文所指是否即為此機制。
