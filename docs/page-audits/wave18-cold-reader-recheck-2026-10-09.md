# 第 18 波冷讀者複驗（2026-10-09）

讀者設定：第一次來、用 Claude Code 寫程式的工程師。只從 `wiki/index.md` 出發，沿 `[[連結]]` 走，index 算第 1 跳。
行號＝Read 顯示的原始 md 行號（含 frontmatter；正文標題都在第 26 行左右開始）。「捲動行數」從正文標題算到答案段落結束。

## 四題結果

| 題 | 路徑 | 跳數 | 結果 | 捲動 |
|---|---|---|---|---|
| Q1 多 agent 分工 | index → community-multi-agent | 2 | 拿到 | 約 31 行（L26→L57） |
| Q2 跨 session 記憶 | index → community-memory | 2 | 拿到 | 約 30 行（L26→L56） |
| Q3 寫 skill 慣例／反模式 | index → community-skills | 2 | 拿到 | 約 32 行（L26→L58） |
| Q4 2026-09 自動化新東西 | index → community-tech-patterns → community-integrations → community-tech-tools → community-guardrails | 5 | 半拿到 | 約 400 行（四頁合計） |

**Q1 答案：** 每個 agent 一個 git worktree 的隔離已定案（官方 subagent 有 `isolation: worktree`）；隔離之後誰先合併、誰驗收官方還沒答案，社群用本地合併佇列或人工把關補（multi-agent L53–54）。
- 卡點：L54「用本地合併佇列（[[topics/community-multi-agent#2026-07]]）」連到月份段，要自己往下翻到 L466 才找到那一則，而且那一則只有 HN 39 分一個來源。
- 「哪種站得住」只有隔離一項有判語，其餘控制平面（L60–61、L140 之後約 25 則）都沒有評比。

**Q2 答案：** 最常見的是兩層：官方 auto memory 加上把決策寫回 repo（CLAUDE.md／spec／ADR）。方向收斂了，工具還沒收斂（memory L45–47、L53–56）。
- 卡點：index 的「開發實務入口」表（L24–34）沒有記憶這一列。我是從 L115 的「↳ 子故事」清單看 slug 猜到 `community-memory`。L27「context 撐爆」那列會把人帶去工具頁，問的不是同一件事。
- L47「方向收斂了（…趨勢九）」只給了編號，沒寫趨勢九是什麼，要再跳一頁才知道。

**Q3 答案：** 慣例是「description 就是觸發器、一個 skill 只做一件事」。地雷有三條：description 有字元預算，超額會被靜默擠掉；公開 skill 有 69% 觸發寫法不可靠；品質目前只有個案量測（skills L47–58）。
- 入口很準：index L34 直接寫了錨點「慣例與地雷」。
- 卡點：L58「前兩條地雷各只有一位作者…」，但地雷有三條，第三條算什麼沒有交代。

**Q4 答案（半）：** 2026-09 有 claude-code-hooks 外掛市集（guardrails L197）、未公開 function hooks 做的精簡輸出外掛（L134）、Snyk agent-scan 掃 MCP／skill（L143），MCP 則多是廣告、創作類 server（integrations L198–348）。但 wiki 明說沒人篩過哪個值得裝。
- 卡在原句：integrations L45「還沒有人篩過哪個值得裝——該裝哪個看 [[topics/community-tech-tools]]」。可是工具頁按症狀排，不按月份；L36 的 10-03 更新只講 09-25～10-02，沒有九月自動化的推薦。
- 「哪幾個值得試」等於沒答案：每則都標「⏳ 新興、僅星數」，我只能自己從星數拼。

## 入口

- 帶到答案的列：L33（多 agent）、L34（skill，含錨點，最好用）、L115 的「↳ 子故事」清單（Q2 靠它）。
- 走錯的列：
  - L27「我卡住了（…context 撐爆…）」：Q2 差點進工具頁。
  - L113 tech-tools 和 L114 skill-interest-watch：Q4 時兩列都像「新東西在哪」，其實都不按時間排。
  - L115 community-tech-patterns：Q4 先去那頁多花了一跳，那頁只是總表。
- 缺的列：「記憶／context 怎麼做」和「最近一個月社群出了什麼值得試的」，「開發實務入口」都沒有。

## 分不出差別的頁

1. **community-tech-patterns vs community-pattern-trends**：都在講「收斂到哪」。patterns L46 寫「已定案四類」，L48 又說 trends 才是「策展過的結論」。看不出哪一頁的結論算數。
2. **community-tech-tools vs skill-interest-watch**：index L22 有解釋，但兩頁都列工具、都有星數，Q4 這種「新東西」問題不知道該去哪頁。
3. **community-large-codebase-workflow vs community-multi-agent／community-memory**：multi-agent L47、memory L45 都把一部分答案外推到 large-codebase 的「第 1 線」「第 3 線」，三頁的界線看不清。

## 雷達還是百科

前 30 行像百科：有摘要、目前結論、你的選項，寫得好。之後全是雷達流水帳：
- multi-agent 的「技術彙整」L136–519，占全頁 74%。
- integrations L57–412 也是。
每則都是「某 repo、N 星、首次收錄、新興」。整體讀起來是頂著百科頭的雷達。

## 內部用語外洩（10 條）

1. multi-agent L23 `signal: "孤島"`、L24 `generated_by: "scripts/gen_wiki_frontmatter.py"`：frontmatter 外露（只有原始 md 看得到，網站版要另驗）。
2. memory L69「**主線：** 索引記憶」、L71「主線填索引記憶」：「主線」是什麼帳、怎麼填，讀者不知道。
3. skills L77「非大型 codebase 特有痛點，主線填 —」：同上，每則都有。
4. skills L106「不進模式概覽表」：這是編輯台的動作，不是給讀者的資訊。
5. skills L208「本庫存量盤點今日首次收錄」、guardrails L148「存量盤點條目」：「存量盤點」是流程名詞。
6. tech-patterns L140「%% 拆頁評估…（第 18 波）…兩張轉知單結案後刪 h3…過渡錨點 %%」：Obsidian／原始 md 看得到。
7. memory L73 等「來源：GitHub Search」：像是抓取管道的名字，看不出是搜尋結果還是某個榜。
8. integrations L59「⟨Q-nn⟩ 標的是這一則還沒查實的地方」、multi-agent L127「⟨Q-07⟩」：編號系統要先學才看得懂。
9. memory L47「趨勢九」、guardrails L45「趨勢一」：只有編號，沒有名字。
10. multi-agent L113「措辭於 2026-09-20 依 official-community-gap 對齊」：編輯對帳紀錄。

## 撐不起的句子（5 條）

1. skills L64「單一職責的寫法已獲社群反覆驗證（[[topics/community-skills#2026-09]]）」：同頁 L51 的依據只是「沒有人再反對」，L58 又說慣例只有單一作者；連結指向整個月份段的約 20 則工具，不是驗證。
2. tech-patterns L103「已經定案的四類…近三個月沒出現反對意見」：「沒有反對」這種不存在證明，頁上看不到查了什麼。
3. multi-agent L53「隔離已定案」：頁內只有 L510「新佐證教學」和總表的 ✅，看不到幾個獨立來源。
4. multi-agent L54「你的選項：用本地合併佇列」：背後只有 L466–471 一則 HN 39 分的貼文。
5. skills L58「前兩條地雷各只有一位作者」：地雷有三條，哪兩條、第三條的證據強度都沒說。

## 最想改的三件事

1. **index「開發實務入口」補兩列**：「跨 session 記憶／CLAUDE.md／context → community-memory『目前結論』」，以及「這個月社群出了什麼值得試 → （某頁某段）」。Q2、Q4 現在都靠猜 slug 或多跳。
2. **「技術彙整」每則拿掉編輯台欄位**（主線、與既有模式的關係、存量盤點、⟨Q-nn⟩ 說明），只留「做什麼／證據強度／連結」。正文裡的 `#2026-07` 這類月份錨點改成指到單則。
3. **讓「定案」「反覆驗證」可以被檢查**：每個定案句後面列出幾則獨立來源、各在哪一行。先修 skills L64 和 L58 的自相矛盾。整合頁另外給一張「本月值得試」短表（就算只寫「沒有，理由是…」也好），不要把問題推給不按月份排的工具頁。
