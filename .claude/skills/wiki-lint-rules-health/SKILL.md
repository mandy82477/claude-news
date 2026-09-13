---
name: wiki-lint-rules-health
description: /wiki-lint C 段：規則檔健檢（6a–6l）——規則矛盾、引用驗證、遵守率、規則年齡、來源健康、品質指標、密度、突變測試、對抗輪、連結缺口、讀者語言，收尾記漏抓帳與規則版本戳。
---

# Wiki Lint — C 段：`6. 規則檔健檢`（6a–6l）

由 `.claude/skills/wiki-lint/SKILL.md` 帶起。**這一段檢查的是規則本身，不是 wiki 內容。**

開工前讀取 `wiki/CLAUDE.md`、`.claude/skills/wiki-ingest/references/classification.md`、`.claude/reporter-rules/page-templates.md`、`.claude/reporter-rules/shared.md`，以及 **`/wiki-lint` 自己的五個 skill 檔**（`.claude/skills/wiki-lint/SKILL.md`、`.claude/skills/wiki-lint-reporters/SKILL.md`、`.claude/skills/wiki-lint-sweeps/SKILL.md`、`.claude/skills/wiki-lint-reader-acceptance/SKILL.md` 與本檔），依序執行下列各項。

> `/wiki-lint` 自己的 skill 檔必須在掃描範圍內：**檢查者把自己排除在檢查範圍外，是這類缺陷的共同形狀。**（沿革檔 2026-08-28 D）

各項回報行原樣填進步驟 8 的 lint 紀錄（模板見 `.claude/skills/wiki-lint/references/log-format.md`）。

---

## 6a. 規則矛盾偵測

逐段掃描，找出同一行為在不同章節有相反指示、同一情境觸發條件衝突、新舊規則語意重疊或互相否定。

→ 輸出：
```
⚠️ 矛盾：[規則 A 位置] vs [規則 B 位置]
  A 說：「…」
  B 說：「…」
  建議：保留 [A/B]，理由：…
```
→ **向使用者確認後再修改**，不自行決定保留哪條規則。

> 修完矛盾後**必須回掃**：依 `.claude/reporter-rules/shared.md`「事實更正必回掃」，拿該事實的關鍵字 grep 全庫，把仍在講舊說法的引用方一併上修。3a 判矛盾時「以較嚴謹者為準」會把結論**下修**到低確信度頁面，而事後那個結論被查實**上修**時，被下修過的引用方不會自己回來——同步是雙向的，但機制原本只有單向。

## 6b. 規則引用驗證

**由 `scripts/check_rules.py` 檢查 3（錨點）看守**：規則描述中引用的頁面錨點（清單住 `.claude/review-registry.json` 的 `anchors`，勿在此另抄一份）必須仍存在於對應檔案。本步只做失敗判讀：紅燈＝該錨點消失或改名 → 向使用者說明是規則過時還是頁面被誤改，**不自行刪除規則**；新增錨點登記進 registry，不改引擎。

輸出：`📎 引用驗證：✅ check_rules 檢查 3 全部有效／⚠️ [錨點名] 失效 → 規則可能過時`

## 6c. 規則遵守率抽樣

讀取 `wiki/log.md` 最近 3 筆 Ingest 條目，對照：

| 規則 | 合格標準 |
|------|---------|
| 每次 ingest 執行呈現品質審查 | log 含 ✅/⚠️/📋 標記，3/3。**明文 rollup 行與表格式摘要等價**——標記散在各記者的表格列裡即算合格，不要求另寫一行總結（該規則要的是「有沒有審查」，不是「用什麼版面呈現」）|
| 每次 ingest 更新 feature-radar.md | log 提及 feature-radar，3/3 |
| 決策表首選變動時同步證據欄 | 有首選更換的 lint 須在 log 提及該症狀列 |
| log.md 格式正確（來源日報、更新頁面、摘要欄位） | 3/3 |

輸出：
```
🔍 遵守率抽樣（近 3 次 ingest）：
  ✅ 呈現品質審查 — 3/3
  ⚠️ 近期工具更新 — 1/3
```
→ 遵守率 < 2/3 的規則：說明原因，**向使用者確認是否調整規則**。

## 6d. 規則年齡審查

```
python scripts/lint_health.py age --days 60
```

年齡由 git blame 取各規則檔 `##`／`###` 節標題的最後修改日，不靠人手標記。

- **逾 60 天**：逐一確認該節描述的行為是否仍與現狀吻合，並問「少了這節，執行者會不會做錯」——不會就提議刪
- **60 天內**：記「在閾值內」

