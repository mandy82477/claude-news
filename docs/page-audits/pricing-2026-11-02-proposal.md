# 第 24 波設計提案：entities/pricing 拆成母頁＋兩新子頁，計費切割死案歸檔（2026-11-02）

> 上游：健檢卡 `pricing-2026-11-02.md`、冷讀者 `wave24-cold-reader-2026-11-02.md`、查證 `pricing-2026-11-02-verified.md`；切法與八點照 ledger「2026-11-02｜第 24 波」條，不重開。
> 機械產物在 `<scratchpad>/w24/design/`（下稱 `D/`）：`newtext.py`（新字單一來源）、`split.py`（切頁；斷言 pricing 1–969 每行恰消費一次，開頭比對 commit `933a34d` 兩檔 blob 且工作樹乾淨）、`verify.py`（獨立逐字＋懸置去 slug 比對；第一參數＝改前副本）、`moves.py`（cell／reader 子樹命中對照）、`rules_patch.py`（規則檔＋1 個測試；pages.md 整節以 sha256 鎖）、`before.sh`、`rebuild_after.sh`（`set -u -o pipefail`；第二參數＝改前副本；內含 rules_patch、gates、build_web、改後 verify、moves）、`gates.sh`、`make_map.py`、`make_draft.py`、`out/wiki/entities/`（四頁改後全文）、`redtest.txt`。改前副本 `<scratchpad>/w24/pristine`＝`git archive 933a34d wiki scripts data`。行號一律指原檔。

## 1. 推薦案（一個）

照裁決甲案：母頁留「我現在怎麼被計費」全部現況層＋三路分流＋子頁路由；事故表、事故流、配額、灰色 → `pricing-incidents`；定價與促銷、成本 → `pricing-history`（自帶三個月結論段）；計費切割 102 行死案歸檔；事故×06、配額×06 蒸進 archive。

| 頁 | 使命一句 | 節清單 | 全行／正文 |
|---|---|---|---|
| 母 `entities/pricing`「Anthropic 訂閱方案與計費政策」 | Claude 現在怎麼收你的錢，以及最近哪幾件事改變了這個答案——帳單出錯在 incidents、價格沿革在 history，各往下鑽。 | 使命／標頭／callout／現況（兩段）／**往下鑽**（路由表 2 列）／我的方案（表整表重判＋方案細節）／一小時／模型 API 定價（+Haiku 5.5）／還沒確定（+表下懸置）／當前生效的計費規則／通路與乘數（含帳務坑、可用性）／**事故現在還在發生嗎**（三路分流＋`###` 指路殼）／省錢一句／相關／參考 | 322／**294** |
| 新 `entities/pricing-incidents`「Anthropic 計費事故：誤扣、額度異常與帳號停用」 | 帳單出錯、額度掉得快、付了錢卻用不了——官方認了沒、現在還在不在，以及你能先做什麼；現在怎麼計費在母頁，逐條 issue 的留言數在 known-issues。 | 還在發生的事故（表 8 列＋表下「沒進上表」一行＋互動數指路＋懸置細節＋已結案三件）／事故與爭議、配額與速率（共 38 則＋06、05、04 總結）／灰色市場／相關 | 323／**296** |
| 新 `entities/pricing-history`「Anthropic 計費沿革：價格、方案與促銷怎麼變過來」 | Claude 的價格、方案與促銷是什麼時候、怎麼變的，以及最近三個月哪幾件改到你的帳單——現在生效的規則與牌價在母頁。 | **最近三個月變了什麼**（11 行＋傳聞一行）／定價與促銷（41 則）／成本案例與優化／相關 | 321／**293** |
| archive `entities/pricing-archive` | — | 原 04／05／06＋06-30、06-24 兩條＋新節 `## 計費切割風波` | 116→230 |

- 正文以 `check_page_thickness.body_lines` 在 `D/tmp_after`（過 gen）量；三頁都在 150–600，母頁 < 300。原 969 行去向：母 297／incidents 253／history 249／archive 109／砍 45／結構 16（`accounting.txt`）。母頁 294 貼線：`%%` 拆頁評估寫下下一刀＝API 塊（一小時、API 定價、通路與乘數連續三節），逾 300 時整塊切出。
- **三路分流只做路由**：計費事故 → incidents 表；token 變多 → `code-quality-decline#三種解釋，目前各自站在哪`；自己的設定 → `community-cost#用量去向歸因`。不抄三解表、不抄互動數（known-issues 一句指過去）。節名 `## 事故現在還在發生嗎` 不變，known-issues L49 錨點照接。
- **方案表整表重判**（verified #1–3）：六欄骨架不動，月度 API credits 放進原本全是「—」的「可領優惠」欄（Pro 寫「無」）；表頭一句寫明「不付 Claude Code 與 Claude apps 的超量」。Ultra 的旗艦 50% 規則官方未重述，格內標「推論」（verified 未涵蓋）。
- **事故表**（裁決 4）：8 列照新條文實跑（排序表見 draft B 節）。條文跑出來的兩個新結果：infostealer 抽乾額度（官方 08-30 通知、已退款＝官方已承認）進第一層；#38335（09-16）排第 9，落到表下可見一行（N1）。表格只寫 issue 號，互動數移除（H-645373 第 2 項）。
- **一事一家**：方案細節砍 4 條與生效規則重複者（L79–80＝L200、L83＝L214、L85＝L215）、L84（archive 06-26 已更正）；還沒確定表移出 3 列已查證＋1 列過期，事實各有家（N3）。L80 的「免費試用不算」資格細節隨之消失——促銷 08-02 已關窗，判為可失。

