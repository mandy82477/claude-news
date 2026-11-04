# 第 22 波評審：topics/market-signals 拆成母頁＋四子頁（2026-11-02）

> 審的對象：`market-signals-2026-11-02-{proposal,proposal-map,draft}.md`；上游健檢卡、冷讀者、verified；ledger 裁決紀錄最上面四條（L124 N1–N5、L125 使用者授權、L126 第 22 波七點、L127 第 21 波）。
> 設計者產物在 `<scratchpad>/w22/design/`（下稱 `D/`），我的重跑在 `<scratchpad>/w22/review/`（下稱 `R/`）；`<scratchpad>`＝`/tmp/claude-0/-home-user-claude-news/d15bcaea-1307-5c78-90dd-54d17b9ee243/scratchpad`。我沒改 `D/`、wiki、規則檔、腳本、基線，也沒跑 git 寫入指令。
> 行號：「原 Lnnn」＝原檔 `wiki/topics/market-signals.md`（blob `e12d896`，1,699 行）；「母 Lnnn」＝`D/out/wiki/topics/market-signals.md`。

## 結論

- 🔴 3 條、🟡 5 條。切法、一則三件同頁、錨點殼、子樹解析都成立，數字全部重算對得上。
- 🔴1：`scripts.diff` 改到了 `scripts/check_wiki_freshness.py`。它在 H6 的閘檔清單裡，雲端不准改。
- 🔴2：懸置命中改派給投資分析記者之後，wiki-ingest 的 4c 沒有把命中交給他。69 筆標記會沒人加 `訊`。
- 🔴3：N2 補登的 4 筆裡，只有 Citywire 過得了 ledger L124 自己定的條件。
- 頁面設計後沒被動過：HEAD `0c0aee8` 的 blob 和 `7dbc92e` 的相同，都是 `e12d896`，工作樹也是乾淨的。`7dbc92e..HEAD` 這段只有兩個 page-audit commit；11-01 的 ingest 已經跑完（log L8446，market 記者回報本日無訊號）。
- **放行條件**：照文末清單第 2 步吃下 🔴1–3，重跑後驗收輸出要和清單寫的一致。🟡 同一步一起吃，成本很低。

## 自己重算的數字

| 項目 | 主 session／設計者 | 我重算 | 證據 |
|---|---|---|---|
| 88 則歸群 | 25／24／14／25 | **屬實**。四子頁的 `^### 💰` 是 25／24／14／25，母頁 0 | `D/out` 的 regex 計數 |
| 正文行 | 116／494／483／304／513 | **屬實** | `check_page_thickness.body_lines` 跑在 `D/out` |
| 懸置 | 69→69（19／21／12／17／母 0） | **屬實**。我跑 `python -I D/verify.py <repo>` 得到 `照搬 1084 行；69→69`、`結論：OK`；原檔 `（標 20` 共 69 筆 | — |
| 結算列與合計 | ✅13／❌1／～36／—14／⏳26 | **屬實**。子頁逐列末欄：A 2/0/14/1/8、B 6/0/10/3/7、C1 1/1/1/5/6、C2 4/0/11/5/5，和母 L124–128 一致 | — |
| `--rebuild-count` 預期 | 212，69 筆換 slug | **count 212、＋69／－69**，增減兩邊都是 market-signals 子樹，其他頁 0 | 在 `R/tmp1`（`D/tmp_after` 的副本）實跑，輸出在 `R/rebuild_sim.txt` |
| W41–W44 產量 | 12／13／9／16 | **屬實**。用原檔判讀日的 ISO 週去數 | — |
| 「現在怎麼判」裡的數字 | — | **屬實**。C1「14 則裡 10 則單一標題」；C2「16 條線裡 14 條只有一則」；B「已結算 19 列裡 10 列仍懸」 | 逐則數一眼欄 |
| N1 L1543 | 和 L1567–1568 同一事實 | **屬實**。L1543 多出的「價格區間與上市日未定」，L1681 改寫後也有了；L1543 不是任何懸置標記的家 | — |
| N2 補登 4 筆 | 4 筆都合格 | **1 筆合格**（🔴3） | 下表 |

