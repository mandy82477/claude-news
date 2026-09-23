# 第 17 波冷讀者複驗（2026-09-23）

實際開過的頁（依序，共 8 跳）：wiki/index.md → topics/community-tech-patterns → topics/community-pattern-trends → topics/community-large-codebase-workflow → topics/community-tech-tools → topics/community-tech-discussions → topics/coding-workflow-guide → topics/official-community-gap

讀者設定：帶 6 個專案的 Claude Code 重度使用者，模型分級寫死在 CLAUDE.md，規則越寫越多卻常被無視。只沿頁內連結走，行號是頁面原始檔的行號。

---

## Q1. CLAUDE.md 40 條規則常被無視：社群怎麼解、哪些搬 hook、exit code 幾才擋得住

- **路徑**：index（「Topics」表 community-tech-patterns 列摘要寫「已定案四類（…CLAUDE.md、Hooks）」）→ community-tech-patterns（概覽表只給一句話，沒有 exit code）→ community-pattern-trends 趨勢一（答案在這）→（補充）coding-workflow-guide「東西該放哪一層」
- **跳數**：3 跳拿到（第 4 跳只是補 deny 的細節）。事後看，index → trends 2 跳就夠，但 index 上 trends 那列的摘要（「九個方向」）完全沒提到 hook，所以我先走錯到 patterns。
- **結果**：**拿到**
- **拿到的答案原句**：
  - 判準：community-pattern-trends.md:74「你 CLAUDE.md 裡任何『必須 100% 遵守』的規則都放錯位置了……偏好留 CLAUDE.md，邊界搬 Hooks。」＋ :76「這條規則被遺漏一次，我會生氣嗎？」＋ :78–85 六列範例表（force push、commit 前跑測試、讀 .env → PreToolUse；prettier → PostToolUse）
  - exit code：community-pattern-trends.md:87「PreToolUse hook 以 exit 2 結束，這次工具呼叫就不會發生；exit 1 只算非阻擋錯誤、動作照跑」，另可回 JSON `permissionDecision: "deny"`，附官方文件連結
  - 強度：coding-workflow-guide.md:210「PreToolUse hook 最硬……回 deny 時連 bypassPermissions 和 --dangerously-skip-permissions 都擋得住」
  - 第一手佐證：community-tech-patterns.md:907–913（dev.to 08-25，遵循率從「機率性」變 100%）
- **卡住或誤導我的原句**：
  - community-tech-patterns.md:57 概覽表「Hooks 與自動化……強制執行勝過建議；CLAUDE.md 做偏好、Hooks 做邊界」：方向對，但這頁從頭到尾（1,710 行）都沒有 exit code，也沒有「哪些該搬」的判準表。index 把我帶到這頁，這頁卻沒指去趨勢一。
  - community-tech-tools.md:70「答案是機制不是工具，做法見 [[topics/community-tech-patterns]]」：決策表「CLAUDE.md 寫了它不聽」那列把讀者送到**沒有做法表的那頁**，真正的做法表與 exit 2 在 community-pattern-trends。
  - community-pattern-trends.md:37 頂部 callout「本頁趨勢一先前寫成『exit 1 硬攔截』，已更正」：更正本身有用，但也告訴我舊版曾經寫錯。其他頁要是轉貼過舊說法，我沒辦法知道。

## Q2. 依難度自動降階到便宜模型：社群走到哪、有沒有現成工具、風險、官方有沒有內建