輸出直接抄腳本的最後一行進 log。→ 逾閾值的列**向使用者確認是否修訂或刪除**，不自行修改。

## 6e. 來源健康檢查

讀取近 7 天 `web_reader/data/digest/*.json` 的 `sourceStatus` 陣列（每來源 `{ok, count}`），統計每個來源的每日抓取數：
- 任一來源 **`ok=false`** → ⚠️ 告警（fetch 拋例外，與「沒新聞」無關）
- **社群／媒體來源**（HN、Reddit、Google News、GitHub、GitHub Issues、dev.to、Blogroll）**連續 3 天 count=0** → ⚠️ 告警（可能是來源壞掉而非真的沒新聞，如時區 bug、RSS 改版、rate limit）
- **清冊／官方型來源**（Official Skills、Official Docs、Claude API Release Notes、Anthropic Blog、Anthropic Status、Topic Watch）`ok=true` 且 count=0 **屬正常**（上游無異動）——「查過確認沒有」與「沒查」的分界就是 `ok` 旗標，**不對這組發連續 0 告警**；它們的異常訊號是 `ok=false`，或 GitHub Actions 的 `daily-gather` 連續失敗（`data/source_funnel.jsonl` 當日缺列）
- 輸出各來源 7 天貢獻統計表，供判斷來源價值

發現 ⚠️ 時回報使用者，不自行修改管線程式。

**發現窗產消對帳：** 讀 `data/discovery_queue_history.csv`（各發現窗每日抓取時寫入，schema `date,window,queued,emitted,note`；window 現值 `rising`／`crossing`／`inventory`／`hn_bridge`，note 值域 `ok|cold_start|disabled|retired|error`；`retired`＝該類已判定結構性不適任、刻意撤下，**不得判為窗死**）。**逐 window 判讀**：
- 某 window 佇列量（queued−emitted 積壓）連兩週上升、或排空預估 > 30 天 → ⚠️ 回報使用者（提高該窗配額／一次清倉擇一），不得只抄數字
- **某 window 連 3 天完全缺列 → ⚠️「該窗未執行或靜默死亡，查 daily gather」**——「今天沒有候選」（queued=0 的列）與「窗沒跑」（整列缺席）必須分得開
- 檔案缺失或全檔最新日期距今 > 3 天 → ⚠️「對帳未寫入，查 daily gather 是否失敗」——**掃描失敗不得當成 0**
- 另讀 `data/repo_star_history.csv`（E 窗記錄端）**行數與最新日期**：連兩週不增長 → ⚠️「星史檔未被保存（雲端 commit 清單？）」——E 窗壞掉時會**永遠冷啟動且吐 0，看起來像正常**，這行檢查是它唯一的看守
- 起因見沿革檔 2026-09-02

**來源記分卡：** 執行 `python scripts/source_scorecard.py`，將輸出表格附入本節回報。判讀規則（指標定義見 `docs/source-scoring-optimization.md`）：
- 標 ⚠️ 樣本不足的來源只讀趨勢，**不得**據以建議汰換
- 樣本充足（✅）且 Wilson 下界與 Presence 雙低的來源 → 列入「觀察名單」回報使用者，不自行動 pipeline 或 registry
- 出現「⚠️ 未註冊 slug」→ 檢查 `data/source_registry.json` 與記者回報的 slug 用字，回報使用者
- Google News 低信譽桶（pc1 < 0.4）> 0 筆 → 列出條目供人工覆核

## 6f. 跨檔案語意矛盾掃描

讀取 `.claude/commands/review-commands.md`「同步配對註冊表」列出的所有配對，逐組**語意比對**（非僅字面 grep）：兩側對同一行為的指示是否實質衝突（例如一方說「必須 foreground」另一方說「可背景執行」；一方列六類 subagent_type 但名稱與另一方不同）。

→ 輸出 dry-run 回報：
```
⚠️ 語意矛盾：[配對名稱]
  A 位置：[檔案:行號] 說：「…」
  B 位置：[檔案:行號] 說：「…」
  建議：保留 [A/B]，理由：…
```
若無矛盾則寫「✅ 全部配對語意一致」。

**向使用者確認後才修改**，不自行決定保留哪條規則。

## 6g. 品質指標

**指標一：ref 覆蓋率（每週必跑）**——回歸偵測器：格式改動弄斷歸因時會連續每天壞，成本僅兩個 grep，不可等月報。

