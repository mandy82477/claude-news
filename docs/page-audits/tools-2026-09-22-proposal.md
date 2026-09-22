# 第 15 波設計提案：topics/community-tech-tools

使命句（主 session 代判，健檢卡候選 A）：**你卡在哪個症狀，社群現在該裝哪一個——以及什麼時候該換掉它。**
逐字稿見 `tools-2026-09-22-draft.md`，逐行去向見 `tools-2026-09-22-proposal-map.md`。
官方事實一律取自 `tools-2026-09-22-verified.md`；頁面上所有數字與 owner 字串以它為準，與健檢卡衝突處以 verified 為準。

## 1. 推薦案（一個）

**給決策表裝上一個讀者看得到的時鐘，並讓那張表自己就能作答；152 列目錄清掉讀者按不下去的 43 列。**

根因（健檢卡第 8 節、verified 第七節）：這頁最值錢的是 L48–L75 那 28 行判斷層，病不在版面——**判斷層沒有時鐘、次選欄不能獨立作答、目錄層有四成的列讀者點不進去**。三個首選（Harness／Omar／Groundtruth）四個多月沒人回頭看，其中兩個已改名、一個 7★，而頁面同時寫著 L50「本表每週複查一次」與 L64「不隨時間自動回訪」——讀者讀完不知道該信哪一句。四件事同時做：

1. **證據欄從一個日期變兩個日期**：`🟢（判 04-29 起多來源｜查 09-22，99★）`。**判**＝下判斷那天、**查**＝最近一次確認這個專案還在不在那天。不加第五欄——`scripts/skill_interest_snapshot.py:248` 把總覽頁重印區的表頭寫死成四欄，加欄會讓那邊出現五格配四欄；`weekly.md:29` 也明訂欄位形狀是總覽頁的解析契約。L50 與 L64 的互打就此解掉：頁面只留一句「最後一次確認寫在證據欄的**查**」，**多久回訪、誰回訪、逾期怎麼標三條住 `weekly.md`**（draft B-1）。
2. **決策表十列的工具名全部帶連結**（原本九列裡只有 3 列有）：首選與次選一律連到 09-22 查證後的現址。冷讀者說「先裝這個」給不出安裝方式——我們不編造安裝指令（verified 沒有這項事實），改成一跳就能到 repo 自己看 README。連結的 URL 在 `check_cell_limits.py` 量測前會被剝掉，幾乎不佔格子長度。
3. **新開「額度快用完，想在斷線前被提醒」一列**（主 session 代判開列）：首選 [Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)，證據 **⚪（查 09-22，8,713★）**——星數就是 ⚪，誠實標。症狀句刻意與「帳單爆了，看不到錢花在哪」分開（Max 訂閱者沒有帳單，這正是冷讀者 Q2 被排除的原因）。官方側被動可見的出口指 [[feature-radar]]，連頁不連錨。
4. **目錄移除 43 列「沒有任何可點連結」的存量列**，並把同一條寫進入選標準。依據不是新規則，是現行 `weekly.md:39` 的排除句（「無公開 repo / demo / 連結」不收錄）——這 43 列是該條立法前的存量。全部 43 個名字在 `wiki/log.md`、`*-archive.md` 或其他頁另有出處（逐列已機械核對，見 map 末節），事實不消失，讀者少 43 次「拿到名字裝不了東西」。

## 2. 不選的方向（各一行）

- **加第五欄「最後確認日」**：形狀最乾淨，但要同批改 `skill_interest_snapshot.py` 的寫死表頭與 `weekly.md:29` 的解析契約，代價落在一個本波不該動的機器頁上。
- **拆子頁**：健檢卡拆子頁候選 0，我獨立同判——三訊號無一組同時亮，病是沒有時鐘不是題目太多。
- **改寫症狀句讓它更好懂**：五個症狀句是 `data/skill_interest_watch.json` 的 `tools_symptom` 與四條 🧰 行的對帳字串，改一個字就讓 `check_tools_page.check_spokes` 轉紅（實測見第 5 節），收益不抵代價。
- **換掉撐不起的首選（Harness／Omar／Groundtruth）**：改名、星數掉、沒人回訪都不是否定證據，`weekly.md:19` 明訂只在新證據時換；三列的替代品（Merge Queue 125★、HUD 28★、Proof Loop 11★）都沒有更強的證據。改的是描述與採用值，不是首選。
- **順手砍「AI 輔助開發的長期副作用」整節**：砍整節屬使用者裁決；改為修掉「尚無成熟工具」與節內引用兩個工具的自相矛盾，壓成三行並指向 [[topics/official-community-gap]]。
- **在 ⟨Q-01⟩ 上再開新的懸置**：它自述「已查證」卻用未決語法，直接降為普通散文（見第 4 節，不影響任何基線）。

