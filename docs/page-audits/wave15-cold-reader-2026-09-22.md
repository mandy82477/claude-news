# 第 15 波 冷讀者實測 2026-09-22

**我開過的頁（依序）：** `wiki/index.md` → `wiki/topics/skill-interest-watch.md` → `wiki/topics/community-tech-tools.md` → `wiki/topics/community-large-codebase-workflow.md` → `wiki/entities/claude-code.md`

**我是誰：** Max 訂閱、接手公司大 repo、最近同時跑 3 個 agent。不知道這個 wiki 誰在寫、怎麼維護。

---

## Q1. 三個 agent 在同一 repo 互相覆蓋（補述：已用 worktree，commit 落地還是打架）

**路徑：** index → 興趣類別 skill 總覽 → 社群工具目錄 →（回頭驗證）大型 codebase 工作流主線
**跳數：** 3 跳拿到主答案，第 4 跳（大型 codebase 頁）沒有加值。
**結果：** **半拿到**。「裝哪一個」「為什麼是它」拿到了；「怎麼裝」整趟沒有。補述（worktree 之後）頁面**接得住，但只接住半句**。

拿到的答案原句：

- `wiki/index.md:27`｜`| 我卡住了（帳單爆、context 撐爆、agent 互踩、它說做完了沒做、agent 讀不懂大 repo、跑 auto 出事……），**社群首選**是哪個 | [[topics/skill-interest-watch]]「我卡在這裡」決策表 |` — 這一列是全程最好的一句，我一眼就知道去哪。
- `wiki/topics/community-tech-tools.md:58`｜`| 多個 agent 在同一 repo 互相覆蓋 | ⌨️ [**Harness**](https://github.com/frenchie4111/harness) | 隔離後 commit 落地仍打架 → Claude Code Merge Queue；要跨 harness 統一協作邏輯 → omnigent | 🟢（04-29 起多來源） |`
- `wiki/topics/community-tech-tools.md:286`｜`| [**Harness**](https://github.com/frenchie4111/harness) | 多 Agent | ✅ | 2026-04-29 | 多 Git worktree 並行管理多個 Claude Code agent，補 cmux/Conductor 不足 |` — 這句才告訴我「為什麼是它」。
- `wiki/topics/community-tech-tools.md:210`｜`| [**Claude Code Merge Queue**](https://github.com/funador/claude-code-merge-queue) | 多 Agent | ⏳ | 2026-07-30 | 讓多個平行 agent 的 commit 排隊依序落地、逐一建置測試後才合併，緩解低規格機器同時建置的資源競爭；HN 39 |`

卡住／誤導我的原句：

- `wiki/topics/community-tech-tools.md:58` 同一句也是誤導來源：**首選 Harness 做的事正是我已經在做的事**（多 worktree 管理）。我照決策表第二欄裝，等於白裝；真正對得上我的是第三欄那半句。決策表的形狀（「先裝這個」＝主答案）把我推向錯的格子。
- `wiki/topics/community-tech-tools.md:64`｜`安裝：🧩 skill/plugin（一行安裝隨時可拔）／⌨️ CLI／🖥️ 桌面 app（注意平台鎖定）／🔌 proxy·MCP（**流量過第三方層，裝前先評估安全**）` — 這行叫「安裝」圖例，我以為下面會有安裝方式，結果它只是**分類**。Harness 標 ⌨️，全頁沒有任何一條 CLI 安裝指令。
- `wiki/topics/community-large-codebase-workflow.md:63`｜`**🧰 現在就能下的解**：見 [[topics/community-tech-tools]]「我卡在這裡」——「多個 agent 在同一 repo 互相覆蓋」列（首選 Harness）與「一堆 agent 在跑，看不到誰卡住」列（首選 Omar）` — 我繞到這頁想找「worktree 之後怎麼辦」，它把我原路送回同一列，這一跳是純浪費。
- `wiki/topics/community-large-codebase-workflow.md:74`｜`| 落地整合 | 本地合併佇列（4–5 agent／日 90 commit／8GB 筆電） | 單一作者實測 | 單一實測 |` — 這是我這題唯一看到的「合併佇列真的有人跑過」的證據，但它**沒有工具名**，我無法把它和 Claude Code Merge Queue 連起來（是我自己猜的）。
- 補述的第二個缺口：Merge Queue 在工具目錄裡只有 `採用 ⏳`（觀望中）與 `HN 39`，**沒有證據等級、沒有判定日、沒有安裝法**。決策表叫我改裝它，落地時一片空白。

