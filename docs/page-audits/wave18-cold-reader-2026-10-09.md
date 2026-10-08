# Wave 18 冷讀者實測（2026-10-09）

讀者設定：第一次來、用 Claude Code 寫程式的工程師。只從 `wiki/index.md` 出發，沿 `[[連結]]` 一頁一頁點；index 算第 1 跳，頁內捲動與頁內搜尋不算跳。行號是 Read（cat -n）顯示的行號。

## 四題結果

| 題 | 路徑 | 跳數 | 結果 |
|---|---|---|---|
| Q1 多 agent 分工 | index → community-pattern-trends → community-large-codebase-workflow | 3（走 index L32 直達只要 2） | 拿到 |
| Q2 跨 session 記憶 | index → community-pattern-trends（趨勢九）→ community-large-codebase-workflow（第 3 線） | 3 | 拿到（「收斂了沒」要自己判斷） |
| Q3 寫 skill 的慣例／反模式 | index → entities/claude-skills → community-tech-patterns → coding-workflow-guide → community-tech-tools | 5 | 半拿到 |
| Q4 2026-09 hooks／plugin／MCP 新東西 | index → feature-radar → community-pattern-trends → community-tech-patterns | 4 | 半拿到 |

### Q1 答案
每個 agent 開一個 worktree 做隔離，官方已內建（`claude --worktree`、subagent 設 `isolation: worktree`）。審查者只掛 Read 工具，不靠角色描述；commit 走合併佇列依序落地。10 個以上要一段一段加、每段自己量。
- 證據：large-codebase L47、L59–62、L66；trends L106–114。
- 卡住的地方：trends L91 的標題是「趨勢二：Multi-agent 隔離工程化」，但「現在該怎麼做」要跳到別頁（L114「現在該怎麼做……見 [[topics/community-large-codebase-workflow]]」）。index L32 其實可以一步到，但 index 上的字是「大型 codebase」，不是「多 agent」，我第一次沒選它。

### Q2 答案
最常見的做法是兩層：官方 auto memory（每個 session 載入前 200 行或 25KB），加上「repo 就是記憶」——決策寫成 CLAUDE.md／spec／ADR。社群工具首選 brain.md。工具和格式都還沒收斂。
- 證據：large-codebase L49、L111–117；tools L58。
- 卡住的地方：trends L267 寫「趨勢九：跨 Session 記憶層／知識庫　`方向已收斂`」，L289 卻寫「至今沒有一個經第二方採用驗證或有量化數據」。要讀到 L49 的「兩把尺」才懂「方向收斂」不等於「做法收斂」，第一次讀直接被打架的兩句搞混。

### Q3 答案（拼出來的）
官方慣例：
- 多步驟程序做成 skill；同一套流程貼第三次就做成 skill（workflow-guide L140、L186–187）。
- skill 只是建議層，要硬擋得用 hook（L210）。
- compact 之後描述清單不會重載（L223）。

社群踩坑：
- `description` 才是觸發器，寫得籠統就永遠不觸發（patterns L1938）。
- description＋when_to_use 合計 1,536 字元，清單總預算是 context 的 1%，超出會靜默失效（patterns L2063）。
- 216 個公開 skill 裡 69% 觸發寫法不可靠（patterns L995）。

- 卡住的地方：沒有任何一頁把這些整理成「慣例／反模式」。claude-skills L116 說「如何寫 skill……皆記錄於該頁」，指向一份 2486 行、按日期排的型錄。三條關鍵心得散在 L992、L1935、L2060，彼此隔了上千行。community-tech-tools L96「🧩 Skills 速查」講的是該裝哪些 skill，不是怎麼寫。

### Q4 答案（拼出來的）
官方 9 月：
- `claude plugin eval`（v2.1.269，給維護 plugin 的人在 CI 設品質門檻），feature-radar L362–376。
- `managedMcpServers`（v2.1.259，企業統一佈署 MCP），L411。
- `CLAUDE_CODE_MCP_STARTUP_WAIT_MS`，L298。

社群 9 月：
- claude-code-hooks 外掛市集（9/6，525★），trends L67。
- 其餘都在 patterns 的 2026-09 段（L567–1553），約百則，沒有挑過、也沒說哪個值得試。

- 卡住的地方：feature-radar L3 寫「僅收官方……社群工具見 [[topics/community-tech-tools]]」，但 tools 頁按症狀排，沒有「本月新品」這個切面。patterns L60 的 Plugin／MCP 列只給「⚡ 活躍｜2026-10-07」，沒有推薦。「哪幾個值得我試」整庫沒有一格在回答。

## 入口
- 帶我到答案的 index 列：L32（大型 codebase 主線）答 Q1、Q2；L115（community-pattern-trends）是我實際走的入口；L15（feature-radar）答 Q4 的官方半邊。
- 讓我走錯的列：
  - L69 claude-skills 的「設計面歸 [[topics/community-tech-patterns]]」把我送進 2486 行的型錄。
  - L28／L112 skill-interest-watch 名字有 skill，其實是 GitHub 星數榜，跟「怎麼寫」無關。這頁我沒開，但它佔掉了我的注意力。