- **路徑**：community-pattern-trends 趨勢四 →（連結）community-tech-tools 決策表＋目錄 →（連結）official-community-gap ⟨G-13⟩
- **跳數**：照實際開啟順序是 5 跳（index → patterns → trends → tools → gap）；最短路徑是 index → trends → tools → gap，共 4 跳。
- **結果**：**拿到**
- **拿到的答案原句**：
  - 社群走到哪：community-pattern-trends.md:147「趨勢四：模型路由自動化 `方向已收斂` ↘ 淡出・最近一次動靜 2026-08-14」；:157 Opus 大腦＋Sonnet 工人提案（#56913）「官方已於 2026-09-15 關閉，標為不做」
  - 現成工具：community-pattern-trends.md:160「Workweave Router：……依難度自動降階」→ community-tech-tools.md:63（首選、🔌 proxy、🟡 單一實測、判 06-27／查 09-22）、:222「實測成本降 40%+」
  - 風險：community-pattern-trends.md:177「黑盒路由的隱患……某些關鍵任務可能被靜默降階」＋「你指定的模型本身不一定釘得住」；community-tech-tools.md:65「🔌 proxy·MCP（流量過第三方層，裝前先評估安全）」
  - 官方內建：community-pattern-trends.md:166「opusplan……CLAUDE_CODE_SUBAGENT_MODEL……依難度自動選模型的路由，官方文件沒有」；official-community-gap.md:59「依成本或任務動態選模型的路由截至 2026-09-19 官方文件未見」
  - 能照抄的降階表：community-pattern-trends.md:170–175（migration SQL 審查「Opus，不可降階」）
- **卡住或誤導我的原句**：
  - community-tech-tools.md:63：Workweave 放在「不想被單一供應商綁死」那一列，不是「想依難度省錢」。我照症狀找決策表會找不到它，得靠 trends:160 的連結才知道要看這列。
  - official-community-gap.md:59／:130「個人端官方只有 `opusplan` 這一種固定切換」：同一 wiki 的 trends:166 與 community-tech-patterns.md:145 都說 subagent 的 model 欄／`CLAUDE_CODE_SUBAGENT_MODEL` 也能分模型，兩邊講法對不起來（見第 6 節）。
  - community-tech-patterns.md:60 概覽表「模型使用策略 ⚡ 活躍，最後動態 2026-09-06」對上 trends:147「淡出・2026-08-14」：只讀這兩頁，會以為兩頁互相矛盾。

## Q3. 跨 session 記憶近三個月變了什麼、現在該看哪一頁；「社群趨勢觀察」和「社群技術模式」差在哪

- **路徑**：community-pattern-trends 趨勢九 →（:287 連結）community-large-codebase-workflow 第 3 線 →（:115 連結）community-tech-tools 決策表「每開新 session 都要重講一遍」列；另外 official-community-gap ⟨G-05⟩ 補官方 hook
- **跳數**：答案在第 4 跳（large-codebase）；拿到首選工具是第 5 跳。
- **結果**：**拿到**（變化時間線、官方零件、該讀哪頁、首選工具都有）；兩頁差別**半拿到**（見第 3 節）
- **拿到的答案原句**：
  - 三個月的變化：community-pattern-trends.md:270–277（7/22 CodeAlmanac → 8/21 OzBrain 團隊共享 → 8/24 手動 Obsidian 取代官方 → 8/25 brain.md → 8/31 否決紀錄防竄改 → 9/6 gentle-ai／cpr → 9/17 Skillsync 跨 agent 搬遷 → 9/18 hister）；:287「先看官方給了什麼：auto memory……前 200 行或 25KB……選型前先問『這個格式會不會只有我一個人在用』」
  - 現在該看哪頁：community-pattern-trends.md:287「官方與社群做法現在怎麼接，見 [[topics/community-large-codebase-workflow]]」→ community-large-codebase-workflow.md:111–113（官方 auto memory＋決策外化成 CLAUDE.md／spec／ADR）、:115（首選 brain.md）
  - 官方 hook 接外部記憶：official-community-gap.md:107「PreCompact／PostCompact／SessionStart／SessionEnd 四個 hook……SessionStart 可回傳 additionalContext」
  - 兩頁差別：community-pattern-trends.md:47「那頁是每一種做法的原始證據型錄……本頁只挑已經收斂成方向的，按時間排、講回頭檢查什麼」
