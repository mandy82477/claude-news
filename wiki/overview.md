# Claude / Anthropic 生態系概覽

**最後更新：** 2026-11-21
**更新頻率：** 🗓️ 週更（每週檢視一次；更新日期停留數天屬正常節奏）

---

## 當前局勢

**IPO 從定價走完到結算，然後股價就跌了**：官方 11-18 以每股 **$83** 定價，11-19 以代號 **ANT** 在 Nasdaq 掛牌（開盤 $111.50、盤中一度 $114.99），11-20 官方公告超額配售權全額行使、發行上修至 **11.27 億股**，結算毛額約 **$935 億**、實收約 **$916 億**，為史上規模最大 IPO。但掛牌第二天股價較前一日再跌逾 **11%**，同日那斯達克綜合指數抹平 2026 全年漲幅。市值估算各家口徑不一（Reuters 稱盤中近 $2 兆後回落約 $1.2 兆，WSJ 稱 $1.5～2 兆）。事實層見 [[topics/anthropic-ipo]]，判讀層見 [[topics/market-signals-ipo]]。

**Gemini 4 Neon 直接對著 Opus 5.5 打**：11-19 Google 發布 Gemini 4 Neon 並同步上線 GitHub Copilot，官方稱程式撰寫能力追平 Claude Opus 5.5、**API 價低 25%**；同期 OpenAI Astra 6.2 被報導在速度與成本上優於 Claude Fable 5.2，但 12 項任務輸 7 項。價格戰這一輪輪到對手降價，見 [[topics/competitor-landscape]]。

**stable 通道一次跳 12 個版號，這一跳不是無痛的**：npm `stable` 由 2.1.311 升到 **2.1.323**、`latest`＝**2.1.330**（dist-tags，2026-11-21 查證）。本站核對過的破壞性變更**現在全部落在 stable 裡**——寫入邊界設定（2.1.314）、auto mode 在 LLM gateway 下不再退回舊分類（2.1.319）、Fable 5.2 成為預設 Fable（2.1.321），加上預設關閉的實驗性 **Code Mode**（2.1.323）。**停在 2.1.311 的人升 stable 會一次吃下這幾項行為改變**，升之前逐列看 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。

**護欄的切換類別由四類收斂為三類，前沿 LLM 開發現在也有接手模型**（本輪對官方說明中心查證）：官方文件標題已再度更名為〈Why Claude switched models in your conversation with Fable models〉，明載同一套機制涵蓋 Fable 5.2／5.1／5。現在會觸發切換的是**攻擊性資安**（接手 Opus 4.8）、**雙重用途生物**與**窄範圍前沿 LLM 開發**（兩者皆接手 Opus 5）。本頁此前寫「模型萃取」是第四個獨立類別、且前沿 LLM 開發「沒有繞法」，兩處都已失效並更正——distillation 分類器仍在，但官方只在計費段提到它。見 [[entities/fable-5]]。

