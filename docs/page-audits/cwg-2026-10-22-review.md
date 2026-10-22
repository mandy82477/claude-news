# 第 19 波評審：topics/coding-workflow-guide（2026-10-22）

讀了提案三件、參考副本、`ops.py`、上游三件、規則檔與腳本。行號：「現 Lnnn」是 wiki 現檔，「副 Lnnn」是 scratchpad 參考副本 `w19/design/repo/wiki/topics/coding-workflow-guide.md`。官方原文用主編存在 scratchpad `w19v/` 的 `.md`（2026-10-22 取得）。我自己寫的重算腳本是 `w19/review/rv.py`。

## 結論（五行）

1. **骨架、自足策略和 17 個錨點的改法都站得住**；設計者自己算的數字全部重算吻合（見下表）。
2. **🔴 2 筆是事實錯誤**：A-38 把 `/doctor` 的建議改掛到 `best-practices`，但官方 `memory` L623 寫的就是 `/doctor`，等於把一個錯誤搬進頁面，冷讀者 Q1 卡住的點也沒解；第 5 段的旋鈕句還沿用過期的「`low`／`medium` 只報最有信心」。
3. **🟡 8 筆**：一處漏改（L658「六個入口」）、Q3 少一個詞、鄰頁還有兩處同樣的過期事實沒開轉知、實作單第 2 步會改寫全庫 frontmatter、規則檔的錨點清單和軸線清單與頁面對不上、殘留的內部用語、實作單分工。
4. 冷讀者四題：做完 R-1、R-4 之後，**Q1–Q4 都能在本頁一句話拿到答案**；verified 表 18 列裡該改的 10 列全部改到。
5. 全庫 `coding-workflow-guide#…` 入邊 0 筆，段標題改字不會讓任何外部連結斷掉；跨維護者事項全部走轉知或交給主 session（另外補 2 筆）。

## 數字重算（`rv.py`；pending／reader-lang 直接呼叫腳本函式）

| 項目 | 設計者 | 我算的 | 判定 |
|---|---|---|---|
| 行數（`t.count('\n')`）／正文（`check_page_thickness.body_lines`） | 675→674／649→646 | 675→674／649→646 | ✅ |
| 頁內 `](#…)` 連結 | 17 個要改 | 現 31 個連結（12 個目標）→副 34 個（15 個目標）；要改的：L68、L70–76（8）＋L88–94（7）＋L47–48（2）＝17 | ✅ |
| 頁內斷錨（`app.js:1374` 的 slug 規則，含重名加 `-n`） | 2→0 | 現 L47、L48 → 副 0 | ✅ |
| 懸置標記（`check_pending_markers.check` 跑全庫） | 177→177，基線 165 | 現樹 177／副本 177，基線 165；舊字樣 23／23 | ✅ |
| 讀者語言新增 | 0 | 0（`crl.WIKI` 必須指到副本，否則白名單吃不到，副 L213「不覆寫」會被誤報）| ✅ |
| 字元上限 | 5 筆不變 | 現 L334／397／404／499／571 → 副 L325／388／395／486／558，長度逐筆相同 | ✅ |
| `[[…#…]]` 錨點目標 | claude-code L824 | 標題確實存在，但現行行號是 `claude-code.md:828`（行號漂移，不影響結果）；ecm L98 也存在 | ✅ |
| `check_page_thickness.assessment` | 2026-10-22、未過期 | 同 | ✅ |
| 全庫 `coding-workflow-guide#` 入邊 | 0 | 搜 wiki／data／.claude／scripts，0 筆 | ✅ |

**去向表抽查 6 節**（對照 map 的新行號與副本實際行號）：我想問的是 47–71 ✅、§1 要放哪幾個檔 114–129 ✅、§5 主體 408–428 ✅、§9 526–547 ✅、熱門專案 548–583 ✅、本週亮點 623–632 ✅。現檔和副本 diff 共 331 行，每一處都對得到 draft A 區的某一條，沒有 A 區以外的改動。

## 特別檢查