## 2. 蒸餾與歸檔範圍（page-lifecycle L84：11−6＝5；每頁 2 段，拆後各自起算）

- **事故×06**（L535–539，06-24 ⏸）、**配額×06**（L840–843，06-30）：錨點 0、非唯一出處、無 🌊 → archive `## 2026-06` 依日期插入；incidents 原位各留一行總結（末句 `原始條目見 [[entities/pricing-archive#2026-06]]`）。incidents 用滿 2 段；history 的 06 早已是總結（L785），本波 0 段。07、08 留下次 `/wiki-lint`（裁決 5）。
- **計費切割風波**（L847–948）：死案歸檔不佔額度（page-lifecycle L25）。archive 新節 `## 計費切割風波` ＋一行導語，L849 凍結 `%%` 砍；頁內兩處引號指路（L57、L531）改寫或刪（L531 只刪括號，不讓超限條目變長）。
- 懸置 4→4：L602 回母頁還沒確定表下（slug 不變，裁決 6，複查日表與標記統一 11-10）；L335、L438、L447 隨頁去 incidents（換 slug 3 筆，`--rebuild-count`）。全站 212→212。

## 3. 錨點入邊逐筆去向（`grep -rnoE "entities/pricing#"`，log、docs 除外）

| 入邊 | 現指 | 拆後 | 誰改 |
|---|---|---|---|
| partnerships-compute L79／104／115（3）、L115、L117；model-comparison L70；business-risks L138、L293；ECM L112 | 通路、乘數、API 定價、我的方案、可用性、方案細節、還沒確定 | 母頁保留節名 | 不動 |
| known-issues L49 | `#事故現在還在發生嗎` | 母頁保留節名（分流） | 不動 |
| 頁內 L77 | `#方案可用性與帳務摩擦` | 母頁內 | 不動 |
| 頁內 L286 | `#事故與爭議（…）` | `pricing-incidents#事故與爭議（…）` | 本波 |
| **daily/2026-10-24 L56**（健檢卡漏列） | `#事故與爭議（…）` | 母頁 `###` 永久指路殼接住（日報不可改） | N2 |
| daily/ 其餘 6 筆 | 模型 API 定價×3、還沒確定、方案細節、事故現在還在發生嗎 | 母頁保留 | 不動 |

不設殼時臨時副本 build `錨點 WARN 0→1`、exit 1（redtest 6）。

## 4. 照查證與冷讀者改的句子（逐字在 draft）

verified #1–3 方案表整表重判、資料截至 11-02；#5 API 表補 Haiku 5.5（兩檔＋快取）、刪「陣容中最低價」、還沒確定移出；L39／L339 依證據等級改寫（callout 移 incidents、標題寫「未見 Anthropic 說法」）；L86 席位矛盾改正＋Enterprise 公開價；L795 `%%` 待查證結案、L794 改寫為查證結果。冷讀者：現況改過去式並給出 Max 5x／Ultra 10x（Q4、Q2）；L117「Opus 5 的 142 小時」→ Opus 5.5 172／200 小時（推算，同表口徑）；L144「僅 Claude API」與研究預覽兩說改指乘數細節（與 L261 衝突）；L192、L194 到期規則移出、L219 點名；「事件流」外洩字 L159、L316 改；Q4「近三個月」答案住 history 結論段，母頁 callout 只指路（裁決 3）。不在本波：L90、L91 無來源句、L187 vs L262 研究預覽說法（列 `/wiki-lint`）。

## 5. 規則檔與腳本（逐字在 draft「進規則檔」；臨時副本實套後 `check_rules.py` ✅）

