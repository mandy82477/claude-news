---
page: "topics/anthropic-partnerships-compute"
kind: "topic"
status: "ongoing"
domain: "💼 商業"
last_updated: "2026-11-02"
last_news_update: "2026-11-02"
status_main: "ongoing"
days_since_news: 1
parent: "topics/anthropic-business"
children: "[]"
page_role: "child"
days_since_news_subtree: 1
inbound_links: 10
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 合作與算力：跟誰簽、算力從哪來

Anthropic 跟誰簽了合作、算力和資金從哪來、跟三大雲各是什麼關係，以及哪幾筆會改到你拿得到什麼、付多少——事實和數字在這頁；同一筆交易該怎麼判讀，在 [[topics/market-signals-compute]]（算力與融資）與 [[topics/market-signals-customers]]（通路與客戶）。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/anthropic-business]]
**開始日期：** 2026-05-28
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-11-02

> **最新動態**（2026-11-02）
> - **Johns Hopkins 大學癌細胞圖譜技術獲選用於 Anthropic AI 專案**：具體應用細節未揭露（[Johns Hopkins University](https://news.google.com/rss/articles/CBMiggFBVV95cUxQQldCbnFMMG95WWZLYVJ0WUJnTHUtYU84enppOVdjSFllRm50WldNM3NfWl9oYXpkVkc0UEhRaGxqWGpHaGJ1a04xbTBXeTVpZ0pNaWZIbi1kNTVmNVZDX0FsLU5KMEJDVWFDR1gxRjVUVDJWaVVkRDV4SDVzdklLMzZ3?oc=5)）
> - **修訂版 S-1 揭露算力採購承諾與租賃協議升至 8,950 億美元**（其中 4,475 億預計 2030 年底前支出完畢），數字細節見 [[topics/anthropic-ipo#S-1 揭露了什麼]]（[CNBC](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)）

---

## 跟三大雲各是什麼關係

**同一家公司可以同時是出資者、算力供應商、通路，也可能是客戶或對手。** 每格一句，金額的家在格內連結。

| 公司 | 出資 | 算力 | 通路 | 也是客戶或對手 |
|---|---|---|---|---|
| Google | 2026-04-24 宣布最高 $400 億，見 [[entities/google-investment]] | TPU；S-1 承諾 $1,140 億（多家引 S-1） | Vertex AI，費率由 Google 自訂，見下方合作表 | Gemini 是直接對手，見 [[topics/competitor-landscape]] |
| Amazon | 累計 $80 億（2023-09～2024-11 三筆，媒體稱）；Series H 再出 $50 億（2026-05-28，多家報導） | S-1 承諾 $1,100 億（多家引 S-1） | Bedrock、Claude Platform on AWS；2025 年近半營收經 Amazon、Google 雲端市集賣出 | 賣家工具首波接 Claude（09-23）；Alexa 傳降低對高成本模型依賴（07-23） |
| Microsoft | 2025-11 承諾投資最高 $50 億（多家報導；實際入股金額未見） | 承諾購買 Azure 容量 $300 億（2025-11；[官方 05-06 公告](https://www.anthropic.com/news/higher-limits-spacex)提及） | Microsoft Foundry，CCU 後付 | 以自研 MAI 取代 Excel／Outlook 裡的 Claude，見 [[topics/anthropic-business-risks]] 細節區 |

Amazon 累計 $80 億與 Microsoft 承諾最高 $50 億是 2026-11-02 多家媒體交叉（[Fortune](https://fortune.com/2024/11/22/amazon-4-billion-investment-startup-anthropic-founder-defected-openai/)、[Nasdaq](https://www.nasdaq.com/articles/microsoft-and-nvidia-deals-push-anthropic-toward-350-bln-valuation)），未見 Anthropic 一手。

Nscale、Akamai、SpaceX 等其餘算力來源見下表；2025 年雲端市集 47% 的口徑見 [[topics/anthropic-ipo#S-1 揭露了什麼]]。


---

## 算力與資金從哪來

**這張總表把散在各處的算力合約與資金來源收在一處，欄位固定為對手方、金額與期限、狀態（洽談或已簽）、對可用性或價格的影響。** 寫不出可見後果的列明寫「目前無可見後果」並列下一個觸發點；不是投資觀點，估值與 IPO 進程見 [[topics/anthropic-ipo]]。

| 對手方 | 金額與期限（日期） | 狀態 | 對可用性或價格的影響 |
|---|---|---|---|
| Nscale（第二筆） | 約 $450 億，條款與年期未見（10-20） | 洽談中，尚未定案 | 目前無可見後果。下一個觸發點：簽約與容量公告 |
| Nscale（第一筆） | $450 億，460 MW Vera Rubin 世代，年期未見（08-28）；Nscale 全部客戶合約共 1,030 億，含 Microsoft | 已簽 | 目前無可見後果；第二筆金額同為 $450 億，與此筆獨立 |
| Blackstone | 晶片融資，兩位數殖利率；併入銀行團 $630 億 Broadcom 晶片融資方案（10-26 更新），殖利率仍未見 | 規模已確認，利率條款未載 | 目前無可見後果。下一個觸發點：利率與條款公開 |
| EverWind（加拿大新斯科舍省） | 資料中心供電給 Claude；規模、金額、時程未見（10-16） | 計畫報導，簽署未載 | 目前無可見後果。下一個觸發點：規模與上線時程 |
| Samsung Foundry | 代工 Anthropic 設計 AI ASIC，2 奈米；金額、產能未見（10-07） | 較 07 月洽談階段具體化，簽約未載 | 目前無可見後果（未見 Claude 改在該晶片上服務的時程） |
| SpaceX | 每月 $12.5 億運算容量（媒體稱，Anthropic 發言人向 Business Insider 證實；官方 [05-06 公告](https://www.anthropic.com/news/higher-limits-spacex) 載 Colossus 1 全部容量，逾 300MW、22 萬顆 GPU；10-31 查證） | 官方已證實合作與 Colossus 1 範圍；月費與期限為媒體稱 | 已見後果：05-06 官方隨 Colossus 1 容量提高用量上限。下一個觸發點：月費與期限的官方說法 |
| Broadcom | 貸款租賃晶片：最高 $420 億（10-01）；華爾街銀行＋Blackstone 安排 $630 億融資（10-26，較 10-02 的 $600 億更新） | 規模已確認，條款未見 | 目前無可見後果。下一個觸發點：條款或交付時程 |
| Akamai | $116 億 7 年 CPU 算力，另有報導稱 $120 億（09-25） | 已簽，含認股權證約 770 萬股 | 目前無可見後果 |
| Fluidstack | $500 億算力建置案，結構與時程未見（09-07） | 報導稱主導建置，簽署未載（僅標題） | 目前無可見後果 |
| Nvidia（經 Lambda） | Lambda 簽 $350 億雲端運算合約；Hut 8 同額案推論為同一筆（09-01） | 已簽 | 目前無可見後果；循環融資質疑屬評論 |
| Volta | 六年 $100 億，算力在挪威 Tydal（08-04） | 已簽 | 目前無可見後果 |
| Riot Platforms | $90 億 20 年雲端運算協議（08-11） | 已簽 | 目前無可見後果 |
| TeraWulf | $190 億 20 年肯塔基州園區租約（07-06） | 已簽 | 目前無可見後果 |
| AMD | 投資最高 $50 億並簽晶片協議；供應規模、股權比例未見（07-22） | 已簽 | 目前無可見後果（未見 Claude 改在 AMD 晶片上服務） |
| AWS | S-1 揭露承諾 $1,100 億（多家引 S-1，10-26）；先前報導逾 $1,000 億（09-06） | 已承諾 | 通路有價格後果：Bedrock 無 50% Batch 折扣，見 [[entities/pricing#通路：誰定價、怎麼開票]] |
| Google | 直接投資最高 $400 億（04-24）；近 $2,000 億融資機制，結構未見（推論，08-04） | 投資已宣布，融資機制結構未見 | 融資無可見後果；Vertex AI 費率由 Google 自訂，見 [[entities/google-investment]] |
| 股權與信貸 | Series H $650 億（05-28）；上市前信用額度傳逾 $100 億（08-18）；資料中心私募信貸 $13 億（08-19） | Series H 已完成；其餘為報導 | 目前無可見後果。下一個觸發點：定價與股數公告（S-1 已於 10-26 提交） |

**來源**
- Nscale 兩筆：第二筆 CNBC、Reuters、Bloomberg（2026-10-20）；第一筆 Forbes、Financial Times（2026-08-28）。
- Blackstone：Financial Times、Yahoo Finance（2026-10-17）；Reuters（630 億美元銀行＋Blackstone 聯合融資，2026-10-26）。EverWind：Global News、CBC（2026-10-16）。Samsung Foundry：TechPowerUp（2026-10-07）。
- SpaceX：Barchart.com（2026-10-03）、Hacker News 轉 WSJ（2026-10-10）；WSJ 稱由共同創辦人 Tom Brown 透過共和黨人脈牽線（單一媒體說法，未獲第二家佐證；交易本身已獲 Anthropic 官方公告證實，2026-10-31 查）。
- Broadcom：Reuters 獨家引文件（2026-10-01）、Yahoo Finance、qz.com（2026-10-02）。
- Akamai：Bloomberg、WSJ、IBD、Reddit（2026-09-25）。Fluidstack：AI Magazine（2026-09-07）。Lambda／Hut 8：多家媒體（2026-09-01／09-07）；24/7 Wall St. 質疑循環融資（09-02，評論）。
- Volta：TechCrunch、The Telegraph（2026-08-04）。Riot Platforms：多家媒體（2026-08-11）。TeraWulf：WSJ、CNBC（2026-07-06）。AMD：Reuters、WSJ（2026-07-22）。
- AWS：Currently.com、The Information（2026-09-06）。Google：2026-04-24 公告、FT（2026-08-04）。股權與信貸：官方（05-28）、Bloomberg、Yahoo Finance。

**此表未列、仍在洽談或僅具名**：GIC（新加坡主權基金）與 Macquarie 合作開發資料中心（08-11，規模未見）；Morgan Stanley 領投 $150 億德州資料中心投資（08-02），10-29 彭博報導銀行已撤回該案一筆債券發行，原因未見報導；Bastrop County 德州園區洽租中（08-25）。各案細節見下方「其餘合作」清單。

**財務面**：S-1 揭露的算力長約四家合計逾 5,000 億美元，會不會轉成定價壓力見 [[topics/anthropic-business-risks#還沒過去的風險]]；Amazon／Google 通路集中（2025 年近半營收經兩家雲端市集銷售，非客戶集中）見 [[topics/anthropic-ipo#S-1 揭露了什麼]]。

**寫得出後果的只有兩則**：05-06 官方隨 SpaceX Colossus 1 容量上線提高用量上限；07-18 Startup Fortune 稱因運算吃緊收緊 Fable 5 存取，本站查證的官方文件只寫方案分界、未載原因，見 [[entities/pricing]]「當前生效的計費規則」07-20 條。各列共同的下一個觸發點是正式定價與股數公告（公開版 S-1 已於 2026-10-26 提交）。

%% 維運備忘：2026-10-04 首次彙整；2026-10-25 週度回顧改為算力合約總表（拆列、補期限與狀態、Nscale 標第二筆）。新合約出現時先判斷「可見後果」欄寫不寫得出，寫不出就寫「目前無可見後果」；各交易原始細節的家仍是下方合作表一行制清單與 ## 時序。席位限縮是否為產能管控：無來源，不寫 %%

## 哪個合作會改到你用的 Claude

**這張表只列會改到你拿得到什麼、或付多少的合作。** 其餘合作是公司擴張的紀錄，在下方一行制清單裡。

**通路差異資料截至 2026-10-31，以 [[entities/pricing#通路：誰定價、怎麼開票]] 為準**（與 pricing「通路與乘數」同批；該頁 10-31 查證明載通路五條與 09-26 一致）。

| 合作方 | 會改到什麼 | 不會改到什麼 | 最後動態 |
|---|---|---|---|
| GSA（美國聯邦總務署，OneGov） | Claude Enterprise／Claude for Government／API 折扣提升至 40%，首度涵蓋全部採購管道（含日後透過雲端供應商採購），並延伸至州、地方、部落與屬地政府 | 非政府機構採購不適用 | 2026-10-27 |
| Amazon Bedrock | 走 Bedrock 拿不到 50% Batch 折扣；compaction／context editing／task budgets 都不可用；首爾／新加坡新增境內推論；新增 structured outputs 支援 | 第一方 API 與訂閱席次不受影響 | 2026-10-20 |
| Claude Platform on AWS | 組織固定在 Start 層不自動升級，月花費上限 $500，提額要聯繫客戶代表 | 費率仍是 Anthropic 標準價 | 2026-09-03 |
| Google Cloud／Vertex AI | 新增走 GCP 帳單／帳戶權限的 Anthropic 代管 API 路線，處理器與功能選擇不同於標準 Vertex（MIXED News／OpenTools，10-26，單一來源各一）| 費率仍由 Google 自訂，第一方牌價不變 | 2026-10-26 |
| AWS（模型上線） | Claude Fable 5.1 已在 AWS 平台可用 | 不改價 | 2026-09-02 |
| Microsoft Foundry | 走 CCU 後付，折扣以「同一筆用量換算出較少 CCU」呈現 | 費率仍是 Anthropic 標準價 | 2026-09-03 |

**通路的完整對照（誰營運、誰定價、計費單位）見 [[entities/pricing#通路：誰定價、怎麼開票]]，乘數見 [[entities/pricing#乘數：會互相疊乘]]。**

**這張表講的是 API 通路。** 訂閱席次（Claude Code、Team、Enterprise）不走上面這幾條通路，雲端合作不改變席次價格或可用性；席次現在包含什麼見 [[entities/pricing#我的方案現在有什麼]]。

%% 維運備忘：2026-10-27 新進 GSA（折扣，影響價格）進表，表滿載觸發讓位，依留表優先序（資料落地類最弱）讓位者為「Enterprise Frontier Safeguards」，已移出表、降為下方一行制清單條目。餘五列最後動態最舊為 2026-09-02，180 天到期日 2027-03-01。 %%

**資本支出的量級（本頁計算，2026-08-29）：** Nscale 單筆 450 億美元（08-28）是多年期合約總額、年期未見，不能拿去跟一年的營收（年化 650 億）直接相比；同月另有 AMD、Nvidia 兩筆算力布局、13 億美元私募信貸（08-19）與 Bastrop County 洽租（08-25）。循環融資質疑見 [[topics/anthropic-business-risks#還沒過去的風險]] 細節區。

**其餘合作（新的在上）** — 未列入上表者每筆一行：

- **Johns Hopkins University**（2026-11-02）：癌細胞圖譜技術獲選用於 Anthropic AI 專案，具體應用細節未揭露（Google News/Johns Hopkins University）
- **AI for Science（擴大至 20 機構）**（2026-10-29）：官方擴大科研夥伴計畫，20 個基金會／機構／研究團隊取得免費 Claude 額度，涵蓋生物、醫學、物理、化學、氣候科學與數學（Anthropic；Google News）
- **Mollie**（2026-10-29）：荷蘭金融科技公司推出 AI plugins 與 MCP server，供 Claude 與 ChatGPT 使用；具體功能與計費未見報導（Google News/The Paypers）
- **生命科學深度研究合作（6 組織）**（2026-10-27）：官方近況：與 BigHat、BMS、Divergence Labs、Enveda、Generate Biomedicines、The Column Group 合作藥物開發，並啟動自家藥物探索；模型面見 [[entities/claude-science]]（Anthropic；HN 294 分）
- **Mithril Medicine（收購）**（2026-10-27｜訊 2026-10-29）：收購一人神秘生技新創，由匿名 Twitter 用戶經營；Forbes 稱該新創此前以 Claude 運行藥物開發專案，金額與整合計畫未見報導（Endpoints News；R&D World；Forbes）
  - Mithril Medicine 為一人生技公司，創辦人 Cody Tranbarger，研究罕見肌肉萎縮症藥物；收購於 2026-10-27 公告，媒體稱交易發生在 7 月，金額未揭露（The Next Web、The Neuron、OfficeChai，2026-11-01 查證）。
  - Anthropic 稱最早 2028 年底進入臨床；「drug R&D chief」Endpoints 專訪原文未找到，負責人身分未確認（2026-11-01 查證）。
- **Claude for Legal Artifacts**（2026-10-28）：Reuters／Law.com 報導 Anthropic 推出互動式法律工具組，僅標題可用，延續 08-07 設立 Claude for Legal 部門（[[entities/robert-mahari|Robert Mahari]] 負責）（Google News/Reuters；Law.com）
- **Lumia Security**（2026-10-27）：資安治理平台新增整合 Claude Compliance API，延續 Surf AI（07-28）、Cyberhaven（07-23）、Orca Security（07-21）等資安夥伴生態擴張模式，具體規模與商業條款未見報導（Google News/Yahoo Finance）
- **Claude for Financial Advisors（訊號）**（2026-10-28｜訊 2026-10-29）：PYMNTS 稱擴大整合範圍，新增對象未見報導；Citywire 稱用戶最高可領 $4,800 額度抵用，門檻與期限未附（PYMNTS；Citywire）
- **Enterprise Frontier Safeguards（AWS／Google Cloud／Azure 三雲）**（2026-09-01）：企業客戶資料改存在自己控制的雲端，EFS 免費，2026 秋季起分階段開放；個人 Pro／Max 不在範圍內（原列於上表，2026-10-27 讓位給 GSA 折扣列移入本清單，事實不變）
- **Hg（歐洲顧問服務）**（2026-10-23）：Financial Times 與 SQ Magazine 同日報導 Anthropic 與私募基金 Hg 合作，於歐洲推出 AI 顧問服務供當地企業導入 AI，合作細節與服務範疇未見報導（Google News/Financial Times；Google News/SQ Magazine）
- **學術機構／生命科學（Guest Investigator Program）**（2026-10-23）：官方公開徵求學術機構、非營利組織或政府實驗室研究團隊，於 8–12 週內與 Anthropic 研究員合作研究因果人類生物學、分子生物學、藥物化學等題目，模型與運算成本由官方負擔（[Anthropic Blog](https://www.anthropic.com/news/open-call-guest-investigators-life-sciences)）
- **Simform**（2026-10-21）：取得 Claude Partner Network「Select Tier」服務夥伴資格，延續 Tenth Revolution Group（10-14）、Aditi Consulting（10-08）等同系列夥伴認證，具體權益未見報導（Google News/EIN Presswire）
- **Google Antigravity**（2026-10-20）：Claude Opus 5.5 與 Sonnet 5.5 已在 Google 旗下 Antigravity 平台上架，具體整合範疇與計費未見報導（Google News/Google Cloud）
- **Emory University**（2026-10-19）：Claude AI 正式開放予 Emory 大學社群使用，具體導入規模與產品線未見報導（Google News/Emory University）
- **Anthropic（新加坡辦公室）**（2026-10-14）：於新加坡開設亞太區第五個辦公室，並與新加坡數位發展與資訊部簽署 MOU；官方點名 GovTech Singapore、Grab、DBS 為既有 Claude 使用方，具體採用規模與產品線未見報導（Anthropic Blog）
- **Tenth Revolution Group**（2026-10-14）：取得 Claude Partner Network「Select」夥伴資格，延續 Fabric（09-28）、IPC Global（10-05）、Nimble.LA（10-06）、Intuitive.ai（10-07）同系列夥伴認證，具體權益未見報導（Google News/HRTech Series）
- **Aditi Consulting**（2026-10-08）：達成 Anthropic「Select Tier」夥伴資格，稱已在自家業務與客戶環境全面導入 Claude 投入生產，具體權益與資格門檻未見報導（Google News/DevOps.com）
- **Hexaware**（2026-10-08）：成為 Anthropic Preferred Partner，將 Claude 導入其 AI-native 平台核心，具體權益未見報導（Google News/PR Newswire）
- **OutSystems**（2026-10-08）：Agent Experience 平台開放支援 Claude Code 與 Cursor，具體整合範疇未見報導（Google News/Techzine Global）
- **xAI（Grok Bot）**（2026-10-07）：Grok Bot 整合 Anthropic Claude、Midjourney、Suno 模型以提升回應品質，具體整合範疇與計費未見報導（The Next Web；9to5Mac）
- **Intuitive.ai**（2026-10-07）：Anthropic 將其列為 Claude Partner Network 優先夥伴，資格門檻與具體權益未見報導（Yahoo Finance；GlobeNewswire）
- **Momentic**（2026-10-06）：Microsoft 官方案例研究，描述其透過 Microsoft Foundry 使用 Claude 將自然語言需求轉換為通過測試，具體整合規模未見報導（Microsoft）
- **Commvault**（2026-10-02）：AgentRecover 可探索、保護並還原 Claude Cowork、Claude Code 的 agent 設定與累積脈絡，涵蓋員工 Windows 與 macOS 端點，定價未見報導（Google News/Blocks & Files）
- **Pureinsights**（2026-09-30）：Discovery 2.12 版本新增 Claude 整合，涵蓋文件擷取與查詢管線，具體功能與計費未見報導（Google News/EIN News）
- **ExodusPoint**（2026-09-29）：避險基金加入與 Anthropic 就 AI 合作的機構陣容，延續 08-06 已記錄之 Millennium 案例，具體技術範疇與商業條款未見報導（Google News/Bloomberg.com）
- **Fabric**（2026-09-28）：加入 Claude Partner Network；同日官方推出 Claude Marketplace，收錄逾 2,000 個 connector 與 plugin，具體合作範疇與計費未見報導（Google News/EIN News；Google News/gHacks）
- **Akamai**（2026-09-25）：簽署 7 年、116 億美元運算合約，供應 CPU 算力；認股權證可認購約 770 萬股 Akamai 股票，另有報導稱總值 120 億美元（Bloomberg；WSJ；IBD；Reddit）
- **09-29 跟進（地方媒體角度，非新事實）**：The Boston Globe 稱波士頓少見的 AI 產業利多，未見新增合約細節（Google News/The Boston Globe）
- **Basecamp**（2026-09-24）：AI 製藥新創 Basecamp 獲 NVIDIA、Anthropic 領投 1.4 億美元融資，用於推進 AI 輔助藥物設計，具體投資額度與角色未見細節（Google News/BioSpace）
- **Adobe**（2026-09-24）：Adobe 把 Acrobat 帶進 Claude 生態，同批對 Google Gemini 開放存取，具體整合範疇與計費未見報導（Google News/9to5mac.com）
- **Oracle**（2026-09-23）：Oracle 官方部落格說明如何串接 Claude 至 Oracle Integration 工具，具體功能範疇未見報導（Google News/Oracle Blogs）
- **Amazon（Seller Assistant／Amazon Quick 外掛）**（2026-09-23）：開放賣家工具予外部 AI 代理人，首波合作對象為 Claude，同步升級 Seller Assistant 並推出結合 Amazon Quick 與 Claude 的新外掛，具體功能與計費未見報導（GeekWire；About Amazon）
- **OpenEvidence**（2026-09-22）：Reuters 獨家報導 Anthropic 與醫療 AI 服務 OpenEvidence 結盟，計畫將醫療 AI 服務推向全球，合約範疇與費用未見報導（Reuters；PYMNTS）
- **09-28 追蹤**：Fierce Healthcare 報導擴大偕 Penn Medicine 合作，將醫師 AI 取得管道推向非洲、亞洲，合約細節仍未見報導（Google News/Fierce Healthcare）
- **未具名資料中心（控制權洽談）**（2026-09-23）：The Information 報導 Anthropic 正洽談加強對更多資料中心的控制權，具體規模、對象未見報導（Google News/The Information）
- **Palo Alto Networks**（2026-09-22）：推出結合 Claude、GPT 模型的 AI 資安服務，具體整合規模與費用未見報導，僅標題可用（Yahoo Finance）
- **Novo Nordisk**（2026-09-16）：與 Anthropic 合作，用 Claude 加速藥物研發與醫學研究，合約範疇與費用未見報導（Reuters；Bloomberg；WSJ；politico.eu）
- **Apple（iOS 27／macOS）**（2026-09-14）：程式碼曝光顯示 Siri 新增「Model Delegation」機制，可讓使用者把 Claude、ChatGPT 設為第三方模型；尚未正式發布，計費與上線時間未見報導（MacRumors／HN 188 分）**訊 09-19**：Reddit 週熱門重新討論同一線索，無新細節
- **Charles Schwab／Orion**（2026-09-14）：兩平台同日宣布導入 Claude，鎖定 RIA 通路，費率未見報導（Bloomberg 等）**訊 09-15**：官方定名「Claude for Financial Advisors」，詳見下方時序（Reuters）**訊 2026-10-24**：追加席位下限，見 [[entities/pricing]]
- **Visa／Mastercard**（2026-09-09）：推出 Claude Commerce Agents 商務代理功能並與兩家建立合作，交易機制、資格與是否另計費均未見報導，僅標題可用；與 09-04「自建支付技術」同屬跨入支付基礎設施（見「商業模式」節）（Crowdfund Insider）
- **LoanPro**（2026-09-09）：貸款管理平台採用建構在 AWS 與 Claude 上的 AI 原生客服介面，客服通話時間最多縮短 15%，具體導入規模未見報導（citybiz）
- **Fluidstack**（2026-09-07）：主導 Anthropic 一筆 500 億美元的算力建置案，詳見下方細節（AI Magazine）
- **Hut 8**（2026-09-07）：比特幣礦業公司藉 350 億美元 Anthropic 合作案加速 AI 業務轉型，推論與 09-01 已記錄的 Lambda 交易為同一筆，詳見下方細節（Yahoo Finance）
- **Amadeus**（2026-09-03）：旅遊科技公司將其技術整合進 Claude Code 與 Cowork，具體整合範疇未見報導（Skift）**訊 2026-09-09 追蹤**：Aviation Week 同日再報導此合作，未見新增整合範疇或金額細節，僅為又一媒體轉述（Google News/Aviation Week）
- **Lambda**（2026-09-01）：Nvidia 支持之雲端業者簽署 350 億美元雲端運算合約，資金牽涉德州比特幣礦商營運的資料中心（多家媒體）
- **Anthropic（培訓生態）**（2026-09-01）：Claude 認證累計達 8.5 萬張，擬擴大夥伴培訓規模（crn.com）
- **Trifecta Technologies**（2026-09-01）：與 Anthropic 合作導入 Claude 服務（Morningstar）
- **Amazon（AWS GovCloud）**（2026-08-31）：Claude 隨 OpenAI、Meta 模型引入 AWS GovCloud（Seeking Alpha）。**訊 2026-10-05**：Unite.AI 詳述部署細節，同日 BBC 報導國防部黑名單後停用，聯邦體系立場不一
- **一般大眾／美國中小學（Claude for Teachers）**（2026-08-31）：開放美國中小學與學區免費使用 Claude for Teachers 企業版（EdTech Innovation Hub）
- **Cursor（SpaceX 旗下）**（2026-08-29）：OpenAI 退出與 Cursor 的合作，Anthropic 加碼投入運算資源承接需求（Wccftech）
- **Nscale**（2026-08-28）：簽署 450 億美元資料中心協議，取得 460 MW Vera Rubin 世代算力（Forbes；Financial Times）
  **訊 2026-09-21 追蹤**：Bloomberg 報導 Nscale 總合約值達 1,030 億美元，Anthropic 與 Microsoft 為最大兩家客戶，首度揭露 Nscale 整體規模與客戶排名（Google News/Bloomberg.com）
  **訊 2026-10-19 追蹤**：CNBC／Reuters／Bloomberg 報導雙方洽談第二筆合作，規模同樣約 450 億美元，尚未定案，為獨立於本筆的新協議，詳見「時序」（Google News/CNBC；Google News/Reuters；Google News/Bloomberg.com）
- **Anthropic（營收信號）**（2026-08-28）：Yahoo Finance 獨家稱 Claude 營收年增達 1,000%，未經官方證實（Yahoo Finance）
- **Salesforce**（2026-08-26，訊 2026-09-08）：深化合作發布 CRM 業務外掛「Claudeforce」，Salesforce 同步上修全年營收預測（Reuters；WSJ）。09-08 Demand Gen Report 稱雙方「擴大」合作，擴大範疇未見報導，僅標題可用（Google News/Demand Gen Report）
- **CrowdStrike**（2026-08-27）：股價單日漲 13%，執行長歸功本季最佳表現部分來自與 Anthropic 合作（Forbes）
- **Meta**（2026-08-27）：NYT 稱雙方「亦敵亦友」，Meta 公開批評 Anthropic 卻也是其最大客戶之一，傳支出達 100 億美元（NYT）
- **Anthropic（澳洲市場）**（2026-08-25）：內部郵件揭露 Anthropic 澳洲佈局規模（ABC News）
- **未具名 AI 資安新創**（2026-08-25）：與 Anthropic、Google 合作的新創獲 1.4 億美元融資（Bloomberg）
- **未具名資料中心業者（Bastrop County）**（2026-08-25）：洽談租用德州 Bastrop County 大型資料中心（KXAN Austin）
- **UpToDate**（2026-08-24）：深化與醫療資訊平台 UpToDate 的合作（Fierce Healthcare）
- **一般大眾／企業客戶（Claude Academy）**（2026-08-23）：推出免費 AI 課程與企業導入指南，首度面向一般大眾（EdTech Innovation Hub）
- **Casper Studios**（2026-08-20）：Ode（Anthropic/Blackstone 合資）收購顧問公司 Casper Studios，金額未公開（crn.com；Seeking Alpha）
- **Anthropic 關聯資料中心（未具名）**（2026-08-19）：取得 13 億美元私募信貸貸款（Yahoo Finance）
- **Decart**（2026-08-13 洽購、2026-09-08 撤回）：原擬以約 60–70 億美元收購以色列世界模型新創 Decart，09-08 傳出計畫遭撤回，以色列與財經媒體同日密集跟進（PYMNTS；Bloomberg；calcalistech；Ynetnews；Globes）
- **Riot Platforms**（2026-08-11）：與加密礦業公司簽署 90 億美元、20 年雲端運算協議（多家媒體）
- **GIC**（2026-08-11）：與新加坡主權基金合作開發資料中心（多家媒體）
- **Macquarie**（2026-08-11）：與澳洲金融集團合作開發資料中心（多家媒體）
- **Naver**（2026-08-11）：南韓 Naver 投資 Anthropic 700 萬美元，屬策略聯盟訊號（KED Global）
- **[[entities/robert-mahari|Robert Mahari]]**（2026-08-07）：任命為新設「Claude for Legal」部門負責人（Legal IT Insider；Law.com）
- **Millennium**（2026-08-06）：避險基金與 Anthropic 合作開發 AI 風險分析師工具（Yahoo Finance）
- **AWS（Continuum）**（2026-08-05）：AWS 官方宣布與 Anthropic、OpenAI 合作推出 AWS Continuum 導入開發者工作流（AWS；VentureBeat）
- **Volta**（2026-08-04）：與英國新創雲端商（2026 年初成立，Nvidia Cloud Partner）簽署 **六年期 100 億美元**運算協議，算力落在挪威 Tydal 資料中心（TechCrunch；The Telegraph）
- **SpaceX**（2026-08-04）：財報揭露營收翻倍，動能含與 Anthropic／Google 運算合作（TechCrunch）
- **Google**（2026-08-04）：FT 稱 Google 為 Anthropic 牽線近 2000 億美元華爾街融資機制（Financial Times）
- **Anthropic（印度市場）**（2026-08-03）：宣布擴大印度市場布局（ndtv.com）
- **Morgan Stanley**（2026-08-02）：領投 150 億美元，投向 Anthropic 德州校園/資料中心（thestreet.com）
- **[[entities/amir-salek|Amir Salek]]**（2026-08-21）：延攬 Google TPU 專案創辦人進 compute 團隊，向 James Bradbury 匯報（Seeking Alpha；Bloomberg）
**其餘合作彙整（2026-07，30 筆）**：算力與晶片——TeraWulf（07-06，20 年 190 億美元租約）、AMD（07-22，最高 50 億投資＋晶片協議）、Meta 運算力租賃洽談（07-17，100 億）、Samsung 代工洽談（07-02／07-06）、SK 集團晶片供應接洽（07-26）、澳洲 1.4GW 資料中心採購（07-05）；企業與服務夥伴——UST（07-10／07-14／07-20）、Cognizant 升為全球首要夥伴（07-28）、Deloitte（07-17）、FIS（07-17）、LTM（07-13）、Optum（07-14）、Blackstone 合資 Ode（07-16，15 億美元）；資安整合——Orca Security、Druva（07-21）、Cyberhaven（07-23）、Surf AI（07-28）、Varonis（07-14）、Oxide 加入 Glasswing（07-29）；雲端與工具——AWS 治理功能（07-09）、Enterprise Gateway（07-01）、Google Workspace（07-06）、Claranova（07-15）、MixRoute（07-05）、企業支出控管（07-04）；政府——美國商務部協議（07-01）、加拿大政府 1,000 萬加幣（07-15）；另有 Blackstone 高淨值基金表現（07-02）。原始條目見 [[topics/anthropic-business-archive#2026-07]]。
**其餘合作彙整（2026-05～06，21 筆）**：晶片／資本——Samsung+SK Hynix（05-28，Series H 同步入股）、Apollo+Blackstone（05-29，360 億美元晶片債務融資）；企業導入——富士通（05-26）、KPMG（05-25）、Stainless 收購（05-18）、DXC Technology（06-12，多年全球聯盟）、Micron Technology（06-22，記憶體協議＋投資）、Charleston Hospitality Group（06-22）、Railway（06-24）、Notion（06-25）、Tenable（06-29，Compliance API）；Partner Network 單日四項（06-30：Rubrik、Okta、DataArt、Globant）；政府／政策——加州州政府（06-29）、美國政府 Mythos 5 分兩批解禁（06-27／06-28）、奧地利／歐盟遊說（06-28）；歷史投資——Google（2026-04-24，最高 $400 億，見 [[entities/google-investment]]）、Amazon（2023–2024，$40 億）。原始條目見 [[topics/anthropic-business-archive#2026-06]]（06-12 以前及兩筆歷史投資見 [[topics/anthropic-business-archive#2026-06-14 以前]]）。

%% 維運備忘：原「意義」欄的敘述併進上方一句，不另外開細節條目；一句寫不下者才下沉「戰略合作細節」區。本清單只保留最近 3 個完整月，逾窗列滾動進 archive。2026-09-20：21 列 ≤2026-06-30 搬出；2026-11-02（第 23 波）：07 月 30 列與 07 月細節 12 條搬至 archive「## 2026-07」末，表清單現起點為 2026-08-01（08 月列 12-01 到期）。條文的家在 `.claude/reporter-rules/commercial/pages.md` 第 5 條。 %%

**戰略合作細節**
- **Amazon Bedrock structured outputs（10-19）**：AWS 官方部落格宣布 Bedrock 上的 Claude 模型新增結構化輸出支援，開發者可省去額外輸出格式校驗邏輯，細節以官方文件為準（Google News/Amazon Web Services (AWS)）。
- **Accenture 內嵌評估者，承諾 10 億美元（2026-09-19）**：Anthropic 宣布由 Accenture 出任首位「內嵌評估者」，回應 CEO「We Must Pace the Frontier」承諾；Washington Post 報導同步承諾投入 10 億美元（WaPo）
  - 官方原文（2026-10-03 查證）載為 Anthropic 與 Accenture 合計至少 10 億美元、五年期，用於內嵌評估能力建設，Anthropic 直接資助 Accenture 的工作（[Anthropic Blog](https://www.anthropic.com/news/accenture-embedded-evaluation)）
- **Amadeus（09-03）**：Skift 報導旅遊科技公司 Amadeus 將其技術整合進 Claude Code 與 Cowork；延續本頁既有 SDK 夥伴生態邊緣擴張模式（如 Claranova、MixRoute），是旅遊產業首個具名整合案例，惟具體整合形式（MCP 連接器、資料 API 或其他）、涵蓋範圍未見報導，僅標題可用（Google News/Skift）。
- **Enterprise Frontier Safeguards（EFS，09-01，官方一手來源）**：Anthropic 官方部落格宣布推出 EFS，結合零資料留存（ZDR——資料存放於**客戶控制**的雲端基礎設施，而非 Anthropic 控制）與最新濫用偵測技術，回應企業客戶「資料主權」與「AI 安全監控」雙重需求；**EFS 本身免費**。由 100 多家企業客戶（涵蓋金融、醫療、製造、電信、法律、零售、公部門七大產業）共同開發，並與 AWS、Google Cloud、Microsoft Azure 三大雲端夥伴合作，**今秋起分階段開放**（未見完整生效時程與資格門檻）。**過渡期安排**：符合資格的企業客戶可在 Fable 5／5.1 上先行取得零資料留存待遇。csoonline.com、SecurityWeek 同步跟進報導，聚焦企業採用角度，未見新增細節（Google News/csoonline.com；Google News/SecurityWeek）。**與既有懸置的關係**：本則為 08-20 Reuters/Bloomberg「企業資料保留政策調整」、08-21 Techzine「自有雲端環境」兩則傳聞的強力後續（查證進度詳見 [[entities/pricing]] 對應段落，已加註訊號日）；惟 EFS 明確定位為「安全監控產品」而非單純保留政策調整，兩者是否完全對應同一政策變動尚未確定。本則側重商業／企業採用角度（客戶共創規模、雲端夥伴生態、市場定位）；EFS 涉及的濫用偵測技術機制、與既有安全事件（Reuters 08-31 METR 獨立審查等，見 [[topics/anthropic-commitments]]）的關係詳見 [[topics/ai-agent-safety]]（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)，2026-09-02）。
%% 維運備忘：EFS 與 08-20/08-21 兩則傳聞是否完全對應同一政策變動，留待主編核對官方全文後於 lint 判定是否結案，本頁不逕自宣告解消；EFS 技術機制面是否需在 ai-agent-safety 補充，已轉知安全政策記者評估。 %%
- **AWS 官方公告 Claude Fable 5.1 上線（09-02）**：AWS 官方部落格宣布 Claude Fable 5.1 於 AWS 平台上線可用，屬雲端夥伴角度公告，未見具體定價或功能差異細節。與同日 EFS 公告中列名之 AWS 合作、以及官方定價文件同步出現「Fable 5.1」版本號互相呼應——Fable 5.1 存在的官方佐證持續累積（另見 [[entities/pricing]]「模型 API 定價現況」快取費率條目）（Google News/Amazon Web Services (AWS)，2026-09-02）。
%% 維運備忘：Fable 5.1 版本狀態已轉知模型記者查證。 %%
- **Lambda（09-01 交易，09-02 追加分析：循環融資質疑）**：本頁 09-01 已記錄 Anthropic 與 Nvidia 支持之雲端業者 Lambda 簽署 350 億美元雲端運算合約（資金牽涉德州一座由比特幣礦商營運的資料中心園區，延續近期 Nscale $450 億、Riot Platforms $90 億、Volta $100 億等算力布局系列）。**09-02 追蹤**：24/7 Wall St. 發表分析文章，質疑此筆交易是否構成「循環融資」（circular financing）——Nvidia 投資／支持 Lambda，Lambda 再以巨額合約向 Anthropic 採購雲端運算，資金流可能部分繞回 Nvidia 生態圈，與既有 07-22 AMD 交易 HN 討論串「ouroboros circle（銜尾蛇循環）」質疑同屬同一類商業模式疑慮（推論，並陳觀點非本頁定論）；具體資金流向、Nvidia 於 Lambda 之實際持股／投資規模未見報導，屬單一媒體分析評論，非新增交易或官方回應。風險層面另見「還沒過去的風險」表新增列（Google News/24/7 Wall St.，2026-09-02）。
- **09-07 推論確認**：Yahoo Finance 報導比特幣礦業公司 Hut 8 藉 350 億美元 Anthropic 合作案加速 AI 轉型；金額、地點與 09-01 記錄之 Lambda 交易相符，推論為同一筆，惟原文未點名 Lambda，尚待其他來源確認（Google News/Yahoo Finance）。
- **Fluidstack（09-07）**：AI Magazine 報導 Fluidstack 主導 Anthropic 一筆 500 億美元算力建置案，延續 Nscale／Lambda 等新興供應商加入模式；合約結構、時程未見報導，僅標題可用（Google News/AI Magazine）。
- **Amazon AWS GovCloud（08-31）**：Seeking Alpha 報導 Amazon 將 OpenAI、Meta、Anthropic 三家模型引入 AWS GovCloud，供政府相關客戶使用。是本頁首度出現 Claude 透過 AWS 政府雲環境（而非既有加州州政府 06-29 直接協議、或既有 AWS Enterprise Gateway 07-01 一般企業導入路線）進入聯邦/政府市場的具名案例，顯示 Anthropic 的政府市場布局正同時走「直接對政府簽約」與「透過既有雲端夥伴的政府專屬環境」兩條路線（推論）；具體服務範疇、與 OpenAI／Meta 模型並列上架是否代表 GovCloud 客戶可自由選型、上線時程均未見報導，僅標題可用。
- **Claude for Teachers 免費開放 K-12 學區（08-31）**：EdTech Innovation Hub 報導 Anthropic 開放美國中小學與學區免費使用 Claude for Teachers 企業版。延續 08-23 的 Claude Academy（面向一般大眾的免費課程＋企業導入指南），本次是教育普及路線的再進一步——從「課程」延伸至「免費開放企業版產品存取權」，且首度鎖定 K-12（非既有高等教育機構具名案例，見 [[topics/enterprise-tool-tracker]] 之 Duke／Syracuse／哈佛 FAS）；可能同時具備 IPO 前公眾敘事建設與未來付費轉換的教育市場布局雙重意涵（推論）；具體適用學區範圍、審核機制、是否設使用量上限均未見報導，僅標題可用。
- **Nscale（08-28）**：Forbes、Financial Times 報導 Anthropic 與英國新創 Nscale 簽署 450 億美元資料中心協議，取得 460 MW Vera Rubin 世代算力容量。是繼近期 AMD（08-05 自研晶片人才招募、07-22 投資協議）、Nvidia（既有算力供應關係）兩筆大型算力布局後，本頁第三筆標題明確以「重大基礎建設交易」框架描述的合作案，顯示算力鎖定策略持續向新興雲端算力供應商延伸（推論）；具體合約年期、Nscale 財務結構、Vera Rubin 世代硬體規格未見報導。
- **Claude 營收年增 1,000%（08-28，媒體獨家，未經證實）**：Yahoo Finance 獨家報導稱 Claude 營收年增達 1,000%，在企業市場對 ChatGPT 的差距持續縮小。**單一媒體獨家、無官方確認**，具體基期、統計口徑（ARR／季營收／哪個時間窗口）均未見報導，與本頁「現在的數字」表既有 ARR 數字（$65B，2026-07）口徑是否一致待查；不可直接與官方揭露數字並列比較，僅作市場信號記錄（推論，待官方或第三方獨立驗證）。
- **Meta（$100 億美元支出，08-28 補強）**：延續 08-27 NYT「亦敵亦友」報導，08-28 起後續報導補上具體金額——Meta 傳將於 Anthropic 支出達 100 億美元，與既有 07-17 的「Meta 洽談 100 億美元運算力租賃」金額相同，惟本則描述角度側重「Meta 支出」而非「租賃洽談階段」，可能為同一筆交易的後續進展或不同報導角度重申（推論，具體是否已從洽談階段推進至確定簽約未見報導）。
- **Salesforce（Claudeforce，08-26）**：Reuters、qz.com、CNBC 等多家媒體報導 Salesforce 與 Anthropic 深化合作，發布整合進 CRM 工作流的 AI 業務外掛「Claudeforce」；Salesforce 同時上修全年營收預測。是本頁首度出現「以具名產品命名方式深度綁定品牌」的合作案例，顯示 Salesforce 將 Claude 定位為核心 CRM AI 能力而非周邊外掛；CNBC 並取得 Salesforce 董事長暨執行長 Marc Benioff 與 Anthropic 共同創辦人暨執行長 Dario Amodei 接受 Jim Cramer 專訪逐字稿，顯示雙方高層親自為此合作背書（推論，具體商業條款、營收貢獻占比未見報導）。
- **CrowdStrike（08-27）**：Forbes 報導 CrowdStrike 股價單日上漲 13%，執行長將公司本季（史上最佳單季）表現部分歸功於與 Anthropic 的合作。是本頁首度出現「企業客戶財報＋股價雙重效應」明確歸因於 Anthropic 合作的具名案例，區別於既有多為「宣布合作」層級的訊號，顯示至少部分企業客戶已將合作實質轉化為可驗證的財務與市場表現（推論）；具體合作內容、對營收貢獻比例未見報導，僅執行長口頭歸因，非官方財報拆分數字。
- **Meta（亦敵亦友，08-27）**：紐約時報以「亦敵亦友」（frenemies）形容 Meta 與 Anthropic 關係：Meta 一邊公開批評 Anthropic，卻同時是其最大客戶之一。與既有 07-17 的 Meta 洽談 100 億美元運算力租賃（Anthropic 向 Meta 租算力）方向相反——本則指出 Meta 反過來是 Anthropic 產品的大客戶之一，顯示兩家公司間存在雙向且方向相反的商業依賴關係，同時 Meta 對外仍維持公開競爭批評姿態；具體 Meta 採用 Claude 的產品範疇、採購規模、與既有運算力租賃洽談的關係均未見報導（推論）。
- **Anthropic 澳洲市場（08-25）**：ABC News（澳洲廣播公司）報導有內部郵件揭露 Anthropic 在澳洲的 AI 佈局規模。延續 08-24 的 Bloomberg「Anthropic 表態指出澳洲在 Claude 程式開發工具採用速度上落後其他市場」，本則揭露內部規劃文件層級的澳洲布局，惟具體內容（資料中心、辦公室擴張或政府合作）未見報導，可能屬本頁戰略合作範疇，亦可能觸及 [[topics/anthropic-government-policy]] 政府合作面向，需後續報導查證後再判斷主要歸屬（推論）；僅標題可用。
- **未具名 AI 資安新創（08-25）**：Bloomberg 報導一家與 Anthropic、Google 合作的 AI 資安新創獲得 1.4 億美元融資。延續近期 Cyberhaven（07-23）、Orca Security（07-21）、Varonis（07-14）等資安夥伴生態擴張趨勢，本次首度出現「合作夥伴自身完成大型融資」作為生態健康度佐證訊號，惟新創公司名稱、合作具體內容均未見報導（推論）；僅標題可用，待後續補充具名。
- **Bastrop County 資料中心（08-25）**：KXAN Austin 引述消息人士報導 Anthropic 正洽談租用德州 Bastrop County（Cedar Creek）一座 2,842 英畝、含 710MW 燃氣電廠的資料中心園區，尚未定案。
- 已查證（2026-09-20）：**與 Morgan Stanley 案非同一設施**——Morgan Stanley 領投的 $150 億貸款案（08-02）對象是 Nexus Data Centers 在德州 Hubbard 的園區，地點、開發商均不同，兩案各自獨立（Google 為 Nexus 案提供信評擔保）。
- **UpToDate（08-24）**：Fierce Healthcare 於 Epic 年度用戶大會（Epic UGM）報導中提及 Anthropic 深化與醫療資訊平台 UpToDate 的合作，同篇報導並提及 Project Glasswing 相關進展。延續近期 Optum＋UST（07-14）、ICON（07-29）等醫療垂直產業深化案例，UpToDate 是又一起具名醫療資訊平台深化合作案例（推論）；Project Glasswing 部分屬安全模型能力面，詳見 [[entities/mythos]]；具體合作範疇、UpToDate 整合方式均未見報導，僅標題可用。
- **Claude Academy（08-23）**：EdTech Innovation Hub 報導 Anthropic 推出「Claude Academy」，提供免費 AI 課程與企業導入指南；首度以自身名義面向大眾推出免費課程，具體內容、涵蓋範圍未見報導，僅標題可用（推論）。
- 08-26 跟進（ababnews.com）已查證（2026-09-20）｜**ababnews.com 可信度**：為 ABAB Labs 旗下區塊鏈財經聚合平台，有 About／Contact 頁，非假新聞站，惟非專業 AI 媒體，屬轉載聚合。
- 本則僅轉載同一消息，未見新增細節，採信度維持低於 08-23 EdTech Innovation Hub 原始報導。
- **Casper Studios（08-20）**：crn.com、Seeking Alpha、The Information 三方同日報導：與 Anthropic 關聯的 AI 服務公司 Ode（見 07-16 的 Anthropic／Blackstone 合資 $15 億美元 AI 導入公司）收購顧問公司 Casper Studios。延續 07-15/16 的 Ode 定位論述——「下一個兆美元級 AI 商機在於實作，而非模型本身」，本次是 Ode 成立後首度公開的具名收購案，從「合資成立公司」進一步落實為「透過併購擴大導入服務能量」，若此模式延續，Ode 可能持續透過併購顧問/實作公司擴張版圖，直接進入 Accenture、TCS、DXC 等既有戰略夥伴業務領域（推論，延續 07-16 的潛在競合關係觀察）；具體收購金額、Casper Studios 規模與客戶基礎、整合時程均未見報導，僅標題可用。
- **Anthropic 關聯資料中心私募信貸（08-19）**：Yahoo Finance 報導一座與 Anthropic 相關的資料中心取得規模達 13 億美元的私募信貸（private credit）貸款。延續近期 TeraWulf（07-06，$19B 20 年租約）、Volta（08-04，$100 億美元）、Morgan Stanley（08-02，$150 億美元）等基礎設施擴張系列信號，本則首次出現以「私募信貸」（債務融資，區別於股權投資或雲端運算協議）形式直接為 Anthropic 關聯資料中心籌資的具名案例，顯示算力基礎設施融資管道正進一步向債務資本市場延伸（推論）；具體資料中心名稱、地點、承貸方、與 Anthropic 的合約關係（自建、租賃或合資）均未見報導，僅標題可用。
- **Decart（08-13起多輪跟進）**：Bloomberg、Reuters、Gizmodo 等多家媒體同日報導 Anthropic 正洽購世界模型 AI 新創 Decart，交易金額約 60 億美元；calcalistech 特別指出 Decart 為以色列 AI 新創。若成真將是 Anthropic 首度公開洽購「世界模型」（world model，區別於既有語言模型核心業務）新創的具名案例，可能代表產品線向多模態／物理世界模擬方向擴張的訊號（推論）；Hacker News 討論串（08-13）出現質疑聲音，部分留言認為此舉是為搶版面而非聚焦既有模型的成本與效能改善。具體交易條款、是否已簽署最終協議未見報導，僅屬洽談階段。08-14 跟進（延續報導，非新事實）：Yahoo Finance 確認交易仍在洽談階段、尚未定案，同一 $6B 數字；calcalistech 另發表分析文章解讀 Anthropic 為何願付此價碼，屬同一事件的分析視角，未見新增交易條款。08-16 跟進（單一來源，未經證實）：calcalistech 報導交易規模上修至約 70 億美元（此前 08-13/14 報導約 $60 億美元），並稱 Anthropic 在競價中先於 Nvidia 一步談成；此為單一來源消息，尚未見其他媒體佐證或官方確認，金額上修幅度與「先於 Nvidia 談成」的競價細節均待其他來源查證。08-23 跟進（分析文章，非新事實）：calcalistech 發表分析文章，主張若 Anthropic 順利完成 IPO，這筆 70 億美元交易的價值可能大幅升值；屬既有交易的估值後續分析視角，未見新增交易條款、進度或金額，僅標題可用。
- **Decart 交易生變（09-08）**：PYMNTS 首報 Anthropic 撤回收購計畫，同日 Bloomberg、calcalistech（兩則）、Ynetnews、Globes 密集跟進；calcalistech 一則標題暗示有分析撤回原因，惟僅標題可用，具體原因未見報導。
- **Riot Platforms（08-11）**：多家媒體報導 Anthropic 與加密貨幣礦業公司 Riot Platforms 簽署規模達 90 億美元、為期 20 年的雲端運算協議。延續近期 Volta（08-04，$100 億美元）、Morgan Stanley（08-02，$150 億美元）等基礎設施擴張系列信號，Riot Platforms 是又一家非傳統雲端商（加密貨幣礦業公司轉型算力供應）加入 Anthropic 算力供應鏈的具名案例，且合約期限長達 20 年，顯示 Anthropic 正鎖定長期穩定算力來源以因應持續擴張的運算需求（推論）；具體交易結構、生效時程未見報導，僅標題可用。
- **GIC（08-11）**：多家媒體報導 Anthropic 與新加坡主權財富基金 GIC 合作開發資料中心。與同日 Macquarie 合作並列，是 Anthropic 首度出現主權財富基金層級資料中心開發夥伴的具名案例，顯示其基礎設施融資管道正從傳統投行（Morgan Stanley）與科技公司延伸至主權基金（推論）；具體投資規模、資料中心地點未見報導，僅標題可用。
- **Macquarie（08-11）**：多家媒體報導 Anthropic 與澳洲金融集團 Macquarie 合作開發資料中心，延續 07-05 的澳洲 1.4GW 算力採購佈局（推論），是澳洲市場基礎設施合作的再一具名案例；具體規模、時程未見報導，僅標題可用。
- **Naver（08-11）**：KED Global 報導南韓 Naver 宣布投資 Anthropic 700 萬美元，作為調整 AI 策略、擴大全球聯盟佈局一環。相較既有 AMD（$50 億美元）、SK 集團等大型投資／供應鏈夥伴，Naver 投資規模明顯較小，性質上更接近策略聯盟訊號而非重大資本挹注（推論）；具體聯盟內容、股權比例未見報導，僅標題可用。
- **Robert Mahari（08-07）**：Legal IT Insider、Law.com（雙重來源確認）同日獨立報導 Anthropic 任命法律科技學者暨新創創辦人 Robert Mahari，出任新設立的「Claude for Legal」部門負責人。是 Anthropic 首度以具名部門形式進軍法律 AI 垂直市場的訊號，延續近期 Cognizant（07-28）、UST（07-10/14/20）等垂直產業深化模式，惟本次是內部設立專責部門而非與既有企業客戶合作深化（推論）；具體部門職掌、團隊規模、產品路線未見報導，僅標題可用，人物背景見 [[entities/robert-mahari]]。
- **Millennium（08-06）**：Yahoo Finance（三重來源確認）報導避險基金 Millennium 宣布與 Anthropic 合作開發 AI 風險分析師（AI risk analyst）工具。是繼 iCapital（金融服務採用，見 [[topics/enterprise-tool-tracker]]）、Nimble Gravity（銀行/保險顧問，05-27）之後，金融業（本次為避險基金）另一起具名採用案例，顯示 Claude 在金融風控垂直應用持續滲透（推論）；具體技術範疇、合約金額未見報導，僅標題可用。
- **AWS Continuum（08-05）**：AWS 官方宣布與 Anthropic、OpenAI 合作，將新推出的 AWS Continuum 導入開發者工作流程。延續既有 Enterprise Gateway（07-01，簡化 AWS/GCP 上的 Claude Code 存取）、AWS 治理功能（07-09）等雲端整合深化路線（推論），本次為 AWS 首度將 Anthropic 與 OpenAI 並列同一新產品的具名合作案例；具體 Continuum 功能範疇、技術細節未見報導，僅標題可用。08-11 跟進（VentureBeat，角度延伸，非新事實）：報導將 AWS Continuum 整合 Codex 與 Claude Code 定位為「大型 AI 資安舉措」一環，與 08-05 已記錄「開發者工作流程」框架不同，惟未見新增技術細節或合作條款，屬同一事件的不同媒體角度重述。
- **Volta（08-04起）**：TechCrunch 報導 Anthropic 與 AI 雲端運算新創 Volta 簽署規模達 100 億美元的運算協議；The Telegraph 補充 Volta 為僅成立八個月的英國新創；TipRanks 補充其獲 Nvidia 支持（三方報導同一事件，合併記錄）。
  - **2026-09-20 查證補齊**：合約為**六年期**，算力來自**挪威 Tydal** 一座與比特幣礦商 Bitdeer 合作、水力發電供能並搭載 Nvidia Vera Rubin 晶片的資料中心。
  - Volta 總部在英國，故媒體的「歐洲算力合約」與「英國新創」指同一件事（[TechCrunch](https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/)）。
  - 延續近期 Morgan Stanley（08-02，150 億美元德州資料中心投資）、TeraWulf（07-06，190 億美元 20 年租約）、Meta（07-17，潛在 100 億美元運算力租賃）等基礎設施擴張系列信號。
  - Volta 是又一起新興 AI 雲端運算商加入 Anthropic 算力供應鏈的具名案例，成立僅八個月即簽下十億美元級合約，反映採購對象持續向新興專營商擴散（推論）；具體交易結構、運算容量、生效時程未見報導。
- ⟨Q-02⟩ **已確認為同一筆 Volta 交易，非獨立新交易**（2026-09-20 查證）：
  - Volta 總部在**英國**、承載算力的資料中心在**挪威 Tydal**，故「英國新創」與「歐洲算力合約」指同一件事；「七個月 vs 八個月」是媒體對「founded earlier this year」的換算差異。
  - 合約條件一致：**六年期、100 億美元**（[TechCrunch](https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/)）。
- **SpaceX（08-04）**：TechCrunch 報導 SpaceX 財報揭露營收較去年翻倍，成長動能含與 Anthropic、Google 的運算合作及 Starlink 業務成長。顯示 SpaceX 已成為 Anthropic（與 Google）運算基礎設施供應鏈的一環，是繼 TeraWulf、Volta 等新興算力供應商後又一起非傳統雲端商參與 Anthropic 算力佈局的案例（推論）；具體合作內容、金額、SpaceX 提供之運算類型（資料中心電力、衛星鏈路或其他）未見報導，僅標題可用。
- **Google 近 2000 億美元融資機制（08-04）**：Financial Times 報導 Google 為 Anthropic 主導/牽線一項規模近 2000 億美元的華爾街融資機制（原文標題："Inside Google's $200bn Wall Street finance machine for Anthropic"）。延續近期 Morgan Stanley（08-02，$150 億美元資料中心投資案）、TeraWulf（07-06，$19B 20 年租約）、Meta（07-17/18，潛在 $100 億美元運算力租賃洽談）等基礎設施擴張系列信號，若屬實將是目前已知規模最大的單一金融安排，顯示 Google 除既有 $400 億美元直接投資（見 [[entities/google-investment]]）外，可能進一步扮演資本市場中介／促成者角色（推論）；具體交易結構（債權/股權比例）、參與銀行團、資金確切用途未見報導，僅標題可用，待後續補充。
- **Anthropic 印度市場（08-03）**：ndtv.com 報導 Anthropic 宣布擴大印度市場布局，稱 AI agent Claude 在當地「更加普及」（more accessible）。延續 07-13 印度盧比在地化定價（Pro 方案 Rs 2,000/月，見 [[entities/pricing]]）之後，是印度市場布局的進一步擴大信號；具體擴張內容（新辦公室、在地團隊、新功能、合作夥伴）未見報導，僅標題可用，待後續補充。
- **Morgan Stanley（08-02）**：thestreet.com 報導 Morgan Stanley 領投一項規模達 150 億美元、投向 Anthropic 德州校園/資料中心的投資案。延續近期 TeraWulf（07-06，$19B 20 年租約）、Meta（07-17/18，潛在 $100 億美元運算力租賃洽談）、澳洲資料中心採購（07-05，1.4GW）等算力/基礎設施擴張系列信號，Morgan Stanley 是又一起金融機構領投 Anthropic 實體資料中心建設的具名案例，顯示 Anthropic 算力自建佈局持續吸引大型金融機構參與融資（推論）；具體投資結構（股權/債權比例）、參與方細節、德州校園規模與時程未見報導，僅標題可用，待後續補充。
- **Amir Salek（08-21起，08-23 具名確認）**：Seeking Alpha 報導 Anthropic 延攬一名前 Google 晶片工程師，據報導是評估自研晶片（in-house solution）方案、跨入硬體領域的訊號；Bloomberg 同日獨立跟進報導同一事件（標題「Anthropic Taps Google Chip Veteran as Part of Push Into Hardware」，雙重來源確認）。延續既有 Samsung 代工洽談（07-02 起，媒體持續追蹤未升級）、AMD／Micron 晶片供應鏈投資合作路線，本次首見「內部招募晶片人才」訊號，顯示 Anthropic 可能不僅止於外部代工／供應鏈合作，亦在評估自研晶片路徑，與 Google（TPU）、Amazon（Trainium）等雲端夥伴的自研晶片模式相似（推論）；具體職位、團隊規模、時程未見報導，僅標題可用。08-23 具名確認：The Times of India 報導確認該工程師身分為 Amir Salek，Google 自研晶片計畫（custom chip programme）創辦人——即 Google TPU 專案的創始人物之一。從「未具名前員工」升級為「創辦人層級具名人才」，招募對象的資歷等級遠高於一般工程師，顯示 Anthropic 自研晶片布局的企圖心可能不僅止於組建團隊，而是延攬曾成功打造 Google 整條自研晶片專案的核心創始人才，招募規格與 Google（TPU）、Amazon（Trainium）路線的可比性因此提高（推論）；**後續（2026-09-06）：** Bloomberg 載明 Salek 2013–2022 創辦並領導 Google TPU 專案（前七代），加入後進 compute 團隊、向 James Bradbury 匯報，到任日未公開；人才流動對戰力與市場意涵之完整分析詳見 [[topics/ai-talent-flow]]。08-24 跟進（citybiz，非新事實）：citybiz 轉載同一事件，未見新增職位、時程或團隊規模細節，僅為既有 08-21/08-23 記錄的又一媒體重述。

---

## 這些數字是誰說的

| 訊號 | 說明 | 來源 | 來源等級 |
|------|------|------|------|
| Anthropic 與 Accenture 合計承諾五年至少 10 億美元於內嵌評估能力建設（Anthropic 直接資助 Accenture 的工作）| 選定 Accenture 為首位獨立評估前沿 AI 安全的「內嵌評估者」，回應 CEO「We Must Pace the Frontier」一文承諾；非排他，官方稱未來數週再宣布其他評估者 | [Anthropic Blog](https://www.anthropic.com/news/accenture-embedded-evaluation)，2026-09-18（查證 2026-10-03）| 官方一手 |
| Anthropic 啟動 500 萬美元身心福祉評測獎助計畫 | 官方部落格：資助獨立研究團隊開發開源評測工具，衡量 AI 對使用者身心福祉的影響 | [Anthropic Blog](https://www.anthropic.com/news/wellbeing-research-grants)，2026-08-26 | 官方一手 |
| Raleigh 合資企業招聘，最高職缺薪資逾 **60 萬美元** | Business Journals 報導 Anthropic 旗下合資企業招聘 | Google News/The Business Journals，2026-08-15 | 一級媒體 |
| Nvidia 對 Anthropic 等公司合計約 700 億美元投資 | Yahoo Finance 分析潛在股東回報，非新增融資事件 | Google News/finance.yahoo.com，2026-08-12 | 第三方研究 |
| Economic Futures Research Fund：承諾 2 億美元支持外部研究 | 聚焦勞工衝擊、AI 轉型輔助、所得支持現代化等五大方向 | Anthropic Blog，2026-07-23 | 官方一手 |

%% 維運備忘：本表與「現在的數字」不重複寫數值；累積封頂 20 列，三頁（anthropic-ipo／-partnerships-compute／-business-risks）各自計，滿了汰除來源日期最舊者。 %%

**這些數字是誰說的·細節**
- **身心福祉評測獎助計畫**：官方部落格公告：受獎助研究人員將完全獨立作業，開發開源評測工具衡量 AI 對使用者身心福祉的影響，成果以開源專案釋出。屬公益/CSR 性質研究資助，非新功能或商業合作，與既有 Economic Futures Research Fund（$2 億美元，07-23，聚焦經濟政策研究）、Claude Corps（$1.5 億美元非營利培力）同屬對外部研究/公益資助的軟性佈局路線，惟本次聚焦身心福祉評測工具開發（推論）；具體受獎助對象、審核機制、單筆金額未見公告細節。
- **Raleigh 合資企業招聘**：Business Journals 報導 Anthropic 旗下合資企業（原文標題涉及「Claude」AI 採用相關業務）正在 Raleigh 招聘，其中一個職位薪資逾 60 萬美元；具體合資企業名稱、職位類型、整體招聘規模均未見報導，僅標題與導言層級資訊，反映公司持續擴大人才投資規模（推論）。
- **Nvidia 約 700 億美元投資分析**：Yahoo Finance 分析 Nvidia 對包含 Anthropic 在內多家 AI 公司合計約 700 億美元的投資，評估對 Nvidia 股東的潛在回報；屬第三方投資分析，非新增融資事件，僅標題可用，具體投資結構、Anthropic 分得金額未見報導。
- **Economic Futures Research Fund**：Anthropic Blog 公布研究議程，聚焦勞工衝擊、AI 轉型輔助、所得支持現代化、工作者在 AI 成長中的持股五大方向；原文：「We're committing $200 million to the fund to support ambitious external research on interventions to prepare society for the economic impacts of AI.」屬對外部研究的資助承諾，非公司內部融資或商業合作，性質與 Claude Corps（$1.5 億美元非營利培力）同屬經濟政策軟性佈局路線，但聚焦研究資助而非人才派遣（推論）；具體受助機構、審核機制未見報導。

---

## 時序

### 2026-11

#### 2026-11-02
- **[戰略合作] Google News：Johns Hopkins 大學癌細胞圖譜技術獲選用於 Anthropic AI 專案**：具體應用細節未揭露，見上方「其餘合作」清單（Google News/Johns Hopkins University）

#### 2026-11-01
- **[戰略合作] The Next Web 引 Stratechery：Palantir CTO 公開表示不後悔與 Anthropic 合作**：呼應既有資料外洩疑慮限縮使用範圍報導，訪談細節未附，僅標題可用（Google News/The Next Web）

### 2026-10

#### 2026-10-30
- **[戰略合作] Reuters 引《The Information》：Nvidia 洽談為 Nscale 與 Anthropic 間雲端合約提供信用支持**：背景為既有 Nscale 兩筆合計約 900 億美元算力交易（見「算力與資金從哪來」表），具體金額與條件未見報導，僅標題可用（Google News/Reuters）

#### 2026-10-29
- **[重大事件] Anthropic：AI for Science 擴大至 20 個基金會與研究機構，提供免費 Claude 額度**：涵蓋生物、醫學、物理、化學、氣候科學與數學，詳見「哪個合作」清單新增列（Anthropic）
- **[戰略合作，僅標題可用] The Paypers：荷蘭金融科技公司 Mollie 推出 AI plugins 與 MCP server，供 Claude 與 ChatGPT 使用**：具體功能與計費未見報導，詳見「哪個合作」清單新增列（Google News/The Paypers）

#### 2026-10-28
- **[重大事件] Anthropic／FedScoop：GSA 擴大 OneGov 協議，Claude Enterprise／for Government／API 折扣提升至 40%，首度涵蓋全部採購管道並延伸至州地方部落屬地政府**：詳見「哪個合作會改到你用的 Claude」表新增列（Anthropic；Google News/FedScoop；Hacker News）
- **[重大事件] Anthropic 官方：生命科學團隊公開近況，與 BigHat、BMS、Divergence Labs、Enveda、Generate Biomedicines、The Column Group 六組織展開藥物開發合作**：詳見「哪個合作」清單新增列（Anthropic；HN 294 分）
- **[戰略合作] Endpoints News／R&D World：Anthropic 收購一人神秘生技新創 Mithril Medicine**：匿名 Twitter 用戶經營的潛伏式新創，詳見「哪個合作」清單新增列（Google News/Endpoints News；R&D World）
- **[戰略合作，僅標題可用] Reuters／Law.com：Anthropic 推出「Claude for Legal Artifacts」法律工具組**：延續 08-07 設立 Claude for Legal 部門（[[entities/robert-mahari|Robert Mahari]]），詳見「哪個合作」清單新增列（Google News/Reuters；Law.com）
- **[戰略合作，僅標題可用] Yahoo Finance：資安治理平台 Lumia Security 整合 Claude Compliance API**：延續 Surf AI、Cyberhaven、Orca Security 等資安夥伴生態擴張模式，詳見清單新增列（Google News/Yahoo Finance）

#### 2026-10-27
- **[戰略合作] Reuters：華爾街銀行與 Blackstone 安排 630 億美元融資，供應 Anthropic 向 Broadcom 採購 AI 晶片**：詳見「算力與資金從哪來」表 Broadcom／Blackstone 列更新（Google News/Reuters）

#### 2026-10-26
- **[戰略合作] SpaceX 再借 400 億美元，Anthropic 的運算合作被點名為關鍵因素**：Barron's 報導，具體牽連機制未見細節（Google News/Barron's）

#### 2026-10-24
- **[重大事件] RIABiz：Charles Schwab 原宣布全數 1.6 萬家 RIA 可用 Claude，現追加 20 席企業採購下限，逾 1.1 萬家小型顧問公司被排除資格**：時間點卡在 IMPACT 2026 大會前，詳見「哪個合作會改到你用的 Claude」清單 Schwab／Orion 列更新；何時新增門檻未見報導（Google News/RIABiz）

#### 2026-10-23
- **[戰略合作] Anthropic Blog／Simon Willison：將 Agent Skills 開放標準捐贈予新設 Agentic AI Foundation（AAIF）**：官方稱已有逾 70 平台整合（含 ChatGPT、Cursor、Copilot、VS Code），治理權轉移後相容性未見報導（[Anthropic Blog](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)；Blog/Simon Willison）
- **[戰略合作，僅標題可用] Financial Times／SQ Magazine：Anthropic 與私募基金 Hg 合作，於歐洲推出 AI 顧問服務供當地企業導入 AI**：合作細節與服務範疇未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/Financial Times；Google News/SQ Magazine）
- **[戰略合作，僅標題可用] Google Cloud 官方部落格：宣布擴大 Claude 在該平台的可用性與部署選項**：具體新增區域或服務細節未見報導（Google News/Google Cloud）

#### 2026-10-21
- **[政府採購，僅標題可用] FedScoop：HHS 將對 Anthropic 做出「唯一來源」聯邦採購決定，提前於更廣泛 AI 採購競標程序**：具體金額、範疇與官方公告均未見報導（Google News/FedScoop）

#### 2026-10-20
- **[戰略合作] AWS 官方部落格：Amazon Bedrock 上的 Claude 模型新增結構化輸出（structured outputs）支援**：開發者可望省去額外輸出格式校驗邏輯，細節以官方文件為準，詳見「哪個合作會改到你用的 Claude」表 Amazon Bedrock 列（Google News/Amazon Web Services (AWS)）
- **[重大事件] CNBC／Reuters／Bloomberg：Anthropic 傳與 Nscale 洽談第二筆雲端合作，規模同樣約 450 億美元，尚未定案**：首筆見「哪個合作」清單 08-28 列，本次為獨立第二筆，條款與時程未見報導（Google News/CNBC；Reuters；Bloomberg.com）

#### 2026-10-17
- **[戰略合作，僅標題可用] Financial Times／Yahoo Finance：Anthropic 在最新一輪晶片融資交易中，向 Blackstone 提供兩位數殖利率**：具體利率、金額與交易條件未見報導，詳見「算力與資金從哪來」表新增列（Google News/Financial Times；Google News/Yahoo Finance）

#### 2026-10-16
- **[戰略合作] Anthropic Blog／Global News／CBC：EverWind 在加拿大新斯科舍省興建的大型資料中心將供電予 Claude**：規模、金額與上線時程未見報導，詳見「算力與資金從哪來」表新增列（Google News/Global News；Google News/CBC）

#### 2026-10-14
- **[戰略合作，官方一手] Anthropic 在新加坡開設亞太區第五個辦公室，並與新加坡數位發展與資訊部簽署 MOU**：官方點名 GovTech Singapore、Grab、DBS 為既有 Claude 使用方，具體採用規模與產品線未見報導，詳見「哪個合作會改到你用的 Claude」一行制清單（Anthropic Blog）
- **[戰略合作，僅標題可用] Tenth Revolution Group 取得 Anthropic Claude Partner Network「Select」夥伴資格**：延續近期 Fabric、IPC Global、Nimble.LA、Intuitive.ai 同系列夥伴認證公告，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/HRTech Series）

#### 2026-10-13
- **[併購，僅標題可用] CTech：Amazon 可能以 55 億美元收購 Decart，稱 Anthropic 已退出該筆收購談判**：具體退出原因、交易條款與結案時程均未見報導（Google News/CTech）

#### 2026-10-10
- **[戰略合作] WSJ：共同創辦人 Tom Brown 利用共和黨人脈牽線促成每月 $12.5 億 SpaceX 運算容量交易**（Hacker News 135 分）：繼 Broadcom 晶片租賃融資案後又一筆牽動算力到位時程的資金動作，詳見「算力與資金從哪來」表 SpaceX 列更新；WSJ 原文付費牆，僅標題與 HN 摘要可用（Hacker News/WSJ）

#### 2026-10-08
- **[戰略合作，僅標題可用] DevOps.com：Aditi Consulting 達成 Anthropic「Select Tier」夥伴資格**：稱已在自家業務與客戶環境全面導入 Claude 投入生產，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/DevOps.com）
- **[戰略合作，僅標題可用] PR Newswire：Hexaware 成為 Anthropic Preferred Partner**：將 Claude 導入其 AI-native 平台核心，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/PR Newswire）
- **[戰略合作，僅標題可用] Techzine Global：OutSystems Agent Experience 開放支援 Claude Code 與 Cursor**：具體整合範疇未見報導，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/Techzine Global）
- **[戰略合作，僅標題可用] TradingView：Anthropic 承諾投入 1.5 億美元支持美國 AI 科學研究計畫**：受益對象、執行方式與時程均未見報導（Google News/TradingView）
- **[戰略合作，僅標題可用] ET Entrepreneur：Anthropic 向印度新創提供最高 $7,000 美元 Claude credits**：資格門檻與領取時效未見報導，與既有 Claude Startups 計畫（見 [[entities/pricing]]）關係未載（Google News/ET Entrepreneur）

#### 2026-10-07
- **[戰略合作] The Next Web／9to5Mac：xAI 旗下 Grok Bot 整合 Anthropic Claude、Midjourney、Suno 模型**：範疇與計費未見報導（2026-10-24 查證：僅見 Musk 在 X 的計畫，Anthropic 無聲明），見「哪個合作會改到你用的 Claude」（Google News/The Next Web；9to5Mac）
- **[戰略合作] TechPowerUp：三星晶圓代工將以 2 奈米製程生產 Anthropic 設計 AI ASIC 晶片**：較 07-02／07-06 代工洽談階段具體化，詳見「算力與資金從哪來」新增列（Google News/TechPowerUp）
- **[戰略合作，僅標題可用] Yahoo Finance／GlobeNewswire：Anthropic 將 Intuitive.ai 列為 Claude Partner Network 優先夥伴**：資格門檻與具體權益未見報導，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/Yahoo Finance；Google News/GlobeNewswire）

#### 2026-10-05
- **[戰略合作，僅標題可用] Channel Dive：Anthropic 與 AWS 攜手加碼推動 Frontier Deployed Engineers（FDE）方案**：延續 10-02 Claude Frontier Academy 培訓計畫，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/Channel Dive）

#### 2026-10-04
- **[戰略合作，僅標題可用] Barchart：SpaceX 與 Anthropic 簽署大型 AI 運算合作**：報導聚焦對 SpaceX 股票（SPCX）影響，合作方向、金額與算力規模均未見報導（Google News/Barchart.com）

#### 2026-10-02
- **[戰略合作，官方一手] Anthropic 推出 Claude Frontier Academy：投入 1 億美元，2027 年底前培訓 10,000 名「Frontier Deployed Engineers」**：學員自 Claude Partner Network 成員遴選，首批含 Accenture、Deloitte、McKinsey（Anthropic Blog；CNBC）
- **[戰略合作] Frontier Academy 的名單與媒體讀法**：首批另有 Bain、Capgemini、澳洲聯邦銀行、Morgan Stanley、Novo Nordisk；Business Insider 稱補企業 AI 落地缺人，Benzinga 點出公司接近預期 IPO，CRN 專訪 Steve Corfield（Business Insider；Benzinga；CRN）
  - **訊 2026-10-05**：AI Magazine 分析文章延續同一則培訓計畫，指其反映業界工程人才缺口；未見新增金額或名單細節，屬既有事實的分析視角（Google News/AI Magazine）。
  - **訊 2026-10-05（AWS 角度）**：Channel Dive 報導 Anthropic 與 AWS 攜手加碼推動 Frontier Deployed Engineers（FDE）方案，延續本則 Partner Network 培訓計畫；具體 AWS 分工、資源投入未見報導，僅標題可用（Google News/Channel Dive）。
- **[生態合作] Blocks & Files：Commvault AgentRecover 支援探索、保護並還原 Claude Cowork、Claude Code 的 agent 設定與累積脈絡**：換機或遺失筆電時不必重建，詳見「哪個合作會改到你用的 Claude」一行制清單（Google News/Blocks & Files）
- **[戰略合作] TechRepublic：Claude for Government 全面開放，美國聯邦機構可直接採用（GA）**：延續 09-11 持續拓展聯邦文職機關採用、09-09 Fable 5.1 進 FedRAMP High 版後續，具體機關名單與採用規模未見報導，僅標題可用（Google News/TechRepublic）

#### 2026-10-01
- **[戰略合作，已查證] Claude for Government 09-30 對聯邦與州政府機關 GA**：FedRAMP High；無席次費，按固定額度購買用量並設不可超過的上限；Claude Code CLI 與 Claude for Microsoft 365 搶先體驗（[官方](https://claude.com/blog/claude-for-government-is-now-generally-available)，查證 10-03）
- **[戰略合作] Barclays 擴大導入 Claude Code 全行，目標 2026 年底開發者採用率達 50%**：2027 年擴及多數工程師，完整規模見 [[topics/enterprise-tool-tracker]]（Anthropic Blog；Bloomberg；PYMNTS）
- **[戰略合作，僅標題可用] The Decoder：Anthropic 持續拓展聯邦文職機關採用，五角大廈供應鏈風險認定爭議未解**：具體機關名單與規模未見報導；供應鏈風險認定與判決細節見 [[topics/anthropic-government-policy]]（Google News/The Decoder）
- **[生命科學布局，僅標題可用] Endpoints News：專訪 Anthropic 生命科學團隊，談酶研究、生物實驗室與臨床前管線**：報導時機與近期類 CRISPR 酶系統歸屬爭議相近，具體內容未見報導，詳見 [[entities/claude-science]]（Google News/Endpoints News）

### 2026-09

#### 2026-09-30
- **[戰略合作，官方一手來源] AWS 官方部落格：Amazon Bedrock 新增首爾、新加坡境內推論**：企業客戶資料可留在當地處理，詳見「哪個合作會改到你用的 Claude」表 Amazon Bedrock 列更新（Google News/Amazon Web Services (AWS)）
- **[生態合作，僅標題可用] EIN News：Pureinsights Discovery 2.12 新增 Claude 整合，涵蓋文件擷取與查詢管線**：具體功能與計費未見報導，詳見「哪個合作會改到你用的 Claude」一行制清單新增列（Google News/EIN News）

#### 2026-09-29
- **[戰略合作] Fierce Healthcare：OpenEvidence 偕 Penn Medicine 擴大合作，將醫師 AI 取得管道推向非洲、亞洲**：與 09-22 已記錄之 OpenEvidence 結盟同一事件後續，詳見「哪個合作會改到你用的 Claude」清單更新（Google News/Fierce Healthcare）
- **[戰略合作] Bloomberg：避險基金 ExodusPoint 加入與 Anthropic 合作的機構陣容**：具體技術範疇與商業條款未見報導，詳見一行制清單新增列（Google News/Bloomberg.com）
- **[公司動態，僅標題可用] The Boston Globe：地方媒體角度回顧 Anthropic-Akamai 合約對波士頓地區經濟的影響**：未見新增合約細節，屬 09-25 已記錄事件的地方媒體延伸報導（Google News/The Boston Globe）

#### 2026-09-28
- **[生態合作] 官方推出 Claude Marketplace，收錄逾 2,000 個 connector 與 plugin；同日 Fabric 加入 Claude Partner Network**：具體合作範疇與計費均未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/gHacks；Google News/EIN News）

#### 2026-09-26
- **[戰略合作，跟進] Yahoo Finance：分析 Accenture 能否把加入 Anthropic AI 安全評測合作轉化為新營收線**：與 09-19 已記錄之 Accenture 內嵌評估者合作屬同一事件，本則新增「評測服務能否商業化」角度，具體營收數字未見報導（Google News/finance.yahoo.com）

#### 2026-09-25
- **[生命科學布局，跨頁關聯] the-scientist.com 揭露 Anthropic 保密中的「AI 驅動濕實驗室」**：即 09-24 公布之 CRISPR 特徵酶系統發現的來處；與本頁 09-18 起記錄的自有生物實驗室應屬同一設施，原文未逐字確認。發現細節與科學界評價見 [[entities/claude-science]]（the-scientist.com）
- **[戰略合作] Bloomberg：Anthropic 與 Akamai 簽署 7 年、116 億美元運算合約，取得 CPU 算力**：認股權證可認購約 770 萬股 Akamai 股票，另有報導以「120 億美元」總值呈現；詳見一行制清單（Hacker News；Google News/WSJ；Reddit）

#### 2026-09-24
- **[戰略合作] BioSpace：AI 製藥新創 Basecamp 獲 NVIDIA、Anthropic 領投 1.4 億美元融資**：用於推進 AI 輔助藥物設計，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/BioSpace）
- **[戰略合作] 9to5mac.com：Adobe 把 Acrobat 帶進 Claude 生態，同批對 Google Gemini 開放存取**：具體整合範疇與計費未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/9to5mac.com）

#### 2026-09-23
- **[戰略合作] Reuters 獨家：Anthropic 與醫療 AI 服務 OpenEvidence 結盟，推向全球醫療 AI 服務**：合約範疇與費用未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/Reuters；PYMNTS）
- **[戰略合作] GeekWire／About Amazon：Amazon 開放賣家工具予外部 AI 代理人，首波合作對象為 Claude**：同步升級 Seller Assistant 並推出結合 Amazon Quick 與 Claude 的新外掛，具體功能與計費未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/GeekWire；About Amazon）
- **[資本支出，僅標題可用] The Information：Anthropic 洽談加強對更多資料中心的控制權**：具體規模、對象未見報導（Google News/The Information）

#### 2026-09-22
- **[戰略合作，僅標題可用] Yahoo Finance：Palo Alto Networks 推出結合 Claude、GPT 模型的 AI 資安服務**：具體整合規模與費用未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列（Google News/Yahoo Finance）

#### 2026-09-21
- **[資本支出] Bloomberg：Nscale 總值 1,030 億美元資料中心合約中，Anthropic 與 Microsoft 為最大兩家客戶**：首度揭露 Nscale 整體合約規模與客戶排名，此前僅知 08-28 Anthropic 自身一筆 450 億美元；詳見「哪個合作會改到你用的 Claude」清單 Nscale 條目更新（Google News/Bloomberg.com）
- **[生命科學布局，僅標題可用] Channel 3000／80 Level 跟進 09-18 已記錄之自有生物實驗室報導：Anthropic 設立生物實驗室，加速 AI 驅動藥物開發**：未見新增細節，與 09-19 TechCrunch／Yahoo Finance 同屬同一事件的持續媒體擴散（Google News/Channel 3000；Google News/80 Level）
- **[戰略合作，僅標題可用，單一來源] The Information：OpenAI 與 Anthropic 傳一度接近達成協議，擬互相對彼此 AI 模型做壓力測試**：具體條款、是否已簽署、測試範疇均未見報導，單一消息來源，細節待證實（Google News/The Information）

#### 2026-09-19
- **[重大事件] Anthropic 宣布 Accenture 出任首位「內嵌評估者」，獨立評估前沿 AI 安全；Washington Post 稱同步承諾投入 10 億美元資金，呼應 CEO「We Must Pace the Frontier」一文承諾**（Anthropic Blog；Google News/The Washington Post）
- **[生命科學布局] TechCrunch、Yahoo Finance 跟進 09-18 已記錄之自有生物實驗室報導：Anthropic 建置專屬濕實驗室，作為 AI 驅動藥物開發計畫一環**（Google News/TechCrunch；Google News/Yahoo Finance）

#### 2026-09-18
- **[生命科學布局] 官方：推出生命科學驗證計畫（LSVP），開放生醫專業人士使用 Mythos、Opus、Sonnet 並放寬部分安全限制，先以機構／團隊 Beta 開放**（Anthropic Blog）
- **[生命科學布局] Reuters 獨家＋qz.com 跟進：Anthropic 悄悄設立自有生物實驗室（wet lab），加速 AI 藥物開發**（Google News/Reuters；Google News/qz.com）
  - 後續（2026-09-26）：[[entities/claude-science]] 記錄的 CRISPR 特徵酶系統發現，出自此濕實驗室首度曝光成果，應屬同一設施，原文未逐字確認。
- **[資本支出] CNBC 引述消息人士：Anthropic 與 OpenAI 同步尋求規模較小的資料中心合作案，加快 AI 運算產能部署**（Google News/CNBC）

#### 2026-09-17
- **[生命科學布局] 官方部落格：說明 Claude 在生物分子建模的應用進展，與同期生命科學布局同源**（Google News/Anthropic，跨來源數 3）
- **[基礎設施，僅標題可用] TechCrunch：Google、Nvidia、Anthropic 支持 Emerald AI，為更多資料中心在電網找空間**：具體投入規模、合作條件均未見報導

#### 2026-09-16
- **[戰略合作] Reuters／Bloomberg／WSJ／politico.eu：Novo Nordisk 與 Anthropic 合作，用 Claude 加速藥物研發**：四家媒體同步報導（Ozempic 藥廠），合約範疇與費用未見報導，詳見「哪個合作會改到你用的 Claude」清單新增列
- **[基礎設施] finance.yahoo.com：Anthropic 簽署首份澳洲資料中心協議**：資料中心版圖首次擴及大洋洲。媒體稱（Real Estate Source、Converge Digest、ABC，2026-10-03 查證）首期租約位於昆士蘭 Western Downs Digital Park
  - 媒體稱該園區由 Zerra DC 開發、Macquarie Capital 與 Dexus 參與，園區峰值 2.16GW、總額約 319 億屬園區開發規模，**不是 Anthropic 的承諾金額**；Anthropic 官方站未載此協議（僅 2026-03-10 雪梨辦公室公告稱「探索」資料中心）

#### 2026-09-15
- **[戰略合作] Reuters 等 7+ 家財經媒體：Anthropic 定名並推出「Claude for Financial Advisors」**：延續 09-14 記錄之 Schwab／Orion 導入，詳見「哪個合作」清單 Schwab／Orion 條目（FF News、InvestmentNews、AdvisorHub 等跟進）
- **[分析評論] RIABiz：分析師對 Schwab 卡位效果意見分歧**：一派稱藉獨家合作卡位 RIA 通路「AI 駕駛座」，另一派批評方案通用、進場不算早，費率與合約期限未見報導（Google News/RIABiz）

#### 2026-09-14
- **[戰略合作] Bloomberg／Business Wire／Yahoo Finance：Charles Schwab、Orion 同日宣布導入 Claude，鎖定 RIA 通路**：跨入財務顧問通路，具體合約條件、費率未見報導，僅標題層級可用
- **[公司動態，僅標題可用] ChannelE2E：Claude 合作夥伴訓練計畫新增安全性相關認證課程**：具體課程內容、通路夥伴規模未見報導

#### 2026-09-10
- **[戰略合作，已查證] Fable 5.1 已進 FedRAMP High 版 Claude for Government**：公共部門負責人 Teresa Carlson 證實；Desktop（含 Claude Code、Cowork）數週內轉正式，金額未揭露（FedScoop 2026-09-09；查證 09-26）

#### 2026-09-09
- **[戰略合作] Crowdfund Insider：Anthropic 推出 Claude Commerce Agents，與 Visa、Mastercard 建立合作關係**：詳見「哪個合作會改到你用的 Claude」一行制清單新增列（Google News/Crowdfund Insider）
- **[戰略合作] citybiz：LoanPro 採用 AWS＋Claude AI 原生客服介面，通話時間最多縮短 15%**：詳見一行制清單新增列（Google News/citybiz）
- **[戰略合作] Aviation Week：跟進報導 Amadeus 與 Anthropic 合作**：與 09-03 已記錄事件為同一合作案，未見新增整合範疇，詳見一行制清單 Amadeus 列（Google News/Aviation Week）
- **[戰略合作] Demand Gen Report：Salesforce 與 Anthropic 擴大 Claudeforce 合作**：與 08-26 已記錄之 Claudeforce 發布為同一合作線的擴大報導，具體擴大範疇未見報導，詳見一行制清單 Salesforce 列（Google News/Demand Gen Report）

#### 2026-09-08
- **[戰略合作] PYMNTS 等多家媒體：Anthropic 撤回收購以色列新創 Decart 計畫**：原擬以約 60–70 億美元收購，09-08 傳出計畫遭撤回，以色列與國際財經媒體同日密集跟進，具體原因未見報導，詳見「哪個合作會改到你用的 Claude」一行制清單（PYMNTS；Bloomberg；calcalistech；Ynetnews；Globes）

#### 2026-09-07
- **[戰略合作] Currently.com：Anthropic 對 AWS 承諾金額已逾 1,000 億美元，招股書可能揭露更多合約細節**：屬前述 5,170 億美元總額中的單一夥伴分項，詳見「現在的數字」表細節（Google News/Currently.com）
- **[戰略合作] AI Magazine：Fluidstack 主導 Anthropic 一筆 500 億美元算力建置案**：詳見「哪個合作會改到你用的 Claude」一行制清單新增列（Google News/AI Magazine）
- **[戰略合作，推論] Yahoo Finance：Hut 8 藉 350 億美元 Anthropic 合作案加速 AI 業務轉型**：金額與地點描述與 09-01 已記錄之 Lambda 交易相符，推論為同一筆，尚待其他來源確認，詳見「哪個合作會改到你用的 Claude」Lambda 細節（Google News/Yahoo Finance）

#### 2026-09-03
- **[戰略合作] Skift：Amadeus 將旅遊科技整合進 Claude Code 與 Cowork**：詳見「哪個合作會改到你用的 Claude」表新增列（Google News/Skift）

#### 2026-09-02
- **[戰略合作，官方一手來源] Anthropic 官方部落格：推出 Enterprise Frontier Safeguards（EFS，公告日 09-01）**：結合零資料留存（ZDR）與濫用偵測技術，**EFS 免費**，今秋起分階段開放；由 100+ 企業客戶共同開發，並與 AWS、Google Cloud、Microsoft Azure 合作，詳見「哪個合作會改到你用的 Claude」表新增列與細節（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)；csoonline.com；SecurityWeek）
- **[戰略合作] AWS 官方部落格：Claude Fable 5.1 上線 AWS 平台**：雲端夥伴角度公告，詳見「哪個合作會改到你用的 Claude」表新增列（Google News/Amazon Web Services (AWS)）

#### 2026-09-01
- **[戰略合作] 多家媒體：Anthropic 與 Lambda 簽署 350 億美元雲端運算合約**：Lambda 為 Nvidia 支持之雲端業者，資金牽涉德州一座由比特幣礦商營運的資料中心園區；延續本頁近期密集的算力布局系列（Nscale $450 億、Riot Platforms $90 億、Volta $100 億等），詳見「哪個合作會改到你用的 Claude」表新增列（多家媒體，2026-09-01）
- **[戰略合作] crn.com：Claude 認證累計 8.5 萬張，Anthropic 擬擴大夥伴培訓規模**：延續既有 DXC（06-12，訓練數萬名認證工程師）、Cognizant（07-28，Global Premier Partner 認證人才梯隊）等培訓型合作訊號，本次首見公司層級累計認證數字，詳見「哪個合作會改到你用的 Claude」表新增列（Google News/crn.com）
- **[戰略合作] Morningstar：Trifecta Technologies 與 Anthropic 合作導入 Claude 服務**：詳見「哪個合作會改到你用的 Claude」表新增列（Google News/Morningstar）

2026-08 以前的條目見 [[topics/anthropic-business#時序]] 的時段總結。

---

## 相關

- [[topics/anthropic-business]]：母頁，指標表與子線路由
- [[topics/anthropic-ipo]]：上市與財報（S-1 揭露的算力承諾）
- [[topics/anthropic-business-risks]]：風險與商業模式
- [[entities/pricing]]：通路怎麼定價、怎麼開票
- [[entities/google-investment]]：Google 投資的完整脈絡
- [[topics/market-signals-compute]]：算力與融資消息的判讀
- [[topics/market-signals-customers]]：通路與客戶消息的判讀