⚠️ **日報有三種歸因格式，必須同時計**：`（ref: url）` 行內式為 2026-07-24 以前；`[N]` 註腳＋檔尾清單為 2026-07-25～2026-09-03；`（[來源名](url)）` 行內連結為 2026-09-04 起（格式定義見 `.claude/skills/news-digest/references/selection.md`「📌 今日聚焦」）。**只計其中一兩種，會把新格式的日子讀成 0 而誤報覆蓋率暴跌**。此為「回歸偵測器自己壞掉」的前例，改日報格式時必須回頭同步本節。

⚠️ **必須先限縮到「今日聚焦」區塊再數**：2026-09-03 以前的日報檔尾「選材門檻」附錄（已於 09-04 廢除）使用相同的 `- **[...]**` 條列形狀，不限縮會灌大分母。

```
# 分母：今日聚焦條列數
awk '/^### 📌 今日聚焦/{f=1;next} /^### /{f=0} f' news/YYYY-MM-DD.md | grep -cE '^- \*\*\['
# 分子：帶歸因的條列數（兩種格式擇一即算）
awk '/^### 📌 今日聚焦/{f=1;next} /^### /{f=0} f' news/YYYY-MM-DD.md | grep -E '^- \*\*\[' | grep -cE '（ref:|\[[0-9]+\]|\]\(http'
```

對近 7 天每一天分別執行。覆蓋率 = 7 天分子總和 / 7 天分母總和。
- **< 80%** → ⚠️ 警示，列出哪幾天缺歸因
- **≥ 80%** → ✅ 通過
- 某天分母為 0（當日無「今日聚焦」區塊）→ 該天不計入分子分母，並在回報中註明是哪一天

**指標二：採用驗證率（僅每月第一次 lint 執行）**——慢變量（14 天升級窗口），週報只有雜訊。月度判斷方式見 `.claude/skills/wiki-lint/SKILL.md`「月度判斷法」；非首次輸出「非本月首次 lint，跳過採用驗證率」。
統計 `wiki/feature-radar.md` 全覽表與 `wiki/topics/community-tech-tools.md` 工具目錄中，14 天前標記 ⏳ 的條目，有多少比例在 14 天內升級為 ⚡ 或 ✅。
- 僅回報趨勢供判讀，**不觸發強制修改**

**指標三：外部死鏈（每週，讀報告檔，雲端本機皆可執行）**——**不自己連網**，讀 `data/link_health.json`：

```
python -c "import json;d=json.load(open('data/link_health.json',encoding='utf-8'));print(d['checked_at'],len(d['dead']),'死鏈 /',len(d['anti_bot']),'疑似反爬')"
```

該檔由 `.github/workflows/weekly-linkcheck.yml`（排程見該檔）產出並 commit 回 repo——掃 `wiki/**/*.md`（不含 `news/`）逐條 HEAD 驗證，429/403 歸「可能反爬」不算死鏈。**每月 1–7 號全量、其餘週次分層**（只驗新連結與上次非 OK 者）——分層報告仍是完整清單（沒掃的沿用上次結果補回），消費端讀法不變，見 `data/README.md`。

- **新鮮度防線**：`checked_at` 距今 > 8 天 → 視為報告過期，本輪不據以標註，改回報「⚠️ link_health.json 過期（checked_at=…），請查 weekly-linkcheck workflow 是否連續失敗」。**過期報告比沒有報告更危險**——它看起來像剛檢查過。**8 天而非 10 天**：報告是**週更**的，門檻必須小於「漏跑一次」的間隔，否則漏跑一週的舊報告照樣通過。8 天＝週更 + 1 天寬限。**門檻鬆過節奏，等於沒有防線。**
- **只有 `dead[]` 驅動頁面標註**：由對應類別記者標「（原文已失效）」（**保留原 URL 不刪**，供讀者仍可嘗試存取或查 web archive）；`dead[].pages` 已列出引用頁面，直接據以派工
- **`anti_bot[]`（401/403/429）與 `unverified[]`（逾時/連線失敗/5xx）一律不派工、不標註**，僅在指標區列數字

> **分類器口徑**：`dead` 只認 404/410；401 併入 `anti_bot`；逾時與 5xx 先用較長逾時重試一次，仍失敗才歸 `unverified`。**單次逾時是很弱的證據**——連續多週落在 `unverified` 才值得人工看。（沿革檔 2026-08-20 B／C）