**去向表抽驗**（map 對 `D/out` 逐字核，4 節）：
- 10-29 的四則：Citywire、Copilot Fusion → C2；Bloomberg 德州債券、BigGo Zero-Rust → C1。和 C1、C2「現在怎麼判」的字面一致。
- 里程碑 L1536（承銷商、定價區間）→ A。`D/verify_red.txt` 的驗紅就是拿這一筆做的。
- 標的表 L54–84 → 母頁，只砍了 L76 那行空行。
- 母 L106–109 是 h4 殼，原 L 的 09-29 Reuters 那則本體在 A。
四節都和 map 相符。

## 一、機器

**🔴1 `scripts.diff` 改了雲端 H6 擋的閘檔**
- `.claude/hooks/guard_roles.py` L52–56 的 `GATE_FILES` 含 `scripts/check_*.py`；L80–81 規定雲端 session 也受限（本 session 的 `CLAUDE_CODE_REMOTE=true`）。
- `D/scripts.diff` L59–69 改的是 `scripts/check_wiki_freshness.py` L78。ledger L126 (4) 只確認了 `build_web.py` 不在清單裡，漏了這一支。
- 用 Edit 改會直接被擋。更糟的是 `git apply` 不在 hook 的 `_shell_targets` 解析範圍內，**擋不到**，等於繞過閘門。
- 這一處只是 `DERIVED_PAGES` 的說明字串，閘的行為和測試都不依賴它，所以不改也沒有功能損失。
- 修法：從 `D/scripts.diff` 刪掉 L59–69 這個 hunk，套用時一律 `git apply --exclude=scripts/check_wiki_freshness.py`；proposal §5 L58 整行刪除，可行性前提的「腳本 6 支」改成「腳本 5 支」；ledger 定稿列補一句 `check_wiki_freshness.py L78 說明字串（market-signals→四子頁）屬閘檔，留使用者本機改`。

**scripts.diff 其餘部分逐行核過，沒有會改變實作單的問題**：
- `market_signal_pages()` 用 `META_RE["parent"]`（build_web L137）讀前 60 行，子頁的上層欄在第 31 行左右。
- h4 殼：`^###\s+` 碰到 `####` 時，第 4 個 `#` 不是空白，所以比對不中。
- 同一天的判讀取清單中先出現的那頁。
- 日後如果有 `-archive` 子頁，它的上層也會指向母頁，但裡面的判讀日期都比較舊，不影響結果。
- `onclick` 裡的 `esc()` 包的是 stem，不含引號，安全。
- 驗紅：14 案中 13 案紅（`D/redtest.txt`）。h4 與免責兩案在舊碼上本來就綠，屬護欄性質，可以接受。

**🟡1 驗收腳本的原檔路徑**（第 21 波 🟡2 重演）
`D/verify.py` L18 從 `<ROOT>/wiki/topics/market-signals.md` 讀原檔。五頁複製進 repo 之後，它讀到的會是新母頁。
修法：複製後的驗收改跑 `python -I D/verify.py D/tmp_before <repo>/wiki/topics`。`D/tmp_before` 這份原檔我核過，blob 是 `e12d896`，和原檔相同。

## 二、明天的維護者

**🔴2 投資分析記者收不到懸置命中與轉知**（主 session 要我查的第 4 點）
- 改完以後，`PAGE_TO_REPORTER` 會把五頁的命中派給 `wiki-reporter-market`，scan 輸出會多一組 `[投資分析]`。`commercial/daily.md` 也改寫成「你不會收到」。
- 但 wiki-ingest SKILL L38 只寫了「『開發實務』組隨 4b 附給開發實務記者」；4c（L116）只貼六類包檔；`dispatch.md` 的 4c 首段也只有一行。
- 結果：69 筆標記的 `訊` 沒有人會加。另外 scan 的 `REPORTER_ORDER`（L87）不含投資分析，所以「無命中記者」那一行不會列出他，主 session 看不出這組是空的還是漏了。
- 轉知（H-b16ef0）過去是主 session 臨場塞進 4c 的（log L8313）。dispatch.md L43 又禁止臨場加料，這個做法本身就不合規。
- 修法：在 `D/rules_patch.py` 的 `EDITS` 末尾加兩條（old 字串在現行檔各出現 1 次，已核過）：
```python
    (".claude/skills/wiki-ingest/SKILL.md", "「開發實務」組隨 4b 附給開發實務記者。",
     "「開發實務」組隨 4b 附給開發實務記者；「投資分析」組（投資訊號母頁與四子頁的命中）隨 4c 附給投資分析記者，scan 輸出沒有這一組就寫「無」（「無命中記者」一行不列投資分析，不能拿它判斷）。"),
    (".claude/skills/wiki-ingest/SKILL.md", "（與六記者同一份步驟 2 產物，不另篩）。",
     "（與六記者同一份步驟 2 產物，不另篩），最後附「待查證命中」（步驟 1 scan 輸出的 `[投資分析]` 組）與「轉知待接手」（`pending_handoffs.py list` 的「→ 投資分析 記者」組）兩區塊，無則各寫「無」。"),
```

