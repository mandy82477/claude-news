# Wiki 目錄

**角色：** 地圖——讀一次就知道該去哪頁（哲學見 `wiki/CLAUDE.md`「資訊架構哲學」）
**收：** 慢變的路由事實——頁面存在、領域、狀態、一句鉤子
**不收：** 快變事實（日期／熱度／近況→頁面標頭，盤點用 Grep）；異動紀錄（→ [[log]]）；每日新聞（→ `news/`）
**讀法：** 整讀（本檔的存在意義就是便宜的一次讀）；查詢分流見 `wiki/CLAUDE.md`「搜尋策略」

**最後更新：** 2026-09-26

---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（🗓️ 週更）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每日更新）
- [[feature-radar-archive-2026-05]] — 2026-05 功能詳細條目封存

---

## 💻 開發實務入口

只放**答「怎麼做」**的頁面（接手 repo 該怎麼設定、卡住了先裝什麼、大 repo 怎麼並行、agent 該用哪種形態跑）；選什麼、出事了、要花多少的頁在各自領域的分頁下；產品動態與事件追蹤住各自的頁，整理後沉澱到這幾頁。工具的判斷（該裝哪個、證據多強）只在社群工具目錄，每週整理；各類工具現在誰大、誰在漲看「社群工具規模榜」。

| 我想…… | 去哪 |
|---|---|
| 接手／新建一個 repo，**官方**建議先做哪些設定（CLAUDE.md、LSP、探索） | [[topics/coding-workflow-guide]] 第 1、2a 段 |
| 我卡住了（帳單爆、額度快用完想被提醒、context 撐爆、agent 互踩、它說做完了沒做、agent 讀不懂大 repo、CLAUDE.md 寫了它不聽、被單一供應商綁住……），**社群首選**是哪個 | [[topics/community-tech-tools]]「我卡在這裡」決策表 |
| 我關心的某類工具，現在誰最大、本週誰在竄升（七日星數差，每日快照） | [[topics/skill-interest-watch]] 各類別（按開發流程段） |
| 它說做完了，我怎麼知道是真的——**官方**做法（要證據、`/goal`、Stop hook） | [[topics/coding-workflow-guide]] 第 9 段 |
| 我想讓 agent 自己跑幾小時／過夜，該用哪個（`/goal`、subagent、dynamic workflows、agent teams、agent view、Managed Agents、Agent SDK） | [[topics/anthropic-agent-stack]]「你該用哪個」 |
| code review 該用哪個入口、怎麼審得起（本庫刻意不推薦單一社群工具，官方六個入口＋明價） | [[topics/coding-workflow-guide]] 第 5 段 |
| 大型 codebase 的做法主線（並行／context／記憶／把關） | [[topics/community-large-codebase-workflow]] |

---

## Entities（實體頁）

