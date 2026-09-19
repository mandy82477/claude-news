# 第 14 波冷讀者複驗（2026-09-19 走查，記錄日 2026-09-20）

走法：唯一入口 `wiki/index.md`，只沿 `[[連結]]` 走，只用 Read。行號＝檔案原始行號（含 frontmatter）。
實際開過的頁（依序）：① `wiki/index.md` ② `wiki/entities/claude-code.md` ③ `wiki/topics/official-community-gap.md` ④ `wiki/topics/community-tech-tools.md` ⑤ `wiki/topics/skill-interest-watch.md` ⑥ `wiki/topics/anthropic-agent-stack.md`

---

## Q1：Claude Code 讀不讀 AGENTS.md？官方有表態嗎？

**路徑**：index → entities/claude-code → topics/official-community-gap　**跳數：3**　**結果：拿到**

- 在 index 我先找「跨工具／設定檔互通」那一列——**沒有**。13 列導覽表（index:26–32）沒有任何一列長得像我的問題，所以我退而點 Entities 表裡最像主角的 `[[entities/claude-code]]`（index:42，摘要寫「功能、已知問題、社群工具」）。
- claude-code 頁 862 行，我讀了開頭 157 行＋第二段 120 行，**沒有 AGENTS.md**。「最新動態」（claude-code:35–38）與版本表（claude-code:45–51）最新只到 **v2.1.276（09-18）**。我放棄這頁，改點該頁「市場與競爭」段裡指出去的 `[[topics/official-community-gap]]`（claude-code:88）。
- 答案在頁頂 callout 第一句：**「Claude Code v2.1.277（09-18）起原生讀 `AGENTS.md`」**（official-community-gap:34），邊界三條在 official-community-gap:115–117。

**卡住我的原句**

- `claude-code.md:36` 「**v2.1.276**：修復 2.1.275 一項迴歸……純 bug 修復。」——09-18 的重點被寫成一則 proxy bug 修復，同一天出的 v2.1.277／AGENTS.md 這頁完全沒有。我差點在這裡下結論「官方沒動作」。
- `index.md:42` 「Claude Code CLI 主頁：功能、已知問題、社群工具」——「主頁」暗示什麼都查得到，實際是一份 800 多行的 issue 清單。

---

## Q2：Max 個人用戶想在額度用完前收到提醒，官方有沒有？要裝哪個社群工具？

**路徑**：index → claude-code → official-community-gap → community-tech-tools → skill-interest-watch　**跳數：5**　**結果：半拿到**

- 官方側拿到：`/usage` 可拆到 skill／子代理／MCP server，狀態列可讀 `rate_limits.five_hour.used_percentage`，VS Code 有 70% 警示橫幅（official-community-gap:57、111–114）。
- **沒拿到的是我真正問的那一半**：official-community-gap:114 寫「沒有主動推到手機或桌面的額度告警、門檻**似乎**不能自訂（官方文件未見此設定，不是官方明說沒有）」。同頁只給了兩個工具名 **LimitBar、CCLimitPing**（official-community-gap:114），沒有證據等級、沒有安裝方式、沒有兩者分界。
- 我照該頁指示（official-community-gap:41「要裝哪個社群工具，答案不在本頁——看 [[topics/community-tech-tools]]『我卡在這裡』」）跳過去，**決策表九列裡沒有我的症狀**：最接近的是「帳單爆了，看不到錢花在哪 → tare」（community-tech-tools:53），那是事後歸因，不是事前提醒。LimitBar／CCLimitPing 在那頁的決策表與 125 列工具目錄都沒出現。
- 再跳 skill-interest-watch 想找「費用／額度」類別的規模榜——**沒有這個類別**（該頁只有專案設定、codebase 探索、規劃、攔錯、code review、測試、除錯、規則維護、multi-agent、git 衛生、知識庫共 11 節）。

**卡住我的原句**

