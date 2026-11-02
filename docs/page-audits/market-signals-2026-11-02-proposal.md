> **2026-11-02 註：** 本檔是第一輪提案；評審 🔴1–3 的修正（`check_wiki_freshness.py` 那段 diff 不套、腳本 5 支；歸因只補 Citywire 1 筆、其餘 3 筆網址不在子頁不補）以 `market-signals-2026-11-02-review.md` 與 commit `7ec4d2b` 為準，文中相反的句子作廢。

# 第 22 波設計提案：topics/market-signals 拆成母頁＋四子頁（2026-11-02）

> 上游：健檢卡 `market-signals-2026-11-02.md`、冷讀者 `wave22-cold-reader-2026-11-02.md`、查證 `market-signals-2026-11-02-verified.md`；切法與七點照 ledger「2026-11-02｜第 22 波」條，不重開。
> 機械產物在 `<scratchpad>/w22/design/`（下稱 `D/`）：`newtext.py`（頁面新字的單一來源）、`split.py`（切頁；斷言 1–1,699 每行恰消費一次，開頭比對 commit `7dbc92e` 的頁面 blob，被每日 ingest 改過就先紅）、`verify.py`（獨立逐字核對＋懸置去 slug 比對）、`moves.py`（cell／reader 兩閘子樹命中改前改後對照）、`rules_patch.py`（規則檔逐字，臨時副本實套）、`scripts.diff`、`gates.sh`、`make_map.py`、`make_draft.py`、`out/wiki/topics/`（五頁改後全文，已過 gen）。行號一律指原檔。

## 1. 推薦案（一個）

88 則判讀連同各自的結算列與里程碑，照線別原文搬進四子頁，一則三件同頁。母頁留摘要、買得到的標的、子頁路由與四頁合計的命中率，記號說明只住母頁。網站的 💰 條目改讀整個子樹。

| 頁 | 使命一句 | 節清單 | 正文行 |
|---|---|---|---|
| 母 `topics/market-signals` | Anthropic 的消息放進市場框架怎麼讀：它動到哪個數字、碰到哪個你買得到的標的、兩週後對不對——判讀依四條子線往下鑽。 | 使命／標頭／免責／callout／摘要（＋「現在」段）／買得到的標的／**近期判讀**（子頁路由表、三段記號說明、h4 指路殼、`### 未歸類`）／**回顧結算**（說明、合計表、股價半邊說明）／相關實體 | **116** |
| A `-ipo`「IPO 與財務揭露這則怎麼判」 | IPO 走到哪一格、外流與 S-1 的數字該打幾折、評等消息怎麼讀——這類消息放進市場框架怎麼判。 | 標頭（上層）／免責／callout／**現在怎麼判**／近期判讀 25 則／回顧結算 25 列／追蹤中的里程碑 23 筆（19 標記）／相關 | **494** |
| B `-legal`「官司、監管與政府這則怎麼判」 | 官司、機關調查與政府採購的消息，會不會寫進 S-1 的風險因素、動到哪個數字。 | 同上：24 則／26 列＋10-03 細節兩條／25 筆（21 標記） | **483** |
| C1 `-compute`「算力與融資這則怎麼判」 | 誰在借錢給 Anthropic 買算力、條件多貴，這則消息動到的是成本還是只有傳聞。 | 同上：14 則／14 列＋細節一條／13 筆（12 標記） | **304** |
| C2 `-customers`「定價、通路與客戶這則怎麼判」 | 價格怎麼改、客戶誰進誰出、對手怎麼比價，這則消息往毛利與成長率哪邊推。 | 同上：25 則／25 列＋細節兩條／24 筆（17 標記） | **513** |

