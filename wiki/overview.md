# Claude / Anthropic 生態系概覽

**最後更新：** 2026-10-31
**更新頻率：** 🗓️ 週更（每週檢視一次；更新日期停留數天屬正常節奏）

---

## 當前局勢

**公開版 S-1 已經在 SEC EDGAR 上，兩個日期不是同一件事**：10-21 首度揭露數字（2026 上半年淨損 **$807 億**、營收 **$163 億**，前一年同期 $11 億），10-26 **公開版正式出現在 SEC EDGAR**，官方同日公告擬掛牌代號 **ANT**、Class A 普通股。數字的關鍵在拆解：$807 億中約 **$720 億是可轉換工具隨估值上升產生的非現金帳列損失**，同期實際投入基礎建設與運算的現金約 $90 億。只看「虧 807 億」會把一家現金燒 90 億的公司讀成燒 807 億。公開版另揭露營收較前期成長 14 倍、Claude Code 企業大戶支出為一般用戶 20 倍。**價格區間與上市日仍未公布**。詳見 [[topics/anthropic-business]]、[[topics/anthropic-ipo]]、[[topics/market-lessons]]。

**寫入範圍終於有了硬邊界**：v2.1.314 新增 `permissions.blockWritesOutsideWorkingDirectories`——Write／Edit／NotebookEdit 在**任何權限模式下**都拒絕工作目錄外的路徑。這是官方在「它會不會跑出破壞性指令」這題上補的最後一塊（git 層與寫入路徑都已補），但**外部內容的信任邊界仍缺**，所以該題在對照表上從 ✅ 下修為 🧪 部分對應。另 v2.1.316 起 **Opus 4.8 的 fast mode 已宣告淘汰、2026-11-30 移除**，用它的人要遷到 Opus 5.5。詳見 [[topics/official-community-gap]]、[[entities/pricing]]。

**Downloads 資料夾：任何網站都能把指令檔丟進去，它會照著執行**：10-26／10-27 兩個獨立來源披露 Claude Code 與 Codex 會遵從 Downloads 資料夾內任意檔案的指令。官方至今無回應，觸發機制與是否需使用者額外動作均未見報導。這是本週站上風險最高且官方沒接的一條。詳見 [[topics/ai-agent-safety]]。

**第三方評估機構的存取範圍，官方自己講清楚了**：本輪查到官方〈獨立評估者更新〉原文——METR 有 6 名員工、取得公司硬體與內部工具，存取程度約與 Anthropic 自家風險評估團隊相當；Anthropic **不能否決 METR 發布**，但可要求遮蔽預定類別；文中**未**賦予中止部署權、也未給發布時程。SecureBio 正審查 8 月風險報告的化生武章節。這把 10-23 Metr 公開質疑那條線從「各說各話」推進到「權限邊界有官方文字可引」。詳見 [[topics/recursive-self-improvement]]、[[topics/ai-agent-safety]]。

**Agent Skills 交給基金會，官方獨自治理結束**：10-23 Anthropic 把 Agent Skills 開放標準捐贈給新成立的 Agentic AI Foundation（AAIF），治理權轉出；官方稱逾 70 個平台已整合。對照 MCP 的路徑，這是 Anthropic 第二次把自己定義的介面標準讓出來。寫 skills 的人短期不用改任何東西，但標準的變更節奏從此不由單一廠商決定。詳見 [[entities/claude-skills]]。

**Claude Duet：它會在你沒開口的時候動**：10-21～22 美國 Pro／Max 開放研究預覽，Opus 5.5 驅動的主動式 agent，獨立 iOS app。這是本庫第一個「不是你叫它才做事」的官方產品形態；10-26 官方另說明了「什麼擋著它不脫軌」。技術細節仍未公開，熱度極高但試用價值仍列 ⏳ 觀望。詳見 [[entities/claude-duet]]、[[feature-radar]]。

**監管與風險移轉同時加碼**：10-28 Anthropic 向加州州長表態，主張法院應有權封殺風險 AI 模型；10-29 起文字輸出隱形浮水印擴大至 Opus 4.7／4.6 與 Sonnet 4.6，**11/3 生效**（法源為歐盟 AI Act 透明度規範）。另一面，10-27 業界指出 AI 相關損失恐超出保險業承保能力——需為 AI 營運風險投保的企業採購方要先確認保單上限。詳見 [[topics/anthropic-government-policy]]、[[topics/anthropic-business]]。

**本週站內最值得記的事實面修正**：`entities/pricing` 的「通路與乘數」對官方計價頁重查後改兩項——**長脈絡標準價有 Haiku 5.5 這個例外**（逾 10 萬 token 改用 $0.50／$2.50 高一檔），以及 **fast mode 不再限第一方 API**（Opus 5.5 另可用於 Google Cloud 與 Azure 上的 Foundry）。另 `entities/claude-code` 原把 `rm` 防護的兩件事寫得像互相矛盾——2.1.287／288 補的是「always-ask 防線被繞過」的漏洞，2.1.309 才是把 bypass 模式的追問改為直接拒絕，而**後者不在 stable**；`topics/market-signals` 另清掉 15 處簡體「价」。