輸出：
```
📊 品質指標（近 7 天 / 14 天窗口）：
  ref 覆蓋率：XX%（閾值 80%）→ ✅ / ⚠️（缺 ref 日期：…）
  採用驗證率：⏳→⚡/✅ 共 N 條中 M 條達成（XX%，僅供判讀）／非本月首次 lint，跳過
  外部死鏈：共 N 條疑似死鏈，已標註 M 條 / 非本月首次 lint，跳過
```

**趨勢表 append：** 算完以上指標後，在 `wiki/metrics.md` 表格 append 一列（只 append 不改舊列；月度指標非首次 lint 時該欄填「跳過」）；並讀最近 3 列，輸出一句趨勢判讀（持平／惡化中／已回升），**惡化中即使未破警戒線也要標 ⚠️**。

## 6h. 規則密度審查

6d 問「逾 60 天的規則還吻合嗎」，從不問「還需要存在嗎、能不能只留判準」。本步是密度的消費端。

```
python scripts/lint_health.py density
```

- 門檻：檔 >300 行、或教訓行 >5%（改門檻改腳本常數）
- 超門檻者為**蒸餾候選**：以 `| 檔 | 段落 | 現況行數 | 擬處置 | 省多少行 |` 提案——處置三選一：下沉到該檔的沿革檔（`docs/rules-changelog/`，不在 agent 讀取範圍）或 `wiki/log.md`（考古鏈靠 `[加入:]` 日期→log Query 保持可追）／併入判準一句／規則已被機械檢查接住者改為一句＋指向檢查器
- **每次 lint 至多提案 2 檔，經使用者確認才動**（同 wiki 月度蒸餾節奏）；無候選回報「無密度候選」
- 規則的閱讀者是每個 agent——規則債跟內容債一樣會壓垮閱讀者。density 只量 agent 實際讀的檔（`RULE_GLOBS` 不含 `docs/`），沿革檔刻意不入量測範圍——這是密度量測的正確方向，不是漏算

## 6i. 檢查器的檢查：突變測試

```
python scripts/lint_health.py mutate          # registry 每組配對：抹掉命中後斷言仍綠＝假看守
python scripts/lint_health.py hits report     # 各步驟連續零命中輪數（≥8 輪 ⚠️）
```

- `mutate` 每輪跑（成本秒級）：回報的假看守當場改 pattern
- `hits report` 標 ⚠️ 的步驟：先做人工突變（故意弄壞一個該步該抓的東西，重跑該步看會不會紅）；不會紅 → 檢查失效，修；會紅但世界真的乾淨 → 排入 6h 評估降頻或合併
- 每月首次 lint 另抽 3 個非 registry 檢查（`check_*.py`）做人工突變，用 `random.seed('YYYY-Wnn')` 擲骰選

> 「連續滿分與抓不到問題是同一枚硬幣」原本只是一句話，本步讓它變成動作。（沿革檔 2026-09-04）

## 6j. 對抗輪（月度）

每月首次 lint（判斷法見 `.claude/skills/wiki-lint/SKILL.md`「月度判斷法」）依 `.claude/skills/wiki-lint-rules-health/references/adversarial.md` 派三個對抗 agent：冷讀者審日報、冷讀者審週報＋隨機 3 頁 wiki、prompt reviewer 審近 30 天改過的規則檔。發現逐項修到「無阻擋意見」，並依該檔「收報後」登記 `lint_health.py misses`。非月度首次寫「非本月首次 lint，跳過」。

## 6k. 連結缺口偵測（每輪）

兩頁被同一批頁引用卻互不相連，通常是漏了一條 wikilink、或該有一頁沒建。3b 只抓「完全孤立」，抓不到這種「有連結但缺對的那條」。

```
python scripts/wiki_graph.py gaps --top 10 --with-news
```

一支指令印**兩張表**，證據等級不同，處置相同：

| 表 | 說的是 | 證據 |
|---|---|---|
| 缺口偵測（第一張） | 兩頁**像**——被同一批頁引用 | 結構推論：加權 Jaccard（鄰居權重 1/度數，樞紐不霸榜）；門檻在腳本（共享鄰居 ≥ 2、各自度數 ≥ 3、封存頁不列），只看正文引用邊 |
| 同一則新聞落地兩頁（第二張） | 兩頁**是同一件事**——同一則新聞（同一 `item_url`）被寫進兩頁，兩頁之間卻無任何邊 | 硬證據：`data/source_attribution.jsonl` 的記者歸因，不是推論。已相連的判定含**任何 zone**（相關實體欄有連結就不算缺），封存頁不列 |

