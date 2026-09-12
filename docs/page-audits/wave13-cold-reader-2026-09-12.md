# Wave 13 冷讀者實測 — topics/anthropic-agent-stack（2026-09-12）

讀者設定：第一次打開這個知識庫的工程師。只從 `wiki/index.md` 出發，只沿 `[[wikilink]]` 前進。行號皆為該檔 `cat -n` 行號。

---

## 入口

**找得到，但不是首屏第一眼。** index 首屏（L1–21）是「角色／收／不收／讀法」的維運說明＋概覽三列（overview、feature-radar、feature-radar-archive），沒有一列提到 agent。

真正把我帶進去的是 **index L30**：

> 「我想讓 agent 自己跑幾小時／過夜，該用哪個（`/goal`、subagent、dynamic workflows、Managed Agents、Agent SDK）」→ `[[topics/anthropic-agent-stack]]`「你該用哪個」

這一列在「💻 開發實務入口」表的第 5 列，而該表前面壓了一段 L22 的長體例說明（130+ 字，講「只放答怎麼做的頁面」「工具判斷由社群工具目錄每週整理」）——那段是寫給維護者的，冷讀者要先跳過它才看得到表。Entities 表（L40–75）與 Topics 表（L85–110）都在更下面，`[[topics/anthropic-agent-stack]]` 的 Topics 列（L102）我是進去之後才回頭看到的。

**評價：** 入口存在且措辭是對的（用「我想……」的讀者語言），但被體例說明擋了一層。

---

## 四題實測

### Q1 dynamic workflows 官方為什麼出，沒有它之前會撞到什麼牆？

- **路徑：** index → topics/anthropic-agent-stack
- **跳數：** 1
- **結果：✅ 拿到**
- **答案一句：** 沒有它之前，多個 agent 之間只能互傳純文字訊息、訊息不帶依賴語意，所以排不出「誰先誰後」；dynamic workflows 把編排從 Claude 逐回合的臨場判斷，換成一支持有整個計畫、可存檔重跑、中間結果不進主對話 context 的 JavaScript script。
- **證據行：** L41（摘要：「先前 agent 之間只能互傳訊息、沒辦法排定誰先誰後」）、L81（第三層完整敘述＋四原語）、L83（「原始需求（issue #24798，75 則留言）要的『依相依性排序高階流程步驟』如今由第三層的 workflows 以 script 承接」——這一句是全頁最有說服力的「撞到什麼牆」證據，因為它指得出社群原始工單）。
- **備註：** 這題答得好的原因是 L83 把「牆」寫成了一個可查的 issue 編號＋留言數，而不是形容詞。全頁最該保留的一句。

### Q2 我現在用 subagent 加 workflows 能跑出什麼具體工作流？要一個能照做的場景，附最小指令。

- **路徑：** index → topics/anthropic-agent-stack →（回 index）→ topics/coding-workflow-guide →（回 index）→ feature-radar
- **跳數：** 1（主要答案來源）＋2 次回頭確認，共 3 頁
- **結果：🟡 半拿到**
- **拿到的部分：** 觸發方式有（L66：prompt 帶 `ultracode` 關鍵字或直說「use a workflow」；存成指令放專案 `.claude/workflows/` 或個人目錄；內建範例 `/deep-research`）、四個原語名稱有（L65：`agent()`／`parallel()`／`pipeline()`／`phase()`）、上限有（L67：16 路並行、單次 1,000 agent）、續跑語意有（L67）。
- **卡住的原句與行號：**
  - L81：「社群拿它玩出什麼配置，**尚無社群配置回報**（2026-09-10）。」——這是全頁對 Q2 最直接的回答，而它的內容是「沒有」。誠實，但讀者的問題沒被解掉。
  - L65：「JavaScript script 持有整個計畫（`agent()`／`parallel()`／`pipeline()`／`phase()` 四原語）」——**四個原語只有名字，沒有任何一行實際 script**。我知道有 `pipeline()`，但不知道它接什麼參數、script 檔長什麼樣、放哪個檔名、存進 `.claude/workflows/` 之後用什麼指令叫它。
  - L66：「跑得好的 script 可存成指令……重複執行」——「跑得好的 script」預設我已經有一支，但本頁從沒教過怎麼產生第一支。
