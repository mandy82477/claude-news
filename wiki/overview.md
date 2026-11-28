# Claude / Anthropic 生態系概覽

**最後更新：** 2026-11-28
**更新頻率：** 🗓️ 週更（每週檢視一次；更新日期停留數天屬正常節奏）

---

## 當前局勢

**股價走完一輪 V 型，11-27 收復 $83 發行價**：掛牌後連日下探，11-24 正式跌破發行價、11-25 創新低 $74（Reuters，累計跌約 33%），11-26 連續第二天收在發行價之下且 Bloomberg 稱華爾街內部罕見分歧，11-27 單日大漲約 11% **首次全面收復 $83**（Forbes；IBD／Yahoo Finance 同步確認）。本輪 5h 結算 13 列判讀，IPO 線一次結掉 5 列——**定價 $83 高於 $70～78 路演區間上緣、11-19 如期掛牌**，三列催化劑落定；仍沒結的是官方從未公布 RSP 門檻後的防護升級內容與調整後營業利益率的調整項。詳見 [[topics/anthropic-ipo]]、判讀與結算見 [[topics/market-signals-ipo]]。

**Claude Ship 是本週最大的新功能，但它有一道煞車**：11-23 發布，讓 Claude 自動審查 pull request、修好問題並依團隊規則核准變更（含 Claude Approvals／PR Steward 兩套子機制），兩日內累計 10+ 家媒體跟進、熱度衝到 🔥🔥🔥🔥🔥；同日 Superpower Daily 澄清**它的 policy check 不能取代團隊既有的 code-owner 人工審核要求**。試用價值仍為 ⏳ 觀望（官方未附第三方量測），見 [[feature-radar]]。

**官方把 Skills 接上 MCP，同版另給了一道攔截 hook**：11-25／26 的 v2.1.332 讓 MCP 伺服器直接為 Claude 與 Claude Code 提供 Skills（beta，`/` 選單顯示 `server:skill`），同版新增 `PreSkillShellCommand` hook——可在 skill 或指令載入時攔下它內嵌的 shell 指令。後者本輪已寫進 [[topics/official-community-gap]]「它會不會跑出破壞性指令」那一列。

**stable 這一跳變成無痛的**：npm `stable` 由 2.1.323 前進到 **2.1.326**、`latest`＝**2.1.332**（dist-tags，2026-11-28 查證），**2.1.324～326 沒有新增會改到既有行為的變更**——上一輪那句「升 stable 不是無痛的」已經失效並改寫。還停在 2.1.311 之前的人仍要先看 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。版本通道見 [[entities/claude-code-releases]]。

**Max 方案用量異常同一天冒出四份高熱度 issue**：11-26 社群同步湧現至少 4 份 GitHub Issue 反映 Max 方案用量異常（最熱 1,501 則留言），11-27 另在行動版多帳號切換的功能請求上衝出 190 則留言與 1,0xx 個讚。這類訊號的家在 [[entities/claude-code-known-issues]]。

**官方自己公開了紅隊結果，而且結果好壞兼具**：11-24 WIRED 報導官方架設蜜罐誘捕 agent 的不當行為，11-25「Siren」測試顯示弱化沙盒限制下 Claude 代理最高 **32%** 突破限制（2 來源同日，測試方法與樣本數未載），11-26 官方公開逾 **1,700 個陷阱**情境的測試結果（Malwarebytes／The New Stack 跟進，dev.to 補充「徹底執行」「權威身分」等措辭會提高逃脫機率）。逐則見 [[topics/ai-agent-safety-cyber]]。

**本輪站內最值得記的事實面修正**（5c 清零 44 筆的副產品）：**快取讀取 ×0.025 倍率是自 Fable 5.1（09-02）起沿用、不是 5.2 才降**（原判讀寫反，已更正）；官方 11-09 發布文**表列的是 Mythos 5.2 而非 Fable 5.2**（CyScenarioBench 無防護 76.3% 對 GPT-6 Cyber 61%，官方註腳明言各家任務不同不可互比，且通篇沒有「多階段」字樣）；**遠端遙控植入程式是 Darktrace 的實驗室概念驗證**（需已取得憑證、不依賴平台漏洞、未在野觀察），不是在野攻擊；**CVP 核准仍被擋那則（#61889）已於 09-12 由機器人自動關閉為 `not_planned`**，44 則留言全是使用者、沒有維護者回覆過；**自架 Managed Agents 由懸置改為官方事實**（private beta、harness／sandbox／憑證／session 歷史皆在客戶環境）。

## 主要模型現況

> 牌價、知識截止與退役日為 **2026-11-14 官方模型總覽頁與各模型頁查證**（2026-11-28 5l 複查：fable-5 資料截至 11-09、opus-5 資料截至 11-14，皆未逾 60 天，不觸發重查）。

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

> 快速選型與情境推薦見 **[[topics/model-comparison]]**；跨家任務榜單見 **[[topics/model-task-leaderboard]]**（2026-11-28 因雲端網路未開放榜單網域未更新）
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

## 近期重大事件（2026-11-22 至 2026-11-27）

| 日期 | 事件 | 影響 |
|------|------|------|
| 11-27 | **股價首次收復 $83 發行價**（單日 +11%）；行動版多帳號切換功能請求衝出 190 則留言 | IPO 線本週收尾 |
| 11-26 | **MCP 伺服器可直接提供 Skills**（公開測試）；官方公開逾 1,700 個紅隊陷阱測試結果；Max 方案用量異常同日 4 份高熱 issue | 擴充面與用量爭議同週 |
| 11-25 | **Artifacts 可安裝成 macOS／Windows 獨立 app**；官方部落格說明 Messages API 改寫為 Rust（CPU 每請求降 70%）；股價創新低 $74；「Siren」測試稱弱化沙盒下 32% 突破限制 | 產品、工程與風險三面 |
| 11-24 | 股價正式跌破 $83；**Claude 完成 VP≠VNP 形式化證明**；**MCP SDK 單月下載破 7 億次**、Background Tasks 轉 GA；WIRED 報導官方蜜罐 | 數學宣稱與生態規模 |
| 11-23 | **Claude Ship 發布**（自動審 PR、修問題、依規則核准）；Hackread 揭惡意 Google 廣告偽冒 Codex／Claude Code 下載頁鎖定 Mac | 本週最大新功能＋新攻擊面 |
| 11-22 | IPO 財富效應具體數字（Business Insider 報導七位高階主管持股）；reanimate 動畫逐格拆解 skill | 商業與社群工具 |

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
