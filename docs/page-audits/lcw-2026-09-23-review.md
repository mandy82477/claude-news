# 第 16 波評審：topics/community-large-codebase-workflow

對象：提案三件（磁碟現行檔，對象頁 186 行）。行號：對象頁＝原始行號；draft＝`lcw-2026-09-23-draft.md` 行號；規則檔＝原始行號。機械項全部自跑（scratchpad 依 draft A 區重建整頁＋整份 `wiki/` 副本；wiki 與規則檔未寫入；未執行任何 git）。
前提照主 session 裁決（不拆、不砍整節、不併、不新增頁；每線加官方句；guide L287 一句分界＋轉知；⟨Q-01⟩⟨Q-03⟩ 併筆；跨維護者只走 `pending_handoffs.py`）。
判定：**🔴 4 條、🟡 7 條**。結論：**放行進實作，但 4 條 🔴 的修法要併進實作單**（本檔末節已併好，實作者只照末節做）。

---

## 〇、代判數字重算

| 提案宣稱 | 我算的 | 判定 |
|---|---|---|
| 186 → 195 行 | 依 draft A-1～A-9 套回原檔：**195** | ✅ |
| 四線 22／24／23／22（原 21／23／23／21） | 標題到「為什麼會這樣」含頭尾：改後 **22／24／23／22**、原 **21／23／23／21** | ✅ |
| 「現在的答案」條數 | 改後 線 1／2／4＝官方 1＋社群 3，線 3＝官方 1＋社群 2 | ✅（需 B-1 先落地，否則違反現行 `weekly.md:89`「≤3 條」） |
| 代表實作 ≤3、證據五值 28/28（原 23/28、21/28） | 腳本逐格：改後 **28/28、28/28**；原 **23/28、21/28**，違規格與健檢卡第 3 節同 | ✅ |
| cell／reader／tools_page 皆 0／0／`[]` | 對副本直呼 `scan()`／`check()`／`check_spokes()`：**0／0／`[]`／`[]`** | ✅ |
| 懸置 119→119、本頁 `iter_pending` 0、`iter_legacy` 1→0 | 副本跑 `check_pending_markers.check()`：**119（基線 106）**、舊字樣 **40（基線 42）** 前後不變；本頁 `iter_legacy` 改前 **[L171]**、改後 **[]**，L171 被 `actionable()` 豁免故全庫不動 | ✅（`pending_markers.py:46–48` SHORT_RE 要 ❓／🔎 前綴，本頁三個 ⟨Q-nn⟩ 皆無，讀碼確認） |
| 去向表：一行不憑空消失 | 抽驗 6 段（見第五節），**1 處對不上**：L93「讀取上限」 | ❌（🔴-4） |
| `review-registry.json` 不咬 B 區 | 列出所有 files 含 `community/weekly.md`／`daily.md` 的 6 條 `all_contain`，把 B-1～B-6 套進副本後 11 個 pattern **全命中** | ✅ |
| 147 subagent 漏收根因是窗口 | patterns L709 節點日 09-04、L710 `**主線：** 並行規模`——**tag 是對的**，漏在窗口（重寫日 09-03／09-12 取自健檢卡 git 證據，本評審未跑 git 覆核） | ✅ 窗口；但新窗口仍有洞（🔴-1） |

---

## 一、明天的維護者

### 🔴-1 B-3 把撈料窗改成「最後更新日之後」，本波實作當天就會重演 147 漏收