## 主要模型現況

| 模型 | 狀態 | 備注 |
|------|------|------|
| **Claude Fable 5.1** | 🟢 旗艦（2026-09-01 發布，取代 Fable 5）| 反萃取機制；快取讀取費率 0.025x（約省 75%）；官方 prompting 指南 2026-10-03 查證補進頁內 |
| **Claude Mythos 5.1** | 🟢 政策限定（2026-09-01 發布）| 僅限信任機構；Anthropic 研究稱中國 GLM-5.3 網攻能力已逼近 Mythos Preview |
| **Claude Opus 5.5** | 🟢 現行 Opus（2026-09-22 發布）| Claude Code v2.1.280 起為 `default`（Foundry 除外）；$4/$20；預設 effort 為 `medium`（Opus 5 為 `high`）|
| **Claude Sonnet 5.5** | 🟢 現行 Sonnet（2026-09-28 發布）| v2.1.284 起為 API 端預設 Sonnet；Terminal-Bench 4.0 由 10.3% → 70.6%；牌價維持 $2/$10，**快取讀取 $0.10（×0.05，本輪更正）**；退役不早於 2027-09-28 |
| Claude Opus 5 | ⚠️ Legacy（2026-09-22 起）| 仍可用，$5/$25、快取讀取 $0.50；**預設 effort `high`**（本輪查實，未被調高）、退役不早於 2027-07-24；跨代「重複修辭套路」問題持續（GitHub #77136）|
| Claude Sonnet 5 | ⚠️ Legacy（官方 2026-10-10 複查）| 仍可用，$2/$10、快取讀取 $0.20；**退役不早於 2027-06-30**、知識截止 Jan 2026（本輪查實）；預設地位已由 Sonnet 5.5 接手 |
| Claude Opus 4.8 | ⚠️ Legacy | 仍是 Fable 5／5.1 **資安類**請求被護欄攔下時的接手模型（生物／化學／生命科學類改由 Opus 5 接手）|
| Claude Opus 4.7 | ⚠️ Legacy（2026-10-03 官方總覽頁查證）| 本輪由「已被取代」更正為 Legacy |
| Claude Sonnet 4.6 | ⚠️ Legacy | 仍可選用 |
| **Claude Haiku 5.5** | 🟢 現行 Haiku（2026-10-07 發布）| From $0.10／$0.50、1M context、預設 effort `medium`；退役不早於 2027-10-07；**官方 prompting 指南 2026-10-17 查實已發布**，差異見頁內「跟它怎麼說話」|
| Claude Haiku 4.5 | ⚠️ Legacy（2026-10-17 官方總覽頁查證）| 退役下限 2026-10-15 已過，官方頁仍列於 Legacy（可用）、未宣布實際退役日；現行選項已是 Haiku 5.5，規格與選型見 [[topics/model-comparison]] |

> 快速選型與情境推薦見 **[[topics/model-comparison]]**；跨家任務榜單見 **[[topics/model-task-leaderboard]]**
> 五個現行模型頁（Fable 5.1、Mythos 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5）的「跟它怎麼說話」節均已從官方 prompting 指南補齊（前四頁 2026-10-03、Haiku 5.5 2026-10-17）——**換代時哪幾句 prompt 要加、哪幾句要刪**看那一節。同一句話在相鄰兩代常是相反的藥。

---

## 進行中議題

### 🔴 高度關注

1. **[[topics/anthropic-business]] — Q3 營收 168 億但季增放緩到 46%，IPO 估值預期開始下修**
   - 10-15 IPO 前最後一次揭露；AI 概念股同步下跌、紐約市主計官要求暫緩；10-16 Reuters 稱投資人轉趨保守
2. **[[topics/anthropic-government-policy]] — FTC 從開啟調查進到取證，白宮擬加通報義務**
   - 10-15 正式發出傳票；10-10 Axios 稱白宮擬要求比照通報「非預期行為」事故；八條線中三條已改到你的 Claude
3. **[[topics/ai-agent-safety]] — 桌面版 SneakPeek 揭露公開（08-17 已修），攻擊面 11 列全數維持**
   - 10-14 Noma Labs CVSS 8.7 與 CSO Online 256KB 預覽窗格外洩為同一漏洞，已於 08-17 修完（2026-10-18 查證）
4. **[[topics/enterprise-cost-management]] — 企業端開始自己裝上限，數字一路往下**
   - 10-16 Accenture 把員工 Claude 月費上限設在每月 29 美元（此前有員工單月花到 1,000）；09-17 摩根大通設的是 2,000

