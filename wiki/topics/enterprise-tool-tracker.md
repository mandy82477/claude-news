---
page: "topics/enterprise-tool-tracker"
kind: "topic"
status: "ongoing"
domain: "💼 商業"
last_updated: "2026-11-04"
last_news_update: "2026-11-03"
status_main: "ongoing"
days_since_news: 2
parent: null
children: "['topics/enterprise-tool-tracker-archive']"
page_role: "hub"
days_since_news_subtree: 2
inbound_links: 52
attribution_count: 51
attribution_last: "2026-11-03"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 大型企業 Claude 採用追蹤：誰在用、誰減用

哪些具名企業與機構在自己內部用 Claude（含 Claude Code）、用多大、誰在減用或退出、為什麼——一家一列。帳單怎麼控在 [[topics/enterprise-cost-management]]，這則客戶進出對營收怎麼判在 [[topics/market-signals-customers]]。

**狀態：** ongoing
**領域：** 💼 商業
**開始日期：** 2026-05-26
**最後更新：** 2026-11-04
**最後新聞更新：** 2026-11-03
**蒐集邊界：** 僅涵蓋 Claude 相關報導所帶出的具名企業與機構，是已見報者的彙整，非市場全貌。只收 Claude 的買方——員工在用，或自家產品呼叫 Claude；替客戶導入、轉賣或認證 Claude 的通路夥伴（Partner Network、系統整合商）在 [[topics/anthropic-partnerships-compute]]。