---

## Q2. Max 訂閱，額度快用完時想被提醒（不是「錢花到哪」）

**路徑：** index → 興趣類別 skill 總覽 → 社群工具目錄（在同一頁往下捲）
**跳數：** 3 跳。
**結果：** **半拿到**。工具存在，但**決策表沒有我的症狀列，也沒有誠實說「這類沒有首選」**；我是自己把 152 列目錄捲完才撿到的。

拿到的答案原句（我自己捲出來的，沒有任何一句話指引我過去）：

- `wiki/topics/community-tech-tools.md:236`｜`| [**agent-baton**](https://www.reddit.com/r/ClaudeAI/comments/1tgel55/) | 費用監測 | ⚡ | 2026-05-18 | 利用 Anthropic 使用量 API + Claude Code hook，在觸及速率上限前主動發出警告並轉移進行中的工作，解決 Claude Code 靜默中斷的長期痛點 |` — **這正是我要的東西**，而且只有這一列是。
- `wiki/topics/community-tech-tools.md:238`｜`| **Claude Usage Widget** | 費用監測 | ✅ | 2026-05-18 | 浮動桌面小工具，讀取 Anthropic 速率限制 API 標頭，即時顯示 5 小時 session 使用量（含色彩進度條）、每週配額、token 輸入輸出統計，每 5 秒更新，支援 Windows + macOS |` — 唯一標 ✅ 的，但**整列沒有連結**，我不知道去哪裝。
- `wiki/topics/community-tech-tools.md:281`｜`| **Throttle Meter** | 費用監測 | ⚡ | 2026-04-30 | macOS menubar 用量計，即時顯示 5h 滾動窗口與週配額 |` — 同樣沒有連結。

卡住／誤導我的原句：

- `wiki/index.md:27`｜`帳單爆、context 撐爆、agent 互踩……` — index 只給我「帳單爆」這個詞。我的問題不是帳單爆，是**額度快見底**。我差點認為這個 wiki 沒收這類。
- `wiki/topics/community-tech-tools.md:54`｜`| 帳單爆了，看不到錢花在哪 | ⌨️ **tare** | 不想動終端、要桌面常駐 → 🖥️ Claude Usage Widget；想比較多個 coding agent 的花費 → Frugal Tokens | 🟡（08-27） |` — 決策表把「花多少錢」和「還剩多少額度」壓成同一列。我是 Max 訂閱，**我沒有帳單**，這一列的症狀文字直接把我排除在外；而真正對的 Claude Usage Widget 被寫成「不想動終端」的次選條件，理由完全是錯的軸（我要的是「快到了叫我」，不是「要不要開終端」）。
- `wiki/topics/skill-interest-watch.md:144`｜`規模榜：無——這類需求無法用 GitHub 描述辨識（治理型需求是讀者講痛點的語言，在 HN／dev.to 全文不在 repo 描述），本庫不掛空榜。` — 這種誠實句在別的類別出現過，**唯獨額度提醒這一類連一句「本庫尚無判斷」都沒有**，因為它根本不被當成一個類別。
- 順帶：`wiki/entities/claude-code.md:801` 的歷史記錄裡還有 `my-time-has-come（配額將至時自動收尾任務）`，又一個對得上的工具，但它躺在 05-15 的流水帳裡，決策表與工具目錄都沒有它。

---

## Q3. 把接手的 codebase 畫成架構圖交付給主管看

**路徑：** index → 興趣類別 skill 總覽 → 社群工具目錄
**跳數：** 3 跳。
**結果：** **拿到**（四題唯一完整拿到的一題：單一答案＋為什麼是它＋怎麼裝）。

拿到的答案原句：