**🟡2 記者寫錯頁的兩個缺口**（第 4 點）
- **找線要靠猜**：「同一條線寫進已有判讀的那頁」，但線散在四頁，規則沒給查法。
- **`### 未歸類` 的結算列和里程碑沒有家**：daily (c)(d) 寫的是「同一子頁」，可是母頁沒有結算表，也沒有里程碑節。
- **母頁最後新聞更新**：(f) 只在覆寫標的表時才動。判讀寫進未歸類那天，母頁就有了自己的新聞；freshness 第 1 類（`own and last_news < own`）會紅。
- 修法：在 `D/rules_patch.py` 裡做三處取代。
  - `PAGES_NEW_BODY` 的路由段，整句換成：
`照**線**歸頁：同一條線的後續判讀寫進該線已有判讀的那頁（查法：`grep -l "線：<線名>" wiki/topics/market-signals-*.md`，命中哪頁寫哪頁）；開新線才照題材判。判不出的新線寫進母頁 `## 近期判讀` 下的 `### 未歸類`（照常用 `### 💰` 格式；該則的 ⏳ 結算列與里程碑標記寫在該則正下方，一則三件同處），主編每週 5h 連同三件分派進子頁——它不是預設子頁。`
  - daily (f) 的 `當天覆寫了標的表才連「最後新聞更新」一起更新`，改成 `當天覆寫了標的表或寫進母頁 `### 未歸類` 才連「最後新聞更新」一起更新`。
  - weekly 第 6 步的 `更新動到的頁的「最後更新」` 前面插入 `母頁 `### 未歸類` 有判讀時連同正下方的結算列與標記搬進對應子頁；`。

**🟡3 h4 殼刪了要誰收尾**
proposal §6 handoff 2 寫「落地後母頁刪殼」，但沒寫由誰刪。母頁是投資分析記者的頁，人物記者動不了。
修法：handoff 2 的事項末尾補一句 `人物記者改完 L49 回報後，主編結案時刪母頁 `#### 💰 Reuters 獨家…` 殼三行（母 L106–109），跑 build_web 確認錨點 WARN 不增`。

## 三、冷讀者

**🟡4 母頁標的表的欄名「本頁判讀」已經不成立**
母 L62 的表頭是「本頁判讀」，可是這一頁已經沒有判讀了。讀者要自己去路由表猜「08-26 Claudeforce」在哪個子頁。
修法：
- `D/newtext.py` 的 `M_SUBS` 加一筆 `(58, "| 本頁判讀 |", "| 相關判讀（所在子頁見「近期判讀」表） |")`。改過的行，`split.py` L80 會標「（改）」，verify 會跳過。
- `rules_patch.py` 的 `PAGES_NEW_BODY` 把 `標的｜跟 Anthropic 的關係｜本頁判讀｜現在方向｜下一個催化劑` 裡的「本頁判讀」改成「相關判讀」。
- 這個字串不是任何腳本的契約，我 grep 過 `scripts/`、`src/`、`.claude/`，只有 pages.md 一處。

