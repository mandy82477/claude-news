# 第 21 波評審複核：實作 `3a96d6b`（2026-11-02）

> 接手原評審（容器重啟），上一輪是 `claude-code-2026-11-01-review.md`。我只讀 git、跑閘，只寫了這一個檔。暫存腳本與輸出放在 `<scratchpad>/w21/recheck/`。
> **複核中途 HEAD 往前走了**：`7473eec`（gen 重算）、`73d6701`／`5ea1940`（web rebuild）、`0b81a10`（冷讀者複驗修正：features hooks 結論、index 加一列）。下面的「實作」指 `3a96d6b`，「HEAD」指 `5ea1940`。
> 我跑了 `build_web.py`，工作樹因此多出 3 個只有建置戳記的 diff：`web_reader/{data/data.js,index.html,sw.js}`，`?v=` 從 1793587204 變 1793587293。我沒有還原，因為還原算 git 寫入。

## 逐步表（review.md L120–133）

| 步 | 判定 | 證據 |
|---|---|---|
| 1 | 照做，做法有偏離 | `D/` 沒有換成 `R/rerun/`（`cmp` 不同，`D/verify2.py` 不存在），改用 `R/rerun/out` 直接出檔。四頁加 archive 的正文和 `R/rerun/out` 逐字相同，`diff` 只差 frontmatter。M 202／AR 362 和預期相同。K 463、R 287、F 266 各比預期少 1–2 行，也來自 frontmatter：gen 不寫 `matrix_role` 等欄位 |
| 2 | 大半漏做（偏離範圍比已知的大） | 步驟裡的 grep 有 6 處命中（draft L344「78 列」、L447「96 列」；map L4、L26；proposal L47「R 2…31」、L92「30→31」）。另外還有幾處沒改：proposal L22／L103 仍寫 N2「17／10」；L73 還列 H-1458cf／H-6e641e 要結；L86 可行性前提仍寫雲端跑「cell 基線 `--rebuild --allow-grow`」；draft L649 仍是舊的 R 規則（2.1.313 掛 🔎）；draft 也沒有 🔴1 的核句。**規則檔都做了**：`features/pages.md` L140 有縮行前核句，L190 是 🔴4 新條文。見發現 4 |
| 3 | 照做 | `git log ae4ce48..3a96d6b^` 加上八條路徑，結果為空。`orig_1234.md`、`orig_archive.md` 和 `3a96d6b^` 的檔 `cmp` 相同。另外，review 第 3 步寫的 `wiki/entities/anthropic-agent-stack.md` 路徑是錯的，應為 `topics/`；我用 `topics/` 重跑過 |
| 4 | 照做，有兩處已知偏離 | `verify2.py <repo> orig_1234 orig_archive <repo>/wiki/entities` 印出 `OK　照搬 925 行逐字、懸置 30→30`。cowork L37、L52、L78、L97 指 K（L52、L78 有帶 `#已知問題`）；claude-tag L45 指 `releases#最新版本`；claude-skills L81 指 F「桌面版文件時序」；agent-stack L90 是新子條列。兩處偏離都說得通：feature-radar L52 現在 197 字元，加錨點會超過 200；agent-stack L89 現在 192 字元 |
| 5 | 照做 | `check_rules.py` 全綠（實作與 HEAD 都綠）。sweeps `## 5a` 第 6 條在 L38，接在原第 5 條之後（🟡6）。safety-policy、models、community、commercial、classification、shared-when 都有改 |
| 6 | 照做 | `check_hierarchy` ✅ 31 個母頁。index L51 的投影列出三個子頁加 mods |
| 7 | 照做 | `pending-marker-count.json` count 212，note 和 🟡5 逐字相同。拿 `3a96d6b^` 和 `3a96d6b` 的 fingerprint 集合相減：added 28／removed 22 |
| 8 | 照做 | `pending-handoffs.jsonl` L357–368：開 8 筆；H-7b713f、H-433341 同 commit 結案；結 H-7526b2；另開 H-afee03。H-26cfb1 的措辭照 🟡3。`check_log_handoffs` 綠（46 行）。log 有 Query 條目，單號齊全 |
| 9 | 實作時照做；HEAD 上不成立 | 實作版：hierarchy ✅；pending ✅；freshness `OK…134 頁`；build_web `斷鏈 WARN 23／錨點 WARN 0`；cell `FAIL…107 筆`；reader `FAIL…2 筆`（K L281、R L236）。**HEAD 的 reader 是 3 筆**，見發現 1 |
| 10 | 照做 | `baseline-moves.md` 有 107 列。拿它的（頁:行）和 cell 閘輸出排序後 `diff`，結果完全相同（K 86／R 15／F 6），「配不回 0」。reader 那一段寫了 #22–#24 的改法，也寫了不要跑 `--write-baseline` |
| 11 | 照做，只漏 ledger | `data/cell-limit-baseline.json`、`reader-language-allow.json` 都沒動（allow 的 L142／148／154 仍是 `entities/claude-code`）。殘留的改動都已由 `7473eec`／`73d6701` 收掉。commit 裡**沒有 `ledger.md`** |
| 12 | 漏做 | ledger L58 的第 21 波列還是「進行中…健檢卡、冷讀者、主編查證已交」，沒有定稿列 |