- `wiki/topics/skill-interest-watch.md:52`（＝`wiki/topics/community-tech-tools.md:56`）｜`…要讓**人**看懂而非 agent → [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)；要把架構畫成圖交付 → [archify](https://github.com/tt-a1i/archify)…` — 「交付」兩個字讓我立刻確定是這個。
- `wiki/topics/community-tech-tools.md:99`｜`| [**archify**](https://github.com/tt-a1i/archify) | ⚪（09-02 查證 user-query；43,378★、forks 2,777、214 commits） | 【給人·交付級圖表】架構／時序／資料流／生命週期圖，自包含 HTML 可匯出——把架構講給別人聽、寫進文件；🧩 npx skills add tt-a1i/archify -g |` — **這一列是全站示範級：一句話用途＋分工定位＋證據＋一行安裝指令全在同一格。**
- `wiki/topics/community-tech-tools.md:70`｜`**接手大 repo 的分界**（09-03 補寫）：graphify 給 **agent** 用（本機 AST、免向量 DB，`/graphify` skill）；同組另三個解的是不同工種——Understand-Anything 給**人**探索、archify 給人**交付圖**、codegraph 是 graphify 的競品…` — 這段讓我確信沒選錯工種。

卡住的原句（輕微）：

- `wiki/topics/community-tech-tools.md:99`｜`⚪（09-02 查證 user-query；43,378★…）` — 「⚪ 僅星數」是全表最弱的證據等級，但頁面沒告訴我「⚪ 的東西該不該裝」。我只知道它弱，不知道弱到什麼程度該放棄。另外 `user-query` 這個詞我完全不懂是什麼。

---

## Q4. Harness 的推薦是「04-29 起多來源」判的，今天 2026-09-22，還可信嗎？

**路徑：** index → 興趣類別 skill 總覽 → 社群工具目錄 → Claude Code CLI 主頁
**跳數：** 4 跳。
**結果：** **半拿到**。「這個判斷多舊」看得出來、「要不要自己再確認」有一句明話；但「去哪確認」把我送進死路。

我會拿來判斷的那一句（不能開網頁時的判準）：

- `wiki/topics/community-tech-tools.md:64`｜`**證據等級為收錄或查證當時的判定，括號內即判定日，不隨時間自動回訪**。` — **就是這句。** 它明白告訴我：04-29 是判定日不是現況，這個結論沒人回頭看過，要信得自己去查。這句寫得好，位置也對（就在表格正下方）。
- 配合 `wiki/topics/community-tech-tools.md:286` 的 `首次出現 2026-04-29`：4 月 29 日到今天接近 5 個月，而該列的採用欄還是 `✅ 廣泛採用`，我無從得知這個 ✅ 是哪一天判的。

讓我卡住／互相打架的原句：

- `wiki/topics/community-tech-tools.md:50`｜`> 本表每週複查一次；首選工具的急性事件（資安、棄坑、下架）另見 [[entities/claude-code]] 與 [[topics/ai-agent-safety]]。` 這句和上面 `:64` 的「不隨時間自動回訪」**當場打架**。到底有沒有人每週看過 Harness？我讀不出來。
- `wiki/topics/community-tech-tools.md:36-37`｜`> **本週策展：新增 11 個工具**（2026-09-19）` ／ `決策表本輪無變動（無新證據推翻現有首選）。` — 讀到這裡我才隱約猜到「每週複查」複的是表、「不回訪」指的是證據日期。但這是我拼出來的，頁面沒講。而且「無新證據推翻」和「有人去找過新證據」是兩回事。
- 我照 `:50` 的指路開了 `wiki/entities/claude-code.md`，整頁關於 Harness 的社群工具記載只有：`wiki/entities/claude-code.md:856`｜`- 04-29：官方發布 Champion Kit 企業推廣素材；社群工具 Cockpit／Harness／CodeThis／Claude Exporter 發布。` **這是一行「發布了」的流水帳，就是 04-29 那天本身。** 叫我去查急性事件的那一頁，關於 Harness 的唯一內容跟原判定日是同一天同一件事。「沒消息」和「沒人查」在這裡長得一模一樣。
- 「🟢 多來源」的來源我一個都看不到：`wiki/topics/community-tech-tools.md:72`｜`**多 agent 互踩**：Harness 為 ✅ 廣泛採用（04-29 收錄，多來源）；omnigent 星數 9,080…` — 說了多來源，但沒有任何一條連結或出處，我無法自己覆核。
- 結論：**頁面給得出判斷的年紀與自查的義務（`:64`），給不出自查的材料。** 我最後能做的只有拿 `:286` 的 repo 連結自己去看 commit 活躍度。

---

## 分不出差別的兩頁

**`wiki/topics/skill-interest-watch.md`（興趣類別 skill 總覽）vs `wiki/topics/community-tech-tools.md`（社群工具目錄）。**