- `commercial/pages.md`：pricing 節整段換（sha256 鎖）——節名「（母頁）與兩子頁」；子樹說明；第 0 條路由表；**母頁每日准動清單**；同步動作表加一列「還沒確定：查證屬實當批移出」（N3）；事故表上限 8、留表優先序四層＋「同層最後動態新者在上、同日起始日新者在上、不看留言數」、單一社群回報型定義、表下可見一行取代 `%% 未列入總表 %%`、互動數的家（裁決 4）；定價與促銷可有 `## 最近三個月變了什麼`（一則一行、逾 3 個月 lint 移除；裁決 3）；計費切割改寫為「已歸檔，重啟寫 history」（裁決 2，刪「凍結到 2027-03-05」）；蒸餾兩子頁各自起算、共用 archive。
- `page-lifecycle.md` L52：登記 pricing 母頁每日寫入例外（裁決 7；清單見 N4）。
- `commercial/daily.md` L19：負責頁面一列拆三列。`models/pages.md` L155：計費事故的家改指 incidents。
- **腳本：無**。測試一處：`src/tests/test_reader_tags.py` EXCLUDED 加兩子頁（同第 23 波）。`reporter_of`／`owner_of` 在臨時副本實測兩子頁皆回商業。規則與測試都不碰 `guard_roles.py` GATE_FILES。
- **排序條文實跑**（`D/draft.md` B 節）：現有 17 件活躍事故（同一事故的多則條目算一件）依四層排完，前 8 即表；同日 10-24 兩件以起始日（08-02 vs 07-20）分先後，沒有平手。

## 6. handoff（主 session 先 `open --dry-run`，四筆已驗負責人；H-645373 本波結案）

| # | --from → --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 商業 → 功能 | entities/claude-code-known-issues | 💰 組 L99–129 各條「見 [[entities/pricing]]」中指事故者改指 `[[entities/pricing-incidents]]`；L49 不動（母頁分流節名保留） |
| 2 | 商業 → 社群 | topics/code-quality-decline | 三解表第三列「你這端的配置」補連 `[[topics/community-cost#用量去向歸因]]`；L229 可改指 `[[entities/pricing-incidents#還在發生的事故]]`（#38335 數字已由 H-9a89bc 涵蓋） |
| 3 | 商業 → 社群 | topics/community-cost | 「用量去向歸因」加一句回指 `[[entities/pricing#事故現在還在發生嗎]]`（分流的回程） |
| 4 | 商業 → 主編 | index | L56 鉤子去掉已過期的「09-14 起週配額換軌」，改「方案與牌價、額度掉得快先看分流」；💻 開發實務入口補一列「要花多少、怎麼被計費 → [[entities/pricing]]」（冷讀者入口） |

H-645373 結案 note：第 1 項總入口＝母頁分流（本波）；第 2 項根因三個（標記被剝、排序漂移、上限）本波以條文＋表修；第 3 項 pricing 側本波補，cqd／community-cost 側移入 handoff 2、3。

## 7. 閘（`D/tmp_before`＝HEAD 原樣、`D/tmp_after`＝套本案＋規則檔；`bash D/rebuild_after.sh <repo> <pristine>` 一鍵重跑，輸出在 `D/gates_*`、`D/run_tests_*.txt`、`D/rebuild_out.txt`）

| 閘 | 改前 | 改後（最後一行原樣） | 驗紅／看守 |
|---|---|---|---|
| `split.py` 防呆 | — | `ok {'pricing': 323, 'pricing-incidents': 324, 'pricing-history': 322, 'pricing-archive': 231}` | 對改後副本跑 → `AssertionError: wiki/entities/pricing.md 自設計 commit 933a34d 後被改過`（redtest 1） |
| `verify.py` | — | `照搬行逐字核對 548 行；懸置標記 4→4`、`結論：OK`（out 與 tmp_after 兩跑法） | 刪 HERMES 列＋刪母頁懸置 → `缺：P303`、`缺：P602`、`4→3`、`FAIL`（redtest 2） |
| `gen_wiki_frontmatter.py` | exit 0 | exit 0；index L56 投影 `↳ 子故事：archive、history、incidents` | — |
| `check_hierarchy.py` | `✅ 通過（32 個母頁）` | `狀態：✅ 通過（32 個母頁）` | 母頁 callout 改 10-31 → `❌ hub 落後：…2026-10-31 < 子樹最新新聞 2026-11-01`（redtest 4） |
| `check_pending_markers.py` | ✅ 212／基線 212 | `狀態：✅ 懸置標記語法檢查通過`（212；3 筆換 slug 待入基線；舊字樣 18→18） | 實作後 `--rebuild-count --reason "第 24 波 pricing 拆頁：3 筆換 slug（entities/pricing→entities/pricing-incidents）"` |
| `check_wiki_freshness.py` | OK 140 頁 | `OK: wiki 新鮮度檢查通過（142 頁；…）` | incidents 的兩個 11-01 歸因網址換掉 → `[無從對照] entities/pricing-incidents`（redtest 5） |
| `check_reader_language.py` | FAIL 2（存量，非本頁） | FAIL 2（同兩筆）；**本波貢獻 0** | `moves.py` reader：改前子樹 0／改後 0 |
| `check_cell_limits.py` | FAIL 153（第 21＋23 波待本機） | FAIL 210；**本波 +57，全是搬家** | `moves.py`：命中 62 全配回 `entities/pricing` 舊基線（同錨點、長度不超）、57 筆換頁名、配不回 0；塞 247 字條列 → `新 … list_item 247`（redtest 3）。逐筆見 map 第四節 |
| `check_rules.py` | ✅ | `狀態：✅ 全部確定性檢查通過`（規則檔已套） | — |
| `build_web.py` | 斷鏈 23／錨點 0，exit 0 | `斷鏈 WARN 23／錨點 WARN 0`，exit 0 | 刪母頁指路殼 → `錨點 WARN 1`、exit 1（redtest 6） |
| `run_tests.py` | 1 FAIL（`test_repo_currently_has_no_new_hits…`）＋2 閘紅、1,334 案 | 同樣 1 FAIL＋2 閘紅、1,334 案 | 沒有新紅種類；cell 數 +57 |