- `official-community-gap:114` 「門檻**似乎**不能自訂（官方文件未見此設定，不是官方明說沒有）」——誠實，但我無法據此行動。
- `community-tech-tools:53` 「帳單爆了，看不到錢花在哪」——症狀表用的是「錢」的語言，我的痛是「額度」；兩者在 Max 訂閱下不是同一件事，表上沒有任何一句幫我分辨。

---

## Q3：哪些痛點官方還沒做、值得投入？哪些已經做掉、不要碰？

**路徑**：index → claude-code → official-community-gap（Q1 已在此頁）　**跳數：3**　**結果：拿到**

- 主表一眼可用（official-community-gap:53–67）：❌ 只剩「想在一個地方操作好幾家 agent」（:55）；🧪 六列；✅ 六列。要避開的三件寫得最清楚：AGENTS.md（:63）、通知（:64）、subagent 編排（:65）都已出貨。
- 加分的是 official-community-gap:73–85「官方為什麼還沒補」——把花費估不準說成商業模式而非技術問題（:77），這是我會拿來做決定的那一段。

**卡住我的原句**

- `official-community-gap:43` 「13 個痛點裡，**1 個**官方目前沒有任何對應」vs `official-community-gap:139–141` 對照矩陣又列了兩個 ❌（CLAUDE.md 規則失效、AI 輔助開發副作用），且 `:75` 自己說「上面那個 ❌、下方對照表裡的**兩列**」。同一頁對「還有幾個空位」給 1 和 3 兩個答案。
- `official-community-gap:66` 「它會不會跑出破壞性指令」核對日是 `—`，而表頭（:50）說 `—` 代表「還沒對過，要拿它做決定時建議自己再查一次官方文件」——一列標 ✅ 卻沒人對過官方。

---

## Q4：官方 Dreaming 能不能用？跟社群記憶工具比我選哪個？

**路徑**：（承 Q1 的 official-community-gap）→ community-tech-tools → skill-interest-watch → anthropic-agent-stack　**跳數：6**　**結果：拿到（但有一處被漏掉的反證）**

- **Dreaming 不是給我的**：它屬 Managed Agents（API 產品），在 beta 之內還是**須另外申請的研究預覽**（official-community-gap:105、166；anthropic-agent-stack:180、244）。
- **給 Claude Code 使用者的官方答案是 auto memory**：依更正與偏好自己寫筆記、`/memory` 管理、子代理各一份、跨 worktree 共享（official-community-gap:56、104）；要自己接外部記憶層有 `PreCompact`／`PostCompact`／`SessionStart`／`SessionEnd` 四個 hook（:106）。
- **社群選哪個**：單機選 brain.md，團隊共享選 OzBrain，已在用 Obsidian 選 VIR（community-tech-tools:56、74）。

**卡住我的原句（這題最嚴重）**

- `official-community-gap:166` 「Claude Code 自己的官方記憶是 auto memory……**這一面已補**」——但我在 claude-code 頁看到 auto memory 現在有三個未修 bug：`autoMemoryEnabled=false` 抑制不了 11–16k token 前導文字（claude-code:214）、session 無從得知記憶索引是完整載入還是截斷（claude-code:215）、壓縮提醒門檻寫死（claude-code:216）。gap 頁一個字都沒提。
- `claude-code.md:255` 「⛔ 官方拒修（NOT_PLANNED，2026-05-25）｜跨 session 持久記憶（#14227）」vs `official-community-gap:56` 同一件事標 🧪。兩頁我都讀了，仍說不出「官方到底有沒有打算做跨 session 記憶」。

---

# 四題走完後的五個回答

## 1. 入口：index 有沒有一列讓我一眼知道去哪？

