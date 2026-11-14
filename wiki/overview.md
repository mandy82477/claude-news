# Claude / Anthropic 生態系概覽

**最後更新：** 2026-11-14
**更新頻率：** 🗓️ 週更（每週檢視一次；更新日期停留數天屬正常節奏）

---

## 當前局勢

**IPO 進入最後一週，數字第一次是官方自己給的**：11-10 官方路演公告載明擬發 **825,000,000 股** A 類（公司自售 801,351,354 股）與每股 **$70～78** 價格區間；11-13 媒體稱路演認購約達**六倍超額**，區間與時程未變。11-12 官方 IPO 頁首度公布 Q3 財務：**單季營收 $170 億**、9 個月累計 $330 億、**單季淨損 $233 億（其中約 $219 億是可轉債等公允價值變動的非現金費用）**、GAAP 營業利益率 **(3)%**、年營收 $10 萬以上客戶**逾 11,900 家**。事實層見 [[topics/anthropic-ipo]]，判讀層見 [[topics/market-signals-ipo]]。**掛牌日（傳 11-19、定價傳 11-18）在本輪仍只有媒體與官方 IPO 頁兩種來源**，本輪雲端環境讀不到官方 IPO 頁、未能自行複核，詳見該頁懸置標記。

**Fable 5.2 成為新預設旗艦，而且降價**：11-09 發布，**$8／$40**（前代 Fable 5.1 為 $10／$50，降約兩成）、1M context、快取讀取為基礎輸入價的 2.5%、知識截止 **Jun 2026**、退役**不早於 2027-11-09**（官方模型總覽頁，2026-11-14 查證）。同日發布信任機構限定的 **Mythos 5.2**（同為 $8／$40）。官方遷移指南列出**四項破壞性變更與三項行為變更**——換代前先讀那一節，見 [[entities/fable-5]]。

**Claude Dispatch：官方確認有缺陷，但決定不修**：11-05／11-06 兩個來源披露 Claude Dispatch 可讓攻擊者跨企業邊界執行遠端指令，官方確認後**決定不修補**。這是目前站上風險最高、且官方明示不會補的一條；在企業環境開了 Dispatch 跨團隊功能的管理者要自己收權限。另 10-26／10-27 披露的 **Downloads 資料夾任意指令檔**至今官方無回應。攻擊面 11 列本輪全查、全數維持，見 [[topics/ai-agent-safety]]。

**Monitor tool 進了 stable**：npm `stable`＝**2.1.311**、`latest`＝**2.1.325**（2026-11-14 查證）。這一跨讓 Monitor tool（2.1.310）不再需要 latest；只有寫入邊界設定 `blockWritesOutsideWorkingDirectories`（2.1.314，預設關）還留在 latest。v2.1.323 另推出實驗性 **Code Mode**（Research Preview）。見 [[entities/claude-code-releases]]、[[entities/claude-code]]。

**三件法律戰同時開線**：11-13 Anthropic 因「**Mythos**」模型名稱遭控商標侵權；同日非營利組織提告要求凍結「AI 軍備競賽」；**紐約州 AI 安全法**本輪生效。加上既有的音樂著作權與專利訴訟，法律面已是 IPO 定價前最密集的一週，見 [[topics/market-signals-legal]]、[[topics/anthropic-government-policy]]。

**Whiteboards／Sheets／Data 上線，而且吃你原有的額度**：11-10 官方推出 Claude Whiteboards 與 Sheets（beta），Dashboards 轉正式版並更名 **Claude Data**；Enterprise 的 Claude Data **2026-11-20 起預設開啟**。本輪查官方說明中心確認：這些 artifact **沒有獨立配額**，吃的是你既有的方案用量、與 Claude Code 共用；Team／席次制 Enterprise 由席次額度扣、管理員可加購 usage credits；唯一例外是 Claude Meetings 通話中建立的 artifact 至 **2027-02-10** 前免費。見 [[entities/pricing]]。

**usage credits 的到期規則查清了**：**2026-12-07 之前買的不會到期**；該日起買的在購買日後 **12 個月**到期。官方只寫「部分國家到期日可能不同」，**未點名日本、也未載 6 個月**那個數字（2026-11-14 查官方說明中心），細節指向 Consumer Credit Terms。這解掉了 11-07 官方改版後懸著的一題，見 [[entities/pricing]]、[[entities/pricing-history]]。

