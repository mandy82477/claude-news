# 第 18 波評審：topics/community-tech-patterns 拆成母頁＋七子頁（2026-10-09）

> 審的對象：`patterns-2026-10-09-proposal.md`、`-proposal-map.md`、`-draft.md`；上游健檢卡、冷讀者、verified；ledger 2026-10-09 裁決（Context 歸 B、archive 不拆、F2 設計者判）。
> 驗證全在 `scratchpad\w18\review\`（下稱 `R\`）：重跑 `split_patterns.py`、逐則比對、臨時 repo 跑全部閘、freshness 改壞驗紅、路由規則重算。檔案路徑都指那裡，修法可直接複製。
> 事故自報：第一次重跑時我的 `common.py` 路徑替換沒成功，輸出寫進了設計者的 `w18\out\`（08:40）。內容逐位元組與 `R\out\`、`out\generated\` 正文相同，沒有改到任何內容，只動了 mtime。

## 結論

- 🔴 4 條、🟡 8 條。對帳相等；251 則逐字搬家屬實；錨點 WARN 0→0；pending 不擋。
- 最要緊的是 🔴1：設計者分群用的不是自己寫進 pages.md 第 0 條的規則，有 7 則節點住錯頁。明天記者照規則寫，就會和今天的落點不一致。
- freshness 補丁改壞驗紅結果：設計者四案全過，但我造的第 5 案（新子頁漏報歸因、母頁天天有自己的歸因）**補丁版判綠、原版判紅**，等於放寬過頭。改成「上層歸因要網址出現在本頁才算」以後，五案全過，現行全庫兩個日期都 exit 0（🔴2）。
- 實作單從 draft §H 的 6 步改成 14 步。三件閘檔的改動子 agent 做不了，hook H6 會擋，所以移到主 session 做（🔴3）。

## 自己重算的數字

| 項目 | 設計者 | 我重算 | 證據 |
|---|---|---|---|
| 正文 2,461 行去向 | 107＋2,289＋37＋16＋12 | 相同，合計 2,461 | `R\run.log`（`split_patterns.py` 斷言每行恰消費一次） |
| 輸出與 generated 正文 | — | 八頁逐字相同 | `R\cmpgen.py` |
| 251 則節點 | 一則不少 | 250 則逐字、1 則（WaLiAPI L342）只改一個錨點；每則都留在原月份；各子頁內順序跟原檔一致 | `R\myverify.py`（另寫一套分段，沒有用 `verify_split.py`） |
| 各月分布 | map 表 | 10 月 A2 B8 C4 D2 E4 F1 15 F2 7，其他月份也全部對得上 | 同上 |
| 母頁行數 | 205（25＋180） | 205；子頁正文 477／385／375／431／348／383／231 | `wc` |
| 抽驗 4 節 | — | 把關層 L95–108→E、查證備註→E、2026-06／05 總結＋相關實體＋參考來源→母頁：逐字相同。誰負責拆分→A、缺口追蹤→A：只有 map 列出的替換 | `R\secchk.py` |
| 錨點 WARN | 0→0 | 改前副本 0、改後 0 | `R\run_gates.py` |
| pending | 3 減 3 增不擋 | 152 筆（基線 131），OK | 同上 |
| cell `--allow-grow` | 新增 66 | 改前副本跑出新增 66、全在七子頁；但設計者副本帳本的 removed 是 **130**，不是 66（見 🟡4） | `w18\tmprepo\data\baseline-changes.jsonl` 最後一行 |

## 一、機器

**🔴1 分群演算法 ≠ pages.md 第 0 條的規則：7 則住錯頁**
- 證據：`R\routechk.py` 和 `R\patterns_tree_audit.py` 照第 0 條字面重算（關係行第一個逐字寫出的類別名，口徑照第 1 條，主線 tag 不算）。設計者的 `nodes2.json` `cats[0]` 不是照文中出現順序排的，而且把主線 tag 也算成類別。
- 7 則：L641 Paritok（B→C，「主線填 Context 管理」被當成類別）、L713 lemo-opuscar（D→F1）、L1634 四子代理 200 萬 token（B→A，「Context 管理」只出現在「歸入主線…」那句）、L1758 Simon Willison（D→C）、L2036 Agenta（C→F2）、L2148 MCP 隱藏 token（F1→C）、L2268 ccteams（D→A）。
- 讀者看得到的後果：A 的「機制細節」和概覽 Multi-agent 列都寫 ccteams，但 ccteams 那則住在 Skills 頁；母頁成本句、A「誰負責拆分」第二點都把 200 萬 token 那則指向 `community-memory#2026-08`。錨點有效，所以閘抓不到。
- 修法（已在 `R\alt\` 實跑：251 則逐字、全部閘綠、自查 OK）：
  1. `w18\split_patterns.py` L37–38 換成 `R\alt\split_patterns.py` 的 L37–53（`ROUTE_NAMES`／`ROUTE_EXTRA`／`first_cat()`；主線那段用 `re.sub(r'(主線填|歸入主線).*?(。|$)', '', t)` 刪掉）。
  2. `SUBS[139]`、`SUBS[2434]` 第一組的 `T('B')` 改 `T('A')`。
  3. `tpl\D.md` 開始日期 2026-07-11 改 2026-07-12（ccteams 搬走後 D 最早一則是 07-12）。
- 新數字：A 42／374、B 37／320、C 40／338、D 39／350、E 32／272、F1 38／340、F2 23／198；子頁正文 494／367／392／403／348／387／239。proposal §2 表、map「L2434–2435」列（「第一類別 Context」改「第一類別 Agent 規模化→A」）、draft 行數表同批改。
- draft A2 第 0 條第一句「（節點…第一個逐字寫出的類別名）」後補：

  > 比對口徑同第 1 條：只去空白、全形斜線轉半形；同義說法不算；「主線填…」「歸入主線…」到句末那一段是主線 tag，不算類別。

  泛化測試題（第 8 條，不是原事故）：關係行「補上「Context 管理」…，也呼應「Skills 設計」；主線填 Token / 成本優化」→ 應住 `community-memory`。

**🔴2 freshness 補丁的「上層歸因」放寬到所有子頁**
- 證據：`R\fresh_break.py` 案 1。在 `entities/claude-code` 下新增一個子頁，宣稱 10-12 有新聞、零歸因，母頁 10-12 有自己的歸因。原版判紅，補丁版 exit 0。這正是第 2 類要抓的「記者漏報歸因」，以後任何掛在活躍母頁下的新子頁都會被放過。
- 修法：把 `ancestor_att()` 改成只認「上層那筆歸因的 `item_url` 出現在本頁正文」。成品是 `R\check_wiki_freshness_v2.py`（新增 `load_attribution_urls()`，`ancestor_att()` 照網址比對）。
- 驗紅：測試換成 `R\test_wiki_freshness_hierarchy_v2.py`（設計者四案補上 item_url，再加案 5）。結果：原版 2 FAIL、設計者補丁 1 FAIL（案 5）、v2 5 OK。
- 拆頁實測：七子頁的網址命中最大日期，剛好等於各自的「最後新聞更新」（`R\urlcover.py`）。副本全閘 exit 0；現行全庫 10-09、10-15 都 exit 0。
- 設計者那份測試會在 v2 上 FAIL 1 案（沒有網址），所以 `src/tests/` 收的要是 v2 版。

**🔴3 子 agent 改不了三件閘檔：draft §H 第 2、4 步會被 hook 擋**
- 證據：`.claude/hooks/guard_roles.py` L48–53、L76–77。子 agent 不能寫 `scripts/check_*.py`、`data/*-allow.json`、`data/*baseline*.json`，也不能帶 `--rebuild`／`--allow-grow` 參數。我在 scratchpad 跑 `--rebuild` 就被它擋下。
- 修法：`check_wiki_freshness.py`、`data/reader-language-allow.json` 兩筆、cell 基線 rebuild 三件由主 session 做，排在實作者交件之後、`run_tests.py` 之前（見實作單 9–11 步）。測試檔 `src/tests/…` 不屬閘檔，可以交給實作者。

**🟡4 cell 基線 rebuild 會順帶收緊另外 5 頁 64 筆**
- 證據：設計者副本帳本 removed 130＝母頁 66＋claude-code 46、discussions 9、enterprise-tool-tracker 5、mythos 2、anthropic-business 2。這些是現況已經沒有命中的槽位，棘輪允許，不等於關閘。基線以「頁＋類型＋錨點＋長度」為鍵，之後的新超限照樣會紅。
- 修法：draft §E 核對句後補：

  > 印出的 removed 中七子頁與母頁以外的條目要逐筆是「現況已無命中」；commit 訊息寫明「順帶收緊 N 頁 M 筆」。

## 二、明天的維護者

**🔴5 記者如果也替母頁報歸因，母頁第 1 類隔天就紅、擋 web build**
- 證據：`R\fresh_break.py` 案 4。子頁 10-11 有歸因，母頁也報了一筆 10-11，母頁「最後新聞更新」照契約不動。補丁版（和 v2）判母頁漏更，exit 1。
- 新 daily 規則要求母頁 callout 每天跟著覆寫，記者很自然會把母頁也列進歸因。
- 修法：draft C 的 daily.md L13 新格末尾補：

  > 來源歸因的 page 一律填節點所在的子頁；母頁 callout 只是轉述，不報歸因（報了，`check_wiki_freshness.py` 第 1 類判母頁漏更）。

  測試題：同一則新聞改了子頁節點也改了母頁 callout，要報幾筆、page 填什麼？答：1 筆，填子頁。

**🟡6 母頁契約和路由都沒有機械看守 → 加一支唯讀自查，掛在週更第 4 步**
- 證據：`check_hierarchy.py` 只看 callout 日期與投影，沒有任何腳本數母頁行數或節點回流（我找過 `check_hierarchy`、`check_page_thickness`）。proposal §11 自己也承認路由沒人看。
- 修法：把 `R\patterns_tree_audit.py` 放進 `scripts/patterns_tree_audit.py`（不是 `check_*`，所以不算閘檔、不進 run_tests，判斷錯不擋 web build）。它直接讀 pages.md 第 0 條那張表，不另抄一份。
- 驗紅：設計者的分群跑出 7 則、exit 1；修後 OK；造一個母頁 `### 2026-07` 底下回流 122 行的節點 → 「302 行 > 300」＋「底下有節點」兩紅。
- draft B weekly 第 4 步開頭加：

  > 先跑 `python scripts/patterns_tree_audit.py`，exit 1 就照輸出把節點搬到它該住的子頁（逐字搬）或把回流母頁的節點下沉，再做下列重寫。

**🟡7 路由表「最後動態」欄沒有定義**
- daily 准記者每天動這欄，weekly 要重算，但兩處都沒說怎麼算。設計者填的值剛好等於各子頁「最後新聞更新」。
- 修法：draft A2 第 0 條表下加一條：

  > 母頁路由表「最後動態」＝該子頁標頭「最後新聞更新」，照抄不另算。

**🟡8 母頁路由表「收哪幾類」欄是 pages.md 第 0 條的第二份副本**
- 已經對不上：母頁欄少了已退出概覽表的 7 類，而 E 列寫著架構邊界合約，概覽該列卻連到 D。
- 修法：weekly 第 4 步「重算路由表最後動態欄」後補：

  > 「收哪幾類」欄＝pages.md 第 0 條該列裡、目前在 `## 模式概覽` 表上的類別，週更照抄。

## 三、冷讀者（拿 `R\out\` 從母頁路由表出發走四題）

| 題 | 走法 | 結果 |
|---|---|---|
| Q1 多 agent | index 新列 → A | 2 跳。A 的摘要、目前結論一頁答完（官方三條路＋隔離已定案＋協調缺口） |
| Q2 跨 session 記憶 | index L113 → 母頁路由表 B 列 → B | 3 跳。B 的摘要一頁給了兩層做法、「方向收斂、做法沒有」、裝哪個指 tools，有拿到 |
| Q3 skill 慣例／地雷 | index 新列 → D「慣例與地雷」 | 2 跳。四條「出處：〈節點標題〉」我逐一 grep 過，標題都在：3 則在 D、1 則在 E 且附連結 |
| Q4 9 月 hooks／plugin 新東西 | 母頁 → E／F1 的 `#2026-09` | 仍是半拿到。「哪個值得試」整庫還是沒有，提案也沒有承諾這件事，不算 finding |

- 路由表七列的「答什麼」都寫成讀者問題，H1 一律「社群做法：…」，slug 和既有頁不撞。`community-cost` 和 `enterprise-cost-management` C 摘要有分工句。這幾點沒有發現。

**🟡9 D「慣例」第二條違反 A12 自己定的入口**
- A12 規定只能引本樹節點或已查證的官方文件，但這條引的是 discussions。
- 修法：A12「只能引本樹既有節點或已查證的官方文件」改成：

  > 只能引本樹既有節點、已查證的官方文件，或 `topics/community-tech-discussions`「現在吵到哪」已列為不再爭的結論

  跟 draft 現在的頁面寫法一致，不必改頁面。

**🟡10 日報讀者版每天會把同一件事印兩次**
- 證據：`scripts/build_reader_digest.py` `collect()`（L181–215）會收每一頁當日日期的 callout，沒有看 parent。新 daily 規則要求子頁和母頁同一天都寫當日 callout（`check_hierarchy` L137 也逼母頁要有），兩者會同時進社群節。
- 修法（只用合成資料試過過濾邏輯：子頁同日在場時母頁被略過；claude-code 在 claude-mods 沒有當日 callout 時保留。沒有跑整支 digest，實作者要補一個單元測試）：在 `collect()` 的排序前加：

  ```python
  # 母頁 callout 是子頁當日新做法的總覽：子頁同日已收時，略過母頁那一項，免得讀者版同一件事印兩次
  got = {it["page"] for its in sections.values() for it in its}
  for sec, its in sections.items():
      sections[sec] = [it for it in its if not (
          (m := re.search(r'^children:\s*"(\[.*?\])"', it["raw"], re.M))
          and any(c in got for c in re.findall(r"'([^']+)'", m.group(1))))]
  ```

## 四、治理

- 轉知三筆：三筆 `--dry-run` 我都跑過，負責人驗證通過（開發實務／功能／功能），指令的類別寫法正確。外部錨點入邊我 grep 全庫，只有 proposal §7 列的 5 處，`daily/`、`weekly/` 沒有錨點連進本頁。registry `anchors` 沒有登記本頁節名，`sync_pairs[39]` 兩個 pattern 改後仍在。archive 的 `**上層：**` 不動。index 兩列新增後 `test_index_sync` 綠。以上無發現。

**🟡11 母頁兩個過渡標題的退場條件只寫在 `%%` 裡，沒有人會去執行**
- 修法：weekly 第 4 步末尾補一句：

  > 母頁過渡 h3「缺口追蹤：…」：`python scripts/wiki_graph.py explain topics/community-tech-patterns --section "缺口追蹤：文獻主張 × Claude Code 現況"` 入邊為 0 就刪；`### 2026-07` 等 2026-07 蒸餾時照 pages.md 第 8 條改成指 archive 的一行。

  `### 2026-07` 本月就到 3 個月門檻，不會變成死標題。

**🟡12 轉知 H-1 漏了同頁 L669**
- coding-workflow-guide L669「跨模型互審通過率方法論，[[topics/community-tech-patterns]] 2026-08-13 查證」：那段查證備註現在住 E。
- 修法：§G 第一筆 note 末尾加：

  > ；L669 的 2026-08-13 查證備註搬到 [[topics/community-guardrails]]「查證備註」，可一併改指

## 原則對照（REVIEW-PRINCIPLES）

- 第 1 條：重跑和逐則比對都是我自己做的。設計者自報的 caveat（L62 日期不符、路由沒看守）有追，後者就是 🔴1。
- 第 2 條：freshness 改壞驗紅五案；自查腳本驗紅兩種；錨點閘沿用設計者的驗紅。cell 基線的 rebuild 被 hook 擋，我沒能親跑，改讀設計者帳本。
- 第 3 條：規則檔改動沒有做新舊兩版記者同題取樣。替代做法是把第 0 條寫成腳本，對 251 則跑一次（🔴1），真正的驗收留給第 6 步的冷讀者複驗。
- 第 6 條：用領域不變量（每則節點恰在一頁、路由規則一致）驗出 🔴1。
- 第 8 條：🔴1、🔴5 都附了泛化測試題。
- 第 9 條：不適用（沒有視覺成品）。
- 第 13 條：每條附指令或檔案證據。
- 第 14 條：🟡6、🟡7、🟡8 都把副本收回單一的家。

## 照順序執行（實作單）

1. **設計者**：照 🔴1 改 `w18\split_patterns.py`（L37–38、SUBS[139]、SUBS[2434]）和 `tpl\D.md`；重跑 `split_patterns.py`、`verify_split.py`，再用 `gen` 重產 `out\generated\`。驗：節點 A42／B37／C40／D39／E32／F1 38／F2 23；`python R\patterns_tree_audit.py <副本 wiki> <pages_sample>` 印 OK。
2. **設計者**：同批改 proposal §2 表、map「L2434–2435」列、draft 行數表與 A2（🔴1 補句）、A12（🟡9）、B 第 4 步（🟡6、🟡8、🟡11）、C L13（🔴5）、新增「最後動態」定義（🟡7）、§E 核對句（🟡4）、§G 第一筆 note（🟡12）、§F 改指 `R\check_wiki_freshness_v2.py`。
3. **實作者**：把 `w18\out\` 八頁複製進 `wiki/topics/`（母頁覆蓋、七子頁新增）。驗：`git diff --stat wiki/topics/community-tech-patterns.md` 剩 205 行。
4. **實作者**：discussions 三處、LCW 五處、index 三處，逐字照 proposal §7 與 map 第三節。驗：`git diff` 只動這 11 處。
5. **實作者**：規則檔 A–D 照 draft「進規則檔」逐條改。驗：`PYTHONIOENCODING=utf-8 python scripts/check_rules.py` exit 0。
6. **實作者**：新增 `scripts/patterns_tree_audit.py`（從 `R\patterns_tree_audit.py` 照抄）。驗：`python scripts/patterns_tree_audit.py` 印 OK、exit 0。
7. **實作者**：新增 `src/tests/test_wiki_freshness_hierarchy.py`（從 `R\test_wiki_freshness_hierarchy_v2.py` 照抄，`SCRIPT` 預設值改回 `parents[2] / "scripts" / "check_wiki_freshness.py"`）。此時預期 2 FAIL，第 9 步後轉綠。
8. **實作者**：在 `scripts/build_reader_digest.py` 加 🟡10 的過濾段並補一案單元測試。驗：`python -m unittest src.tests.test_build_web_reader_digest`。交件。
9. **主 session**：`scripts/check_wiki_freshness.py` 換成 v2 的 `load_attribution_urls()`＋`ancestor_att()`＋第 1、2 類區塊，docstring 照 draft §F 補句。驗：`python -m unittest src.tests.test_wiki_freshness_hierarchy` 5 OK。
10. **主 session**：`data/reader-language-allow.json` 兩筆 `page` 改子頁（draft §E）。驗：`python scripts/check_reader_language.py` 無新增。
11. **主 session**：先跑 `python scripts/gen_wiki_frontmatter.py`，再跑 `python scripts/check_cell_limits.py --rebuild --allow-grow --reason "第 18 波 patterns 拆頁：母頁 66 筆存量隨節點原文搬到 7 子頁（錨點與長度不變）"`。驗：新增恰 66、全在七子頁；removed 裡別頁的條目逐筆是「現況已無命中」。
12. **主 session**：依序跑閘 `python scripts/check_hierarchy.py && python scripts/check_pending_markers.py && python scripts/check_wiki_freshness.py && python scripts/check_cell_limits.py && python scripts/check_rules.py && python scripts/build_web.py`（尾行錨點 WARN 與改前同數）`&& python scripts/run_tests.py`，結束碼為 0 才往下。
13. **主 session**：只 `git add` 本波的八頁、index、discussions、LCW、規則檔、`scripts/check_wiki_freshness.py`、`scripts/patterns_tree_audit.py`、`scripts/build_reader_digest.py`、兩個測試檔、`data/` 三檔；commit 後跑 `python scripts/devpractice_diff.py mark`。
14. **主 session**：§G 三筆轉知（先 `--dry-run` 再實跑）、`wiki/log.md` Query 條目帶單號、ledger 定稿列；`git fetch` 確認沒有新 commit，再同一 commit push。之後派新冷讀者用原四題複驗。

## 實作複核（2026-10-09，commit 7fdb05af／18622713／a3e859b7）

重跑結果（原樣）：`patterns_tree_audit.py` → `OK: patterns 樹母頁契約與節點落點無異常`，exit 0；`check_wiki_freshness.py` → `OK: wiki 新鮮度檢查通過（121 頁；衍生頁 11 頁已宣告觸發邊）`，exit 0；`cd src && python -m unittest tests.test_wiki_freshness_hierarchy tests.test_build_web_reader_digest tests.test_wiki_search` → `Ran 81 tests … OK`；`check_cell_limits.py` → `OK: 字元上限機械閘 — 無新增超限`。
抽驗：子頁三則改派節點（ccteams→multi-agent、Agenta→interfaces、Paritok→cost）跟拆前原文逐字相同（7／7／8 行）；母頁路由表 multi-agent、skills、interfaces 三列跟 draft 逐字相同；兩處「200 萬 token」都已改指 `community-multi-agent#2026-08`；D 的開始日期是 2026-07-12。

| 步 | 判定 | 說明 |
|---|---|---|
| 1–2 設計者改分群與三件文件 | 照做 | 落點 audit OK；A2 比對口徑（pages.md L36）、最後動態定義＋收哪幾類（L38）、A12 討論頁入口、§G 那則 L669 都在 |
| 3–4 八頁＋鄰居 11 處 | 照做 | 抽驗見上；錨點 WARN 0→0（commit 訊息自報，web a3e859b7 已上站） |
| 5 規則檔＋check_rules | 偏離，合理 | 「CLAUDE.md 管理」是 wiki 類別名，audit 要逐字比對，不能改寫；在 `line_allowlist` 加一筆、附理由，範圍只限 pages.md，比改類別名對 |
| 6 audit 腳本 | 照做 | weekly.md L59 第 4 步先跑它，回報格式有 `patterns_tree_audit：OK／❌` |
| 7 freshness 測試 | 照做 | 5 案在 81 案裡全綠 |
| 8 digest 去重 | 偏離，合理 | 實作版只在母頁 callout 內連到同日也有 callout 的子頁時才略過母頁，比我的 children 版窄：母頁自己的新聞照收。兩案測試；驗證指令改用 `cd src` 是對的 |
| 9 主 session 換 v2＋docstring | 照做 | |
| 10 allowlist 兩筆 | 照做 | 閘綠 |
| 11 cell rebuild | 照做 | 新增 66 全在七子頁。各頁分布和我評審時的版本不同（memory 13／multi-agent 14），是改派 7 則的結果，總數對；移除 129＋收緊 1 是現況已無命中的槽位，棘輪允許 |
| 12 閘＋run_tests | 照做＋一處測試改寫，不算放水 | 見下 |
| 13 git add 範圍 | 偏離，無害 | 142 個檔，其中約 100 頁只有 gen 漂移。抽 6 頁看，diff 都只有 `days_since_news`／`pending_*`／`inbound_links`／`signal`，沒有正文；draft §H 原本寫「其餘頁 frontmatter 漂移不收」。沒有混進他 session 的正文改動，不要求回退 |
| 14 轉知＋log＋ledger | 照做 | H-fc0960 開發實務／coding-workflow-guide、H-9d1672 功能／official-community-gap、H-817203 功能／claude-skills，類別與頁都對；H-fc0960 note 含 L669 |

**test_wiki_search 改寫，不算放水，但註解要修：**
- 舊斷言「第一筆是字面命中」綁的是語料，拆頁讓 archive 頁的改寫命中分數領先，屬於正常變動。新斷言保留「有字面命中」，另外加「圖擴散頁之前全是 found 種子」，比舊的更嚴。
- 註解寫「search() 的排序契約：found 的種子 → 圖擴散」不準。`scripts/wiki_search.py` L296 是把種子和擴散頁合在一起按 `rel` 排序；擴散頁的 `rel`＝`EXPAND_WEIGHT×Σ(seed rel/√deg)`，可能高過弱種子。所以這是現況剛好成立，不是程式保證的契約，日後可能 flaky。
- 修法：註解改成「現況斷言：擴散權重下種子目前都排在擴散頁前；L296 是合併排序，此條紅時先查 EXPAND_WEIGHT 是否變了，再決定改斷言或改權重」。

**放行**：條件都已滿足；上面那句註解是下一批順手修的小事，不擋。冷讀者用原四題複驗照流程第 6 步另派。
