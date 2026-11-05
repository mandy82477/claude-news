# 第 25 波設計提案：topics/enterprise-tool-tracker 改成一家一列的買方名冊，08 月蒸進 archive（2026-11-04）

> 上游：健檢卡 `enterprise-tool-tracker-2026-11-04.md`、冷讀者 `wave25-cold-reader-2026-11-04.md`、查證 `enterprise-tool-tracker-2026-11-04-verified.md`。十個裁決點照 ledger「2026-11-04｜第 25 波」條，不重開。
> 機械產物在 `<scratchpad>/w25/design/`（下稱 `D/`）：`newtext.py`（新字單一來源）、`build.py`（重排；斷言原檔 1–366 每行恰消費一次，開頭比對 commit `e90dace` 兩檔 blob 且工作樹乾淨）、`verify.py`（獨立核對：照搬逐字、懸置去 slug、archive 一字不刪、公司不憑空消失、⟨Q⟩ 成對）、`moves.py`（cell／reader 對照）、`rules_patch.py`（pages.md 本頁節 sha256 鎖）、`before.sh`、`gates.sh`、`rebuild_after.sh`（一鍵：build → verify → 建 `tmp_after` → 規則檔 → 全閘 → 再 verify → moves）、`make_map.py`、`make_draft.py`、`out/wiki/topics/`（兩頁改後全文）、`redtest.txt`。行號一律指原檔。

## 1. 推薦案（一個）

**使命句**（H1 下第一行，照裁決 1）：「哪些具名企業與機構在自己內部用 Claude（含 Claude Code）、用多大、誰在減用或退出、為什麼——一家一列。帳單怎麼控在 ECM，這則客戶進出對營收怎麼判在 market-signals-customers。」H1 改為「大型企業 Claude 採用追蹤：誰在用、誰減用」（archive H1 同步，N6）。

| 節（改後） | 行 | 內容 |
|---|---|---|
| H1＋使命句＋標頭＋callout | 14 | 蒐集邊界加一句範圍：只收買方，通路夥伴指 partnerships-compute（裁決 2 的「一句範圍說明與指路」）；callout 11-03 Goldman，75 字＋PYMNTS 歸因網址 |
| `## 摘要` | 8 | 兩段：結論＋數表家數；退出與減用理由兩分法 |
| `## 企業工具使用現況`（節名、表頭不動） | 59 | 圖例 3 行＋48 列＋表下一句三大雲指路 |
| 已查證的三件事 | 8 | 原懸置細節，⟨Q-01..03⟩ 原字，加圖例 |
| `## 對 agent 開發者的選型影響` | 12 | 七條判讀 |
| `## 時序` | 115 | 11、10、09 原文（細節條目插回同日）；08 總結 8 行；07、06、05、04 不動 |
| 相關、參考 | 18 | 加兩頁 |

主頁 366→**259 行**（正文 341→234），archive 151→194。原 366 行：留 212／進 archive 41／改 22／併入 9／砍 81／結構 1（`D/accounting.txt`，逐段見 map 第二節）。

**主表一家一列（裁決 3、冷讀者最想改 2），不改表頭：**
- 列鍵＝公司。同一家多列併成一列，舊事件細節回 `## 時序`。四種多列各有收法：同公司不同辦公室（JPMorgan 美國本部／香港）→ 一列，狀態取仍在用的 ✅，香港寫備註；同公司多條產品線（Rubrik 3 列）→ 工具欄並列、備註按日期一句；Claude 換成他家（Microsoft 3 列）→ 工具欄「Claude Code → GitHub Copilot；Claude（內部整體）」、狀態取整體的 ⚠️；雙軌並行（Amazon、UiPath、Uber）→ 工具欄「＋X」。
- 狀態欄改語意為「這家**現在**對 Claude 的整體狀態」，❌ 涵蓋被切斷並在備註寫誰劃的線（健檢卡 §7 第三條規則）。不加新符號：`build_web.py` STATUS_MAP 只認五個。
- 排序依確認日期新者在上（確認日期格開頭必為日期，可括註首見日）；Shopify 那格原填來源名，改 08-26。
- 副作用：網站矩陣的 Rubrik 同鍵覆蓋（`build_web.py` L476–483）因一家一列自然消失；矩陣 51×24／58 格 → 48×27／48 格。工具欄詞彙與稀疏表仍是裁決 10 的程式工作。