| 頁面 | 類型 | 領域 | 狀態 | 摘要 |
|------|------|------|------|------|
| [[entities/sonnet-5]] | model | 🤖 模型 | active | Claude Sonnet 5：Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 標準價（08-10 永久化），agentic 效能接近 Opus 4.8 |
| [[entities/claude-science]] | product | 🛠️ 工具/功能 | active | Claude Science：科學家專用 AI 工作台，整合研究工具套件、可稽核 artifact、彈性運算資源；Anthropic 宣布自行開發藥物 |
| [[entities/claude-code]] | product | 🛠️ 工具/功能 | active | Claude Code CLI 主頁：功能、已知問題、社群工具　↳ 子故事：[[entities/claude-code-archive]] |
| [[entities/opus-5-5]] | model | 🤖 模型 | active | Claude Opus 5.5：2026-09-22 發布的現行 Opus，$4/$20、快取讀取 $0.20，官方稱多數工作追平 Fable 5.1；v2.1.280 起為 Claude Code 預設模型 |
| [[entities/opus-5]] | model | 🤖 模型 | active（Legacy） | Claude Opus 5：2026-09-22 起官方改列 Legacy 仍可用，$5/$25；預設 Opus 已由 [[entities/opus-5-5]] 接手 |
| [[entities/opus-4-8]] | model | 🤖 模型 | active（Legacy） | Opus 4.8：SWE-bench Pro 69.2%、1M context、Fast Mode 1/3 費用；官方已列 Legacy、退役不早於 2027-05-28，建議遷移至 [[entities/opus-5]]　↳ 子故事：[[entities/opus-4-8-archive]] |
| [[entities/opus-4-7]] | model | 🤖 模型 | active（已被取代）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 💼 商業 | active | 訂閱方案、牌價與乘數、計費規則現況；09-14 起週配額換軌、還在發生的計費事故　↳ 子故事：[[entities/pricing-archive]] |
| [[entities/mythos]] | model | 🤖 模型 | active（已解禁） | 高能力安全模型；2026-06-30 出口管制解除，07-01 全球恢復存取；僅限授權機構/安全研究用途，非一般消費市場　↳ 子故事：[[entities/mythos-archive]] |
| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/claude-design]] | feature | 🛠️ 工具/功能 | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | 🛠️ 工具/功能 | beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境　↳ 子故事：[[entities/claude-security-archive]] |
| [[entities/openclaw]] | product | 💼 商業 | active | 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費　↳ 子故事：[[entities/openclaw-archive]] |
| [[entities/google-investment]] | event | 💼 商業 | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構　↳ 子故事：[[entities/google-investment-archive]] |
| [[entities/bernanke]] | person | 👤 人物 | active | 前聯準會主席，2026-07-09 加入 Anthropic 長期利益信託（Long-Term Benefit Trust）董事會 |
| [[entities/boris-cherny]] | person | 👤 人物 | active | Claude Code 創始人，「Loops 是未來」設計哲學；07-17 稱同時執行數千個 Claude Code agent（出處已查實）　↳ 子故事：[[entities/boris-cherny-archive]] |
| [[entities/john-jumper]] | person | 👤 人物 | active | 諾貝爾化學獎得主（AlphaFold），2026-06-19 離開 Google DeepMind 加入 Anthropic（Reuters 確認）|
| [[entities/cat-wu]] | person | 👤 人物 | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |
| [[entities/andrej-karpathy]] | person | 👤 人物 | active | 近期加入 Anthropic，CLAUDE.md 四條規則、「最小必要 context」費用控管原則 |
| [[entities/fiona-fung]] | person | 👤 人物 | active | Anthropic 工程副總裁；「Claude Code 讓工程師更孤獨；coding 不再是瓶頸」論述（2026-06-22） |
| [[entities/dario-amodei]] | person | 👤 人物 | active | Anthropic CEO：政府監管立場、企業文化論述、Code with Claude 大會現場宣布速率政策　↳ 子故事：[[entities/dario-amodei-archive]] |
| [[entities/teresa-carlson]] | person | 👤 人物 | active（待核實）| 前 Microsoft、AWS 高管；2026-07-07 加入 Anthropic 主導公部門（public sector）業務；職稱已查證，到任日期官方仍未公開（FedScoop）|
| [[entities/kevin-buzzard]] | person | 👤 人物 | active | Imperial College London 數學教授、Xena Project 主持人，主持 EPSRC 資助的 FLT Lean 形式化計畫；2026-09-04 公開回應 Anthropic 搶先完成形式化（「Anthropic has beaten me to it」）|
| [[entities/opencode]] | product | 💼 商業 | active（快速成長）| Claude Code 主要開源替代品，157K 開發者分流，OpenCode-power-pack 移植官方 11 個 skills　↳ 子故事：[[entities/opencode-archive]] |
| [[entities/claude-tag]] | feature | 🛠️ 工具/功能 | active | Claude Tag：Slack-native AI 協作工具，可讀取頻道上下文、跨 session 記憶、主動完成任務；Anthropic 內部 65% 程式碼由其生成 |
| [[entities/claude-skills]] | feature | 🛠️ 工具/功能 | active | Claude Skills：官方 Skills 產品線與生態單一入口——六大控制層之一，官方小企業/教師技能包、平台支援、第三方移植動態；設計面歸 [[topics/community-tech-patterns]]　↳ 子故事：[[entities/claude-skills-archive]] |
| [[entities/cowork]] | product | 🛠️ 工具/功能 | active（09-17 起與聊天介面合併） | 與聊天介面合併為單一 Claude；同步推出 [[entities/claude-docs]]、[[entities/claude-slides]]（beta），先於 Pro／Max 開放 |
| [[entities/claude-docs]] | feature | 🛠️ 工具/功能 | beta | 官方文件工具，2026-09-17 隨 Cowork／Chat 合併同步推出，可直接在 Claude 對話中建立、編輯文件；先開放 Pro、Max 方案 |
| [[entities/claude-slides]] | feature | 🛠️ 工具/功能 | beta | 官方簡報工具，2026-09-17 隨 Cowork／Chat 合併同步推出，可直接展示或下載為 PowerPoint／PDF；先開放 Pro、Max 方案 |
| [[entities/fable-5]] | model | 🤖 模型 | active | 現行旗艦 5.1（09-01 GA）；5 轉 Legacy，退役不早於 2027-06-09；兩代同價；護欄擋什麼、被擋會不會知道　↳ 子故事：[[entities/fable-5-archive]] |
| [[entities/tom-blomfield]] | person | 👤 人物 | active| 前 Monzo 共同創辦人，2026-07-13 加入 Anthropic（2026-09-20 查證確認到任與職稱）|
| [[entities/claude-for-teachers]] | product | 🛠️ 工具/功能 | active | Anthropic 面向美國通過認證 K-12 教師的免費方案，開放進階 Claude 功能與教學技能庫，對接全美 50 州學術標準 |
| [[entities/tino-cuellar]] | person | 👤 人物 | active | Anthropic 首任 Chief Global Affairs Officer（2026-08-05 到任），前 Carnegie Endowment for International Peace 總裁、加州最高法院大法官 |
| [[entities/robert-mahari]] | person | 👤 人物 | active | Anthropic「Claude for Legal」負責人（2026-08-07 任命；哈佛／MIT JD-PhD、史丹佛 CodeX 副主任、Akiva AI 創辦人，職掌為法律垂直的 GTM，2026-09-13 查證）|
| [[entities/jensen-huang]] | person | 👤 人物 | active | Nvidia 執行長；2026-08-26 財報電話會議說對投資 OpenAI／Anthropic「唯一的後悔是投得不夠多、不夠早」（已查實）|
| [[entities/amir-salek]] | person | 👤 人物 | active | Google TPU 專案創辦人（2013–2022，經手前七代）；2026-08 加入 Anthropic compute 團隊，向 James Bradbury 匯報（Bloomberg 查證 2026-09-06）|
| [[entities/evan-hubinger]] | person | 👤 人物 | active | Anthropic 安全研究員；2026-09-09 公開估計 AI 十年內導致人類全滅機率逾 10%（BBC 具名報導） |
| [[entities/jack-clark]] | person | 👤 人物 | active | Anthropic 共同創辦人；2026-09-15 向 BBC 稱 AI「緊急關閉開關」未來或需強制、向 NPR 稱放緩開發是「集體行動難題」|
| [[entities/jacob-coxon]] | person | 👤 人物 | active（待核實）| 前 OpenAI／剛離職 Anthropic pretraining 研究員；2026-09-09 辭職聲明指控兩家公司「不負責任衝向自我改進超級智能」（HN 623 分；資歷已由具名媒體查證，官方未證實）|
| [[entities/joe-benton]] | person | 👤 人物 | active | 前 Anthropic 安全研究團隊負責人；2026-09-10 接受 NBC News 首次專訪，警告先進 AI 研究進展恐失控 |
| [[entities/josh-engels]] | person | 👤 人物 | active | 前 Google DeepMind AI 安全研究員；2026-09-10 接受 NBC News 首次專訪，稱「這裡面沒有大人在把關」|
| [[entities/simon-willison]] | person | 👤 人物 | active | 獨立開發者／部落客，全站引用最多的第一手觀點來源（114 次／15 頁）；多筆 Boris Cherny、Dario Amodei 聲明的原文轉引管道 |
| [[entities/mustafa-suleyman]] | person | 👤 人物 | active | Microsoft AI 執行長；2026-09-16 批評 Anthropic 對 Claude「類人化」論述有「災難性影響」風險，並抨擊其 AI 意識說法（Bloomberg／BBC／Axios）|
| [[entities/michael-burry]] | person | 👤 人物 | active | 知名放空交易員（《大賣空》原型人物）；2026-09-17 在 X 批評 OpenAI、Anthropic 等公司高層呼籲放慢 AI 發展是「自利」之詞 |
| [[entities/sridhar-vembu]] | person | 👤 人物 | active（單一來源） | Zoho 創辦人，2026-09-23 向 NDTV 稱 OpenAI、Anthropic「可以放慢腳步」（僅標題可用） |
| [[entities/joe-lonsdale]] | person | 👤 人物 | active（單一來源） | Anthropic 投資人；2026-09-25 向 Reuters 稱 AI 公司渲染風險是為了影響政策走向（僅標題可用） |