- 缺的列：L24–32 的「我想……」表沒有「我想寫一個 skill／hook」，也沒有「這個月有什麼新東西」。

## 分不出差別的兩頁
- **community-pattern-trends vs community-tech-patterns**：中文都叫「社群××模式／趨勢」，slug 只差一個字（index L113、L115）。兩頁都要靠頁內「和 X 差在哪」那段（trends L47、patterns L46）才分得出來：一個是策展過的結論，一個是原始證據型錄。
- **community-tech-tools vs skill-interest-watch**：index L111「社群工具目錄」對 L112「社群工具規模榜」。要讀到 tools L44 的「該裝哪個只有這一頁有答案」才知道規模榜不給判斷。

## 雷達還是百科、捲了多少行
- community-large-codebase-workflow：雷達。L45–50 一張表就答完，捲大約 20 行。
- community-pattern-trends：半雷達。結論在每段的「對現有設計的啟示」，Q1 捲到 L114（約 80 行），Q2 捲到 L289（約 260 行）。
- community-tech-patterns：百科。答案分散在 L992、L1935、L2060，不用頁內搜尋找不到；照順序讀要捲 2000 行以上。
- feature-radar：官方的雷達。但 9 月在 L153–463，前面先擋著 10 月、升版表、倒數表，捲大約 300 行。

## 內部用語外洩（10 條）
1. 每頁 L1–26 的 frontmatter 讀者看得到：`generated_by: "scripts/gen_wiki_frontmatter.py"`、`pending_signalled`、`attribution_count`（如 trends L16–25）
2. index L3「哲學見 `wiki/CLAUDE.md`「資訊架構哲學」」；L6「查詢分流見 `wiki/CLAUDE.md`「搜尋策略」」，讀者不知道這是什麼檔
3. index L5「快變事實（日期／熱度／近況→頁面標頭，盤點用 Grep）」
4. patterns L191「**主線：** —」，L193「非大型 codebase 特有痛點，主線填 —」（每則都有）
5. patterns L1940「依 dev.to 內容判斷原則收錄……0 讚不作為排除理由……暫不歸入主線」
6. claude-skills L158「**懸置細節**」＋「⟨Q-01⟩」；feature-radar L83「見 [[entities/haiku-5-5]] ⟨Q-01⟩」
7. trends L324「%% 週更撈料水位：週更已收至 2026-09-19（規則：.claude/reporter-rules/community/weekly.md……）%%」，在 Markdown 原檔裡看得到
8. large-codebase L191「%% 週更撈料：patterns 節點以 `**主線：**` 欄位標記所屬線（規則：.claude/reporter-rules/community/daily.md……）%%」
9. feature-radar L17「%% ……在 30 天時間閘內達標……依規則排序優先 %%」
10. feature-radar L48「因上限 12 列移出的較舊門檻」；L23「不是本庫的報導覆蓋率」，這是編輯台的帳

## 撐不起的句子（5 條）
1. claude-skills L45「**官方目前尚未提供正式的 skill 分享／同步平台或市集機制**」：同頁 L97 寫「✅ **已有官方市集**（2026-08-08 查證官方文件更正）」，現況段自相矛盾。
2. claude-skills L116 說「實測『74 個 skill 只有 3 個真正改變行為』等一手心得皆記錄於該頁」：community-tech-patterns 頁內搜「74」，只命中無關的 HN 分數與星數，找不到這筆。
3. patterns L44「Multi-agent 架構與 Skills 設計等四類已是社群定案的做法」，L56 Skills 設計標「✅ 成熟」：表裡列的代表技巧是 drawio-skill、geo-score 這類作品，看不到「定案的是哪幾條做法」。
4. trends L267 趨勢九標「方向已收斂」，同段 L289 說沒有一條路線經過第二方驗證：標籤和證據方向相反。
5. large-codebase L60「社群近三個月沒有出現反對意見」：這是「沒有」的宣稱，頁上看不到怎麼查的。

## 最想改的三件事
1. **補上兩個缺的入口和一頁統整**：index「我想……」表加「我想寫 skill／hook，有哪些慣例和地雷」與「這個月社群有什麼新東西、哪個值得試」。Skills 設計要有一段像 trends 那樣的統整（慣例＋反模式＋證據強度），把散在 patterns L992、L1935、L2060 和 workflow-guide L186–223 的心得收在一處，不要把讀者送進型錄。
2. **改名，拆開長得像的兩對頁**：pattern-trends 對 tech-patterns、tech-tools 對 skill-interest-watch，頁名直接寫出角色，例如「社群做法：結論版」對「社群做法：原始證據」、「該裝哪個」對「GitHub 星數榜」。
3. **把編輯台的帳收起來，矛盾先修**：讀者看得到的 frontmatter、「主線：」欄、⟨Q-nn⟩、懸置細節、收錄理由不要出現在正文；claude-skills L45 和 L97 的市集矛盾、L116 指向不存在的 74 個 skill 心得，先修掉。