- **Q3 有**（index:109「社群喊的痛，官方補了哪幾個……」），一點就中。
- **Q1、Q2、Q4 都沒有**。Q1 是跨工具設定檔互通，13 列導覽表（index:26–32）沒有這個維度；Q2 的「額度」只在 Entities 表 `[[entities/pricing]]`（index:46）的摘要裡出現「計費規則」，看起來像政策不像工具；Q4「跨 session 記憶」在 index 全表找不到任何一列。
- **誤導過我的一列**：`index.md:27` 「我卡住了……**社群首選**是哪個 → [[topics/skill-interest-watch]]「我卡在這裡」決策表」。我照這條走，但真正維護那張表、有推薦細節與分界說明的是 `topics/community-tech-tools`（community-tech-tools:47–74）。index 把讀者送到副本、不是正本。index:22 那句「讀者只需看總覽一頁」讓這個誤導更硬。

## 2. 我分不出差別的兩頁

**`topics/community-tech-tools` vs `topics/skill-interest-watch`。**
兩頁都有一節叫「我卡在這裡」，表頭四欄一模一樣、九列內容逐字相同（community-tech-tools:51–63 ≡ skill-interest-watch:44–56），連圖例段都一字不差。我是讀到 skill-interest-watch:42「本表每日同步自 [[topics/community-tech-tools]]（判斷與證據的家；改判斷請改那頁）」才知道它們是正副本關係——而那句話是寫給維護者的，不是寫給我的。我到現在也說不出「什麼情況我該開 A、什麼情況開 B」，只知道 B 多了星數榜，而 B 自己又說「星數是規模不是品質，榜不做推薦」（skill-interest-watch:36）。

## 3. 我最常落腳的那一頁

**`topics/official-community-gap`**（四題有三題落在這裡）。它讀起來**像雷達，不像百科**——這是全程最好的一頁：

- official-community-gap:53–67 一張表 13 列，每列都用「你痛的是什麼／官方補了沒／還缺什麼、你現在能怎麼辦／核對日」，最後一欄直接給我可行動的東西。
- official-community-gap:50 明寫核對日的定義與 `—` 的意思，我知道哪一列可以信。
- official-community-gap:73–85「官方為什麼還沒補」給的是判斷不是流水帳。

雷達感被兩件事拖累：頁尾「時序」（official-community-gap:197–266，全頁 70 行、約四分之一）是純編輯部流水帳；以及 ⟨G-01⟩–⟨G-13⟩ 的代號（:55–129），我要在表格與細節之間來回對號。

## 4. 看不懂的內部用語／維運口吻

| # | 頁名:行 | 原句 | 為什麼卡住 |
|---|---|---|---|
| 1 | claude-code:55 | 「❓ **待查證**（標 2026-09-18｜查 claude-projects、Claude Code Projects｜複 2026-10-02）」 | 「標／查／複」三個單字縮寫全頁沒有圖例 |
| 2 | claude-code:246 | 「🔎 **查無官方**（標 2026-08-09｜查 #60705、stop-hook｜複 2026-10-13｜**訊** 2026-09-16）」 | 又多一個「訊」，更猜不到 |
| 3 | claude-code:127 | `%% 上方「現在還沒修好的」為本組的結論層索引，非搬移 %%` | 維運備忘直接漏在正文裡 |
| 4 | claude-code:263 | `%% 2026-08-08：五家媒體同步報導……08-08「changelog 未見對應」為當時漏看 %%` | 整段編輯部自我檢討 |
| 5 | 每頁:1–24 | `pending_count: 27`／`pending_overdue: 21`／`signal: "健康"`／`generated_by:` | 開頁先看到 24 行內部欄位；「signal 健康」是誰健康？ |
| 6 | official-community-gap:55–129 | 「⟨G-11⟩」「⟨G-05b⟩」「⟨Q-01⟩ 結案」 | 三套代號、三種語意，讀者沒有對照表 |
| 7 | index:5 | 「不收：快變事實（日期／熱度／近況→頁面標頭，**盤點用 Grep**）」 | 對我講的是維護規則，而且 Grep 我在網站上做不到 |
| 8 | index:88 | 「Topics 頁面本身無「類型」欄位，故表格僅三欄……為**刻意設計差異**」 | 編輯部在向自己交代，讀者不需要知道 |
| 9 | skill-interest-watch:117/166 | 「**本庫尚無判斷**（榜上無 🧭 條目）——星數不是推薦，裝前自行查證」 | 「本庫」「🧭」是內部詞；整節等於沒有結論卻佔一整塊版面 |
| 10 | community-tech-tools:36 | 「決策表本輪**無變動**（無新證據推翻現有首選）」 | 「本輪」是編輯周期，讀者只想知道現在該裝什麼 |

