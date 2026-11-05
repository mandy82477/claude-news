# 第 25 波逐字稿：topics/enterprise-tool-tracker（2026-11-04）

> 新字的單一來源是 `<scratchpad>/w25/design/newtext.py`（頁面）與 `rules_patch.py`（規則檔），本檔由 `make_draft.py` 從那兩檔產出；照搬行不列（見 proposal-map）。行號指改前原檔。改後全文在 `<scratchpad>/w25/design/out/wiki/topics/`。

## 一、進頁面

### A. 頁首（L26 H1、使命句新增、L31、L33、L36）

    # 大型企業 Claude 採用追蹤：誰在用、誰減用

    哪些具名企業與機構在自己內部用 Claude（含 Claude Code）、用多大、誰在減用或退出、為什麼——一家一列。帳單怎麼控在 [[topics/enterprise-cost-management]]，這則客戶進出對營收怎麼判在 [[topics/market-signals-customers]]。

    **最後更新：** 2026-11-04
    **蒐集邊界：** 僅涵蓋 Claude 相關報導所帶出的具名企業與機構，是已見報者的彙整，非市場全貌。只收 Claude 的買方——員工在用，或自家產品呼叫 Claude；替客戶導入、轉賣或認證 Claude 的通路夥伴（Partner Network、系統整合商）在 [[topics/anthropic-partnerships-compute]]。

    > **最新企業採用異動**（2026-11-03）
    > 高盛全面禁止行員使用 Claude Code 與 GitHub（僅標題，範圍與生效時間未見），與 08-20 香港被切斷是不同案例（[PYMNTS](〈歸因網址：source_attribution 2026-11-03 PYMNTS 那筆 item_url〉)）

### B. 摘要（L40、L42；L43–L82 砍）

第一段的家數由 `build.py` 從改後表的狀態欄數出，實跑結果：

    表上 48 家具名企業與機構：✅ 使用中 35、⚠️ 縮減或限縮 7（含 Replit 有爭議）、❌ 退出或被切斷 3、🔄 切換 1、❓ 未確認 2（2026-11-04 數表，一家一列）。見報的具名導入仍以新增為主；減用的理由集中在成本、自家有競品與資料外洩疑慮。

    **退出與減用理由分兩類：** 客戶自己選的是成本（Uber、Lindy、Microsoft）、安全或資料疑慮（Alibaba；Nvidia、Palantir、Booz Allen）、自家有競品（Meta、Microsoft，10-05 已查證），Goldman 11-02 禁令的理由未見報導；別人劃線的是出口管制（JPMorgan 香港，06-18，06-30 解除）、區域存取（Goldman、OKX 香港，08-20，Anthropic 區域存取政策，與出口管制無關，見 ⟨Q-03⟩）、Pentagon 黑名單，詳見 [[topics/anthropic-government-policy]]。

### C. 主表（L88、L90 圖例；改寫列與新列；表下一句）

    > 狀態＝這家現在對 Claude 的整體狀態：✅ 使用中 ／ ⚠️ 縮減中或限縮 ／ 🔄 切換中 ／ ❌ 已退出或被切斷（備註寫誰劃的線） ／ ❓ 未確認
    > 確認日期：最近一則報導的日期（括號內為首見日）；一家公司一列，同一家有新消息就更新同一列，依確認日期新者在上

改寫列（左欄＝原行；併入列見 map 第二節）：

