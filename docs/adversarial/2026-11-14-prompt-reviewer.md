# 對抗輪 C：規則檔 prompt reviewer 報告（2026-11-14）

> `/wiki-lint` 6j 月度對抗輪的第三位 agent（Opus，只讀不寫）。審查範圍：`git log --since=30.days --name-only -- .claude/` 的 20 個檔，深審 10 個。
> **雲端不改 `.claude/`**，故本檔保存 reviewer 的**修訂文字原文**，供下次本機 session 的主編逐項判定採不採。
> 摘要與主編判定見 `wiki/log.md` 2026-11-14 Lint 紀錄的「本機承接」行與下方補記。
> reviewer 自述：所有機械契約均以 grep／實跑驗證；`check_rules.py` 與 `patterns_tree_audit.py` 現狀全綠，**下列 20 條沒有一條是現行檢查器抓得到的**。

## 深審檔與選擇理由

| 深審檔 | 為什麼選它 |
|---|---|
| `.claude/reporter-rules/page-lifecycle.md` | 30 天內被 5 個拆頁波次改過，churn 最高；六記者＋主編共用的拆頁／蒸餾／併回正典 |
| `.claude/reporter-rules/README.md` | reporter-rules 的路由表與索引，錯了所有人找錯檔 |
| `features/daily.md` ＋ `features/pages.md` | 最大（93＋307 行）、機械契約最密、11-08 剛動過 |
| `.claude/agents/wiki-reporter-features.md` | 11-08 剛改，且內嵌 `features/pages.md` 的契約**副本** |
| `commercial/daily.md` ＋ `commercial/pages.md` | 第 23／24 波拆頁主受害者，249 行 |
| `market/{daily,pages,weekly}.md` ＋ `agents/wiki-reporter-market.md` | 第 22 波拆四子頁；daily.md 自帶「機械契約字串」表可驗完整性 |
| `.claude/commands/weekly.md` | 10-25 改版；三段 skill 的收尾單一家 |
| `.claude/commands/pipeline-change-check.md` | 同批改版；直接消費 `web_reader/data/digest/*.json` 欄位 |
| `community/pages.md` | 第 0 條路由表被 `patterns_tree_audit.py` 逐字 grep ＋ `assert len(ROUTE) == 7` |

略看：`devpractice/{daily,pages}.md`、`models/pages.md`、`commercial/weekly.md`、`community/weekly.md`、`agents/wiki-reporter-commercial.md`、`safety-policy/pages.md`。

---

## 🔴 阻擋級

### 1. `/weekly` 的兩個子 skill 仍用退役的 web build gate（10-03 對抗輪只修了總指揮）

**檔**：`.claude/commands/weekly.md:24`（授權單獨執行）→ `.claude/skills/weekly-report/SKILL.md:70`、`.claude/skills/wiki-weekly-review/SKILL.md:71`

**證據**：registry 兩組 gate 看守（`all_contain: scripts.gate_web_build\.py`、`max_count: Tests FAILED - (web )?build skipped`）的 `files` 只有 `web-publish/SKILL.md`、`wiki-lint/SKILL.md`、`commands/weekly.md`。10-03 那輪補了 `weekly.md`、放寬 pattern 成 `(web )?`，**同樣的缺陷留在兩個子 skill 裡沒動**。`weekly.md:24` 明文允許單獨執行，該路徑會用 `run_tests.py` 當閘（不吃 `known-test-gaps` 登記缺口）、跳過修復迴圈、回報抄退役措辭。`check_rules.py` 現在全綠，抓不到。

**修訂文字（1／2）** — `.claude/skills/weekly-report/SKILL.md:70` 整行取代：

```markdown
- **其餘照 `.claude/skills/web-publish/SKILL.md` 的 `Step 4`／`Step 5` 做，本檔不另寫一套**：build 前的閘是 `PYTHON REPO_ROOT\scripts\gate_web_build.py`（**不另外自己跑 `run_tests.py` 再判斷**），擋下時走該檔「gate 擋下時的修復迴圈」（至多 2 輪），放行後的 `build_web.py` → add `web_reader/` → web commit、**單一 push** 與 push 失敗重試（`pull --rebase` 上限 2 次）全部以該檔為準；回報的 gate 欄抄 `gate_web_build.py` 輸出的最後一行摘要，不自己改寫措辭
```

同檔 `:90` 改為：

```markdown
- 驗證閘：`scripts/check_weekly_ledger.py`（掛在 `scripts/run_tests.py` 內）綠了才算完；單獨執行時 build 前的閘是 `gate_web_build.py`，擋下則跳過 build 與 web commit，仍推送已完成的 weekly commit。
```