- 正文 1,673 行拆成 116／494／483／304／513（`check_page_thickness.body_lines`，臨時副本過 gen 後量），五頁都在 150–600 之間，母頁遠低於 300。
- slug 用 `market-signals-` 前綴、標題用「這則怎麼判」問句，和 business 規劃的 `anthropic-partnerships-compute`、financials、business-risks 不撞。
- **子頁三題**照健檢卡 §3。B、C1 第 3 題原本偏弱，本案替它們補兩個入口：母頁路由表一列一子頁，標的表「本頁判讀」欄的日期可以對到子頁。
- **新寫結論層只有兩處，都由主編每週寫**：子頁 `## 現在怎麼判`（≤4 條，數字都取自該頁既有判讀與結算列，`stats.py` 重算過），以及母頁合計表（✅13／❌1／～36／—14／⏳26，與健檢卡同數）。冷讀者 Q3「準不準」以前得自己數 90 列，現在母頁一張表就答得了。
- **一事一家**：一眼、結算、里程碑三套記號的說明只住母頁 `## 近期判讀`，子頁 `現在怎麼判` 末條指回去。L1502 跨三群，住母頁。免責是規則要求的常駐 callout，五頁各一份。
- **💰 條目**：`build_web.market_signal_pages()` 從標頭「上層」欄現算子樹，不寫死清單，取日期最新的一則並帶出所在頁。網站點擊直接進子頁（`app.js`）。

## 2. 照查證改的句子（逐字在 draft F 節）

807 億判讀 L406 補「約 724 億為非現金公允價值變動、營業損失約 6.9 億」，與里程碑 L1569 口徑一致。GSA 這則 L181 標題改「（媒體稱 OneGov）」；L185 寫明官方 10-27 發布並附原文連結，註明「OneGov」是媒體用語；里程碑 L1529 同改。判讀日 10-28 不動，因為它是判讀日，結算列與標記都綁這天。Public Benefit Fund 的 L447 標題、L451、L458–459 一課的概念與機制、里程碑 L1547 都改成「撥入全資子實體」；「下次怎麼認」照引媒體字眼，不改，教材頁抄的就是這行。里程碑 L1680 改成「當時公開版 S-1 尚未遞交」；L1681 改寫為「已過時：10-26 已提交，10 月上市的預期落空，股數、價格區間、掛牌日仍未公布」並縮排。標的表 L76 空行砍掉。摘要 L50 改成「公開版已於 10-26 提交」，母頁另插「現在」段，A 頁 `現在怎麼判` 的第一句就是「S-1 已公開、未生效、價格與日期未定」。S-1 的數字一律標「多家引 S-1」，不寫成官方一手（查證三句之 3）。

## 3. 錨點入邊逐筆去向（`grep -rn "market-signals#" wiki/`，log 除外：3 檔 4 筆）

| 入邊 | 現指 | 拆後 | 誰改 |
|---|---|---|---|
| yann-lecun L49 | `#💰 Reuters 獨家…存在性風險（2026-09-29）` | 母頁同名 **h4 殼**接住，指向 A；`MARKET_SIGNAL_RE` 只認 `###`，殼不會被當成判讀（新測試 `test_h4_shell_is_not_a_signal`） | handoff 2，落地後刪殼 |
| market-lessons L75 | `#近期判讀` | 母頁同名節仍在，現在是路由表 | handoff 4 改指子頁 |
| market-lessons L127 | `#近期判讀`、`#回顧結算` | 母頁兩節都在，後者是合計表 | handoff 4 |
| 頁級：anthropic-ipo L40、L44、L210 → A；tom-brown L41 → C1；mustafa-suleyman L53、business L711 → C2；其餘 7 筆指母頁不動 | — | 母頁路由一跳可達 | handoff 2、3 |

本頁出邊：`anthropic-business#IPO 走到哪一格` 7 筆搬進 A；`#哪個合作會改到你用的 Claude` 2 筆搬進 **C2**（健檢卡 §7 寫本頁，第 23 波回掃時要改看 C2）。臨時副本 build：錨點 WARN 0→0。

## 4. 懸置與保命

