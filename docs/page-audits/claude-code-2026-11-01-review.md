# 第 21 波評審：entities/claude-code 拆成母頁＋三子頁（2026-11-02）

> 審的對象：`claude-code-2026-11-01-proposal.md`、`-proposal-map.md`、`-draft.md`；上游健檢卡、冷讀者、verified；ledger 第 21 波兩條（L123 使用者裁決、L124 七點）＋N1–N5（主 session 預設照設計者，只重算）。
> 我的腳本與重跑產物在 `<scratchpad>/w21/review/`（下稱 `R/`；`<scratchpad>`＝`/tmp/claude-0/-home-user-claude-news/d15bcaea-1307-5c78-90dd-54d17b9ee243/scratchpad`），設計者的在 `w21/design/`（下稱 `D/`）。我沒改 `D/`、wiki、規則檔、腳本、基線，也沒跑 git 寫入指令（只讀：`git show`、`git diff`）。
> 行號：「舊 Lnnn」＝設計者用的 `ba9bf17` 版（1,231 行，`R/orig_1231.md`）；「新 Lnnn」＝現行 HEAD `ae4ce48`（1,234 行）。

## 結論

- 🔴 5 條、🟡 6 條。設計方向不用重開：切法、蒸餾、錨點去向、殼都成立。我把設計者的 `split_cc.py` 改成吃 1,234 行新檔，重跑了一次（`R/rerun/`）：新檔 1–1,234 行每行恰好消費一次，照搬的 925 行逐字核對通過，懸置 30→30。
- 11-01 的 ingest 併進來後，有兩件事一定會壞：K 頁的新鮮度閘會紅（🔴3）；設計者的 🔎 讓 2.1.313 有了第二個懸置家（🔴4）。
- N2 有一條判錯：L269 攝影機那條在安全頁的家，狀態比 K 舊，所以不能縮成一行（🔴1）。
- reader-language 那 2 筆不是基線的事，是白名單的事。提案寫的 `--write-baseline` 會把已經清到 0 的基線重新種回 2 筆（🔴5）。
- **放行條件**：設計者第二輪用 `R/rerun/` 的三個檔重出，並吃下 🔴1–5 的文件改動；🟡 能吃就吃。

## 自己重算的數字

| 項目 | 主 session／設計者 | 我重算 | 證據 |
|---|---|---|---|
| N1 退場列 | 82（04:2／05:20／06:30／07:30） | **82 屬實**。但留在 R 的不是 96 列，是 **107 列**；加上 v2.1.289、v2.1.269 兩列，R 表共 109 列。L712–900 共 189 列＝82＋107。今天（11-02）切線移到 08-04，仍是 82 列，因為沒有發布日落在 08-03 的列 | `R/n1n2.py`、`D/accounting.txt` L712–900 的 fate 計數 |
| N2 🛡️ 重疊／獨有 | 17／10 | **舊檔是 16／11，新檔是 17／11**。27 條裡 L269 要改回獨有（🔴1）。新檔多了 Cursor 一條，它重疊。新檔組頭是 19🔴／5✅／1⛔／3❓ | `R/rerun/out` 的 K 頁逐組實數 |
| 正文行 母／K／R／F | 173／432／260／239 | **173／434／260／239**。K 多的兩行是 Cursor 一行和 #37951 | `check_page_thickness.body_lines` 跑在 `R/tmp_after` |
| 懸置 | 30→31（+1＝2.1.313） | **30→30**：母 6／K 20／R 1／F 2／archive 1。去 slug 比對前後相等 | `R/rerun/verify2.py`。驗紅：刪 K 的 fsmonitor 標記＋#37951 → 兩處都抓到，exit 1 |
| `--rebuild-count` 預期 | — | count 212，added 28／removed 22。去 slug 後：減少 ∅；增加 6 筆，都是他頁 10-31／11-01 ingest 新加的（blackstone、jiahaoshao1、copilot fusion、edgar、hugging face、128 MB） | `R/` 模擬 `_do_rebuild` 差集 |
| cell 新增 | 107，全是搬家 | **107 筆全部配得回 `entities/claude-code` 舊基線**（同類型、同錨點、上限 ≥ 現長）：K 86／R 15／F 6。本機 `--rebuild --allow-grow` 預期 added 107／removed 181（都在舊頁名下）——這是用 `match()` 模擬的推論 | `R/moves.py` → `R/moves_cell.txt` |
| reader-language 2 | 基線以頁為鍵 | **其實是白名單**：`data/reader-language-allow.json` 的 #22、#23（「只談封存」，兩筆重複）、#24（「對話封存後完全消失」）page 都寫 `entities/claude-code`。改成 K、R 後，副本跑出 `OK: 讀者語言閘 — 無新增命中` | `R/tmp_after` 實測 |
| 其他閘（`R/tmp_after`，含 cowork／claude-tag 兩處） | — | hierarchy ✅ 31 母頁；pending ✅（新語法 212、舊字樣 20→18）；freshness 套 🔴3 後 OK 134 頁；build_web `斷鏈 WARN 23／錨點 WARN 0`、exit 0 | `R/*.txt`、`R/build.txt` |