## 3. 可行性前提（一行）

決策表症狀欄一字不改、`## 我卡在這裡` 與 `## 🧩 Skills 速查（依 coding 用途分類）` 兩個節名不改、`| 首次出現 |` 欄保留——`review-registry.json:101–119` 的三個凍結錨點與 `skill_interest_snapshot.py:147／167` 的兩條 regex 全部靠這三件事，本案未動其中任何一項（清單見第 5 節）。

## 4. 新骨架

| 節 | 一句用途 | 行數（原→新） |
|---|---|---|
| 標頭＋callout | 一個日期口徑；今天最重要的是三個首選改名 | 12 → 12 |
| `## 摘要` | 本頁答什麼、兩個日期怎麼讀、六個出口（新增 OCG 與 SIW 分工句） | 6 → 6 |
| `## 我卡在這裡` | 決策表 9 → **10 列**，全列帶連結，證據欄兩個日期；圖例把守則句拿掉 | 17 → 18 |
| `**推薦細節**` | 8 → **12 條**（新增：三個改名、ness 現況、額度告警官方側、額度三工具強度、Groundtruth 為何仍是首選、三個查不到的次選） | 10 → 14 |
| `### AI 寫久了人會不會退化` | 節名不再與內容互斥；四個現象壓成三行，指向 OCG | 8 → 6 |
| `## 🧩 Skills 速查` | 四組，「寫碼紀律」移除 awesome-ux-skills（無連結、🟡 05-08 最弱），5 → 4 列留餘裕 | 42 → 41 |
| `## 指標說明` | 類型列 10 → **12 值**（補 `模型路由`／`UI 工具`）；證據列補「判／查」；採用列給 ✅ 一句讀者看得懂的判準；入選標準改寫成「點不進去就不列」 | 8 → 8 |
| `## 工具目錄` | **152 → 112 列**（移除 43、新增 3、改寫 10、倒序修正 6 列移位）；表前加一句「每一列都點得進去」 | 156 → 116 |
| 收錄註記＋Geosql 細節 | ⟨Q-01⟩ 降為普通散文，L124／L212 兩處指路同批改 | 6 → 6 |
| `## 參考來源` | 4 → 6 條（補 `skill-interest-watch`、`community-large-codebase-workflow`） | 6 → 8 |

**315 → 281 行**（scratchpad 實測值，非估算）。

## 5. 我保住的錨點清單（實測，非宣稱）

改對象頁前先讀 `scripts/check_tools_page.py`、`scripts/skill_interest_snapshot.py` 原始碼，本案保住以下六項：

| 錨點 | 誰在讀 | 本案動了嗎 |
|---|---|---|
| `## 我卡在這裡`（行首、獨佔一行） | `check_tools_page.py:32／41／55`、`skill_interest_snapshot.py:167`、`review-registry.json:107` | 沒動 |
| `## 🧩 Skills 速查（依 coding 用途分類）` | `check_tools_page.py:41／43` | 沒動 |
| `## 工具目錄` | `skill_interest_snapshot.py:147`（總覽頁印「N 列工具目錄」的分母） | 節名沒動；列數 152 → 112，總覽頁隔天自動改印 112 |
| 決策表四欄表頭與 `|---|---|---|---|` | `skill_interest_snapshot.py:248` 寫死四欄表頭 | 沒動（這是不加第五欄的原因） |
| 五個症狀句原文 | `data/skill_interest_watch.json` 的 `tools_symptom`（codebase-understanding／implementation-guard／testing-verification／orchestration×2／git-hygiene）＋ `check_tools_page.check_spokes` | 一字沒動；新列的症狀句是新增，不影響對帳 |
| `| 首次出現 |` 欄、`先裝這個` 欄 | `review-registry.json:103／115` | 沒動 |