- 新語法 69 筆 → A 19／B 21／C1 12／C2 17／母 0，`verify.py` 去 slug 比對 (標記日, 探針) 多重集相等。每筆標記日都對得上同頁某則判讀或結算列的判讀日，算是歸群抽驗，0 筆對不上。驗紅：刪 A 一條標記＋一列結算 → 兩行缺＋標記少 1，exit 1。
- 計數閘：212（基線 212）不低於，綠；但 69 筆換了 slug、「尚未入基線」。實作後跑 `check_pending_markers.py --rebuild-count --reason "第 22 波 market-signals 拆頁：69 筆換 slug"`。`--rebuild-count` 不在 `guard_roles.py` L57 的 `BASELINE_FLAGS`，雲端可跑。
- `scan_pending_verifications.compute_marker_id`（L208）含頁 slug，69 筆的命中次數從零起算。這是換 slug 必然的結果，不另處理。
- 14 筆「已查證」結案殘留照裁決 (6) 不清，隨群下沉（A 3、B 4、C2 7：L1596、1679、1680／L1648、1672、1676、1677／L1582、1586、1589、1599、1617、1623、1654）。

## 5. 規則檔與腳本（逐字在 draft「進規則檔」「進腳本」；臨時副本實套後 `check_rules.py` ✅）

- `market/pages.md`：整節改寫，加路由表（照線歸頁、新線照題材、判不出的進母頁 `### 未歸類`）和結論表歸屬（加母頁路由表〔記者每日〕、合計表、子頁「現在怎麼判」〔主編每週〕）。回顧結算與里程碑改成「同一子頁」，20 列門檻改為各頁分算。
- `market/daily.md`：L7 負責頁面改成母頁＋四子頁；L54 消費端寫 `market_signal_pages()`；L83 寫入對象改成該子頁；L90 第 2 步 a–f（子頁三件、母頁標的表、callout、路由列；母頁「最後新聞更新」只在當天覆寫標的表時才動，歸因多報一筆母頁）；L107 回報欄。L42 頻率**不改**（裁決 (1)，交 handoff 1）。
- `market/weekly.md`：L20 讀四子頁；L21 看同一子頁的里程碑；L28 第 6 步加「覆寫母頁合計表與各子頁現在怎麼判」；L45 20 列門檻改各頁分算。`sweeps.md` 5h L221 同步。
- `agents/wiki-reporter-market.md` L3、L9、L25、L29、L30；`page-lifecycle.md` L52 例外清單加「`topics/market-signals` 的 `## 買得到的標的`」（裁決 (5)）；`commercial/daily.md` L25 改成「五頁不歸你，命中直接派投資分析」；`review-registry.json` L1401 同步對加第三個 pattern `market_signal_pages`；`Design Diagram.md` L181 一行。
- 腳本（最小 diff，見 `D/scripts.diff`）：
  - `build_web.py` L885–897：新增 `market_signal_pages()`，`parse_market_signal()` 改收清單並帶出 `page`；L1833 呼叫端同步改。
  - `pending_markers.py` L511 `PAGE_TO_REPORTER` 加五頁 → `wiki-reporter-market`。
  - `scan_pending_verifications.py` L75 `REPORTER_LABEL` 加 `"wiki-reporter-market": "投資分析"`：缺這筆時 L351 的分組輸出會整組漏印。
  - `pending_handoffs.py` L53 `OWNER_OVERRIDES` 加四子頁（裁決 (7)）。
  - `check_wiki_freshness.py` L78 說明文字。
  - `app.js` L327 點擊改用 `d.marketSignal.page`；L959 加四子頁短標籤。`index.html` 的 `?v=` 由 build_web L2129 重蓋。
- 測試：
  - `test_market_signals.py`：既有案例改成帶 `page`；新增跨頁取最新、h4 殼不算判讀、子樹由上層欄找到、子樹最新＝解析結果、五頁免責都在第一個 callout、`TestOwnership` 兩案。
  - `test_reader_tags.py` L71：EXCLUDED 加四子頁。
  - **驗紅**：新測試檔放進「頁已拆、腳本未改」的副本跑，14 案中 13 紅（3 ERROR＋10 FAIL，`D/redtest.txt`）。