- **對照：** 同一頁對別的積木是有最小指令的（L60 `/goal` 給了「最小用法 `/goal npm test 執行結果零失敗`」；L64 `--agent` 搭 `--name`）。feature-radar 對跨 session 傳訊也給了程式碼區塊（feature-radar L522–527）。**唯獨 dynamic workflows 沒有。** 這是本次實測最明確的單一缺件。
- **順帶撞到一個矛盾：** feature-radar L227 把 Dynamic Workflows 列為「🔥 ／ ❌ 暫不推薦 ／ **Research Preview**」（2026-05-28，UltraCode 1.7M token bug 無退款），而 anthropic-agent-stack L54 寫「✅ **全部付費方案**（Pro 需在設定開啟；2026-09-10 查證）」。兩頁狀態不一致，且互相沒有指認對方、沒有一句「05-28 的 Research Preview 已於 X 日升格」。冷讀者兩頁都讀完後，不知道自己現在到底能不能用。

### Q3 agent teams 加跨 session 傳訊讓我多做什麼，跟 subagent 差在哪？

- **路徑：** index → topics/anthropic-agent-stack（第二層 L79 ＋第四層 L83）；補充 index → feature-radar（L513–529）
- **跳數：** 1
- **結果：✅ 拿到（差異軸清楚，但「多做什麼」偏弱）**
- **答案一句：** subagent 是**單向扇出**——主 agent 分配、收回結果，分身之間沒有通道，所以不會協調也不會互相覆蓋（代價是重複工作，L79）；agent teams ＋ `SendMessage` 是**點對點傳訊**——分身之間可以直接對話，但只傳純文字、不傳對話歷史與檔案，且訊息不帶依賴語意，所以傳訊層自身仍無編排（L83）。
- **最有用的一句：** L83「**傳訊層自身仍無編排**——訊息不帶依賴語意，teams 也還是實驗性」。這句同時回答了「差在哪」與「別期待什麼」。
- **弱的地方：** 「多做什麼」只拿得到能力描述，拿不到場景。L83 唯一的具體畫面是社群工具（Concord、cumora），不是我自己能做的事。要到 L64 才有半個場景：「`--agent` 搭 `--name` 可組出長駐領域專家：別的 session 用傳訊丟任務給他、隔天 `--continue` 接續，context 不歸零」——**這句其實是全庫對 Q3 最好的答案，但它被埋在「選型細節」的第 5 個 bullet，而不是在講傳訊的第四層。** 位置錯了。
- **另一個要自己拼的點：** agent teams 是實驗性、預設關閉（L83），但**怎麼打開沒寫**。L83 說「互動 session 下的 agent teams（實驗性、預設關閉）」，讀者拿不到開關名稱。

### Q4 這頁跟 topics/coding-workflow-guide、entities/managed-agents 三頁分不分得出差別？

- **路徑：** index → topics/anthropic-agent-stack → entities/managed-agents（L35／L97／L103 三處都連得到）；index → topics/coding-workflow-guide
- **跳數：** 1–2
- **結果：🟡 半拿到——三頁中兩頁分得清楚，一對分不清楚**

**分得清楚的：**

| 頁 | 我讀完後會怎麼一句話描述它 |
|---|---|
| `topics/anthropic-agent-stack` | 「五種官方 agent 形態該選哪個（選型表）＋它們怎麼疊成六層架構」 |
| `topics/coding-workflow-guide` | 「一條開發流程九個階段，每階段官方給了什麼、社群補了什麼、還缺什麼」 |

這兩頁的分界是**「按 agent 形態切」vs「按流程階段切」**，而且兩邊都明說了：agent-stack L107 寫「`[[topics/coding-workflow-guide]]` —『我在做這件事該用哪個』的流程視角」，coding-workflow-guide L77 反向指回「各選項的分界見 `[[topics/anthropic-agent-stack]]`」。互相指認、措辭一致，**這一對做得很好，是本庫該當範本的寫法。**

**分不清楚的一對：`topics/anthropic-agent-stack` ↔ `entities/managed-agents`。**

- index L102 把 managed-agents 標成 agent-stack 的「↳ 子故事」，frontmatter 也是 parent/child（agent-stack L11、managed-agents L11）。結構上清楚。
- 但**內容切分反直覺**：Managed Agents 的**計費算式與官方算例住在母頁**（agent-stack L68、L69，$0.08／session-hour、Opus 5 一小時 ≈ $0.705），子頁 L59 還要寫一句「**計費算式與官方算例……見上層**」把讀者送回去。同時母頁 L55 的選型表格裡又已經寫了「token 牌價＋$0.08／session-hr」。
- 結果是：想知道 Managed Agents 多少錢，我在兩頁之間來回三次（母頁表格 L55 → 子頁 L59 的指路 → 母頁 L68–69）。**一個事實（計費）在兩頁各有一部分，還附一句互相指路。**
- 兩頁還各有一份「什麼時候適合用它」：母頁 L55「要跑數小時以上並跨 session 保留狀態，或需 20 路並行、資料不出境」、子頁 L56–57「最適合／不適合」欄。措辭幾乎同義。
- **判斷：** 分界規則寫得出來（「產品本身的現況／零件成熟度／歷史在子頁，跨形態的選型與計費在母頁」），但這條規則不符合讀者的提問形狀——沒有人會先問「這是選型問題還是產品問題」再決定點哪頁。

