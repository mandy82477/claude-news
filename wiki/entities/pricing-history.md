---
page: "entities/pricing-history"
kind: "entity"
type: "policy"
status: "active（持續調整中）"
domain: "💼 商業"
last_updated: "2026-11-07"
last_news_update: "2026-11-07"
status_main: "active"
days_since_news: 0
parent: "entities/pricing"
children: "[]"
page_role: "child"
days_since_news_subtree: 0
inbound_links: 2
attribution_count: 1
attribution_last: "2026-11-07"
top_source: "official-docs"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 計費沿革：價格、方案與促銷怎麼變過來

Claude 的價格、方案與促銷是什麼時候、怎麼變的，以及最近三個月哪幾件改到你的帳單——現在生效的規則與牌價在 [[entities/pricing]]。

**類型：** policy
**狀態：** active（持續調整中）
**領域：** 💼 商業
**上層：** [[entities/pricing]]
**首次出現：** 2026-04-25
**最後更新：** 2026-11-07
**最後新聞更新：** 2026-11-07

> **最新動態**（2026-11-07）
> - [官方 usage credits 說明頁](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) 大改版：新增帳戶刪除不退額度、auto-reload 措辭改寫；移除日本等地區 6 個月到期條款原文，新規則待查證。

---

## 最近三個月變了什麼

官方已確認、會改到帳單的，新的在上；每條的現行規則住母頁，這裡只記什麼時候變。⚠️＝不必你操作就會改到帳單。