- **自足四題**：Q1 §1 有答案，但卡點出在 L147／L585 的出處不一致 → R-1。Q2：副 L452 加了「評估者不跑工具」、副 L538 有一句話的階梯，index D-2 改指第 6、9 段 ✅。Q3：副 L412–421 的表格加一句話，方案、單價、試跑估法、$13 參考值都有；只差「$5–25 看什麼」→ R-4。Q4：§3 本來就有答案，入口靠 D-1 補上 ✅。
- **verified 逐列對照**：❌／⚠️ 的 10 列（L218／541／631、L214、L599／663、L173、L131、L257、L421、L427 方案、L434 兩句引文、L440）都改到；L438 補上了 `default` ✅。但有一處 verified 沒覆蓋、仍然過期：第 5 段的 effort 旋鈕 → R-2。
- **新聞條目搬家**：五小時額度全庫只出現在本頁（`pricing.md` 搜 11145838 只在 L269、L528 以頁面連結出現，沒有這句話），C-1 附了原句和來源，有地方可放 ✅。L283 那句有同源的家（pricing L295、L369、L766）✅。effort 預設值的家在 `model-comparison` ✅。
- **錨點入邊**：0 筆。index 和 skill-interest-watch 都用「第 N 段」指過來，段號沒變 ✅。`community-large-codebase-workflow:139` 指第 9 段的內容，新稿仍在 ✅。
- **跨維護者**：C-1～C-5 都走 `pending_handoffs.py open`，參數格式符合 `:228–233`，類別在 `CATEGORIES:37` ✅。D 區歸主 session ✅。漏了兩處同樣的過期事實 → R-5。

## 四視角（只列會改變實作單的）

### 冷讀者

**🔴 R-1　A-38 把正確的出處改錯了；Q1 的「官方衝突」其實有三頁，不是兩頁。** 官方 `memory.md` L623（w19v）原文：「The `/doctor` checkup proposes trims for a checked-in CLAUDE.md: it cuts content Claude can derive from the codebase, such as directory layouts, dependency lists, and architecture overviews, and keeps pitfalls, rationale, and conventions that differ from tool defaults.」所以現 L585「官方 `/doctor` 建議砍掉」本來是對的，A-38 的改法反而錯了；導讀 L604「`/doctor` 的減法原則」、參考來源 L653 也都指向 memory 頁。冷讀者卡住的真正原因是 L147 只列了兩頁。修法：
- **新 A-07b，取代現 L147–L148：**
```markdown
⚠️ **官方三頁在這裡說法不一。** `best-practices` 把「file-by-file descriptions」列為不該放；`features-overview` 兩處明寫「Put it in CLAUDE.md… project structure」「Use CLAUDE.md for… project architecture」；`memory` 頁則說 `/doctor` 的瘦身建議會砍掉 Claude 讀 code 就推得出的內容（目錄結構、依賴清單、架構概述），留下陷阱、理由，以及和工具預設不同的慣例。
可調和的讀法（本頁歸納，官方未明說）：**分界在「讀 code 推不推得出」**——架構決策背後的理由與取捨該放；目錄樹、逐檔描述、讀 code 就看得出的架構概述不該放。
```
- **A-38 改成**：舊 `官方 \`/doctor\` 建議砍掉` → 新 `官方 \`memory\` 頁說 \`/doctor\` 的瘦身建議會砍掉目錄結構（見第 1 段）`
- **A-41 第二條改成**：`- **官方文件自己有衝突**，最明顯的是 CLAUDE.md 該不該寫專案結構（\`features-overview\` 說寫，\`best-practices\` 與 \`memory\` 的 \`/doctor\` 說不寫）。分界是讀 code 推不推得出：架構決策的理由該寫，目錄樹與逐檔描述不該寫。`
- **A-05 第 1 列「缺什麼」欄**：`官方兩頁措辭衝突，總量無判準` → `官方三頁說法不一，總量無判準`
- 參考來源 memory 那列（現 L653）的「`/doctor` trim」保留不動。

**🟡 R-4　Q3 卡點「$5–25 看不出由什麼決定」還沒解。** 官方 `ultrareview.md` L125 寫「depending on the size of the change」。A-22 表格 ultrareview 那一格改成：`Pro／Max 各 3 次免費（一次性、不重置），之後每次約 $5–25 usage credits，看變更大小`（約 50 字，未超過 120）。

**🟡 R-9　殘留的內部用語**（不在健檢卡的 10 處裡，但屬同一類）：副 L466「原始條目見」→「原始報導見」；副 L493「全庫沒有任何一個」→「本站收錄的資料裡沒有任何一個」；副 L518「全庫只查到」→「本站只查到」；副 L522「缺口原句「規則內容是否還與程式碼現狀相符」仍是全庫零證據」→「「規則內容是否還與程式碼現狀相符」至今沒有任何證據」。