**🟡5 冷讀者 Q3「融資有什麼風險訊號」在 C1 還少評等**
KBRA 非投資級、Blackstone 預期 BB 級住在 A，C1 的「現在怎麼判」沒有指過去。C1 已經用滿 4 條，所以不加新條，接在第 2 條末尾。
修法：`D/newtext.py` 的 `NOW["C1"]` 第 2 條，`是第一個實際受挫的訊號。` 改成 `是第一個實際受挫的訊號；評等面（KBRA 非投資級最高一檔、Blackstone 預期上市後 BB 級）在 [[topics/market-signals-ipo]]。`

**子故事三題**：
- A：入邊有 anthropic-ipo 三處，加上 yann-lecun 錨點。
- C1：tom-brown。
- C2：suleyman、business L711。
- B：獨立入邊只有 handoff 4 在 market-lessons 消息線表上給的那幾條線。這一項是推論：法律線在 market-lessons 有列，它們改指 B 之後才算成立。
- 四頁的第 1、2 題都過，各有使命問句、callout 和「現在怎麼判」。不改實作單。

**母頁契約**（第 5 點）：
- 116 行，不到 300。
- 留下的是索引加重要結論：摘要「現在」段、標的表、一子頁一列的路由表（答什麼＋最新一則）、合計表。事件流全部下沉。
- 每日可寫的部分（callout、路由表、標的表、未歸類）都登記在 page-lifecycle L52 的例外裡（patch 已加標的表）。
- 週更的結論層登記在 weekly 第 6 步。
- 讀者版不會重複：`build_reader_digest.py` L217–227 會略過連到同日子頁的母頁 callout，而母 L41、L44 都連到了子頁。
- 這部分沒有發現問題。

## 四、治理

**🔴3 N2 只准補 1 筆**
ledger L124 寫明「實作前逐筆核網址確在 10-29 日報與子頁內，不符者不補」。逐筆核對結果：

| 筆 | `news/2026-10-29.md` | 子頁內 | 判 |
|---|---|---|---|
| Citywire $4,800 | 1 次 | C2 callout L42 | **補** |
| The New Stack Copilot Fusion | 1 次 | 無（判讀用 wikilink，不放網址） | 不補 |
| BigGo Zero-Rust | 1 次 | 無 | 不補 |
| Bloomberg 德州債券 | 1 次 | 無 | 不補 |

- 後 3 筆確實是記者漏報：log L8283 記了這四則判讀，標題也和日報條目逐字相符。但它們不符合補登條件，照裁決不補。
- 只補 Citywire 一筆後，我在 `R/tmp1` 實跑 freshness，結果是 `OK: wiki 新鮮度檢查通過（138 頁；衍生頁 11 頁已宣告觸發邊）`、exit 0。C2 靠 Citywire 撐住，A／B／C1 照舊靠各自 callout 裡的網址。
- 修法：
  - `D/attribution_1029.jsonl` 只留第 1 行（Citywire）。
  - proposal §7 freshness 列改成「含 N2 補登 1 筆（Citywire）」。
  - §8 N2 改成 `補登 1 筆（Citywire，網址在 C2 callout）；The New Stack、BigGo、Bloomberg 三筆網址不在子頁，依 L124 不補，漏報事實見 log L8283`。
  - ledger 定稿列照抄這句。

**N3–N5**：
- N3：本波對 cell 和 reader 兩閘的貢獻都是 0。我重跑 `moves.py` 得到子樹改前 0、改後 0；`data/cell-limit-baseline.json` 裡 market-signals 也是 0 筆。紅的只會是第 21 波那一組。
- N4、N5：沒有新意見。

## 照順序執行（實作單）