本波實作把「最後更新」改成實作當天（draft L18），卻刻意不收 09-20／09-22 三則帶 tag 節點（proposal §2 第 4 條：Foremerge、Chief of Staff、aoci-code「是下次週更的正常料」）。下次週更照 B-3 取「最後更新之後」＝09-23 之後——三則全漏，正是 147 的同一個洞。「最後更新」還會被非週更的修改推動（第 15 波 09-22 改 L63 即一例，健檢卡 7(2)#9）。「最後新聞更新」也不能當錨：`shared.md:39` 規定它填「帶來新內容的那天」，不是「收到哪一則節點」。
**修法**：水位記在頁上的 `%%` 維運備忘，撈料從水位往前退 3 天。
(a) draft L185（A-9 的 `%%` 行）整行換成：
```
%% 週更撈料：patterns 節點以 `**主線：**` 欄位標記所屬線（規則：.claude/reporter-rules/community/daily.md「主線 tag 規則」、weekly.md「週更整線重寫」）；週更已收至 2026-09-16 %%
```
(b) draft L213（B-3，取代 `weekly.md:83`）整條換成：
```
1. **撈料**：`Grep "\*\*主線：\*\* [^—]" wiki/topics/community-tech-patterns.md`，取節點標題日期不早於本頁 `%%` 維運備忘「週更已收至 YYYY-MM-DD」前 3 天的帶 tag 節點（日報晚 26–30 小時，節點會晚到；名字已在本頁的跳過）——不用固定 7 天窗，也不用「最後更新」（非週更的修改也會推動它）；另掃同期填 `—` 的節點，照 `.claude/reporter-rules/community/daily.md`「主線 tag 規則」的判準與反例重判一次。代表實作的名字與數字若已不在 patterns 本體（月度封存搬走），去 [[topics/community-tech-patterns-archive]] 找
```
(c) 新增 B-7：`weekly.md:111` 整條換成：
```
5. 更新「最後更新」「最後新聞更新」，並把本頁 `%%` 內「週更已收至」改成本次收進的最新節點日期；本週零新節點且結論未變 → 不動頁面
```
與現行 `weekly.md:83`「近 7 天（補跑時取上次更新日以來）」的關係：**取代，不矛盾**——舊句的補跑分支本來就是「從上次收到的地方接著撈」，新句把它變成唯一路徑、並把「上次」從會漂的日期換成專用水位。

### 🟡-1 B-1 沒寫「官方句從哪來、官方沒有時怎麼寫」，下一個社群記者沒法照做

社群記者週更時不做官方查證；B-1 只寫「官方逐字只用已查證的句子」，沒說去哪拿、庫內沒家怎麼辦（本波線 1／線 2 就靠直連官方文件＋C-2／C-3 轉知）。
**修法**：draft L201（B-1）整行換成：
```
   **現在的答案**            ← 首條「**官方已給**：…」只轉述 [[topics/anthropic-agent-stack]]／[[topics/coding-workflow-guide]] 已寫的官方零件，連頁不連錨；庫內沒有時才直連官方文件並開轉知請功能記者收，收進後改回指頁；官方確實沒有對應零件就寫「**官方已給**：無」；其後 ≤ 3 條社群可執行結論
```

### 🟡-2 B-6 反例的「才填 `—`」讀起來像所有非計費工具都歸並行

draft L247 後半「只解計費、裝置存取或單一 agent 使用體驗的**才**填 `—`」脫離前半的多 agent 語境，會把 Skill 類、格式類節點也推進並行線。與 `daily.md:71`「大型 codebase 特有」判準不矛盾，但要鎖範圍。
**修法**：draft L247 整條換成：
```
- 容易誤判成 `—` 的反例：多 agent 協作、編排、互相傳訊、commit 落地排序的工具，即使不限 monorepo 也填「並行規模」——大 repo 最先撞到的就是這一面牆；同屬多 agent 類、但只解計費、裝置存取或單一 agent 使用體驗的，仍填 `—`
```

### 🟡-3 已誤填 `—` 的五則並行節點沒有人會再看

新窗口只往後撈，健檢卡第 4 節點名的 pstack（patterns L220）、orca（L401）、ccteam（L465）、agent-orchestrator（L510）、09-09 六款 Show HN（L537）——五則我逐一確認 `**主線：** —`——永遠落在水位之前。本波不改 patterns（一次一頁），但要留下待辦。
**修法**：`wiki/log.md` 本波條目加一句：`patterns L220／L401／L465／L510／L537 五則多 agent 工具依新判準（daily.md 反例）應改標並行規模，下次週更一次性重判並收進線 1。`

---

## 二、機器

### 🔴-2 C-5 會直接被腳本拒絕：`--from 社群 --to 社群`