### 機器

**🔴 R-2　第 5 段的 effort 旋鈕已過期，而且把兩個入口的旋鈕混在一起。** 官方 `code-review-local.md` L85：「At `low`, the review reports the findings it's most confident in… From `medium` through `max`, the review broadens coverage.」——現在只有 `low` 會收斂，不是「`low`／`medium`」。GitHub 上的 Code Review 調的是審查等級（`code-review-costs.md` L11「review level」；ecm L104 寫 Quick／Standard／Deep），不是 effort。「重審收斂」verified 也沒核到（提案 §14.3）。A-22 倒數第二段整段換成：
```markdown
**官方給的成本收斂旋鈕**：GitHub 上的 Code Review——觸發模式選 Manual 或 Once、審查等級選 Quick（Standard 為預設、Deep 最貴）、`REVIEW.md` 列出要跳過的路徑與類別、專屬月上限、看各 repo 的估算成本；本機 `/code-review`——effort 給 `low` 只報最有信心的（少誤報而非少覆蓋，`medium` 起擴大覆蓋），自 v2.1.288 起可加 `--max-findings <n>`（或 `all`、`default`）限制回報條數，見 [[entities/claude-code]]；security-guidance 可分層關閉。
```

**🟡 R-3　漏改一處，查證日也不實。** 現 L658「— 六個入口與定價」→「— review 入口、方案限制與定價」。現 L650「官方文件（全部 2026-08-08 查證）：」→「官方文件（2026-08-08 查證；context-window、memory、sub-agents、code-review 系列 2026-10-22 重查）：」。行數不變。

**🟡 R-6　實作單第 2 步 `gen_wiki_frontmatter.py` 會寫入全庫。** `main` 在 `:204–208` 會 glob 全部 entities／topics 並寫入，沒有 `--page` 參數；`run_tests` 和各個閘都不讀 frontmatter 的日期（`grep last_news_update scripts/` 只有產生器本身）。這是在共用工作樹裡多寫幾十頁 diff。**修法**：刪掉第 2 步；frontmatter 交給 `web-publish` 重新產生（`.claude/skills/web-publish/SKILL.md:83`）。

**🟡 R-7　B-3 的錨點清單少列一處，頁內錨點也沒有任何閘看守。** A-36 在第 9 段新加了 `[第 6 段](#6-…)`，所以頁內錨點不只三處。B-3 第二段「頁內「我想問的是」「這條流程長什麼樣」「本週 coding 亮點」三處的錨點由標題算出，標題一改錨點就斷，改標題時三處同批改」改成：「頁內所有 `](#…)` 連結（目前在「我想問的是」「這條流程長什麼樣」「本週 coding 亮點」與第 9 段）的錨點都由標題算出，標題一改錨點就斷；改標題時用 `grep -n '](#' wiki/topics/coding-workflow-guide.md` 全數同批改」。「沒有閘看守」這個缺口寫進 ledger（本波不改 script）。

### 明天的維護者

**🟡 R-8　`pages.md` L21 的軸線清單和頁面對不上**，B-2 只改了末句。L21 寫的軸是「設計→實作→審查→測試→部署→事故→償還」，但頁面實際是 9 段，沒有部署、事故、償還這幾段。B-2 改成**整行取代 L21**（registry 看守字串「不得改以開發領域」保留）：
```markdown
**軸線鐵則：** 以**工程流程階段**為軸（本頁第 1–9 段：寫 CLAUDE.md→探索→規劃→動手寫→review→測試與上線→規則跟上改動→規則保鮮→除錯），**不得改以開發領域（嵌入式／遊戲／資料工程）分欄或分列**。官方做法本身不按領域切，照領域組織會產出大量空格；領域差異只在有具體依據時，於該段寫一句，沒有依據就不寫。
```