## 5. 撐不起的句子 / 互相矛盾

1. **同一頁對「還剩幾個空位」給兩個數**：official-community-gap:43「1 個官方目前沒有任何對應」vs :75「上面那個 ❌、下方對照表裡的**兩列**」＋ :139–141 兩個 ❌ = 實際 3 個。
2. **跨 session 記憶，兩頁兩個狀態**：official-community-gap:56 標 🧪（已補 auto memory）vs claude-code:255「⛔ 官方拒修（NOT_PLANNED，2026-05-25）」。
3. **「這一面已補」下得比證據硬**：official-community-gap:166 稱 auto memory「這一面已補」，但 claude-code:214–216 有三則 auto memory 未修 bug（停用不生效、載入狀態不可知、門檻寫死），gap 頁未收。
4. **同一天的版本事實兩頁不一致**：official-community-gap:34「v2.1.277（09-18）起原生讀 AGENTS.md」vs claude-code:36/45 最新版本停在 v2.1.276（09-18），全頁無 v2.1.277。
5. **✅ 卻沒核對日**：official-community-gap:66 破壞性指令列狀態 ✅、核對日 `—`，與 :50 的自訂規則（`—` ＝ 還沒對過，決策前請自查）直接衝突。
6. **推播能力自我打架**：official-community-gap:114「沒有主動推到手機或桌面的額度告警」vs 同頁 :102「接上 Remote Control 後長任務結束或需要你決定時推手機通知」——推播通道存在，只是不接額度事件，這一層差別沒寫出來。
7. **入口指向不一致**：index:27 把「我卡在這裡」指向 skill-interest-watch，official-community-gap:41、:91 兩次指向 community-tech-tools，而 skill-interest-watch:42 說判斷的家在 community-tech-tools。

---

# 只能改三件，我改這三件

1. **補 v2.1.277／AGENTS.md 進 `entities/claude-code`，並讓 index 有一列答「跨工具互通」**。現在同一天的官方版本在兩頁講不同的話（gap:34 vs claude-code:36），而 index 的 13 列導覽表沒有任何一列接得住「我同時用 Cursor／Codex／Claude Code」這種問法——這是我四題裡唯一必須靠運氣跳對頁才拿到的答案。
2. **「我卡在這裡」只留一個入口**。把 index:27 改指 `topics/community-tech-tools`（判斷與證據的家），並在 skill-interest-watch 頁頂第一行直說「這是決策表的每日副本＋星數榜，要看推薦細節與分界請去正本」——現在兩頁九列逐字相同，我讀完仍說不出該開哪一頁。
3. **把維運標記移出讀者視線**。`%%…%%` 備忘（claude-code:127、263）、24 行 frontmatter、「標／查／複／訊」縮寫、⟨G-nn⟩／⟨Q-nn⟩ 代號——四類東西合計佔掉我不少閱讀預算，卻沒有一項是為我寫的。至少給一行圖例，最好是根本不輸出給讀者。

**順帶一提（不列入三件）**：Q2「額度快用完想收提醒」是我四題裡唯一沒答完的。官方側的缺口寫得清楚（gap:114），但兩個社群工具名（LimitBar、CCLimitPing）沒進決策表、沒有證據等級——建議在 community-tech-tools 決策表加一列「額度快爆，想在斷線前收到提醒」，或明寫「這一格本庫還沒判斷」。