- L94：`| Goldman Sachs | 頂尖 | Claude Code；Claude AI（香港） | ❌ | — | 11-02 報導全面禁止行員用 Claude Code 與 GitHub，範圍與生效時間未見；08-20 香港先被切斷，屬 Anthropic 區域存取政策（⟨Q-03⟩） | 2026-11-02 |`
- L98：`| Epic Games | 頂尖（遊戲引擎大廠，Unreal Engine 開發商） | Claude Code ＋ Codex | ✅ | 2026-10-12 | TweakTown（10-29）稱已用 Claude Code／Codex 改善除錯 Unreal Engine；10-12 官方釋出 skills 供外掛，527 星，細節見時序 | 2026-10-29（首見 2026-10-12） |`
- L99：`| Barclays | 頂尖（英國環球銀行） | Claude Code；Claude（營運） | ✅ | — | 官方 10-01：預期 2026 年底半數開發者用 Claude Code、2027 年擴及多數工程師（目標，非已達成）；郵件分流約 12 萬封／日、1.6 萬人用於知識檢索 | 2026-10-01 |`
- L100：`| JPMorgan Chase | 頂尖 | Claude Code（美國本部）；Claude API（香港分行） | ✅ | — | 美國本部 8 月約 8,000 人持授權，部分工程師每月 $2,000 上限；香港分行 06-18 因出口管制停用，06-30 管制解除後是否恢復未見 | 2026-09-17 |`
- L102：`| Rubrik（NYSE: RBRK） | 大型 | Claude Code；Claude Mythos 5 | ✅ | 2026-06-09 | 06-09 Agent Cloud for Claude Code、06-30 Claude Code 安全層、09-15 Code Guardian 用 Mythos 5 做程式碼紅隊測試 | 2026-10-09 |`
- L105：`| Shopify | 頂尖 | Claude Code | ❓ | — | 執行長 Tobi Lütke 揚言封殺；Anthropic 早已關閉相關功能請求；未見官方確認執行，暫標未確認（細節見時序） | 2026-08-26 |`
- L108：`| OKX | 大型（加密貨幣交易平台） | Claude AI | ❌ | — | 與高盛同批：香港被切斷 Claude AI 存取權限，屬 Anthropic 區域存取政策（⟨Q-03⟩），詳見 [[topics/anthropic-government-policy]] | 2026-08-20 |`
- L118：`| Microsoft | 頂尖 | Claude Code → GitHub Copilot；Claude（內部整體） | ⚠️ | 2026-06-21 | 06-21 起停用 Claude Code、改推 Copilot；10-05 內部 Claude 支出砍逾三分之一（已查證 2026-10-07），合約未取消 | 2026-10-05 |`
- L121：`| 加州州政府 | 政府（州級） | Claude API | ✅ | 2026-06-29 | 州長 Newsom 與 Anthropic 正式簽署協議，Claude 進入加州州政府應用；迄今最明確的美國地方政府採用案例 | 2026-06-29 |`
- L140：`| Amazon | 頂尖 | Claude Code ＋ OpenAI Codex | ✅ | 2026-05-05 | 雙軌並行，不押注單一供應商 | 2026-05-05 |`
- L142：`| Uber | 頂尖 | Claude Code ＋ Cursor | ⚠️ | 2026-05-01 | 4 個月燒完全年 AI 預算，CTO 承認成本失控，隨後設用量上限；COO 5/27 確認帶來 25% 生產力提升 | 2026-06-02 |`
- L147：`| UiPath | 大型 | Claude Code ＋ OpenAI Codex | ✅ | 2026-05-12 | RPA 平台雙工具整合，同時部署 | 2026-05-12 |`

新列（ledger (8)）：

- `| Palantir | 大型 | Claude | ⚠️ | — | 09-14 報導因資料外洩疑慮限縮內部使用，要求不可撤銷的零資料保留保證才上架；11-01 CTO 稱不後悔合作 | 2026-11-01 |`
- `| Charles Schwab | 頂尖（美國券商） | Claude for Financial Advisors | ✅ | 2026-09-14 | 把 Claude 接進給獨立投資顧問（RIA）的平台；10-24 追加 20 席採購下限，見 [[entities/pricing]] | 2026-10-24 |`
- `| Novo Nordisk | 頂尖（丹麥藥廠） | Claude | ✅ | — | 用 Claude 加速藥物研發與醫學研究，合約範疇與費用未見（Reuters 等 4 家） | 2026-09-16 |`
- `| Nvidia | 頂尖 | Claude | ⚠️ | — | 09-14 The Information（經多家轉述）：因資料外洩疑慮限於較不敏感任務、內部改用自家 Nemotron；官方未回應個案 | 2026-09-14 |`
- `| Booz Allen | 大型 | Claude | ⚠️ | — | 同批報導：禁止員工以其商用模型處理專有資安工作；官方未回應個案 | 2026-09-14 |`
- `| Orion | 大型（RIA 財富管理平台） | Claude for Financial Advisors | ✅ | 2026-09-14 | 與 Schwab 同日宣布把 Claude 接進 RIA 平台，費率未見 | 2026-09-14 |`

