# Claude / Anthropic 生態系概覽

**最後更新：** 2026-10-03
**更新頻率：** 🗓️ 週更（每週檢視一次；更新日期停留數天屬正常節奏）

---

## 當前局勢

**Claude Mods 出貨，官方明說外掛讀得到你的 API Key**：10-01 Claude Code v2.1.287 推出 Mods——外掛以 JS／TS 在 Claude Code 行程內執行，可改寫 prompt、tool call 與介面，官方追蹤 issue #91870 當日累積 233 則留言。官方文件（2026-10-04 查證）明載 mod 以你的權限執行、讀得到環境變數與設定檔裡的 API key、不受沙箱隔離——這是設計，不是漏洞。只裝可信來源，裝前先跑 `claude plugin validate`。詳見 [[entities/claude-mods]]。

**Claude Sonnet 5.5 接手 API 預設 Sonnet，Sonnet 5 轉 Legacy**：09-28 發布，Terminal-Bench 4.0 由 10.3% 跳到 70.6%，牌價維持 $2/$10；v2.1.284 起 Anthropic API 端的 Sonnet 系列預設改指它。同批官方模型總覽頁（2026-10-03 查證）把 **Sonnet 5 與 Opus 4.7 都列進 Legacy**，本庫兩頁狀態已同步更正。詳見 [[entities/sonnet-5-5]]、[[entities/sonnet-5]]、[[topics/model-comparison]]。

**美國 FTC 對 Anthropic、OpenAI 開啟產品風險調查**：09-30 至少五家媒體同日報導，具體調查範圍、法源與是否已發傳票均未見報導。目前是「觀察」級——調查剛開啟，還沒有傳票、執法行動或產品限制，**不改變你現在拿得到的 Claude**。這條線一進表就把「國會立法壓力」頂出八線名單。詳見 [[topics/anthropic-government-policy]]。

**IPO 招股書外流：近半營收來自 Amazon 與 Google，並首度書面警示 AI 存在性風險**：09-29／09-30 Reuters 獨家，是本庫首次看到 Anthropic 在正式文件裡寫下存在性風險。客戶集中度這個數字看的是**依賴度**——兩家同時是大客戶也是大股東與算力供應方。外流版屬機密草案階段、單一來源，不等於公開版 S-1。詳見 [[topics/anthropic-business]]、[[topics/market-lessons]]。

**晶片租賃融資一週內從 420 億長到 600 億美元**：10-01 Reuters 獨家稱 Broadcom 擬貸款 Anthropic 最高 420 億美元租賃晶片，10-02 多家媒體續報已啟動 600 億美元債務融資，條款未見報導。這是 AMD（07-22）、Nvidia-Lambda（09-02）之後第三輪循環融資疑慮，判讀見 [[topics/market-signals]]，事實見 [[topics/anthropic-business]]。

**1M context 長 session 會靜默清除工具結果，而且沒有已知的規避做法**：10-01 GitHub issue #42542 整理出三種獨立機制（microcompact、cached microcompact、session memory compact）都會在未通知使用者的情況下清掉工具結果。官方未回應、社群也還沒提出可靠解法——現階段能做的只有「別預設工具結果會留到 session 結束」，重要中間產物自己落地成檔案。這是「你看不出自己在不在 1M 上」控制權缺口的第五條。詳見 [[topics/long-context-1m]]。

**Claude for Government 全面開放美國聯邦機構，香港那端則再收緊**：10-02 官方宣布聯邦機構全面可用；同日 SCMP 報導 Anthropic 近期收緊 VPN 存取、部分香港用戶原可用的連線方式受影響且事前未獲通知（僅標題可用）。兩件事方向相反但同屬一條線：區域與客戶分層正在變細。詳見 [[topics/anthropic-government-policy]]「政府動作對你的產品做了什麼」。

**Anthropic 研究稱中國 GLM-5.3 網攻能力已逼近 Mythos Preview**：09-30 Frontier Red Team 研究指 GLM-5.3 在控制流劫持上達 4%、Mythos Preview 為 6%，跨越先前模型做不到的門檻——意思是高階網攻能力正在擴散到他家模型，不再是單一供應商的護欄問題。詳見 [[topics/ai-agent-safety]]、[[entities/mythos]]。