`pending_handoffs.py:77–78`：`if src == dst: raise SystemExit("from 與 to 相同——同記者的待辦不是轉知，寫進頁面或 log 即可")`。cqd 是社群記者自己的頁（`community/daily.md:15`），C-5 照抄就中斷實作單第 5 步。C-5 的 note 還寫「主線頁現改指官方 /context（經 guide）」，在 🔴-3 修掉後也不成立。
**修法**：刪掉 draft L280–L284 整個 C-5，改在 draft L288「同維護者、本波不改」那段末尾加：
```
`topics/code-quality-decline` 與 `topics/community-tech-discussions` 的分界（冷讀者分不出：discussions L67／L77「已確認根因不在模型退步」vs cqd L113–L118「三種解釋都排除不掉」、L157 沒說差在哪）——主線頁線 2 已分流成「同一 session 越跑越笨→discussions，換版本後變差→cqd」；cqd L78 🧰 把「先量 context 組成」送回主線頁線 2，下次 cqd 策展時兩頁各補一句讀者看得到的分界，並處理 L78 的回送。
```

### 🟡-4 實作單第 1 步的驗收會誤紅

draft L297「全頁 grep『沉澱』＝0（`%%` 內除外）」——frontmatter L8 `update_freq` 仍含「沉澱」，要到第 4 步 `gen_wiki_frontmatter.py` 才重產。**修法**：驗收改成「L27 以下 grep『沉澱』『節點』『本輪』＝0（`%%` 行除外）」，frontmatter 在跑完 `gen_wiki_frontmatter.py` 後再驗一次。（已寫進末節實作單。）

---

## 三、冷讀者

### 🔴-3 線 2 首條把 `/context` 指向 guide，guide 沒有這句

draft L82「`/context` 看得到啟動時載入了什麼……——見 [[topics/coding-workflow-guide]]」。實核 guide：`/context` 全頁只出現在 L508「`/context` 的 Skills 列」一個詞；設計者自己的 C-2（draft L265）也寫「全站沒有任何一頁寫 session 變笨先打 /context」。verified §三 Q2 明寫 context-window 文件「本波未逐字抓」——這句同時違反「只取已錨句」與「不指向空處」。讀者照指路去 guide，找不到。
**修法**：draft L82 整行換成（`--bare` 與讀取上限都有錨：verified §一-4、guide L287）：
```
- **官方已給**：腳本或 SDK 呼叫加 `--bare`，跳過 hooks、skills、MCP server、auto memory、CLAUDE.md 等自動載入（[官方文件](https://code.claude.com/docs/en/headless)）；單次讀取量官方也已設上限——見 [[topics/coding-workflow-guide]]
```
`/context` 等 C-2 收進 guide 後，下次週更再照 B-1 補指路。

### 🔴-4 「讀取上限」從子問題表也被刪了，L163 卻說「兩條只留在子問題表」

原 L93「預先 @-mention 定為反模式；**讀取上限＋**索引層；…」在 draft L93 變成「…反模式；索引層；…」，去向表 L153 寫「讀取上限拿掉（同 L83）」。但 draft L157（新 L163）說兩條「只留在子問題表」——對「已否決方案」成立（新 L128 留著），對「讀取上限」不成立，同一頁自己打自己。
**偏離判定（必審項）**：主 session 代判是「一句分界寫明」，設計者多做了「從『現在的答案』拿下」。**拿下這一步我判對，但理由要換**：不是「guide 不推薦所以拿下」（那會違反本頁「記社群走到哪」的分界），而是兩條在社群這邊本來就撐不起可執行結論——否決方案索引證據強度是「推論」（L126：兩則概念觀察、無工具），讀取上限在社群是 issue 要求放寬而非做法（guide L287）。表格列必須留著，那是「做到哪」的事實。
**修法**：
(a) draft L93 的「預先 @-mention 定為反模式；索引層；」改回「預先 @-mention 定為反模式；讀取上限＋索引層；」（剝連結後該格 95 字元，上限 120，實測閘 0 命中）。
(b) draft L157 整條換成：
```
- **與官方做法頁說法不同的兩處**：[[topics/coding-workflow-guide]] 不再推薦「自己加讀取上限」（官方已內建上限）與「已否決方案索引」（對應官方 issue 已關閉、零回應）；分界是那頁只收官方機制撐得起的做法、本頁記社群走到哪。社群這兩條也只到個別做法與概念觀察，撐不起可執行結論，所以只留在子問題表。
```
(c) 去向表 L145 與 L153 的「互斥句併入 L163」改為「現在的答案拿下（證據撐不起可執行結論）；子問題表列留；分界句在 L163」。