**去向表抽驗**（拿 `R/rerun/out` 逐字核）：
- 開發者須知 L903–914：L909→R；L903、904、906–908、913、914→F；L905、911、912→母；L910 是改字行（F_SUBS），和 map 第 27 列一致。
- 歷史記錄 08 月：L1165–1188 共 24 列，全在 archive `## 2026-08`，R 裡 0 列重複；⟨Q-14⟩⟨Q-15⟩ 的 L1229–1231 也在同一節。
- 🌐 服務穩定性：K 剩 16 條，就是總數 1 行＋未解決 Status 6 條＋非 Status 9 條；archive 新節 41 條，就是 40 條＋L151。
- 桌面版文件時序：F 有 23 條。
四節都和 map 相符。

## 一、機器

**🔴2 設計者的腳本對新檔跑不起來；同一刀還有 11-01 的文字要換**（回答主 session 的 (a)(c)）
`D/split_cc.py` L22 寫死 `assert len(L) == 1231`。`git diff ba9bf17 HEAD -- wiki/entities/claude-code.md` 的 hunk 對應如下：
- 插入兩處：舊 L243 後插新 L244–245（Cursor 🛡️ 一條＋子條列），舊 L319 後插新 L322（#37951）。
- 原位改：frontmatter、L36、L38–40 callout、L235、L318 兩個組頭、L362、389、392、531、553、556。
所以位移是：舊 n ≤243 → n；244–319 → n+2；≥320 → n+3。我拿 `orig_1231.md` 對新檔逐行比過：位移後內容不同的行，恰好就是 frontmatter（L8、11、15、17、18）加上上列 12 行。這些原位改的行，原本的去向都是「K／母 原文」或「組頭重算」，所以新文字會自動流到正確的頁，行號不必重編。
修法：以 `R/rerun/split_cc.py`、`R/rerun/newtext.py` 取代 `D/` 同名檔（`diff` 只有下面這幾處）。
- `split_cc.py`：`ROOT` 改成必填參數；改讀新檔，assert 1,234；加 `o2n()` 與 `NEW_ONLY`；在 K 迴圈的 n==244 前插 `T.K_SHIELD_CURSOR`、n==320 前插新 L322 原文；結尾斷言「新檔 1–1,234 每行恰好一次」，`accounting.txt` 改用新行號。
- `newtext.py` 末尾加一段覆寫：
  - `M_CALLOUT`、`K_CALLOUT` 換成 11-01 的兩條（/buddy 進 K；Cursor 指 product-vulns#2026-10）；
  - `K_HEAD` 的「最後新聞更新」改 2026-11-01；`M_ROUTE` 的 K 列改 2026-11-01；
  - `M_REFS` 改成 11-01～10-23；`R_HEAD` 的「78 列」改「82 列」（🟡1）；
  - 加上 🔴1、🔴3、🔴4 的改動。
