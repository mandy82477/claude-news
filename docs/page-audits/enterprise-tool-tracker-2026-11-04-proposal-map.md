# 第 25 波去向表：topics/enterprise-tool-tracker（2026-11-04）

> 行號指改前原檔（commit `e90dace`，366 行）。第二節由 `<scratchpad>/w25/design/make_map.py` 從 `accounting.txt` 產出：`build.py` 斷言 1–366 每行恰消費一次，`verify.py` 對「M／A」照搬行逐字核對（155 行）。去向代號：**M**＝留主頁（原字）、**A**＝進 archive `## 2026-08`（原字）、**M（改）／A（改）**＝行內小改後留／搬（逐字在 draft F 節）、**改**＝新字取代、**併入**＝併進同公司的一列、**砍**＝刪（理由寫在格內）。

## 一、逐節去向

| 原節（行） | 行數 | 去向 | 備註 |
|---|---|---|---|
| frontmatter（1–25） | 25 | 留 | `gen_wiki_frontmatter.py` 重寫 |
| H1＋標頭（26–33） | 8 | 留；H1、最後更新、蒐集邊界改；H1 下加使命句 | 蒐集邊界欄有 review-registry 錨點，`**蒐集邊界：**` 字樣保留 |
| callout（35–36） | 2 | 留；L36 改成 75 字＋PYMNTS 歸因網址 | 網址＝`source_attribution.jsonl` 2026-11-03 本頁那筆 |
| 摘要 L40、L42 | 2 | 改 | 家數由 `build.py` 數表 |
| 摘要 L44 | 1 | 砍 | 併入 H1 下使命句 |
| 近期新增 L46–65、近期退出 L67–76 | 31 | **砍**（裁決 3） | 每條都在表上有列；L59 Samsung「跨 2」已與表「跨 3」漂 |
| 計數口徑 L78 | 1 | 砍 | 一家一列後計數＝數狀態欄；條文進 pages.md「摘要」段 |
| L80、L82 | 2 | 砍（裁決 3） | L80 與 ⟨Q-03⟩ 衝突；L82 的 06 淨變化家在 06 總結（原 L322–331） |
| 現況表（86–152） | 67 | 留；**一家一列**（59 列／50 家→48 列）；原字 30 列、改寫 12 列（7 列是併後的新列）、併入 9 列、移出 8 列、新增 6 列，依確認日期重排 | 表頭 L92 一字不改；逐列見第三節 |
| 使用現況細節（154–177） | 24 | **併進時序**（裁決 4） | 12 條照搬到同日條目下；5 條（08 月）隨時段進 archive；6 條與時序或表重複者砍；標題砍 |
| 懸置細節（179–183） | 5 | 留；L179 標題改「已查證的三件事」＋⟨Q-nn⟩ 圖例 | 冷讀者外洩 #8 |
| 工具競爭態勢＋採用企業清單（187–201） | 18 | **砍**（裁決 5） | 指路句進選型影響第 7 條；計數漂移證據見健檢卡 §0-4 |
| 市場分層觀察（205–209） | 8 | **砍**（N2） | L207–208 各家都在表上；L209 BI 05-23 的家在 competitor-landscape L626 |
| 選型影響（213–215） | 3 | 留；L215 一段 → 七條（裁決 6） | 每條撐腳見 proposal §3 |
| 時序 11、10、09（219–273） | 55 | 留；L229、L245、L269 刪掉指向已不存在的「細節」的半句 | 細節條目插在 L232、L245、L253 之後 |
| 時序 08（274–310） | 37 | **蒸**（裁決 7）：主頁 8 行總結；原文進 archive `## 2026-08` | 先改 L286（出口管制→區域存取、不同源）、L297（h3→h4） |
| 時序 07、06、05、04（312–347） | 36 | 留；L324 指路改 partnerships-compute、L327「下方」→「上方」 | — |
| 相關實體、參考來源（351–366） | 16 | 留；相關實體加 partnerships-compute、market-signals-customers | — |
| archive（151 行） | — | H1、最後更新改；末尾 append `## 2026-08`（43 行） | 原 151 行一字不刪（`verify.py` 第 3 項） |

改後主頁 259 行（正文 234），archive 194 行。原 366 行去向：M 212（含 M 改 5）／A 41（含 A 改 2）／改 22／併入 9／砍 81／結構 1。