### 🟡-5 callout 把「要 Claude 出示證據」算成「官方內建」

draft L28「……要 Claude 出示證據才算做完——這四件官方都已內建」。出示證據是官方建議的提示寫法（guide L528），不是內建功能；guide L536 也寫 `/goal` 抓不到 Claude 沒說出口的事，真正擋得住的是 Stop hook。不虛報優先。
**修法**：draft L28 整行換成：
```
> 每個 agent 一個 worktree、腳本呼叫加 `--bare`、跨 session 的 auto memory、用 Stop hook 擋住「說做完卻沒做」——四面牆官方都已給了零件；Claude Code 一個 session 預設最多同時跑 20 個 subagent，那是上限，不是「20 個都跑得穩」。四條線的「現在的答案」第一條因此都改成官方零件在哪，社群做法接在後面。
```

### 🟡-6 線 4 首條把 `/goal` 與 Stop hook 寫成可互換

draft L131「再用 `/goal` 或 Stop hook 把『做完沒』的裁決權從執行者手上拿走」——guide L536：「`/goal` 的評估者不跑工具……要真正閉環得靠 `Stop` hook」。
**修法**：draft L131 整行換成：
```
- **官方已給**：要 Claude 出示證據（測試輸出、跑過的指令）而不是宣稱完成；`/goal` 只看得到對話裡說過的話，要真的擋住得靠 Stop hook 跑檢查——見 [[topics/coding-workflow-guide]] 第 9 段
```

---

## 四、治理

### 🟡-7 A-1「最後新聞更新 2026-09-16」違反 `shared.md:39`，C-4 措辭可以更準

(1) `shared.md:39`：帶來新內容時「最後新聞更新」填當天；本波新收 147、hcom 與四條官方句，屬新內容。設計者用 09-16 是想拿它當撈料水位——那個工作已由 🔴-1 的 `%%` 水位接手。**修法**：draft L19 改成 `**最後新聞更新：** <實作當天>`。
(2) C-4：我 grep 核實 `claude-code.md:502`「新增 `--worktree` 旗標與 `claude agents` 視圖的 GitLab merge request URL 支援」vs `:821`（05-08 v2.1.133 已可控制 `--worktree`）——互斥屬實，但 L502 也可能只是斷句：新增的是「兩者的 GitLab MR URL 支援」。請對方確認哪一種，不預設是錯。**修法**：draft L277 的 `--note` 換成：
```
"L502 寫 v2.1.233（2026-08-14）『新增 --worktree 旗標與 claude agents 視圖的 GitLab merge request URL 支援』，同頁 L821 記 2026-05-08 v2.1.133 已可控制 --worktree、EnterWorktree。讀者讀成『8 月才新增 --worktree』而與 L821 互斥（第 16 波冷讀者『撐不起的句子』第 5 條）；也可能只是斷句（新增的是兩者的 GitLab MR URL 支援）。請對 v2.1.233 release note 原文核對是哪一種。"
```

**其餘轉知**：C-1～C-3 類別「社群→功能」都在 `CATEGORIES`（`pending_handoffs.py:37`），內容都是「請確認前提／缺這件官方事實、若收進則主線頁改指」——請對方確認事實，沒有要求照改 ✅；三個 page 參數都是功能記者的頁（`features/daily.md:15`、`:21`）✅。帳本 210 行 grep 無同題未結轉知 ✅。

---

## 五、必審項逐條

