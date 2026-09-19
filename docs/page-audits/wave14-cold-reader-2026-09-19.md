# 第 14 波 冷讀者實測（2026-09-19）

身分：第一次來這個 wiki 的工程師。入口只有 `wiki/index.md`，只沿 `[[連結]]` 走，只用 Read。
跳數＝開過幾頁，index 算第 1 頁。行號皆為檔案原始行號（含 frontmatter）。

---

## Q1：Claude Code 現在讀不讀 AGENTS.md？官方表態了嗎？沒有的話怎麼辦？

**路徑**：index（第 42 行 `[[entities/claude-code]]`，摘要「Claude Code CLI 主頁：功能、已知問題、社群工具」是唯一像的一列；我在 index 全檔搜過 AGENTS，零命中）→ entities/claude-code
**跳數**：2（但同一頁 Read 了 6 次：1-157 / 560-720 / 158-232 / 233-302 / 302-372 / 372-432 才撈到）
**結果**：半拿到

- 答案：`entities/claude-code.md:375`「AGENTS.md 規範不支援（#6235，396 則留言、6643 個讚，全站讚數最高）：Codex、Amp、Cursor 已採用 AGENTS.md，Claude Code 仍僅認 CLAUDE.md；官方尚未回應。」
- 同一事也在 `topics/official-community-gap.md:65`（矩陣列，狀態 ❌ 無官方對應）與 `:80`（⟨G-08⟩ 細節）。
- **沒拿到的是第三問**：兩頁都只說「官方尚未回應」，沒有任何「你現在該怎麼辦」——要不要手寫一個 CLAUDE.md 去 import AGENTS.md、有沒有人做 symlink、社群有沒有工具，全站我走過的路徑上沒有。`:80` 只補了一句「`/doctor` 精簡建議非互操作標準」，那不是給我用的。

**卡住我的原句**

- `entities/claude-code.md:105`「上限 8 列；完整清單見下方『已知問題』分組」——8 列裡沒有 AGENTS.md，我以為這頁沒有，差點放棄。它其實在 260 行外的「🔌 平台相容性（70 條未修復）」第 70 條。
- `entities/claude-code.md:704`「互動數更新 7 則（AGENTS.md #6235、多帳號 #18435…）」——歷史記錄先漏了答案的存在，但只給數字不給結論，逼我回頭在正文再找一次。

---

## Q2：個人 Max，想在額度快用完前收到提醒。官方有內建嗎？要裝哪個？

**路徑**：index（第 27 行「我卡住了（帳單爆、context 撐爆……），**社群首選**是哪個」→ `[[topics/skill-interest-watch]]`）→ skill-interest-watch →（回 index 第 109 行）→ topics/official-community-gap
**跳數**：3
**結果**：半拿到

- 官方有沒有內建：`official-community-gap.md:61`「企業版 Spend Controls（2026-07-04 宣布，控管粒度未公開）；**個人用戶仍無官方儀表板/告警 UI**」——這句直接回答了我，是全程最有用的一行。
- 裝哪個：**兩頁給了不同答案，我選不出來**。
  - `skill-interest-watch.md:21`「帳單爆了，看不到錢花在哪 → ⌨️ **tare**；要桌面常駐 → Claude Usage Widget」（證據 🟡，08-27）
  - `official-community-gap.md:61` 同一格列的社群工具是「LimitBar、CCLimitPing、claude-needs-input」——完全不同的三個名字，沒有任何一頁說它們跟 tare 什麼關係、哪個才是現在該裝的。

**卡住我的原句**

- index `:27`「帳單爆了」把我導去的那列，講的是**事後看錢花到哪**，不是**事前告警**。這是兩件事，決策表第 21 行的症狀文案沒有分。
- `official-community-gap.md:79`「⟨G-07⟩ 迫切性隨計費轉換 deadline 逼近而升高，見 [[feature-radar]] ⏰ 倒數中」——我跟過去，`feature-radar.md:59` 寫「目前沒有已知的截止日」。指路指到一個空的。

---

## Q3：哪些痛點官方明顯還沒做、值得投入？哪些已被做掉、別碰？

**路徑**：index（第 109 行 `[[topics/official-community-gap]]`，摘要「官方功能 vs 社群痛點缺口矩陣」一眼就是我的題）→ official-community-gap
**跳數**：2
**結果**：拿到，四題裡最順的一題

- 別碰（✅ 已產品化）：Subagent 派工／編排（`:54`）、破壞性指令防護（`:57`）、Slack 內 AI 隊友（`:62`）。
- 值得做（❌ 無官方對應）：成本感知模型路由（`:60`）、跨 harness 統一操作層（`:63`）、agent 間商業／支付（`:64`）、AGENTS.md 相容（`:65`）、多平行 agent 即時可觀測性（`:66`）。
- 另有結構性缺席三項：CLAUDE.md 規則失效、Token 成本不透明、AI 輔助開發副作用（`:104`–`:108`）。

