# Wave 13 冷讀者複驗 — 官方 agent 積木頁（2026-09-12）

**身分：** 第一次打開這個知識庫的工程師讀者
**規則：** 只從 `wiki/index.md` 出發，只沿 `[[wikilink]]` 開頁；不 Glob、不 grep、不 web、不讀 docs/.claude/scripts/news。
**受測頁：** `wiki/topics/anthropic-agent-stack.md`（官方 agent 積木）

---

## 入口

index 第 30 列（💻 開發實務入口表）：

> 「我想讓 agent 自己跑幾小時／過夜，該用哪個（`/goal`、subagent、dynamic workflows、agent teams、agent view、Managed Agents、Agent SDK）」→ `[[topics/anthropic-agent-stack]]`「你該用哪個」

**入口判定：找得到。** 這列把七個專有名詞攤在鉤子裡，冷讀者就算只認得 subagent 一個詞也會點進去。第 102 列 Topics 表也有同一頁（「官方 agent 積木總覽：八塊積木各自為什麼出、讓你多做出什麼、怎麼疊」），兩個入口措辭一致、不打架。
唯一小摩擦：第 30 列的問句是「跑幾小時／過夜」，而我四題裡有三題不是問時長，是問「為什麼出／怎麼組」。靠 Topics 表那列才確認是同一頁。

---

## Q1 dynamic workflows 官方為什麼出，沒有它之前會撞到什麼牆？

- **路徑：** `index` → `topics/anthropic-agent-stack`
- **跳數：** 1 跳（讀 2 頁）
- **結果：拿到**
- **答案：** 沒有它之前計畫握在 Claude 手上、逐回合決定下一個派誰，每份中間結果都落進 context 視窗；workflow 把迴圈、分支與中間結果收進一支可存檔重跑的 script，主對話只拿到最終答案。官方判斷式是「計畫握在誰手上」。
- **命中行：** L83（「沒有它之前」整段）、L42（摘要同義覆述）、L237（第三層「這個編排下週還會照原樣再跑一次嗎？」）
- **卡住的原句：** L95「怎麼叫它：prompt 帶 `ultracode` 或直說 use a workflow；`/effort ultracode` 讓 Claude 自己決定每個實質任務要不要開」——`ultracode` 這個詞全頁只出現在這一行，沒說它是 effort 等級、也沒指路到哪頁有解。冷讀者到這裡會停一下但不影響 Q1 答案。

---

## Q2 我現在用 subagent 加 workflows 能跑出什麼具體工作流？要一個能照做的場景，附最小指令。

- **路徑：** `index` → `topics/anthropic-agent-stack`
- **跳數：** 1 跳
- **結果：拿到（script 那節），「加」字半拿到**
- **答案：** 場景＝掃 `src/routes/` 下每個 route handler 有沒有漏做認證檢查；存成 `.claude/workflows/audit-routes.js`，用 `/audit-routes` 叫它跑、`/workflows` 看進度；script 裡 `agent()` 先列檔案、`pipeline()` 逐檔審、最後 `.filter(Boolean)` 濾掉被停掉的 agent。想要一句話版本就直接貼 L87 那行 prompt。

### 特別留意一：那支 script 看得懂怎麼存、怎麼叫、怎麼看進度嗎？

| 問 | 答得到嗎 | 依據 |
|---|---|---|
| 怎麼存 | **半拿到** | L97 給了 `.claude/workflows/audit-routes.js`，可直接照做；但同句「（或個人目錄）」沒寫那個目錄是什麼路徑，冷讀者無從照做，也沒說 `meta.name` 要不要跟檔名一致（範例裡一致，但沒明說是規則還是巧合） |
| 怎麼叫 | **拿到** | L97「用 `/audit-routes` 叫它跑」。只是沒說存檔後要不要重啟 session 才會出現這個指令 |
| 怎麼看進度 | **拿到** | L97「`/workflows` 看進度」＋ L116「`phase()` 在進度畫面分組」——兩處互相印證，確實有一個進度畫面 |
| 四個全域函式 | **拿到** | L116 一句話講完 `agent()`／`pipeline()`／`parallel()`／`phase()`，並明說「不用 import」、被停掉的 agent 回 `null`。這是全頁最實用的一行 |

### 特別留意二：「怎麼疊」那節有沒有答到「subagent 加 workflows」的「加」？

**有答到，而且答的是反直覺的那個方向。** L193–198：

