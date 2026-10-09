---
page: "topics/community-skills"
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
inbound_links: 1
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
# 社群做法：Skills 怎麼寫

社群寫 Claude Code skill 的做法：怎麼寫才會被觸發、有哪些慣例和地雷、品質怎麼量。

**狀態：** ongoing
**領域：** 🌐 社群
**上層：** [[topics/community-tech-patterns]]
**開始日期：** 2026-07-12
**最後更新：** 2026-10-09
**最後新聞更新：** 2026-10-07

> **最新做法**（2026-10-07）
> - **把創業流程封裝成 skill**：claude-skills-founder 從終端機產出產品簡報、競品分析、定價策略與募資 deck。
> - **平實語言寫的 skill**：10-02 open-steps 給 Claude Code、Codex、Cursor、Gemini CLI 共用。

---

## 摘要

官方的寫法規範在 [官方 skills 文件](https://code.claude.com/docs/en/skills)，什麼時候該把流程做成 skill、skill 和 hook 各管什麼，見 [[topics/coding-workflow-guide]]。本頁收社群實際寫出來的 skill 與踩到的坑；該裝哪些現成 skill 見 [[topics/community-tech-tools]]「Skills 速查」，官方 Skills 產品線見 [[entities/claude-skills]]。

## 慣例與地雷

**慣例（社群目前的寫法）**
- **description 就是觸發器**：session 啟動時只把 name 和 description 建成索引，SKILL.md 本體要等描述對上提示才載入——描述寫得籠統，skill 就永遠不會被叫起來。出處：〈Skill 不觸發的根因：session 啟動只索引 name+description，本體不預先載入〉（2026-08-04，見下方 2026-08）。
- **一個 skill 只做一件事**：單一職責的寫法自 2026-05 起沒有人再反對，見 [[topics/community-tech-discussions]]「現在吵到哪」表下。

**地雷（會靜默失效的地方）**
- **描述字數有預算**：單一 skill 的 description 加 when_to_use 上限 1,536 字元，整份清單的預算約為 context 的 1%；skill 裝多了，舊的會被悄悄擠出清單、不報錯。出處：〈Claude Code Skills 清單字元預算機制：description 超額會讓既有 skill 悄悄失效〉（2026-07-28，見下方 2026-07）。
- **公開 skill 多數觸發寫法不可靠**：一份對 216 個公開 skill 的靜態檢查，判 69% 的觸發條件寫法不可靠。出處：〈Show HN：Linting 216 個公開 Claude Code skills——69% 觸發條件寫法不可靠〉（2026-09-17，單一作者工具，見 [[topics/community-guardrails#2026-09]]）。
- **品質量得出來，但只有個案**：用 linter 掃一個高星 repo 的 24 個 skill 得 84/100，歸納出邊界不明、指令模糊等共通問題。出處：〈Skill Linter 對 52k-Star Repo 的 84/100 診斷案例：Skill 品質共通模式〉（2026-07-12，見下方 2026-07）。

證據強度：前兩條地雷各只有一位作者的第一手拆解或工具，沒有第二方重現；慣例第一條也是單一作者的機制說明。

---

## 目前結論

- **Skills 正從「指令封裝」變成「知識框架載體」**：單一職責的寫法已獲社群反覆驗證（[[topics/community-skills#2026-09]]）。**接下來看什麼：** 第三方 skill 的品質量測（可靠性測試那一類）會不會補上來。
- **你的選項：** 寫新 skill 前先把 description 寫成「什麼時候該叫我」的具體條件；skill 一多就檢查清單有沒有被擠掉；要硬擋的規則改用 hook。

---

## 技術彙整

### 2026-10

#### emotixco/claude-skills-founder：給創業者的 Claude Code Skills，從終端機產出產品簡報、競品分析、定價策略、募資 deck 與 GTM 計畫（2026-10-07）

- **主線：** —
- **核心模式：** 一套 Claude Code skills，鎖定創業者族群，從終端機直接產出產品簡報、競品分析、定價策略、募資 pitch deck 與 go-to-market 計畫；GitHub Search 507 星。
- **與既有模式的關係：** 為「Skills 設計」補上「創業商業面」這個垂直領域——既有 rsmdt/the-startup 訴求工程面「生產級」技能集合，本則改鎖定非工程的商業產出（簡報、定價、GTM），兩者取向不同、不合併；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（507★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/emotixco/claude-skills-founder)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一作者工具，尚無社群採用回饋數據）

#### kharmanskyi/open-steps：給 Claude Code、Codex、Cursor、Gemini CLI 的平實語言 agent skills（2026-10-02）

- **主線：** —
- **核心模式：** 跨 Claude Code、Codex、Cursor、Gemini CLI 的平實語言 agent skills，產出誠實的 session 報告與直白結論、可依循的步驟；MIT 授權；GitHub Search 1,078 星。
- **與既有模式的關係：** 補上「Skills 設計」既有代表技巧（知識框架化、drawio-skill、personal-os-skills、reladraw、geo-sleuth、geo-score 等）一個「誠實回報」取向——既有做法多聚焦知識封裝或流程自動化，本則鎖定「不浮誇、說真話」的 session 報告風格；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,078★），無 forks／issues／近期 commit 佐證可查，未另行查證；近 3 天星數穩定成長（1,071→1,077→1,078），非短時間異常暴衝。
- **來源：** GitHub Search；[GitHub](https://github.com/kharmanskyi/open-steps)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

### 2026-09

#### Anionex/agent-vision-toolkit：為純文字模型補視覺能力的工具箱與 skill（2026-09-30）

- **主線：** —
- **核心模式：** 為純文字模型「看圖」設計的視覺工具箱與 skill，支援多圖理解、圖片問答、長截圖 OCR、前端 UI 還原、GUI 自動化，可選接入 Codex、Claude Code、Pi、Oh My Pi、OpenCode，並可直接識別貼上的圖片；GitHub Search 1,219 星。
- **與既有模式的關係：** 本表既有類別皆未鎖定「替純文字模型補視覺感知能力」這個應用面，與「Skills 設計」相近但服務對象不同——本則補的是模型本身缺的感知能力，不是知識／流程的封裝，暫不併入既有列，留待第二個同類實作出現再判斷是否需要新類別（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,219★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Anionex/agent-vision-toolkit)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### decodingai-magazine/building-a-coding-agent-from-scratch-course：從零打造 Claude Code 風格 agent 教學課程（2026-09-30）

- **主線：** —
- **核心模式：** 用 Python 從零打造 Claude Code 風格編碼 agent 的教學課程，含 8 篇文章、4 支影片與完整程式碼；GitHub Search 501 星。
- **與既有模式的關係：** 屬課程／教材類資源盤點，非新做法或工具，與 2026-09-24 Callous-0923/agent-study 同屬彙整型教學參考資料，不進模式概覽表；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（501★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊教材，尚無社群採用回饋數據）

#### Serokell：把內部工程規範轉為 Claude Code skills（2026-09-29）

- **主線：** —
- **核心模式：** 工程顧問公司 Serokell 分享把內部工程規範轉成 Claude Code skills 的做法，動機是 coding agent 熟悉語法但不熟悉團隊內部慣例；同一篇同步登上 r/ClaudeCode 與 r/ClaudeAI（2 個來源同日出現）。
- **與既有模式的關係：** 補上「Skills 設計」既有代表技巧「知識框架化」一個具名真實企業案例——把公司工程規範（而非公開書籍／流程）封裝成 skill；具體轉換機制原文遭截斷未載，暫不確認是否構成新取向。
- **可信度註記：** Reddit 貼文，0 留言，但 r/ClaudeCode＋r/ClaudeAI 兩個來源同日出現，符合跨來源門檻；內容細節僅摘要可讀，原文被截斷。
- **來源：** Reddit / r/ClaudeCode ＋ Reddit / r/ClaudeAI；[原文](https://www.reddit.com/r/ClaudeCode/comments/1wteorc/how_we_use_claude_code_at_serokell/)
- **成熟度：** ⏳ 新興（本庫首次收錄，具名企業案例，尚無社群回饋數據）

#### jianruntech/geo-score：GEO（生成式引擎優化）評分與跨模型引用追蹤 MCP 伺服器（2026-09-29）

- **主線：** —
- **核心模式：** 用自帶 API 金鑰對 OpenAI、Perplexity、Gemini、Claude 做引用追蹤，依開放 GEO 準則提供免費 0–100 就緒度評分；零依賴，MCP 伺服器；GitHub Search 616 星。
- **與既有模式的關係：** 補上「Skills 設計」既有 SEO／GEO 代表技巧（fire-your-seo-agency、open-seo-mcp-skills）一個「跨模型引用追蹤」取向，既有兩例聚焦稽核／優化排名，本則鎖定「AI 引擎有沒有真的引用你的網站」這個量測面；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（616★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/jianruntech/geo-score)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### 同日三款 Skills 設計新實作：headcount（公司化 agent 組織）、personal-os-skills（Obsidian）、reladraw（可控版面圖表語言＋agent skill）（2026-09-27）

- **主線：** —
- **核心模式：**
  - headcount：把 agent 組織成一間公司，15＋部門、125＋個各自可獨立安裝的 skill，每個 skill 附上其依據的標準或監管機構出處；可跑在 Claude Code 與 ChatGPT（1,684★）
  - personal-os-skills：一套給 Obsidian 用的 Claude Code skills（537★）
  - reladraw：可自訂版面配置的圖表描述語言，附 npm 套件與可搭配 Claude 等 agent 使用的 skill，作者不滿 Mermaid／Graphviz 自動排版與 Draw.io 太耗時；Hacker News 351 分
- **與既有模式的關係：** 補上「Skills 設計」既有代表技巧三個新取向——組織化 skill 目錄（headcount）、Obsidian 整合（personal-os-skills）、圖表描述語言（reladraw，與既有 drawio-skill 同屬圖表類但走描述語言而非工具整合）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** headcount／personal-os-skills 僅有 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；reladraw 來自 Hacker News，351 分遠高於當日其他討論，惟未見留言數或跨平台佐證。
- **來源：** GitHub Search；[headcount](https://github.com/cbrock84/headcount)（1,684★）、[personal-os-skills](https://github.com/ArtemXTech/personal-os-skills)（537★）；Hacker News；[reladraw](https://github.com/reladraw/reladraw)（351 分）
- **成熟度：** ⏳ 新興（三者皆本庫首次收錄，尚無社群採用回饋數據）

#### 同日四款專項 Skills 合集：nature-skills、emilkowalski/skills、drama-skills、asd-ste100-skill（2026-09-26）

- **主線：** —
- **核心模式：**
  - nature-skills：符合 Nature 論文學術表達與科研繪圖規範的 skill（44,559★，2026-04 出生，本庫今日首次收錄，forks 2,338）
  - emilkowalski/skills：給設計師與工程師使用的通用 skills 集合（41,183★，2026-03 出生，本庫今日首次收錄，forks 2,340）
  - drama-skills：開源 AI 短劇／漫劇創作 skill 合集，涵蓋劇本、角色資產、分鏡、圖片／影片提示詞、審查，適配 Claude Code 與 Codex，MIT（2,272★，forks 497）
  - asd-ste100-skill：把 ASD-STE100 簡化技術英文規則轉為 Claude Code skill，用於改寫模糊的 agent 對話英文（2,241★，forks 125）
- **與既有模式的關係：** 補上「Skills 設計」既有代表技巧四個新取向的具名實作——學術寫作、設計/工程通用、創作全流程、語言精簡；前兩款星數異常高卻本庫今日首次收錄，推測受限於 GitHub Search 抓取覆蓋（推論）；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 四者 forks 占星數約 5%–22%，皆在 GitHub Search 抓取當日或前兩日內仍有 commit 或 issue 往來，非「異常高星數無佐證」情況。
- **來源：** GitHub Search；[nature-skills](https://github.com/Yuan1z0825/nature-skills)（44,559★）、[emilkowalski/skills](https://github.com/emilkowalski/skills)（41,183★）、[drama-skills](https://github.com/zenstory-ai/drama-skills)（2,272★）、[asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)（2,241★）
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### Ryze-AI-Adgent/open-seo-mcp-skills：免費 SEO MCP 伺服器＋開源 SEO／GEO Claude skills，串真實 GSC／GA4／廣告數據（2026-09-24）

- **主線：** —
- **核心模式：** 免費 SEO MCP 伺服器與開源 SEO／GEO Claude skills，可用真實 Google Search Console／GA4／廣告數據做關鍵字研究、排名追蹤、稽核與反向連結分析；GitHub Search 1,449 星。
- **與既有模式的關係：** 補上「Skills 設計」既有代表技巧 fire-your-seo-agency（2026-09-21）同屬 SEO／GEO 領域的另一實作，差異在本則直接串接 MCP 伺服器讀真實數據源，而非僅稽核既有排名；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（1,449★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊工具，尚無社群採用回饋數據）

#### Callous-0923/agent-study：36 章 AI Agent 全端課程，涵蓋 ReAct、Claude Code 逆向、MCP／A2A、RAG、DSPy（2026-09-24）

- **主線：** —
- **核心模式：** 36 章 AI Agent 全端課程，涵蓋 ReAct 迴圈、Claude Code 逆向工程、MCP／A2A 協議、RAG、DSPy 與生產可觀測性，全部附可執行 Python 檔；GitHub Search 500 星。
- **與既有模式的關係：** 屬課程／教材類資源盤點，非新做法或工具，與 2026-08-29 x1xhlol/system-prompts-and-models-of-ai-tools、2026-08-30 Shubhamsaboo/awesome-llm-apps 同屬彙整型參考資料，不進模式概覽表；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（500★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Callous-0923/agent-study)
- **成熟度：** ⏳ 新興（本庫首次收錄，單一團隊教材，尚無社群採用回饋數據）

#### leopard627/fire-your-seo-agency：Claude Code skill 自動稽核並優化 SEO／AEO／GEO／LLMO／NEO 排名（2026-09-21）

- **主線：** —
- **核心模式：** Claude Code skill，自動稽核並優化網站在 SEO／AEO／GEO／LLMO 與 Naver（NEO）排名，作者訴求取代每月數十萬韓元的代操服務；GitHub Search 504 星。
- **與既有模式的關係：** 補上「Skills 設計」類別一個「垂直領域稽核流程 skill 化」的代表技巧，與既有金融分析 skill 合輯（RKiding/Awesome-finance-skills，09-16 收錄）同屬把特定領域專業知識封裝成可複用 skill 的取向，本則鎖定 SEO／在地搜尋（Naver）稽核；非大型 codebase 特有痛點，主線填 —。
- **可信度註記：** 僅有 GitHub Search 星數（504★），無 forks／issues／近期 commit 佐證可查，未另行查證；作者自述訴求取代付費代操服務，屬產品行銷框架，機制本身（自動稽核＋優化）有 repo 佐證。
- **來源：** GitHub Search；[GitHub](https://github.com/leopard627/fire-your-seo-agency)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### Claude Code journal plugin：個人 `/journal` skill 包裝成公開 plugin，session 摘要自動整理進 Notion（2026-09-02）

- **主線：** —
- **核心模式：** 作者把個人使用的 `/journal` skill 包裝成公開 plugin，把每次 Claude Code session 的摘要依主題與星期自動整理進 Notion，一次 run 觸發三次 Notion API 呼叫
- **與既有模式的關係：** 補上「Skills 設計」類別「流程 skill 化」既有取向的一個具體案例——把個人日常記錄流程封裝成可安裝 skill 並公開分享，機制具體（三次 Notion API 呼叫、依主題/星期分類）；個人 session 摘要記錄與 codebase 規模無關，暫填 —。
- **可信度註記：** dev.to 條目依內容判斷（非讚數）：第一手描述具體機制與呼叫次數，非行銷稿或新聞轉述；13 讚
- **來源：** 「[Claude Code journal plugin: Notion session summaries at a glance](https://dev.to/cseeman/claude-code-journal-plugin-notion-session-summaries-at-a-glance-940)」— dev.to / #claudecode
- **成熟度：** ⏳ 新興（本庫首次收錄，個人專案公開化，尚無社群採用回饋數據）

#### Nanako0129/sepia：去 AI 化寫作風格修正 skill，相容 77 種以上 Agent Skills 相容 agent（2026-09-16）

- **主線：** —
- **核心模式：** 修正 AI 寫作風格使其較不像 AI 生成的 skill，宣稱相容 77 種以上支援 Agent Skills 標準的 agent，含 Claude Code、Codex、Grok Build、Antigravity 原生外掛。
- **與既有模式的關係：** 與既有「I-have-ADHD」（鎖定「Claudism」冗語，2026-09-08）同屬「消除 AI 產出的痕跡特徵」skill 化做法，本則聚焦寫作風格而非任務收尾語；非大型 codebase 特有痛點。
- **可信度註記：** 僅有 GitHub Search 星數（2,640★），無 forks／issues／近期 commit 佐證可查，未另行查證。
- **來源：** GitHub Search；[GitHub](https://github.com/Nanako0129/sepia)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### RKiding/Awesome-finance-skills：金融分析 Agent Skills 開源合輯（2026-09-16）

- **主線：** —
- **核心模式：** 彙整金融分析領域 Agent Skills 的開源合輯，屬策展型參考資源。
- **與既有模式的關係：** 與既有「Shubhamsaboo/awesome-llm-apps」「x1xhlol/system-prompts-and-models-of-ai-tools」同屬「靜態彙整供橫向參考」類別，本則範圍限定金融分析垂直領域；非大型 codebase 特有痛點。
- **可信度註記：** 僅有 GitHub Search 星數（3,011★），無 forks／issues／近期 commit 佐證可查，未另行查證；repo 2026-01-31 出生（存量盤點，本庫今日首次收錄）。
- **來源：** GitHub Search（存量盤點｜2026-01-31 出生、本庫今日首次收錄）；[GitHub](https://github.com/RKiding/Awesome-finance-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### rpamis/comet：把想法轉成可評測工作流程的 agent skill harness，本庫存量盤點今日首次收錄（2026-05-14 出生、3,023 星）（2026-09-12）

- **主線：** —
- **核心模式：** Agent skill harness，把想法轉成可評測（evaluated）的工作流程
- **與既有模式的關係：** 補上「Skills 設計」類別一種「skill 產出即附評測」取向的做法——既有代表技巧（知識框架化、流程 skill 化、免 git 雲端硬碟分享、hordev、drawio-skill）多聚焦封裝與分享，本則鎖定把評測綁進 skill 產出流程本身；通用 skill harness 與 codebase 規模無關，暫填 —。
- **可信度註記：** 本庫存量盤點通道首次收錄（已成名但本庫未報導過的 repo，2026-05-14 出生），未見 forks／issues／近期 commit 佐證，功能敘述為廠商自述
- **來源：** GitHub Search（存量盤點）；[GitHub](https://github.com/rpamis/comet)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### Agents365-ai/drawio-skill：把自然語言、程式碼、Terraform/K8s、SQL 與 OpenAPI 來源轉成可編輯、通過測試的 draw.io 架構圖（2026-09-11）

- **主線：** —
- **核心模式：** Agent Skill，將自然語言描述、程式碼、Terraform/K8s、SQL schema 與 OpenAPI 規格轉換為可編輯、經測試的 draw.io 架構圖；具備增量同步、多視角投影、drift diff（圖與程式碼歧異偵測）、CI 架構測試、手繪白板去光柵化、互動式 HTML/PPTX/Mermaid 匯出
- **與既有模式的關係：** 補上「Skills 設計」類別一種「架構圖生成與同步」取向的做法——既有代表技巧（知識框架化、流程 skill 化、免 git 雲端硬碟分享、hordev）聚焦知識與流程封裝，本則鎖定把多種程式碼／規格來源轉成會隨程式碼變動同步更新、且可通過 CI 測試的視覺化文件；架構圖生成對任何規模專案皆適用，非大型 codebase 特有痛點，暫填 —。
- **可信度註記：** 本庫存量盤點通道首次收錄（已成名但本庫未報導過的 repo），未見 forks／issues／近期 commit 佐證，功能清單為廠商自述
- **來源：** GitHub Search（存量盤點）；[GitHub](https://github.com/Agents365-ai/drawio-skill)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### heffrey/hordev：Claude Code skills 集合，設計理念是遇到不確定情境時直接動手嘗試建構、而非停下反覆詢問使用者（2026-09-09）

- **主線：** —
- **核心模式：** 一套 Claude Code skills 集合，設計理念是遇到不確定情境時優先直接動手嘗試建構，而非停下反覆向使用者確認
- **與既有模式的關係：** 補上「Skills 設計」類別一種「互動姿態」取向的做法——既有代表技巧多聚焦知識框架化與流程 skill 化，本則鎖定 skill 在不確定情境下的行為傾向（動手試 vs 反覆詢問）
- **可信度註記：** Hacker News（討論串連結存在，本則摘要未提供分數）；未見 forks／issues／近期 commit 佐證
- **來源：** 「Show HN: Hordev – Claude Code skills that build instead of asking questions」— Hacker News（[討論串](https://news.ycombinator.com/item?id=49630355)）；[GitHub](https://github.com/heffrey/hordev)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無社群採用回饋數據）

#### borski/travel-hacking-toolkit：旅遊比價 Skill 與 MCP server，跨 Claude／Codex／OpenCode（2026-09-09）

- **主線：** —
- **核心模式：** 提供可掛載的 skill 與 MCP server，協助搜尋現金、點數、里程與獎勵機票的省錢旅遊方案；相容 Claude、Codex、OpenCode；GitHub Search 累積 657 星
- **與既有模式的關係：** 延續本頁「Skill 生態多元化」既有趨勢（coding agent 透過 Skill／MCP 跨足非程式碼垂直領域），與影片、簡報、SSH 等既有領域案例同屬一取向，本則鎖定旅遊比價這個此前未見的垂直領域
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（657★）；[GitHub](https://github.com/borski/travel-hacking-toolkit)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### zenstory-ai/video-recap-skills：Claude Code Skill 把任意影片剪成中文口述影評，支援剪映匯出（2026-09-08）

- **主線：** —
- **核心模式：** Claude Code skill，將任意影片自動剪輯成中文口述影評（narration recap），並支援匯出至剪映格式；GitHub Search 累積 500 星
- **與既有模式的關係：** 補上「Skills 設計」類別一個「影片內容自動化生產」的具體案例，與 aqm857886159/Nomi（開源 AI 影片工作台，MCP 驅動）同屬「coding agent 跨足非程式碼影片生產」取向，差異在本則鎖定單一垂直任務（剪輯成口述影評並匯出剪映格式）而非通用影片工作台
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search（500★）；[GitHub](https://github.com/zenstory-ai/video-recap-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### plannotator/effective-html：Agent Skills 技能包，產出可用 HTML artifact、線框稿、互動原型、計畫與圖表（2026-09-07）

- **主線：** —
- **核心模式：** 一套 Agent Skills 技能包，協助生成可直接使用的 HTML artifact、線框稿、互動原型、計畫文件與圖表；GitHub Search 累積 3,023 星
- **與既有模式的關係：** 補上「Skills 設計」類別一種「產出物格式」導向的技能包——既有代表技巧多聚焦流程 skill 化與知識框架化，本則鎖定輸出格式本身（HTML artifact／線框稿／原型）
- **可信度註記：** 僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；存量盤點（2026-06-09 建立、本庫今日首次收錄）
- **來源：** GitHub Search（存量盤點，3,023★）；[GitHub](https://github.com/plannotator/effective-html)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### GitHub Search 同日湧現五款 Claude Code／Codex 週邊 Skill：影片分鏡、短劇製作、簡報生成、API 相容伺服器、SSH 工作流（2026-09-05）

- **主線：** —
- **核心模式：** 五款新 Skill／工具同日出現，涵蓋影片分鏡、短劇製作、簡報生成、API 相容伺服器、SSH 工作流五個不同用途，星數 500～7,524★ 不等，詳見下方「來源」逐一連結
- **五款簡介：** video-shotcraft（分鏡卡＋運鏡預覽影片模板）、shuohao-skills（短劇製作 skill 集合）、slides_maker（論文/文件轉可編輯 PPTX）、anti-api（多 agent 介面轉 API 相容伺服器）、ssh-skill（跨平台 SSH 工作流）
- **與既有模式的關係：** 延續本頁持續記錄的「Skill 生態多元化」趨勢（產出格式類：slides_maker、shuohao-skills；領域串接類：ssh-skill、anti-api）；非大型 codebase 特有痛點，暫不歸入 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** anti-api 與 ssh-skill 星數恰好同為 500，落在同一狹窄區間、缺乏佐證（同 08-12「GitHub 熱門清單」先例的星數叢集現象）；五款皆僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證
- **來源：** GitHub Search；[video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)（原文已失效）、[shuohao-skills](https://github.com/eternityspring/shuohao-skills)、[slides_maker](https://github.com/addsumtech/slides_maker)、[anti-api](https://github.com/silasxbt/anti-api)、[ssh-skill](https://github.com/badseal/ssh-skill)
- **成熟度：** ⏳ 新興（同日批次亮相，尚無社群採用回饋數據）

#### addyosmani/agent-skills：AI coding agent 生產級工程技能集合（2026-09-02）

- **主線：** —
- **核心模式：** AI coding agent 的生產級工程技能（skills）集合，作者為 Addy Osmani（Google Chrome DevRel 資深工程師）；GitHub Search 累積 9.2 萬星
- **與既有模式的關係：** 補上本頁「Skills 設計」類別一位具名資深工程師的策展案例——與既有 rsmdt/the-startup（套件化 subagent／commands 集合）、baoyu-design（官方工具 Skill 化移植）不同取向，本則訴求「生產級」（production-grade）品質標準的工程技能集合，非單一功能封裝；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（9.2 萬），無 forks／issues／近期 commit 佐證；repo 2026-02-15 出生（收錄時約 6.5 個月），累積速度偏快，惟作者具名（Addy Osmani，Google 資深工程師）且內容具體，依內容判斷收錄，星數速度不作為獨立驗證訊號
- **來源：** GitHub Search（9.2 萬★，存量盤點｜2026-02-15 出生、本庫今日首次收錄）；[GitHub](https://github.com/addyosmani/agent-skills)
- **成熟度：** ⏳ 新興（本庫首次收錄，尚無星數以外的社群採用回饋數據）

#### wanghuan9/skilldock：AI skill 管理桌面應用，安裝、整理、編輯、同步、更新 Skills／MCP servers／plugins（2026-09-02）

- **主線：** —
- **核心模式：** AI skill 管理桌面應用，支援 Claude Code、Cursor、Codex、Windsurf、Gemini CLI 等多種 AI coding 工具，可安裝、整理、編輯、同步、更新 Skills、MCP servers、plugins；GitHub Search 累積 503 星
- **與既有模式的關係：** 直接回應 [[topics/community-tech-discussions]]「🌊 持續關注中的長期議題」中「工具生態發現性問題」（🌙靜候，「Skills/MCP 散落各處，缺乏集中發現機制」）——本則是針對此痛點的具體桌面應用解法，把跨工具（5 種 AI coding 工具）的 Skills／MCP／plugins 管理集中到單一介面；[[topics/community-tech-discussions]] 該議題的狀態是否因此類工具出現而調整，留待後續追蹤
- **可信度註記：** 星數（503），惟資料僅含 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證，依內容具體程度（功能清單明確、跨工具支援清楚）判斷收錄
- **來源：** GitHub Search（503★）；[GitHub](https://github.com/wanghuan9/skilldock)
- **成熟度：** ⏳ 新興（今日首見，尚無社群採用回饋或量化效果數據）

#### dev.to：把 markdown 一鍵轉為多平台發布版本的 Claude Code Skill——dev.to／AWS Builder Center／Medium／LinkedIn（2026-09-02）

- **主線：** —
- **核心模式：** 一個 Claude Code skill，將一份 markdown 檔轉換為 dev.to、AWS Builder Center、Medium、LinkedIn 等多平台適配版本，發布前附檢查機制，並可透過各平台 API 自動發布
- **與既有模式的關係：** 為本頁「Skills 設計」類別補上「內容多平台發布」這個此前未見的具體應用領域——與既有 rsmdt/the-startup（開發流程指令集合）、baoyu-design（UI 原型產出）不同垂直領域，本則鎖定技術寫作者將單一文稿改寫並發布至多個內容平台的流程自動化
- **可信度註記：** 具體工具，附發布前檢查與 API 自動發布機制；單一來源，無跨平台佐證
- **來源：** 「Streamline Publishing with a Claude Code Skill」— dev.to `#claudecode`（9 讚）；[原文](https://dev.to/gde/streamline-publishing-with-a-claude-code-skill-1bdn)
- **成熟度：** ⏳ 新興（今日首見，單一工具，尚無社群採用回饋數據）

### 2026-08

#### Shubhamsaboo/awesome-llm-apps：彙整百餘款 AI Agent、Agent Skills 與 RAG 開源應用清單（2026-08-30）

- **主線：** —
- **核心模式：** 彙整 100 多款 AI Agent、Agent Skills 與 RAG 應用的開源清單，屬策展型參考資源；GitHub Search 累積 13.5 萬星
- **與既有模式的關係：** 與本頁既有「system prompt 版本追蹤」「system prompt 彙整檔案庫」（x1xhlol，2026-08-29）同屬「靜態彙整供橫向參考」類別，本則範圍更廣（涵蓋 Agent、Skills、RAG 三種應用型態），非單一格式的彙整
- **可信度註記：** 星數（13.5 萬），僅取得 GitHub Search 星數，無 forks／issues／近期 commit 佐證可查，未另行查證；repo 已存在逾 2 年（2024-04 出生），星數累積時間跨度合理，依內容具體程度（涵蓋範圍明確可查證）判斷收錄
- **來源：** GitHub Search（13.5 萬★，存量盤點｜2024-04-29 出生、本庫今日首次收錄）；[GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)
- **成熟度：** ✅ 廣泛採用（13.5 萬星且已存在逾 2 年，屬長期累積型參考資源）

#### JimLiu/baoyu-design：本機以 Agent Skill 執行 Claude Design，供 Cursor／Claude Code 產出自足式 HTML UI 原型（2026-08-29）

- **主線：** —
- **核心模式：** baoyu-design 讓使用者在本機以 Agent Skill 形式執行 Claude Design，供 Cursor、Claude Code 等工具產出自足式（self-contained）HTML 的 UI 原型、簡報與線框稿；官方建議搭配 Opus 4.8 使用；GitHub Search 累積 3,637 星
- **與既有模式的關係：** 為本頁「Skills 設計」類別補上「官方產品線的第三方 Skill 化封裝」這一取向——不同於既有的套件化 subagent／commands 集合（如 rsmdt/the-startup、ccteams），本則是把官方 [[entities/claude-design]] 工具的能力，以 Agent Skill 形式移植到官方介面以外的 Cursor、Claude Code 中執行，屬「官方功能→社群 Skill 化再散布」的具體案例；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（3,637），惟資料僅含 GitHub Search 星數，無 forks／issues／commit 佐證可查，未另行查證；依內容具體程度（功能明確、官方推薦模型清楚）判斷收錄
- **來源：** GitHub Search（3,637★，新發現）；[GitHub](https://github.com/JimLiu/baoyu-design)
- **成熟度：** ⏳ 新興（今日首見，尚無社群採用回饋或量化效果數據）

#### rsmdt/the-startup：「The Agentic Startup」風格 Claude Code 指令／Skills／Agent 集合（2026-08-25）

- **主線：** —
- **核心模式：** rsmdt/the-startup 是一套「The Agentic Startup」風格的 Claude Code commands、skills 與 agents 集合，GitHub Search 累積 507 顆星
- **與既有模式的關係：** 呼應本頁「Skills 設計」「Multi-agent 架構」類別既有套件化打包做法（如 ccteams 套件化 subagent 團隊配置），本則將 commands／skills／agents 三者一起打包為單一「新創風格」工具集，屬同一「把驗證過的配置打包成可安裝套件」取向的另一實例；非大型 codebase 特有痛點（通用型工具套件），暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **可信度註記：** 星數（507），惟資料僅含星數，無 forks／issues／commit 佐證可查，依內容具體程度判斷收錄
- **來源：** 「The Agentic Startup - A collection of Claude Code commands, skills, and agents.」— GitHub Search（507★）；[GitHub](https://github.com/rsmdt/the-startup)
- **成熟度：** ⏳ 新興（今日首見，單一開源專案，尚無社群採用回饋）

#### l3a0/claude-plugins：Claude Code Skill 用 OCR 從 Kindle Cloud Reader 復原被限制匯出的畫線筆記（2026-08-24）

- **主線：** —
- **核心模式：** 開發者分享用 Claude 打造的瀏覽器擴充功能／Claude Code skill，透過 OCR 從 Kindle Cloud Reader 擷取官方限制匯出的畫線筆記內容，繞過 Kindle 原生匯出功能的限制
- **與既有模式的關係：** 屬本頁既有「利用 OCR／視覺辨識繞過官方限制或擷取非結構化資料」取向的新實例，性質上與「pxpipe 把文字 context 圖片化」方向相反（此則是把畫面文字經 OCR 還原為可用文字）；HN 留言區有使用者分享自己也做過類似萃取工具（聚焦語言學習情境，擷取畫線詞彙的上下文），顯示此類需求有一定普遍性但均為個別實作，尚無共通工具；非大型 codebase 特有痛點，暫不歸入主線 [[topics/community-large-codebase-workflow]] 四條主線
- **來源：** 「A Claude Code skill that recovers export-blocked Kindle highlights」— Hacker News（score 45）；[GitHub](https://github.com/l3a0/claude-plugins)
- **成熟度：** ⏳ 新興（單一開發者分享，留言區有相似獨立實作經驗佐證共鳴，惟均為第一手心得，尚無工具化／套件化的公開複用版本）

#### GitHub 熱門清單同日聚集六款工具，五款星數集中於狹窄區間、缺乏佐證（2026-08-12）

- **主線：** —
- **核心模式：** GitHub Search 熱門清單今日同批帶出六款鎖定 Claude Code／Codex 等 coding agent 生態的工具：Waishnav/devspace（宣稱可把 ChatGPT 網頁介面變成類 Codex／把 Claude Web 變成 Claude Code 的體驗）、tzachbon/smart-ralph（結合 Ralph Wiggum loop 與結構化規格流程的 Claude Code plugin，主打規格驅動開發與智慧壓縮 compaction）、gglucass/headroom-desktop（macOS 桌面工具 Headroom，宣稱可將 Claude Code 與 Codex 的 token 成本削減約 50%）、aisa-group/PostTrainBench（評測 CLI agent 能否在單張 H100 GPU 上於 10 小時內完成基礎模型後訓練的基準）、ZeroPointRepo/youtube-skills（供 AI agent 使用的 YouTube 字幕擷取 skill，相容 OpenClaw、Hermes-Agent、Claude Code、Cursor、Windsurf）、clawplays/ospec（規格驅動 agentic 工作流框架，「規劃—執行—驗證」可驗證目標迴圈，相容 Claude Code、Codex、Gemini、OpenCode）
- **與既有模式的關係：** smart-ralph、ospec 呼應「Skills 設計」／「架構邊界合約」既有 spec-driven 取向；headroom-desktop 補「Token / 成本優化」Mac 工具實作；devspace／PostTrainBench／youtube-skills 無直接對應，暫記觀察；六款皆非大型 codebase 特有痛點，暫不歸入主線
- **主線：** —
- **星數真實性（2026-08-13 查證，GitHub API）：** devspace 3,675 星／forks 399（10.9%）／open issues 55／最後 push 08-13——佐證充分；smart-ralph 510 星／forks 46（9.0%）／issues 11／push 07-23；headroom-desktop 508 星／forks 52（10.2%）／issues 3／push 08-12；PostTrainBench 511 星／forks 58（11.3%）／issues 21／push 08-05；youtube-skills 506 星／forks 54（10.7%）／issues 2／push 08-12——五者 forks 比例與 issue 往來皆達防刷佐證基準，判斷非刷星；ospec 502 星／forks 30（6.0%，略低於基準）／issues 0／push 07-29，僅近期有實質 commit 一項佐證，刷星可能性無法完全排除，成熟度維持 ⏳
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）
- **成熟度：** ⚡ 活躍（devspace／smart-ralph／headroom-desktop／PostTrainBench／youtube-skills 星數已查證非刷星；ospec 佐證較弱，實際採用情形仍待觀察）

#### spec-driven 工作流工具批次亮相：ospec／smart-ralph／devspace／headroom-desktop 同日湧現（2026-08-11）

- **主線：** —
- **核心模式：** GitHub Search 今日同批出現四款鎖定 spec-driven／agentic 工作流的工具：clawplays/ospec（503 星，「規劃—執行—驗證」可驗證目標迴圈，相容 Claude Code、Codex、Gemini、OpenCode）、tzachbon/smart-ralph（505 星，結合 Ralph Wiggum loop 與結構化規格流程的 Claude Code plugin）、Waishnav/devspace（3,645 星，宣稱可把 ChatGPT 網頁介面／Claude Web 轉換成類 CLI agent 的體驗）、gglucass/headroom-desktop（502 星，macOS 桌面工具，宣稱可將 Claude Code／Codex 的 token 成本削減約 50%，機制未見說明）
- **與既有模式的關係：** ospec、smart-ralph 呼應「Skills 設計」／「架構邊界合約」既有 spec-driven 取向；headroom-desktop 補「Token / 成本優化」既有做法；四款隔日（08-12）以更高星數再現，持續發酵；非大型 codebase 特有痛點，暫不歸入主線
- **星數與聲稱真實性（2026-08-13 查證）：** 四款工具星數已於次日節點（見上方 2026-08-12 節點）查得 forks／issues／近期 commit 數據，devspace／smart-ralph／headroom-desktop 佐證充分，ospec 佐證較弱；headroom-desktop 削減機制已查證：本機執行的壓縮 pipeline，攔截 prompt 後移除 tool output／log／樣板文字等雜訊再送出，JSON／log 類項目可壓縮約 50%，但純文字使用者訊息不壓縮，實測整體 session 平均省約 15–25% token（非全面 50%）——[GitHub](https://github.com/gglucass/headroom-desktop)、[extraheadroom.com FAQ](https://extraheadroom.com/faq)（2026-08-13 查證）
- **來源：** GitHub Search（今日日報「⭐ 重點話題」已收錄）
- **成熟度：** ⚡ 活躍（星數佐證與 headroom 削減機制已查證屬實，惟整體省幅低於宣傳的 50%）

#### 把 Claude Code 工作區依情境資料夾組織：任務與交付物分離、重複工作沉澱為 skills（2026-08-11）

- **主線：** —
- **核心模式：** 文章分享一套將 Claude Code 工作區整理成情境資料夾（context folders）的實務做法，把任務本身與交付物（deliverables）分離存放，並把重複出現的工作流程沉澱為可複用的 skills，聚焦「產品工作（product work）」情境（非純程式碼開發）下如何組織 Claude Code 的日常使用方式
- **與既有模式的關係：** 呼應本頁「Skills 設計」類別既有「流程 skill 化」共識——既有節點多聚焦工程／程式碼場景，本篇補上「情境資料夾」「任務與交付物分離」這類尚未見於既有節點的組織技巧，並將適用範圍延伸至非純工程的產品工作場景；屬個人工作區整理習慣，非大型 codebase 多 agent 協作痛點，暫不歸入主線
- **來源：** 「How to organize Claude Code for product work」— Hacker News（score 35）
- **成熟度：** ⏳ 新興（今日首見，單一作者實務分享，尚無其他來源複現或延伸應用）

#### 把維基百科「Signs of AI writing」頁改寫成 Claude 自訂指示，宣稱可通過人工判讀（2026-08-11）

- **主線：** —
- **核心模式：** 使用者將維基百科「AI 寫作特徵」（Signs of AI writing）頁面內容改寫成 Claude Code 自訂指示（如 CLAUDE.md／system prompt 片段），宣稱經實測可讓輸出通過人工判讀、不易被辨識為 AI 生成
- **與既有模式的關係：** 與本頁 2026-07-01「Claude Code 隱寫術：同形字符隱寫元資料的信任危機」（見 [[topics/community-tech-discussions]]）及當日社群對隱形浮水印政策的反彈（見同頁 2026-08-11 節點）同屬「AI 輸出可辨識性」這個議題軸線的對立面實作——前者關注 Claude 輸出被動加註可辨識標記，本篇則是使用者主動要求 Claude 主動規避人類/工具辨識 AI 寫作的痕跡；工具與作者身分已查證：即開源 Claude 外掛「Humanizer」，由 Siqi Chen 開發，直接取用 Wikipedia WikiProject AI Cleanup 志工彙整的 24 條 AI 寫作特徵清單餵給 Claude 作為規避依據——[Nieman Journalism Lab](https://www.niemanlab.org/reading/a-new-plugin-uses-wikipedias-ai-spotting-guide-to-make-ai-writing-sound-more-human/)、[Slashdot](https://news.slashdot.org/story/26/01/22/015250/wikipedias-guide-to-spotting-ai-is-now-being-used-to-hide-ai) 等多方媒體已獨立報導此現象（2026-08-13 查證）；惟「經實測可通過人工判讀」一句仍為作者自陳，各報導均未見具體測試方法與樣本數第三方驗證
- **來源：** Reddit r/ClaudeCode（0 留言，無「週熱門」標記，score 不可信；單一貼文，具體技術操作但成效聲稱未經驗證，依內容判斷收錄；屬輸出可辨識性議題，非大型 codebase 協作痛點，暫不歸入主線）
- **成熟度：** ⏳ 新興（今日首見，單一使用者聲稱，成效未經第三方驗證）

#### Skill 不觸發的根因：session 啟動只索引 name+description，本體不預先載入（2026-08-04）

- **主線：** —
- **核心模式：** 作者說明 Claude Code 在 session 啟動時只掃描 skill 目錄，把每個 skill 的 name 與 YAML frontmatter 的 description 建成索引並注入 system prompt；SKILL.md 完整內容並不會預先載入，只有在 Claude 判斷 description 與使用者提示夠接近時才會載入——因此 description 才是實際的「觸發器」而非文件說明，寫得太籠統（如「helps with code quality」）永遠不會被真實提示語句匹配到
- **與既有模式的關係：** 補充本頁「Skills 設計」類別既有「description 自動觸發」機制的根因層說明——既有記錄多聚焦如何封裝內容為 skill，本篇解釋觸發失效的具體機制與如何寫出可被匹配的 description
- **來源：** 「Claude Code Skill Not Triggering? Here Are the 5 Actual Causes」— dev.to / dev_encyclopedia（依 dev.to 內容判斷原則收錄：具體揭露 skill 索引/觸發機制的第一手技術說明；0 讚不作為排除理由；屬單一工具機制說明，非大型 codebase 協作痛點，暫不歸入主線）
- **成熟度：** ⚡ 活躍（補充既有 Skills 設計最佳實踐的觸發機制細節）

### 2026-07

#### Claude Code Skills 清單字元預算機制：description 超額會讓既有 skill 悄悄失效（2026-07-28）

- **主線：** —
- **核心模式：** 拆解 Claude Code skills 清單載入的字元預算機制：單一 skill 的 description + when_to_use 合計上限 1,536 字元；整體 skills 清單的字元預算則依 context window 的 1% 計算——新增 skill 數量一多，既有 skill 可能悄悄被排出清單、不再被模型觸發使用，且過程中不會出現任何錯誤訊息
- **與既有模式的關係：** 補充本頁「Skills 設計」類別既有「description 自動觸發」機制的邊界條件：過去記錄的是「怎麼設計 skill 讓它被觸發」，本篇補上「觸發預算有硬上限、超額會靜默失效」這項使用者需知曉的限制，屬機制補完而非全新類別
- **來源：** 「Too many Claude Code skills? How the listing budget decides which descriptions Claude sees」— dev.to / rulestack（依 dev.to 內容判斷原則收錄：第一手技術實作拆解，非行銷/SEO 稿；讚數 2 不作為判斷依據）
- **成熟度：** ⚡ 活躍（既有 Skills 設計類別的機制補完）

#### nb2lite-skill-claude：以 Gemini Interactions API 打造有狀態圖片編輯 Claude Code Skill（2026-07-22）

- **主線：** —
- **核心模式：** 作者將 Google gemini-3.1-flash-lite-image 封裝為 Claude Code Skill 與 MCP server（nb2lite-skill-claude），支援多輪、有狀態的圖片編輯（版本追蹤與迭代修改，而非每次重新生成獨立圖片），並提供安裝指南與 dogfood 封面圖範例
- **與既有模式的關係：** 延伸「Skills 設計」與「模型使用策略」類別中「跨模態內容生成分工（InstantVideos）」的既有做法——不同於單次生成或單向 pipeline，此技巧強調「有狀態」的多輪編輯迴圈，補上 Skills 生態中「圖像類多輪任務狀態管理」的具體實作案例
- **來源：** 「Teaching Claude Code to Paint: A Stateful Image-Editing Skill Built on Gemini's Interactions API and MCP」— dev.to / #claudecode（3 讚；依規則以第一手實作內容判斷，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一開發者第一手實作，尚待社群採用回饋）

#### tpu-management：讓 Gemma 4 在 Cloud TPU 上運行的 Claude Code Skill（2026-07-22）

- **主線：** —
- **核心模式：** 作者釋出 Claude Code skill 搭配 MCP server 組合，可一鍵佈建 Google Cloud TPU、以 vLLM 服務 Gemma 4 模型、執行 benchmark，並在完成後自動拆除雲端資源，將原本繁瑣的 TPU 基礎設施佈建/拆除流程封裝為 Claude Code 可呼叫的 skill
- **與既有模式的關係：** 屬「Skills 設計」類別新型態——既有 Skills 案例多聚焦知識框架化或流程封裝，本篇將其延伸至「雲端基礎設施生命週期管理」（佈建→服務→測試→拆除全流程自動化）；與「Agent 預算控制」類別（AgentWatch）同屬降低雲端資源浪費風險的思路，但聚焦點是基礎設施自動拆除而非請求層費用攔截
- **來源：** 「tpu-management: a Claude Code skill for running Gemma 4 on Cloud TPUs」— dev.to（7 讚；依 dev.to 收錄規則以內容判斷，屬第一手實作記錄，非讚數）
- **成熟度：** ⏳ 新興（今日首見，單一作者實作記錄，尚無其他來源複現）

#### Sx 2.0：透過 Dropbox / Google Drive / iCloud 免 git 分享 Claude/Codex Skill（2026-07-14）

- **主線：** —
- **核心模式：** Sx 2.0 讓非技術團隊透過既有雲端硬碟（Dropbox、Google Drive、iCloud 等）分享 Claude/Codex 的 skill vault，不需依賴 git 版控知識；2.0 版新增 Mac/Windows/Linux 原生 app 與 Skill Evals 擴充系統，vault 格式重構為可直接作為 Claude 或 Codex plugin 使用
- **與既有模式的關係：** 屬「Skills 設計模式」類別下新的**分享／分發**取向，與既有 ccteams（npm 套件化 subagent 團隊，2026-07-11）同屬「降低 skill/subagent 配置重複勞動」思路，差異在於 ccteams 面向技術團隊（npm 生態），Sx 2.0 面向非技術團隊（免 git、雲端硬碟同步）
- **來源：** 「Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder」— Hacker News（score 39）
- **成熟度：** ⚡ 活躍（達 HN，2.0 版已有既有使用者基礎，但採用規模不明）

#### Skill Linter 對 52k-Star Repo 的 84/100 診斷案例：Skill 品質共通模式（2026-07-12）

- **主線：** —
- **核心模式：** 作者自製 skill linter，對一個 52k star 高星 repo 中 24 個 skills 逐一檢測，量化出 84/100 品質分數，並歸納出多個 skill 撰寫的共通可修正模式（如缺乏明確邊界、指令模糊等）
- **與既有模式的關係：** 呼應既有「Caliper：pass@k 指標的 Skill 可靠性測試方法」（2026-06-29），同屬「量化評估 skill 品質」思路的新工具，此案例聚焦靜態規則檢查（linter）而非執行時測試
- **來源：** 「I Pointed a Skill Linter at a 52k-Star Repo. Here Is What 84/100 Looks Like.」— dev.to（作者 sayed_ali_alkamel，原文發布 06-13）
- **成熟度：** ⏳ 新興（單一作者工具與案例，尚無其他來源複現）

#### 用 Claude Code Skill 在 Reddit/LinkedIn 找潛在客戶而非同業（2026-07-12）

- **主線：** —
- **核心模式：** 作者建置自動搜尋潛在客戶的 Claude Code skill，早期版本曾誤抓同業競品作為目標，記錄調整篩選邏輯排除同業、聚焦真實潛在客戶的過程
- **與既有模式的關係：** 新的應用領域案例——「Skill 設計模式」類別過去多聚焦開發流程本身，此案例將 skill 用於銷售/業務開發場景，補充 skill 應用場景多樣性的佐證
- **來源：** 「I built a Claude Code skill that finds customers, not competitors, on Reddit & LinkedIn」— dev.to（作者 newan2001，原文發布 06-19）
- **成熟度：** ⏳ 新興（單一作者工具，尚無採用數據）