**本輪站內最值得記的事實面修正**：`entities/opus-5`「你現在拿到的是什麼」表距今 68 天，對官方模型頁重查後改一列——**官方已不再建議拿 Opus 5 起手**（官方標為 Active (legacy)、建議遷移到 Opus 5.5），牌價、知識截止（May 2026）與退役日（不早於 2027-07-24）複查一致。另 [[topics/ai-agent-safety]] 原寫「stable 是 2.1.308」已更正為 2.1.311；feature-radar 有 1 條因近 4 週零提及降一格熱度，**API Inference Hooks 則因 11-05 官方 Help Center 已列入 Enterprise 功能，由 ⏳ 觀望升為 ⚡（限 Enterprise）**。

## 主要模型現況

> 牌價、知識截止與退役日為 **2026-11-14 官方模型總覽頁與各模型頁查證**。

| 模型 | 狀態 | 備注 |
|------|------|------|
| **Claude Fable 5.2** | 🟢 旗艦（2026-11-09 發布，取代 Fable 5.1）| $8／$40（降約兩成）；1M context／128K 輸出；預設 effort `high`、thinking 恆開；知識截止 Jun 2026；退役不早於 2027-11-09；**官方遷移指南列四項破壞性變更** |
| **Claude Mythos 5.2** | 🟢 政策限定（2026-11-09 發布）| 僅限信任機構（Cyber Verification 等計畫）；$8／$40 |
| **Claude Opus 5.5** | 🟢 現行 Opus | $4／$20；快取讀取為輸入價 5%；預設 effort `medium`（Opus 5 為 `high`）；知識截止 Jun 2026；退役不早於 2027-09-22 |
| **Claude Sonnet 5.5** | 🟢 現行 Sonnet | $2／$10；知識截止 Jun 2026；退役不早於 2027-09-28；Models API 回報它**不接受關閉 thinking**、可用 `between_tools` |
| **Claude Haiku 5.5** | 🟢 現行 Haiku | From $0.10／$0.50；**唯一按 prompt 長度計價的現行模型**（逾 10 萬 token 改高一檔）；退役不早於 2027-10-07 |
| Claude Fable 5.1 | ⚠️ Legacy（2026-11-09 起）| 仍可呼叫，$10／$50 |
| Claude Mythos 5.1 | ⚠️ Legacy | 仍限信任機構，$10／$50 |
| Claude Opus 5 | ⚠️ Legacy｜官方標 Active (legacy) | $5／$25、快取讀取 $0.50；知識截止 May 2026、退役不早於 2027-07-24；**官方已不建議新採用、建議遷移 Opus 5.5**（2026-11-14 複查）|
| Claude Sonnet 5 | ⚠️ Legacy | $2／$10；退役不早於 2027-06-30 |
| Claude Opus 4.8 | ⚠️ Legacy | 仍是 Fable 系**資安類**請求被護欄攔下時的接手模型；**fast mode 已宣告淘汰、2026-11-30 移除** |
| Claude Opus 4.7／4.6、Sonnet 4.6、Haiku 4.5 | ⚠️ Legacy | 仍可選用；4.7 起為新 tokenizer（同文字約多 30% token）|

> 快速選型與情境推薦見 **[[topics/model-comparison]]**；跨家任務榜單見 **[[topics/model-task-leaderboard]]**（本輪因雲端網路未開放榜單網域未更新）
> 現行模型頁的「跟它怎麼說話」節均已從官方 prompting 指南補齊——**換代時哪幾句 prompt 要加、哪幾句要刪**看那一節。同一句話在相鄰兩代常是相反的藥。

---

## 進行中議題

### 🔴 高度關注

1. **[[topics/anthropic-ipo]] — 定價前最後一週，官方數字與媒體時程並存**
   - $70～78 區間、825M 股、約六倍超額認購；Q3 單季營收 $170 億但淨損 $233 億（含 $219 億非現金）；掛牌日本輪未能自行向官方頁複核