再補一道防呆：`split_cc.py` 讀進新檔後先跑下面這行，確認位移後內容不同的行沒有超出這份已知清單：
`assert [n for n in range(1,1232) if OLD[n-1]!=LN[o2n(n)-1]] == [8,11,15,17,18,36,38,39,40,235,318,362,389,392,531,553,556]`
`OLD` 是 `git show ba9bf17:wiki/entities/claude-code.md`。實作前頁面如果又被 ingest 動過，這條會先紅，不會靜默切錯。

**🔴3 K 宣稱「最後新聞更新 2026-11-01」，freshness 閘會紅**
11-01 的 7 筆歸因都記在 `entities/claude-code`，例如 `issues/45596`、`issues/37951`。K 頁 11-01 的新內容（/buddy、#37951、#19649、#92984、#71542、#44763、#21151）只寫了 issue 號，沒有附網址。`check_wiki_freshness.py` 的 `ancestor_att`（L201–211）只在「上層那筆歸因的網址出現在本頁」時才認帳，所以實跑結果是 `[無從對照] entities/claude-code-known-issues：頁面宣稱 2026-11-01 有新聞更新，但歸因記錄從無此頁`，exit 1。設計者跑的是 10-31 舊檔，K 的 Wccftech 網址剛好在頁內，所以他那次是綠的。
修法：`K_CALLOUT` 第一條的 `#45596` 換成 `[#45596](https://github.com/anthropics/claude-code/issues/45596)`（`R/rerun/newtext.py` 已改）。改完實跑 `OK: wiki 新鮮度檢查通過（134 頁…）`。不要改用補歸因帳本：那 7 筆當天確實是寫在母頁上，補一份只會讓計數重複。

**🟡1 數字寫錯的地方**
- R 頁 `%%` 的「78 列」改成「82 列」；這句會進 wiki，`R/rerun` 已改。
- proposal §1 表 R 列、map 第 26 列、draft L447 的「96 列／96＋2 列」改成「107 列／107＋2＝109 列」。
- 行數表 K 改成 434；proposal §4 的「R 2」「31」改成「R 1」「30」。

**🟡2 驗證腳本的路徑**（第 20 波 🟡A 重演）
- `D/verify_split.py` 和 `D/split_cc.py` 的 `ROOT = HERE.parents[2]`，搬家後指到的是 scratchpad 根目錄，不是 repo。
- `D/build_tmp.sh` L4–5 寫死 `<repo>/scratchpad/w21/design`。
- 九檔複製進 repo 後，`verify_split.py` 會去讀新母頁當「原檔」。
修法：驗收改用 `R/rerun/verify2.py`，四個參數都要明寫：`<repo> <原檔> <原 archive> <out 目錄或 repo/wiki/entities>`。原檔在複製前先存一份：`git show HEAD:wiki/entities/claude-code.md > <scratchpad>/w21/review/orig_1234.md`，archive 同理存成 `orig_archive.md`。

## 二、明天的維護者

**🔴1 L269 攝影機那條不能縮成一行**（N2 重算）
K 原文（舊 L269）寫的是 2026-08-10 查證的結果：經 HN #48192403 與 Theo（t3.gg）證實，這是 Anthropic 刻意加的防自動化機制。它要指過去的家 `topics/ai-agent-safety-archive#2026-05-20`（L49、L53）卻寫「Anthropic 尚未正式說明」「尚未確認是否為正式功能」，比 K 舊，說法也相反；而且 archive 一字不刪，不能去更新它。`shield_unique.py` 只比對號碼和日期 token，所以漏了這種「狀態比較舊」的情形。縮成一行的話，查證結論就沒有家了，還會把讀者指去一個說法相反的頁。
修法：`newtext.py` 刪掉 `K_SHIELD[269]` 和 `K_SHIELD_SPAN[269]`，讓 L269 原文留在 K（`R/rerun` 已改）。K 頁 `%%` 的「重疊的 17 條」數字不用動，因為 16 條＋Cursor 1 條還是 17。另外 draft F1 §0 第二條末尾補一句：`縮成一行前先核：事件所在頁對這件事的狀態與查證日不舊於本條；較舊、或那一頁是 archive 時，本條留全文。`