## 2. 砍、搬與補列（逐行在 map）

- **通路夥伴移出 8 家**（裁決 2）。判準一句（寫進 pages.md）：「寫得出這家自己的人或自家產品怎麼用 Claude 嗎？寫不出 → 通路，不開列。」移出：Cognizant、Globant、DataArt、Okta、DXC、Fujitsu、Nimble Gravity、KPMG。留下：TCS（5 萬員工部署，business-archive L512）、Accenture（員工 $29 上限）、Rubrik、JFrog、Atlassian 等把 Claude 做進自家產品者、Travelport（Cognizant 的客戶）。前 7 家在 partnerships-compute L207／L208 彙整句已有家，**本波 partnerships-compute 0 行變動**，所以沒有超限條目搬過去（cell 閘不受影響）。N1、N3。
- **摘要的兩串清單、L78、L80、L82 砍**（裁決 3）：每條都在表上有列；L80 與 ⟨Q-03⟩ 衝突；L82 的家是 06 總結。
- **細節區併進時序**（裁決 4）：L156–159（Replit）、L162–167（Meta／Microsoft 10-05）、L169–170（JPMorgan 09-17）原字插到同日條目下；L173–177（Shopify、ReliaQuest、Samsung，皆 08 月）隨 08 月時段進 archive；L155、L160、L161、L168、L171、L172 與同日時序條目＋表列重複，砍（L172 提到的 Millennium，家在 partnerships-compute L249）。時序三處「詳見上方…細節」半句同批刪（只縮短）。
- **工具競爭態勢＋採用企業清單砍**（裁決 5），指路句成選型影響第 7 條，錨點 `competitor-landscape#Microsoft／GitHub`（h3 實存）。**市場分層觀察砍**（N2）。
- **補列 6 家**（裁決 8）：Nvidia、Palantir、Booz Allen（09-14 限縮，⚠️；出處 product-vulns L380；三家的官方懸置標記住 customers L525，本頁不另開也不複製；Palantir 另引 partnerships-compute L298 的 11-01 CTO 表態）、Novo Nordisk（09-16，pc L165）、Charles Schwab、Orion（09-14，pc L167、L323）。10-02 人才計畫七家不入表（ledger 另依查證）。
- **依查證改的列**：Barclays 補「預期，非已達成」＋12 萬封／日、1.6 萬人（verified #1）；Microsoft 三列併一，「內部用不用」寫列、「投資／通路」寫表下一句指 `partnerships-compute#跟三大雲各是什麼關係`（verified #4）；OKX「成因未明」改區域存取政策；Cognizant 隨通路移出，本頁不再宣稱「官方公告」（N8）。
- **重數**：✅ 35／⚠️ 7／❌ 3（Goldman、OKX、Alibaba）／🔄 1（Lindy）／❓ 2，共 48；舊「6 家退出」中 Microsoft 改計 ⚠️、JPMorgan 計 ✅。家數由 `build.py` 數改後表填入摘要，不手打。

## 3. 選型影響七條的撐腳（裁決 6；reader-notes 10-07 三切角＋冷讀者 Q4）

| 條 | 撐腳 | 撐不起的部分照寫 |
|---|---|---|
| 退出≠不好用 | 表 Meta、Microsoft、Google、Amazon 列；competitor-landscape Meta／Microsoft 節 | 「自研夠強所以退」→ 目前沒有證據（reader-notes 10-07：模型線查無 Muse Code／MAI 編碼基準） |
| 主詞與基期 | 時序 10-05 第 7 條（原 L167 原字） | — |
| 不押單一供應商 | 表 Amazon、UiPath、Epic、Uber 的工具欄 | 其餘有無並用 → 目前沒有證據 |
| Claude Code 會被設上限 | 表 Accenture、JPMorgan、Uber 列 | API 自建應用的控管案例本頁沒有 → 指 ECM |
| 資料保留是具名理由 | 表 Nvidia、Palantir、Booz Allen 列；product-vulns L373–380 | — |
| 可用性不由你決定 | 摘要第二段、⟨Q-03⟩；business-risks「換得了供應商」 | 建議句標（推論） |
| 誰搶誰 | 指 competitor-landscape | 本頁不計數 |

## 4. 08 月蒸餾（裁決 7；page-lifecycle：11−8＝3，錨點 0，例外 2 不成立）

