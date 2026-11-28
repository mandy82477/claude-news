---
page: "topics/community-creative-tools"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-11-26"
last_news_update: "2026-11-26"
status_main: "ongoing"
days_since_news: 2
parent: "topics/community-integrations"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 5
attribution_count: 3
attribution_last: "2026-11-26"
top_source: "github"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-12-05"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 社群做法：讓 agent 操作影片、3D、遊戲引擎等創作工具

社群把 Claude Code 等 coding agent 接進影片剪輯、Blender 3D、遊戲引擎、音效與設計軟體的做法，一則一則收在這頁。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-integrations]]
**開始日期：** 2026-07-23
**最後更新：** 2026-11-26
**最後新聞更新：** 2026-11-26

> **創意工具添雲端影片／圖片生成：gflow-cli 接 Google Flow 直接出 Veo 3.1 與 Nano Banana**（2026-11-26）
> ffroliva/gflow-cli 讓 Claude Code 等多款工具直接呼叫 Google Flow 產生 Veo 3.1 影片與 Nano Banana／Imagen 圖片，免費、MIT 授權；955 星。

---

## 摘要

這一群從 2026-07 的 Palmier Pro 開始，覆蓋範圍一路擴大：影片剪輯與生成（最多）、Blender／Unity／Unreal／Godot 等 3D 與遊戲引擎、ComfyUI、音效配樂、像素美術與網頁動畫。多數是單一作者工具（推論），僅 Epic Games 的 Unreal Engine skills 出自引擎廠商官方；尚無使用回報說明哪一款值得裝。Blender 一線出現同名外掛換帳號重發的現象，星數不宜當採用證據。MCP 與 plugin 的一般做法與 MCP 長 session 穩健化見母頁 [[topics/community-integrations]]；skill 本身怎麼設計見 [[topics/community-skills]]。

---

## 目前結論

- **影片是最熱的一類**：十一月新節點以影片剪輯與生成工具為主（openmotion、ChatCut、ghost-editor、Kino AI 等），取向從「生成」延伸到「人機共用同一條時間軸」。
- **3D 與遊戲引擎已三大引擎齊備**：Godot（GodotMaker）、Unity（unity-mcp-server）、Unreal（Epic 官方 skills）；Blender 生態最擠，也最常見疑似刷星的重複發布。
- **採用證據仍薄**：全部節點皆為首次收錄、單一作者為主，未見採用回饋；看星數前先查帳號歷史與連結是否仍有效。
- **你的選項：** 想讓 agent 碰創作軟體，先找該軟體官方或最多實作的那一款，再看它是 MCP 還是 skill 形態、會載入多少工具定義進 context。

---

## 技術彙整

### 2026-11

#### ffroliva/gflow-cli：MCP server／CLI 接 Google Flow，直接從 Claude Code 出 Veo 3.1 影片與 Nano Banana／Imagen 圖片（2026-11-26）

