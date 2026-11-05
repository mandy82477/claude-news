# 第 28 波設計提案：entities/sonnet-5-5 從「誰報導了什麼」改回「怎麼拿到、會壞什麼」（2026-11-05）

> 上游：健檢卡 `sonnet-5-5-2026-11-05.md`、冷讀者 `wave28-cold-reader-2026-11-05.md`、查證 `sonnet-5-5-2026-11-05-verified.md`。ledger「2026-11-05｜第 28 波」十個裁決點照做，不重開。
> 機械產物在 `<scratchpad>/w28/design/`（下稱 `D/`）：`out/wiki/entities/sonnet-5-5.md`（新頁全文，單一來源）、`apply.py`（鄰居逐段替換；每段舊字須在 HEAD 恰出現一次，否則 AssertionError；`--only-core` 不套 N2／N3）、`rules_patch.py`（models/pages.md、daily.md）、`tmp_after/`（套用後的 repo 副本）、`gates_inrepo.txt`、`build_after.txt`、`run_tests_after.txt`。行號一律指 HEAD `e66cc9d` 原檔。

## 1. 推薦案（一個）

使命句（ledger 1）放在標頭欄位後、callout 前，前面另有 page-templates L42 要的 H1 下定位句（≤60 字）。

| 節（改後） | 行 | 內容 |
|---|---|---|
| 標頭＋定位句＋使命句＋callout | 20 | callout 三條：預設不是它／`/model sonnet`＋v2.1.284+＋effort medium／換來 5＋1 項（ledger 5；可見字 113） |
| `## 現況` | 6 | 兩段：①11-05 查官方的預設與 fallback ②發布與定位；刪「自 10-01 起無新動態」 |
| `## 你現在拿到的是什麼` | 18 | 錨點凍結；8 列（加「context 與最大輸出」，ledger 7）；資料截至 11-05；表下「補充」4 條（別名看平台、兩個 effort 預設、牌價不變、快取價是發布價） |
| `## 從 Sonnet 5 換過來會壞什麼`（新） | 18 | 官方 What's new 5＋1 項，一項一條附官方錨點；「換過來還會遇到的事」5 條（Claude Code fallback、API fallback、快取下限 512、sampling 400＝N1、兩則媒體佐證） |
| `## 這些數字是誰量的` | 20 | 官方表 8 項 × Sonnet 5.5／Sonnet 5／Opus 5.5（N2）；4 條表下（對 Opus 5.5 差距、註腳 effort、Reddit、跨家出口） |
| `## 熱度與試用價值` | 4 | 一行指 feature-radar（ledger 6） |
| `## 跟它怎麼說話` | 14 | 5 句；第 1 句去掉「預設 high」（家在對照表）；第 4 句改指新節；L130 刪 |
| ~~`## 核心功能`~~ | 0 | 砍（ledger 7）：1M／128K 進對照表，v2.1.284 在對照表，設計敏銳在現況 |
| 相關議題 | 12 | 補 haiku-5-5；business → anthropic-ipo；sonnet-5、opus-5-5 鉤子改成現況 |
| 參考來源 | 19 | 補官方 6 份（模型頁、What's new、migration guide、model-config、Sonnet 5 模型頁、prompting） |
| 歷史記錄 | 34 | 10-01、09-30 兩列把查證結果寫進事件欄；09-28 細節瘦身，HN、路透留在這裡（ledger 4） |

主頁 190→**204 行**（正文 164→178）。變長的 14 行全是新節的官方 5＋1 清單；表下細節 11 條→8 條，「GDPval 差兩分」4 處→0、v2.1.284 8 行→6 行。

## 2. ⟨Q-01⟩ 收尾（ledger 3；daily-contracts L94–103）

- 本頁 L60 短標記與 L69–71 懸置細節**成對刪除**，改寫為事實（對照表「現在誰是預設」列，出處 model-config 2026-11-05）。sonnet-5 L48–49 同題 🔎 同批改寫為事實（同維護者）。
- 回掃探針「v2.1.284、Claude Code CLI 預設」「Sonnet 5.5、Claude Code CLI 預設」：sonnet-5 L57／L78／L95，opus-5-5 L160，model-comparison L63／L76／L85／L151–152／L160（N3），haiku-5-5（N4）都列在 draft C 節；pricing L113／L133／L134、pricing-history L112／L114 → 商業；feature-radar L37 → 主編。
- **計數閘明示**：兩筆都是 `PENDING_RE`（`scripts/pending_markers.py` L36）的完整標準式，指紋就在 `data/pending-marker-count.json`。全庫 **223→221（−2）**，`check_pending_markers.py` 會紅（`_marker_count_gate`，L288–326）。實作者同批跑 `python scripts/check_pending_markers.py --rebuild-count --reason "第 28 波 sonnet-5-5：⟨Q-01⟩ 與 sonnet-5 同題 🔎 兩筆經官方 Claude Code model-config 查實結案（−2）"`。在 `D/tmp_after` 實跑過：rebuild 只列這兩筆 removed、0 筆 added，重跑轉 ✅。本頁 `pending_count` 1→0（`gen_wiki_frontmatter.py` 實跑確認）。