先修 L286（標籤「香港出口管制」→「香港區域存取」；「與 JPMorgan 屬同類案例」→「成因為 Anthropic 區域存取政策，與 JPMorgan 香港的出口管制案不同源（2026-09-20 查證）」）與 L297（`###`→`####`），再把 L275–310 原字＋L173–177 五條細節依日期插入，append 至 archive 新節 `## 2026-08`。主頁留 8 行總結，末行 `原始條目見 [[topics/enterprise-tool-tracker-archive#2026-08]]`（建置錨點驗過）。09-02 Samsung 四度確認屬 09 月，留。⟨Q-01..03⟩ 不搬：所指的表列都還在主頁。09 月 12 月到期。

## 5. 規則檔（逐字在 draft 第二節；臨時副本實套後 `check_rules.py` ✅）

- `commercial/pages.md` 本頁節整段換：這頁答什麼＋買方／通路判準＋四個「不收→去哪」；觸發條件改「採用、擴大、縮減、限縮、停用或被切斷」；**一家一列**、工具欄寫法、狀態語意、確認日期格式、排序、備註 ≤120、三大雲指路；摘要兩段與「不列近期清單」；選型影響「撐不起寫目前沒有證據」；時序細節緊接同日條目、不另開細節區；刪「更新工具競爭態勢採用數」；**表頭一字不改**並說明 `parse_enterprise_tracker()`。同檔第 0 條路由表：「企業客戶」改「通路夥伴」，加一列「具名企業自己用 Claude 的採用、減用、退出 → enterprise-tool-tracker」（健檢卡 §11 兩條規則重疊）。
- `commercial/daily.md` 負責頁面表：本頁那格與 partnerships-compute 那格各改一句，對齊上面的邊界。
- `.claude/review-registry.json` anchors 加主表表頭（`check_rules.py` L226–249 `check_anchors()` 看守；redtest 4：表頭改字 → check_rules 紅、矩陣 0 列）。
- 腳本、測試、`data/*baseline*.json`、`data/*-allow.json`：**0 改**。

## 6. handoff（主 session 先 `open --dry-run` 驗負責人）

| # | --from → --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 商業 → 投資分析 | topics/market-signals-customers | (a) L349「首次具名導入、每人 2,000」對齊本頁 10-07 查證「部分工程師、每月 $2,000」（JPMorgan 列）；(b) L50 把 Accenture 歸「具名縮減」，本頁 ✅（設上限不等於減用），Replit 本頁為「有爭議」；(c) L405 等節的採用數字只引用、狀態指 `[[topics/enterprise-tool-tracker#企業工具使用現況]]`，不重抄（裁決 9） |
| 2 | 商業 → 主編 | index | L138 鉤子去掉「AI 編碼工具」，改為「哪些大企業在用、減用或退出 Claude，一家一列」；頁名已改（N6） |

裁決 10 的程式工作（工具欄詞彙、稀疏矩陣）由主 session 另開建議任務，不在本波。

## 7. 閘（`D/tmp_before`＝HEAD 工作樹原樣；`D/tmp_after`＝套本案兩頁＋規則檔；`bash D/rebuild_after.sh <repo>` 一鍵重跑，輸出在 `D/gates_before`、`D/gates_after`）

| 閘 | 改前 | 改後（原樣） | 驗紅／看守 |
|---|---|---|---|
| `build.py` 防呆 | — | `ok {'main': 259, 'archive': 194}` | 對改後樹跑 → `AssertionError: … 自設計 commit e90dace 後被改過`（redtest 1） |
| `verify.py` | — | `照搬行逐字核對 155 行；懸置標記 0→0；表 59 列/50 家 → 48 列/家（通路移出 8）`、`結論：OK` | 刪 ⟨Q-02⟩ 定義 → `⟨Q⟩ 引用與定義不成對`、FAIL；刪 Apple 列 → FAIL（redtest 2、3） |
| `gen_wiki_frontmatter.py` | exit 0 | exit 0 | — |
| `check_hierarchy.py` | `✅ 通過（32 個母頁）` | `✅ 通過（32 個母頁）` | — |
| `check_pending_markers.py` | 220 筆（基線 212）✅ | 220 筆（基線 212）✅；本頁 0→0 | 不需 `--rebuild-count` |
| `check_wiki_freshness.py` | OK 143 頁 | OK 143 頁 | callout 宣稱 11-03，附當日歸因網址 |
| `check_rules.py` | ✅ | `✅ 全部確定性檢查通過`（規則檔已套） | 表頭改字 → 紅（redtest 4） |
| `check_cell_limits.py` | OK 無新增 | **OK 無新增**；本頁命中 9→2 全配回原基線、新寫 0、釋出 7 槽 | 插 259 字條列 → FAIL `新增的超限`（redtest 5） |
| `check_reader_language.py` | OK | **OK**（新寫 0） | 首版圖例「覆寫」命中 1 筆，已改字 |
| `build_web.py` | 斷鏈 23／錨點 WARN 0，exit 0 | 斷鏈 23／**錨點 WARN 0**，exit 0 | archive `## 2026-08` 改名 → 錨點 WARN 1、exit 1（redtest 6） |
| 企業矩陣 `parse_enterprise_tracker()` | 59 列／51 家／24 工具欄／58 格 | 48 列／48 家／27 工具欄／48 格 | 表頭改字 → 0 列（redtest 4） |
| `run_tests.py` | 1,334 案全過 | 1,334 案全過 | — |