- **卡住或誤導我的原句**：
  - 四頁都在講記憶（trends 趨勢九、large-codebase 第 3 線、tools 第 58 列、gap ⟨G-05⟩），每頁各給一塊，沒有一頁說「記憶這題以這頁為準」。trends:287 算是最接近的指路。
  - auto memory 是哪天上線、算不算「近三個月」的變化，四頁都沒寫日期（official-community-gap.md:110 只寫「auto memory 上線後數量沒有下降」）。
  - community-large-codebase-workflow.md:115 說「團隊共享與 Obsidian 路線的分界在同列第三欄」，但 tools:58 第三欄的 Obsidian 選項「VIR」沒有連結，目錄段我也沒找到可以裝的頁。

## Q4. Fast Context Task Router 已下架，本地小模型分流還能拿什麼做

- **路徑**：community-pattern-trends.md:153–154 →（連結）community-tech-discussions →（連結）community-tech-tools 目錄 Dragoman／claudely →（trends:166 連結）coding-workflow-guide:287 官方立場
- **跳數**：頁面在第 3 跳給出替代；確認替代能不能用到第 5 跳；看官方立場是第 6 跳。
- **結果**：**拿到**（頁面誠實寫「下架、原因未公開」，並給了三個替代，其中兩個可執行）。有一個替代偏題，見下方。
- **拿到的答案原句**：
  - community-pattern-trends.md:153「原專案已下架，不要照著找」；:154「替代：官方最接近的是 `CLAUDE_CODE_SUBAGENT_MODEL`……本地模型的混合做法見 [[topics/community-tech-discussions]]，可路由到 Ollama 的 Dragoman 見 [[topics/community-tech-tools]]」
  - 可執行 1：community-tech-discussions.md:226 用 MCP 架構把部分工作分給本地 Qwen3.8-27B（Reddit 與 XDA 原文連結都有）
  - 可執行 2：community-tech-tools.md:248 Dragoman（有 repo 連結，依問題類型路由到 Perplexity/Gemini/Ollama）
  - 為什麼不再推薦：coding-workflow-guide.md:287「本地小模型分流省 50–60% context（生態只驗證成本不驗證 context）」；community-pattern-trends.md:166 同義
- **卡住或誤導我的原句**：
  - community-pattern-trends.md:154「官方最接近的是 `CLAUDE_CODE_SUBAGENT_MODEL`」：這個設定是把 subagent 指到便宜的 **Claude** 模型，不是本地模型。我問的是「本地」分流，這條替代答到另一題。
  - community-tech-tools.md:256 claudely「2026-09-22 查不到公開 repo 或產品頁」：tools:63 決策表把它列成「只想改用本地模型」的次選，實際上裝不到。
  - Dragoman（tools:248）歸在「多 Agent」類、最後一筆是 2026-05-13，表上沒有「查」日期，我看不出它現在還活著沒有。

---

## 分不出差別的兩頁

**topics/community-tech-patterns（社群技術模式）vs topics/community-pattern-trends（社群趨勢觀察）**

- **為什麼分不出**：在 index 上，patterns 的摘要寫「已定案四類（Multi-agent、Skills、CLAUDE.md、Hooks）」（index.md:101），trends 寫「社群做法收斂成的九個方向」（index.md:103）。「定案四類」和「收斂九個方向」看起來是同一把尺量出兩個數字，我在 index 上判斷不了哪頁回答「現在該怎麼做」，所以先走錯到 patterns。
- **讀到哪一句才懂**：community-pattern-trends.md:47「那頁是每一種做法的原始證據型錄……本頁只挑已經收斂成方向的，按時間排、講回頭檢查什麼」，加上 :49「兩把尺……『方向已收斂』量的是做法有沒有收斂成一個方向，不是用的人多不多」。讀到這兩句才懂：patterns 是證據庫（查某個工具或某則貼文），trends 是解讀（拿來回頭檢查自己的設計）。
- **懂了之後還是會被絆到**：兩頁對同一件事的日期與狀態不一致，差異的理由寫在 trends:322 的 `%%` 維運註解裡，網站讀者看不到。
  - patterns:60 模型使用策略「⚡ 活躍，2026-09-06」對上 trends:147「淡出，2026-08-14」
  - patterns:59 記憶「2026-09-20」（aoci-code）對上 trends:265「最近一次動靜 2026-09-18」