**🔴4 2.1.313 不該掛 🔎**（回答 (b)）
- 新的 🛡️ 條目（新 L244–245）照 N2 規則要縮成一行。它的全部事實 product-vulns 都已經有：L72 表列有窗口、5,000 人和兩說；L85–93 是節點；L59 有清查步驟；L89 有歸屬分歧。所以新 L245 子條列刪掉，換成 `K_SHIELD_CURSOR` 一行：狀態、延伸套件版號、最多 5,000 人、「解除安裝不夠」，加上「證據見 product-vulns#2026-10」。
- R 的 🔎 要拿掉。主編查證確認 CLI changelog 沒有 2.1.313 節，而 2.1.314 已經發布，版號不會倒回去補；ingest 也講明了這是延伸套件的版號。兩邊不衝突，問題已經答完。事件本身還懸著的部分（CVE、發布權限、實際濫用），product-vulns L100 已經有一筆 ❓（標 10-30｜查 2.1.313、SSH backdoor）。R 再掛一筆 🔎，同一個問題就有兩個懸置家。
修法：
- `R_MARK_2313` 換成一句不掛標記的說明：`> 版本表沒有 2.1.313：官方 CLI changelog 在 2.1.312 之後是 2.1.314（2026-11-01 查）；「2.1.312／2.1.313」是 Cursor 市集遭竄改的 VS Code 延伸套件版號，事件見 [[topics/ai-agent-safety-product-vulns#2026-10]]。`
- `verify2.py` 的預期改成「拆後＝拆前」，不再加 1。
- draft F1 R 節第二條換成：`- 官方 changelog 沒有的版本號不得寫成表列。媒體報導的版號對不上時：該號已被跳過（後一號已發布）→ 表上方寫一句說明並指向事件所在頁，不掛懸置標記；該號比最新版還新 → 標 🔎，複查日照常。`

**🟡3 handoff 帳已經變了**
H-1458cf、H-6e641e 在 11-01 的 ingest 已經結案（`data/pending-handoffs.jsonl` L352、L353），提案 §6 末段改成只結 H-7526b2。handoff 5 的後半句「請寫明是 Cursor 市集延伸套件版本」刪掉：product-vulns L72、L85 已經寫了延伸套件。剩下的改成：`stable 11-01 為 2.1.309（L54 仍寫 2.1.308）；K 🛡️ 17 條已改為一行指向本頁，L269 攝影機一條因安全 archive 狀態較舊而留全文`。其餘 handoff 的目標行，這次 merge 都沒動（feature-radar、cowork、claude-tag、claude-skills、agent-stack、index、cwg、guardrails 的 diff 都是空的；code-quality-decline 只有 L225→L226，而那一處是文字指路，不用改）。

## 三、冷讀者

拿 `R/rerun/out` 從母頁走四題，路徑都通：
- Q1：結論表在路由表下方。
- Q2：母頁「版本」兩條，再到 R「現在該跟哪條」。
- Q3：F 的 hooks 結論和三子條；母頁 hooks 殼一句就答到。
- Q4：F 的「平行分派選哪種」。
11-01 換上的 callout 第二條，原文寫「詳見已知問題」。我改成直接指 product-vulns：K 只有一行，讀者要的事件證據在安全頁。這一條已經併進 🔴2 的 `M_CALLOUT`。沒有其他會改變實作單的條目。

## 四、治理

**🔴5 reader-language 要本機修白名單，不是 `--write-baseline`**
`check_reader_language.py` 現在的存量基線是 0 筆（`存量基線內 0 筆／0 頁`）。那 2 筆之所以能過閘，是因為白名單 #22–#24 認定「封存」在這裡是產品功能名。拆頁後白名單上的 page 對不上，才變紅。如果本機跑 `--write-baseline`，會把兩筆被白名單認可的產品詞種進「內部用語外洩」的存量基線，等於把一個已經歸零的棘輪退回 2，白名單三筆也會一直留著失效。
修法：proposal §8 的 reader-language 列、可行性前提、搬家清單，都改成：`本機把 data/reader-language-allow.json 的 #22、#23（line_contains「只談封存」）page 改為 entities/claude-code-known-issues、#24（「對話封存後完全消失」）改為 entities/claude-code-releases，reason 原樣保留，#23 與 #22 重複可刪；不跑 --write-baseline`。雲端改不了，因為 `guard_roles.py` L54 把 `data/*-allow.json` 也列在 H6 裡；跟 cell 一樣，只准在分支上紅。