---

## 這頁是「雷達」還是「百科」？

**是百科，而且是好的百科——但頭上戴了一頂雷達的帽子。**

百科的證據：全頁主體（L45–89）在回答「這是什麼、為什麼這樣、該怎麼挑」，六層架構每層都寫「官方現在給了什麼／agent 之間怎麼互動／社群玩出什麼」，是穩定的結構知識，不是本週新聞。L75 的導讀句（「一層比一層外——你多半是從第一層開始，撞到牆才往下一層走」）是典型百科筆法。L89 的 hooks 判斷式（「你要的是多一個 agent，還是要在現有 agent 的某個動作前後插一句話？」）同樣。

雷達的帽子：L34–35 的「最新動態」callout 是 **09-11 SDK 版號**，內容自陳「積木架構本身無變動」——也就是這頁的主體這一天沒動，callout 講的是子頁的事。冷讀者打開第一眼讀到的是「anthropic-sdk-python v1.5.0 為 Managed Agents 新增 auto mode 工具權限設定」，這對「我該用哪個 agent」的讀者零價值，還先消耗了他一格注意力。

**建議的定性：** 這頁應該自我定位成百科，callout 位置讓給一句「這頁在回答什麼」（coding-workflow-guide L35–38 就是這樣做的，效果明顯較好）。最新動態若要留，降到時序節。

---

## 內部用語外洩（冷讀者看不懂的詞）

1. `topics/anthropic-agent-stack` L2–23 — 整段 frontmatter（`page_role: "hub"`、`days_since_news_subtree`、`inbound_links`、`attribution_count`、`top_source: "user-query"`、`pending_overdue`、`signal: "健康"`、`generated_by`）。我在 Obsidian／原始檔打開這頁，第一屏全是這個。沒有一個詞對讀者有意義。
2. `topics/anthropic-agent-stack` L48 — `%% 維運備忘：分界只填查得到出處的欄位……2026-09-10 冷讀者驗收後移入備忘 %%`。「冷讀者驗收」是本庫的內部流程名詞。（註：網站版會剝除，但 Obsidian 與原始檔讀者看得到。）
3. `entities/managed-agents` L62 — 同上，`%% 維運備忘：2026-09-05 頁面健檢一次性下修。量測：python scripts/news_mentions.py --since 4w --any ... 現行「連續 4 週零命中 −1 格」……上限式判準是否成法見 docs/page-audits/ledger.md 待裁決。%%` 出現了腳本名、內部評分規則、內部待裁決檔路徑。
4. `entities/managed-agents` L123、L145 — `⟨Q-02⟩`、「**懸置細節**」、「標 2026-08-10｜查 anthropic-sdk-python」。「懸置」與 `⟨Q-nn⟩` 是本庫的待辦編號體例，讀者無從理解那個角括號是什麼。
5. `index` L46、L65、L89 等 — 「↳ **子故事**：」。讀者不知道「子故事」是本庫的階層術語還是內容描述。
6. `topics/coding-workflow-guide` L231、L342、L408 — `` `[已深查]` `` ；L476、L497 — `` `[社群面待補]` `` ；L385、L445、L517 — `` `[已補：庫內證據]` ``。這是查證流程的內部標記，掛在讀者要點的 h2 標題上。L99 雖有一整段解釋，但那段在第 99 行，標記從第 231 行才開始出現，讀者未必記得。
7. `topics/coding-workflow-guide` L41 — 「## **本週 coding 亮點**」。「coding」作為一個領域代號（對應某位記者的認領範圍）是內部語；讀者眼中這一節與整頁的關係不明——它是十則跨頁摘要，跟本頁「九階段流程」的主體沒有結構關係。
8. `topics/anthropic-agent-stack` L47 — 「每格分界都附得出出處，查不到的留 `—` 或標為**待查證**。」這是寫給編輯的填表方針，不是寫給讀者的。
9. `index` L81 — 「Topics 頁面本身無『類型』欄位，故表格僅三欄……為**刻意設計差異**（Entities 四欄含類型）」。純維護者對話，佔掉 Topics 表正上方的位置。
10. `feature-radar` L18 — `%% 09-02 換上 Fable 5.1……照 wiki-ingest-features.md §7(c) 覆寫 %%`，出現規則檔章節號。

---

## 撐不起的句子（讀起來像結論，但沒給證據）