- **主線：** —
- **核心模式：** MCP server 與 CLI 雙形態，讓 Claude Code、Claude Desktop、Cursor、VS Code、Codex 或終端機能直接呼叫 Google Flow 產生 Veo 3.1、Omni 影片與 Nano Banana／Imagen 圖片；免費、MIT 授權，PyPI 上架；近 2 天新增約 289 星（約 144 星/日），累積 955 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「接外部雲端生成服務而非本機創作軟體」取向——既有做法多接 Blender、Unity 等本機工具或 ComfyUI 本機 pipeline，本則直接呼叫 Google 雲端影像／影片生成 API；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（955★）與近 2 天星速，forks／issues／近期 commit 佐證未查，未另行查證；星速達每日 144 星，尚待下一輪連結健檢確認是否為正常採用或批次效應。
- **來源：** GitHub Search；[GitHub](https://github.com/ffroliva/gflow-cli)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，MIT 授權已上架 PyPI，尚無第三方採用回饋數據）

#### op7418/guizang-game-skill：歸藏 Game Skill，Claude Code／Codex 從零生成可玩瀏覽器 3D 動作遊戲，附demo《霧鎖山門》（2026-11-25）

- **主線：** —
- **核心模式：** Agent skill 讓 Claude Code、Codex 從零生成可在瀏覽器執行的 3D 動作遊戲，AI 產生素材並以 three.js、單一 HTML 檔輸出；附可玩 demo《霧鎖山門》；GitHub Search 506 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「skill 直接生成完整可玩遊戲」取向——既有做法多是接進既有創作軟體或輸出動畫／影片素材，本則輸出的是可互動的瀏覽器遊戲本體，與同日 Moh4696/open-3d-skills 同屬本輪新出現的「3D／遊戲向 skill」取向；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（506★），無 forks／issues／近期 commit 佐證可查，未另行查證；與同日另外 4 款倉庫（502、502、136、130 星）同一時間點（19:59 UTC）同步衝上 GitHub 搜尋榜，疑似批次快照效應，真實熱度未能進一步驗證。
- **來源：** GitHub Search；[GitHub](https://github.com/op7418/guizang-game-skill)
- **成熟度：** ⏳ 新興（本庫首次收錄，附可玩 demo，尚無第三方採用或複現數據）

#### Moh4696/open-3d-skills：8 個 three.js／3D 動畫網站 agent skill，涵蓋場景生成到 60fps 錄製（2026-11-25）

- **主線：** —
- **核心模式：** 8 個針對 3D 與動畫網站的 agent skill：從程式碼生成 three.js 場景、捲動式影片（scroll film）、透明影片、游標裝置、爆炸視圖（exploded view）、AI 動態素材、瀏覽器檢查到 60fps 錄製；供 Claude Code、Codex、Cursor、Gemini CLI 使用；GitHub Search 502 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「網頁 3D／動畫技能包」取向——既有做法多鎖定遊戲引擎本體，本則把瀏覽器 three.js 動畫從生成拆到錄製共 8 個獨立 skill；與同日 guizang-game-skill 同屬「3D／遊戲向 skill」取向；主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（502★），無 forks／issues／近期 commit 佐證可查，未另行查證；與同日另外 4 款倉庫（506、502、136、130 星）同一時間點（19:59 UTC）同步衝上 GitHub 搜尋榜，疑似批次快照效應，真實熱度未能進一步驗證。
- **來源：** GitHub Search；[GitHub](https://github.com/Moh4696/open-3d-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無第三方採用或複現數據）

#### bookwjitchieni1986/blender-ai-mcp-addon：同名 Blender MCP 外掛兩個月內第三度換帳號出現（2026-11-21）

- **主線：** —
- **核心模式：** 與兩個月內另兩次同名同描述的 Blender MCP 外掛（hitkeeen 11-16、LiCinCan 10-18，原連結皆已失效）相同，本次由第三個帳號 bookwjitchieni1986 發布；近 2 天新增約 1,871 星，累積 2,075 星。
- **與既有模式的關係：** 不計入「創意工具 Agent 整合」代表技巧——同一描述換帳號重發兩次後連結皆已失效，本次第三度出現星速異常，佐證為重複假帳號衝星數，非新做法；主線填 —。
- **可信度註記：** ❓ **待查證**（標 2026-11-21｜查 blender-ai-mcp-addon、bookwjitchieni1986）｜**是否為重複假帳號衝星數手法**：星速偵測收錄（近 2 天 +1,871 星，約 936 星/日），無 forks／issues／近期 commit 佐證可查，待下一輪連結健檢確認是否重演。
- **來源：** GitHub Search；[GitHub](https://github.com/bookwjitchieni1986/blender-ai-mcp-addon)
- **成熟度：** ⏳ 新興（本庫首次收錄，同名專案第三度換帳號出現，疑似假星數手法，尚無第三方採用或複現數據）

#### nexu-io/openmotion：開源 Claude Motion／CapCut 替代品，全端 agentic 影片工作室支援 22 款 agent（2026-11-19）

- **主線：** —
- **核心模式：** 開源的 Claude Motion／CapCut 替代品，把參考影片轉成可編輯動態圖像並套用品牌素材，匯出短影音格式；全端 agentic 影片工作室，支援 22 款 agent（含 Claude）；近 2 天新增約 1,954 星（約 977 星/日），累積 12,737 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」（[[topics/community-creative-tools#2026-11]]）一個「取代既有商業剪輯軟體」取向——既有做法多是技能包，本則是獨立全端產品；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 星速偵測收錄（近 2 天 +1,954 星，約 977 星/日），無 forks／issues／近期 commit 佐證可查，未另行查證；22 款 agent 的具體清單與相容程度未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/nexu-io/openmotion)
- **成熟度：** ⏳ 新興（本庫首次收錄，星速偏高，尚無第三方採用或複現數據）

#### arjun988/blender-skills：94 個 Blender 專精 skill 組成完整生產管線，供 Cursor／Claude Code／Kiro／Codex 使用（2026-11-17）

- **主線：** —
- **核心模式：** 94 個 Blender 專精技能（specialist skills）透過 MCP 串接，涵蓋從 blockout 建模到遊戲引擎匯出的完整生產管線，供 Cursor、Claude Code、Kiro、Codex 使用；近 2 天新增約 494 星（約 247 星/日），GitHub Search 累積 4,084 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有 Blender 代表技巧一個「技能庫而非外掛／copilot」取向——既有做法是單一外掛接多供應商模型，本則拆成 94 個獨立技能模組組成生產管線；主線填 —。
- **可信度註記：** 星速偵測收錄（近 2 天 +494 星，約 247 星/日），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，94 個技能的具體清單未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/arjun988/blender-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，星速偏高，尚無第三方採用或複現數據）

#### ChatCut-Inc/agent-plugin：對話剪輯自己素材的 AI 影片編輯器，plugin＋MCP server 同時相容八款 agent 客戶端（2026-11-17）

- **主線：** —
- **核心模式：** ChatCut 推出的影片編輯 plugin 與 MCP server，供 Codex、ChatGPT、Claude Code、Cursor、Grok、Gemini CLI、WorkBuddy、Doubao Work、Qwen Work 使用；可用對話剪自己拍的素材、加字幕、去除冗音與填充詞、產生動態圖像，並匯出可編輯時間軸；GitHub 累積 1,055 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（cth9191/animate 等生成式影片工具，[[topics/community-creative-tools#2026-11]]）一個「剪輯使用者既有真實素材」取向——既有做法多是生成全新影片內容，本則針對使用者自己拍好的素材做對話式剪輯；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub 星數（1,055★），無 forks／issues／近期 commit 佐證可查，未另行查證；匯出時間軸相容哪些剪輯軟體未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/ChatCut-Inc/agent-plugin)
- **成熟度：** ⏳ 新興（本庫首次收錄，多客戶端相容，尚無第三方採用或複現數據）

#### tuzhechen2005/opus-video-skills：Claude Opus 5.5 專用影片製作 skill 庫，一風格一技能、逐格與分鏡皆由程式產生（2026-11-17）

- **主線：** —
- **核心模式：** 供 Claude Code 中 Claude Opus 5.5 使用的影片製作 skill 庫，每種風格獨立成一個 skill（如手繪動畫、動態排版影片），逐格畫面與分鏡筆記皆由程式碼產生；GitHub 525 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「單一風格單一 skill」的影片製作庫取向——與 cth9191/animate 同屬程式化動畫，本則改用技能庫拆分風格而非單一工具內建風格選單，與 arjun988/blender-skills（見上）同屬本輪新出現的「專精 skill 庫」做法；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（525★），無 forks／issues／近期 commit 佐證可查，未另行查證；技能總數與具體風格清單未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/tuzhechen2005/opus-video-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### hitkeeen/blender-ai-mcp-addon：Blender 用的多模型 AI／MCP 外掛，視覺化對話＋場景工具＋multi-agent 工作流（2026-11-16）

- **主線：** —
- **核心模式：** Blender 外掛＋MCP server，供 ChatGPT、Claude、Gemini、Ollama、OpenCode 等多款模型使用，提供視覺化對話介面、場景操作工具與 multi-agent 工作流；近 3 天新增約 1,995 星（約 665 星/日），GitHub Search 累積 2,123 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（blender-ai-copilot-hub 等，[[topics/community-creative-tools#2026-11]]）本週第二個多模型接 Blender 實作——既有做法聚焦場景工具與連線管理，本則另加視覺化對話與 multi-agent 工作流；主線填 —。
- **可信度註記：** 星速偵測收錄（近 3 天 +1,995 星，約 665 星/日），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，multi-agent 工作流具體機制未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/hitkeeen/blender-ai-mcp-addon)（原文已失效，2026-11-20 連結健檢；URL 保留供查 web archive）
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，星速異常偏高，尚無第三方採用或複現數據）

#### cth9191/animate：Claude Code 專用程式化動畫工具，單檔案輸出短篇 canvas 動畫並配分鏡回饋（2026-11-16）

- **主線：** —
- **核心模式：** 供 Claude Code 使用的程式化動畫工具，產出單檔案、任意風格的短篇 canvas 動畫；內建 7 種風格可選，或自動比對參考素材抓風格，可配自己的音樂與真實產品截圖，過程附故事與分鏡回饋 check-in。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（andyhuo520/digital-human-koubo 等生成式影片工具，[[topics/community-creative-tools#2026-11]]）一個「程式化動畫＋分鏡回饋迴圈」取向——既有做法多是單次生成，本則在生成過程加入故事與分鏡的中途檢查點；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（2,054★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，具體「分鏡 check-in」互動方式未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/cth9191/animate)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### andyhuo520/digital-human-koubo：一張照片生成數字人說話影片，5 種剪輯風格＋48 個打包元件（2026-11-15）

- **主線：** —
- **核心模式：** 由一張照片生成數字人（digital human）說話影片的 agent skill：以 Renoise MCP 做生成，提供 5 種編輯風格與 48 個「創作者級」打包元件，供 Claude Code、Codex、OpenClaw、WorkBuddy 等多款 agent 使用；GitHub Search 1,993 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（ghost-editor 對嘴素材剪輯等，[[topics/community-creative-tools#2026-11]]）一個「單張照片生成數字人影片」取向——既有做法多是剪輯既有素材，本則改為從單張照片直接生成會說話的數字人影像；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,993★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，48 個打包元件與 5 種剪輯風格的具體內容未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/andyhuo520/digital-human-koubo)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### imraywang/ray-sticker-shop：一張照片或角色圖生成一整套形象一致的動態表情包與微信投稿素材（2026-11-15）

- **主線：** —
- **核心模式：** 供 Claude Code／Codex 使用的 skill：輸入一張照片或角色圖，生成一整套角色形象一致的動態表情包（貼圖）與微信投稿素材；GitHub Search 500 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（open-carrusel 社群媒體輪播圖等，[[topics/community-creative-tools#2026-11]]）一個「角色一致性貼圖包生成」取向——既有做法多是單張靜態排版，本則要求整套輸出維持同一角色形象一致；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，角色一致性具體做法未見報導（細節未載）。
- **來源：** GitHub Search；[GitHub](https://github.com/imraywang/ray-sticker-shop)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### baiblinocun1986/blender-ai-copilot-hub：多供應商 AI copilot 中樞接進 Blender，27 個受監督場景工具＋內建 MCP server（2026-11-15）

- **主線：** —
- **核心模式：** Blender 用的多供應商 AI copilot 中樞：把 OpenAI、Anthropic Claude、Google Gemini、OpenRouter、OpenCode Zen、Ollama 與自訂端點都接進同一套已儲存連線管理中心，附 27 個受監督的場景操作工具與內建 MCP server；GitHub Search 466 星（2 個來源）。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧一個「多 LLM 供應商可切換」取向——既有 Blender 整合多綁單一供應商，本則讓使用者切換不同廠商模型，並對場景操作加監督把關；主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（466★，2 個來源），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search（2 個來源）；[GitHub](https://github.com/baiblinocun1986/blender-ai-copilot-hub)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### Hainrixz/open-carrusel：與 Claude 對話設計 Instagram 輪播圖，匯出符合官方尺寸的 PNG（2026-11-14）

- **主線：** —
- **核心模式：** AI 輔助的 Instagram 輪播圖產生器，與 Claude 對話設計每張投影片，匯出符合 Instagram 官方規格尺寸的 PNG；Claude Code 中輸入 `/start` 即可啟動；GitHub Search 522 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro 等）一個「社群媒體輪播圖設計」取向——既有做法多鎖定影片或遊戲素材，本則把對話式設計延伸到 Instagram 輪播圖排版與匯出；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（522★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，日報未另行收錄。
- **來源：** GitHub Search；[GitHub](https://github.com/Hainrixz/open-carrusel)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### kurbaitaev/ghost-editor：開源 AI 影片編輯器，把對嘴素材剪成成品 reel（2026-11-14）

- **主線：** —
- **核心模式：** 開源 AI 影片編輯器，供 Claude Code 使用，輸入未經剪輯的對嘴（talking-head）素材，輸出剪好的成品短影片；GitHub Search 516 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（reelmimic 等）一個「對嘴素材轉短影片」取向——既有做法多以參考影片定風格或分段規劃，本則聚焦單一素材類型（對嘴講話）直接產出成品；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（516★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述較簡略，日報未另行收錄。
- **來源：** GitHub Search；[GitHub](https://github.com/kurbaitaev/ghost-editor)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### Launch HN: Kino AI (YC S23)——團隊與 Claude Code／Codex 共用同一條影片剪輯時間軸（2026-11-04）

- **主線：** —
- **核心模式：** 整合素材儲存、剪輯器與審閱連結的 AI 影片協作工具，讓團隊成員與 Codex、Claude Code 這類 coding agent 在同一條時間軸上一起剪片、留審閱備註。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「人機共用同一條時間軸」取向——既有例子多是 agent 單獨操作創作軟體，本則讓真人協作者與 agent 共享同一個工作區；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** YC S23 團隊正式產品發布（Launch HN），非匿名倉庫星數訊號；Hacker News 95 分。
- **來源：** Hacker News；[官方網站](https://kino.ai)
- **成熟度：** ⏳ 新興（本庫首次收錄，團隊產品剛發布，尚無第三方採用回饋）

#### HamSanders/soundbox：本機免費開源 AI 音效、配樂與語音克隆，21 工具 MCP server 接 Claude Code（2026-11-02）

- **主線：** —
- **核心模式：** 本機運行、免費開源的 ElevenLabs／Suno 替代品，用自己的 GPU 跑 AI 音效、帶歌詞配樂、文字轉語音與語音克隆（底層含 Stable Audio、ACE-Step 等模型）；免帳號免點數、可離線，提供 Windows／macOS app、HTTP API，以及一個 21 工具的 MCP server 供 Claude Code、Cursor 使用。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、reelmimic、GodotMaker、Quick Study 等，[[topics/community-creative-tools#2026-10]]）一個音訊創作類實作——既有例子多在影像／遊戲／設計場域，本則擴到音效與語音；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 查核 commit 記錄，近期由作者本人與 dependabot 共同提交（依賴更新、功能修正），非一次性發布後棄置；GitHub 132★，規模不大但有持續維護訊號。
- **來源：** GitHub Search；[GitHub](https://github.com/HamSanders/soundbox)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### actionow-ai/vvv：開源可編輯影片範本打包為 Agent Skill，一次製作跨 25+ coding agent 複用（2026-11-01）

- **主線：** —
- **核心模式：** 開源、可編輯的影片範本（示例為婚禮影片）包成 Agent Skill，一次打造即可在 Claude Code、Codex 等 25+ 款 coding agent 上重複使用，免去每個工具各自重寫一套範本；510★。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「範本可攜性」取向——既有做法多是把創作軟體整合進 agent，本則把範本本身包成可跨 25+ 款 agent 安裝的 Skill；主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（510★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/actionow-ai/vvv)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

### 2026-10

#### Simon Willison：Quick Study，Opus 5.5 以 Sobel 邊緣偵測即時模擬畫筆作畫（2026-10-24）

- **主線：** —
- **核心模式：** Simon Willison 提示 Claude Opus 5.5 High 打造 artifact：開啟一張照片後，用 canvas 元素與模擬畫筆於數秒內「畫」出該照片的畫作版本，核心技術為 Sobel 邊緣偵測，除 Google Fonts 外無外部函式庫；延續其先前用 Fable 模擬水彩插畫（P5.js）的實驗系列。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「單一提示生成獨立繪圖 artifact」取向——既有代表技巧多是把 agent 接上既有創作軟體（Aseprite、Unity、Blender），本則是模型直接生成繪圖程式本身，不依賴外部創作工具；非大型 codebase 特有痛點，主線填 —。
- **來源：** Blog／Simon Willison（具名開發者第一手實作記錄）；[原文](https://simonwillison.net/2026/Oct/23/quick-study-painter/)
- **成熟度：** ⏳ 新興（單次示範，非工具發布，無法複用為套件）

#### with-pebbly/aseprite-ai-artist：coding agent 直接在開著的 Aseprite 視窗畫像素風美術（2026-10-21）

- **主線：** —
- **核心模式：** MCP server ＋ skills，讓 coding agent 在使用者已開啟的 Aseprite 視窗內作畫、檢視成果、animate 與匯出；同時相容 Claude Code、omp、Codex、Gemini CLI、Cursor；附公開畫廊與基準站 pixeli.pebbly.space；GitHub Search 438 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Unity MCP Server、blender-ai-mcp-addon 等遊戲／3D 創作整合）一個「2D 像素美術」方向——既有做法多鎖定遊戲引擎與 3D 建模，本則把 agent 整合延伸到像素美術編輯器；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（438★），無 forks／issues／近期 commit 佐證可查，未另行查證；具體繪製與動畫機制未見細節。
- **來源：** GitHub Search；[GitHub](https://github.com/with-pebbly/aseprite-ai-artist)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### LiCinCan/blender-ai-mcp-addon：Blender 的 AI 助理與 MCP 伺服器外掛，支援多 agent 工作流程（2026-10-18）

- **主線：** —
- **核心模式：** Blender 外掛提供 AI 助理與 MCP 伺服器，支援視覺化對話、場景工具操作與多 agent 工作流程，可接 Claude、ChatGPT、Gemini、Ollama、OpenCode 等模型；GitHub Search 累積 736 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」一個「3D 建模工具（Blender）」取向——既有做法多接影片、遊戲引擎，本則延伸到 3D 建模與 bpy Python 腳本層；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（736★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/LiCinCan/blender-ai-mcp-addon)（原文已失效，2026-10-23 連結檢查回 404；URL 保留供追溯）
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### AnkleBreaker-Studio/unity-mcp-server：Unity MCP Server，268 個工具支援 AI 輔助遊戲開發（2026-10-14）

- **主線：** —
- **核心模式：** MCP server 讓 Claude、Cursor 等任何 MCP client 連上 Unity Editor／Unity Hub，提供 268 個工具涵蓋場景管理、GameObject／元件、建置、效能分析、Shader Graph、Amplify、地形、物理、NavMesh、動畫與 MPPM 多人連線；免費開源；GitHub Search 504 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（GodotMaker、EpicGames Unreal Engine skills）第三款引擎整合，補齊 Unity；三者工具形態不同，暫各自列；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 經查 forks 65（約星數 12.9%，高於 1/10 健康區間）；開發方為具名遊戲工作室組織帳號（非個人），倉庫 10-06 仍有實質 push。
- **來源：** GitHub Search；[GitHub](https://github.com/AnkleBreaker-Studio/unity-mcp-server)
- **成熟度：** ⏳ 新興（本庫首次收錄，具名工作室開發，尚無社群採用回饋數據）

#### oil-oil/oil-motion：網頁動畫 skill，做出跟著捲動與滑鼠移動的網頁動態效果（2026-10-12）

- **主線：** —
- **核心模式：** Claude Code 與 Codex 共用的網頁動畫 skill，協助產生跟隨捲動（scroll-driven）與跟隨滑鼠移動的網頁動態效果；GitHub Search 2,575 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、reelmimic、GodotMaker 等）一個「網頁互動動畫」取向——既有做法多聚焦影片或遊戲產出，本則鎖定網頁捲動／滑鼠互動效果這個前端細分場景；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（2,575★），無 forks／issues／近期 commit 佐證可查，未另行查證；原始描述僅標題可用（殼層摘要）。
- **來源：** GitHub Search；[GitHub](https://github.com/oil-oil/oil-motion)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### EpicGames/unreal-engine-skills-for-claude-code-plugin：Epic Games 官方釋出 Unreal Engine skills，供 Claude Code 外掛使用（2026-10-12）

- **主線：** —
- **核心模式：** Epic Games 官方帳號釋出一組 Unreal Engine skills，供 Claude Code 外掛在 Unreal Engine 專案中使用；GitHub Search 527 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（GodotMaker 等）一個「官方遊戲引擎廠商自建」取向——GodotMaker 是社群把 Claude Code 接上 Godot，本則是遊戲引擎廠商自己發布 Unreal Engine 的官方整合；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 原始描述僅標題可用（殼層摘要），依日報段落判讀；僅有 GitHub Search 星數（527★），無 forks／issues 佐證可查；官方遊戲引擎廠商帳號發布，造假誘因低於個人開發者項目（推論）。
- **來源：** GitHub Search；[GitHub](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin)；企業採用面見 [[topics/enterprise-tool-tracker]]
- **成熟度：** ⏳ 新興（本庫首次收錄，官方遊戲引擎廠商發布，尚無社群採用回饋數據）

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

#### rehan-remade/universal-modder：讓 Claude Code 改裝任意 PC 遊戲的 skills／工具組合（2026-10-01）

- **主線：** —
- **核心模式：** 整合 skills、工具與 fal MCP，讓 Claude Code 對任意 PC 遊戲進行偵查、反組譯分析、fal 生成美術／3D／音效、遊戲內測試與成果影片產出；GitHub Search 1,388 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、anything2explainer、chess-postmortem-skills、video-talkcraft）一個「遊戲改裝」取向，既有做法多聚焦單一風格影片或棋局分析，本則把反組譯分析與素材生成整進同一改裝流程；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,388★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/rehan-remade/universal-modder)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

### 2026-09

#### Vincentwei1021/video-talkcraft：配音驅動動態設計工作室 agent skill（2026-09-30）

- **主線：** —
- **核心模式：** Agent skill，把 Claude Code／Codex 變成動態設計工作室，產出配音驅動的解說影片；含逐字稿配音同步、109 套運鏡範本卡、反投影片式運鏡系統，以 Remotion 算圖；GitHub Search 1,314 星。
- **與既有模式的關係：** 補上「創意工具 Agent 整合」既有代表技巧（Palmier Pro、anything2explainer、chess-postmortem-skills、lemo-opuscar）一個「配音驅動動態設計」取向，既有做法多聚焦單一風格化影片或棋局分析，本則另附大量運鏡範本卡與逐字稿同步機制；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,314★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Vincentwei1021/video-talkcraft)（原文已失效）
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

### 2026-07

#### Palmier Pro：開源 macOS 影片編輯器，內建 AI 生成與本機 MCP server（2026-07-23）

- **主線：** —
- **核心模式：** Palmier 團隊釋出開源 macOS 影片編輯器 Palmier Pro，內建 AI 影片生成能力，並提供本機 MCP server 供使用者連接自己的 agent，讓 agent 可直接操作編輯流程，而非侷限於程式碼協作場景
- **與既有模式的關係：** 屬本頁新出現的「創意工具 Agent 整合」類別——過往 Skills/MCP 整合案例多聚焦程式碼、雲端資源或知識管理，此案例將 agent 整合延伸至影片創作工具鏈本身，顯示 MCP 協定的應用場景正從開發者工具擴及一般創作軟體
- **來源：** 「Show HN: Palmier Pro – Open-source macOS video editor built for AI」— Hacker News（score 171，本輪最高分）
- **成熟度：** ⏳ 新興（今日首見，單一團隊產品，尚待社群採用回饋）