1. **官方句放第一條**：三線是官方＋3、線 3 是官方＋2（「已否決」拿下）。社群兩條（repo 即記憶、本地索引）足以回答「社群怎麼組」；≤3 契約要等 B-1 先落地（實作單第 0 步）。**逐句對 verified**：`--worktree`／`isolation: worktree`（§一-1、§三 Q1）✅、20 subagent 上限可調（§一-2）✅、Managed Agents 20（managed-agents L89）✅、fork 繼承＋同工具池、無「重送／累積」句（§一-3）✅、`--bare` 跳過清單＋建議模式（§一-4）✅、auto memory 200 行／25KB＋「context 不是強制設定」（§一-5、§三 Q3）✅、CLAUDE.md 分層同方向（§三 Q3）✅、71.6→89.7 與 arXiv（§二）✅；**`/context` 沒有錨** ❌（🔴-3）。**連頁不連錨**：四條首句都只連頁 ✅。**目標頁現在有沒有那句**：agent-stack L213 worktree 隔離 ✅、guide L253 sparsePaths ✅、L287 讀取上限 ✅、L195–L204 分層與 auto memory ✅、L528／L530／L536 證據、`/goal`、Stop hook ✅、managed-agents L89 ✅；guide 的 `/context` ❌。本頁不再把官方事實指向 claude-code（只剩 L188 版本紀錄）✅。
2. **guide L287 兩條**：判定見 🔴-4——拿下可以，理由改成「社群證據撐不起可執行結論」，表格列都要留；分界句仍是主 session 要的那一句。
3. **撈料窗**：取代不矛盾；147 的根因是窗口（tag 正確），hcom 等六則的根因是 tag 判準（B-6 管）——兩個洞兩條規則，設計者的拆法對；但新窗口本身有洞（🔴-1）。
4. **併筆與懸置計數**：讀碼與實跑都支持 119→119；主 session 的 118 不成立，設計者更正正確。
5. **五筆轉知**：C-5 不合法（🔴-2），C-4 措辭（🟡-7），C-1～C-3 合規。
6. **去向表抽驗**（逐字對 draft）：摘要表 L47／L50 改、L48／L49 原字不動 ✅；線 1 L59–L61→新 L60–L62、L65 的「創始人每晚數千」家在 boris-cherny L124–L128 ✅，L71 被移除的 HarnessFlow／opencodex／metaharness／claw-orchestrator 在 patterns 各 3–7 次命中 ✅；線 2 L93 ❌（🔴-4）；線 3 L111 拿下、L126→L128 留 ✅；目前結論 L159「第四個獨立實作」移除、L160→L188 ✅；懸置細節 L163–L171→L168–L174，L165「延續累積」反轉成「文件沒有累積句」與 verified §一-3 一致 ✅；相關實體 L182→L183 一字不改（`graph_gap_ignore.json:199` 依據）✅、L177 維運說明→L191 `%%` ✅；L186→L195 ✅。
7. **閘重跑**：見第〇節；四條 🔴 修法全數套進副本後重跑：cell **0**、reader **0**、`check()`／`check_spokes()` **`[]`／`[]`**、懸置 **119／基線 106**、舊字樣 **40／基線 42**、四線 **22／24／23／22**、28/28／28/28、**195 行**。
8. **內部用語**：套用後頁面 L27 以下逐字掃「節點／本輪／沉澱／tag／查證日／縫合／懸置」＝**0**（只剩 L191 `%%` 內）；「主線」只在 H1（L27，全站入邊顯示名）與摘要表表頭 L45；「推論」只作證據強度值與 L155「為什麼」原句。設計者自承的「節點」「本輪」閘漏，draft 裡已無殘留 ✅。
9. **規則檔**：B-1～B-6 與既有條文無矛盾（B-5 的 `:108` 順手修掉「目前收斂點」這個不存在的欄名 ✅）；registry 6 條 all_contain 套改後全綠（第〇節）；`check_rules.py` 內部呼叫 git，本評審未跑，留給實作者第 0 步。

---

## 照順序執行（實作單；實作者不必看提案）