**卡住我的原句**

- `:43`「截至 2026-07-08，矩陣涵蓋 **9 個核心痛點**」——下面的表有 **14 列**，最新一列是 09-13 加的。摘要比表舊兩個月，我一度以為自己看錯表。
- `:66` 多平行 agent 可觀測性那列，「官方對應」欄列了 Agent View＋兩個旗標，狀態欄卻是「❌ 無官方對應」。要讀到 `:81` 才知道意思是「有東西但不是 live map」。表上自相矛盾。
- `:39`「⟨G-11⟩ …均未新增矩陣列，詳見『時序』」——⟨G-11⟩ 是什麼、「時序」在哪一節，開頭沒說。

---

## Q4：官方 Dreaming 現在到底能不能用？跟社群記憶工具比該選哪個？

**路徑**：index → official-community-gap（`:58` 提到 Dreaming）→ feature-radar（`:79` 指路來的）→ feature-radar-archive-2026-05 → entities/managed-agents（從 index `:110` 括號裡的「↳ 子故事」）
**跳數**：5
**結果**：拿到，但繞了三頁冤枉路

- 能不能用：`entities/managed-agents.md:44`「Dreaming 與 Agent View 仍是 research preview（**Dreaming 另需申請並帶 `dreaming-2026-04-21` header**）」。這是唯一告訴我「要申請」的地方。
- 該選哪個：`official-community-gap.md:77` ⟨G-05⟩「Dreaming 僅限 Anthropic 生態、社群 OKF 跨工具跨模型；OzBrain 鎖團隊共用；ambient-context 走被動螢幕記錄、brain.md 走顯式寫入」，加上 `skill-interest-watch.md:24`「每開新 session 都要重講一遍 → ⌨️ **brain.md**」。夠我做決定了。

**卡住我的原句**

- `official-community-gap.md:58`「Dreaming 記憶整合（2026-05-07，Research Preview）」——沒說要申請 header，我以為是打開就能試，跑去 feature-radar 找「快速上手」。
- `official-community-gap.md:77`「Dreaming 兩個月後仍為 Research Preview、試用價值『⏳ 觀望』」——「試用價值」是 feature-radar 的欄位，我照這句去 `feature-radar.md` 找 Dreaming，**正頁沒有**；再去 `feature-radar-archive-2026-05.md`（全檔 435 行讀完）**也沒有 Dreaming 條目**。被引用的評級在它該在的頁上不存在。

---

## 四題走完的回答

### 1. 入口

- index 有一列讓我一眼知道去哪：**第 109 行 official-community-gap**（Q3 兩跳到底），這是全站最好的一列。
- **誤導我的是第 27 行**「我卡住了（帳單爆、context 撐爆、agent 互踩……）」：它把「我想要額度告警」吸進一個只談「錢花到哪」的決策表列（`skill-interest-watch.md:21`），而真正的答案（個人版官方沒有）在另一頁。
- index **完全沒有**互通性／多工具並用這條路（AGENTS.md、跨 harness），而那正是全站讚數最高的 issue。我是靠猜「CLI 主頁應該有」才撞到的。

### 2. 分不出差別的兩頁

`topics/skill-interest-watch`（index `:100`）與 `topics/community-tech-tools`（index `:99`）。
兩列摘要都寫「先查『我卡在這裡』決策表」，`skill-interest-watch.md:17` 又說「本表每日同步自 community-tech-tools」。讀完我說不出「A 看這、B 看那」——一個是同一張表的副本加星數榜，那為什麼是兩頁、我該先開哪一頁，沒有一句話講。
（同頁內也有一組：official-community-gap 的「Agent 工作模式產品化追蹤」表 `:52` 與「對照矩陣」表 `:98`，兩張表講同一批痛點、狀態符號不同體系（✅/🧪/❌ vs ✅/⚡/❌/⏳），沒說哪張是結論。）

### 3. 最常落腳的那一頁

`entities/claude-code.md`（862 行）。**像百科，不像雷達。**

- 雷達的部分只有 `:103`–`:120`「現在還沒修好的」8 列（有「誰會遇到」「你能做什麼」，這一節做得好）。
- 其餘是百科：`:124`–`:384` 是 260 行分組已知問題（🛡️16＋💰22＋🧠52＋📂13＋👤5＋🔌15＋🔌70 條），`:698`–`:862` 是逐日歷史記錄表，`:432`–`:583` 是逐版變更表。
- 我要的那一行在 `:375`，是第 7 個分組的第 70 條。雷達層（8 列）刻意不收它，但它是全站讚數最高的一條。