- L195「**workflow 裡的 agent 可以再派 subagent**」——這是「加」的合法方向，還附了層數上限（主對話以下最多三層，`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 控制）。
- L197「**subagent 裡開不了 workflow**」——反方向被明文擋掉，`Workflow` 工具從 subagent 工具池移除。L79 積木卡裡也講了同一句，兩處一致。

所以我問的「subagent 加 workflows」實際上只有一種疊法：workflow 在外、subagent 在內。這節把它講清楚了，**且 L193 明說「其餘組合官方沒寫，本頁不猜」**——冷讀者知道這張清單為什麼只有四條，不會以為是漏寫。這是全頁最好的一個設計。

- **卡住的原句：** L97「存成 `.claude/workflows/audit-routes.js`（**或個人目錄**）」——括號裡這四個字是我照做時唯一卡住的地方。

---

## Q3 agent teams 加跨 session 傳訊讓我多做什麼，跟 subagent 差在哪？

- **路徑：** `index` → `topics/anthropic-agent-stack`
- **跳數：** 1 跳
- **結果：半拿到**
- **答案：** 跟 subagent 的差別答得很乾淨——subagent 是派出去、回報、結束，分身之間沒有通道（L122）；agent teams 讓隊友交換發現、互相質疑、自己協調；跨 session 傳訊讓另一個終端機的 session 回你話，只傳純文字、不傳對話歷史與檔案、訊息不帶依賴語意（L156）。
- **命中行：** L122（官方分界句＋「開團隊之前先確認輕一點的做法是不是就夠了」）、L143–156（跨 session 傳訊卡）、L207（決策樹第 2 問「這些工人需不需要互相講話」）、L238（第四層「點對點傳訊，傳訊層自身仍無編排」）
- **為什麼只算半拿到：** 我問的是「agent teams **加** 跨 session 傳訊」合起來多做什麼。這兩塊各自的卡都完整，但**沒有任何一句把兩者合起來講**。L193 的「怎麼疊」四條裡沒有這組（只有 workflow×subagent、goal×workflow、subagent✗workflow、workflow✗teams）。L238 把兩者放進同一層（「分身開始互相講話」），這是全頁最接近的答案，但它是架構層的歸類，不是「合起來能做什麼」的場景。
- **卡住的原句：** L238「**傳訊層自身仍無編排**，要排先後仍得回到第三層」——這句我讀得懂字面，但它回答的是「兩者合起來做不到什麼」，我想要的「做得到什麼」那半沒有。另外 L141「一個 session 只能有一個 team、不可巢狀」與 L139 的環境變數開關，讓我不確定 team 裡的成員算不算「另一個 session」、能不能對外用 `SendMessage`——這一點全頁沒答。

---

## Q4 這頁跟 topics/coding-workflow-guide、entities/managed-agents 三頁分不分得出差別？

- **路徑：** `index` → `topics/anthropic-agent-stack` →（L262）`topics/coding-workflow-guide`；`index` → `topics/anthropic-agent-stack` →（L251）`entities/managed-agents`
- **跳數：** 2 跳
- **結果：拿到，三頁分得出來**
- **答案：** 一句話分界＝**這頁答「有哪些積木、各自為什麼出、怎麼疊」（積木視角）；coding-workflow-guide 答「我現在在開發流程的第幾步、該下哪個」（流程視角）；managed-agents 答「代管平台這個產品現在怎樣、怎麼算錢」（產品視角）。**
- **依據（三頁自己都說了，而且說法一致）：**
  - 本頁 L42 摘要：「想知道『我現在在開發流程的哪一步、該下哪個』，那是流程視角，見 coding-workflow-guide；Managed Agents 這個平台產品本身的現況、計費算式與零件成熟度在子頁 managed-agents」
  - 本頁 L246–251「子頁怎麼分」表，兩列各一句話
  - coding-workflow-guide L77：「我想讓它自己跑幾小時／過夜 → 第 6 段；**各選項的分界見 anthropic-agent-stack「你該用哪個」**」——反向指回來，沒有自己重講一次選型
  - managed-agents L32「上層：anthropic-agent-stack」、L59「跟其他官方 agent 形態怎麼挑、八塊積木各自為什麼出，見上層」
- **殘餘重疊（不到分不出的程度）：** 兩頁都出現「該用哪個」措辭——本頁 L202「你該用哪個」vs guide L77 那一列。但 guide 那列是路由、不給答案，指回本頁，所以只會多走一跳、不會迷路。
- **另一處重疊：** managed-agents L56「最適合：要跑數小時以上、跨 session 保留狀態」與本頁選型表 L223 同一格內容重複一次。兩邊數字一致，但這是「同一事實兩個家」，母頁改了子頁不會自動跟。
- **卡住的原句：** 無。這題是全部四題裡最順的。

**分不出差別的兩頁：沒有。** 三頁邊界清楚且互相聲明。

---

## 內部用語外洩（冷讀者不該看到 / 看不懂的字眼）

以 `wiki/topics/anthropic-agent-stack.md` 原始檔為準，共 8 條：

| # | 行號 | 原句片段 | 為什麼是外洩 |
|---|---|---|---|
| 1 | L1–24 | 整段 frontmatter：`page_role: "hub"`、`signal: "健康"`、`inbound_links: 5`、`attribution_count`、`pending_overdue`、`days_since_news_subtree`、`generated_by: "scripts/gen_wiki_frontmatter.py"` | 維運計量欄位，冷讀者讀原始檔第一眼就是這 24 行。`signal: 健康` 尤其容易誤讀成「這個功能很健康」 |
| 2 | L36 | 「**子頁** SDK v1.5.0 為 Managed Agents 加 auto mode」 | 「子頁」是本庫的頁面階層術語，不是讀者概念 |
| 3 | L42 | 「Managed Agents 這個平台產品本身的現況……在**子頁**」 | 同上 |
| 4 | L226 | 「成本對照的唯一第三方數字，**本庫未採信**」 | 「本庫」＝這個 wiki 的自稱。判斷本身很有價值，措辭是內部視角 |
| 5 | L48 / L233 | 「**逐則記錄在** community-tech-patterns，本頁不重述」 | 「本頁不重述」是編輯紀律的自我說明，對讀者是雜訊（指路留著就好） |
| 6 | L250 | 子頁表第一列頁名寫「**本頁**」 | 表格要給讀者看，第一格應該是頁名不是代名詞 |
| 7 | L267–271 | 「**時序**」區塊：「建頁」「選型表與積木架構自 managed-agents **移入**並增補」「改以『一塊積木一張卡』**重寫**」 | 記的是編輯史不是功能史。讀者想看的是功能什麼時候變的，不是這頁什麼時候被改寫的 |
| 8 | L269 | 「2026-09-10：**建頁**」 | 同上，最刺眼的一筆——頁面誕生日被當成事件寫進時序第一行 |

（附帶：連到的 `entities/managed-agents` L62 有一整段 `%% 維運備忘 %%`，裡面出現 `python scripts/news_mentions.py`、`docs/page-audits/ledger.md`、「上限式判準是否成法……待裁決」。在 Obsidian／網站上會被剝除，但讀原始檔的人看得到。不計入本頁 8 條。）

---

## 撐不起的句子（寫了但讀者無法照做／無法驗證）

5 條，依嚴重度排：

1. **L97「（或個人目錄）」** — 沒給路徑。這是全頁唯一一個「我想照做但做不了」的點。
2. **L95「prompt 帶 `ultracode`……`/effort ultracode`」** — `ultracode` 全頁孤立出現一次，沒定義、沒指路。讀者只能猜它是 effort 等級。
3. **L118「上限 16 路並行（v2.1.269 起可用 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 提到 256）」** — 三個數字（16／256／1,000 agent／4,096 項）一口氣丟出，沒說我怎麼知道自己撞到哪一條、撞到會怎樣（報錯？排隊？）。
4. **L222 選型表「同一 session 內可續跑（**已完成 agent 吃快取**）」** — 「吃快取」是什麼機制、省的是錢還是時間、要不要我做什麼，一概沒有。而 L62 又說 `/goal` resume「token 基線歸零」，兩處對「續跑省不省」的暗示方向相反。
5. **L175「帳號預設可用，請求帶 `managed-agents-2026-04-01` beta header 即可開始」** — 「即可開始」但這裡沒有任何一行可貼的請求範例（本頁其他七塊積木都有指令）。第七塊是唯一沒有可貼指令的積木卡，格式在這裡破掉一次。

---

## 最想改的三件

1. **補完 script 那節的「怎麼存」** — L97 把「（或個人目錄）」換成實際路徑，並補一句「存檔後 `/檔名` 就是指令、`meta.name` 要跟檔名一致」。這是唯一擋住冷讀者照做的缺口，一行就補得起來。
2. **「怎麼疊」那節補一列「agent teams ＋ 跨 session 傳訊」** — 四條規則只講了 workflow 相關的疊法，Q3 這組最常一起被想到的搭配沒有任何一句正面說明「合起來能做什麼」（只有 L238 的架構歸類與「傳訊層無編排」的否定句）。若官方確實沒寫，就在 L193 那句「其餘組合官方沒寫」下面明點一句「含 agent teams × 跨 session 傳訊」，讓讀者的問題被承認、而不是找不到。
3. **時序區塊只留功能史，編輯史移走** — L267–271 四筆裡有三筆在講這頁自己被怎麼改（建頁、移入、重寫），只有 09-10／09-11 那兩筆前半是真的功能變動。讀者在時序裡找「這塊積木什麼時候變的」，撞到的是「這頁什麼時候被重寫」。順手把 L250 表格第一格的「本頁」換成頁名、L36／L42 的「子頁」換成頁名。

---

## 四題總表

| 題 | 路徑 | 跳數 | 結果 | 卡點行號 |
|---|---|---|---|---|
| Q1 dynamic workflows 為什麼出 | index → anthropic-agent-stack | 1 | 拿到 | L95（`ultracode` 未定義，不影響答案） |
| Q2 subagent＋workflows 能跑什麼 | index → anthropic-agent-stack | 1 | 拿到（「存哪」半拿到） | L97「（或個人目錄）」 |
| Q3 agent teams＋跨 session 傳訊 | index → anthropic-agent-stack | 1 | 半拿到 | L238、L141 |
| Q4 三頁分不分得出差別 | index → stack → guide／managed-agents | 2 | 拿到，三頁分得出 | 無 |

**入口：** index L30（開發實務入口表「我想讓 agent 自己跑幾小時／過夜」），L102 Topics 表為第二入口，兩者一致。
**分不出差別的兩頁：** 無。