## 3. 規則檔（逐字在 draft 第二節；`tmp_after` 實套後 `check_rules.py` ✅）

- `models/pages.md` 在「entities/opus-5 的兩張表」前新增 `## entities/sonnet-5-5 的五節`：對照表 8 列固定、「現在誰是預設」出處須為 model-config；新節「一項一條附官方錨點、前代本有的限制不寫成換代變更」；基準表四欄、上限 8 列、互動量進歷史；熱度一行不建表；歷史上限 20 列。h3 標題自帶 slug 與「覆寫」（pages.md L179），`table_census.py` 的 `_mechanism()`（L51）對本頁三張表從「無」轉「有（pages.md）」，已在 `tmp_after` 實跑。
- `models/daily.md` 負責頁表加 sonnet-5-5 一列（觸發條件明列 What's new／migration guide／model-config）。健檢卡 §9 指出本頁只靠 L21 概括條款、無執行機制。
- 三頁 5.5 共用骨架不做（ledger 9）。opus-5-5、haiku-5-5 的節不在本波。

## 4. 同維護者鄰居（只改事實句與互指句）

- sonnet-5：L48–49 懸置改寫為事實；L57、L95 現在式改過去式；L78 程式區塊改「要用本代必須明確指定」，ID 改 `claude-sonnet-5`（N5）；最後更新 → 11-05。
- opus-5-5：L160「[[entities/sonnet-5]] — Claude Code 的整體預設」改指 sonnet-5-5；最後更新 → 11-05。
- model-comparison（N3）、haiku-5-5（N4）：預設做，主 session 否決就跑 `apply.py --only-core`（已驗，閘全綠）。

## 5. 轉知（draft 第四節；三筆都已 `--dry-run` 驗過負責人：H-275867 ×2、H-390777）

商業 ×2（pricing L113／L133／L134「為預設」；pricing-history L112 標題與 L114「11-02 更正」）、主編 ×1（feature-radar L37 指路目標，ledger 10 說主編直接改，附原文備用）。

## 6. 閘（`gates_inrepo.txt`＝臨時換進 repo 跑完、已用 `git show HEAD:<path> > <path>` 還原七檔，`git status` 乾淨）

| 閘 | 改前 | 改後 | 驗紅 |
|---|---|---|---|
| `check_cell_limits.py` | OK 無新增 | **`OK: 字元上限機械閘 — 無新增超限`**（本頁 0 筆、鄰居 0 筆新增） | 對照表一格加長到 >120 → exit 1。model-comparison L63 第一版 245、第二版 201 字元都被擋，第三版才過（L91–92 `TABLE_LIMIT`／`LIST_LIMIT`） |
| `check_reader_language.py` | OK | **`OK: 讀者語言閘 — 無新增命中`** | 熱度句塞「記者」→ exit 1（`TERMS`，L51） |
| `check_pending_markers.py` | ✅ 223 | **`狀態：❌ 懸置標記語法有誤`**（223→221，預期的紅，見 §2）；rebuild 後 `狀態：✅ 懸置標記語法檢查通過` | 本身就是驗紅 |
| `check_rules.py` | ✅ | `狀態：✅ 全部確定性檢查通過`（規則檔已套） | — |
| `build_web.py`（副本） | 斷鏈 23／錨點 0 | 斷鏈 23／**錨點 WARN 0**，exit 0 | callout 錨點截字 → `錨點 WARN 1`、exit 1（`check_wikilink_anchors`，L372） |
| `check_hierarchy`／`check_wiki_freshness`（副本） | ✅ | ✅ 32 母頁／OK 143 頁 | — |
| `run_tests.py`（副本） | — | 1,334 案：cell 測試在第三版綠；另 2 筆 devpractice 失敗是副本沒有 `.git`（`KeyError: 'last_sha'`），實作時在 repo 內重跑 | — |