**我怎麼決定讀哪頁**：要「我該改什麼」讀 trends（每條都有「對現有設計的啟示」），要「這個工具／這則貼文的來源與可信度」讀 patterns，要「現在就做」讀 large-codebase-workflow，要「裝哪個」讀 tools。這個分工只有讀完 trends:47–48 才拼得出來，patterns:44 的指路句沒講這麼清楚。

---

## 雷達還是百科（各頁一句）

| 頁 | 判定 | 一句 |
|---|---|---|
| index | 地圖 | 一格一頁的路由表，但 trends 那列的鉤子沒提 hook、路由、記憶這些讀者會搜的詞。 |
| community-tech-patterns | 百科（證據流水帳） | 1,710 行、每則貼文一節，頂部 callout 是雷達，底下全是型錄，拿來查出處，不是拿來找答案。 |
| community-pattern-trends | 百科（解讀型） | 九條趨勢各有演進、代表模式和「對現有設計的啟示」，是這趟唯一直接回答「我該怎麼改」的頁。 |
| community-large-codebase-workflow | 百科（手冊） | 四面牆各給「現在的答案＋官方零件＋🧰 工具」，照做即可。 |
| community-tech-tools | 雷達 | 症狀決策表每列都有判定日與查證日，最像「今天該裝什麼」的雷達。 |
| community-tech-discussions | 雷達 | 爭論表標熱度與狀態（延燒／靜候／重燃），追的是吵到哪，不是結論。 |
| coding-workflow-guide | 百科（官方手冊） | 分層表與「本頁不再推薦」清單是官方立場的定錨點。 |
| official-community-gap | 百科＋尾巴雷達 | 上半是狀態矩陣，下半「時序」是逐日紀錄，舊紀錄的狀態符號和上半矛盾。 |

---

## 內部用語外洩表

| # | 用語 | 出處 | 讀者看到的困惑 |
|---|---|---|---|
| 1 | 「主線：—」 | community-tech-patterns.md:177、:186 等 | 「主線」是什麼？破折號代表沒有，還是沒填？ |
| 2 | ⟨Q-07⟩、⟨G-13⟩、⟨G-05⟩ | community-tech-patterns.md:151；official-community-gap.md:59 | 看起來像引用編號，實際是頁內跳點，要往下捲才知道。 |
| 3 | 「懸置細節」 | community-tech-patterns.md:153 | 聽起來像待辦清單，其實裝的是已查證的結論。 |
| 4 | 「存量盤點條目……本庫今日首次收錄」 | community-tech-patterns.md:243 | 這是維護流程的狀態，讀者不需要知道。 |
| 5 | 「依 dev.to 內容判斷原則收錄」「score 不可信」 | community-tech-patterns.md:1196、:1010 | 收錄準則外洩，讀者要的是可信度結論，不是準則名稱。 |
| 6 | 「HN Repo Bridge」「Blogroll 策展來源」「GitHub Search 星數」 | community-tech-patterns.md:250、:196、:180 | 資料管道的名字，讀者不知道它們和 HN、GitHub 差在哪。 |
| 7 | 「與既有模式的關係：……暫不併入既有代表技巧列」 | community-tech-patterns.md:197 | 編輯決策寫進了正文。 |
| 8 | 「矩陣狀態維持 🧪 部分產品化」「⏳ 正在做但不夠」 | official-community-gap.md:234、:245 | 符號系統換過，舊的狀態詞還留在頁上。 |
| 9 | 🌊延燒／🌙靜候／🌋重燃／☄️閃現 | community-tech-discussions.md:177、:195、:201、:226 | 頁內沒有圖例（我查的段落沒看到），得自己猜。 |
| 10 | 「判」「查」 | community-tech-tools.md:54–65 | 有圖例（:65）可以懂，但第一眼看不懂。 |