**🟡 R-5　鄰頁還有同樣的過期事實，沒開轉知。** (a) `anthropic-agent-stack.md:87` 也寫「Explore 的模型繼承主對話、在 Claude API 上以 Opus 為上限」→ 併進 C-4 的 note。(b)「AGENTS.md 尚未支援 Bedrock、Vertex、Foundry」還留在 `feature-radar.md:486`、`:494` 和 `claude-code.md:89`，三處都用現在式寫，本頁 A-06 已經刪了 → 新開 C-6。C-4 的 note 句尾加上：
`另 L87「Explore 的模型繼承主對話、在 Claude API 上以 Opus 為上限」與官方 sub-agents 頁（L39–41，2026-10-22 查）不符：現行是模型跟主對話相同，主對話跑 Fable 時 Explore 改跑 Opus；guide 第 2a 段已改。`
C-6：
```bash
python scripts/pending_handoffs.py open --from 開發實務 --to 功能 --page feature-radar --note "AGENTS.md 原生讀取（v2.1.277）：feature-radar L486、L494 與 entities/claude-code L89 用現在式寫「尚未支援 Bedrock、Vertex、Foundry」。第 19 波主編 2026-10-22 查官方 memory 頁（L350–369、L411–417），現行不支援情形只列三種（v2.1.277 前、停用內建 plugin、升級後第一個 session），沒有平台限制；guide 已刪此句。請查現況後改寫或標上時點；claude-code L661 版本表是當時 changelog 的原文，可以留。"
```

### 治理

**🟡 R-10　實作單分工。** draft 第 6 步把 `run_tests.py` 排進實作者的閘鏈，但實作者不准跑 → 移給主 session。H-fc0960 的 `close` 要帶 `--by`、`--result`（`pending_handoffs.py:235–236`），完整指令寫在下方第 7 步。A-01 把「最後新聞更新」改成實作當天：本波收了新的官方事實，有先例可循（`lcw-2026-09-23-review.md` 🟡-7），**不算違規**，維持原案。

## 照順序執行（實作單）

| # | 誰 | 檔 | 做什麼 | 驗收 |
|---|---|---|---|---|
| 0 | 主 session | `.claude/tree-claims/` | 宣告 guide、index、`devpractice/pages.md`、`reporter-rules/README.md`、`docs/rules-changelog/reporter-devpractice.md` | 宣告檔存在 |
| 1 | 實作者 | `wiki/topics/coding-workflow-guide.md` | 先跑 `diff <(tr -d '\r' < 現檔) 參考副本`：確認 diff 只有 A 區 hunks，也就是現檔在副本之後沒被別人改過。是 → 用副本覆蓋正文（frontmatter 照舊）；否 → 照 A 區由下往上手動套 | diff 只有 A 區的改動 |
| 2 | 實作者 | 同上 | 套本評審的 R-1（A-07b、A-38、A-41 第二條、A-05 第 1 列）、R-2、R-3、R-4、R-9；把三處 `<實作當天>` 填成當天日期 | `grep -n "實作當天\|六個入口\|/doctor\` 建議\|low\`／\`medium\|全庫零證據\|原始條目" 頁` 0 筆；`grep -c "官方三頁" 頁` = 1；總行數 674 |
| 3 | 實作者 | 同上 | 閘：`check_reader_language.py --page coding-workflow-guide && check_cell_limits.py --page coding-workflow-guide && check_pending_markers.py && python <scratchpad>/w19/design/anchors_js.py wiki/topics/coding-workflow-guide.md` | 新增 0／新增 0／177 ≥ 165／斷錨 0 |
| 4 | 實作者 | `devpractice/pages.md`、`reporter-rules/README.md`、`docs/rules-changelog/reporter-devpractice.md` | B-1；B-2 改為 R-8 的整行版；B-3 換成 R-7 的句子；B-4、B-5、B-6 照貼 | `check_rules.py` 全綠；pages.md 裡「格式表」「官方涵蓋不到」「「深入」」「探索時常撞到」「領域注意」「部署→事故→償還」都 0 筆 |
| 5 | 實作者 | — | **不跑** `gen_wiki_frontmatter.py`（R-6）；不碰 git、不跑 `run_tests.py`；回報改了哪些檔與步驟 3、4 的輸出 | 回報表 |
| 6 | 主 session | `wiki/index.md` | D-1～D-4 | 主 session 自查 index 四列 |
| 7 | 主 session | `data/pending-handoffs.jsonl` | C-1、C-2、C-3、C-5 照原文；C-4 加上 R-5(a) 的句尾；新開 C-6；都先 `--dry-run`。另跑 `python scripts/pending_handoffs.py close H-fc0960 --by 開發實務 --result "第 19 波核對：guide 現行 L483、L674 已是新指向"` | `pending_handoffs.py list` 看到 6 筆新單、H-fc0960 已結案 |
| 8 | 主 session | — | `build_web.py`（錨點 WARN 不增加）→ `run_tests.py`；兩支都綠才 commit，只 add 第 0 步宣告的路徑加上 `data/pending-handoffs.jsonl` | exit 0 |
| 9 | 主 session | `wiki/log.md`、ledger | Query 條目寫三條使用者裁決＋本波改動；ledger 記第 19 波一列，附「頁內 `](#…)` 錨點無閘看守」與 R-1 新發現（官方三頁說法不一） | append-only |
| 10 | 評審（我） | — | 實作複核：照本檔逐條對照，四題路徑重走 | 複核報告 |