**官方 Fable 5.2 專屬 prompting 指南已出並逐條讀過**：解掉 11-09 起懸著的一題。和 5.1 最不一樣的三件事——effort 級距跨代不等量、照搬 5.1 的值是白花錢；長任務「還沒做完就收手」官方給了可貼的 system prompt 段落，但代價是輸出 token 多三成、它問你的次數變少；**「這份程式碼是你的」那一句**會把重複程式碼收斂率由不到 10% 推到約 75%，同時輸出 token 多 70–80% 並做沒人要求的改動。另有新的拒絕類別 `reasoning_extraction`。見 [[entities/fable-5#跟它怎麼說話]]、[[entities/mythos]]。

**金融業三家同週導入，數學與物理各出一個未經同行審查的宣稱**：Barclays／Citadel／BNY 將 Claude 導入工作流（11-20）；同日 Anthropic 數學家 Levent Alpöge 聲稱與 Claude 合作找到黎曼猜想的證明（**尚未經同行審查**，多家媒體以 unverified 措辭跟進），Anthropic Research 另發文稱 Claude 解開黑洞物理兩個懸置逾 20 年的理論問題（附預印本）。採用面見 [[topics/market-signals-customers]]。

**IPO 前夕的安全品牌質疑，本輪查出了具體內容**：聯名信〈The MisAnthropic Statement〉具名簽署人包含 Thomas Wolf、Igor Babuschkin、Steven Pinker、Max Tegmark 與 [[entities/gary-marcus|Gary Marcus]]，Center for AI Safety 亦加入，網站列 89 人；主張是 Anthropic 一邊警告遞迴自我改進 AI、一邊競相打造，並以安全品牌向投資人與大眾取得權力。Anthropic 回應稱自己有「業界最強安全防護之一」。評級那一則**本庫此前寫錯了評級方**：給出「商業倫理嚴重、人力資本高」評等的是 **Morningstar Sustainalytics**（報告日 11-16），ESG Dive 只是報導者，已更正。以上皆為媒體轉述、未讀到原文（`businesswire.com` 仍不在雲端網路白名單內）。見 [[topics/ai-agent-safety]]。

**本輪站內最值得記的事實面修正**：除上面兩條官方查證外，`feature-radar` 的「升級前要知道的」表由 22 列裁回規則上限 **12 列**（破壞性變更 8 列全留），被裁的 10 列事實先搬進 [[entities/claude-code-releases]] 才移出；`entities/claude-code-releases` 另把發布逾 90 天的 23 列版本搬進 [[entities/claude-code-archive]]。

## 主要模型現況

> 牌價、知識截止與退役日為 **2026-11-14 官方模型總覽頁與各模型頁查證**（本輪 5l 複查：fable-5 資料截至 11-09、opus-5 資料截至 11-14，皆未逾 60 天，不觸發重查）。

| 模型 | 狀態 | 備注 |
|------|------|------|
| **Claude Fable 5.2** | 🟢 旗艦（2026-11-09 發布，取代 Fable 5.1）| $8／$40（降約兩成）；1M context／128K 輸出；預設 effort `high`、thinking 恆開；知識截止 Jun 2026；退役不早於 2027-11-09；**官方遷移指南列四項破壞性變更** |
| **Claude Mythos 5.2** | 🟢 政策限定（2026-11-09 發布）| 僅限信任機構（Cyber Verification 等計畫）；$8／$40 |
| **Claude Opus 5.5** | 🟢 現行 Opus | $4／$20；快取讀取為輸入價 5%；預設 effort `medium`（Opus 5 為 `high`）；知識截止 Jun 2026；退役不早於 2027-09-22 |
| **Claude Sonnet 5.5** | 🟢 現行 Sonnet | $2／$10；知識截止 Jun 2026；退役不早於 2027-09-28；Models API 回報它**不接受關閉 thinking**、可用 `between_tools` |
| **Claude Haiku 5.5** | 🟢 現行 Haiku | From $0.10／$0.50；**唯一按 prompt 長度計價的現行模型**（逾 10 萬 token 改高一檔）；退役不早於 2027-10-07 |
| Claude Fable 5.1 | 🟡 前代（**官方 deprecations 表仍列 Active**，退役不早於 2027-09-01）| 仍可呼叫，$10／$50；新工作建議改用 5.2 |
| Claude Mythos 5.1 | ⚠️ Legacy | 仍限信任機構，$10／$50 |
| Claude Opus 5 | ⚠️ Legacy｜官方標 Active (legacy) | $5／$25、快取讀取 $0.50；知識截止 May 2026、退役不早於 2027-07-24；**官方已不建議新採用、建議遷移 Opus 5.5**（2026-11-14 複查）|
| Claude Sonnet 5 | ⚠️ Legacy | $2／$10；退役不早於 2027-06-30 |
| Claude Opus 4.8 | ⚠️ Legacy | 仍是 Fable 系**資安類**請求被護欄攔下時的接手模型；**fast mode 已宣告淘汰、2026-11-30 移除** |
| Claude Opus 4.7／4.6、Sonnet 4.6、Haiku 4.5 | ⚠️ Legacy | 仍可選用；**4.7 起換新 tokenizer**，同一份文字約 **1x–1.35x** token（官方遷移指南；計價頁另寫「約多 30%」，取決於內容）|

> 快速選型與情境推薦見 **[[topics/model-comparison]]**；跨家任務榜單見 **[[topics/model-task-leaderboard]]**（本輪因雲端網路未開放榜單網域未更新）
> 現行模型頁的「跟它怎麼說話」節均已從官方 prompting 指南補齊，**本輪 Fable／Mythos 兩頁已換成官方 5.2 版指南**——**換代時哪幾句 prompt 要加、哪幾句要刪**看那一節。同一句話在相鄰兩代常是相反的藥。

---

## 進行中議題

### 🔴 高度關注

1. **[[topics/anthropic-ipo]] — 已結算，戲份轉到股價與鎖定期**
   - $83 定價、11.27 億股、毛額約 $935 億；掛牌次日跌逾 11%；市值口徑各家不一，下輪看首份季報與解禁時程
2. **[[topics/competitor-landscape]] — Gemini 4 Neon 稱追平 Opus 5.5 且便宜 25%**
   - 對手這輪用降價回應降價；Astra 6.2 速度／成本佔優但任務勝率仍輸
3. **[[topics/ai-agent-safety]] — Claude Dispatch 官方確認但不修補的狀態未變**
   - 安全品牌質疑（聯名信、ESG 評級）**仍缺一手來源**，雲端網路白名單擋住查證，見「需使用者端設定」
4. **[[entities/claude-code-releases]] — stable 一次跳 12 版，破壞性變更全進 stable**
   - 停在 2.1.311 的人升級前必須逐列看 feature-radar 的升級表

### 🟡 持續追蹤

5. **[[topics/anthropic-business]]**（ongoing）— 金融業三家（Barclays／Citadel／BNY）同週導入；指標表官方估值那列資料日期 11-24 滿 180 天
6. **[[topics/anthropic-government-policy]]**（ongoing）— 八條政府線在動；遊說支出開線（兩家公司、合計已付 $163 萬）
7. **[[topics/enterprise-cost-management]]**（本輪由 ongoing 下修 **monitoring**，最後新聞 11-05）
8. **[[topics/code-quality-decline]]**（ongoing）— 本輪對 GitHub issue 實查：#41930 已結案、#65687／#77136／#83510 仍開啟，狀態與表上一致
9. **[[topics/community-tech-patterns]]**（ongoing）— 記憶層與「要它出示證據」兩路同時加厚；本輪工具目錄新增 34 筆
10. **[[topics/official-community-gap]]**（ongoing）— 18 列本輪對官方一手重核
11. **[[topics/market-lessons]]**（monitoring）／**[[topics/ai-eval-boundary-incidents]]**（monitoring）
12. **[[topics/recursive-self-improvement]]**（ongoing）— 黎曼猜想與黑洞物理兩個宣稱都未經同行審查，屬本頁射程
13. **[[topics/safety-china-trust-dispute]]**（monitoring，已宣告新鮮度豁免——刻意停在 07-11，之後見政策頁）

## 近期重大事件（2026-11-15 至 2026-11-21）

| 日期 | 事件 | 影響 |
|------|------|------|
| 11-20 | **IPO 結算完成**（11.27 億股、毛額約 $935 億）；次日股價再跌逾 11%；**Barclays／Citadel／BNY 導入**；兩個未經同行審查的研究宣稱 | 資本面落地、採用面擴張，研究宣稱待驗 |
| 11-19 | **IPO 定價 $83、以 ANT 在 Nasdaq 掛牌**（開盤 $111.50）；**Google Gemini 4 Neon 發布**並上線 GitHub Copilot（稱追平 Opus 5.5、API 低 25%）| 上市日與對手旗艦撞在同一天 |
| 11-18 | **IPO 定價最後階段**；Amazon／Google 合計持股近 30%；**安全品牌三面受質疑**（聯名信、評級、Altman）；遊說支出 $163 萬曝光 | 定價前夕的信任面壓力測試 |
| 11-17 | Claude Code v2.1.326：agent teams 可與 **Code Mode** 同開 | 實驗功能與多 agent 接上 |
| 11-16 | Jasjeet Sekhon（Google DeepMind 前策略長）離職加入 Anthropic 傳聞；Brad Gerstner 宣布 $50 億認購 | 人才與認購同週 |

> 完整事件時序見各 topics 頁面「時序」區塊；[[log]] 含每日更新完整紀錄。

---

## 社群工具生態

社群工具目錄（[[topics/community-tech-tools]]）本輪（news 窗口 2026-11-14～11-20）**新增 34 筆、移出 14 筆、另對 14 列逾 30 天零後續者加註首見日**，目錄現為 **280 列**。六個症狀列的首選**全部沒換**。

- 🔥🔥🔥🔥 **「它說做完了但沒做」** — 本週一次多三個證據導向的新做法：canary（500★，附錄影與 trace）、code-review-gate-skill（504★，發現項要附證據）、Gravitas（501★，移植到 Gemini）
  - 首選 Groundtruth 仍未換，但它只有 7★ 且 07-20 後未更新，**下輪該複查是否換首選**（已連兩輪掛在這）
- 🔥🔥🔥 **記憶層** — Memro（PostgreSQL＋pgvector 經 MCP 共享記憶）、Crosshead（compaction 後的身分保留）；兩個都只有單一來源、無使用回報
- 🔥🔥🔥 **費用監測** — tokendoctor（Show HN，HN 31 分）分析 token 浪費在哪；留言有人主張一味砍用量會犧牲品質
- 🔥🔥 **盯 agent 狀態** — Cyberviber（15 美元實體螢幕）、Fardesk（不經第三方伺服器的 iPhone app）

> 功能熱度評分與試用推薦見 **[[feature-radar]]**；社群趨勢週更見 **[[topics/community-pattern-trends]]**

---

## 商業動態

- **IPO 已結算**：$83／股、11.27 億股（含超額配售全額行使）、毛額約 $935 億、實收約 $916 億；掛牌次日股價較前一日跌逾 11%
- **股權結構**：Amazon 與 Google 合計持股近 30%（Amazon 約 14.7%，部分來自低換股價可轉債；TechCrunch 11-18）；Brad Gerstner 宣布 $50 億認購
- **客戶**：年營收 $10 萬以上客戶逾 11,900 家、年增逾 12 倍（官方 IPO 頁 11-12）；**金融業本週一次三家**（Barclays／Citadel／BNY）
- **算力承諾**：採購承諾總額 $8,950 億，其中 $4,475 億預計 2030 年底前支出完畢（修訂版 S-1）
- **競爭**：Gemini 4 Neon 稱追平 Opus 5.5 且 API 低 25%；Astra 6.2 速度與成本佔優但 12 項任務輸 7 項
- **政策支出**：兩家遊說公司活動於國務卿辦公室，合計已付 $163 萬（ZeroHedge 11-18，單一來源）
- **風險**：安全品牌質疑（聯名信、ESG「高風險」評級）**尚未查到一手來源**；音樂出版商訴訟升級仍在表上

---

## 功能試用推薦（快速查閱）

| 功能 | 熱度 | 推薦 |
|------|------|------|
| Claude Fable 5.2／Mythos 5.2（新預設旗艦）| 🔥🔥🔥🔥🔥 | ✅ 強烈推薦（自動套用）——**官方 5.2 prompting 指南已出，換代前連同四項破壞性變更一起讀** |
| Claude Duet（主動式 agent，研究預覽）| 🔥🔥🔥🔥🔥 | ⏳ 觀望——技術細節仍未公開 |
| Claude Code 讀取 AGENTS.md（v2.1.277）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——無 CLAUDE.md 時原生改讀，回應 #6235 |
| Auto mode 免計費 server-side classifier | 🔥🔥🔥🔥 | ✅ 強烈推薦——API／Enterprise／閘道器用戶不再被收分類器費用 |
| Code Mode（v2.1.323，已進 stable，預設關閉）| 🔥🔥🔥 | ⏳ 觀望——跟進報導稱 token 最多降 77%，但仍是實驗性選項；2.1.326 起可與 agent teams 同開 |
| Claude Whiteboards／Sheets／Data | 🔥🔥🔥 | ⚡ 有條件推薦——**吃你原有的方案額度、無獨立配額**；Enterprise 的 Data 11-20 起已預設開啟 |
| Claude Haiku 5.5 | 🔥🔥🔥🔥 | ⚡ 有條件推薦——成本比前代降約 75%，但**逾 10 萬 token 改高一檔計價** |

> 完整功能熱度評分、**升上去會遇到什麼**與倒數中事件見 **[[feature-radar]]**
> 本輪熱度降溫掃過 ≥🔥🔥 的 22 條，**降 0 條**（全部在近 4 週日報有真實提及，逐條看過原文）；⏳ 逾 90 天的 9 條中 8 條已加註、本輪無新後續故跳過，剩 1 條（Managed Agents Web Search 設定）本輪補加註

---

## 社群情緒指標

- HN 討論熱度：🔥🔥🔥 中高（IPO 掛牌週、Gemini 4 Neon 對標、Code Mode 跟進）
- Reddit 情緒：😤 成本與品質疑慮延續；掛牌次日股價話題壓過產品話題
- 開發者工具活躍度：📈 持續升溫（新增 34 筆、目錄 280 列；「要它出示證據」這一類一週出三個新品）
- 信任指標：↘ 走弱（**Claude Dispatch 官方確認卻不修補**未變；IPO 前夕安全品牌遭聯名信與 ESG 評級質疑，且本庫查不到一手來源）
- 競爭壓力：🔴 升高（Gemini 4 Neon 宣稱追平旗艦且便宜 25%，是本季最直接的一次對標）