**四條 🧰 spoke 行**（`community-large-codebase-workflow:63／87／113／139`、`enterprise-cost-management:82`）引用的症狀句全部保留；只有 `:63` 的括號裡寫「首選 Harness」要隨改名同批改（見第 7 節），那句不在機械對帳範圍內，靠人。

**驗紅（scratchpad 副本，未動 wiki）**：把副本的 `## 我卡在這裡` 改成 `## 我現在卡在這裡` 後——
- `skill_interest_snapshot.py:167` 的 `re.search(r"^## 我卡在這裡\s*$…")` 找不到 → `decision_table_from_tools()` 回 `([], "")` → `render()` 第 219 行改印「⚠️ 本次抄不到決策表」，**總覽頁整張決策表消失**，且 `row_by_symptom` 空掉、九個類別的「本庫判斷」全部退回「本庫尚無判斷」。它不會丟例外，是**安靜降級**。
- `check_tools_page.py:70–71` 同時報 `找不到 \`## 我卡在這裡\` 決策表`，exit 1。
另一次驗紅：把 `它說做完了，但根本沒做` 改成 `它說做完了，其實沒做`，`check_spokes` 立刻吐兩條——`spoke 引用失效 community-large-codebase-workflow.md:139` 與 `榜橋引用失效 skill_interest_watch.json[testing-verification]`。

## 6. 閘：我自己跑過的結果（原樣抄最後一行）

現行基線（動手前，對象頁）：
```
WARN: 存量基線內 4 筆／1 頁（前 5 頁：topics/community-tech-tools(4)）
OK: 字元上限機械閘 — 無新增超限
```
```
WARN: 存量基線內 0 筆／0 頁（前 5 頁：無）
OK: 讀者語言閘 — 無新增命中
```
```
狀態：✅ 數字皆帶日期、首選皆唯一、全站 🧰 spoke 症狀句對帳通過
```
```
ℹ️ 懸置標記 114 筆（基線 106，未低於）
狀態：✅ 懸置標記語法檢查通過
```

把 draft 的「進頁面」部分整份套進 scratchpad 副本後（`scan()` 直接對副本跑，wiki 未動）：

| 閘 | 改後 | 說明 |
|---|---|---|
| `check_cell_limits` | 命中 3 筆，**新增 0** | 存量四筆刻意**不改寫** L68／L69／L70（指紋＝內容雜湊，改寫就掉出基線、若仍 >200 會轉紅；這三條今天內容仍成立）；第四筆 ⟨Q-01⟩ 因改寫而消失（新句 <200）。新增的 omnigent 格首版量到 121 字元（上限 120），已在 draft 裡砍成 105 |
| `check_reader_language` | 命中 **0** | 注入「本表由記者每日 ingest 維護，逾期列一律退場。」→ **3 命中**（記者／ingest／退場），閘會紅 |
| `check_tools_page` | `check()` 與 `check_spokes()` 皆回 `[]` | 10 列首選皆唯一（`—` 那列豁免）、數字皆帶日期 |
| `check_pending_markers` | 114 筆不變，基線 106 | ⟨Q-01⟩ 是**舊字樣**不是新語法標記（`iter_pending` 對本頁回 0 筆），降級不動總數；舊字樣 41 → 40，腳本只擋「增加」 |

注入 130 字元儲存格 → cell 閘 **新增 1**，兩閘都驗過會紅。

## 7. 回掃清單

**同維護者（社群記者，本波同批；只改該句，不重寫頁）**

| 頁：行 | 現況 | 改成 |
|---|---|---|
| `community-large-codebase-workflow:63` | 「…列（首選 Harness）與…（首選 Omar）」 | 「首選 ness（原名 Harness）」；Omar 不變 |
| `community-tech-patterns:1199` | `#### Cockpit（episko.dev）：…（2026-08-02）` | **不改**——技術彙整是 08-02 當時的事件條目，改名的事實寫在本頁目錄列 |