**主 session 指定的改寫：proposal §8 與可行性前提**
- §8 表裡 `check_cell_limits.py` 列的「看守什麼」欄末尾加：`本波不重建（雲端 H6 擋 --rebuild／--allow-grow）；107 筆搬家證明見 claude-code-2026-11-01-baseline-moves.md，使用者本機重建`。
- `check_reader_language.py` 列照 🔴5 改。
- `check_pending_markers.py` 列改成 `新語法 212、舊字樣 20→18；--rebuild-count 照做（不在 H6 擋的範圍）`。
- 可行性前提整句換成：`wiki 九檔、規則檔 5 份＋sweeps、gen_wiki_frontmatter.py **只跑不改**（改 scripts/ 會觸發 Stop hook 跑 run_tests，而 cell／reader 兩閘本波刻意紅）、pending --rebuild-count、handoff 與 wiki/log.md Query 條目、搬家清單 claude-code-2026-11-01-baseline-moves.md，同一個 commit 進 claude/stoic-edison-ewvmcx 並 push；cell 與 reader-language 只准因純搬家而紅（cell 107 筆、reader 2 筆，清單逐筆對得上），由使用者本機跑 cell --rebuild --allow-grow 與白名單三筆改 page 後再併 master；cowork 兩錨點不改，build_web 當場 ERROR。`
- 這個分支不是 master，所以 `gate_wiki_commit.py`（H9，PROTECTED 只有 master／main／HEAD）不會擋這次 commit。

**🟡4 搬家清單怎麼產**
實作第 9 步後跑 `python -I <scratchpad>/w21/review/moves.py <repo> <repo>/wiki`，把輸出的 107 列表格（新頁、行、類型、錨點、長度、舊頁基線上限）原樣貼進 `docs/page-audits/claude-code-2026-11-01-baseline-moves.md`。文件頂上寫三件事：
- 「配不回 0」；
- 本機兩個動作：`python scripts/check_cell_limits.py --rebuild --allow-grow --reason "第 21 波 claude-code 拆頁：107 筆存量超限隨原文搬到三子頁（內容與長度不變，清單見 claude-code-2026-11-01-baseline-moves.md）；舊頁名下失效存量一併收緊"`，預期 added 107／removed 181；
- 白名單三筆改 page（🔴5），預期 reader 閘 `OK`。

**🟡5 `--rebuild-count` 的理由句**
`第 21 波 claude-code 拆頁：23 筆隨條目換 slug（K 20／F 2／R 1，含 11-01 新增的 128 MB 一筆）；去 slug 比對無減少；2.1.313 不新增標記（懸置住 product-vulns）；基線自 10-31 206 筆後他頁 ingest 淨增 6 筆一併入帳`。預期印出 count 212、added 28／removed 22。

**🟡6 N3–N5 照判**：沒有新意見。N4 的 5a 第 4 條要寫進 sweeps.md 的 `## 5a`（L29 起），現在那一節是「feature-radar 熱度降溫」，條號要接在它現有的末條之後。

## 照順序執行（實作單）