### 4. 看不懂的內部用語／維運口吻（10 條）

| # | 頁：行 | 原句 | 我看不懂什麼 |
|---|---|---|---|
| 1 | claude-code:55 | 「❓ **待查證**（標 2026-09-18｜查 claude-projects、Claude Code Projects｜複 2026-10-02）」 | 標／查／複是什麼，全站沒解釋 |
| 2 | claude-code:246 | 「（標 …｜複 2026-10-13｜**訊** 2026-09-16）」 | 又多一個「訊」 |
| 3 | claude-code:127 | 「`%% 上方「現在還沒修好的」為本組的結論層索引，非搬移 %%`」 | 編輯部自己的備忘出現在頁面裡 |
| 4 | claude-code:263 | 「`%% 2026-08-08：…狀態暫懸置。2026-09-19 查證：…08-08『changelog 未見對應』為當時漏看 %%`」 | 同上，是給維護者的認錯紀錄 |
| 5 | claude-code:711 | 「`%% 補跑：09-04 排程抓料失敗，隔日現抓補齊 %%`」 | 排程失敗是我的事嗎 |
| 6 | feature-radar:18 | 「`%% …照 wiki-ingest-features.md §7(c) 覆寫 %%`」 | 引用了一份我看不到的內規 |
| 7 | official-community-gap:39 | 「⟨G-11⟩ 跨 harness…未新增矩陣列，詳見『時序』」 | ⟨G-nn⟩／⟨Q-nn⟩ 代號沒有說明，「時序」節我沒走到 |
| 8 | index:88 | 「Topics 頁面本身無『類型』欄位，故表格僅三欄，**為刻意設計差異**」 | 對讀者解釋自己的欄位設計 |
| 9 | skill-interest-watch:11 | 「**機器產出**；決策表抄自社群工具目錄、最多落後一天」 | 「機器產出」要我打幾折信它 |
| 10 | claude-code:184、208 等 | 「**今日全站互動量最高**」「本輪互動最高功能請求」 | 「今日／本輪」是哪天，讀到時已無意義 |

### 5. 撐不起的句子

- `official-community-gap.md:43`「截至 2026-07-08，矩陣涵蓋 9 個核心痛點」 vs 同頁 `:52`–`:67` 共 14 列（最新 09-13 新增）。摘要落後表格兩個月。
- 同一個 issue #6235 的讚數：`official-community-gap.md:65` 寫 5889（標 2026-08-14），`entities/claude-code.md:375` 寫 6643（09-17）。差 754，兩頁都沒說哪個是現值。
- `official-community-gap.md:66` 狀態「❌ 無官方對應」，同一列「官方對應」欄卻列了 Agent View、`--forward-subagent-text`、`/fork`。欄位互相打架。
- `entities/claude-code.md:314` 與 `:362` 是同一個 issue #26302，一條寫「44 則留言、44 個讚，2026-08-21」、另一條寫「46 則留言、43 個讚，2026-08-15」。同頁重複收錄且數字互相矛盾。
- `entities/claude-code.md:32`「最後更新 2026-09-18」／`:33`「最後新聞更新 2026-09-19」／`:35`「最新動態（2026-09-18）」／frontmatter `:7`–`:8` 兩個都是 09-18。同一頁四處日期三個版本。
- `official-community-gap.md:77` 說 Dreaming「試用價值『⏳ 觀望』」，但 feature-radar 正頁與 2026-05 封存頁都查無 Dreaming 條目——引用了一個不存在的評級。
- `official-community-gap.md:79` 指「見 [[feature-radar]] ⏰ 倒數中」，`feature-radar.md:59`「目前沒有已知的截止日」。指路到空節。

### 6. 只能改三件

1. **給「互通性／我同時用好幾個 agent 工具」一條 index 入口。** 全站讚數最高的 issue（AGENTS.md #6235，6643 讚）現在埋在 862 行頁面的第 375 行第 7 分組，index 無任何字串可命中；順帶把「官方沒做→你現在怎麼辦」補上一句，現在三頁都只寫到「官方尚未回應」就停了。
2. **拆 `entities/claude-code.md`，或讓 `:103` 的 8 列雷達真的能路由。** 我為了一行資訊在同一頁 Read 六次。雷達表現在是「挑 8 條講」，不是「通往 190 條的索引」——至少每個分組要在雷達層有一列帶讚數排序的入口。
3. **「該裝哪個」只留一個出口。** 同一個需求，決策表給 tare（`skill-interest-watch.md:21`，08-27），缺口矩陣給 LimitBar／CCLimitPing（`official-community-gap.md:61`，07-03），兩邊互不引用、時間差兩個月。要嘛缺口矩陣的工具欄改成指向決策表，要嘛明寫「矩陣列的工具是當時的歷史快照，現行推薦只看決策表」。