## 實作複核（2026-10-22）

方法：用工作區現檔（未 commit）和設計者的參考副本做 diff（都先去掉 CR），再在現檔上直接跑各支閘、讀 `git diff`，不靠實作者的回報。

**逐步對照**

| # | 判定 | 證據 |
|---|---|---|
| 0 | 照做 | `.claude/tree-claims/` 有本 session 的宣告檔 |
| 1 | 照做 | 現檔和副本的 diff 只剩本評審要求的改動和日期；frontmatter 沒動 |
| 2 | 照做 | 三處 `<實作當天>` 填成 2026-10-22（現 L35、L36、L42）；R-1（L76、L138–139、L572、L617）、R-2（L425）、R-3（L647、L655）、R-4（L417）、R-9（L466、L493、L518、L522）都逐字吻合本檔修法；總行數 674 |
| 3 | 照做 | 我重跑：讀者語言新增 0、字元上限新增 0、懸置標記 177（基線 165）／舊字樣 23、`anchors_js.py` 斷錨 0 |
| 4 | **偏離（接受）** | B-2 的「寫 CLAUDE.md→」被 `check_rules.py` 擋下，主 session 改成「寫專案指示檔→」。只動了規則檔裡的用詞，軸線清單和看守字串「不得改以開發領域」都還在；`check_rules.py` 全綠。pages.md 搜「格式表／官方涵蓋不到／「深入」／探索時常撞到／領域注意／部署→事故→償還」0 筆 |
| 5 | 照做 | frontmatter 沒動（diff 沒有這一區）；`git status` 只有第 0 步宣告的 5 個檔加帳本 |
| 6 | 照做 | index：D-1 插在 L26 之後；D-2 改指第 6、9 段；D-3 拿掉「六個入口＋明價」；D-4 鉤子換成使命 A |
| 7 | 照做 | 帳本新增 6 筆 open：H-f353a0（商業）、H-e8a985、H-8245fe（社群）、H-f80c1d（句尾含 R-5(a) 的 Explore 句）、H-7e836a、H-130d53（C-6）；H-fc0960 標 done，by 開發實務，result 有寫 |
| 8–9 | **尚未做** | `build_web.py`、`run_tests.py`、log、ledger 歸主 session，複核時還沒跑 |

**逐字抽驗（對 draft 加本評審的修法）**：A-19（L391 hook 三件事）✅、A-22 表格與「一次多少錢」那句（L412–421）✅、A-36（L538 一句話驗證階梯）✅、A-44（檔尾 `%% 拆頁評估` 那行）✅、A-42（L623–632 亮點節加上 `%%` 檢查日）✅。

**重算**：674 行、正文 646 行（`check_page_thickness`：「646 行｜評估 2026-10-22 不拆」）；頁內連結 34 個（15 個目標）、斷錨 0；懸置標記 177／基線 165，舊字樣 23。

**在頁面上重走四題**（從 index 進來）：
- Q1：index L26 → §1 L130–166：include／exclude、「每份 CLAUDE.md 目標 200 行以內」、錯兩次就寫進去；L138–139 三頁說法不一的分界寫成一句 ✅
- Q2：index L30 → 第 6 段 L450–453 的四級階梯（含「評估者不跑工具」）；從第 9 段進也有 L538 一句話版本 ✅
- Q3：index L32 → §5 L412–421：四個入口、每個入口的方案與付費方式、Code Review 限 Team／Enterprise 且沒有單價、試跑估法、$13／活躍日 ✅
- Q4：index L27（新列）→ §3 L342–352：「一句話講得完就跳過 plan」、改多個檔才規劃 ✅

**結論：放行**，前提是主 session 跑完第 8、9 步，且 `build_web.py` 的錨點 WARN 不增加、`run_tests.py` exit 0。沒有需要實作者再修的地方。