2. **[[topics/ai-agent-safety]] — Claude Dispatch 官方確認但不修補，Downloads 資料夾仍無回應**
   - 攻擊面表 11 列滿載、本輪全查全留；下輪先看 Gmail 代寄（判定日 11-17）與套件供應鏈（11-27）兩列
3. **[[topics/market-signals-legal]] — 三條法律線同週開啟**
   - Mythos 商標侵權、AI 軍備競賽凍結訴訟、紐約州 AI 安全法生效
4. **[[entities/claude-code-known-issues]] — 多起錯誤升高事故與 Microsoft 365 同步故障**
   - 11-13 claude.ai／Claude API／Claude Code 同期事故；逾期待查證筆數本輪為站上最高

### 🟡 持續追蹤

5. **[[topics/anthropic-business]]**（ongoing）— 指標表 10 列滿載，官方估值那一列資料日期將於 11-24 滿 180 天
6. **[[topics/anthropic-government-policy]]**（ongoing）— 八條政府線在動，其中**三條已改到你手上的 Claude**（地區存取、隱形浮水印、高風險請求換模型）
7. **[[topics/competitor-landscape]]**（ongoing）— 戰場仍在「誰更便宜」；Schwab 自建 MCP 動搖獨家 LLM 地位
8. **[[topics/code-quality-decline]]**（ongoing）— 三條線本輪對 GitHub issue 實查：#41930 已結案、#65687／#77136／#83510 仍開啟
9. **[[topics/community-pattern-trends]]**（ongoing）— 跨 Session 記憶層持續成形；context-mode（33,266★）本輪入目錄
10. **[[topics/official-community-gap]]**（monitoring）— 18 列全在 11-08 核過；H-6db5d4 評估後判定不開新列（表滿 18/18）
11. **[[topics/market-lessons]]**（monitoring）— 本輪由 ongoing 下修，週更教材頁
12. **[[topics/recursive-self-improvement]]**（ongoing）／**[[topics/ai-eval-boundary-incidents]]**（本輪下修 monitoring，距最後新聞 18 天）
13. **[[topics/safety-china-trust-dispute]]**（monitoring，已宣告新鮮度豁免——刻意停在 07-11，之後見政策頁）

---

## 近期重大事件（2026-11-08 至 2026-11-14）

| 日期 | 事件 | 影響 |
|------|------|------|
| 11-13 | **Mythos 商標侵權訴訟**、非營利組織訴請凍結 AI 軍備競賽、IPO 路演約六倍超額、**Claude Code v2.1.323 推出 Code Mode**、claude.ai／API／Claude Code 多起事故 | 法律與事故同週加壓，定價前最密集 |
| 11-12 | **官方 IPO 頁公布 Q3 財務**（營收 $170 億、客戶逾 11,900 家）；招股書稱已達 RSP 安全標準；**Managed Agents 可自架**；Claude for Manufacturing | 財務首度官方化 |
| 11-10 | **官方路演公告**：825M 股、$70～78；**Whiteboards／Sheets（beta）與 Claude Data 上線**（Enterprise 的 Data 11-20 起預設開啟）| IPO 價格首次官方化；工作區產品線補齊 |
| 11-09 | **Claude Fable 5.2／Mythos 5.2 發布**（新預設旗艦、降價兩成、1M context）| 旗艦換代，四項破壞性變更 |
| 11-05～11-06 | **Claude Dispatch 安全缺陷官方確認但不修補**；Personal Finance（beta）；官方 Help Center 列入 inference hooks | 站上唯一「官方明示不修」的攻擊面 |

> 完整事件時序見各 topics 頁面「時序」區塊；[[log]] 含每日更新完整紀錄。

---

## 社群工具生態

社群工具目錄（[[topics/community-tech-tools]]）本輪（news 窗口 2026-10-31～11-13）**新增 52 筆、移出 15 筆**，目錄由 206 列增至 **243 列**；另對 56 列逾 30 天零後續者加註首見日。