**AMD 以約 82 億美元收購 World Labs，Fei-Fei Li 出任首席科學家**：09-29 公布，是本季最大一筆 AI 人才與技術同時易手的案子。詳見 [[topics/ai-talent-flow]]、[[entities/fei-fei-li]]。

**企業具名採用再添一筆，而且首見量化目標**：10-01 Barclays 宣布擴大導入，Claude Code 目標 2026 年底涵蓋 50% 開發者——本庫記錄到的第一個帶時間表的採用目標，比單純的採用公告好驗證。判讀見 [[topics/market-signals]]，課程表見 [[topics/market-lessons]]。

**Yann LeCun 公開批評 Dario Amodei 看待 AI 風險的方式**：10-01 Fortune 報導，用語為「deluded」「crazy」且稱其不懂資安（僅標題可用）。詳見 [[entities/yann-lecun]]、[[entities/dario-amodei]]。

**本週站內新補的東西**：四個現行模型頁（[[entities/fable-5]]、[[entities/mythos]]、[[entities/opus-5-5]]、[[entities/sonnet-5-5]]）的「跟它怎麼說話」節**首次有了實際內容**——此前四頁都只寫著「官方指南尚無可讀內容」，本週已依官方 prompting 指南補齊「換代時哪幾句 prompt 要加、哪幾句要刪」。另有 36 筆原本標著「待查證」的條目完成查核（19 筆查到官方說法、11 筆確認官方未公開、6 筆依日報收斂），站內目前沒有逾期未查的懸置項目。

---

## 主要模型現況

| 模型 | 狀態 | 備注 |
|------|------|------|
| **Claude Fable 5.1** | 🟢 旗艦（2026-09-01 發布，取代 Fable 5）| 反萃取機制；快取讀取費率 0.025x（約省 75%）；官方 prompting 指南 2026-10-03 查證補進頁內 |
| **Claude Mythos 5.1** | 🟢 政策限定（2026-09-01 發布）| 僅限信任機構；Anthropic 研究稱中國 GLM-5.3 網攻能力已逼近 Mythos Preview |
| **Claude Opus 5.5** | 🟢 現行 Opus（2026-09-22 發布）| Claude Code v2.1.280 起為 `default`（Foundry 除外）；$4/$20；預設 effort 為 `medium`（Opus 5 為 `high`）|
| **Claude Sonnet 5.5** | 🟢 現行 Sonnet（2026-09-28 發布）| v2.1.284 起為 API 端預設 Sonnet；Terminal-Bench 4.0 由 10.3% → 70.6%；牌價維持 $2/$10 |
| Claude Opus 5 | ⚠️ Legacy（2026-09-22 起）| 仍可用，$5/$25；跨模型代際「重複修辭套路」問題持續（GitHub #77136）|
| Claude Sonnet 5 | ⚠️ Legacy（2026-10-03 官方總覽頁查證）| 仍可用，$2/$10；預設地位已由 Sonnet 5.5 接手 |
| Claude Opus 4.8 | ⚠️ Legacy | 仍是 Fable 5／5.1 **資安類**請求被護欄攔下時的接手模型（生物／化學／生命科學類改由 Opus 5 接手）|
| Claude Opus 4.7 | ⚠️ Legacy（2026-10-03 官方總覽頁查證）| 本輪由「已被取代」更正為 Legacy |
| Claude Sonnet 4.6 | ⚠️ Legacy | 仍可選用 |
| Claude Haiku 4.5 | ✅ Active | 低延遲／高頻批量任務的現行選項，退役不早於 2026-10-15；沒有獨立新聞可寫，不設專頁，規格與選型見 [[topics/model-comparison]] |

> 快速選型與情境推薦見 **[[topics/model-comparison]]**；跨家任務榜單見 **[[topics/model-task-leaderboard]]**
> 四個現行模型頁（Fable 5.1、Mythos 5.1、Opus 5.5、Sonnet 5.5）的「跟它怎麼說話」節已於 2026-10-03 從官方 prompting 指南補齊——**換代時哪幾句 prompt 要加、哪幾句要刪**看那一節。