我到最後都說不出「A 看這、B 看那」。理由：

- 兩頁的「我卡在這裡」決策表是**逐字同一張表**：`skill-interest-watch.md:48-60` 與 `community-tech-tools.md:52-64`，連圖例段（`:60` 對 `:64`）都一字不差。我讀第二頁時整整捲了半頁才意識到「我是不是回到剛才那頁了」。
- 更糟的是 skill-interest-watch 在內文**又把同一列重印了三次以上**（`:99-101`、`:140-142`、`:156-158`、`:191-194`、`:217-219`）。同一句 Harness 建議我在這趟裡讀到 4 次。
- 我讀到 `skill-interest-watch.md:46`｜`本表每日同步自 [[topics/community-tech-tools]]（判斷與證據的家；改判斷請改那頁），同步日 2026-09-21。` 才**勉強**弄懂差別——但這句是寫給維護者看的（「改判斷請改那頁」關我什麼事），而且它告訴我的是「兩頁一樣」，不是「你該看哪一頁」。
- 真正的差別（A 多了 GitHub 星數榜、B 多了 152 列目錄與推薦細節）沒有任何一句話直說。`skill-interest-watch.md:40`｜`完整證據、推薦細節、Skills 速查與 152 列工具目錄在 [[topics/community-tech-tools]]。` 是最接近的一句，但它的意思是「另一頁比較全」——那我為什麼要待在這頁？
- 結論：對我這個讀者，skill-interest-watch 的唯一獨有價值是星數榜，而頁面自己在 `:39`｜`**星數是規模不是品質**：榜不做推薦，推薦只看決策表` 說它不能拿來做決定。**一頁唯一獨有的東西，自己聲明不能用。**

（次要的一組：`wiki/topics/community-large-codebase-workflow.md` 與 `wiki/topics/community-tech-tools.md`。前者 `:63`、`:87`、`:113` 每一節的「現在就能下的解」都是把我送回後者的同一張表，我三次都在想「那我直接待在工具目錄就好了吧」。）

---

## 這幾頁是「雷達」還是「百科」？

| 頁 | 我讀起來是 |
|---|---|
| `wiki/index.md` | **百科**（目錄）——給我路由、不給我近況，這符合我的預期，是這趟最乾淨的一頁。 |
| `wiki/topics/skill-interest-watch.md` | **雷達**——星數榜與「本週竄升」是它唯一獨有的東西；但它偽裝成百科（頂上掛著一張和別頁一字不差的決策表），害我以為它是答案頁。 |
| `wiki/topics/community-tech-tools.md` | **百科**——症狀→首選→分界→證據，加一份 152 列目錄；頂上的「本週策展」想扮雷達，兩種身分在同一頁打架。 |
| `wiki/topics/community-large-codebase-workflow.md` | **百科**（四條主線的現狀敘事）；「本週答案變動」callout 又在扮雷達，內容卻說「四條線的答案皆不變」——雷達開著卻沒有訊號。 |
| `wiki/entities/claude-code.md` | **百科＋流水帳**——上半現況（已知問題）是百科，下半版本史／歷史記錄是不可檢索的日誌；我在裡面找 Harness 只撈到一行 04-29。 |

---

## 內部用語外洩表