## 二、逐段去向（`make_map.py` 產出）

| 原行 | 行數 | 去向 | 開頭 |
|---|---|---|---|
| 1–25 | 25 | M | page: "topics/enterprise-tool-trac |
| 26 | 1 | 改：H1 | # 大型企業 AI 編碼工具使用追蹤 |
| 27–30 | 4 | M | **狀態：** ongoing |
| 31 | 1 | 改：最後更新 | **最後更新：** 2026-11-03 |
| 32 | 1 | M | **最後新聞更新：** 2026-11-03 |
| 33 | 1 | 改：蒐集邊界加範圍句 | **蒐集邊界：** 僅涵蓋 Claude 相關報導所帶出的企業案例。 |
| 34–35 | 2 | M | > **最新企業採用異動**（2026-11-03） |
| 36 | 1 | 改：callout ≤120＋歸因網址 | > PYMNTS 報導高盛全面禁止行員使用 Claude Code  |
| 37–39 | 3 | M | ## 摘要 |
| 40 | 1 | 改：摘要第一段（結論＋數表家數） | **目前追蹤 51 家具名企業/機構，多數使用中（✅）、6 家退出/ |
| 41 | 1 | M |  |
| 42 | 1 | 改：退出理由兩分法（補 Nvidia 等、Goldman 禁令） | **退出理由分兩類：** 客戶自己選的是成本、安全疑慮、自家有競品（ |
| 43–45 | 3 | 砍：結構（空行）／L44 併入使命句 | 追蹤各大型企業目前正在使用的 AI 編碼工具，以及工具選擇的變化軌跡 |
| 46–66 | 21 | 砍：近期新增清單＝表的第二份副本（裁決 3） | **近期新增／擴大採用：** |
| 67–77 | 11 | 砍：近期退出清單＝表的第二份副本（裁決 3） | **近期退出／縮減：** |
| 78–79 | 2 | 砍：計數口徑（一家一列後不需要；條文進 pages.md） | **計數口徑：** 摘要按企業計，JPMorgan Chase 美國 |
| 80–81 | 2 | 砍：與 ⟨Q-03⟩ 衝突（裁決 3） | 出口管制 + 成本壓力雙重因素持續影響頂尖企業工具選擇。 |
| 82 | 1 | 砍：06 淨變化快照，家在 06 總結 L322–331（裁決 3） | **2026-06 淨變化回顧（歷史快照，非最新月份；最新異動見頂部 |
| 83–87 | 5 | M | ## 企業工具使用現況 |
| 88 | 1 | 改：狀態語意 | > 狀態說明：✅ 使用中 ／ ⚠️ 縮減中 ／ 🔄 切換中 ／ ❌  |
| 89 | 1 | M | > 事件日期：狀態實際生效的時間點（❌ 為退出日、🔄 為切換日、✅  |
| 90 | 1 | 改：確認日期＋一家一列 | > 確認日期：媒體報導或消息來源的日期 |
| 91–93 | 3 | M | ／ 企業 ／ 規模 ／ AI 編碼工具 ／ 狀態 ／ 事件日期 ／  |
| 94 | 1 | 改：一家一列新列 | ／ Goldman Sachs ／ 頂尖 ／ Claude Code |
| 95–97 | 3 | M | ／ Replit ／ 大型（AI 編碼/應用開發平台） ／ Clau |
| 98 | 1 | 改：一家一列新列 | ／ Epic Games ／ 頂尖（遊戲引擎大廠，Unreal En |
| 99 | 1 | 改：一家一列新列 | ／ Barclays ／ 頂尖（英國環球銀行） ／ Claude C |
| 100 | 1 | 改：一家一列新列 | ／ JPMorgan Chase（美國本部） ／ 頂尖 ／ Clau |
| 101 | 1 | M | ／ Google ／ 頂尖 ／ Claude（不限版本，媒體未指明是 |
| 102 | 1 | 改：一家一列新列 | ／ Rubrik（NYSE: RBRK） ／ 大型 ／ Claude |
| 103–104 | 2 | M | ／ T. Rowe Price ／ 大型（全球資產管理公司） ／ C |
| 105 | 1 | 改：一家一列新列 | ／ Shopify ／ 頂尖 ／ Claude Code ／ ❓ ／ |
| 106 | 1 | M | ／ ReliaQuest ／ 大型（資安廠商） ／ Claude A |
| 107 | 1 | 併入：P94 新列 | ／ Goldman Sachs ／ 頂尖 ／ Claude AI ／ |
| 108 | 1 | 改：一家一列新列 | ／ OKX ／ 大型（加密貨幣交易平台） ／ Claude AI ／ |
| 109–113 | 5 | M | ／ Payward（Kraken 母公司） ／ 大型（全球加密貨幣交 |
| 114 | 1 | 砍：通路夥伴，Cognizant → pc L207 07 月彙整；原始條目 business-archive L336、L367（附 anthropic.com/news/cognizant-anthropic） | ／ Cognizant ／ 頂尖 ／ Claude API ／ ✅  |
| 115–117 | 3 | M | ／ Grasshopper Bank ／ 中型（銀行，聚焦金融科技產 |
| 118 | 1 | 改：一家一列新列 | ／ Microsoft ／ 頂尖 ／ Claude（泛指內部整體使用 |
| 119–120 | 2 | M | ／ Alibaba ／ 頂尖 ／ Claude Code → Qod |
| 121 | 1 | 改：一家一列新列 | ／ 加州州政府 ／ 政府（州級） ／ Claude API ／ ✅  |
| 122 | 1 | 砍：通路夥伴，Globant → pc L208 05～06 月彙整；business-archive L473 | ／ Globant（NYSE: GLOB） ／ 頂尖 ／ Claud |
| 123 | 1 | 砍：通路夥伴，DataArt → pc L208；business-archive L381 | ／ DataArt ／ 大型 ／ Claude API ／ ✅ ／  |
| 124 | 1 | 砍：通路夥伴，Okta → pc L208；business-archive L471 | ／ Okta ／ 大型 ／ Claude API ／ ✅ ／ 202 |
| 125 | 1 | 併入：P102 新列 | ／ Rubrik（NYSE: RBRK） ／ 大型 ／ Claude |
| 126–129 | 4 | M | ／ Notion ／ 大型 ／ Claude Agents + Cu |
| 130 | 1 | 併入：P100 新列 | ／ JPMorgan Chase ／ 頂尖 ／ Claude API |
| 131 | 1 | 砍：通路夥伴，DXC → pc L208；pc L476 | ／ DXC Technology ／ 頂尖 ／ Claude API |
| 132–133 | 2 | M | ／ TCS（Tata Consultancy Services） ／ |
| 134 | 1 | 併入：P102 新列 | ／ Rubrik（NYSE: RBRK） ／ 大型 ／ Claude |
| 135–137 | 3 | M | ／ AppFolio ／ 大型 ／ Claude API ／ ✅ ／ |
| 138 | 1 | 併入：P118 新列 | ／ Microsoft ／ 頂尖 ／ Claude Code ／ ❌ |
| 139 | 1 | 併入：P118 新列 | ／ Microsoft ／ 頂尖 ／ GitHub Copilot  |
| 140 | 1 | 改：一家一列新列 | ／ Amazon ／ 頂尖 ／ Claude Code ／ ✅ ／  |
| 141 | 1 | 併入：P140 新列 | ／ Amazon ／ 頂尖 ／ OpenAI Codex ／ ✅ ／ |
| 142 | 1 | 改：一家一列新列 | ／ Uber ／ 頂尖 ／ Claude Code ／ ⚠️ ／ 2 |
| 143 | 1 | 併入：P142 新列 | ／ Uber ／ 頂尖 ／ Cursor ／ ⚠️ ／ 2026-0 |
| 144 | 1 | 砍：通路夥伴，Fujitsu → pc L208（富士通） | ／ Fujitsu ／ 頂尖 ／ Claude API ／ ✅ ／  |
| 145 | 1 | M | ／ Travelport ／ 大型 ／ Claude API ／ ✅ |
| 146 | 1 | 砍：通路夥伴，Nimble Gravity → 本頁 archive #2026-05 原始條目；pc 不補（N3） | ／ Nimble Gravity ／ 中型 ／ Claude API |
| 147 | 1 | 改：一家一列新列 | ／ UiPath ／ 大型 ／ Claude Code ／ ✅ ／  |
| 148 | 1 | 併入：P147 新列 | ／ UiPath ／ 大型 ／ OpenAI Codex ／ ✅ ／ |
| 149 | 1 | M | ／ Apple ／ 頂尖 ／ Claude API ／ ✅ ／ —  |
| 150 | 1 | 砍：通路夥伴，KPMG → pc L208 | ／ KPMG ／ 大型 ／ Claude API ／ ✅ ／ 202 |
| 151–153 | 3 | M | ／ iCapital ／ 大型 ／ Claude API ／ ✅ ／ |
| 154 | 1 | 砍：結構（細節區標題，細節併進時序，裁決 4） | **使用現況細節** |
| 155 | 1 | 砍：重複 L229（Epic 10-29） | - **Epic Games 使用面跟進（10-29，TweakTo |
| 156–159 | 4 | M（搬到時序 P232 之後） | - **Replit 執行長說法（10-16）**：Amjad Ma |
| 160 | 1 | 砍：重複 L233＋表 Accenture 列 | - **Accenture 支出上限（10-16，3 家媒體）**： |
| 161 | 1 | 砍：重複 L236＋表參議院列 | - **美國參議院（10-15）**：Bloomberg Gover |
| 162–167 | 6 | M（搬到時序 P245 之後） | - **Meta 使用量（10-05，已查證 2026-10-07） |
| 168 | 1 | 砍：重複 L248＋表 Barclays 列 | - **Barclays（10-01）**：官方宣布擴大合作導入 C |
| 169–170 | 2 | M（搬到時序 P253 之後） | - **JPMorgan Chase 美國本部（09-17，已查證  |
| 171 | 1 | 砍：重複 L263＋表 T. Rowe Price 列 | - **T. Rowe Price（09-10）**：PR News |
| 172 | 1 | 砍：重複 L269＋表 PicPay 列（Millennium 的家在 pc L249） | - **PicPay（09-04）**：PYMNTS.com 報導巴 |
| 173–174 | 2 | A（搬到 archive，P277 之後） | - **Shopify（08-26）**：analyticsindi |
| 175–176 | 2 | A（搬到 archive，P283 之後） | - **ReliaQuest（08-22）**：TipRanks 報 |
| 177 | 1 | A（搬到 archive，P295 之後） | - **Samsung（08-15，首見 08-14）**：跨 3  |
| 178 | 1 | M |  |
| 179 | 1 | 改：懸置細節標題→已查證＋圖例 | **懸置細節** |
| 180–186 | 7 | M | - ⟨Q-03⟩ 已查證（2026-09-20，對照 [[topic |
| 187–204 | 18 | 砍：工具競爭態勢＋採用企業清單（手算計數漂移，裁決 5；指路句進選型影響） | ## 工具競爭態勢（企業視角） |
| 205–212 | 8 | 砍：市場分層觀察（05 月凍結；BI 05-23 的家在 competitor-landscape L626，N2） | ## 市場分層觀察 |
| 213–214 | 2 | M | ## 對 agent 開發者的選型影響 |
| 215 | 1 | 改：一段話→七條，每條有列或鄰頁撐（裁決 6） | Claude Code 是工程師日常編碼工具（CLI），成本隨使用量 |
| 216–228 | 13 | M | ## 時序 |
| 229 | 1 | M（改） | - **[既有企業，使用面跟進] TweakTown：Epic Ga |
| 230–244 | 15 | M | #### 2026-10-16 |
| 245 | 1 | M（改） | - **[⚠️ 縮減中，狀態更新] The Information： |
| 246–268 | 23 | M | #### 2026-10-01 |
| 269 | 1 | M（改） | - **[新增具名企業，✅ 使用中] PYMNTS.com：巴西金融 |
| 270–273 | 4 | M | #### 2026-09-02 |
| 274 | 1 | 結構：### 2026-08 → archive ## 2026-08 | ### 2026-08 |
| 275–285 | 11 | A | #### 2026-08-26 |
| 286 | 1 | A（改） | - **[❌ 新增退出，香港出口管制] Goldman Sachs、 |
| 287–296 | 10 | A | #### 2026-08-19 |
| 297 | 1 | A（改） | ### 2026-08-14 |
| 298–310 | 13 | A | - **[❓ 未確認，新增追蹤] Digital Trends：三星 |
| 311–323 | 13 | M | ### 2026-07（總結；原始條目已移出） |
| 324 | 1 | M（改） | - **Partner Network 密集擴張（06-09～06- |
| 325–326 | 2 | M | - **產品/平台整合案例**：Atlassian Claude A |
| 327 | 1 | M（改） | - **JPMorgan Chase 香港出口管制退出（06-18～ |
| 328–366 | 39 | M | - **Lindy 100% 切換至 DeepSeek（06-29） |

## 三、主表一家一列：逐列帳

- **併入 9 列**：Goldman L107→L94；JPMorgan 香港 L130→L100（備註寫香港分行與「06-30 管制解除後是否恢復未見」）；Rubrik L125、L134→L102（三條產品線寫進一格，確認日 10-09）；Microsoft L138（❌ Claude Code）、L139（✅ Copilot）→L118（⚠️，工具欄「Claude Code → GitHub Copilot；Claude（內部整體）」）；Amazon L141→L140、Uber L143→L142、UiPath L148→L147（工具欄寫「＋X」）。
- **改寫但不併 5 列**：L98 Epic（確認日改 10-29，括號首見 10-12，排序才對）；L99 Barclays（verified #1：「預期，非已達成」＋12 萬封／日、1.6 萬人）；L105 Shopify（確認日期格原填來源名，改 08-26；健檢卡 §3 格式漂移）；L108 OKX（「成因未明」與 ⟨Q-03⟩ 衝突，改「Anthropic 區域存取政策」）；L121 加州（刪指向拆頁前舊家 anthropic-business 的括號）。
- **移出 8 列（通路夥伴，裁決 2；判準見 proposal §2）**：Cognizant L114、Globant L122、DataArt L123、Okta L124、DXC L131、Fujitsu L144、Nimble Gravity L146、KPMG L150。前 7 家的家已在 partnerships-compute L207／L208 彙整句與 business-archive 原始條目，本波**不改 partnerships-compute 任何一行**；Nimble Gravity 見 N3。
- **新增 6 列（裁決 8）**：Nvidia、Palantir、Booz Allen（09-14；出處 ai-agent-safety-product-vulns L380、market-signals-customers L525–529；Palantir 另引 partnerships-compute L298 11-01）、Novo Nordisk（09-16；partnerships-compute L165）、Charles Schwab、Orion（09-14；partnerships-compute L167、L323）。三家限縮的官方懸置標記住 customers L525（複 11-30），本頁不另開標記、不複製。
- **原字留 30 列**；狀態語意改後重數：✅ 35／⚠️ 7（Meta、Microsoft、Uber、Nvidia、Palantir、Booz Allen、Replit 有爭議）／❌ 3（Goldman、OKX、Alibaba）／🔄 1（Lindy）／❓ 2（參議院、Shopify）。舊摘要「6 家退出」裡的 Microsoft 改計 ⚠️（合約未取消、仍是投資人與通路），JPMorgan 計 ✅（香港寫備註）。
- 網站矩陣（`parse_enterprise_tracker()` 實跑）：改前 59 列／51 家（Rubrik 3 列同鍵、06-09 蓋 06-30）×24 工具欄、58 格；改後 48 列／48 家 ×27 工具欄、48 格，同鍵覆蓋消失。工具欄寫法詞彙與稀疏表仍屬程式工作（裁決 10）。

## 四、cell 與 reader 兩閘搬家清單（`moves.py`，改前 `tmp_before`＝HEAD 工作樹）

| 類別 | 筆數 | 明細 |
|---|---|---|
| 改後命中、配回原基線（同錨點、長度不超） | 2 | L111（新行號）⟨Q-01⟩ 已查證 288≤288；L192 Wccftech 四度確認 214≤214 |
| 配不回（本波新寫或改長） | **0** | — |
| 原基線槽位釋出（隨 08 月進 archive 或砍掉） | 7 | PicPay（09-04）244（砍，重複）；Samsung（08-15）583、TechSpot 301、Shopify 240、ICON Vanguard 233、Microsoft 備忘錄 335、Duke 201（進 archive，閘外） |
| reader 閘 | 改前 0／改後 0 | 首版圖例「覆寫」一詞曾命中 1 筆，已改「更新同一列」 |

本波**不需要** `--rebuild`／`--allow-grow`；釋出的 7 槽留待本機任一次 `--rebuild` 自然收緊（只移除，不需 `--allow-grow`）。partnerships-compute 0 行變動，其 31 筆基線不受影響。