0. 改 `.claude/reporter-rules/community/weekly.md`：`:83` 換成本檔 🔴-1(b)；`:89` 換成本檔 🟡-1 那行；`:96` 段末接 draft L207；`:105` 換成 draft L219；`:106` 之後插入 draft L227–L229 三條；`:107` 換成 draft L235；`:108` 換成 draft L241；`:111` 換成本檔 🔴-1(c)。**由下往上改**，行號才不漂。驗：`grep -c "週更已收至" .claude/reporter-rules/community/weekly.md` ＝ 2、`grep -c "官方已給" …weekly.md` ≥ 2、`grep -c "近 7 天" …weekly.md` ＝ 0。
1. 改 `.claude/reporter-rules/community/daily.md`：`:71` 之後插入本檔 🟡-2 那條。驗：`grep -c "容易誤判成" …daily.md` ＝ 1；跑 `python scripts/check_rules.py` 須綠。
2. 對象頁 `wiki/topics/community-large-codebase-workflow.md` 標頭：L31 換 draft L17；L33 換成 `**最後更新：** <實作當天>`；L34 換成 `**最後新聞更新：** <實作當天>`（🟡-7，**不是** 09-16）。
3. callout L36–L37：L36 換 draft L27；L37 換本檔 🟡-5 那行（日期填實作當天）。
4. 摘要：L43 換 draft L38；L47 換 draft L44；L50 換 draft L50；L45／L46／L48／L49 不動。
5. 線 1：L58–L74 換 draft L58–L75（18 行）；L56 標題、L76「為什麼」不動。
6. 線 2：L82–L100 換 draft L81–L100，**再做兩處**：首條換成本檔 🔴-3 那行；「按需取回」列的「反模式；索引層；」改成「反模式；讀取上限＋索引層；」。L80、L102 不動。
7. 線 3：L108–L126 換 draft L106–L124；L106、L128 不動。
8. 線 4：L134–L150 換 draft L130–L147，首條換成本檔 🟡-6 那行；L132、L152 不動。
9. 目前結論＋查過的數字：L158–L171 換 draft L155–L168，其中第三條（「與官方做法頁說法不同的兩處」）換成本檔 🔴-4(b) 那條。
10. 相關實體＋參考來源：L177–L186 換 draft L174–L189，其中 `%%` 行換成本檔 🔴-1(a) 那行。
11. 驗頁面：`wc -l` ＝ 195；四個 `### N.` 標題與改前逐字相同；四條 🧰 行七個「」症狀句與改前逐字相同；L27 以下 `grep -c "⟨Q-"` ＝ 0；L27 以下除 `%%` 行外 grep「沉澱」「節點」「本輪」「懸置」＝ 0；`grep -n "/context"` ＝ 0；`grep -c "讀取上限"` ＝ 2（按需取回列、目前結論第三條）。
12. 轉知：照抄 draft L259、L265、L271 三筆（C-1～C-3）；C-4 用 draft L277 但 `--note` 換成本檔 🟡-7(2)；**不開 C-5**。驗：`python scripts/pending_handoffs.py list --to 功能` 多出 4 筆。
13. `wiki/log.md` 新增一筆本波條目，含：⟨Q-01⟩⟨Q-03⟩ 併筆與三個短標記改普通條列（懸置 119 不變）；147 subagent、hcom 補進線 1；四處跨頁數字改指 tools／trends；兩條「現在的答案」拿下的理由（🔴-4 措辭）；本檔 🔴-2 那段 cqd／discussions 同維護者待辦；本檔 🟡-3 五則待重判；draft L288 tools／trends 同維護者待辦；`claude-code:197` 的 🔎 與新措辭一致。
14. 主編自理：`wiki/index.md:102` 本頁那列「節點證據」改「每個做法的證據」。
15. 跑閘（依序，每支 exit 0）：`python scripts/check_tools_page.py` → `python scripts/check_cell_limits.py --page topics/community-large-codebase-workflow` → `python scripts/check_reader_language.py --page topics/community-large-codebase-workflow` → `python scripts/check_pending_markers.py`（須 119 筆、基線 106）→ `python scripts/gen_wiki_frontmatter.py`（之後驗 frontmatter `update_freq` 不含「沉澱」）→ `python scripts/check_hierarchy.py` → `python scripts/check_rules.py` → `python scripts/build_web.py` → `python scripts/run_tests.py`。**每支的最後一行原樣抄進回報。**

我在 scratchpad 對「draft＋本檔四條 🔴 修法」副本跑前四支的等價函式，結果（前四支預期最後一行）：
```
狀態：✅ 數字皆帶日期、首選皆唯一、全站 🧰 spoke 症狀句對帳通過
OK: 字元上限機械閘 — 無新增超限
OK: 讀者語言閘 — 無新增命中
狀態：✅ 懸置標記語法檢查通過
```

