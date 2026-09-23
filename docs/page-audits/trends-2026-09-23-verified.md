# 第 17 波主編官方查證：topics/community-pattern-trends

查證日 2026-09-23。工具：WebFetch 官方文件（code.claude.com）、HN Algolia API（分數為當日即時值）、`gh api`。行號＝對象頁檔案原始行號（含 frontmatter），以 `grep -n` 取得。

## 一、結論（五行）

1. **L85「Hook 的原理：exit 1 = 硬攔截」與官方相反**：[hooks 文件](https://code.claude.com/docs/en/hooks)逐字「Exit 2 means a blocking error… exit 2 blocks whether or not you print JSON」「Without valid JSON on stdout, Claude Code treats exit code 1 as a non-blocking error and proceeds with the action, even though 1 is the conventional Unix failure code」。趨勢一整段「對現有設計的啟示」的可執行結論建立在錯的 exit code 上；同節 L68「Pre-completion Hook…回傳非零 exit，逼模型繼續」也不精確（Stop hook 只有 exit 2「Prevents Claude from stopping」）。
2. **頁面自己的熱度錨點（L47）沒有被自己遵守**：HN 即時分數 Adrafinil 124（頁 L60 🔥🔥、頁記 113，依 L47 ≥100 應 🔥🔥🔥🔥）、machine0 Launch HN 83（L98 🔥、頁記 78，應 🔥🔥🔥）、Merge Queue 42（L97 🔥、頁記 39，應 🔥🔥🔥）、Workweave 216（L165 🔥🔥🔥🔥、頁記 181，一致）。四筆有 HN 分數的節點三筆與定義不符；分數本身漂移 5–20%，頁面未標判定日。
3. **趨勢四「官方有沒有內建路由」的答案官方文件有寫、本頁沒指**：[model-config](https://code.claude.com/docs/en/model-config)「The `opusplan` model alias… In plan mode: uses `opus`… In execution mode: automatically switches to `sonnet`」；`CLAUDE_CODE_SUBAGENT_MODEL` 給 subagent／teammate／workflow agent 預設模型；除此之外「no automatic difficulty-based model routing」。庫內家：`official-community-gap` L59 已寫 🧪 opusplan＋org default model；本頁 L179 啟示段零字提官方。
4. **L170「GitHub Issue #56913，47 👍」過期且方向變了**：`gh api` 2026-09-23：**closed / not_planned（2026-09-15）**、49 則留言、👍 0（reactions total 0）。「分層 Opus 大腦＋Sonnet 工人」被官方標不做，本頁仍列為加溫節點。
5. **趨勢一末節點「claude-code-hooks 500★」現 525★／push 09-18**，成立；`opusplan`、auto memory（第 16 波 verified）、Remote Control 已出貨（第 14 波 verified #29006 COMPLETED 08-17）三項官方對應分別落在趨勢四／九／八，本頁三條線的啟示段都沒有一句官方對應。

## 二、頁面數字 vs 一手

| 行號 | 頁面寫什麼 | 一手（2026-09-23） | 判定 |
|---|---|---|---|
| L85 | 「exit 1 = 硬攔截…工具呼叫根本不會發生」 | 官方：exit 2 才擋；exit 1 非阻擋、動作照跑 | **錯**，改 exit 2（或 JSON `permissionDecision: "deny"`） |
| L68 | Pre-completion Hook「回傳非零 exit，逼模型繼續」 | Stop hook exit 2「Prevents Claude from stopping, continues the conversation」；其他非零不擋 | 不精確 |
| L60 | Adrafinil（6/28，HN 113）🔥🔥 | HN 124（2026-06-27 發文，78 則） | 分數漂移；依 L47 應 🔥🔥🔥🔥 |
| L97 | Merge Queue（7/30，HN 39）🔥 | HN 42／22 則 | 依 L47 應 🔥🔥🔥 |
| L98 | machine0（8/18，Launch HN 78）🔥 | HN 83／44 則；另有 06-15 Show HN 96 分 | 依 L47 應 🔥🔥🔥；6/15 那則本頁未收 |
| L165 | Workweave Router（6/27，HN 181）🔥🔥🔥🔥 | HN 216／113 則（2026-06-26 發文） | 等級一致；日期差一天 |
| L170 | Issue #56913「47 👍」 | closed not_planned 09-15；49 則；👍 0 | **過期＋方向反** |
| L63 | claude-code-hooks 500★ | karanb192/claude-code-hooks 525★／38 forks／push 09-18 | 成立 |
| L179–190 | 「全走 Opus ≈ $100；Haiku 50%／Sonnet 40%／Opus 10% ≈ $18」 | 庫內 `entities/pricing` L119／L122：Sonnet 5 $2/$10、Opus 5 $5/$25 | 「$100／$18」無 token 假設、無日期，是示意不是數字；Opus／Sonnet 牌價比 2.5×，18% 的比例撐不起「省 82%」 |
| L179 | 「簡單任務降階可省 60%+」 | 出處為 L175「分層模型策略…節省約 60% 用量」單一社群案例 | 社群單一，維持 |

## 三、考題的官方錨句

- **Q1 hook 怎麼擋**：「For most hook events, exit code 2 is the only exit code that blocks through the code alone」；PreToolUse「Blocks the tool call」；JSON 路線「`permissionDecision: "deny"`」。
- **Q2 官方有沒有內建路由**：`opusplan`（規劃 Opus、執行 Sonnet）、`CLAUDE_CODE_SUBAGENT_MODEL`；「no automatic difficulty-based model routing」。庫內家 `official-community-gap` L59／L183–187。
- **Q3 跨 session 記憶官方側**：auto memory 四類筆記、每 session 載前 200 行／25KB（第 16 波 verified 第五條）。
- **Q4 本地小模型分流替代**：官方無；社群側 `CLAUDE_CODE_SUBAGENT_MODEL=haiku` 是最接近的官方零件（把探索類 subagent 指到便宜模型），非本地模型。

## 四、需設計者處理但主編查不到的

- 演進條列中無 HN 分數的節點（多數）🔥 數為「熱度估計」（L47 自承），無法對一手；只能要求頁面標明哪幾筆是估計。
- Dragoman／三角色 Pipeline／分層模型策略 60%：Reddit 或個人文章，未查。
- model-config 文件今天寫預設模型「Opus 5.5」（Pro／Max／Team／Enterprise／API）——若屬實是新模型，屬模型記者範圍，本波不處理，建議轉知模型記者核一手。

## 五、給設計者三句

1. 趨勢一的啟示段是全頁最可執行的一段，但 exit code 寫反了；改成官方語意（exit 2 擋、exit 1 不擋、或 JSON deny）並連官方文件。
2. 🔥 標記要嘛照 L47 定義重打並標判定日，要嘛把 L47 改成「收錄當時的估計」——現在是定義與標記各說各話。
3. 三條線（四／八／九）的官方對應一句都沒有：opusplan、Remote Control 已出貨、auto memory；「對現有設計的啟示」若不先說官方給了什麼，讀者會把官方已內建的東西再去社群找一遍。