## 抽驗：新文字對 verified 一手

- **stable 2.1.309**：母頁 L80、R L48 都寫「stable＝2.1.309、latest＝2.1.316，查證 2026-11-01」，R L48 另寫「差 7 個版號」。對得上 verified #1。
- **2.1.309 rm 拒絕只限 Desktop／VS Code**：R L49、L79 都寫了適用範圍。對得上 #2。
- **2.1.316 fast mode**：R L42 寫「10-30 起棄用、11-30 移除，不會自動改用別的模型，請求直接回錯誤」；R L70 版本列；母頁 L81 寫該不該升。對得上 #3 和 Q2。
- **2.1.313**：R L66 和 🔴4 規定的句子逐字相同，沒有掛 🔎。
- **hooks 結論三子條**：實作版 F L170–173 和 #8 一致（擋得硬／不一定觸發／allow 蓋不過 deny＋`tool.check` 例外）。HEAD 上已被 `0b81a10` 改動，見發現 2。
- **subagent 平行分派**：F L48、L177 寫「預設在背景跑、同時最多 20 個、`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調、fork 共用 context」。對得上 #9 和 Q4。
- **行數**：wc 是母 202／K 463／R 287／F 267（HEAD）／AR 362。正文 `body_lines` 是 173／434／260／240（HEAD 的 F 比實作多 1 行）。母頁 ≤300、子頁 ≤600，都在限內。

## 發現（每條附可貼上的修法）

**🔴1 HEAD 上 reader-language 多紅了一筆，不是搬家造成的，超出使用者批准的「只准 2 筆」。** `0b81a10` 加的 index L34「要平行分派工作該選哪種」裡含「派工」，`check_reader_language.py` 判 `index.md:34 [派工]`，所以總數變 3 筆。
修法：index L34 換成
`| subagent 有哪幾種型別、要同時派出好幾個時該選哪種 | [[entities/claude-code-features#Subagent 型別差異對照]] |`
改完重跑，應回到 `FAIL…2 筆`（只剩 K L281、R L236）。

**🔴2 HEAD 上 F 頁的 hooks 結論，摘要和本文說法相反。** `0b81a10` 把 F L171 改成「要保證一定擋，用沙箱；deny 規則……可能漏掉……hook 與 deny 規則都當第二層」。但 F L47 摘要和母頁 L173 的殼仍寫「用 deny 規則或沙箱」。冷讀者 Q3 從母頁進來，拿到的會是舊說法。
推論：commit 訊息寫的是「改以沙箱為保證」，所以以 L171 為準。修法：
- F L47：`- **hook 能不能當防線**：hook 一觸發就是硬擋，但不保證會觸發；要保證一定擋，用沙箱，deny 規則與 hook 都當第二層（見 [[#hooks：事件、失效模式與能不能當防線]]）。`
- 母頁 L173 的「要保證一定擋，用 deny 規則或沙箱。」換成：`要保證一定擋，用沙箱；deny 規則比對指令文字、換個寫法可能漏，和 hook 一樣只當第二層。`
- 另外：verified #8 和 Q3 的一句答案仍寫「deny 規則或沙箱」。主編要在 verified 末尾補一行，說明這次改判的依據（`topics/ai-agent-safety`「deny-list 也不是」）。

**🟡3 第 12 步漏做：ledger 沒有定稿列。** 修法：把 ledger L58 的「進行中（…）。健檢卡、冷讀者、主編查證已交」換成
`定稿（主 session 代判七點＋N1–N5，使用者裁兩題）：拆成母頁＋三子頁 known-issues／releases／features，正文 173／434／260／239；N1 退場 82 列（R 留 107＋2＝109 列）；N2 🛡️ 舊 16／11、新 17／11（L269 留全文）；懸置 30→30；實作 3a96d6b。**併 master 前提**：使用者本機跑 cell --rebuild --allow-grow 與 reader 白名單三筆改 page（見 claude-code-2026-11-01-baseline-moves.md）`
產物欄補上 `-proposal{,-map}.md、-draft.md、-review{,-recheck}.md、-baseline-moves.md`。

**🟡4 第 2 步的偏離範圍比已知的大：不只數字，文件裡的治理句也沒回寫。** 最危險的是 proposal L86 的可行性前提：照它做，會在雲端跑 `--rebuild --allow-grow`，被 H6 擋下。規則檔和頁面都已經對了，所以只需要止血。修法：在 proposal、proposal-map、draft 三檔的第 1 行下方各插一行
`> **第二輪未回寫本檔**：數字、🔴1–5 與治理步驟以 [claude-code-2026-11-01-review.md](claude-code-2026-11-01-review.md)、實作 commit 3a96d6b 與 `.claude/reporter-rules/features/pages.md` 為準；本檔的 96 列、78 列、17／10、R 2、30→31、2.1.313 🔎、雲端 --rebuild 皆已作廢。`

**🟡5 H-7b713f 的結案文字和實際改動對不上。** 帳本 L366 寫「L28／L52／L467 改指 claude-code-releases#最新版本」，但 feature-radar L52 實際寫的是 `[[entities/claude-code-releases]]`，沒有錨點（已知偏離）。帳本是 append-only，不改。修法：在發現 3 的定稿列末尾補一句 `feature-radar L52 為守 200 字元上限改指 releases 頁不帶錨點（H-7b713f result 所寫錨點不確）`。

**🟡6 F 頁 frontmatter 的 `signal: "孤島"`（inbound_links 2）。** 現在不用動手。H-02df2d（coding-workflow-guide L393）和 H-0fd390（ai-agent-safety L78）執行後，F 會多兩條入邊。第一週回訪時再核一次。

## 放行

- **`3a96d6b` 本身：放行。** 925 行逐字核對、懸置 30→30、107 筆搬家清單和閘輸出逐筆相符，reader 2 筆。紅的只有使用者批准的那兩道閘，其餘閘全綠。
- **分支 HEAD 要先修 🔴1、🔴2 才放行。** 🔴1 讓 reader 閘出現批准範圍外的第 3 筆；🔴2 讓 Q3 的入口和本文給出不同答案。兩條都是一行就能改完。改完重跑 `check_reader_language.py`（應為 2 筆）和 `check_cell_limits.py`（應為 107 筆）。🟡3–5 可以併進同一個 commit。