| 檔名:行號 | 原句 | 我讀起來的困惑 |
|---|---|---|
| `wiki/topics/skill-interest-watch.md:46` | `本表每日同步自 [[topics/community-tech-tools]]（判斷與證據的家；改判斷請改那頁）` | 「判斷的家」「改判斷請改那頁」——這是在對維護者說話，我不改任何東西。 |
| `wiki/topics/skill-interest-watch.md:32` | `🗓️ 每日快照（機器產出；決策表抄自社群工具目錄、最多落後一天…）` | 「抄自」「機器產出」——所以我看的是二手複製品？那我要不要直接去看正本？ |
| `wiki/topics/skill-interest-watch.md:39` | `榜上標 🧭 者代表決策表或工具目錄已有判斷` | 🧭／📰 兩個符號得回頭查圖例；「已有判斷」不等於「推薦」，那 🧭 到底幫我什麼？ |
| `wiki/topics/skill-interest-watch.md:144` | `本庫不掛空榜。` | 「掛空榜」是編輯台政策講法，讀者只想知道「這類有沒有東西可裝」。 |
| `wiki/topics/community-tech-tools.md:36` | `> **本週策展：新增 11 個工具**（2026-09-19）` | 「策展」是編輯台的詞；「新增 11 個」對我零價值——我不知道那 11 個是不是我要的。 |
| `wiki/topics/community-tech-tools.md:64` | `首選只在出現新證據時更換，不為輪替而換。` | 這是編輯守則。我關心的是「這個首選上次被看過是哪天」，不是你們換不換。 |
| `wiki/topics/community-tech-tools.md:99` | `⚪（09-02 查證 user-query；43,378★…）` | `user-query` 是什麼？某個人問過？某種來源分類？完全猜不到。 |
| `wiki/topics/community-tech-tools.md:129` | `skill 分享基建（Sx 2.0）與彙整清單（awesome-llm-apps）不入本節` | 「不入本節」的收錄政策，讀者不需要知道你們為什麼不收。 |
| `wiki/topics/community-tech-tools.md:140` | `**入選標準** ｜ HN score ≥ 30 或評論 ≥ 5 / Show HN 投稿 / 同日 2 個獨立來源` | 這其實對我有用（判斷這份目錄可不可信），卻埋在「指標說明」表最後一列、用編輯台語氣寫。 |
| `wiki/topics/community-large-codebase-workflow.md:70` | `（官方文件已證實機制方向，見下方懸置細節 ⟨Q-01⟩）` | 「懸置細節」「⟨Q-01⟩」——不知道「懸置」是狀態還是分類，Q-01 是編號還是問題。 |

---

## 撐不起的句子

1. **「每週複查」vs「不自動回訪」**：`wiki/topics/community-tech-tools.md:50`（`本表每週複查一次`）↔ `wiki/topics/community-tech-tools.md:64`（`證據等級…不隨時間自動回訪`）。同一頁相隔 14 行，我讀完不知道 Harness 的 🟢 到底 9 月有沒有人看過。
2. **「有人判斷過，帶證據等級與判定日」撐不起判定日的年紀**：`wiki/topics/skill-interest-watch.md:37`（`該裝哪個：看「我卡在這裡」決策表——有人判斷過，帶證據等級與判定日。`）↔ 同頁 `:54`（`🟢（04-29 起多來源）`）、`:56`（`🟡（04-27）`）。頁面掛著「每日快照」的頻率標籤（`:32`），表裡最關鍵的兩列卻是近五個月前的判定，兩者在同一螢幕上互相削弱。
3. **「多來源」撐不起任何可查的來源**：`wiki/topics/community-tech-tools.md:72`（`Harness 為 ✅ 廣泛採用（04-29 收錄，多來源）`）↔ `wiki/entities/claude-code.md:856`（`04-29：…社群工具 Cockpit／Harness／CodeThis／Claude Exporter 發布。`）。它自己指路要我去查的那一頁，關於 Harness 的唯一記載是一行發布快訊，看不到第二個來源。
4. **「每個症狀給一個首選」撐不起自己**：`wiki/topics/community-tech-tools.md:43`（`每個症狀給一個首選、一條改用分界、一個帶日期的證據等級`）↔ 同頁 `:61`（`CLAUDE.md 寫了它不聽 | —（答案是機制不是工具，見細節）`）。第一格就沒有首選。（這個例外本身是好的誠實，壞的是摘要把話說死。）
5. **「安裝」圖例撐不起安裝**：`wiki/topics/community-tech-tools.md:64`（`安裝：🧩 skill/plugin（一行安裝隨時可拔）／⌨️ CLI／…`）↔ 全頁唯一出現的安裝指令只有 `:99` 的 archify 那一行。決策表 9 列首選裡 8 列標了安裝類型、0 列給得出安裝方式。

---

## 最想改的三件

1. **決策表第三欄要能獨立作答**：我走到「隔離後 commit 落地仍打架 → Claude Code Merge Queue」時，它就該和首選一樣有連結、證據等級與安裝方式，而不是一個裸名字——對已經做過隔離的人來說，第三欄才是主答案。
2. **每一列首選旁邊放一行安裝指令**（像 archify 那格一樣），不然「先裝這個」這三個字是空話。
3. **把「額度快用完叫我」補成一列症狀**，或明寫「本庫尚無判斷」；現在它被塞進「帳單爆了，看不到錢花在哪」，而 Max 訂閱的我根本沒有帳單，等於被這張表排除在外。