## 7. 新裁決點（主 session 判；括號內是我的預設）

- **N1 sampling 參數 400 不是換代變更**：設計時對 Sonnet 5 官方模型頁（2026-11-05 WebFetch）看到「Good to know」同樣寫 `temperature`／`top_p`／`top_k` 回 400。照 ledger (2) 寫進「會壞什麼」就是虛報。（預設：放在「換過來還會遇到的事」，寫明「Sonnet 5 本來就是如此，從 4.x 跳上來的才會撞到」；pages.md 條文同時禁止把前代本有的限制寫成換代變更。）
- **N2 官方基準表是 8 項，不是 7 項**：發布文另有 FrontierCode 1.1（Main）46.2／42.4／54.4，Opus 5.5 的 54.4 和 opus-5-5 L81 吻合；verified 漏列。另有兩條註腳：TB 4.0 的 Opus 5.5 是 xhigh、FrontierCode 的 Sonnet 5.5 是 max。verified 說「與 Opus 5.5 差距在 1–3 分內」，在 FrontierCode 不成立（差 8.2）。來源是設計者用 WebFetch 取得的摘要。（預設：8 列加註腳；主編實作前對原文再核一次。）
- **N3 model-comparison 回掃（同維護者，ledger 沒點名）**：L63／L76／L85 三處「CLI 是否同步見 sonnet-5-5」改成事實；L151–152 兩列的判準是「官方沒確認」，現在官方已確認，照該表 Sonnet 4.5 的先例移出表，L160 改一句指新節。L151 是本頁唯一的錨點入邊，改指 `#從 Sonnet 5 換過來會壞什麼`，建置驗過。（預設：做。daily-contracts L99 要求回掃引用方。）
- **N4 haiku-5-5 的「10-07 同批砍半」是錯的（V5）**：L67、L167 刪；L126 鉤子改「同 5.5 家族的中階款，快取讀取 $0.10」。（預設：做。這幾句指向本頁一件不存在的事。）
- **N5 sonnet-5 L78 的 `claude-sonnet-5-20260701`**：官方 Sonnet 5 模型頁的 Model ID 是 `claude-sonnet-5`。這個區塊本來就要改，順帶修正。（預設：改。）
- **N6 表下區塊名「表下細節」改成「補充」**：冷讀者內部用語第 3 條。只改本頁；opus-5-5、haiku-5-5 留給三頁共用骨架那一波。（預設：改。）
- **N7 OSWorld 版本標示兩頁不一致**：本頁依 Sonnet 5.5 發布文寫「2.1（partial）」，opus-5-5 L87 寫「2.0（partial）」，同為 81.8%。本頁照一手寫，不碰 opus-5-5。（預設：記 ledger，留給 opus-5-5 下次健檢。）

## 8. 不選的方向

- 收窄成換代卡：ledger (1) 已否，官方單家基準會沒有家。
- 「會壞什麼」留在對照表一格：6 項加 5 條塞不進 120 字元，ledger (2) 要求自成一節。
- 5＋1 做成表（變更｜會怎樣｜怎麼改）：沒有要跨列比較的東西，daily-contracts L23 判用條列。
- 熱度保留 4 列鍵值表：ledger (6) 否，鍵值表也不合 L23。
- 刪掉 10-01、09-30 兩則歷史：那是當時的報導，結果寫進事件欄就夠（opus-5 歷史條文同法）。
- 這波順便補 model-comparison Effort dial 的 Sonnet 5.5 檔位（冷讀者 §最想改 3）：不在本波，一次一頁。

**可行性前提**：同一個 commit 含本頁、sonnet-5、opus-5-5（N3／N4 過的話再加 model-comparison、haiku-5-5）、`models/pages.md`、`models/daily.md`、`data/pending-marker-count.json`（rebuild），外加三筆 handoff 開帳。`apply.py` 以 HEAD `e66cc9d` 為底；今天 11-05 的 ingest 如果先動到這五頁，斷言會先紅，要續用設計者重產，不准手改。

## 9. 最不確定的一件事

「Claude Code 各方案」的寫法。model-config 列的是 Pro、Max、Ultra、Team、Enterprise、Anthropic API 預設 Opus 5.5，Foundry 預設 Sonnet 4.5。本頁 callout 與現況寫「各方案」，沒提 Foundry；Foundry 例外只在表下「`sonnet` 別名看平台」一條。讀者若用 Foundry，從 callout 會讀錯，要看原考題複驗 Q2 有沒有人撞上。