## 8. 新裁決點（主 session 判）

- **N1** 照條文排序後 infostealer（官方已承認）入表、#38335 出表到表下一行。備案：主編先查 08-30 官方通知是否等於「已修」（是→轉 ✅ 出表，#38335 回第 8 列）。
- **N2** 母頁 `### 事故與爭議（…）` 永久指路殼（daily/2026-10-24 錨點，健檢卡 §9 漏列）。同第 23 波 N2。
- **N3** 還沒確定表補退場條文「查證屬實當批移出」，本波移 4 列（3 ✅＋1 過期）。ledger 只點名 Haiku 5.5 一列；其餘三列不移則表又只增不退（健檢卡 §11）。
- **N4** page-lifecycle L52 登記的母頁每日例外＝同步動作表全部對象＋`## 現況`＋路由表最後動態，比 ledger (7) 列的三樣寬：只登三樣，API 表與一小時表的每日覆寫（pages.md 同步動作表既有）就違反母頁契約。通路與乘數不入每日清單（主編週更，已有 weekly.md）。
- **N5** 17 行舊 `%% 未列入總表 %%` 備忘一併砍（理由寫著「互動量低於現有 6 列」，正是要廢的排序；留著會被明天的維護者照抄）。讀者可見一行取代。
- **N6** cell 基線本波 +57 全為搬家，比照第 21／23 波分支例外，累計待本機重建 153＋57＝**210**；`docs/page-audits/claude-code-2026-11-01-baseline-moves.md` 第 1 步預期值與 reason 同批改。
- **N7** history 宣稱最後新聞更新 10-30（`claude.com/pricing` 歸因），不宣稱 10-31（#47509 那則無歸因，宣稱即 freshness 紅）。
- **N8** Ultra 5 小時窗（V5）列進還沒確定；Ultra 旗艦 50% 標推論。若主編實作前補查到官方原文，改兩格即可。

## 9. 不選的方向

- 乙案（按讀者三子頁）：ledger 已評，多一頁、多 5 筆回掃。
- 事故表依類型分組或上限 10：ledger 定 8；分組會讓「最後動態」排序失效。
- 把 #38335／#16157／#37394 併一列：頁面明寫未證同根因，不可合併。
- 事件流內的留言數也改成只寫號碼：那是當日快照，照搬不改（條文寫明）。
- known-issues L49 直接改指 incidents：分流入口在母頁才三路都只一跳。
- 本波蒸 history 07／08、移出收錄漂移 3 則：ledger (5)(8) 留下次 lint。
- 方案表加「月度 API 額度」新欄：骨架規則禁加欄，原「可領優惠」欄整欄是「—」正好承接。

**可行性前提**：同一個 commit 含四頁、規則檔 4 份＋測試 1 份、`--rebuild-count`、baseline-moves 文件 153→210、handoff 1–4 開帳與 H-645373 結案、`wiki/log.md` Query 條目、ledger 定稿列；在 `pricing.md`、`pricing-archive.md` 仍是 `933a34d` 版、`commercial/pages.md` pricing 節 sha 未變時跑 `split.py`／`rules_patch.py`（否則先紅，續用設計者重跑，不准手切）；今天 11-02 的 ingest 若先落地 pricing，第 0 步就會擋下。

## 10. 最不確定的一件事

incidents 的長速：事故＋配額 10 月約 14 則、50 行，296 行的頁約三個月後過 450；07 月（12-01 到期）與 08 月兩段蒸完約回到 220。真正的不確定是「額度掉得快」類 Reddit 單帖每週數則都會進事件流——若 lint 不照條文把 90 天無佐證的單帖移出，頁面會被它們撐大，而它們從來進不了表。