- 🔥🔥🔥🔥 **Context／記憶層** — context-mode（33,266★）本輪入目錄並進決策表細節；「記住失敗」仍無第三方使用回報
- 🔥🔥🔥🔥 **「它說做完了但沒做」** — claim-check（11-12 dev.to，作者自測擋 86 則）與首選 Groundtruth 同解一題；Groundtruth 僅 7★且 07-20 後未更新，**下輪應複查是否換首選**
- 🔥🔥🔥 **手機／遠端操控 Claude Code** — t3code（forks 10,774）、cc-desk-tunnel、Aq 同期出現
- 🔥🔥🔥 **大型 codebase 並行規模化** — 見 [[topics/community-large-codebase-workflow]]

> 功能熱度評分與試用推薦見 **[[feature-radar]]**；社群趨勢週更見 **[[topics/community-pattern-trends]]**

---

## 商業動態

- **IPO 與財務**：$70～78 區間、825M 股、約六倍超額；Q3 單季營收 $170 億、淨損 $233 億（約 $219 億為非現金公允價值變動）、GAAP 營業利益率 (3)%、調整後 15%
- **客戶**：年營收 $10 萬以上客戶逾 11,900 家、年增逾 12 倍（官方 IPO 頁 11-12）
- **算力承諾**：採購承諾總額 $8,950 億，其中 $4,475 億預計 2030 年底前支出完畢（修訂版 S-1）
- **通路**：Schwab 自建 MCP，動搖其獨家 LLM 地位（11-13）；Claude for Manufacturing 推出（11-12）
- **風險**：風險表 6 列本輪全查全留（最舊 09-06，未逾 90 天）；音樂出版商訴訟升級、AI 損失恐超出保險業承保能力
- **定價**：Fable 5.2 降價兩成；長脈絡**除 Haiku 5.5 外全為標準價**（2026-11-14 複查一致）；usage credits 到期規則見上方

---

## 功能試用推薦（快速查閱）

| 功能 | 熱度 | 推薦 |
|------|------|------|
| Claude Fable 5.2／Mythos 5.2（新預設旗艦）| 🔥🔥🔥🔥🔥 | ✅ 強烈推薦（自動套用）——但**先讀官方遷移指南的四項破壞性變更** |
| Claude Duet（主動式 agent，研究預覽）| 🔥🔥🔥🔥🔥 | ⏳ 觀望——技術細節仍未公開 |
| Claude Code 讀取 AGENTS.md（v2.1.277）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——無 CLAUDE.md 時原生改讀，回應 #6235 |
| Auto mode 免計費 server-side classifier | 🔥🔥🔥🔥 | ✅ 強烈推薦——API／Enterprise／閘道器用戶不再被收分類器費用 |
| Claude Whiteboards／Sheets／Data | 🔥🔥🔥 | ⚡ 有條件推薦——**吃你原有的方案額度、無獨立配額**；Enterprise 的 Data 11-20 起預設開啟 |
| API Inference Hooks（Enterprise）| 🔥 | ⚡ 有條件推薦（限 Enterprise）——11-05 官方 Help Center 已列入 |
| Code Mode（v2.1.323，Research Preview）| 🔥 | ⏳ 觀望——11-13 剛推出 |

> 完整功能熱度評分、**升上去會遇到什麼**與倒數中事件見 **[[feature-radar]]**
> 本輪 1 條條目因近 4 週日報零提及而降一格熱度（Claude Code v2.1.285）；⏳ 逾 90 天的 9 條已逐條處置（升 1、加註或明寫在等什麼 3、已加註者跳過 5）

---

## 社群情緒指標

- HN 討論熱度：🔥🔥🔥🔥 高（Fable 5.2 換代、IPO 定價週、Whiteboards／Sheets 官方文 273 分）
- Reddit 情緒：😤 成本與品質疑慮延續；11-13 多起事故當日「Claude Code Is Down」討論再起
- 開發者工具活躍度：📈 明顯升溫（本輪策展新增 52 筆、目錄 243 列；手機遠端操控與 Context 管理同期爆發）
- 信任指標：↘ 走弱（**Claude Dispatch 官方確認卻不修補**、Downloads 資料夾無回應、提示注入已產業級）
- 競爭壓力：🟡 中（Fable 5.2 降價兩成回應價格戰；Schwab 自建 MCP 顯示大客戶開始去獨家化）