---

## 進行中議題

### 🔴 高度關注

1. **[[topics/anthropic-government-policy]] — 八條線在動，FTC 新線剛開**
   - FTC 產品風險調查（09-30 開啟，觀察級）；五角大廈案 09-25 上訴法院推翻一審、維持認定；香港 VPN 存取 10-02 再收緊
2. **[[topics/ai-agent-safety]] — 攻擊面九條仍擋不住，提示注入已是產業級**
   - Auto 模式非安全邊界（官方立場）；Plugin4Shell 修補狀態媒體稱已修、官方未載；GLM-5.3 網攻能力擴散
3. **[[topics/anthropic-business]] — IPO 招股書外流，客戶集中度與存在性風險首度書面化**
   - 近半營收來自 Amazon／Google；Broadcom 晶片租賃融資 420 億 → 600 億美元
4. **[[topics/long-context-1m]] — 1M session 會靜默清除工具結果，無已知規避做法**
   - GitHub #42542（三種機制），官方未回應；控制權缺口第五條
5. **[[entities/claude-mods]] — Mods 出貨，外掛讀得到 API Key 且不受沙箱隔離**
   - 官方文件明載為設計能力；防範只能靠來源信任與裝前 `claude plugin validate`

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

## 近期重大事件（2026-09-26 至 2026-10-02）

| 日期 | 事件 | 影響 |
|------|------|------|
| 10-02 | Claude for Government 全面開放美國聯邦機構；Broadcom 晶片租賃融資擴大為 600 億美元債務融資；SCMP 稱香港 VPN 存取收緊 | 🏛️ 政策；💼 商業 |
| 10-01 | Claude Code v2.1.287 推出 Mods（官方明載外掛可讀 API Key）；Barclays 訂年底 50% 開發者目標；Broadcom 擬貸 420 億美元；1M context 靜默清除工具結果（#42542）| 🛠️ 功能；💼 商業 |
| 09-30 | 美國 FTC 對 Anthropic、OpenAI 開啟產品風險調查（5+ 媒體同日）；Anthropic 研究稱 GLM-5.3 網攻能力逼近 Mythos Preview；Claude Code v2.1.285 發布 | 🏛️ 政策；🛠️ 功能 |
| 09-29 | IPO 招股書外流：近半營收來自 Amazon／Google、首度書面警示 AI 存在性風險（Reuters 獨家）；AMD 以約 82 億美元收購 World Labs | 💼 商業 |
| 09-28 | **Claude Sonnet 5.5 發布並取代 Sonnet 5 成為 API 預設 Sonnet**（Terminal-Bench 4.0 10.3% → 70.6%，牌價不變）| 🤖 模型 |
| 09-26 | Claude 發現類 CRISPR 酶成果遭質疑可能借用他人研究；Fable 5／5.1 護欄接手模型分兩路經官方查證（資安 → Opus 4.8，生物化學 → Opus 5）| ⚖️ 爭議；🤖 模型 |

> 完整事件時序見各 topics 頁面「時序」區塊；[[log]] 含每日更新完整紀錄。

---

## 社群工具生態

社群工具目錄（[[topics/community-tech-tools]]）本輪（2026-10-03 整理，news 窗口 09-26～10-02）**新增 31 筆**、**移出 13 筆**（10 筆原標「有條件推薦」但逾 120 天、近 8 週無人再提；3 筆原標「觀望」但逾 30 天、近 4 週無人再提），目錄現為 123 列；「我卡在這裡」決策表 9 列首選**全數不變**。

- 🔥🔥🔥🔥 **跨 Session 記憶層／知識庫（趨勢九）** — 本輪再添 agent-memory／deja-vu／hippo-memory 三個獨立實作，但**皆無第三方使用回報**
- 🔥🔥🔥🔥 **規格驅動開發（趨勢七）** — 已站穩成形
- 🔥🔥🔥 **大型 codebase 並行規模化** — 見 [[topics/community-large-codebase-workflow]]
- 🔥🔥🔥 **額度／成本焦慮** — 本輪新增 Usage Updates（時間軸，**不是告警工具**）；要額度預警仍是 Claude-Code-Usage-Monitor