### 🟡 持續追蹤

6. **[[topics/competitor-landscape]]**（ongoing）— 戰場從「誰更強」移到「誰更便宜」
7. **[[topics/community-pattern-trends]]** — 跨 Session 記憶層／知識庫（趨勢九）已站穩成形
8. **[[topics/code-quality-decline]]**（ongoing）— 三條線只有 2026-04 那條有官方說法
9. **[[topics/enterprise-cost-management]]**（monitoring）— **自 2026-09-04 起無新消息（10-03 核）**，剩混合計費管理一項缺口無官方對應
10. **[[topics/ai-talent-flow]]** — AMD 以約 82 億美元收購 World Labs、Fei-Fei Li 出任首席科學家
11. **[[topics/anthropic-commitments]]**（monitoring）— Accenture 內嵌評估者為首個落地的「踩煞車」承諾
12. **[[topics/recursive-self-improvement]]**（ongoing）— 官方自評 Claude 負責內部模型開發約 26% 工作量（人時加權，官方頁 10-03 查證）
13. **[[topics/enterprise-tool-tracker]]**（ongoing）／**[[topics/official-community-gap]]**（ongoing）
14. **[[topics/safety-china-trust-dispute]]**（monitoring，已宣告新鮮度豁免——刻意停在 07-11，之後見政策頁）

---

## 近期重大事件（2026-10-17 至 2026-10-23）

| 日期 | 事件 | 影響 |
|------|------|------|
| 10-23 | **Agent Skills 捐贈給 Agentic AI Foundation**（官方獨自治理結束，逾 70 平台已整合）；Theorem 形式驗證研究；Metr 公開質疑官方安全說法 | 標準治理權轉出；第三方首度具名質疑自評數字 |
| 10-22 | **Claude Duet 開放研究預覽**（Opus 5.5 驅動的主動式 agent，美國 Pro／Max）；音樂出版商 Reservoir 控告 Suno 與 Anthropic | 第一個「不等你開口」的官方產品形態；著作權再開一條戰線 |
| 10-21 | **S-1 正式提交，首度揭露具體數字**：上半年淨損 $807 億、營收 $163 億（其中約 $720 億虧損為非現金帳列）；美國衛生部（HHS）將對 Anthropic 做出「唯一來源」聯邦採購 | IPO 財務口徑首次可查；政府端綁定加深 |
| 10-20 | 傳與 Nvidia 支持的 Nscale 洽談第二筆巨額算力合作；前 Google 執行長 Eric Schmidt 持有約 1% 股權於 IPO 前曝光；Citrini Research 揭露以 Claude 輔助設計蛋白質的研究方法 | 算力承諾續增；IPO 前股東結構曝光 |
| 10-19 | **捐出 5% 股權成立 Anthropic Public Benefit Fund**；媒體續報悄悄遊說國會版 AI 安全法案；第三方編碼平台 OpenCode 主控台資料外洩 | 公益結構入 IPO 敘事；第三方平台外洩波及存放其中的憑證 |


> 完整事件時序見各 topics 頁面「時序」區塊；[[log]] 含每日更新完整紀錄。

---

## 社群工具生態

社群工具目錄（[[topics/community-tech-tools]]）本輪（2026-10-17 整理，news 窗口 10-10～10-16）**新增 22 筆**、**移出 5 筆**（皆為「有條件推薦」逾 120 天且近 8 週無人再提），目錄現為 **164 列**；另有 14 筆「觀望」逾 30 天、近 4 週零後續，已逐筆加註「此後未見後續報導」。「我卡在這裡」決策表 10 列首選與次選**全數不變**——本輪沒有否定既有首選的證據，也沒有達「≥2 筆獨立需求證據」的新症狀。

- 🔥🔥🔥🔥 **跨 Session 記憶層／知識庫（趨勢九）** — 「記住失敗」本輪出現第一批工具（projectmem、hippo-memory），但仍**無第三方使用回報**
- 🔥🔥🔥🔥 **協調前移到寫碼前** — Foremerge 把衝突協調從合併時移到動工前，是大型 codebase 主線本輪最大的方向變化
- 🔥🔥🔥 **大型 codebase 並行規模化** — 見 [[topics/community-large-codebase-workflow]]
- 🔥🔥🔥 **額度／成本焦慮** — 企業端開始自己裝月費上限（Accenture 29 美元）；個人端要預警仍是 Claude-Code-Usage-Monitor

社群做法概覽（[[topics/community-tech-patterns]]）由 21 類收為 **19 類**——「MCP 長 Session 穩健化」「架構邊界合約」皆逾 60 天無新證據，已移到表下。討論盤點（[[topics/community-tech-discussions]]）現在還在吵的有 **6 場、僵住 3 場**；熱門討論表 5 列因逾期由 🌊延燒／☄️閃現 改標 🌙靜候。