| 步 | 誰 | 做什麼 | 驗 |
|---|---|---|---|
| 1 | 設計者（第二輪） | 用 `R/rerun/{split_cc.py,newtext.py,verify2.py}` 取代 `D/` 同名檔，`split_cc.py` 加 🔴2 的防呆 assert；重跑 `python D/split_cc.py <repo>`、`python D/make_draft.py` | 印 `OK {'M': 202, 'K': 465, 'R': 288, 'F': 267, 'AR': 362}`、`archive 版本列： 82`；`python -I D/verify2.py <repo> <repo>/wiki/entities/claude-code.md <repo>/wiki/entities/claude-code-archive.md D/out/wiki/entities` 印 `OK　照搬 925 行逐字、懸置 30→30` |
| 2 | 設計者（第二輪） | 文件：🟡1 的數字；proposal §1 的 N2 改成「舊 16／11、新 17／11（L269 獨有）」、§4、§6（🟡3）、§8 與可行性前提（照「四、治理」逐字）；draft F1 §0 補縮行前核句（🔴1）、R 節第二條換掉（🔴4）；map 第 26 列 96→107、🛡️ 列的 17 條清單刪 269 加「新 L244 Cursor」 | `grep -n "96 列\|78 列\|30→31\|R 2" docs/page-audits/claude-code-2026-11-01-*.md` 0 命中 |
| 3 | 主 session | `git log --oneline ae4ce48..HEAD -- wiki/entities/claude-code.md wiki/entities/claude-code-archive.md wiki/entities/cowork.md wiki/entities/claude-tag.md wiki/entities/claude-skills.md wiki/entities/anthropic-agent-stack.md .claude/reporter-rules .claude/skills/wiki-lint-sweeps`；存原檔 `git show HEAD:wiki/entities/claude-code.md > <scratchpad>/w21/review/orig_1234.md`（archive 同） | log 為空。不空的話，第 1 步的防呆 assert 會紅，回到第 1 步照新 hunk 補 `o2n` |
| 4 | 實作者 | `D/out/wiki/entities/` 五檔複製進 `wiki/entities/`；cowork L52、L78 `#已知問題`→`entities/claude-code-known-issues#已知問題`，L37、L97 指 K；claude-tag L45→`entities/claude-code-releases#最新版本`；claude-skills L81→F「桌面版文件時序」；anthropic-agent-stack L89 補連 F `#Subagent 型別差異對照` | `python -I D/verify2.py <repo> <scratchpad>/w21/review/orig_1234.md <scratchpad>/w21/review/orig_archive.md <repo>/wiki/entities` 印 OK、30→30 |
| 5 | 實作者 | 規則檔：draft F1–F5 照第二輪定稿；F6 跨維護者照主 session 判 | `python scripts/check_rules.py` exit 0 |
| 6 | 主 session | `python scripts/gen_wiki_frontmatter.py`（只跑不改） | index L48 投影含三子頁＋mods；`check_hierarchy` ✅ 31 |
| 7 | 主 session | `python scripts/check_pending_markers.py --rebuild-count --reason "<🟡5 那句>"` | count 212、added 28／removed 22 |
| 8 | 主 session | handoff 1–8（第 5 筆照 🟡3）先 `--dry-run` 再 `open`；`pending_handoffs.py close H-7526b2`；`wiki/log.md` 寫 Query 條目並帶單號 | `python scripts/check_log_handoffs.py` 綠 |
| 9 | 主 session | 閘一次跑完：hierarchy、pending、freshness、build_web 必須綠；cell、reader 預期紅 | hierarchy ✅；pending ✅；freshness `OK…134 頁`；build_web 尾行 `斷鏈 WARN 23／錨點 WARN 0`；cell `FAIL…107 筆`；reader `FAIL…2 筆`（K L281、R L236）；不在這兩閘的紅一律停下 |
| 10 | 主 session | 照 🟡4 產 `docs/page-audits/claude-code-2026-11-01-baseline-moves.md` | 表 107 列、配不回 0；reader 段列出白名單三筆的改法 |
| 11 | 主 session | 只 `git add` 指名的檔：wiki 9 檔、規則檔、`data/pending-marker-count.json`、`data/pending-handoffs.jsonl`、`wiki/log.md`、`docs/page-audits/{ledger.md,claude-code-2026-11-01-*.md}`；commit 進 `claude/stoic-edison-ewvmcx` 並 push | `git status` 殘留只准是 gen 改的 frontmatter 數值與 `web_reader/` 產物；`data/cell-limit-baseline.json`、`data/reader-language-*.json` 未動 |
| 12 | 主 session | ledger 定稿列：正文 173／434／260／239、N1 82（留 107）、N2 舊 16／11、新 17／11、懸置 30→30；寫明本機兩個重建動作是併 master 的前提 | — |