cell、reader 兩閘都是 0 筆新增，本波不需要本機 `--rebuild`／`--allow-grow`。

## 8. 新裁決點（主 session 判）

- **N1** 通路判準落地後移出 8 家，不是健檢卡估的「約 11」：TCS（5 萬員工）、Rubrik、Travelport 寫得出自己怎麼用，留在表上。
- **N2** 市場分層觀察整節砍。ledger 沒有點名這一節；它是 05 月凍結的內容，L207–208 各家都在表上，L209 的家在 competitor-landscape L626，砍掉不會讓任何事實失去家。
- **N3** Nimble Gravity 移出後，只剩本頁 archive `#2026-05` 原始條目，partnerships-compute 的 05–06 彙整句沒列它。本波不補：補了要改長 L208，計數「21 筆」也要跟著改。交下次 ingest 判斷，或就不補。
- **N4** Schwab／Orion 照裁決 8 入表，判準算它們「自家平台呼叫 Claude」；market-signals 稱 Schwab「通路夥伴」，兩頁用詞不同，所以 handoff 1 不追這一點。
- **N5** 摘要家數照裁決 3 寫入、照查證重算，由 `build.py` 數表；以後換狀態時，條文要求同批重數。一家一列之後只數一欄，比舊的手算口徑穩，但仍沒有閘看守（推論）。
- **N6** H1 改名，archive 同步；index 鉤子走 handoff 2。
- **N7** 08 月的五條細節（Shopify、ReliaQuest、Samsung）跟著時段進 archive，不留主頁。cell 基線因此釋出 7 槽，本機下次 `--rebuild` 時自然收緊。
- **N8** Cognizant 的官方連結：business-archive L367 附了 `anthropic.com/news/cognizant-anthropic`，verified #5 說官方索引查無。本頁已不再宣稱，是否回頭修 archive 由主 session 一查定案。

## 9. 不選的方向

- 使命句收窄成 coding agent：ledger (1) 已否。
- 表加「買方／通路」欄或新狀態符號：表頭凍結，STATUS_MAP 只認五個。
- 細節壓進備註欄：≤120 字放不下，會新增 cell 命中。
- 在 partnerships-compute 替 8 家新寫一行：已有彙整句，再寫就是第二個家；L207／L208 本身是長段。
- 腳本從表算工具態勢：ledger (5) 不改腳本。
- 09 月一起蒸：11−9＝2，未到期。
- 重排 archive 既有分節順序（07、05、04、06）：不在裁決範圍，讀者也得不到東西。

**可行性前提**：同一個 commit 含兩頁、pages.md、daily.md、review-registry、ledger 定稿列、handoff 1–2 開帳；跑 `build.py`／`rules_patch.py` 時，兩頁仍須是 `e90dace` 版，pages.md 本頁節 sha 也不能變（否則先紅，續用設計者重跑，不准手改）。今天 11-04 的 ingest 若先動到本頁，第 0 步就會擋下。

## 10. 最不確定的一件事

買方與通路的界線：把 Claude 做進自家產品賣給客戶的公司（Rubrik、JFrog、Grasshopper、Schwab）照判準留表，但每日寫的人遇到「加入 Partner Network 並推出 Claude 整合產品」這種一則兩面的新聞，很可能兩頁各寫一次。條文給了判準句和路由列，有沒有守住要看一週回訪。