> **最新企業採用異動**（2026-11-03）
> 高盛全面禁止行員使用 Claude Code 與 GitHub（僅標題，範圍與生效時間未見），與 08-20 香港被切斷是不同案例（[PYMNTS](https://news.google.com/rss/articles/CBMiswFBVV95cUxNclZrZGl6M0NLSFpRNXhZMEItQmhQR1QyUEpudk5WeU02eXF4MjAzUS15VlllV0ZyYXZkQmdPM1BZZzZac2VTQTJvekM3VTYtOEx1aXBudmpVakw5RXNXYWExc05Od1FOdzY0T01sZkNCOU80X3lVOXJfVXFJR0FjdXVmTUJVTHgzSGFJWEFLMHRTQmRPaU5RWUdzOHFBWTJvbE5sZFp6NmVCbC1JN2RQS2Npaw?oc=5)）

## 摘要

表上 48 家具名企業與機構：✅ 使用中 35、⚠️ 縮減或限縮 7（含 Replit 有爭議）、❌ 退出或被切斷 3、🔄 切換 1、❓ 未確認 2（2026-11-04 數表，一家一列）。見報的具名導入仍以新增為主；減用的理由集中在成本、自家有競品與資料外洩疑慮。

**退出與減用理由分兩類：** 客戶自己選的是成本（Uber、Lindy、Microsoft）、安全或資料疑慮（Alibaba；Nvidia、Palantir、Booz Allen）、自家有競品（Meta、Microsoft，10-05 已查證），Goldman 11-02 禁令的理由未見報導；別人劃線的是出口管制（JPMorgan 香港，06-18，06-30 解除）、區域存取（Goldman、OKX 香港，08-20，Anthropic 區域存取政策，與出口管制無關，見 ⟨Q-03⟩）、Pentagon 黑名單，詳見 [[topics/anthropic-government-policy]]。

---

## 企業工具使用現況

> 狀態＝這家現在對 Claude 的整體狀態：✅ 使用中 ／ ⚠️ 縮減中或限縮 ／ 🔄 切換中 ／ ❌ 已退出或被切斷（備註寫誰劃的線） ／ ❓ 未確認
> 事件日期：狀態實際生效的時間點（❌ 為退出日、🔄 為切換日、✅ 為採用日）
> 確認日期：最近一則報導的日期（括號內為首見日）；一家公司一列，同一家有新消息就更新同一列，依確認日期新者在上

| 企業 | 規模 | AI 編碼工具 | 狀態 | 事件日期 | 備註 | 確認日期 |
|------|------|-----------|------|---------|------|---------|
| Goldman Sachs | 頂尖 | Claude Code；Claude AI（香港） | ❌ | — | 11-02 報導全面禁止行員用 Claude Code 與 GitHub，範圍與生效時間未見；08-20 香港先被切斷，屬 Anthropic 區域存取政策（⟨Q-03⟩） | 2026-11-02 |
| Palantir | 大型 | Claude | ⚠️ | — | 09-14 報導因資料外洩疑慮限縮內部使用，要求不可撤銷的零資料保留保證才上架；11-01 CTO 稱不後悔合作 | 2026-11-01 |
| Epic Games | 頂尖（遊戲引擎大廠，Unreal Engine 開發商） | Claude Code ＋ Codex | ✅ | 2026-10-12 | TweakTown（10-29）稱已用 Claude Code／Codex 改善除錯 Unreal Engine；10-12 官方釋出 skills 供外掛，527 星，細節見時序 | 2026-10-29（首見 2026-10-12） |
| Charles Schwab | 頂尖（美國券商） | Claude for Financial Advisors | ✅ | 2026-09-14 | 把 Claude 接進給獨立投資顧問（RIA）的平台；10-24 追加 20 席採購下限，見 [[entities/pricing]] | 2026-10-24 |
| Replit | 大型（AI 編碼/應用開發平台） | Claude（API 整合） | ⚠️ 有爭議 | 2026-10-16 | 執行長稱已不合作，匿名知情人士否認，雙方無正式聲明；細節見時序 | 2026-10-17 |
| Accenture | 頂尖（全球諮詢巨頭，Anthropic「內嵌評估者」夥伴） | Claude（員工一般使用，不限特定工具） | ✅ | — | 將員工可由公司報銷的 Claude 支出上限設在每月 $29，此前已有員工單月花費高達 $1,000；多家媒體同日跟進 | 2026-10-16 |
| 美國參議院 | 政府（聯邦立法機關） | Claude（幕僚辦公室一般使用） | ❓ | — | Bloomberg Government 報導參議院準備讓幕僚開始使用 Claude，尚未確認已上線，資料存取規範未見報導 | 2026-10-15 |
| Rubrik（NYSE: RBRK） | 大型 | Claude Code；Claude Mythos 5 | ✅ | 2026-06-09 | 06-09 Agent Cloud for Claude Code、06-30 Claude Code 安全層、09-15 Code Guardian 用 Mythos 5 做程式碼紅隊測試 | 2026-10-09 |
| Meta | 頂尖 | Claude Code | ⚠️ | — | 限制使用屬實（⟨Q-02⟩）；10-05 報導 Claude Code 使用者約 6 萬→約 3 萬，已查證 2026-10-07，細節見時序 | 2026-10-05（首見 2026-07-06）|
| Microsoft | 頂尖 | Claude Code → GitHub Copilot；Claude（內部整體） | ⚠️ | 2026-06-21 | 06-21 起停用 Claude Code、改推 Copilot；10-05 內部 Claude 支出砍逾三分之一（已查證 2026-10-07），合約未取消 | 2026-10-05 |
| Barclays | 頂尖（英國環球銀行） | Claude Code；Claude（營運） | ✅ | — | 官方 10-01：預期 2026 年底半數開發者用 Claude Code、2027 年擴及多數工程師（目標，非已達成）；郵件分流約 12 萬封／日、1.6 萬人用於知識檢索 | 2026-10-01 |
| JPMorgan Chase | 頂尖 | Claude Code（美國本部）；Claude API（香港分行） | ✅ | — | 美國本部 8 月約 8,000 人持授權，部分工程師每月 $2,000 上限；香港分行 06-18 因出口管制停用，06-30 管制解除後是否恢復未見 | 2026-09-17 |
| Novo Nordisk | 頂尖（丹麥藥廠） | Claude | ✅ | — | 用 Claude 加速藥物研發與醫學研究，合約範疇與費用未見（Reuters 等 4 家） | 2026-09-16 |
| Google | 頂尖 | Claude（不限版本，媒體未指明是否限 Claude Code） | ✅ | 2026-09-15 | Business Insider 報導 Google 已開放全體工程師使用 Anthropic 的 Claude；具體工具範疇、部門、上線時程均未見報導細節 | 2026-09-15 |
| Nvidia | 頂尖 | Claude | ⚠️ | — | 09-14 The Information（經多家轉述）：因資料外洩疑慮限於較不敏感任務、內部改用自家 Nemotron；官方未回應個案 | 2026-09-14 |
| Booz Allen | 大型 | Claude | ⚠️ | — | 同批報導：禁止員工以其商用模型處理專有資安工作；官方未回應個案 | 2026-09-14 |
| Orion | 大型（RIA 財富管理平台） | Claude for Financial Advisors | ✅ | 2026-09-14 | 與 Schwab 同日宣布把 Claude 接進 RIA 平台，費率未見 | 2026-09-14 |
| T. Rowe Price | 大型（全球資產管理公司） | Claude API + Claude Code | ✅ | — | 官方新聞稿宣布擴大在投資流程中使用 Claude 與 Claude Code；具體整合範疇、涵蓋部門未見報導細節 | 2026-09-10 |
| PicPay | 大型（巴西金融科技公司） | Claude API（對話式 AI 金融服務） | ✅ | 2026-09-04 | 導入 Claude 處理銀行客服詢問，09-07 FF News 稱擴大為對話式 AI 金融服務；拉美市場首見具名金融科技採用案例，具體整合範疇未見報導 | 2026-09-07（首見 2026-09-04）|
| Shopify | 頂尖 | Claude Code | ❓ | — | 執行長 Tobi Lütke 揚言封殺；Anthropic 早已關閉相關功能請求；未見官方確認執行，暫標未確認（細節見時序） | 2026-08-26 |
| ReliaQuest | 大型（資安廠商） | Claude API（AI 驅動資安平台整合）| ✅ | — | 深化與 Anthropic 技術整合，作為去 SIEM 化資安策略一環；具體整合範疇、合作規模未見報導（細節見時序） | 2026-08-22 |
| OKX | 大型（加密貨幣交易平台） | Claude AI | ❌ | — | 與高盛同批：香港被切斷 Claude AI 存取權限，屬 Anthropic 區域存取政策（⟨Q-03⟩），詳見 [[topics/anthropic-government-policy]] | 2026-08-20 |
| Payward（Kraken 母公司） | 大型（全球加密貨幣交易平台母公司） | Claude Mythos 5 | ✅ | — | 採用僅限授權機構存取的 Claude Mythos 5，強化全球加密基礎設施；規模未見細節 | 2026-08-19 |
| Duke University | 大型（高等教育機構） | Claude（pay-as-you-go 訂閱方案） | ✅ | — | 提供師生 pay-as-you-go Claude 訂閱方案；繼哈佛 FAS、Syracuse 後另一高教具名案例 | 2026-08-18 |
| Samsung | 頂尖 | Claude Code | ✅ | — | 跨 3 媒體確認：壓縮晶片設計/驗證時程（數週→數天／一月→兩天，數字不一），仍會犯嚴重錯誤（細節見時序） | 2026-08-15（首見 2026-08-14）|
| ICON（NASDAQ: ICLR） | 大型（全球臨床研究委外機構 CRO）| Claude API | ✅ | 2026-07-29 | 整合 Claude AI 進臨床試驗流程；醫療研究/CRO 產業首個具名案例，08-04/08-10 媒體二三度跟進（非新事實）| 2026-08-10（首見 2026-07-29）|
| Syracuse University | 大型（高等教育機構）| Claude Code + Claude Cowork | ✅ | 2026-08-05 | 擴大 Claude Enterprise 授權，納入 Claude Code + Cowork；繼哈佛 FAS 後另一高教擴大採用案例 | 2026-08-05 |
| Grasshopper Bank | 中型（銀行，聚焦金融科技產業）| Claude API（MCP 整合） | ✅ | 2026-07-15 | 首家列入 Anthropic MCP 目錄的銀行；具體整合規模、應用場景未見細節 | 2026-07-15 |
| Alberta 省政府（加拿大） | 政府（省級） | Claude Code | ✅ | 2025 | 自 2025 年起用 Claude Code 審查系統；20 小時內掃描 4.66 億行程式碼完成資安盤點與修補 | 2026-07-07 |
| Alibaba | 頂尖 | Claude Code → Qoder（內部工具） | ❌ | 2026-07-10 | 「疑似後門風險」/資安疑慮禁用 Claude Code，改用 Qoder，生效 07-10；三方媒體確認替代方案；封鎖成因已查證見下方 ⟨Q-01⟩ | 2026-07-07 |
| Lindy | 中型（AI 新創） | Claude API → DeepSeek | 🔄 | 2026-06-29 | CEO 宣告 100% 流量切至 DeepSeek，每月省數百萬美元；最具名成本敏感案例（見 [[topics/enterprise-cost-management]]） | 2026-06-29 |
| 加州州政府 | 政府（州級） | Claude API | ✅ | 2026-06-29 | 州長 Newsom 與 Anthropic 正式簽署協議，Claude 進入加州州政府應用；迄今最明確的美國地方政府採用案例 | 2026-06-29 |
| Notion | 大型 | Claude Agents + Cursor | ✅ | 2026-06-25 | 正式整合 Claude Agents 與 Cursor 作為外部 agent，進入工作區協作流程；協作 SaaS 平台原生 AI agent 採用案例 | 2026-06-25 |
| Charleston Hospitality Group | 中型 | Claude API | ✅ | 2026-06-22 | 加入 Anthropic Claude 企業 AI 網路；餐旅業具名採用案例 | 2026-06-22 |
| Atlassian | 大型 | Claude API | ✅ | 2026-06-18 | Claude Agent for Jira 正式推出，企業整合嵌入全球最大專案管理工具 | 2026-06-18 |
| JFrog | 大型 | Claude Code | ✅ | 2026-06-18 | Governed Claude Code Integration，提供企業級安全管控的 Claude Code 部署方案 | 2026-06-18 |
| TCS（Tata Consultancy Services） | 頂尖 | Claude API | ✅ | 2026-06-11 | Global Premier Partnership；5 萬員工部署 Claude；同取得 Mythos Preview（Project Glasswing）存取 | 2026-06-11 |
| LG Group | 頂尖 | Claude API | ✅ | 2026-06-09 | LG 集團旗下全體關聯企業宣布採用 Anthropic Claude，韓國大型財閥全面入局企業 AI | 2026-06-09 |
| AppFolio | 大型 | Claude API | ✅ | 2026-06-09 | Realm-X 套件接入 Claude，agent-to-agent 架構直接觸發房地產績效管理流程 | 2026-06-09 |
| ZoomInfo | 大型 | Claude API | ✅ | 2026-06-07 | 透過 GTM.AI 平台整合 Claude，建構 GTM Context Graph 企業銷售情報系統 | 2026-06-08 |
| Salesforce | 頂尖 | Claude Code | ✅ | — | 宣布 2027 年起不新增軟體工程師，直接點名 Claude Code 壓縮系統移轉成本 | 2026-06-06 |
| Uber | 頂尖 | Claude Code ＋ Cursor | ⚠️ | 2026-05-01 | 4 個月燒完全年 AI 預算，CTO 承認成本失控，隨後設用量上限；COO 5/27 確認帶來 25% 生產力提升 | 2026-06-02 |
| Travelport | 大型 | Claude API | ✅ | 2026-05-27 | 與 Cognizant 三方合作，建構旅遊 AI 對話訂票系統 | 2026-05-27 |
| UiPath | 大型 | Claude Code ＋ OpenAI Codex | ✅ | 2026-05-12 | RPA 平台雙工具整合，同時部署 | 2026-05-12 |
| Amazon | 頂尖 | Claude Code ＋ OpenAI Codex | ✅ | 2026-05-05 | 雙軌並行，不押注單一供應商 | 2026-05-05 |
| Apple | 頂尖 | Claude API | ✅ | — | 外洩文件確認內部採用，非 Claude Code | 2026-05-01 |
| iCapital | 大型 | Claude API | ✅ | 2026-05-01 | 替代資產平台，為客戶建立 AI 工具 | 2026-05-01 |
| 哈佛 FAS | 大型 | Claude API | ✅ | 2026-04-28 | 取代 ChatGPT Edu，學術授權 | 2026-04-28 |

Microsoft、Amazon、Google 同時是 Anthropic 的出資者與雲端通路；表上只寫它們的員工用不用，投資與通路見 [[topics/anthropic-partnerships-compute#跟三大雲各是什麼關係]]。

**已查證的三件事**（⟨Q-nn⟩ 是本頁的查證編號，表與摘要引用處都指這裡）
- ⟨Q-03⟩ 已查證（2026-09-20，對照 [[topics/anthropic-government-policy]] 既有查證）：**兩案不同源**——JPMorgan（06-18）肇因出口管制（已於 06-30 解除）；Goldman／OKX（08-19/20）肇因 Anthropic 區域存取政策，與出口管制無關。此前「同源」猜測不成立，已更正。
- ⟨Q-02⟩ 已查證（2026-09-20，The Information＋Meta 回應）｜**Meta 限制工程師使用 Claude 屬實**：內部文件證實 Applied AI 團隊自 5 月起需核准才能用 Claude Code／Codex，6 月底生效，外部輸出禁入訓練樣本、須人工審查。
- Meta 發言人僅稱有「明確政策」，未直接證實或否認具體內容；與本頁既有 MetaCode 自建、降低外部依賴脈絡一致。
- ⟨Q-01⟩ 已查證（2026-08-13）：非混淆，為同一組事實的正確引用——tech-insider.org 報導確認封鎖係「兩起爭議交會」的結果：(1) 資安研究者指出 Claude Code 更新曾內含可辨識中國地區用戶的隱藏邏輯（「後門」爭議，Anthropic 否認為監控工具，稱是已在淘汰中的窄範圍反濫用實驗）；(2) 即為 06-25 已記錄之 Anthropic 蒸餾攻擊指控（約 2.5 萬假帳號、2,880 萬次對話）。兩者並非各自獨立的「新理由」，而是同一封鎖決策的兩項並存成因（[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens)；[tech-insider.org](https://tech-insider.org/ie/alibaba-bans-claude-code-2026/)）

---

## 對 agent 開發者的選型影響

- **退出不等於 Claude 不好用**：減用有數字的 Meta、Microsoft 都自己賣編碼工具（Muse Code、GitHub Copilot），而 Google（09-15）開放全體工程師使用、Amazon（05-05 起）雙軌並行；「自研夠強所以退」目前沒有證據。
- **讀數字先問主詞與基期**：10-05 Meta 的數字是 Claude Code 使用人數、Microsoft 的是全部 Claude 花費，拆法見 [[#2026-10-05]]。
- **大公司多半不押單一供應商**：表上明寫並用他家的有 Amazon、UiPath、Epic Games（＋Codex）與 Uber（＋Cursor），Notion 則在自家產品同時接 Claude 與 Cursor；其餘只寫用了 Claude，有沒有並用目前沒有證據。
- **員工的 Claude 用量會被設上限**：Accenture 報銷每月 $29（是否限 Claude Code 未見）、JPMorgan 部分工程師 Claude Code 每月 $2,000、Uber 燒完全年預算後設上限；API 自建應用的控管案例本頁沒有，機制見 [[topics/enterprise-cost-management]]。
- **資料保留是限縮的具名理由**：09-14 The Information 稱 Nvidia、Palantir、Booz Allen 都因資料外洩疑慮限縮（官方未回應個案），Palantir 要求零資料保留；官方保留政策見 [[topics/ai-agent-safety-product-vulns]]。
- **可用性可能不由你決定**：香港兩起切斷（06-18 出口管制、08-20 區域存取）與 Pentagon 黑名單都是別人劃的線；在這些地區或產業，先備好換得了供應商的工作流（推論，見 [[topics/anthropic-business-risks]]）。
- **工具之間誰搶誰**：Codex、Copilot、Cursor 的企業攻勢本頁不另計數，見 [[topics/competitor-landscape]]（Microsoft 轉向見 [[topics/competitor-landscape#Microsoft／GitHub]]）。

---

## 時序

### 2026-11

#### 2026-11-02
- **[新增具名企業，❌ 已退出] PYMNTS：高盛全面禁止行員使用 Claude Code 與 GitHub**：首見具名大型金融機構對 coding agent 下達禁用令；與 08-20 香港 Claude AI 存取權限切斷（區域存取政策）為不同案例，僅標題可用，禁令範圍與生效時間未見報導，詳見上方使用現況表新增列（Google News/PYMNTS.com）

### 2026-10

#### 2026-10-29
- **[既有企業，使用面跟進] TweakTown：Epic Games 已用 Claude Code 與 Codex 直接改善／除錯 Unreal Engine**：僅標題可用，導入範圍與成效數字未見報導，詳見上方使用現況表 Epic Games 列（Google News/TweakTown）

#### 2026-10-16
- **[新增具名企業，⚠️ 有爭議] TechCrunch：Replit 執行長表示已不再與 Anthropic 合作**：匿名知情人士否認合作已結束，雙方無正式聲明；10-18 由「已退出」改標「有爭議」，詳見上方使用現況表（Google News/TechCrunch；Unite.AI）
- **Replit 執行長說法（10-16）**：Amjad Masad 在 TechCrunch Disrupt 被問 8 月宣布的 OpenAI 合作是否代表不再與 Anthropic 合作，答「Yeah. I mean, yeah」；理由是成本、夥伴關係與效能（TechCrunch；[Unite.AI](https://www.unite.ai/replit-ceo-masad-says-company-no-longer-works-with-anthropic/)）
- **Replit 選型理由（10-16）**：Masad 稱 OpenAI 的 Sol／Astra 在從零 vibe-coding 建 app 上持續表現較好（TechCrunch）
- **Replit 反證（10-16）**：一位熟悉合作的匿名人士對 TechCrunch 否認合作已結束；Replit 9 月部落格仍列 Fable 5／5.1 用在 Replit Agent 生產環境；Replit 與 Anthropic 都沒發正式聲明
- **Replit 狀態判讀**：台上答問是執行長個人說法，不等於合約終止；標「有爭議」而非「已退出」，實際是否全面停用 Claude 未經證實（推論）
- **[新增具名企業，✅ 使用中] Accenture 將員工可報銷的 Claude 支出上限設在每月 $29，此前單月花費高達 $1,000**：詳見上方使用現況表新增列與 [[topics/enterprise-cost-management]]（Google News/Startup Fortune；24/7 Wall St.；The Times of India）

#### 2026-10-15
- **[新增具名機構，❓ 未確認] Bloomberg Government：美國參議院準備讓幕僚開始使用 Claude**：尚未確認已上線，詳見上方使用現況表新增列（Google News/Bloomberg Government News）

#### 2026-10-12
- **[新增具名企業，✅ 使用中] Epic Games 官方 GitHub 帳號釋出 Unreal Engine skills，供 Claude Code 外掛使用**：527 星，遊戲引擎廠商官方生態系支持信號；內部採用規模、使用範疇未見報導細節，詳見上方使用現況表新增列（GitHub Search）

#### 2026-10-09
- **[既有企業新產品線，補充來源] Business Wire：Rubrik 擴大「Project Hourglass」計畫，納入 Rubrik Code Guardian**：與 09-15 首發同一產品，本則首次點名所屬計畫名稱，未見額外效能數字，詳見上方使用現況表 Rubrik 列（Google News/Business Wire）

#### 2026-10-05
- **[⚠️ 縮減中，狀態更新] The Information：Meta 的 Claude Code 使用者約 6 萬降至約 3 萬，Microsoft 內部 Claude 支出砍逾三分之一**：4 家媒體跟進，兩家均未取消合約；與同週 Barclays 擴大導入對比，已查證 2026-10-07（The Information）
- **Meta 使用量（10-05，已查證 2026-10-07）**：The Information 報導 Claude Code 使用者由今年稍早約 6 萬降至約 3 萬；春季裁員約 10%（7.8 萬人）只解釋一部分，動機為推自家工具；近 28 天仍花逾 1.05 億美元（The Information）
- **Meta 自家工具（10-05，已查證 2026-10-07）**：MetaCode 是內部專用工具，使用者逾 3 萬；Muse Code 是 8 月起測試的對外產品、Claude Code 競品，內部使用者逾 6,000。兩者是不同工具，見 [[topics/competitor-landscape#Meta（Muse Code／Muse Glimmer／Muse Wonder）]]
- **Microsoft 支出（10-05，已查證 2026-10-07）**：原估逾 10 億美元的內部 Claude 支出砍逾三分之一；雲端部門人均月預算由 10 萬降至約 1 萬美元；動機為成本與推自家工具（The Information；PYMNTS）
- **Microsoft 改用工具（10-05，已查證 2026-10-07）**：Scott Guthrie、Jay Parikh 指示改用 GitHub Copilot／OpenAI 模型；Experiences and Devices 部門工程師遷往 GitHub Copilot CLI，見 [[topics/competitor-landscape#Microsoft／GitHub]]
- **兩家共通（10-05，已查證 2026-10-07）**：均未取消與 Anthropic 的合約，縮減只限員工內部工具；經 Microsoft 平台賣給客戶的 Anthropic 用量仍在成長；報導未見兩家或 Anthropic 回應（the-decoder；Yahoo Finance；GuruFocus）
- **主詞與基期（2026-10-11 註記）**：Meta 的數字是 Claude Code 使用人數（約 6 萬→3 萬）、Microsoft 的是全部 Claude 花費（金額），主詞不同；Meta 同期裁員約一成，人數降幅含裁員效應，兩家不可混比。

#### 2026-10-01
- **[新增具名企業，✅ 使用中] Barclays 擴大導入 Claude Code 全行，目標 2026 年底採用率達 50%**：2027 年擴及多數工程師，詳見上方使用現況表新增列（Anthropic Blog；Bloomberg；PYMNTS）

### 2026-09

#### 2026-09-17
- **[新增具名企業細節，✅ 使用中] Business Insider：JPMorgan Chase 美國本部Claude Code 設每月 $2,000 支出上限，並推 Devspace 沙箱**：與香港分行退出（06-18）為不同辦公室，已查證 2026-10-07，詳見上方使用現況表（Google News/Business Insider）
- **JPMorgan Chase 美國本部（09-17，已查證 2026-10-07）**：Claude Code 每月 $2,000 美元支出上限，只套用於部分工程師，每月重置、可申請提高；與香港分行退出（06-18）屬不同辦公室（Business Insider；[Newsquawk](https://www.newsquawk.com/headlines/jpmorgan-jpm-introduced-usd-2k-monthly-claude-code-spending-limits-for-some-engineers-and-is-rolling-out-a-more-secure-devspace-environment-business-insider-reports)）
- **JPMorgan Devspace（09-17，已查證 2026-10-07）**：AWS 上的容器化沙箱，隔離員工憑證與內部系統；8 月約 8,000 人持 Claude 授權，約 1,900 人在 Devspace 測試組（[Crypto Briefing](https://cryptobriefing.com/jpmorgan-claude-code-spending-limits/)）

#### 2026-09-16
- **[既有企業新產品線，補充來源] TNGlobal：Rubrik Code Guardian 另支援 MCP，用於 AI agent 情境**：與 09-15 marketscreener.com 首發同一產品，本則首次點名 MCP 整合，未見額外效能數字，詳見上方使用現況表 Rubrik 列（Google News/TNGlobal）

#### 2026-09-15
- **[新增具名企業，✅ 使用中] Business Insider：Google 開放全體工程師使用 Anthropic 的 Claude**：具體工具範疇（是否限 Claude Code）、部門、上線時程均未見報導細節，詳見上方使用現況表新增列（Google News/Business Insider）
- **[既有企業新產品線] marketscreener.com：Rubrik 發布 Rubrik Code Guardian，用 Claude Mythos 5 做程式碼紅隊測試**：既有 Claude Code agent（06-30）之外另一產品線，效能數字未見報導，詳見上方使用現況表新增列（Google News/marketscreener.com）

#### 2026-09-10
- **[新增具名企業，✅ 使用中] PR Newswire：T. Rowe Price 宣布擴大在投資流程中使用 Claude 與 Claude Code**：資產管理公司官方新聞稿宣布，marketscreener.com 同日獨立跟進報導；具體整合部門、規模、應用場景均未見細節，詳見上方使用現況表新增列（Google News/PR Newswire）

#### 2026-09-07
- **[既有企業擴大採用] FF News：PicPay 整合 Claude 擴大對話式 AI 金融服務**：延續 09-04 已記錄之銀行客服詢問導入，本則報導擴大整合範疇，具體技術細節未見報導，詳見上方使用現況表 PicPay 列更新（Google News/FF News）

#### 2026-09-04
- **[新增具名企業，✅ 使用中] PYMNTS.com：巴西金融科技公司 PicPay 導入 Claude 處理銀行客服詢問**：拉丁美洲市場首見具名金融科技採用案例，詳見上方使用現況表新增列（Google News/PYMNTS.com）

#### 2026-09-02
- **[四度確認，非新事實] Wccftech：Samsung 押注以 Claude Code 進行晶片設計**：與 08-14／08-15／08-25 既有記錄同一事實的第四次媒體確認，同篇報導並提及 Claude Fable 5.1 定價（見 [[entities/pricing]]），未見新增晶片設計時程或準確度數字，詳見上方使用現況表 Samsung 列（Google News/Wccftech，2026-09-02）

### 2026-08（總結；原始條目已移出）

- **Samsung 晶片設計（08-14～08-25）**：08-14 Digital Trends 首報（未確認）；08-15 TechSpot、Tech My Money 給出時程壓縮數字（兩說並陳），08-25 TechRadar 再確認，都指出仍會犯嚴重錯誤。
- **Goldman Sachs、OKX 香港被切斷（08-20）**：成因為 Anthropic 區域存取政策，與 JPMorgan 香港的出口管制案不同源（⟨Q-03⟩）。
- **Shopify（08-26）**：執行長揚言封殺 Claude Code，未見執行，維持 ❓。
- **新增具名採用**：Syracuse University 擴大授權納入 Claude Code 與 Cowork（08-07）、Duke University pay-as-you-go 訂閱（08-18）、Payward 採用 Mythos 5（08-19）、ReliaQuest 深化整合（08-22）。
- **跟進，非新事實**：ICON 臨床試驗合作二、三度報導（08-04、08-10）；Microsoft 內部備忘錄再傳不利消息（08-06，未改狀態）。
- 原始條目見 [[topics/enterprise-tool-tracker-archive#2026-08]]

### 2026-07（總結；原始條目已移出）

- **Alibaba 禁用 Claude Code（07-03～07-08）**：Reuters 07-03 首報「疑似後門風險」（HN 313 分）；07-05 確認生效日 07-10；07-07 三媒體確認改用內部工具 Qoder；07-08 Yahoo Finance 定調為中美 AI 資安爭端。首個以安全疑慮退出的案例，成因查證見 ⟨Q-01⟩。
- **Meta 限制工程師使用 Claude**：07-06 日報首提（未確認），後於 ⟨Q-02⟩ 查證屬實。
- **Alberta 省政府（07-07）**：Claude Code 20 小時掃描 4.66 億行程式碼，用於資安審查；繼加州州政府後第二個量化的地方政府案例。
- **Partner 擴張**：Cognizant 升級 Global Premier Partner（07-28）；ICON 把 Claude 整合進臨床試驗流程（07-29，Cognizant 股價次日再漲 8%）；Grasshopper Bank 成為首家列入 MCP 目錄的銀行（07-15）。
- **Microsoft（07-15）**：Yahoo Finance 傳其訓練業務團隊向客戶淡化 OpenAI 與 Anthropic 優勢（推論，未經官方證實）。
- **採購行為（07-06）**：The Information 稱部分小型企業改用 Claude 自建工作流取代 Salesforce，未點名企業。
- 原始條目見 [[topics/enterprise-tool-tracker-archive#2026-07]]

### 2026-06（總結；原始條目已移出）

- **Partner Network 密集擴張（06-09～06-30）**：LG、TCS（5 萬員工）、DXC（數萬認證工程師）相繼全面入局；06-29～06-30 單日/隔日新增 Globant、DataArt、Okta、Rubrik、加州州政府（Newsom 協議）等具名案例（詳見 [[topics/anthropic-partnerships-compute]]）。
- **產品/平台整合案例**：Atlassian Claude Agent for Jira、JFrog Governed Claude Code Integration（06-19）、Notion 整合 Claude Agents 與 Cursor（06-25）、ZoomInfo GTM.AI（06-08）、AppFolio A2A（06-09）。
- **Microsoft 退出加速（06-04～06-22）**：AI 主管批評定價過高（06-04）→ 宣布逐步停用 Claude Code（06-21，值 Fable 5 封鎖期間）→ The Jerusalem Post 跨媒體確認系統性降低依賴（06-22），GitHub Copilot 為主要替代方案。
- **JPMorgan Chase 香港出口管制退出（06-18～06-20）**：FT 首報香港辦公室因美國出口管制切斷 Anthropic 存取（06-18），Private Banker International 跨媒體跟進確認（06-20）；成因已於上方 ⟨Q-03⟩ 查證與 Goldman／OKX 案不同源。
- **Lindy 100% 切換至 DeepSeek（06-29）**：API 客戶流失代表案例，CEO 公開宣告每月節省數百萬美元。
- **Uber 成本管控（06-02～06-03）**：四個月燒完整年 AI 工具預算，隨即設用量上限，與 5/27 COO 確認的生產力提升形成對照。
- **其他具名新增**：Salesforce 宣布停招工程師並歸因 Claude Code（06-06）、Charleston Hospitality Group（06-23，餐旅業首例）。
- 原始條目見 [[topics/enterprise-tool-tracker-archive#2026-06]]

### 2026-05

- **2026-05-27**：Uber COO 確認 25% 生產力提升；Travelport+Cognizant 新增採用（見上方表）；富士通、Nimble Gravity 屬通路夥伴
- **2026-05-25**：Microsoft 宣布原訂 6/30 停用 Claude Code（後於 06-21 加速退出）
- **2026-05-12**：UiPath 同時整合 Claude Code 與 Codex
- **2026-05-05**：Amazon 全員雙品牌並行部署 Claude Code + Codex
- **2026-05-01**：Apple 內部採用經外洩文件確認；Uber 成本問題首報（Forbes 後於 5/18 深度確認）

原始條目見 [[topics/enterprise-tool-tracker-archive#2026-05]]

### 2026-04

- **2026-04-28**：哈佛 FAS 以 Claude 取代 ChatGPT Edu，學術機構結構性轉換

原始條目見 [[topics/enterprise-tool-tracker-archive#2026-04]]

---

## 相關實體

- [[topics/competitor-landscape]]
- [[topics/enterprise-cost-management]]
- [[entities/claude-code]]
- [[topics/anthropic-partnerships-compute]]
- [[topics/market-signals-customers]]

## 參考來源

- [[news/2026-05-27]]
- [[news/2026-05-25]]
- [[news/2026-05-18]]
- [[news/2026-05-15]]
- [[news/2026-05-12]]
- [[news/2026-05-05]]
- [[news/2026-05-01]]
- [[news/2026-04-28]]