---

## 撐不起的句子（附兩邊行號）

1. **Workweave 的 HN 分數**：community-pattern-trends.md:151「Workweave Router（6/27，HN 216）」對上 official-community-gap.md:131「Workweave Router（HN 181……）」與 community-tech-tools.md:222「Show HN score 181」。同一個專案出現兩個分數，trends 的 🔥🔥🔥🔥 分級就是拿這個分數算的。
2. **官方個人端有幾種分模型方法**：official-community-gap.md:59／:130「個人端官方只有 `opusplan` 這一種固定切換」對上 community-pattern-trends.md:166「`CLAUDE_CODE_SUBAGENT_MODEL` 可替 subagent 指定預設模型」與 community-tech-patterns.md:145「subagent 定義有 model 欄……也有全域環境變數」。
3. **模型路由是活躍還是淡出**：community-tech-patterns.md:60「模型使用策略 ⚡ 活躍，最後動態 2026-09-06」對上 community-pattern-trends.md:147「↘ 淡出・最近一次動靜 2026-08-14」與 :50「近 30 天本頁與 patterns 都沒有新做法進來，標『↘ 淡出』」。patterns 明明有 09-06 的條目，:50 的定義本身就站不住；理由只寫在 :322 的隱藏註解裡。
4. **記憶路線有沒有量化數據**：community-pattern-trends.md:287「至今沒有一個經第二方採用驗證或有量化數據」對上 community-large-codebase-workflow.md:122「向量 DB（39ms 檢索）……圖譜路線採用量最大（graphify）」與 community-tech-tools.md:57 graphify「🟢 多來源實測」。
5. **Fast Context 何時下架**：community-pattern-trends.md:154「原專案 07-05 起下架」對上 community-tech-discussions.md:585「使用者重新測試 Microsoft 已下架的 Fast Context 專案」（該節標題日期同為 07-05，:582）。07-05 是社群貼文的日期，不是下架日；兩頁連專案名稱也不一致（「Fast Context Task Router」與「Microsoft Fast Context」）。

---

## 最想改三件（讀者立場）

1. **把「CLAUDE.md 不聽」的路由指到真正有答案的地方。** community-tech-tools.md:70 和 index 的 patterns 列都把人送到 community-tech-patterns，但判準表和 exit 2 在 community-pattern-trends 趨勢一（:74–87）。建議 tools:70 改成指 `[[topics/community-pattern-trends#趨勢一：強制層取代建議層]]`，index 的 trends 列鉤子也寫出「hook 怎麼擋」這類讀者會搜的詞。
2. **兩頁對同一類的狀態和日期要一致，或者在頁面上講明為什麼不一致。** patterns 概覽表的「最後動態」和 trends 的「最近一次動靜／淡出」各用各的尺，理由藏在 `%%` 註解裡。至少在 trends:50 加一句「patterns 有新條目，但沒有推進這個方向，所以不算」，讓網站讀者也看得到。
3. **替代方案要答到原題。** trends:154 把 `CLAUDE_CODE_SUBAGENT_MODEL` 列為本地分流的「官方最接近」，但它不是本地模型；claudely 在決策表當次選，卻查不到 repo。建議改成：本地分流目前沒有活著的同功能工具 → 可執行的是 discussions:226 的 MCP＋本地 Qwen 做法或 Dragoman（附最近查證日）；想省錢但不一定要本地，才用 `CLAUDE_CODE_SUBAGENT_MODEL`。