**跨維護者（`python scripts/pending_handoffs.py open --from 社群 --to <類別>`，類別用中文；3 筆）**
1. → **功能**：`feature-radar` 沒有「額度快用完主動告警」的官方狀態條目，本頁新列的官方側出口指過去；官方一手見 verified 第四節（#13585 OPEN／👍 124、#65292 not_planned、`/usage` 與狀態列僅被動可見）。
2. → **功能**：`official-community-gap:78` 以 Throttle Meter 當代表社群工具，該列已因無連結移出本頁目錄；若仍要引用，請換成點得進去的工具。
3. → **主編**（`wiki/index.md`）：L27 括號裡的症狀清單沒有「額度快用完」，本頁已開列，建議補進去；L99 摘要「再看工具目錄的活躍度與採用狀態」與新的 112 列目錄仍相符，不必改。

**只記 `wiki/log.md`、不另開轉知**：43 列移除的理由與名單、⟨Q-01⟩ 降級、新列開列依據（#13585＋#65292＋兩波冷讀者，達 `weekly.md:43` 的兩筆獨立需求證據）。

## 8. 裁決點（一個，屬使用者）

**tools 的「我卡在這裡」與 `skill-interest-watch` 的逐字副本要不要併。**
- 保守預設（本案正文照此寫）：**兩頁都留、SIW 不動、`index.md:27` 不改指**——這是 2026-09-03 方案 D 的已知代價。
- 本案在保守預設下**仍降低了代價**：摘要 L44 補一句讀者語言的分工（「SIW 是這張決策表的每日副本＋各類規模榜，判斷只寫在這一頁」），冷讀者兩波「說不出 A 看這、B 看那」的直接原因就是這句不存在。
- 若使用者裁「併」，本頁要動的句子逐字見 draft 的〔併〕區塊（摘要出口句、參考來源那一條）。
- **不改 `skill-interest-watch.md`**：機器整頁覆寫頁，它的決策表抄自本頁，本頁改了它隔天自動跟。

## 9. 實作順序（單一序列，10 步）

1. 標頭 A-1、callout A-2、摘要 A-3。可驗：全頁只剩一個日期口徑。
2. `## 我卡在這裡` 整節換成 A-4（節名、表頭、10 列、圖例、12 條推薦細節、副作用節）。**症狀欄五個舊句一字不改。**
3. 速查「寫碼紀律」組移除 awesome-ux-skills 那一列。
4. 指標說明四列照 A-5 換。
5. 工具目錄：先移除 43 列 → 再套 10 列改寫 → 再插 3 列新列 → 最後依日期重排（六列移位）。可驗：112 列、無倒序違規。
6. ⟨Q-01⟩ 降為普通散文，同批改 L124／L212 兩句指路。
7. `## 參考來源` 補兩條。
8. 同維護者回掃 `community-large-codebase-workflow:63`。
9. 跑閘：`check_tools_page.py` → `check_cell_limits.py --page topics/community-tech-tools` → `check_reader_language.py --page topics/community-tech-tools` → `check_pending_markers.py` → `gen_wiki_frontmatter.py` → `check_hierarchy.py` → `build_web.py`（錨點 WARN 不得增加）。
10. 跨維護者轉知 3 筆、`wiki/log.md` 條目、`python scripts/run_tests.py` exit 0。

## 10. 仍需主編補查（本案沒有它也能上，但下一波該補）

1. **verified 第五節的五個查不到的工具**（Writ／VIR／clarp／claudely／Caliber）——三個是決策表次選。本案的處置是誠實寫「09-22 查不到公開頁」，不是刪次選；下一波若仍查不到，該考慮把它們從次選欄拿掉。
2. **clarp 的政策風險前提**：計費制度自 05-21 已數次改版，L74 那句「6/15 起的計量計費」的前提未重查。
3. **決策表「判／查」的機械看守**：本波只有人工填。最小方案是一支只掃決策表證據欄、`查` 逾 60 天 WARN 的腳本，照 `data/reader-language-baseline.json` 的存量基線先例；本波不做——它要掛 `run_tests.py`，而實作者不准改該檔。