## 6. handoff（主 session 先 `pending_handoffs.py open --dry-run`）

| # | --from → --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 主編 → 投資分析 | topics/market-signals（子樹） | **六類判準回頭檢查**（使用者批准）：W41–W44 每週 12／13／9／16 則，daily.md L42 預期 3–5 則，逐則看是否都過「新資訊」門檻與六類；只查不改規則。另附兩件：S-1 公開後六類第 1、2 類是否改以「S-1 修正版／首份季報」為準（查證 #7）；硬度值漂移 L287「官方一手＋官方文件」（A）、L538「具名表態但有爭議」（C2）不在五值內 |
| 2 | 主編 → 人物 | entities/yann-lecun、tom-brown、mustafa-suleyman | L49 錨點改指 `[[topics/market-signals-ipo#💰 Reuters 獨家：Anthropic IPO 招股書外流，首度書面警示 AI 存在性風險（2026-09-29）]]`（落地後母頁刪殼）；tom-brown L41 → `topics/market-signals-compute`；suleyman L53 → `topics/market-signals-customers` |
| 3 | 主編 → 商業 | topics/anthropic-ipo、anthropic-business | anthropic-ipo L40、L44、L210 的「市場判讀」→ `topics/market-signals-ipo`；business L711 → `-customers`；母頁標的表下 L81「細節（Microsoft 列）」是事實，家該在 business／enterprise-tool-tracker（健檢卡 §6）；Nscale「1,030 億」與「第一筆 450 億」的口徑（冷讀者 Q3） |
| 4 | 主編 → 主編 | topics/market-lessons、index | L75、L127 改指四子頁（消息線表一線一列各指其子頁；`#回顧結算` 可留母頁合計表）；L77 IPO 線「18 則 · 10-21」本週 5h 更新為 21 則 · 10-31；index L138 鉤子補「判讀分四條子線」（子頁投影 gen 已產生） |

## 7. 閘（臨時副本 `D/tmp_before`＝HEAD、`D/tmp_after`＝套本案；`gates.sh` 一鍵重跑，輸出在 `D/gates_*`）

| 閘 | 改前 | 改後（最後一行原樣） | 驗紅／看守 |
|---|---|---|---|
| `split.py` 防呆 | — | `ok {…}` | 頁面與 `7dbc92e` blob 不同 → `AssertionError: market-signals.md 自設計 commit 7dbc92e 後被改過` |
| `verify.py` | — | `結論：OK`（照搬 1,084 行；69→69） | 見 §4 |
| `gen_wiki_frontmatter.py` | exit 0 | exit 0；index L138 投影出四子頁，子頁 `page_role: "child"` | — |
| `check_hierarchy.py` | `✅ 通過（31 個母頁）` | `狀態：✅ 通過（32 個母頁）` | 母頁 callout 改 10-29 → `❌ hub 落後：topics/market-signals callout 日期 2026-10-29 < 子樹最新新聞 2026-10-31`（L138） |
| `check_pending_markers.py` | ✅ | `狀態：✅ 懸置標記語法檢查通過`（212／基線 212，69 筆待入基線） | §4 |
| `check_wiki_freshness.py` | OK 134 頁 | `OK: wiki 新鮮度檢查通過（138 頁；…）`——**含 N2 補登**；不補登則 `[無從對照] topics/market-signals-customers` 紅 1 | `ancestor_att` L201：A／B／C1 callout 的歸因網址撐住 |
| `check_reader_language.py` | FAIL 2（第 21 波搬家，待本機） | FAIL 2（同兩筆）；**本波 0** | `moves.py`：子樹改前 0／改後 0 |
| `check_cell_limits.py` | FAIL 107（同上） | FAIL 107（同上）；**本波 0** | `moves.py` 驗紅：子頁塞一條 230 字條列 → `新 … list_item 230`，exit 1 |
| `check_rules.py` | ✅ | `狀態：✅ 全部確定性檢查通過`（規則檔已套） | registry 第三個 pattern |
| `build_web.py` | 斷鏈 23／錨點 0，exit 0 | `wikilink 健檢合計：斷鏈 WARN 23／錨點 WARN 0`，exit 0；子樹解析 → 10-31 A 那則、`page: market-signals-ipo` | 只讀母頁時 → `None`（舊行為會讓 💰 消失） |
| 改過的測試 | — | 4 檔 46 案 OK | 驗紅 13 案（§5） |
| `run_tests.py` | 1 FAIL＋2 閘紅（全是第 21 波）、1,329 案 | 同樣 1 FAIL＋2 閘紅、1,334 案 | 本波沒新增任何紅 |