> 功能熱度評分與試用推薦見 **[[feature-radar]]**；社群趨勢週更見 **[[topics/community-pattern-trends]]**

---

## 商業動態

- **營收與 IPO**：Q3 營收年增至 168 億美元、季增約 46%（10-15，IPO 前最後一次對投資人揭露）；消息後 AI 概念股下跌、紐約市主計官要求暫緩 IPO，10-16 Reuters 稱投資人開始下修估值預期
- **客戶與通路集中度（口徑已於 10-17 更正）**：招股書外流顯示 2025 年約 21.6 億美元、占營收 47% 是**經** Amazon 與 Google 的雲端市集銷售——那是通路不是客戶；兩家另代收應收帳款的 60%，另有兩家未具名客戶各占 12%（Reuters 獨家，機密草案階段，公開版 S-1 未遞交）
- **基建與融資**：Broadcom 晶片租賃融資 420 億 → 600 億美元（10-01／10-02／10-06 銀行團正式 launch，條款未見報導）；WSJ 稱 Tom Brown 牽線每月 12.5 億美元 SpaceX 運算交易（10-10，僅標題）
- **採用與成本控管**：Accenture 把員工 Claude 月費上限設在每月 29 美元（10-16）；Barclays 的「2026 年底 50% 開發者」是官方稿裡的**預期目標**，合約金額與席位數未載（10-17 查證更正）
- **政策**：FTC 10-15 正式發出傳票，從「開啟調查」進入取證程序；調查範圍與法源仍未公布
- **法律**：Sony Music／Warner（Warner Chappell）音樂著作權訴訟、UTRF 專利訴訟均進行中；另有四名訂閱戶 09-18 於加州北區聯邦法院提起擬議集體訴訟，主張「踩煞車」呼籲構成反壟斷合謀（媒體稱，法院文件未讀）
- **人才**：AMD 以約 82 億美元收購 World Labs，Fei-Fei Li 出任 AMD 首席科學家

---

## 功能試用推薦（快速查閱）

| 功能 | 熱度 | 推薦 |
|------|------|------|
| Claude Sonnet 5.5（API 預設 Sonnet）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——牌價 $2/$10 不變、快取讀取 $0.10；effort 級距已重新校準，**換過來要重跑一次 sweep** |
| Claude Code 讀取 AGENTS.md（v2.1.277）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——無 CLAUDE.md 時原生改讀，回應 #6235 |
| Claude Haiku 5.5（現行 Haiku）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——成本比前代降約 75%；**它是第一款有 effort 的 Haiku**，thinking 預設開著且算進 `max_tokens`，沿用 4.5 的 `max_tokens` 會把回覆截斷 |
| Claude Fable 5.1（旗艦）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——長時 agentic 工作流首選；`low` effort 下搜尋觸發會變少 |
| Claude Opus 5.5（現行 Opus）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——$4/$20；預設 effort 從 `high` 降為 `medium`，沿用 Opus 5 的設定會換到更長的回合 |
| Claude Mods（v2.1.287）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——**mod 讀得到你的 API Key、不受沙箱隔離**（官方明載）；只裝可信來源，裝前 `claude plugin validate` |
| Auto mode 免計費 server-side classifier（v2.1.278）| 🔥🔥🔥🔥 | ✅ 強烈推薦——API／Enterprise／閘道器用戶不再被收分類器費用 |
| Code Review（GitHub App，GA）| 🔥🔥🔥 | ⚡ 有條件推薦——10-16 轉 GA，官方同日補 6 頁文件；點數方案金額出自媒體，官方頁未載 |

> 完整功能熱度評分、**升上去會遇到什麼**與倒數中事件見 **[[feature-radar]]**
> 本輪有 7 條條目因近 4 週日報零提及而降一格熱度（v2.1.288、`claude plugin eval`、Auto 模式預設化、額度重置後自動續行、Opus 4.8、`/goal`、macOS Computer Use），降幅同步回對應 entities 頁。

---

## 社群情緒指標

- HN 討論熱度：🔥🔥🔥🔥 高（Linus Torvalds 用 Claude Code 寫 kernel、Scion 抄襲爭議、Q3 營收放緩）
- Reddit 情緒：😤 額度／成本焦慮持續，企業端開始自己裝月費上限；模型品質退化疑慮跨代際延燒
- 開發者工具活躍度：📈 升溫（本輪策展新增 22 筆、移出 5 筆，目錄 164 列；記憶類工具仍無第三方使用回報）
- 信任指標：↘ 走弱（桌面版漏洞雖已修但揭露前無官方公告、1M 靜默清除工具結果無解法、提示注入已產業級）
- 競爭壓力：🟡 中（GPT-6.1 Sol 與 Sonnet 5.5 同價、中國陣營「免費夠用」、開源旗艦權重釋出）