| 步 | 誰 | 做什麼 | 驗 |
|---|---|---|---|
| 1 | 主 session | `git log --oneline 7dbc92e..HEAD -- wiki/topics/market-signals.md .claude/reporter-rules/market .claude/agents/wiki-reporter-market.md .claude/skills/wiki-ingest scripts web_reader/assets src/tests`；`git rev-parse HEAD:wiki/topics/market-signals.md` | log 只有 page-audit commit（`0c0aee8`、`73a7794`）；blob 是 `e12d896…`。如果 blob 變了（下一次 ingest 先跑了），**停下**：`split.py` 防呆會紅，交設計者照新 hunk 擴充 `split.py` 的行號表後，從第 2 步重來 |
| 2 | 設計者（第二輪） | 照 🔴1–3、🟡2–5 改 `D/scripts.diff`（刪 L59–69）、`D/rules_patch.py`、`D/newtext.py`、`D/attribution_1029.jsonl`；重跑 `python -I D/split.py <repo>`、`python -I D/make_map.py <repo>`、`python -I D/make_draft.py <draft 檔>`、`bash D/gates.sh D/tmp_after after`（臨時副本要先重套 rules_patch 和 out） | `split.py` 印 `ok {…}`；`python -I D/verify.py <repo>` 印 `69→69`、`結論：OK`；`grep -c check_wiki_freshness D/scripts.diff` 是 0；`wc -l D/attribution_1029.jsonl` 是 1；gates 的 check_rules 是 `✅`；freshness `OK…138 頁` |
| 3 | 設計者（第二輪） | 文件：proposal §5 刪 L58、「腳本 6 支」改「5 支」、§7 freshness 列、§8 N2（照 🔴3 逐字）；draft 由 make_draft 重產 | `grep -n "check_wiki_freshness\|補登 4 筆\|腳本 6 支" docs/page-audits/market-signals-2026-11-02-{proposal,draft}.md` 0 命中 |
| 4 | 主 session | `D/out/wiki/topics/` 五檔複製進 `wiki/topics/`；`git apply --exclude=scripts/check_wiki_freshness.py D/scripts.diff`；`python -I D/rules_patch.py <repo>`；把 `D/attribution_1029.jsonl` 的 1 行 append 進 `data/source_attribution.jsonl` | `python -I D/verify.py D/tmp_before <repo>/wiki/topics` 印 `結論：OK`；`git diff --name-only` 不含 `scripts/check_`、`data/*baseline*`、`data/*-allow.json` |
| 5 | 主 session | `python scripts/gen_wiki_frontmatter.py`（只跑不改） | `check_hierarchy` 印 `✅ 通過（32 個母頁）`；index L138 投影出四子頁 |
| 6 | 主 session | `python scripts/check_pending_markers.py --rebuild-count --reason "第 22 波 market-signals 拆頁：69 筆換 slug（母頁→四子頁 19／21／12／17），去 slug 比對無增減"` | 印 `基線已重建：212 筆`，＋69／－69 全在 market-signals 子樹 |
| 7 | 主 session | handoff 1–4，第 2 筆照 🟡3 補句：先 `pending_handoffs.py open --dry-run`，再 `open`；`wiki/log.md` 寫 Query 條目，帶單號和「N2 補 1 筆、3 筆不補」 | `python scripts/check_log_handoffs.py` 綠 |
| 8 | 主 session | 閘一次跑完：hierarchy、pending、freshness、rules、build_web；`python -m unittest` 跑 `src/tests/test_market_signals.py`、`test_reader_tags.py`、`test_pending_handoffs.py`、`test_check_pending_markers.py`；`python scripts/run_tests.py` | freshness `OK…138 頁`；rules `✅`；build_web 尾行 `斷鏈 WARN 23／錨點 WARN 0`；四檔測試全 OK；run_tests 只准第 21 波那一組紅（1 FAIL＋cell 107、reader 2），**多出的任何紅一律停下** |
| 9 | 主 session | 只 `git add` 指名的檔：wiki 五頁＋gen 改到的 index／frontmatter、規則檔 9 份＋wiki-ingest SKILL、腳本 5 支、測試 2 支、`data/source_attribution.jsonl`、`data/pending-marker-count.json`、`data/pending-handoffs.jsonl`、`wiki/log.md`、`docs/page-audits/{ledger.md,market-signals-2026-11-02-*.md}`；commit 進 `claude/stoic-edison-ewvmcx` 並 push | `git show --stat HEAD` 不含 `scripts/check_wiki_freshness.py`；`git status` 殘留只准是 `web_reader/` 產物 |
| 10 | 主 session | ledger 定稿列：正文 116／494／483／304／513、懸置 69→69、rebuild ＋69／－69、N2 補 1 筆、freshness 說明字串留本機 | — |