- **11-07｜usage credits 說明頁大改版**：帳戶刪除不退額度、auto-reload 措辭改寫；移除日本等地區 6 個月到期條款原文，新規則待查證。見 [[entities/pricing#當前生效的計費規則]]
- **11-02 查證｜方案改名與附帶 API credits**：$200 一檔現名 Ultra（每週 Pro 的 10 倍用量、驗證帳號無 5 小時上限）；Max／Ultra／Team 每月附 $100／$200／最多 $500 API credits，不付 Claude Code。見 [[entities/pricing#我的方案現在有什麼]]
- **10-30｜Opus 4.8 fast mode 宣告淘汰，11-30 移除** ⚠️：之後請求直接回錯誤、不退回標準 Opus 4.8；同批 Opus 5.5 fast mode 不再限第一方 API。見 [[entities/pricing#乘數：會互相疊乘]]
- **10-30｜Enterprise／API 可依承諾支出談客製折扣**（門檻未公開）。見 [[entities/pricing#當前生效的計費規則]]
- **10-15｜Team 年繳 20 席下限**。見 [[entities/pricing#方案可用性與帳務摩擦]]
- **10-11｜經 gateway／proxy 時，server-side classifier 檢查未送達就改計入用量** ⚠️。見 [[entities/pricing#當前生效的計費規則]]
- **10-09～11｜Haiku 5.5 依 prompt 長度分兩檔計價** ⚠️：逾 10 萬 token 改用 $0.50／$2.50，長脈絡不加價的待遇不適用。見 [[entities/pricing#模型 API 定價現況]]
- **10-09｜說明頁拿掉「改走額外計費需你明確同意」** ⚠️：開了 usage credits，額度用完就直接扣款；同日 Dashboards（beta）算進方案用量。條目見下方 10-09
- **10-06→10-24｜Claude for Startups 的免費 Team＋$1,000 額度暫停**，不受理新申請。見 [[entities/pricing#額度與通路的帳務坑]]
- **10-05 查證｜Sonnet 4.5 11-30 退役**（Claude API；夥伴平台另訂時程）。見 [[entities/pricing#模型 API 定價現況]]
- **09-22／09-28｜Opus 5.5 $4／$20、Sonnet 5.5 $2／$10 上線並成為預設**。見 [[entities/pricing#模型 API 定價現況]]
- **09-19｜Auto mode 改用 server-side classifier，分類器耗用不計費**（API、Enterprise、雲端通路）。見 [[entities/pricing#當前生效的計費規則]]
- **09-14｜週配額換軌** ⚠️：+50% 加成到期、永久 +25% 接手，水位約為加成期間的 83%。見 [[entities/pricing#現況]]
- **08-10｜Sonnet 5 維持 $2／$10**，原訂 9/1 漲到 $3／$15 的計畫取消。見 [[entities/pricing#模型 API 定價現況]]
- **還沒證實的**：Opus 5.5 實驗性用量重置。見 [[entities/pricing#還沒確定的計費變動]]

---

## 定價與促銷（模型定價、方案設計）

#### 2026-11-07：官方 usage credits 說明頁大改版——新增帳戶刪除不退額度、auto-reload 措辭改寫，移除日本等地區 6 個月到期條款原文

- **Official Docs 異動（diff 偵測）**：[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) 字數由 8,715 增至 10,355 字；新增 21 段、移除 11 段。
- **新增內容**：帳戶刪除後剩餘 usage credits 不予退還、不予退款；auto-reload 措辭改寫為「餘額低於門檻時自動購買額度」；新增「能否退款」問答、「購買用量包」段落（另有 16 段未列細節）。
- **移除內容**：舊版「餘額低於門檻自動加值」措辭、「部分地區（如日本）額度 6 個月到期」條款原文；新版是否沿用相同地區規則未見明文，見 [[entities/pricing#當前生效的計費規則]] 待查證標記。
- **與既有記錄的關係**：本頁與母頁多次引用此同一頁作為 usage credits 規則的單一來源（如 08-08、09-24、10-04、10-09 條目），本次為該頁最大規模改版之一。

#### 2026-10-31：GitHub Issue #47509 升至 195 👍、70 留言——Team 方案高階座位提案仍無官方回應

- **GitHub Issue #47509**：延續 09-19 的 151 👍、46 留言，累積至 **195 👍、70 則留言**（GitHub Issues，2026-10-31）；提案不變——Team 方案新增對等 Max 20x 的席位，現有最高為 Premium（官方只寫是 Standard 的 5 倍）。官方回應與時程未見。

#### 2026-10-16：官方 API 定價頁格式改版，Fast mode 拿掉「research preview」標籤

- **Official Docs 異動（diff 偵測）**：platform.claude.com/docs/en/about-claude/pricing 新增 3 段、移除 4 段；Opus 5／4.8／5.5 的 Fast mode 價格數字不變（$10/$50、$8/$40），新增段落僅格式補上「USD」單位標示。
- **非純格式的部分**：移除段落原文帶「in research preview」，新增段落已不再出現此字樣——Fast mode 的「研究預覽」標籤已從官方頁拿掉；同時移除「Fast mode 不適用於 Opus 4.7／4.6」的舊限制語句，兩款模型已非現行陣容，屬清理舊版文字，非新增限制。
%% 維運備忘：下方「模型 API 定價現況」Opus 5 細節原載「Fast mode（research preview，僅 Claude API）」（來源日 2026-08-08），已同批依本次官方文字更正 %%

#### 2026-10-14：官方 API 定價頁 Managed Agents 範例模型從 Opus 5 換成 Opus 5.5

- **Official Docs 異動（diff 偵測）**：platform.claude.com/docs/en/about-claude/pricing 新增 6 段、移除 7 段，範例標題由「...using Claude Opus 5」改為「...using Claude Opus 5.5」；新增段落含快取讀取、輸入、輸出三行計算與總額 **$0.428**。
- **確認事實**：40k／50k 輸入走快取情境下，總成本由 Opus 5 時代的 $0.525 降至 Opus 5.5 的 $0.428，對應上方「一小時／一個月大概多少」表與上方 Managed Agents 計費規則同步更新。
- **無快取情境已補查證（2026-10-14 當日 WebFetch 官方定價頁逐字核對）**：無快取總成本同步由 Opus 5 時代的 $0.705 降至 Opus 5.5 的 **$0.58**（input $0.20＋output $0.30＋session-hour $0.08），官方頁面兩套算例（無快取／快取）皆保留，diff 偵測當時未列全只是摘要截斷，非官方拿掉無快取版本。

#### 2026-10-10：官方 Plans & Pricing 頁新增「$100–$200/月 API 額度」段落，同日傳出免費 Team 試用與額度優惠暫停

- **Official Docs 異動**：claude.com/pricing 頁字數增至 22,083 字（+273），新增「$100 to $200/month in API credits」等片段（diff 偵測，非完整原文）；同時移除「Industries: Financial services」段。
- **Google News／Pasquale Pillitteri**：稱 Anthropic 今日暫停先前上線的免費 Claude Team 試用與每月 $1,000 API 額度優惠；此來源過往曾被查出以同網域發多語言重複報導（見下方 09-23 條），單一來源，不採信為定案。
- **2026-10-24 查證**：「$100–$200/月」字樣即 [claude.com/pricing](https://claude.com/pricing) Max 卡片的「$100 to $200/month in API credits」，比較表列 Max 5x $100、Max 20x $200、Team 最高 $500／月（pooled）。
- **2026-10-24 查證（Team 席位）**：[官方文件](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)載 Team 每 Standard 席 $20、Premium 席 $100、池上限 $500，不涵蓋 Claude Code 與 Claude apps。這是月度 API credits 福利的定價頁呈現，不是 Startups 暫停的官方版本；媒體 $200／$500 分屬 Max 與 Team，不矛盾。

#### 2026-10-09：官方說明中心三頁同步改版——usage credits 機制拿掉「需明確同意」與「購買用量包」措辭

- **Official Docs 同日三頁同步變動**：[Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)、[How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)、[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)，字數均增長（各頁 +100～1,100 字）。
- **改版內容**：三頁均移除「過渡到 API 額度計費需使用者明確同意」的敘述，也拿掉「Buy usage bundles（購買用量包）」選項，改寫為「啟用 usage credits 後，額度用盡仍可繼續使用」。
- **對讀者的意涵**：既有「usage credits 是用量上限失效開關」規則不變，拿掉「需同意」措辭後，Max／Pro 用戶應重新至 `Settings > Usage` 確認開關現況，避免額度用盡後被動改走計費而不自知。
- **Manage usage credits 頁新增 15 段 FAQ**：含「能否在觸及週用量上限後繼續使用」，重申 session／weekly 兩種限制並存，與既有規則一致，未見新數字。

#### 2026-10-06：Anthropic 擴大 Claude Startups 計畫，媒體稱合格新創可領一年免費 Team＋$1,000 額度

- **媒體稱**：TechCrunch、CNBC、Quartz、Unite.AI 等至少 4 家同日報導 Anthropic 擴大 Claude Startups 計畫，合格早期新創可獲一年免費 Claude Team 方案＋$1,000 額度；官方計畫頁、資格門檻（公司階段、募資輪次上限）與適用席位層級（standard／premium）均未見本站查證，不得視為官方數字。
- **後續（2026-10-07）**：Android Headlines、Tech Edition（＋TechCrunch）、Dataconomy、Techish Kenya、Konsulteer 等至少 6 家媒體同步跟進報導同一方案，數字（一年免費 Team＋$1,000 額度）一致，資格門檻與席位層級細節仍未見官方頁面補齊。
- **2026-10-24 查證：Claude Startups 免費 Team／$1,000 額度已暫停**：[官方計畫頁](https://claude.com/programs/startups)載「current cohort is now full」、不受理新申請，審核中的申請未推進，無恢復日期。
- **暫停原因（媒體稱）**：Forbes（含 Australia 版）、AI Weekly 轉述 Sarah Wolf 的 X 貼文：資格條件未妥善調校致非新創也取得資格，前 48 小時申請量為前五個月的 21 倍；已兌換者保留、其餘重新審核。Startup Stack 夥伴折扣與 Applied AI office hours 續辦。
- **2026-10-11 查證**：官方方案頁 10-10 改版，但未寫暫停與生效時間；Startups 計畫頁仍無一手來源，暫停與否已於 2026-10-24 查證（見上條與「額度與通路的帳務坑」第 3 條）。
- **訊 2026-10-10 追蹤**：Google News／Pasquale Pillitteri（單一來源）稱已暫停免費 Team 試用與每月 $1,000 額度優惠，與同日官方 Plans & Pricing 頁新增 API 額度段落方向相符，但官方頁未明寫暫停與生效時間（2026-10-24 補：官方計畫頁已載申請額滿，Forbes 亦報導同事）。
%% 維運備忘：Team 分層官方資格與席位細節未經查證，暫不列入「我的方案現在有什麼」表，待官方說明中心或公告確認後補列 %%

#### 2026-10-05：Sonnet 4.5 退役日 2026-11-30 經官方查證屬實

- dev.to 報導 Sonnet 5.5 在 Terminal-Bench 4.0 拿下 70.6% 分、牌價為 Opus 5.5 一半（$2/$10 per Mtok，與本頁既有 Sonnet 5.5 牌價一致），同篇稱 Sonnet 4.5 將於 2026-11-30 退役。
- 經[模型棄用頁](https://platform.claude.com/docs/en/about-claude/model-deprecations)查證屬實：09-30 公告棄用、11-30 退役，建議遷移至 `claude-sonnet-5-5`；Bedrock、Google Cloud 另訂時程。

#### 2026-09-28：Claude Sonnet 5.5 上線，牌價 $2/$10 per Mtok，取代 Sonnet 5 為預設

- **官方一手來源＋Reuters**：Anthropic 官方發布 Sonnet 5.5，隨 Claude Code v2.1.284 更新，API 端 Sonnet 系列預設選項換成此版；牌價與前代 Sonnet 5 相同（$2/$10 per Mtok），支援 1M context，快取讀取 $0.10/Mtok（11-02 更正；[Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)；Reuters）。
- 完整定價表見上方「模型 API 定價現況」；模型能力面見 [[entities/sonnet-5-5]]。
- **Plans & Pricing 頁同步小改**：Batch processing 選項的示範模型從 Opus 4.8／Opus 5 換成 Sonnet 5、Fable 5，屬頁面範例更新，非費率變動（Official Docs）。

#### 2026-09-23：Claude Code cloud sessions 上線，新用戶最高可領 $250 額度
3 個獨立來源同日報導（Google News/Pasquale Pillitteri 等）：Claude Code cloud sessions 正式上線，新用戶可領最高 $250 額度；額度使用條件、到期日與是否僅限特定方案均未見報導細節，功能本身見 [[entities/claude-code]]。後續（2026-09-26）：BleepingComputer 報導補上使用條件缺口——此額度僅限 cloud sessions 使用，到期日仍未見報導。後續（2026-09-27）：gHacks 報導同一額度明確限定 Pro 與 Max 訂閱戶可領，與此前「新用戶」說法是否為同一資格範圍未見報導釐清，僅標題可用（Google News/gHacks）。

#### ❓ 2026-09-23：Opus 5.5 上線同時傳「實驗性用量上限重置」機制
查證進度與現況見 [[entities/pricing#還沒確定的計費變動]]。

#### 2026-09-22／23：Claude Opus 5.5 發布，牌價 $4/$20 per Mtok

- **官方一手來源**：Anthropic 官方部落格 2026-09-22 發布 Opus 5.5，牌價較 Opus 5（$5/$25）低，官方口徑為執行成本省 40%（來源：[Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)）。
- **媒體查證**：MIXED Reality News（09-23）確認 $4/Mtok 起、Pro／Max 用量上限同步調高，完整定價表見上方「模型 API 定價現況」（Google News/MIXED）。
- **與媒體「60%」說法的關係**：VentureBeat 報導 Opus 5.5 API 價格較 Fable 5.1（$10/$50）便宜 60%——與官方「40%」比較基準不同（Fable 5.1 vs Opus 5），兩者不可互換引用，詳見上表下方更正說明。

#### 2026-09-19：GitHub Issue #47509 互動量持續攀升至 151 👍、46 留言——Team 方案高階座位提案仍待官方回應

- **GitHub Issue #47509**：延續 09-06 已記錄之 133 👍、35 留言，互動量持續攀升至 **151 👍、46 留言**（2026-09-19 查證）；提案內容不變——Team 方案新增對等 Max 20x 用量的高階座位，供 CTO、技術主管等重度使用者選用，官方仍無回應；若獲採用將改變上方「我的方案現在有什麼」表的 Team 分層。

#### 2026-09-14：官方說明中心確認週用量換軌已如期發生，並澄清不影響 5 小時用量上限

- **Official Docs（support.claude.com）更新確認**：促銷（05-13 起實施，歷經多次延長，見 09-02 條目）已於 **09-13** 到期，Claude Code 週用量自 **09-14** 起回復標準額度（即上方 08-29 條目所記之永久 +25% 規則接手）。
- **官方澄清**：本次配額調整**不影響 5 小時用量上限的計算方式**——與週配額換軌是兩套獨立機制，讀者不需因本次變動額外調整 5 小時窗的用量節奏。
- **與既有記錄的關係**：本則為官方一手來源，坐實 08-29／09-02 兩則條目所記之換軌時程與水位換算（相較加成期間約減少 17%），未見數字修正（來源：[Claude Code May–August 2026 Weekly Limits Promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)，2026-09-14 查證）

#### 2026-09-06：GitHub Issue #47509（133 👍、35 留言）——使用者提案 Team 方案新增對等 Max 20x 用量的高階座位

- **GitHub Issue #47509**：Team 方案目前僅 Standard（1.25x Pro 用量）與 Premium（6.25x）兩檔座位，使用者提案新增對等 Max 20x 用量的高階座位，供 CTO、技術主管等重度使用者選用；累積 133 個 👍、35 則留言，尚無官方回應。
- **與既有社群訴求的關係**：與印度盧比在地化訴求（#17432，07-13 獲官方回應）同屬「社群提案、待官方回應」型座位／方案設計訴求，惟本則尚無時程跡象；若獲採用將改變上方「我的方案現在有什麼」表的 Team 分層。

#### 2026-09-05：官方定價頁再爆大改版（新增110+／移除168+段）；同日媒體稱「Anthropic 重置 Claude 限制」（2026-09-06 查證：價格結構未變）

- **Official Docs（claude.com/pricing）機械頁面比對**：頁面新增逾 **110** 個段落（多為 Mtok 計價區間，如 $0.10、$0.20、$0.25、$0.30、$0.50）、移除逾 **168** 個段落（多為依企業人數規模分類的介紹文字，如「20–100 人」「100+ 人」）。
- **字數變化**：頁面整體字數由約 **24,384** 字縮減至約 **20,870** 字；改版後最終呈現方式尚待人工開啟頁面全文確認。
- **與 09-02 條目的關係**：09-02 已記錄同頁「同步大幅改版」但未附具體段落增減數字，本次為機械偵測到的更大規模改版，兩者是否為同一輪改版分次偵測無法從機械 diff 判斷。
- ✅ **已查證**（2026-09-06 查官方定價頁全文）：改版後價格結構已完整取得——牌價、Managed Agents、乘數、內建工具計費、CCU 制皆載於本頁對應各節。段落增減為呈現方式調整，未改變費率。
- **同日媒體標題（Google News／Pasquale Pillitteri）稱「Anthropic Resets Claude Limits」**：見於報導 GPT-6 Astra 上線 Pro／Enterprise／API 的文章副標，惟原文全文未能取得，無法確認具體異動內容。
- **促銷說明頁同日複查**：週用量促銷說明頁（May–August 2026）本次僅頁首／頁尾樣板文字變動，核心內容未見結構性變化；09-13 到期日暫無新證據需修正，惟本次比對範圍有限，不足以確認促銷是否仍生效

#### 2026-09-02：官方更正週用量促銷延長至 09-13（非如期於 08-31 終止）；定價文件新增 Fable 5.1／Mythos 5.1 快取費率；印度盧比訴求互動再攀升

- **Official Docs（support.claude.com）更正促銷狀態**：Claude Code 週用量 +50% 促銷再度延長，新到期日 **2026-09-13**（原記 2026-08-31 到期），適用 Pro、Max、Team。原文：「We've extended this promotion. Increased weekly limits now run through September 13, 2026.」**更正本頁既有記錄**：08-29 條目曾記「促銷如期於 08-31 終止、不再延長」，本次官方更新顯示該促銷實際上又獲延長，並非終止；上方「當前生效的計費規則」與「已失效並移除的規則」均已同步修正（來源：[Claude Code May–August 2026 Weekly Limits Promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)，2026-09-02）
- **Official Docs（platform.claude.com/docs/en/about-claude/pricing）新增快取費率**：定價頁更新反映 Claude Fable 5.1、Claude Mythos 5.1 的快取讀取／刷新費率降至**標準輸入價的 0.025 倍**（標準快取讀取為 0.1 倍），長對話情境下快取成本較前代最多省下 75%；方案與定價頁（claude.com/pricing）同步大幅改版（新增/移除多段定價說明，完整差異未見比對）。**與模型頁的關係**：Fable 5.1／Mythos 5.1 為官方定價文件首度出現的具體版本號，此前僅見於 08-28 Reddit 社群臆測（[[entities/fable-5]] 懸置標記）；本則為一手來源，強力佐證兩版本已存在。本頁僅記錄快取乘數，兩版本完整基礎 $/Mtok 定價未見公布，暫不列入上方「模型 API 定價現況」表；此快取乘數變動屬本頁「通路與乘數」節範疇，待納入該節乘數對照表（來源：[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[claude.com/pricing](https://claude.com/pricing)，2026-09-02）
- **GitHub Issue #17432 留言數更新**：留言數由 08-17 查證的 212 增至 **213**，本次首度記錄 reactions 達 **628 👍**（本輪商業類條目互動量最高之功能請求）；訴求內容不變——使用者要求 Anthropic 仿照 OpenAI（ChatGPT）、Google（Gemini）推出印度盧比定價方案，涵蓋 Claude Pro 與 Claude Code 兩項訂閱。與既有記錄相同：07-13 官方回應僅確認 Pro 方案訂閱定價，Claude Code 涵蓋範圍缺口依然存在（GitHub https://github.com/anthropics/claude-code/issues/17432，2026-09-01）

#### 2026-08-29：官方公告週配額改版——09-14 起標準週配額永久 +25%，但 08-31 起不再延續 +50% 促銷，實際減少約 17%

- **官方公告**：Anthropic 官方（[Bluesky @anthropicbot](https://bsky.app/profile/anthropicbot.bsky.social/post/3muaaxs5nx424)）宣布自 **2026-09-14** 起將 Claude Code 標準週配額**永久**調高 **25%**，適用 **Pro、Max、Team 與座位制 Enterprise** 方案；同時本頁已追蹤逾三個月的「週用量 +50% 促銷」（見上方「當前生效的計費規則」）如期於 **2026-08-31** 到期、不再延長。
- **對讀者的實際影響（換算）**：`1.25 ÷ 1.50 ≈ 0.833`——09-14 起的永久週配額約為現行 +50% 加成水位的 83%，即**相較「目前」實際減少約 17%**；BleepingComputer 標題〈Anthropic is cutting Claude Code's current weekly limits by 17 percent〉即以此框架報導，多家媒體同步跟進。
- **與既有沿革的關係**：+50% 促銷自 2026-05-13 起歷經 06-22→07-07→07-12→07-19→08-18 五度延長，本次是首度明確終止且改以「永久」而非「促銷」形式接手，性質從「暫時加成」轉為「基準值調整」——讀者不應再期待第六次延長。
- **來源**：[Bluesky @anthropicbot](https://bsky.app/profile/anthropicbot.bsky.social/post/3muaaxs5nx424)、[BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/)，2026-08-29
- **08-31 跟進（非新事實，社群／媒體評論延燒）**：Hacker News 社群貼文（08-31）與 Android Headlines 分析文章同步討論此次改版，兩者均沿用官方已確認之「相較目前水位實際減少約 17%」換算數字，未提出新增數字；Android Headlines 將此定性為「悄悄降規」（quiet nerf），HN 討論串則拿 OpenAI Codex 的配額調整方式相比。**兩者均為社群/媒體評論或推算，非官方新公告**——17% 換算本身已於 08-29 由官方公告＋BleepingComputer 官方測算確認，本則僅補充後續輿論反應層面，不改變上方已記錄之官方規則內容（[Hacker News](https://twitter.com/ClaudeDevs/status/2093742322525810912)；[Android Headlines](https://www.androidheadlines.com/2026/08/anthropic-claude-code-weekly-limits-update.html)，2026-08-31）

#### 2026-08-21：官方查證更正——3,500 萬美元為 Defender Advantage Fund（資助修補開源漏洞組織），非企業導入 Mythos 5 的額度；企業導入本身按標準 token 計費

- **事實更正（2026-09-06 查證）**：四方媒體報導誤把「$35M」與「企業導入 Mythos 5」併為一事，實為兩件事：$35M 是 **Defender Advantage Fund**，資助修補開源漏洞的組織，非企業導入額度。
- 出處：[Anthropic Blog](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)，2026-08-21。
- **企業導入 Mythos 5 掃描本身**：Claude Enterprise 方案可在 Claude Security 產品線跑 Mythos 5 漏洞掃描，**按既有方案的標準 token 用量計費，無須加購**；模型能力釋出面詳見 [[entities/mythos]]，產品功能細節見 [[entities/claude-security]]。
- **與「我的方案現在有什麼」表的關係**：兩件事皆非該表涵蓋的一般訂閱方案優惠，不列入表內。

#### 2026-08-21：Techzine 報導 Anthropic 允許企業將 AI 資料存放於自有雲端環境（單一來源，後於 09-03 由官方 EFS 公告確認）

- **Techzine Global（2026-08-21 07:46 UTC）**：報導稱 Anthropic 讓企業客戶可將 AI 資料存放在自有雲端環境，僅標題可用，未見實作機制（是否限特定雲端商、涵蓋哪些模型／方案）、生效時間或官方公告連結。
- **與下方 08-20 資料保留政策報導的關係**：時間相近、同屬企業資料治理，但措辭不同（一稱「自有雲端存放」、一稱「保留政策調整」），標題層級無從判斷是同一政策的兩種描述或兩項獨立變動。**後續（2026-09-03）**：官方 09-01 的 EFS 公告同時涵蓋兩者（資料留在客戶自有雲端＝Anthropic 端不留存）。
- **企業資料存放於自有雲端環境——官方已確認（2026-09-03 查證）**：Anthropic 09-01 公告 Enterprise Frontier Safeguards（EFS），明載企業用量資料存放於**客戶自行控制的雲端基礎設施**而非 Anthropic 端；EFS 免費，自 2026 年秋季起分階段對企業客戶開放。08-21 Techzine 標題所述即此政策的預告（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)，2026-09-01；詳見 [[topics/anthropic-business]]「哪個合作會改到你用的 Claude」EFS 條目）

#### 2026-08-20：路透社／彭博社（消息人士）報導 Anthropic 計畫調整企業資料保留政策（未經官方證實）

- **Reuters（19:34 UTC）／Bloomberg（17:51 UTC）同日報導**：兩家均引述消息人士稱 Anthropic 計畫調整企業客戶的資料保留政策；Bloomberg 標題聚焦「進階 AI」的適用範圍。兩則僅標題與極簡導言可用，調整內容（保留天數增減、涵蓋模型範圍、生效時間）未見細節。
- **與既有「30 天資料保留政策」的關係（見 2026-06-09 條目）**：本頁已記錄 Fable 5／Mythos 5 流量（含 AWS Bedrock）強制保留 30 天；本則「計畫調整」是否針對此政策、方向為何均未見細節，不可推定延長或縮短。
- **與競品動態的呼應**：同期 The Register／TechCrunch 報導 OpenAI 祭出「零資料保留」（zero data retention）承諾搶攻 Anthropic 企業客戶，被解讀為競爭回應，詳見 [[topics/competitor-landscape]]「OpenAI ChatGPT Work / GPT-5.6」子區塊。
- **企業資料保留政策調整——官方版本為 EFS（2026-09-03 查證）**：08-20 Reuters／Bloomberg 匿名消息稱 Anthropic 計畫調整企業資料保留政策；官方 09-01 公告的 Enterprise Frontier Safeguards 即其落地形式——資料留在客戶自有雲端、Anthropic 端不留存，並搭配濫用偵測。官方公告**未載**媒體先前傳的「保留天數」數字，該口徑僅為媒體稱（Reuters、Bloomberg），不得視為官方數字（[Anthropic Blog](https://www.anthropic.com/news/enterprise-frontier-safeguards)，2026-09-01；詳見 [[topics/anthropic-business]]「哪個合作會改到你用的 Claude」EFS 條目）

#### 2026-08-19：DevOps.com 稱「暫時性用量提升」當晚到期，與週用量 +50% 促銷延長是否同一時程尚無法確認

- ✅ **已查證**（2026-09-06）：DevOps.com 所稱「當晚（08-19）到期」與 08-18 官方確認的延長，為**同一促銷的當期到期日被延長**——促銷歷次到期日 07-19→08-18 前後→08-31→09-13，DevOps.com 報導描述的正是其中一次到期日交接點，之後即被延長，與本頁時序不矛盾。
- **與既有記錄的關係**：目前生效的計費規則仍以 08-18 官方公告為準——+50% 促銷持續至 2026-08-31，見上方「當前生效的計費規則」。本則「暫時性用量提升」若確為獨立的另一項時程調整（如 05-19 記錄的「5 小時使用量加倍」類臨時優惠），到期後額度是否縮減仍待官方文件或後續報導證實。

#### 2026-08-18：Claude Code 週用量 +50% 促銷再度延長至 2026-08-31，Google News 另傳「滾動限額加倍」但用詞與官方數字不一致

- **官方確認再延長**：Hacker News 轉載 support.claude.com 公告（276 分，2026-08-18 17:02 UTC）確認 Claude Code 週用量 +50% 促銷再度延長，運作期間由原訂 **2026-05-13** 起延續至 **2026-08-31**；適用 Pro／Max／Team 及舊制席位制 Enterprise 使用者，**Free 方案與消耗制（consumption-based）Enterprise seat 不適用**；僅調升週用量上限，**5 小時用量上限不受影響**；符合資格帳號自動套用，無需使用者操作。
- **更正本頁既有記錄**：本頁 07-12 條目曾將此促銷與 Fable 5 免費期一併記為「同步延至 7/19」到期，07-21 Reddit 週熱門貼文當時已提示 Claude Code 另有獨立的、約 2026-08-19 到期的延伸方案（見下方 07-21 條目）。本次官方公告證實兩者確為**兩條獨立時程**：Fable 5 免費期確於 07-19 到期並由 07-20 分界取代（不受影響、如常記錄）；週用量 +50% 促銷則持續延長至今，**並未於 07-19 終止**。已同步修正上方「當前生效的計費規則」。
- **Geeky Gadgets：「滾動限額加倍」，用詞與官方「+50%」數字不一致**：Google News／Geeky Gadgets（2026-08-18 11:20 UTC）標題稱「Anthropic Doubles Claude Code Rolling Limits for Paid Plans」，原文僅標題層級可用。時間點與適用對象（付費方案）均與上述官方公告高度重疊，判斷為**同一波政策調整的媒體轉述**，但「加倍（100%）」與官方明載的「+50%」數字不一致——不採信「加倍」數字，以官方 support.claude.com 公告的 +50% 為準；若後續證實為另一項獨立於本次延長的配額調整，需另行查證區分（Google News/Geeky Gadgets）。

#### 2026-08-17：印度盧比定價訴求 GitHub Issue #17432 留言數再攀升，Claude Code 涵蓋範圍仍未見官方確認

- **留言數更新**：GitHub Issue #17432〈Feature Request: India-Specific Pricing Plans (INR) for Claude & Claude Code〉留言數由 07-29 查證的 210 增至 **212**（reactions 未見本次查證更新）。
- **與 07-13 官方回應的範圍缺口依然存在**：07-13 印度盧比計價公告僅確認 Pro 訂閱定價，原始訴求同時提及的 **Claude Code** 是否同步在地化仍未見報導。互動量在官方回應後持續攀升（07-03 留言 205 → 07-29 210 → 08-17 212），可能反映此缺口，也可能只是舊討論串持續累積，無從確認（僅記錄現象）。
- **用詞界定**：本則為使用者訴求延續，**非**官方新公告（GitHub https://github.com/anthropics/claude-code/issues/17432）。

#### 2026-08-10：Claude Sonnet 5 入門定價 $2/$10 永久化，9/1 漲至 $3/$15 的計畫取消（2026-08-26 補記）

- **官方公告**：Anthropic 官方帳號宣布「making Claude Sonnet 5's introductory pricing permanent」——Sonnet 5 於 6 月發布時載明 $2/$10 per Mtok 為入門價、有效期至 2026-08-31，該價格**維持不變**；原定 2026-09-01 起調至 $3/$15（各降幅 50% 的漲幅）**不會發生**（部分媒體記為 08-11）
- **官方文件佐證（2026-08-26 查證）**：官方模型總覽頁 Sonnet 5 定價欄現為 `$2 / input MTok, $10 / output MTok`，**已無任何 introductory／temporary／到期字樣**；官方定價文件另載明該價格「is now the standard price」
- **⚠️ 收錄延遲**：此則為官方定價變動，但**本站日常追蹤的新聞來源於 08-10～08-26 全數未提及**——官方公告發布於 X 與官方說明中心，兩者皆非本站例行監看範圍。結果是本頁在漲價日前 5 天仍掛著「⏰ 08-31 到期」倒數，讀者會據以做錯誤的成本決策
- **連帶更正**：本頁「模型 API 定價現況」表、「⏰ 倒數中」、[[feature-radar]]、[[topics/model-comparison]]、[[entities/sonnet-5]] 的到期敘述已於 2026-08-26 一併上修
- **缺口已修補（2026-08-28）**：官方 API 定價頁（`platform.claude.com/docs/en/about-claude/pricing`，即記載本次變動的那一頁）已納入官方文件監看清單；同時官方頁的變更偵測由「只說變了」升級為列出新增／移除的段落——本次這種「少了一句到期字樣」的移除型變動，先前的偵測方式看不出來

#### 2026-08-11：官方文件補充 usage credits 僅限網頁版開通，pricing 頁確認 Free 方案功能範圍

- **官方 usage-credits 條目補充限制**：support.claude.com 說明中心確認行動 App 訂閱者無法直接於 App 內開啟 usage credits，須改至網頁版操作；額度用盡後可切換按量計費（API 標準費率）不中斷。詳見上方「方案細節」新增條目
- **claude.com/pricing 確認方案分層**：官方定價頁列出 Free／Pro／Max 各方案，Pro 明確標示涵蓋 Claude Code／Cowork／Design／Science，與 2026-08-12 已記錄之「Free／Pro 功能組成補充」屬同一份官方頁面的不同時點查證，不重複記錄

#### 2026-08-08：官方 Help Center 查證，07-18～21 四方矛盾報導收斂（✅ 已收斂）

- **查證動機**：本頁自 07-18 起累積四則互相矛盾的媒體報導（Tech Times「Max 永久」／Dawn「50% 上限」／the-decoder「Pro 導向 API 計費」／Reddit「轉為 metered」），懸置 20 天無官方澄清。日報來源不含 `support.claude.com`，媒體轉述始終只有標題層級，故直接查證官方說明中心原文。
- **官方結論（[Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)）**：2026-07-20 生效。Max 方案／Team premium seats／舊制席位制 Enterprise premium seats — Fable 5 標配，可用至多**週用量上限的 50%**，不額外收費；Pro 方案／Team standard seats／Enterprise standard seats — Fable 5 **不計入方案用量**，改以 usage credits 按 API 費率付費。先前促銷結束於 **2026-07-19 23:59:59 PT**。合格 Pro 與 Team standard seats「qualify for a one-time credit to help with the change」。
- **四則矛盾報導其實各對一半**：Tech Times「Max 永久」✅（Max 確為標配）、Dawn「50% 上限」✅（標配確有 50% 週上限）、Reddit「轉為 metered」✅（但那是講 Pro）—— 三則各自描述不同 seat 層級卻都未指明層級，才被記成互斥（推論）。
- **一次性 credit 金額 ✅ 已於 2026-08-22 官方查證為 $100（此前僅媒體數字）**：官方促銷條目載明 Pro 每帳戶 $100、Team 每 standard seat $100（每組織上限 $2,500），領取窗 2026-08-02 關閉、credits 2026-09-17 到期、不限 Fable 5 可用於任何模型（[官方條目](https://support.claude.com/en/articles/15862783)）。先前 XenoSpectrum／XDA／nerdzap 的 $100 說法事後證實正確，但當時無官方佐證，本頁按分級紀律標為媒體數字屬正確處置。credits 購買方式亦有歧異——官方寫「Add funds 自行輸入金額」，XenoSpectrum 稱固定包（$45 買 $50／$200 買 $250／$700 買 $1,000），以官方為準。
- **usage credits 的隱性風險（[Manage usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)）**：credits 為 opt-in、預設關閉（`Settings > Usage`），可設 auto-reload（每日兌換上限 $2,000）。開啟後方案用量上限不再是硬停止——Claude 繼續回答並從 credits 扣款，體感與額度內無異。此即 08-01 XDA「多數人從沒注意到」報導所指的計費異動（見下方同組條目），至此獲官方文件佐證。
- **官方 Help Center 未把此事寫進 Release notes**：[Release notes](https://support.claude.com/en/articles/12138966-release-notes) 只記模型發布與功能（07-24 Opus 5、07-09 Reflect、07-01 Fable 5 恢復），方案／配額／計費改制不在其中——代表即使把該頁納為來源，此類異動仍抓不到（流程缺口見 `wiki/log.md` 2026-08-08 Query 條目）。

#### 2026-08-01：XDA 報導多數用戶未留意 Fable 5 免費促銷已悄悄改變計費方式（媒體視角補充，非新事實）

- **XDA：免費促銷附帶靜默計費異動，多數用戶未察覺**：XDA 文章稱先前 Fable 5 相關的 $100 免費體驗促銷附帶改變了 Claude 計費方式，多數使用者並未留意。**與既有事實的關係（推論，待證實是否同一事件）**：本頁已記錄 Fable 5 免費期歷經多次延長（06-09→07-01→07-07/08→07-12→07-19）後轉為 usage-based billing；本則僅標題可用，無費率、額度換算或生效時間等新細節，無法確認是同一轉換事件或另一項獨立異動。若為同一事件，本則的獨特角度是「多數用戶未察覺計費已變」的認知落差，呼應本頁一貫記錄的「靜默計費改動損傷信任」風險（見 [[topics/anthropic-business]]「還沒過去的風險」表）（Google News/XDA）

#### 2026-07-29：印度盧比定價訴求 GitHub Issue #17432 互動持續攀升，距官方 07-13 回應已 16 天

- **互動量新高**：GitHub Issue #17432〈Feature Request: India-Specific Pricing Plans (INR) for Claude & Claude Code〉留言數由 07-09 查證的 205 增至 **210**、reactions 由 **598** 增至 **613**，遠超「高」門檻（GitHub Issue ≥50 留言）。
- **與已回應事實的張力（非官方政策異動）**：Anthropic 於 07-13 推出印度盧比計價（Pro 方案 Rs 2,000/月，見下方條目），當時視為對此訴求的官方首度回應。惟 issue 原始訴求同時提及 **Claude 與 Claude Code**，07-13 公告僅確認 Pro 訂閱定價，Max/Team/Enterprise 與 Claude Code 是否同步在地化未見報導；互動量在官方回應後仍攀升，可能反映此範圍缺口，也可能只是舊討論串持續累積，兩者均無從確認（僅記錄現象）。
- **用詞界定**：本則為使用者訴求延續，**非**「Anthropic 將推出新方案」——尚無官方聲明承諾進一步異動（GitHub https://github.com/anthropics/claude-code/issues/17432）。

#### 2026-07-24：Claude Opus 5 發布，官方稱定價為 Fable 5 的一半，與此前 MarkTechPost「維持原定價」說法方向不一致

- **官方公告**：Anthropic 發布 Claude Opus 5（[官方公告](https://www.anthropic.com/news/claude-opus-5)，2026-07-24 16:57 UTC，Hacker News 1587 分），稱定價為 Fable 5 的一半，相同成本下效能較 Opus 4.8 大幅提升；現為 Max 方案新預設模型、Pro 方案最強可用模型，取代 Opus 4.8 次旗艦地位。**與既有訊號的落差**：MarkTechPost（2026-07-14，見 [[topics/model-comparison]] 延伸閱讀）此前稱 Opus 5 將「維持原 Opus 定價」，與「砍半」方向不同；官方公告未給 $/Mtok 數字，以 Fable 5 $10/$50 推算半價約 $5/$25，屬讀者端推算而非官方確認。**後續（2026-08-08 查證、2026-08-20 複查一致）**：官方文件載明 **$5 / $25**，「unchanged from Claude Opus 4.8」——推算獲證實，兩則報導的方向差異隨之解消（同一組數字的兩個對照對象）。見上方「模型 API 定價現況」；能力面見 [[entities/opus-5]]。

#### 2026-07-21：Reddit 週熱門回顧 Fable 5 免費期延長史，社群觀察指向 Max／Team Standard 轉為計量存取

- **延期歷史彙整 + Max/Team Premium 稱轉為計量存取**：r/artificial 週熱門貼文（2026-07-20 07:56 UTC）整理 Fable 5 免費存取期限延後歷程（6/22→7/7→7/12→7/19），並指出 7/20 起 Max 與 Team Premium 方案轉為**計量存取（metered）**。**與既有矛盾訊號的關係**：本則社群來源方向與既有 07-19 Tech Times「Max 永久」說法相反，較接近 Dawn「用量上限 50%」與 07-18 Startup Fortune／the-decoder.com「收緊 Max/Team Premium 配額」的方向；惟本則僅為 Reddit 週熱門貼文，非官方公告，與既有官方層級矛盾報導並列記錄，不可視為官方定案（推論）。
- **Claude Code 額外延伸方案提醒**：同則貼文提醒讀者 Claude Code 另有 **2026-08-19** 到期的延伸方案值得關注，暗示 Claude Code 訂閱層與 Fable 5 免費期為兩條獨立的計費時程；具體延伸方案內容未見報導細節，待後續補充。
- **07-17 早期信號（回溯記錄）**：r/artificial 週熱門貼文（2026-07-17 18:48 UTC，標題帶問號，非確認事實）反映部分月付 $200 的 Claude.ai Max 用戶回報 Fable 5 存取遭停用；早於 07-18 官方訊號分歧報導兩天出現，可視為社群端最早察覺存取異動的訊號，但當時未經證實（推論：與 07-18/07-19/07-20 後續報導方向一致，顯示社群端偵測先於媒體確認）（Reddit r/artificial）

#### 2026-07-19：免費期到期日當天，Fable 5 存取政策再添兩則標題層級報導，仍未消解矛盾

- **Tech Times：「Max 永久、Pro Credits-only」（2026-08-10 官方查證確認屬實）**：標題稱 Claude Fable 5 訂閱限制調整為「Max 方案轉為永久提供、Pro 方案改為 Credits-only」。經 2026-08-08 官方 Help Center 查證（見上方「官方 Help Center 查證」段），此標題所述**方向正確**：Max 方案／Team premium seats 確為標配（不脫離、"permanent" 意指不下架），Pro 方案／Team standard seats 確改為 usage credits 按 API 費率計費——與 07-18 Startup Fortune／the-decoder.com「Pro 導向 API 計費」方向一致，兩則報導確實是同一政策的「方案別拆解」，非互斥（[Tech Times](https://www.techtimes.com/articles/320905/20260718/claude-fable-5-ends-subscription-limbo-permanent-max-credits-only-pro.htm)，2026-07-18）
- **Dawn：「併入 Max、Team Premium，用量上限 50%」**：標題稱 Anthropic 將把 Fable 5 模型以「50% 用量上限」的方式併入 Max、Team Premium 方案。**與 Tech Times 報導的落差**：若 Max 方案是「永久提供」（Tech Times），與本則「50% 用量上限」的描述無法完全對照——「永久」可能指存取權限本身不下架，「50% 上限」則可能指配額分配比例，兩者未必互斥，但缺乏官方公告確認具體機制（Google News/Dawn，07-18 12:50 UTC）
- **⚠️ 不擇一呈現**：本頁採「如實記錄矛盾」原則，兩則新報導均為標題層級資訊，與 07-18 已記錄的矛盾訊號一併保留，待官方於免費期到期後進一步公告釐清。

#### 2026-07-18：Fable 5 存取政策訊號分歧——「收緊限制」vs「設為永久」同日並存

- **收緊限制方向**：Startup Fortune（「Anthropic Limits Claude Fable 5 Access as It Runs Out of Compute」）與 the-decoder.com（另有媒體同步報導，「Anthropic slashes Claude Fable 5 limits in Max and Team Premium and pushes Pro users toward API pricing」）同日報導，Anthropic 因運算資源吃緊，大幅縮減 Max 與 Team Premium 方案的 Fable 5 使用配額，並將 Pro 方案用戶導向改用 API 計費。**與 Meta 運算力租賃洽談的呼應（推論）**：同日 [[topics/anthropic-business]] 記錄 Meta 據報洽談以 100 億美元規模租賃運算力予 Anthropic，兩則報導共同指向「Anthropic 運算需求已超出現有供給」的同一根因——對外租算力、對內收緊高階模型配額，是同一資源缺口下的一體兩面（推論）。
- **設為永久方向（矛盾訊號）**：Simon Willison 部落格同日（06:00 UTC，早於上述兩則收緊限制報導）引述官方 `@claudeai` Twitter 帳號發布內容，標題為「Claude make Fable 5 permanent」（將 Fable 5 設為永久）；原文於標題引述後即截斷，無更多細節可查證。
- **⚠️ 如實記錄矛盾，不擇一呈現**：兩則方向相反的報導同日出現，可能反映（a）官方公告本身存在時間差或表述模糊、（b）「設為永久」specifically 指某項功能/免費層級的一部分而非整體 Fable 5 免費存取、或（c）媒體對同一份公告有不同解讀。目前生效的免費期到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），實際政策走向待 7/19 前後官方進一步公告釐清。

#### 2026-07-17：交易員押注 Fable 5 免費期將第四度延長（市場猜測，非官方，07-18 獨立來源佐證）

- **市場押注，非官方公告**：Proactive financial news 報導交易員押注 Anthropic 將第四度延長 Claude Fable 5 免費使用期限。**注意**：此為財經媒體對交易員市場行為的報導，非 Anthropic 官方公告，目前生效的到期日仍為 **2026-07-19**（見上方「當前生效的計費規則」），未見變動。
- **07-18 獨立來源佐證**：Yahoo Finance UK（另有媒體同步報導）獨立報導同一押注方向，強化此市場預期訊號的傳播度，非新增事實。
- **對既有延長序列的意涵（推論）**：Fable 5 免費期已延長三次（06-09 原訂 6/22 → 07-01 明確 7/7 → 07-07/08 延至 7/12 → 07-12 再延至 7/19），交易員押注第四度延長顯示市場預期 Anthropic 對 usage-based billing 轉換將持續採取謹慎策略，與既有「Anthropic 對 Fable 5 計費轉換態度謹慎」的判斷（見 07-12 條目）方向一致；惟押注本身不構成事實依據，7/19 後實際走向仍待官方公告確認（Google News/Proactive financial news）

#### 2026-07-13/14：印度盧比在地化定價正式推出，回應長期社群訴求（重大）

- **官方推出印度盧比計價，Pro 方案 Rs 2,000/月**：TechCrunch、NDTV、Times of India、bestmediainfo.com 同步報導，Anthropic 為美國以外最大市場印度啟動盧比計價，Pro 方案訂為每月 **Rs 2,000**。**對採用率的意涵**：是官方首度正式回應下方 07-03 條目記錄的 GitHub Issue #17432（reactions 598、留言 205，長期無官方回應）印度在地化定價訴求，若能提升印度市場訂閱轉換率，將直接驗證此前「未回應在地化定價將影響全球最大開發者社群之一的轉換率」的推論；具體匯率換算基準、是否同步適用 Max/Team/Enterprise 方案未見報導細節，待後續補充（NDTV「Anthropic Starts India Pricing For Claude AI, Pro Plan At Rs 2,000」；TechCrunch「Anthropic starts localizing Claude pricing for India, its biggest market after the US」）
- **API 定價跨供應商比較難度浮上檯面（The Register）**：Google News/The Register（多家媒體同步報導）分析指出 Anthropic tokenizer 設計較複雜，使 API 定價與跨供應商成本估算更難以直接比較；僅標題式報導，無具體量化細節，惟此議題與印度盧比在地化定價同日出現，共同凸顯 Anthropic 全球定價透明度議題（推論：一為訂閱端在地化，一為 API 端可比性，兩者性質不同，不宜混為一談）
- **社群對 Fable 5 訂閱去留持續揣測（非官方，無新事實）**：Reddit r/ClaudeCode（2026-07-14，無週熱門標記）用戶詢問 Fable 5 是否會退出訂閱方案改為純點數（credit-based）付費，反映月付 $100 訂閱用戶對加購點數的不滿；同時 Reddit r/ClaudeAI · 週熱門（2026-07-10）另一貼文推論，隨 OpenAI Sol 上市成為同級競品，現階段將 Fable 5 移出訂閱方案的可能性不高，如同 Opus 4.5 上市後未被移出訂閱方案的先例。**注意**：兩則均為社群揣測，非官方公告，與上方「Fable 5 免費使用期限延長至 7/19 後是否轉 usage-based billing」的既有未決問題方向一致，可視為市場對該懸而未決政策的持續關注訊號（推論）（Reddit r/ClaudeCode；Reddit r/ClaudeAI）

#### 2026-07-12：週用量 +50% 促銷再延長至 7/19，Fable 5 免費期同步順延

- **官方公告**：Anthropic 官方公告（Hacker News 轉載，support.claude.com，2026-07-12 18:01 UTC）將原訂 5–7 月週用量 +50% 促銷再延長，效期由 7/13 延至 **2026-07-19**；適用範圍限定 **Pro／Max／Team 及舊制（席位制）Enterprise 方案**，**Free 方案與用量制 Enterprise 席位不適用**，5 小時額度不受影響。
- **Fable 5 免費期同步順延**：Fable 5 原訂 7/12 到期的免費使用期限（Pro/Max/Team 每週配額含 50% 用量）隨此公告同步延至 **7/19**，為繼 06-09（原訂 6/22）、07-01（明確 7/7）、07-07/08（延至 7/12）之後第三度延後轉為 usage-based billing 的時程。
- **競爭角度（推論）**：Google News/The Economic Times、Simon Willison（2026-07-12）分析指出，此次延長與 GPT-5.6 Sol 被業界認為屬同級模型有關，Anthropic 可能藉延後轉付費時程維持促銷期間對用戶的競爭吸引力；模型能力面比較詳見 [[entities/fable-5]]、[[topics/model-comparison]]。
- **注意**：連續三次延後同一到期日顯示 Anthropic 對 Fable 5 計費轉換採取謹慎策略（呼應既有 07-07/08 條目判斷），本次是首次明確與競品能力對標掛鉤的延後理由。

#### 2026-07-10：Wired 報導聚焦「Anthropic 要消費者為 Fable 5 付費」

- **媒體視角補充，非新政策**：Wired 報導「Anthropic Wants You to Pay Up for Claude Fable 5」，聚焦 Anthropic 要求消費者為使用 Fable 5 額外付費的趨勢。**注意**：此報導呼應既有 07-01（7/7 起 usage-based billing 生效）與 07-07/08（免費期限延長至 7/12）已記錄的政策時程，未見新的定價數字或時程異動，屬媒體對既有政策走向的解讀補充（Wired，2026-07-09 18:30 UTC）

#### 2026-07-07～08：Fable 5 免費使用期限再延長 5 天至 7 月 12 日

- **官方延長免費期**：Times of India、Forbes 報導 Anthropic 將 Claude Fable 5 免費使用期限再延長 5 天，由原定 2026-07-07 延至 **2026-07-12**；Pro/Max/Team 每週配額含 50% Fable 5 用量的過渡期同步順延。**注意**：這是繼 06-09（原定 6/22 轉消費制）、07-01（明確 7/7 為 usage-based billing 生效日）之後第二次延後轉換時程，顯示 Anthropic 對 Fable 5 計費模式轉換採取謹慎、分批延後的策略，可能反映對用戶留存或計費系統就緒度的顧慮（推論）（Times of India https://timesofindia.indiatimes.com/technology/tech-news/anthropic-extends-claude-fable-5-free-offer-till-july-12-eligibility-and-other-details-explained/articleshow/132255396.cms；Forbes https://www.forbes.com/sites/sandycarter/2026/07/07/claude-fable-5-extends-by-five-more-days-10-moves-to-make-now/）

#### 2026-07-04：企業版 Claude 支出控管（spend controls）功能上線

- **官方推出企業支出控管功能**：Tech Times 報導（07-04），企業導入 agentic AI 後帳單頻繁超出預算成為普遍痛點，Anthropic 針對企業客戶推出 Claude 支出控管功能協助管理成本。**注意**：報導僅描述功能定位，未揭露具體控管粒度（部門/團隊層級預算上限、per-user 報表、即時警報等 [[topics/enterprise-cost-management]] 長期呼籲的功能是否齊備）；是官方首次針對企業成本失控問題推出產品化解法，而非僅靠配額縮減或計費政策調整（推論：對正面臨 Uber 式成本失控的企業客戶構成留存誘因）。詳見 [[topics/anthropic-business]]、[[topics/enterprise-cost-management]]（Tech Times https://www.techtimes.com/articles/319687/20260704/claude-enterprise-spend-controls-arrive-agentic-ai-bills-blow-past-budgets.htm）

#### 2026-07-03：印度盧比定價需求（✅ 已於 2026-07-13 獲官方回應，見上方 07-13/14 條目）

- **GitHub Issue 要求 INR 在地化定價方案（持續發酵，互動量攀升）**：印度用戶在 `anthropic/claude-code` Issue #17432 要求 Anthropic 推出盧比計價方案，比照 OpenAI（ChatGPT）、Google（Gemini）已有的在地化定價。互動量持續攀升：留言數維持 **205**、reactions 由 👍594 增至 **598**（2026-07-09 查證），為近期社群需求類 issue 中互動量顯著較高者之一。**注意**：純社群 feature request，Anthropic 至今（07-09）仍無官方回應或時程承諾；若 Anthropic 未來跟進在地化定價，將直接影響印度市場（全球最大 AI 開發者社群之一）的訂閱轉換率（推論）（GitHub https://github.com/anthropics/claude-code/issues/17432）
- **✅ 已解決（2026-07-13 更新）**：Anthropic 於 07-13 正式推出印度盧比計價（Pro 方案 Rs 2,000/月），為此需求首次獲得官方正式回應，長期無回應狀態結束；詳見上方「2026-07-13/14：印度盧比在地化定價正式推出」條目

#### 2026-07-02：第三方實測確認 Sonnet 5 促銷定價，籲設為預設路由模型

- **dev.to 第一手定價實測**：作者計算確認 Anthropic 已將 Sonnet 5 以 $2/$10（每百萬 token）廣泛開放，優惠將持續至 **2026-08-31**，與官方 07-01 公告數字一致；文章建議開發者應將 Sonnet 5 設為**預設路由模型**而非僅作為用量上限的備援，以最大化促銷期內的成本節省（dev.to https://dev.to/tokenmixai/i-did-the-math-on-claude-sonnet-5-the-60-opus-discount-is-real-but-temporary-31pf）
- **注意**：優惠當時明確為「temporary」，8/31 後走向未見公告 —— **後續（2026-08-10）：Anthropic 宣布此定價永久化，取消 9/1 漲價，本則的到期風險已解除**（見下方 2026-08-10 條目）

#### 2026-07-01：Claude Sonnet 5 促銷定價 + Fable 5 計費架構調整

- **Claude Sonnet 5 促銷定價**：$2/Mtok（輸入）、$10/Mtok（輸出），發布時載明有效期至 2026-08-31（**該到期日後於 2026-08-10 取消，定價永久化**）；Claude Code 用戶以此定價使用新預設模型，相較 Opus 4.8 估計省 60% 成本。**對採用率的意涵**：若 Claude Code 預設路由切換至 Sonnet 5，重度使用者的月均 API 費用可能顯著降低，有助於緩解近期配額縮減導致的訂閱留存壓力（推論）。
- **Fable 5 計費架構調整**：Pro/Max/Team 方案 2026-07-07（7/7）前每週配額含 50% Fable 5；2026-07-07 後改為 usage-based billing（依用量計費）；Enterprise 方案需聯繫帳戶主管確認條件；定價細節另行公告。**注意**：此架構意味 7/7 後 Pro/Max 訂閱用戶使用 Fable 5 將不再包含在訂閱配額內，須另計費用；對重度使用 Fable 5 的用戶構成成本衝擊風險（推論）。**與 06-09 舊公告銜接說明**：06-09 條目記錄 Fable 5「6/22 前含括於訂閱、之後改為消費制」，本次公告明確 6/22–7/7 為過渡期（每週配額仍含 50% Fable 5），7/7 才是 usage-based billing 正式生效日；兩則公告方向一致、非互相矛盾，但 Anthropic 並未使用「過渡期」字眼，此銜接判斷為由兩則公告推得（推論）。此調整與同日公布的 Sonnet 5 促銷定價同屬毛利率相關政策，對公司財務面的意涵詳見 [[topics/anthropic-business]]。

**2026-06 定價與促銷**：Fable 5 定價發布（06-09）——$10/$50 per Mtok、context window 1M，6/22 前訂閱內含、之後改按用量計費；Mythos 5 定價更高、細節未公開；30 天資料保留政策涵蓋 AWS Bedrock；06-21 新增 AWS Bedrock 強制 provider data sharing 條款。社群一度誤植 Max 5x 為 $50/月（06-26），已依 05-14 官方公告更正為 Max 5x $100／Max 20x $200，雙 Max 5x 帳號可並行兩個 session 的性價比論點仍成立。原始條目見 [[entities/pricing-archive#2026-06]]。

**2026-05 定價與促銷**：模型別名退役警示＋Max 方案實質差異說明（05-23）、Anthropic 定價主導權強勁（05-13）。完整記錄見 [[entities/pricing-archive#2026-05]]。

## 成本案例與優化

- **訂閱制對 API 計費的價差已由三個獨立方法論量化在 40–44 倍區間**：Quesma（40 倍，2026-08-11）、modelplane.ai（44 倍，2026-07-23）、cookbook-meter 使用量換算（2026-08-14）互相佐證。
- 具名企業案例、省錢策略與完整時序見 [[topics/enterprise-cost-management]]，本頁不重複列。
- 個人層級費用失控事件（$6,000 徹夜運行、30 天 $514 成本分析等）已併入該頁時序。

---

## 相關

- [[entities/pricing]]：母頁，現在生效的規則、牌價與方案表
- [[entities/pricing-incidents]]：計費事故與額度異常
- [[topics/model-comparison]]：同一份工作換模型差多少
- [[topics/enterprise-cost-management]]：具名成本案例與省錢方法
- [[entities/pricing-archive]]：2026-04～06 的原始條目