表下：

    Microsoft、Amazon、Google 同時是 Anthropic 的出資者與雲端通路；表上只寫它們的員工用不用，投資與通路見 [[topics/anthropic-partnerships-compute#跟三大雲各是什麼關係]]。

### D. L179 標題

    **已查證的三件事**（⟨Q-nn⟩ 是本頁的查證編號，表與摘要引用處都指這裡）

### E. 選型影響（L215 → 七條）

    - **退出不等於 Claude 不好用**：減用有數字的 Meta、Microsoft 都自己賣編碼工具（Muse Code、GitHub Copilot），而 Google（09-15）開放全體工程師使用、Amazon（05-05 起）雙軌並行；「自研夠強所以退」目前沒有證據。
    - **讀數字先問主詞與基期**：10-05 Meta 的數字是 Claude Code 使用人數、Microsoft 的是全部 Claude 花費，拆法見 [[#2026-10-05]]。
    - **大公司多半不押單一供應商**：表上明寫並用他家的有 Amazon、UiPath、Epic Games（＋Codex）與 Uber（＋Cursor），Notion 則在自家產品同時接 Claude 與 Cursor；其餘只寫用了 Claude，有沒有並用目前沒有證據。
    - **員工的 Claude 用量會被設上限**：Accenture 報銷每月 $29（是否限 Claude Code 未見）、JPMorgan 部分工程師 Claude Code 每月 $2,000、Uber 燒完全年預算後設上限；API 自建應用的控管案例本頁沒有，機制見 [[topics/enterprise-cost-management]]。
    - **資料保留是限縮的具名理由**：09-14 The Information 稱 Nvidia、Palantir、Booz Allen 都因資料外洩疑慮限縮（官方未回應個案），Palantir 要求零資料保留；官方保留政策見 [[topics/ai-agent-safety-product-vulns]]。
    - **可用性可能不由你決定**：香港兩起切斷（06-18 出口管制、08-20 區域存取）與 Pentagon 黑名單都是別人劃的線；在這些地區或產業，先備好換得了供應商的工作流（推論，見 [[topics/anthropic-business-risks]]）。
    - **工具之間誰搶誰**：Codex、Copilot、Cursor 的企業攻勢本頁不另計數，見 [[topics/competitor-landscape]]（Microsoft 轉向見 [[topics/competitor-landscape#Microsoft／GitHub]]）。

### F. 時序行內小改（只縮短或等長；L286、L297 隨 08 月進 archive，閘外）

| 原行 | 舊 | 新 |
|---|---|---|
| 229 | `詳見上方使用現況表 Epic Games 列與細節` | `詳見上方使用現況表 Epic Games 列` |
| 245 | `已查證 2026-10-07，詳見上方使用現況細節（The Information）` | `已查證 2026-10-07（The Information）` |
| 269 | `詳見上方使用現況表新增列與細節` | `詳見上方使用現況表新增列` |
| 286 | `[❌ 新增退出，香港出口管制]` | `[❌ 新增退出，香港區域存取]` |
| 286 | `與 06-18 JPMorgan Chase 香港分行因出口管制退出屬同類案例` | `成因為 Anthropic 區域存取政策，與 06-18 JPMorgan Chase 香港分行的出口管制案不同源（2026-09-20 查證）` |
| 297 | `### 2026-08-14` | `#### 2026-08-14` |
| 324 | `（詳見 [[topics/anthropic-business]]）` | `（詳見 [[topics/anthropic-partnerships-compute]]）` |
| 327 | `成因已於下方 ⟨Q-03⟩ 查證` | `成因已於上方 ⟨Q-03⟩ 查證` |
| 95 | `細節見下方` | `細節見時序` |
| 106 | `（詳見下方細節）` | `（細節見時序）` |
| 111 | `（詳見下方細節）` | `（細節見時序）` |
| 117 | `細節見下方` | `細節見時序` |
| 335 | `富士通、Travelport+Cognizant、Nimble Gravity 三案新增採用（詳見上方使用現況表）` | `Travelport+Cognizant 新增採用（見上方表）；富士通、Nimble Gravity 屬通路夥伴` |

### G. 08 月總結（取代 L274–310；原文照搬進 archive `## 2026-08`，L173–177 細節依日期插在該日條目下）

    ### 2026-08（總結；原始條目已移出）

    - **Samsung 晶片設計（08-14～08-25）**：08-14 Digital Trends 首報（未確認）；08-15 TechSpot、Tech My Money 給出時程壓縮數字（兩說並陳），08-25 TechRadar 再確認，都指出仍會犯嚴重錯誤。
    - **Goldman Sachs、OKX 香港被切斷（08-20）**：成因為 Anthropic 區域存取政策，與 JPMorgan 香港的出口管制案不同源（⟨Q-03⟩）。
    - **Shopify（08-26）**：執行長揚言封殺 Claude Code，未見執行，維持 ❓。
    - **新增具名採用**：Syracuse University 擴大授權納入 Claude Code 與 Cowork（08-07）、Duke University pay-as-you-go 訂閱（08-18）、Payward 採用 Mythos 5（08-19）、ReliaQuest 深化整合（08-22）。
    - **跟進，非新事實**：ICON 臨床試驗合作二、三度報導（08-04、08-10）；Microsoft 內部備忘錄再傳不利消息（08-06，未改狀態）。
    - 原始條目見 [[topics/enterprise-tool-tracker-archive#2026-08]]

### H. 相關實體加兩行；archive H1 與最後更新

    - [[topics/anthropic-partnerships-compute]]
    - [[topics/market-signals-customers]]

    # 大型企業 Claude 採用追蹤 — 原始條目封存
    **最後更新：** 2026-11-04

## 二、進規則檔

### `commercial/pages.md`：`## topics/enterprise-tool-tracker` 節整段換（L7–26，sha256 `936139d1…` 鎖）

    ## topics/enterprise-tool-tracker

    **這頁答什麼：** 哪些具名企業與機構在自己內部用 Claude（含 Claude Code）、用多大、誰在減用或退出、為什麼。**只收 Claude 的買方**——員工在用，或自家產品呼叫 Claude。**不收**：替客戶導入、轉賣或認證 Claude 的通路夥伴（Partner Network、系統整合商）→ `topics/anthropic-partnerships-compute`；帳單怎麼控 → `topics/enterprise-cost-management`；客戶進出對營收怎麼判 → `topics/market-signals-customers`；Codex／Copilot／Cursor 誰搶誰 → `topics/competitor-landscape`。判不出時問：寫得出這家自己的人或自家產品怎麼用 Claude 嗎？寫不出 → 通路，不開列。

    **觸發條件（滿足其一即更新）：**
    - 具名企業或機構採用、擴大、縮減、限縮、停用 Claude（含 Claude Code），或被切斷存取
    - 含規模描述的匿名企業切換工具 → 只進 `## 時序`，不開列
    - 具名企業替員工的 Claude 用量設上限 → 本頁只改該列狀態與一句備註，上限怎麼設、缺什麼工具寫 `topics/enterprise-cost-management`

    **現況表（現名 `## 企業工具使用現況`；名冊，累積不封頂、不退場）：**
    `| 企業 | 規模 | AI 編碼工具 | 狀態 | 事件日期 | 備註 | 確認日期 |`——**表頭字串一字不改**：`scripts/build_web.py` 的 `parse_enterprise_tracker()` 以「企業」＋「AI 編碼工具」找這張表，改字網站企業矩陣會靜默變空（已登記 `.claude/review-registry.json` anchors）。
    - **一家公司一列**：同一家有新事件就覆寫該列，不開第二列；不同辦公室、產品線或時間點的事件寫進同一列備註（例：JPMorgan 美國本部與香港分行）。舊事件的細節只留在 `## 時序`。
    - **AI 編碼工具欄**：這家用的 Claude 產品；並用他家寫「＋X」，換掉寫「→ X」。
    - **狀態欄**＝這家**現在**對 Claude 的整體狀態，一列一個符號：✅ 使用中／⚠️ 縮減中或限縮（含設上限後減用、合作狀態有爭議）／🔄 切換中／❌ 已退出或被切斷（被 Anthropic 或管制切斷者，備註寫明誰劃的線）／❓ 未確認。部分單位退出、其餘仍用者標仍在用的狀態，退出寫備註。
    - **事件日期**：YYYY-MM-DD，不確定填 `—`。**確認日期**：最近一則報導的日期開頭，可括註首見日。
    - **排序**：確認日期新者在上；新增或覆寫一列時移到對應位置。
    - **備註 ≤120 字元**：只寫現況與最關鍵的一個數字；來源與細節進 `## 時序` 該日。
    - Microsoft、Amazon、Google 這類同時是出資者或雲端通路的公司，表上只寫員工用不用；投資與通路的家是 `topics/anthropic-partnerships-compute` 三大雲表，表下一句指路，不在列裡寫。

    **`## 摘要`（兩段，各 ≤3 句）：** 第一段一句結論＋按狀態欄數出的家數（新增列或任一列換狀態時同批重數；不另寫計數口徑）；第二段退出與減用理由的兩分法（客戶自己選的／別人劃的線），管制成因指 `topics/anthropic-government-policy`。**不列近期新增或退出清單**——那是表的副本。

    **`## 對 agent 開發者的選型影響`：** 一條一個判讀，每條要有本頁表列或鄰頁事實撐；撐不起的寫「目前沒有證據」，不補推測。有新證據推翻或補強某條時改寫該條。工具之間的採用家數不在本頁計，指 `topics/competitor-landscape`。

    **更新動作：**
    1. 現況表新增或覆寫該公司的列（一家一列），依確認日期移位
    2. 在 `## 時序` 該月 `### YYYY-MM` 下的 `#### YYYY-MM-DD` prepend 一則；同一事件的細節條列緊接在該則下面，不另開細節區
    3. 狀態或家數變了，同批改 `## 摘要`
    4. 更新「最後更新」；有新聞時同批更新「最後新聞更新」與頂部 callout

    **蒸餾與封存**照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」，archive 為 `topics/enterprise-tool-tracker-archive`，新時段開 `## YYYY-MM`。

    **不在此頁追蹤：** 個人開發者趨勢、成本機制細節（→ `topics/enterprise-cost-management`）、通路夥伴（→ `topics/anthropic-partnerships-compute`）、無具名也無規模描述的匿名案例。

### `commercial/pages.md` 第 0 條路由表：一列改、一列加

    | 戰略合作（雲端、SDK 生態、企業客戶）、收購、算力合約與資本支出、政府採購 | `topics/anthropic-partnerships-compute` |
→

    | 戰略合作（雲端、SDK 生態、通路夥伴）、收購、算力合約與資本支出、政府採購 | `topics/anthropic-partnerships-compute` |
    | 具名企業或機構自己用 Claude 的採用、減用、退出 | `topics/enterprise-tool-tracker`（不在合作頁另寫用量） |

### `commercial/daily.md` 負責頁面表兩格

    | `wiki/topics/enterprise-tool-tracker.md` | 具名企業採用 / 退出 AI 編碼工具；企業工具切換報導（含有規模描述的匿名企業）；企業 AI 工具預算或成本相關的具名案例 |
→

    | `wiki/topics/enterprise-tool-tracker.md` | 具名企業或機構自己用 Claude（含 Claude Code）的採用、擴大、減用、退出或被切斷；企業工具切換報導（含有規模描述的匿名企業，只進時序）；通路夥伴不收（→ partnerships-compute） |

partnerships-compute 那列處理條件尾段：

    …戰略合作、收購、算力合約與資本支出、政府採購、具名企業導入（採用率指數換值寫母頁 `## 現在的數字`） |
→

    …戰略合作、收購、算力合約與資本支出、政府採購、通路夥伴（採用率指數換值寫母頁 `## 現在的數字`；企業自己用 Claude 寫 enterprise-tool-tracker） |

### `.claude/review-registry.json` anchors 加一筆

    {"label": "企業採用主表表頭——scripts/build_web.py parse_enterprise_tracker() 以「企業」＋「AI 編碼工具」找表，改字網站企業矩陣靜默變空（第 25 波）", "pattern": "\\| 企業 \\| 規模 \\| AI 編碼工具 \\| 狀態 \\| 事件日期 \\| 備註 \\| 確認日期 \\|", "file": "wiki/topics/enterprise-tool-tracker.md"}