**修訂文字（2／2）** — `.claude/skills/wiki-weekly-review/SKILL.md:71` 與 `:82`：

```markdown
2. `PYTHON REPO_ROOT\scripts\gate_web_build.py`（**不另外自己跑 `run_tests.py` 再判斷**；擋下時走 `.claude/skills/web-publish/SKILL.md` Step 4「gate 擋下時的修復迴圈」，至多 2 輪仍擋下則跳過 build 與 web commit，仍執行步驟 4 推送 wiki commit）
```

```markdown
- 單獨執行時步驟 6 的 `gate_web_build.py` 放行才 build web；由 `/weekly` 帶起時步驟 6 跳過，收尾由總指揮負責。
```

**registry 同批修訂**（`.claude/review-registry.json`，兩個 gate sync_pair 的 `files` 各補兩個檔）：

```json
      "files": [
        ".claude/skills/web-publish/SKILL.md",
        ".claude/skills/wiki-lint/SKILL.md",
        ".claude/commands/weekly.md",
        ".claude/skills/weekly-report/SKILL.md",
        ".claude/skills/wiki-weekly-review/SKILL.md"
      ],
```

`_note` 末尾補：`2026-11-14 加入兩個子 skill：10-03 只修了總指揮，子 skill 單獨執行（weekly.md 使用方式明文允許）仍走舊閘與舊措辭。`

### 2. 回報契約欄數：規格端寫「八欄」，消費端 `CORE_FIELDS` 是 9 欄

**檔**：`reporter-rules/README.md:26`、`features/daily.md:93`、`commercial/daily.md:43`、`community/daily.md:89`、`models/daily.md:59`、`safety-policy/daily.md:37`

**證據**：`scripts/collect_reporter_reports.py:54` 的 `CORE_FIELDS` 有 9 個（更新頁面、feature-radar 新增、index.md 狀態變更、新增頁面、同步自查、待查證命中處置、轉知處置、分類回退、來源歸因）；`review-registry.json:290` 已改「九欄」，六份規則檔仍寫「八欄」。記者照八欄數，最可能漏掉 `來源歸因`——該欄一漏，`data/source_attribution.jsonl` 當天少一批歸因，`check_wiki_freshness.py` 第 1 類與 6g 歸因覆蓋率雙雙失真。

**修訂文字** — 五份 `daily.md` 的「八欄」改「九欄」；`README.md:26` 改為：

```markdown
| `shared.md` | 邊界限制、書寫紀律、回報契約（九欄骨架＋呈現品質審查列＋機械自查列的單一家；欄名與順序由 `scripts/collect_reporter_reports.py` 的 `CORE_FIELDS` 消費，改欄必須同批改該常數與 `.claude/review-registry.json`） |
```

`shared.md`「回報格式（回報契約）」code fence 正下方加一行：

```markdown
**欄數以上面的骨架為準，不以別處寫的數字為準**：九個具名欄（更新頁面→來源歸因）＋`呈現品質審查` 列＋`機械自查` 列。欄名被 `scripts/collect_reporter_reports.py` 的 `CORE_FIELDS` 逐字消費，少一欄該欄當天靜默歸零。
```

### 3. 「對稱規則：併回」沒排除封存頁與轉址殼，照字面執行會把整個證據層併掉；且無偵測端

**檔**：`page-lifecycle.md:60`（條文：「子頁 < 80 行且 60 天無新聞更新 → lint 當輪併回直接上層」）

**證據**：以 `check_page_thickness.body_lines` 同口徑量，全庫符合判準的 **17 頁全部是 `-archive` 封存頁**（ai-talent-flow-archive 32 行／138 天、cowork-archive 19／187、google-investment-archive 29／197、john-jumper-archive 20／141 等），外加 `community-tech-timeline`（10 行／176 天，已是 redirect 殼）。同檔「時段蒸餾與封存」要求 archive 一字不刪、末行固定 `原始條目見 [[<archive>#YYYY-MM]]`，`build_web.py` 的 `check_wikilink_anchors()` 會驗，`check_hierarchy.py:12-13、125-129` 要求 archive 必掛父且狀態為 `resolved（封存頁）`。併回它們＝刪掉蒸餾產物的證據層＋斷全庫 archive 錨點＋打紅 check_hierarchy。
**另一半是空頭承諾**：`grep -rn "併回" .claude/skills/wiki-lint*/` 只有「拆錯一週內併回」；沒有任何腳本算「子頁 < 80 行」。