---

## 實作複核（2026-09-23）

以磁碟現行檔為準（未 commit）。對照 draft L300–L325「實作單（最終版）」16 步（0–15）。git 只用了唯讀的 `git diff`／`git show HEAD:`（協調者指定）。**結論：放行**。16 步都照做，沒有偏離；只有 1 條 log 措辭建議 commit 前順手改（見「最後一批」）。另更正本檔前文：🔴-1(c) 我寫的 `weekly.md:111` 是錯的，實際是 `:110`（`:109` 是第 4 步、`:111` 是空行）。設計者在 draft L248 已更正，實作者照 `:110` 做，對。

### 逐步對照

| 步 | 判 | 證據 |
|---|---|---|
| 0 weekly.md B-1～B-5、B-7 | 照做 | 用 `git show HEAD:` 取改前檔，照 draft B 區由下往上重套，與磁碟檔**整份逐行相同**（171 行＝171 行，CRLF 正規化後比對）。git diff 區塊落在 `:83`、`:89`、`:96`、`:105`、`:107–:111`（插入 3 條＋換 2 條）、`:110→:113`，位置全對。`週更已收至` 2 處、`近 7 天` 0 處 |
| 1 daily.md B-6 | 照做 | 同法重套後整份相同；diff 只有 `@@ -71,0 +72 @@` 一行插入（判準那條之後） |
| 2 標頭 | 照做 | L31／L33／L34＝A-1；`**最後新聞更新：** 2026-09-23`（不是 09-16） |
| 3 callout | 照做 | L36–L37 與 A-2 逐字相同（Stop hook 版） |
| 4 摘要 | 照做 | L43／L47／L50 換掉，L45／L46／L48／L49 原字不動 |
| 5–8 四線 | 照做 | 由 HEAD 原檔套 draft A-4～A-7 fence 內文，建出的期望檔與磁碟檔從 L27 起**逐行 0 差異**（expected 195 行＝disk 195 行） |
| 9 目前結論＋查過的數字 | 照做 | 同上 0 差異；第三條是 🔴-4(b) 版 |
| 10 相關實體＋參考來源 | 照做 | 同上 0 差異；`%%` 行帶「週更已收至 2026-09-16」 |
| 11 驗頁面 | 照做 | `wc -l`＝195；`⟨Q-` 0 處、`/context` 0 處、`讀取上限` 2 處、`週更已收至` 1 處；四個標題與七句症狀句 0 差異（spoke 閘綠） |
| 12 轉知 4 筆 | 照做 | `pending-handoffs.jsonl` 新增 4 列：H-c63724、H-90ad60（guide）、H-fc5914（agent-stack）、H-f91933（claude-code）。把 draft C-1～C-4 用 shlex 解析後比對 from／to／page／note 四欄，**4/4 逐字相符**；沒開 C-5 |
| 13 log | 照做（1 處措辭，見最後一批） | `wiki/log.md:6720` 是末則，列項齊全：併筆＋119 更正、147／hcom、四處跨頁數字、兩條拿下的理由（證據撐不起、表列留）、同維護者待辦（tools L213、trends L37／L99、**cqd／discussions 分界與 L78 回送**、patterns 五則待重判）、`claude-code:197`、4 個轉知 id |
| 14 index | 照做 | `index.md:102` 只有「節點證據」→「每個做法的證據」這一處改動 |
| 15 閘＋重產 | 照做 | 見下；frontmatter `update_freq` 已重產為「每週策展一次」 |

### 抽驗