社群做法概覽（[[topics/community-tech-patterns]]）由 21 類收為 **20 類**——「Agent 版本控制」逾 60 天沒有新證據，已移到表下；討論盤點（[[topics/community-tech-discussions]]）現在還在吵的有 8 場，熱門討論表已到 50 列上限，本輪換掉其中最舊的 8 列。

> 功能熱度評分與試用推薦見 **[[feature-radar]]**；社群趨勢週更見 **[[topics/community-pattern-trends]]**

---

## 商業動態

- **基建與融資**：Broadcom 晶片租賃融資 420 億 → 600 億美元（10-01／10-02，條款未見報導）；此前 Akamai 7 年 116 億美元、Nscale 450 億美元／460MW、Lambda 350 億美元。循環融資疑慮已是第三輪
- **IPO**：招股書外流顯示近半營收來自 Amazon 與 Google，並首度書面警示 AI 存在性風險（Reuters 獨家，機密草案階段、單一來源，不等於公開版 S-1）
- **採用**：Barclays 擴大導入並首見量化目標（Claude Code 2026 年底涵蓋 50% 開發者）；Claude for Government 全面開放美國聯邦機構
- **安全治理支出**：Anthropic 與 Accenture 合計承諾五年至少 10 億美元於內嵌評估能力建設，Anthropic 直接資助 Accenture 的工作，非排他（官方公告 2026-10-03 查證）
- **政策**：FTC 產品風險調查開啟（觀察級，尚未見傳票或產品限制）
- **法律**：Sony Music／Warner（Warner Chappell）音樂著作權訴訟、UTRF 專利訴訟均進行中
- **人才**：AMD 以約 82 億美元收購 World Labs，Fei-Fei Li 出任 AMD 首席科學家

---

## 功能試用推薦（快速查閱）

| 功能 | 熱度 | 推薦 |
|------|------|------|
| Claude Sonnet 5.5（API 預設 Sonnet）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——牌價不變、Terminal-Bench 大幅躍升；effort 級距已重新校準，**換過來要重跑一次 sweep** |
| Claude Code 讀取 AGENTS.md（v2.1.277）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——無 CLAUDE.md 時原生改讀，回應 #6235 |
| Claude Mods（v2.1.287）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——**mod 讀得到你的 API Key、不受沙箱隔離**（官方明載）；只裝可信來源，裝前 `claude plugin validate` |
| Auto mode 免計費 server-side classifier（v2.1.278）| 🔥🔥🔥🔥 | ✅ 強烈推薦——API／Enterprise／閘道器用戶不再被收分類器費用 |
| Claude Opus 5.5（現行 Opus）| 🔥🔥🔥🔥 | ⚡ 有條件推薦——$4/$20；預設 effort 從 `high` 降為 `medium`，沿用 Opus 5 的設定會換到更長的回合 |
| Claude Fable 5.1（旗艦）| 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦——長時 agentic 工作流首選；`low` effort 下搜尋觸發會變少 |

> 完整功能熱度評分、**升上去會遇到什麼**與倒數中事件見 **[[feature-radar]]**

---

## 社群情緒指標

- HN 討論熱度：🔥🔥🔥🔥 高（Mods 外掛權限、Opus 5.5 降智觀感、IPO 招股書外流）
- Reddit 情緒：😤 額度／成本焦慮持續；模型品質退化疑慮跨代際延燒
- 開發者工具活躍度：📈 升溫（本輪策展新增 31 筆，記憶類工具一次三個，但皆無第三方使用回報）
- 信任指標：↘ 走弱（Mods 外掛權限面大且無沙箱、1M 靜默清除工具結果無解法、提示注入已產業級）
- 競爭壓力：🟡 中（Meta 三層訂閱、中國陣營「免費夠用」、開源旗艦權重釋出）