## 8. 新裁決點（主 session 判）

- **N1** L1543 砍：它和 L1567–1568 同一事實（10-26 提交、ANT、晚三天），沒有標記。裁決 (6) 把它當續行看，實際不是。備案：原樣留在 A。
- **N2** `data/source_attribution.jsonl` 補登 4 筆 10-29（Citywire、The New Stack、BigGo、Bloomberg），`page=topics/market-signals`。這 4 筆是記者當天漏報，逐字在 `D/attribution_1029.jsonl`，網址取自 `news/2026-10-29.md`。不補的話 C2 只能宣稱 10-28，等於說謊；或者 freshness 紅。
- **N3** 本波改到 `scripts/`、`src/`、`web_reader/assets/`，而 `run_tests` 已經因第 21 波的 109 筆搬家而紅。兩條路：等使用者本機做完 `claude-code-2026-11-01-baseline-moves.md` 兩件事、測試轉綠再 commit；或者沿用第 21 波例外，紅只能是那 109 筆，`moves.py` 證明本波貢獻 0。
- **N4** 主編 5h 多兩件每週工作：母頁合計表、四子頁「現在怎麼判」。不做的話 Q3 回到「自己數 90 列」。
- **N5** 💰 條目帶出 `page`，網站點擊直達子頁。這超出裁決 (4)「讀子樹」的字面，但不帶的話點進去是母頁，要再找一跳。

## 9. 不選的方向

- 結算與里程碑留母頁：母頁約 400 行（裁決 (3)）。
- 結算改住 market-lessons：記者得每天寫他唯讀的頁（裁決 (3)）。
- 母頁留最新一則副本：一事兩家（裁決 (4)）。
- yann-lecun 錨點不設殼、接受 WARN +1：違反「錨點 WARN 不增」閘。
- 子頁 slug 用題材名詞（`-financials`、`-risks`）：會和 business 規劃的子頁撞名。
- 記號說明複製到四子頁：同一段字四個家。
- `build_web` 寫死四子頁清單：日後增減子頁漏改，💰 條目會靜默消失。
- 子頁「現在怎麼判」交記者每日寫：每天一則就重寫結論，會變成 callout 的副本。

**可行性前提**：同一個 commit 包含 wiki 五頁、規則檔 9 份（market 三份、角色檔、page-lifecycle、sweeps、commercial/daily、registry、Design Diagram）、腳本 6 支＋測試 2 支、N2 補登、`--rebuild-count`、handoff 1–4 開帳、`wiki/log.md` Query 條目，在 `market-signals.md` 仍是 `7dbc92e` 版時跑 `split.py`，否則它先紅；run_tests 依 N3。

## 10. 最不確定的一件事

成長速度。C2 正文 513 行、A 494 行，以 10 月每月約 50 則（約 750 行）攤到四頁來算，C2 與 A 大約 11 月中下旬就會再過 600。第一個能明顯瘦身的時點是 12-01，那天起 09 月時段滿 3 個月可蒸（A 9 則、B 13、C1 3、C2 8）。中間這段 `check_page_thickness` 有 60 天寬限，不會紅。但如果 handoff 1 回報六類判準確實鬆了，真正的解法是收緊產量，不是再拆一次。