- **(a) 四線逐字，以及自承誤刪又補回的兩段**：四線各層都與 draft 相同（見上表 5–8 步）。線 1、線 2 的「為什麼會這樣」：`git diff -U0` 對本頁的輸出裡**沒有任何含「為什麼會這樣」的行**，淨差異為零。另拿 HEAD 的 L76／L102 和磁碟的 L77／L104 直接 diff，逐字相同；線 3、線 4（HEAD L128／L152 對磁碟 L130／L155）也相同。
- **(b) 行數**：兩個數字是同一頁用兩種口徑量的。設計者口徑（`### N.` 到「為什麼會這樣」，含頭尾）是 **22／24／23／22**。實作者口徑（`### N.` 到分隔線 `---`，含中間空行與 `---`）是 **24／26／25／24**，我重算兩種都對得上。契約 `weekly.md:86`「每條線固定四層、≤30 行」說的是四層本體，應該用設計者口徑。用哪種口徑都在 30 以內，**契約守住**。
- **(c) 規則檔位置**：B-3 在 `:83`；B-7 在原 `:110`，插入 3 條後位移到 `:113`，是「5. 更新…」那一步本身，不是空行。見第 0 步。
- **(d) 水位**：「週更已收至 2026-09-16」只出現在 L191 的 `%%` 行，正文 0 處。`web_reader/data/wiki/community-large-codebase-workflow.json`、`data.js`、`search-index.json` 都沒有這串字，也沒有 `%%`，網站版確實剝掉了。
- **(e)–(g)**：見上表第 12、13、14 步。
- **(h) 內部用語**：正文 L27–L195（排除 `%%` 行）逐字掃「節點／本輪／沉澱／懸置／查證日／縫合／tag／⟨Q-／今日／第 N 波／佐證／覆核」，**0 命中**。

### `gen_wiki_frontmatter.py`／`build_web.py`：在實作單內（第 15 步），沒有不該有的副作用

- **wiki**：104 個變動檔中，只有 3 檔的正文有改（本頁、`index.md`、`log.md`），都在計畫內。其餘 101 檔只改了 frontmatter：`days_since_news`／`days_since_news_subtree`（跨日重算）、`pending_overdue`／`pending_next_review`（6 頁，到期日跨日）、`signal`（1 頁，跨日）、`inbound_links`（11 頁）。
- **`inbound_links` 的增減都能由本頁出邊的變化解釋**：
  - claude-code −2：原本三處連結，現在剩一處。
  - managed-agents −1。
  - agent-stack +2、guide +6、patterns-archive +3、cqd +2、tools +2。
  - OCG、llm-wiki-pattern、discussions、patterns 各 +1。
- **web_reader**：8 檔是 build_web 的正常產物。有一處要知道：`digest/2026-09-13.json` 的「今日 wiki 動態」拿掉了本頁。原因是 `build_web.py:555–559` 的 `sedimentedToday` 用頁面**現行**的 `lastNewsUpdate` 比對日期，本頁從 09-13 改成 09-23 後就從舊日期消失。這是這支腳本本來的設計，每頁每次更新都會這樣，也是 `shared.md:39` 要求的結果，**不是本波的缺陷，不處理**。
- **`.claude/.last-rules-check`** 沒出現在 `git status`。

### 七道閘（我自己重跑；每支 exit 0，最後一行原樣抄）

```
狀態：✅ 數字皆帶日期、首選皆唯一、全站 🧰 spoke 症狀句對帳通過      （check_tools_page.py）
OK: 字元上限機械閘 — 無新增超限                                      （存量基線內 0 筆）
OK: 讀者語言閘 — 無新增命中                                          （存量基線內 0 筆）
狀態：✅ 懸置標記語法檢查通過                                         （119 筆／基線 106；舊字樣 40／基線 42）
狀態：✅ 全部確定性檢查通過                                           （check_rules.py）
狀態：✅ 通過（29 個母頁）                                            （check_hierarchy.py）
OK: CSS 覆寫閘 — 1 個檔無新增死媒體查詢（存量 9 筆、簡寫提示 0 筆）   （run_tests.py，exit 0）
```

### 最後一批（1 條，commit 前順手改，不擋放行）

1. **`wiki/log.md:6727` 用引號包了一句頁面上沒有的話**。它寫本頁新措辭是「fork 子代理繼承父對話，官方沒給累積速度數字」，但頁上並沒有這句。log commit 後就不再改，引號內必須是原句。**修法**：把該行的 `（「fork 子代理繼承父對話，官方沒給累積速度數字」）` 換成 `（L101「fork 子代理繼承父對話（官方證實）；社群回報四個平行子代理耗約 200 萬 token，官方沒給數字」）`。