1. `topics/anthropic-agent-stack` L41／index L102 — 「編排缺口已**被補上大半**」。「大半」是量詞，但全頁沒有任何東西量過缺口的大小。L83 反而寫「傳訊層自身仍無編排」，兩句放一起讀，「大半」到底指多少無法判斷。
2. `topics/anthropic-agent-stack` L89 — 「hooks……**不打開任何新架構**」。這是一句強斷言（全稱否定），沒有附出處或推論過程，而同頁其他每一格都自我要求「附得出出處」（L47）。
3. `entities/managed-agents` L46 — 「獨立第三方生產環境回饋**至今為零**」。零命中是最難證的一種主張。頁面正文沒說這個「零」是怎麼掃出來的（掃了哪些來源、哪段期間）；量測方法被藏在 L62 的維運備忘裡，而且那段量的是「提及次數」不是「生產環境回饋」，對不上。
4. `topics/coding-workflow-guide` L97 — 「評的是同一件事，**九段用同一把尺**」。宣稱九段評分一致，但那把尺（🟢／🟡／🔴 的判準）只寫了一句同義反覆（「讀者實際拿不拿得到可執行答案」）。同頁 L99 自己承認「第 6、7、8 段只掃過官方文件」，證據深度不同卻共用一把尺，這句與 L99 互相削弱。
5. `feature-radar` L518 — 「是 multi-agent 協作基礎設施的**重要一步**」。評價語，唯一的支撐是「5 家媒體同日報導」＋「官方文件驗證存在」，兩者都只證明這功能存在，不證明它重要。

---

## 最想改的三件事

### 1. 給 dynamic workflows 一支最小可跑的 script（Q2 的唯一缺件）

`topics/anthropic-agent-stack` L65–67 有四個原語的名字、有觸發詞、有上限、有續跑語意，**就是沒有一行 script**。同一頁的 `/goal` 有最小用法（L60）、`--agent` 有指令（L63–64），feature-radar 對跨 session 傳訊也有程式碼區塊——dynamic workflows 是唯一一個「讀完知道它存在、但打不開第一步」的積木。

建議補在 L67 之後，形狀對齊 L60 的「最小用法」：一支 8–12 行的 script（一個 `parallel()` 扇出 ＋ 一個 `pipeline()` 收斂就夠）、檔案放哪（`.claude/workflows/<名>.js`）、怎麼叫它跑、進度在哪看（`/workflows`）。**不必等社群配置回報**——官方文件本身就足以撐起一個最小骨架，而 L81「尚無社群配置回報」不該是「所以讀者拿不到範例」的理由。

### 2. 修掉 dynamic workflows 的狀態矛盾，並在兩頁互相指認

`feature-radar` L227：Research Preview ／ ❌ 暫不推薦（2026-05-28）。
`topics/anthropic-agent-stack` L54：✅ 全部付費方案開放（2026-09-10 查證）。

兩頁都是現行頁、都沒有標示對方存在。冷讀者照 index 的路由先讀 feature-radar 會得到「別碰」，先讀 agent-stack 會得到「可以用」。至少要：feature-radar 該列補一句升格日期＋指向 agent-stack；agent-stack L54 補一句「05-28 曾為 Research Preview（含 1.7M token 退款爭議），X 日起開放全付費方案」——那個退款爭議對要不要開 1,000 個 agent 的人是關鍵資訊，目前只活在 feature-radar 的表格括號裡。

### 3. 把「進了門的第一眼」讓給讀者

三個地方同一個病：讀者的第一屏被維護者的話佔走。

- `topics/anthropic-agent-stack`：L34–35 的最新動態 callout 講的是子頁的 SDK 版號，自陳「積木架構本身無變動」。換成一句「這頁在回答什麼」（照 coding-workflow-guide L35–38 的做法），把 09-11 那則降到時序節。
- `index` L22：「開發實務入口」表前的體例說明壓著表格，把 L30 這個真正的入口推下去。體例說明搬到表後或改成 `%% %%`。
- 全庫的 frontmatter（如 agent-stack L2–23、managed-agents L1–25）：23 行機器欄位擋在標題前。網站版有處理，但 Obsidian 讀者與任何直接讀檔的人第一眼看到的就是 `signal: "健康"`。

**外加一件（順位第四，但成本最低）：** 把 `topics/anthropic-agent-stack` L64 那句「`--agent` 搭 `--name` 可組出長駐領域專家：別的 session 用傳訊丟任務給他、隔天 `--continue` 接續，context 不歸零」從「選型細節」的第 5 個 bullet **移進第四層（L83）**。那是全庫對「跨 session 傳訊讓我多做什麼」最具體的一個場景，現在放錯了段。

---

*本檔為冷讀者實測記錄，未修改任何 wiki 檔案，未 commit。*