---

## Topics（進行中議題）

> Topics 頁面本身無「類型」欄位，故表格僅三欄（領域 / 狀態 / 摘要），為刻意設計差異（Entities 四欄含類型）。

| 頁面 | 領域 | 狀態 | 摘要 |
|------|------|------|------|
| [[topics/long-context-1m]] | 🛠️ 工具/功能 | monitoring | 1M context 的計費與控制權：加不加價看模型世代（舊世代 ×2 輸入）、Pro 預設開啟且關不掉、選定的 1M 變體會從選單消失　↳ 子故事：[[topics/long-context-1m-archive]] |
| [[topics/claude-code-experimental]] | 🛠️ 工具/功能 | ongoing | Claude Code 實驗功能追蹤：出貨 build 裡先出現、還沒公告的旗標，四階狀態機（出現→有人談→官方承認→出貨/移除），每階要證據；09-15 建頁，基線 2.1.272 |
| [[topics/model-comparison]] | 🤖 模型 | ongoing | 模型選型對照：「我該用哪個 Claude 模型、換一個實付差多少」單一入口——快速選型表、情境推薦、換代成本換算；跨家排名指向榜單頁 |
| [[topics/model-task-leaderboard]] | 🤖 模型 | ongoing | 🗓️ 週更 任務 × 跨家模型領先者快照：「做某類任務目前哪家最強」——18 類任務的活榜單每週速讀＋各榜評比方式索引；跨家排名的終點在這頁，Claude 家內選型見模型選型對照 |
| [[topics/anthropic-commitments]] | 🏛️ 政策/安全 | monitoring | 承諾兌現追蹤：「Anthropic 說過要做的事做了嗎」——官方承諾/拒絕建檔，狀態變化時每日更新 |
| [[topics/code-quality-decline]] | 🌐 社群 | ongoing | 「變笨了」三條線：04 月那次官方已結案，06 月起 token 異常與 Opus 5 品質觀感官方沒說法；先知道你釘不住你選的模型　↳ 子故事：[[topics/code-quality-decline-archive]] |
| [[topics/competitor-landscape]] | 💼 商業 | ongoing | Meta 三層訂閱打價格戰 + 中國陣營「免費夠用」+ 開源旗艦權重釋出，戰場從「誰更強」移到「誰更便宜」　↳ 子故事：[[topics/competitor-landscape-archive]] |
| [[topics/community-tech-tools]] | 🌐 社群 | ongoing | 🗓️ 週更：先查「我卡在這裡」症狀決策表拿首選，再看工具目錄的活躍度與採用狀態 |
| [[topics/skill-interest-watch]] | 🌐 社群 | ongoing | 🗓️ 每日快照 社群工具規模榜：各類工具在 GitHub 上現在誰最大、本週誰在漲；該裝哪個每類附一行連到社群工具目錄症狀列；機器產出，星數是規模不是品質 |
| [[topics/community-tech-patterns]] | 🌐 社群 | ongoing | 每種社群做法的原始證據與採用量，20 類（Multi-agent、Skills、CLAUDE.md、Hooks 四類已定案）；「該怎麼改設定」看 [[topics/community-pattern-trends]]　↳ 子故事：[[topics/community-tech-patterns-archive]] |
| [[topics/community-large-codebase-workflow]] | 🌐 社群 | ongoing | 🗓️ 週更 大型 codebase 規模化開發主線——每條線先給「現在的答案」，再列子問題表；每個做法的證據見 [[topics/community-tech-patterns]] |
| [[topics/community-pattern-trends]] | 🌐 社群 | ongoing | 🗓️ 週更 社群做法收斂成的九個方向：各自怎麼走到今天、你現有設計可以回頭檢查什麼；每種做法的原始證據與成熟度見 [[topics/community-tech-patterns]] |
| [[topics/community-tech-discussions]] | 🌐 社群 | ongoing | 社群觀念爭論盤點 8 場：5 場還在吵、3 場僵住（已吵出共識的另列一節），每場標最後一則證據的日期與官方說法　↳ 子故事：[[topics/community-tech-discussions-archive]] |
| [[topics/llm-wiki-pattern]] | 🌐 社群 | ongoing | Karpathy 式 LLM wiki 模式：三層＋三動作怎麼設計、外面八種公開實作各自最有辨識度的一招，以及本庫對照下來有什麼、缺什麼 |
| [[topics/safety-china-trust-dispute]] | 🏛️ 政策/安全 | monitoring | 中美 AI 工具信任對峙：代理偵測指控 → 企業禁用 → 官方後門警示 vs 07-10 否認。記到 07-11，之後見 [[topics/anthropic-government-policy]]　↳ 子故事：[[topics/safety-china-trust-dispute-archive]] |
| [[topics/ai-agent-safety]] | 🏛️ 政策/安全 | ongoing | AI agent 安全：Auto 模式非安全邊界，惡意 `.git` 跨廠可觸發程式碼執行　↳ 子故事：[[topics/ai-agent-safety-archive]] |
| [[topics/anthropic-government-policy]] | 🏛️ 政策/安全 | ongoing | 出口管制已解除；現有八條線在動，其中香港存取限制、輸出浮水印、高風險請求換 Opus 4.8 已改到你的 Claude　↳ 子故事：[[topics/anthropic-government-policy-archive]] |
| [[topics/official-community-gap]] | 🛠️ 工具/功能 | ongoing | 社群喊的痛，官方補了哪幾個、哪幾個還沒補、為什麼沒補　↳ 子故事：[[topics/official-community-gap-archive]] |
| [[topics/anthropic-agent-stack]] | 🛠️ 工具/功能 | ongoing | 官方 agent 積木總覽：八塊積木各自為什麼出、讓你多做出什麼、怎麼疊；選型表與六層架構收附錄　↳ 子故事：[[entities/managed-agents]]、[[entities/managed-agents-archive]] |
| [[topics/coding-workflow-guide]] | 🛠️ 工具/功能 | ongoing | 🗓️ 週更 程式開發實戰手冊：我現在在做這件事，該下哪個 skill、它會做什麼、有什麼坑——以流程階段為軸（官方技能不按開發領域切） |
| [[topics/enterprise-cost-management]] | 💼 商業 | monitoring | 企業規模採用 Claude 的成本結構挑戰：Uber/Microsoft 案例、缺失工具、因應策略；08-14 新增成本管控動態　↳ 子故事：[[topics/enterprise-cost-management-archive]] |
| [[topics/enterprise-tool-tracker]] | 💼 商業 | ongoing | 大型企業現在用哪套 AI 編碼工具、換過什麼；Alibaba 已禁用 Claude Code　↳ 子故事：[[topics/enterprise-tool-tracker-archive]] |
| [[topics/anthropic-business]] | 💼 商業 | ongoing | Anthropic 商業健康度：現在的數字、IPO 走到哪一格、合作會不會改到你的帳單；補貼倍數只有社群估算　↳ 子故事：[[topics/anthropic-business-archive]] |
| [[topics/market-signals]] | 💼 商業 | ongoing | 投資訊號判讀（每日）：先列你買得到的標的，再逐則照分析師六問判——新資訊嗎、動到哪個數字、誰有感、多可信、下一個催化劑、所以呢——兩週後結算催化劑出現了沒（教學型事件研究，非投資建議；事實在商業各頁，本頁只放觀點） |
| [[topics/market-lessons]] | 💼 商業 | ongoing | 投資判讀教材（週更）：判讀沉澱出的課程表（一課一列、押對了嗎）、未上市消息線各走到哪、IPO 流程六格與 S-1 先看五處 |
| [[topics/recursive-self-improvement]] | 🏛️ 政策/安全 | ongoing | AI 遞歸自我改進：官方《Risk Report August 2026》（08-14）首度就內部 AI R&D 加速幅度提供量化區間自評，並確認 Model 2 暫無釋出計畫　↳ 子故事：[[topics/recursive-self-improvement-archive]] |
| [[topics/ai-talent-flow]] | 💼 商業 | ongoing | AI 實驗室人才流動與對各公司影響：Google DeepMind 高層與核心研究員異動（事件 08-05，08-13 查證補記），Anthropic 主要承接　↳ 子故事：[[topics/ai-talent-flow-archive]] |