**修訂文字** — `page-lifecycle.md` 的「### 對稱規則：併回」整節取代：

```markdown
### 對稱規則：併回

**對象只有真子頁**：slug 不含 `-archive`、`page_role` 不是 `redirect`、狀態不是 `resolved（封存頁）`。封存頁是證據層（原文一字不刪、被全庫 `原始條目見 [[…-archive#YYYY-MM]]` 錨點指著），轉址殼本來就只剩標頭——兩者永不併回，否則 `scripts/check_hierarchy.py` 第 4 條與 `build_web.py` 的 `check_wikilink_anchors()` 會紅，蒸餾產物的證據層會整批消失。

**判準**：真子頁正文（扣 frontmatter 與 `%%` 備忘）< 80 行，且「最後新聞更新」距今 > 60 天 → lint 當輪併回直接上層，log 記一行。

**偵測端**：`/wiki-lint` 5o 跑 `python scripts/check_page_thickness.py` 的同一趟，一併跑 `python scripts/check_page_thickness.py --thin` 列出候選（欄位：頁、行數、最後新聞更新天數）；輸出為空就回報「無併回候選」。**腳本還沒有 `--thin` 之前，本節判準不生效**——規則與偵測端同批上線，不留手算版本。

**併回必留 redirect 殼**：原 slug 保留標頭＋一行「已併回 [[母頁]]」（`page_role=redirect`），否則週報與外部連結永久斷。
```

（替代方案：把偵測端那段換成「本節判準自 2026-11-14 起暫停適用，直到偵測端上線；在此之前不得手算執行」。重點是不能留一條沒有觸發端又會誤傷 archive 的條文。）

---

## 🟡 應修級

### 4. 「母頁本身不逾 300 行，受『母頁契約』看守」——母頁契約沒有任何行數檢查

**證據**：唯一驗 300 的是 `patterns_tree_audit.py:42`，且 `:41` 把頁名寫死為 `community-tech-patterns`；`check_hierarchy.py` 無行數檢查；`check_page_thickness.py` 門檻是 600。實測母頁正文：`entities/pricing` **314 行（已逾且無訊號）**、`anthropic-agent-stack` 264、`community-tech-patterns` 199、`anthropic-business` 193、`claude-code` 184、`ai-agent-safety` 173、`market-signals` 135。

**修訂文字** — `page-lifecycle.md:25` 中該句整句取代：

```markdown
母頁本身不逾 300 行——**機械看守只覆蓋 patterns 樹**（`scripts/patterns_tree_audit.py` 把 `topics/community-tech-patterns` 的 300 行寫死，`/wiki-lint` 社群週更第 4 步跑）；其餘母頁靠 5o 的 `check_page_thickness.py`，而它的門檻是 600 行，**不會看到母頁破 300**。因此每次升格或母頁結論層重寫，執行者自己量一次（`python -c "import sys;sys.path.insert(0,'scripts');from check_page_thickness import body_lines;from pathlib import Path;print(len(body_lines(Path('wiki/<頁>.md').read_text(encoding='utf-8-sig'))))"`），逾 300 當輪下沉事件流，並在 `%%` 備忘記一行 `母頁行數 YYYY-MM-DD：N 行`。
```

### 5. 同檔兩個長度政策打架：「> 200 行…不建議拆分」vs「逾 600 行必須交代切法」

**證據**：`page-lifecycle.md:111` 的 200 行門檻**沒有任何消費端**（`grep "200 行\|LINE_LIMIT\|MAX_LINES" scripts/ src/tests/` 只有 `check_cell_limits.py` 的 200 **字元**與 `devpractice_diff.py` 的 120），而它寫的處置「不建議拆分」正面否決同檔 `:25` 與 5o 的拆頁政策。

**修訂文字** — 該列整列取代：

```markdown
| 頁面過長 | 正文 > 600 行（口徑同 `scripts/check_page_thickness.py`） | 先檢查入口層（callout / 概覽表 / 月份或主題分組）；入口層齊了仍逾 600 → 進 `/wiki-lint` 5o 的拆頁流程（本檔「頁面拆分原則」），不得以「已有入口層」為由不交代切法 |
```

### 6. `/pipeline-change-check` 的指標組漏掉 🧭 專頁雷達（`topicRadar`）

**證據**：`web_reader/data/digest/2026-11-13.json` 有 `topicRadar`（list 2）、`bulletin`、`sedimentedToday`（list 23）等鍵；日報 8 個區塊，指標組只列 6 個。registry 另有 sync_pair「專頁定向抓取的三處說法必須同步」，而動 `topic_watch.json` 正是本指令的適用情形。

**修訂文字** — `pipeline-change-check.md:18-20` 區塊清單整段取代：

```markdown
- 各區塊條目數（**與 `.claude/skills/news-digest/references/format.md` 的八個區塊 emoji 一一對應，新增區塊時兩邊同批加**）：`focus`(📌) / `topStories`(⭐) / `techUpdates`(🔧) / `billing`(💰) / `mediaReports`(📰) / `discussions`(💬) / `topicRadar`(🧭) / `sourceStatus`(📡，記長度)
- `sedimentedToday` 長度與 `bulletin` 是否非空（讀者版投影面，改版常忘）
- `discussions` 條目中含 `sentiment` 非空值的比率（格式健康 proxy）
- 各區塊條目中 `body` 非空的比率（解析健康 proxy）；`focus` 無 `body` 欄，改記 `ref_urls` 非空比率
```

### 7. `sourceStatus` 括號註記已過期；「由 6e 接手」只接一半

**證據**：`sourceStatus` 現有 15 筆 `{name, ok, count}`，非空陣列。6e 確實讀 `sourceStatus`，但**整份 6e 沒有任何一條看 `articleCount`**，而 `:43` 承諾「連續 3 天的文章數與來源分布由 6e 接手」。

**修訂文字**：`:16` 改 `- \`sourceStatus\`：各來源 \`{name, ok, count}\`（來源分布；回報長度＋\`ok=false\` 的來源名）`；`:43` 改：

```markdown
5. 全部通過後在回報寫一行：「來源分布的連續 3 天趨勢由 `/wiki-lint` 6e 來源健康檢查接手（它讀 `sourceStatus`）；**文章數總量沒有週更接手端**，±30% 以上的變動在本步當輪歸因完畢，不得留給 6e。」
```

### 8. `/pipeline-change-check` 的「改動前必跑 baseline」沒有任何執行端

**證據**：`grep -rn "pipeline-change-check\|pipeline_baseline" .claude/ CLAUDE.md scripts/` 只命中指令自己、registry allowlist 與 docs；`dev-done.md` 三條完工條件沒有一條提 baseline，也沒有 hook。`docs/workaround-register.md:39、:55` 兩筆已收斂條目的理由都是「原基線已被後續改版覆寫」——正是沒有執行端的後果。

**修訂文字** — `.claude/rules/dev-done.md` 三條之後、判斷式之前插入：

```markdown
4. **改到產出的，改前有基線**：動 `src/news_aggregator/`、`scripts/build_web.py`、`.claude/skills/news-digest/references/{format,selection}.md`、或 `.claude/reporter-rules/shared.md` 互動門檻對照表時，寫第一行程式**之前**先跑 `/pipeline-change-check baseline`（寫 `src/logs/pipeline_baseline.json`），改完並跑過一次 pipeline 後跑 `/pipeline-change-check compare`。沒有基線就不是「進行中」而是「無法驗收」——基線會被下一次改版覆寫，事後補不回來（`docs/workaround-register.md` 兩筆因此作廢）。
```

`pipeline-change-check.md:8` 句末補：`本指令的義務登記在 \`.claude/rules/dev-done.md\` 第 4 條（改上述檔時自動載入），不靠記得。`

### 9. `agents/wiki-reporter-features.md` 內嵌的 feature-radar 條目格式是過期副本

**證據**：agent 檔 `L32` 寫 `**狀態：** GA / Preview`，而 `features/pages.md:58` 的狀態值域是「正式發布／Beta（範圍）／官方公告（尚未生效）／Research Preview／正式發布（安全修復）」，**沒有 GA**；agent 檔的副本還**少了 `**現在要試嗎：**` 一整段**，而現行 `wiki/feature-radar.md` 的條目全部有它。

**修訂文字** — 把 `L26` 與整個 `L28-44` 區塊取代為兩行：

```markdown
- feature-radar 有新條目時，在回報中附上完整條目**與全覽表那一列**，讓主編寫入（不直接改 feature-radar.md / index.md / log.md）
- **條目格式與全覽表列格式不抄在本檔**——單一家是 `.claude/reporter-rules/features/pages.md`「feature-radar」節的「新功能條目格式」與「新條目必須同時補全覽表一列」（該節每日必讀，見上方第 3 項）。兩個家必漂：本檔舊副本曾寫 `狀態：GA / Preview`（不在狀態值域裡）並漏掉 `**現在要試嗎：**` 一整段。
```

### 10. 三支腳本把 delta-first callout 的規則端指到已搬走的檔

**證據**：規則現住 `.claude/reporter-rules/daily-contracts.md:13、:25`，但 `scripts/check_callout_coverage.py:21`、`scripts/check_reader_digest.py:25`、`scripts/check_reader_language.py:164` 都指向 `page-templates.md`「頂部 delta-first callout」，而該檔全文只有 `:42` 一處順提、沒有該節。`check_reader_language.py:164` 那句是**印給被點名記者看的 why 訊息**。`check_rules.py` 檢查 2 只驗檔存在、不驗節存在。

**修訂文字** — 三處逐字改成 `.claude/reporter-rules/daily-contracts.md`，並在 registry `sync_pairs` 加一筆：

```json
    {
      "name": "頂部 delta-first callout 的規則端節名：規格端（daily-contracts.md）與四個消費端的指路字串同步（節名或檔案搬家只改一側，被點名的記者會被導去不存在的節）",
      "assertion": "all_contain",
      "files": [
        ".claude/reporter-rules/daily-contracts.md",
        "scripts/check_callout_coverage.py",
        "scripts/check_reader_digest.py",
        "scripts/check_reader_language.py",
        "scripts/build_reader_digest.py"
      ],
      "patterns": ["頂部 delta-first callout"]
    },
```

### 11. `market/daily.md` 的「機械契約字串」表漏登記免責 callout 的逐字字串

**證據**：`src/tests/test_market_signals.py:124-140` 逐字斷言 `非投資建議` 且必須是正文第一條 `>` 行；`market/daily.md:13` 只寫「常駐免責 callout，不得移除」，`:48` 的契約表只登記「判讀標題」一列。記者改寫成「不構成投資建議」就會讓 `run_tests.py` 紅。

**修訂文字** — `market/daily.md:52-54` 契約表加兩列：

```markdown
| 免責 callout | 首行必須逐字含 `非投資建議`，且必須是 H1 之後**第一條** `>` 行（排在 delta-first `> **最新判讀**（日期）` callout 之前） | `src/tests/test_market_signals.py::TestDisclaimer`（母頁與四子頁逐頁驗，掛 `run_tests.py`） |
| 線名查法 | 子頁判讀的 `**一眼**` 行含 `線：<線名>` | `.claude/reporter-rules/market/pages.md`「路由」的 `grep -l "線：<線名>" wiki/topics/market-signals-*.md`——線名改寫等於這條線在路由上失蹤 |
```

`:13` 改為：

```markdown
本頁是**教學型消息面事件研究，不是投資建議**。母頁與四子頁的頁首都常駐免責 callout，**首行逐字含「非投資建議」、且必須是 H1 之後第一條 `>` 行**，不得移除、不得改寫那四個字（機械契約，見下方表）。
```

### 12. `community/pages.md` 的硬編行號已漂一處；patterns 路由表的「7 列」硬斷言未登記

**證據**：`pages.md:49` 寫「（L329）」，而 `build_web.py` 的 `ANCHORED_WIKILINK_RE` 實際在 `L337`（L329 是空行）；`:87` 的 L186 與 `community/daily.md` 的 L137 目前正確。`patterns_tree_audit.py:23` 有 `assert len(ROUTE) == 7`——開第 8 個子頁會 AssertionError 整支掛掉，而 `pages.md:39、:45` 都沒提這條耦合，registry 也沒登記。

**修訂文字**：`:49` 刪「（L329）」改為

```markdown
**不可寫同頁簡寫 `[[#YYYY-MM]]`**——`scripts/build_web.py` 的 `ANCHORED_WIKILINK_RE` 要求 `#` 前至少一個字元，同頁簡寫不會被 `check_wikilink_anchors()` 檢查到，等於沒有看守。（引用符號名不引行號：行號會隨檔案長大而漂，`check_rules.py` 檢查 7 只驗符號存在。）
```

`:87` 刪「，L186」；`:45` 那條 bullet 改為：

```markdown
- 新類別入 `## 模式概覽` 的同一輪加進本表某一列；某一群自己長出第二個故事、子故事三題答得齊，才開新子頁，屬裁決事項。**本表列數是硬契約**：`scripts/patterns_tree_audit.py` 有 `assert len(ROUTE) == 7`，增刪一列會讓它直接 AssertionError（不是回報違規），所以開新子頁／併回子頁必須與該腳本的常數同批改，並同批更新 `.claude/review-registry.json`。
```

### 13. `README.md` 的「記者 × 檔案」表數字在第 20–24 波之後全面過期

**證據**：8 格裡 5 格的「負責頁數」錯、7 格裡 4 格的「節數」錯（features 實際 14 頁／表寫 11；commercial 13／6；market 5／1；safety-policy 4／3；features pages 10 節／表寫 6）。`reporter_pages.py --all`：模型 15／功能 28／商業 24／安全政策 13／社群 19／人物 39／開發實務 1／投資分析 5／合計 144。

**修訂文字** — `README.md:9-20` 取代（把會腐的數字換成查法）：

```markdown
## 記者 × 檔案

| 記者 | daily | weekly | pages |
|---|---|---|---|
| features（🛠️ 工具/功能） | ✅ | — | ✅ |
| community（🌐 社群） | ✅ | ✅ | ✅ |
| commercial（💼 商業） | ✅ | ✅（主編層：pricing 通路與乘數） | ✅ |
| models（🤖 模型） | ✅ | — | ✅ |
| market（投資分析，不在分類路由內） | ✅ | ✅（主編層：回顧結算＋教材頁） | ✅ |
| people（👤 人物） | ✅ | — | —（無結論表） |
| safety-policy（🏛️ 政策/安全） | ✅ | — | ✅ |
| devpractice（開發實務，只收官方使用指南一種條目） | ✅ | ✅ | ✅ |

**頁數不寫在這裡**（拆頁波次每改一次就全錯一輪，2026-11-14 審查時 8 格有 5 格對不上）：
- 明列頁數 → 讀該記者 `daily.md` 的「負責頁面」表（market 的在 `daily.md` 開頭的「負責頁面：」一句，不是表）
- 實際認領頁數 → `python scripts/reporter_pages.py --all`（依頁面 `domain` ＋ `pending_handoffs.OWNER_OVERRIDES`，含子頁，是唯一權威口徑）
- `pages.md` 的節數 → `grep -c '^## ' .claude/reporter-rules/<類別>/pages.md`

「明列」與「概括覆蓋」的差別很重要：`wiki/CLAUDE.md`「搜尋策略」第 5 路規定，只被「領域＝X 的所有頁面歸本記者」概括條款覆蓋的頁，不算證實會被更新（2026-08-05 large-codebase-workflow 孤兒化 10 天的教訓）。
```

### 14. 「五份跨記者共用檔」漏掉 `batch-edit.md`（實際六份）

**證據**：目錄有 6 份（`shared.md`、`daily-contracts.md`、`shared-when.md`、`page-templates.md`、`page-lifecycle.md`、`batch-edit.md`）；`batch-edit.md` 被 `agents/wiki-reporter-features.md:17` 當每日必讀觸發條件、被 `scripts/apply_edits.py:6` 指為家，但 `README.md:22-30、:33` 都沒列。

**修訂文字**：「五份」改「六份」，表末加一列：

```markdown
| `batch-edit.md` | 批次修改（`scripts/apply_edits.py`）的步驟與禁令。**試點中**：目前只有功能記者在每日派工被要求讀（觸發條件在 `.claude/agents/wiki-reporter-features.md`「開始前必讀」第 5 項：本輪跨頁合計 ≥ 3 處）。試點的對照算法、通過門檻與複查日登記在 `docs/workaround-register.md`（owner 主編，複查日 2026-11-22） |
```

`:33` 必讀鏈改為：

```markdown
記者由 `.claude/agents/wiki-reporter-*.md` 的「開始前必讀」清單指名（`shared.md` ＋ `daily-contracts.md` ＋自己資料夾的 `daily.md`／`pages.md`／`weekly.md`，建頁時另加 `page-templates.md`，本輪改動 ≥ 3 處時另加 `batch-edit.md`；`pages.md` 一頁一節，只讀本次要動的頁的那幾節，不整檔讀）；…
```

`batch-edit.md:3` 改為：

```markdown
試點中，目前只有功能記者在每日派工被要求讀本檔（觸發條件在 `.claude/agents/wiki-reporter-features.md`「開始前必讀」第 5 項）。試點的通過門檻（回合數對基線 52.1 降幅 ≥ 30%）與複查日登記在 `docs/workaround-register.md`——本檔不重抄，那裡才是結案的家。
```

### 15. `features/pages.md` 漏登記「旗標名必須含 `CLAUDE_CODE_` 前綴」這條硬契約

**證據**：`scripts/build_flags_mentions.py:33` 的 `FLAG_RE = CLAUDE_CODE_[A-Z0-9_]{3,}`，`:78-84` 無法辨識就 `raise PageFormatError` → exit 2（整支掛掉，不是跳過該列），而錯誤訊息寫的是「階欄要 1–4 單一數字」。`features/pages.md:303` 的紀律段沒提前綴，同節示例正是沒有前綴的 `DISABLE_TURN_HANDOFF`。

**修訂文字** — 「**階欄只寫 1–4 單一數字**」那條 bullet 整條取代：

```markdown
- **追蹤表兩個硬契約，破任一條整支 `build_flags_mentions.py` exit 2（不是只跳過那一列）**：① 階欄只寫 1–4 單一數字，備註寫別欄；② **旗標欄必須含一個 `CLAUDE_CODE_…` 字樣的名字**（`FLAG_RE = CLAUDE_CODE_[A-Z0-9_]{3,}`）——沒有這個前綴的名字（`DISABLE_TURN_HANDOFF` 型）不進追蹤表，寫進「代號旗標」節只記出現與消失。對帳腳本靠表頭「旗標」「階」兩欄名定位，欄序可換、可加欄。**exit 2 的錯誤訊息寫的是「階欄要 1–4 單一數字」，但真正的原因也可能是前綴**——先核旗標名，再核階欄。
```

示例改為：`- 第一階只抄名字，**不猜功能**。名字能推測的（\`CLAUDE_CODE_DISABLE_TURN_HANDOFF\`）也只寫名字，解讀等第 3 階證據。`

### 16. `strip_rule_markers.py` 留下的空括號殘骸；且「搬入」類標記逃過廢除

**證據**：`features/pages.md:79`「**先過時間閘**（）」、`:84`「**防霸榜規則（）：**」、`:89`「…不上讀者正文，）」、`shared-when.md:24`「（）：」、四處沿革檔行「…（歷史敘事不進 agent 讀取範圍，）」；`scripts/strip_rule_markers.py:36` 的 `_KIND` 不含「搬入」，故 `shared.md:29` 仍殘留 `[搬入: 2026-09-12，原住 wiki/CLAUDE.md]`——而它緊接在「❌ 日期後接括號或任何說明」之後，記者會讀成範例的一部分。

**修訂文字**（逐行）：`features/pages.md:79` → `1. **先過時間閘**：候選池 = 發布日期距今 ≤ 30 天、…`；`:84` → `**防霸榜規則：** 若某條目已連續上榜超過 7 天，…`；`:89` → `…寫進頁面的 \`%% … %%\`（維運備忘，不上讀者正文） |`；四處沿革檔行統一為 `> **沿革檔：** \`docs/rules-changelog/<檔名>.md\`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍）`；`shared-when.md:24` → `1. **先跑入邊清單，那是必查名單**：`；`shared.md:29` 行尾 `[搬入: …]` 整段刪除；`strip_rule_markers.py:36`：

```python
_KIND = r"(?:加入|改版|順序改版|改名|裁決|移入|搬入|擴充|使用者指示)"
```

並在 `strip_text()` 收尾加一行把 `（）`、`，）`、`（ ）` 收掉。

---

## 🟢 建議級

### 17. market 的 `## 回顧結算` 表引用「時段蒸餾與封存」不成立

`market/pages.md:39` 與 `market/weekly.md:45` 都指向該節，但該節（`page-lifecycle.md:82、84`）明文「結論層（摘要、現況、決策表、對照表、風險表）永遠不適用」且「時段＝一個區塊 × 一個月份」。回顧結算是累積列表、不按月分組。

**修訂文字**（兩處同字）：

```markdown
已結算列**永久保留**（表是判準的紀錄，不是待辦清單）。**本表不走「時段蒸餾與封存」**——那節只處理按時間 prepend 的事件流，明文排除決策表。某子頁表長超過 20 列時：把判讀日距今 ≥ 6 個月、且「對錯」已定案（非 ⏳、非 `～ 仍懸`）的列，整批逐字搬進 `wiki/topics/market-signals-archive.md` 的 `## 回顧結算（已結案）`，原表留一行「YYYY-MM 以前的 N 列見 [[topics/market-signals-archive#回顧結算（已結案）]]」；合計表的數字含已搬的列（命中率不因搬家變好看）。
```

### 18. sweeps `5j` 標題寫「四表」，正文與引用都是五表

`sweeps.md` 的 `## 5j. 商業健康度四表退場複查` 與 `SKILL.md:31` 寫「四表」，正文列五張（指標／人物／風險／合作／三大雲），`commercial/pages.md:10` 寫「第 1、4、5、6、12 條」（五條）。

**修訂文字**：三處「四表」改「五表」，回報格式行補三大雲：

```
商業健康度五表健檢（5j）：指標 N 列（移除 a／補位 b）／風險 M 列（移除 c／補位 d）／合作 K 列／人物 P 人／三大雲 ✅ 無異動或已覆寫 Q 格／通路快照資料截至 YYYY-MM-DD
```

### 19. 三處措辭不可判定

| 檔:行 | 現文 | 修訂文字 |
|---|---|---|
| `page-lifecycle.md:107` | `## 警示觸發重構（超過閾值時嘗試修復；工作量過大則記錄 log.md 待辦）` | `## 警示觸發重構（逾閾值即當輪修復；修復需新建頁或拆頁時不在本節做，改記一行進 \`wiki/log.md\` 並轉 5o 厚頁流程）` |
| `features/daily.md:66` | `\| 功能從 Preview 升格正式 \| 考慮升為 ✅，回報主編 \|` | `\| 功能從 Preview 升格正式 \| 官方公告 GA／正式發布當輪升為 ✅；公告同時載明已知限制或範圍（Beta 範圍、僅某方案可用）則升 ⚡ 並在條目「注意事項」寫出範圍。兩者都回報主編 \|` |
| `agents/wiki-reporter-commercial.md:22` | `每條目盡量帶金額/百分比/股價/HN score + 來源 + 日期。` | `每條目必帶**來源＋日期**；金額／百分比／股價／HN score 有具體數字就寫，沒有就在同一句明寫「報導未載金額」——不得省略不提（同檔「分析視角」的同一條判準：寫不出具體對象或數字就明說，空的意涵句讓讀者誤以為有結論）。` |

### 20. 範本 fence 缺「不要照抄佔位字」的護欄（預防性）

`market/daily.md:60-71` 的 fence 直接接在「每則五段，順序固定：」之後，`事件名`／`線名`／`課名`／`標的` 等佔位字無標註（`features/pages.md` 的對應 fence 有）。實測現行 `wiki/` 無佔位字洩漏。

**修訂文字** — `market/daily.md:59` 改為：

```markdown
前四題壓成第一行，後兩題各一段，最後加「一課」。每則五段，順序固定（**下方 fence 是骨架，`事件名`／`線名`／`課名`／`標的` 都是佔位字，一律換成本則的實際內容；fence 的三個反引號本身不寫進頁面**）：
```

### 21. 已驗證為「真有執行端」的承諾（反面對照，不需修）

`page-lifecycle` 蒸餾例外 1（`wiki_graph.py explain --section` 可用）、母頁 callout 不落後子樹（`check_hierarchy.py:137`）、archive 狀態（`:126-129`）、index `↳ 子故事：` 投影（`:152`）、feature-radar 當月對帳（`check_feature_radar.py` 掛 `run_tests.py:52`）、`devpractice_diff.py` 三個子命令、`check_devpractice_state.py`（掛 `run_tests.py:65`）、market 五頁歸屬三層看守（`PAGE_TO_REPORTER` ＋ `OWNER_OVERRIDES` ＋ `TestOwnership`）、記者無 web 工具／不可再委派（`guard_roles.py` H7 ＋ `WEB_AUTH_MARK`）、批次修補量測端（`ingest_metrics.py:58`）。

---

## 類型分佈

```
類型分佈：規格改了機器沒跟 8（#1 #2 #6 #7 #10 #11 #12 #15）／新舊打架 6（#5 #9 #13 #14 #17 #18）／措辭不可判定 3（#19 三處）／空頭承諾 3（#3 #4 #8）／長度與殘留 4（#16 殘骸、#19 標題、#20 混染）
```

**長度與注意力補充**：`commercial/pages.md:30-78` 一節塞 13 條編號條文，第 1、4 條各逾 900 字元單段，「入口只有兩種訊號」藏在段中央——建議每條拆成「判準／上限／退場／讓位」四個小標。可直接砍的重複：「讓位理由寫 `%%` 備忘」那句在 `commercial/pages.md` 2 次、`safety-policy/pages.md` 2 次、`community/pages.md` 1 次共 5 份逐字副本，建議在 `daily-contracts.md`「呈現品質標準」加一列，五處各改為「讓位註記照 `daily-contracts.md` 該列」。`page-lifecycle.md:25` 是 700＋字元單段含 6 條獨立規則，關鍵的 600 行門檻被夾在第四句。