- 第二張表比第一張**更該優先處理**：第一張是「你們可能該認識」，第二張是「你們已經在報導同一件事了」。門檻 ≥1 則（判斷依據寫在 `scripts/wiki_graph.py` 的 `CO_LANDED_MIN_DEFAULT` docstring）
- 兩張表**每對三選一**，派給該對頁面所屬類別的記者（跨類別時派頁 A 的記者並登轉知帳）：**補 wikilink**（在語意相關的句子加，不是塞進相關實體欄）／**併頁或蒸餾候選**（兩頁其實在講同一件事 → 進 3f 或月度蒸餾提案）／**登記 `data/graph_gap_ignore.json`**（已審、無需連結，附一句理由；**兩張表共用同一份 ignore 檔**）——沒有第三個出口，同一對會每週重現，變成固定假警報
- 回報：`連結缺口（6k）：相似候選 N 對（補連結 a／併頁候選 b／登記無需連結 c）；同新聞候選 M 對（補連結 d／併頁候選 e／登記 f）`；**連續 2 輪全是 c → 閾值太鬆，調腳本 `min_score`**
- 同一支計算的讀者端是詳頁「你可能也想看」（build 時寫進 graph.json 的 `alsoSee`）：lint 補了連結，該對就從推薦消失，改進相連列表——兩端共用一個分數，不另養一套

## 6l. 讀者語言存量清理（每輪）

內部維運用語（ingest／lint／派工／記者／汰出／不回訪／門檻／二手…）外洩到讀者正文。機械閘已上線，**只擋新增、不追殺存量**——存量得靠本步每週清。

```
python scripts/check_reader_language.py          # WARN 摘要（存量頁數／筆數／前 5 頁）
python scripts/check_reader_language.py --list   # 禁詞清單＋讀者語言替代詞（給修的人抄）
python scripts/check_reader_language.py --page <slug>   # 單頁清單
```

- 讀 WARN 摘要，從命中最多的頁取 **2 頁**，派 `subagent_type: "general-purpose"` + `model: "sonnet"`（機械式改寫，不需旗艦模型）逐條處理，每條三選一：**改寫成讀者語言**（用 `--list` 的替代詞）／**移進 `%% … %%` 維運備忘**（見 `.claude/reporter-rules/shared.md`「維運備忘的家」）／**登記 `data/reader-language-allow.json`**（附理由；page 與 term 不得同時填 `*`）
- 清完該頁後從 `data/reader-language-baseline.json` 的 `pages` **移除該頁整筆**——棘輪只能往下轉，不得為了轉綠把新命中加回基線
- 禁詞清單住 `scripts/check_reader_language.py` 頂部常數（單一來源），要增刪禁詞改那裡，不在規則檔另抄一份
- 回報：`讀者語言（6l）：基線剩 N 頁，本輪清 M 頁，新增命中 K`——**K > 0 代表機械閘擋下了新外洩**，在回報寫出是哪頁哪句

## 漏抓帳與規則版本戳（每輪）

- **漏抓帳**：本輪任何由使用者質疑、對抗輪或記者回報揭露、而 lint 既有步驟**本該抓到卻沒抓到**的缺陷，一律 `python scripts/lint_health.py misses add --date … --issue … --should-catch <步驟> --why <考卷外|考卷內抽樣不足|檢查失效|無對應檢查> --fix …`；每季看 `misses stats` 決定投資哪一步
- **規則版本戳**：步驟 8 記 `規則版本：` ＝ `git log -1 --format=%h -- .claude/`，否則跨週的命中率趨勢無法比較

---

## 邊界

- 由主編（本機主 session 或雲端頂層 session）執行；6l 的改寫可派 `model: "sonnet"` agent，其餘親做。
- **凡本節標明「向使用者確認」者（6a、6c、6d、6f、6h、6j 的規則改動）一律只回報**，寫進步驟 8 的待使用者確認區，不自行改規則檔。
- 改任何 `.claude/` 下的規則檔依 `.claude/rules/claude-md-edit.md` 流程，完成後 `python scripts/check_rules.py` 必須零 ❌。
- `news/` 唯讀、`log.md` 只能 append、繁體中文為主：見 `wiki/CLAUDE.md`「🚫 絕對限制」。
- 驗證閘：十三行回報（6a–6l ＋漏抓帳／規則版本戳）全部有值，且本段若動過規則檔則 `check_rules.py` 綠，才算完。

> **沿革檔：** `docs/rules-changelog/wiki-lint.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍）
