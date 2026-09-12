# 設計提案：`wiki/topics/anthropic-agent-stack.md`（第 13 波，樞紐 入邊 6／出邊 14）

2026-09-12｜設計者（只派一次）｜⚠️ 疑似注入：無（讀到的 wiki 內容一律當資料）
使命句（使用者已批，不改）：**每個官方 agent 積木是為了解決什麼痛而出，讓我多做出哪些工作流。**

## 0. 推薦案一句

> **換軸，不重寫關係軸。** 頁面現有兩個軸（選型表、六層架構）講的都是「積木之間的關係」，使命句問的是「每塊積木自己的來歷與產出」——這個軸頁面上不存在，所以八積木盤點 16 格中 11 格「無」。做法：**新增「八個積木」主軸節，一積木一卡、每卡固定三欄**（沒有它之前的痛／官方多給了什麼＋可貼上的指令／它現在還做不到什麼），新增「這八塊怎麼疊」四條，「你該用哪個」節名留、內容換成官方三問決策樹，**選型表與六層架構降為頁尾兩份附錄（不砍）**。116 → 234 行正文（含 frontmatter 258 行）。

三件連帶：① 四處硬錯同批修（`/goal` 專頁、MCP 隧道、issue #24798、Agent SDK 計費改 wikilink）；② 計費事實搬回子頁，母頁只留一句指路（Q4 卡點）；③ 同維護者鄰居各改一格（`feature-radar` L227 狀態欄、index L30 路由措辭）。

## 1. 不選的方向（各一行）

- **拆頁**（八卡各自開頁或另開「工作流食譜」頁）不選：三訊號只亮一個——有人問（✅ 使用者 Q2），但答案不會各自有時序、也還沒有同一件事住在兩三頁。
- **砍六層架構**不選：使用者已裁決降附錄不砍；且它是全頁唯一「互動模式」（單向扇出／點對點／依賴順序流動）的家，八卡答不了那一題。
- **改節名「你該用哪個」**不選：現行三處路由以引號指名（index L30、`coding-workflow-guide` L77／L462），改名會讓三處措辭失準，而決策樹本來就是「你該用哪個」的正面答案。
- **併頁**（與 `community-large-codebase-workflow`，log:6229 的擱置候選）不選：本波不處置併頁，八卡上線後重疊變大或變小屬回訪項。
- **兩案並陳**不做：使命句已批，附錄位置與計費歸家皆為已裁決點，本稿只出一案。
- **在頁上補「通用工程常識」填空格**不做：每一格「為什麼出」只用 V 第一節逐字句或其忠實改寫，官方沒說的寫「官方未說明」而不補。

## 2. 可行性前提（一行）

**不需要任何新進料，唯一待核一處：** 卡三那支最小 script 的**參數形狀**（`export const meta` 欄名、四原語是注入參數還是 import）——形狀依使用者指定的官方 `audit-routes` 範例寫成，實作前請主編對照 https://code.claude.com/docs/en/workflows 逐字校一次；除此之外每一句都有 V 的錨句或本庫既有文字。

## 3. 八卡三欄填充盤點（24 格）

| 積木 | 沒有它之前（官方為什麼出） | 官方多給了什麼（含最小指令） | 還做不到什麼 |
|---|---|---|---|
| `/goal` | ✅ V:L11 逐字 | ✅ 官方四例＋2 條指令 | ✅ 單 session；背景工作在跑時跳過該回合檢查 |
| 內建 subagent | ✅ V:L12 逐字 | ✅ 三情況＋`--agent`／`--name`＋官方續用兩句 | ✅ Explore/Plan 限制、開不了 workflow |
| Dynamic workflows | ✅ V:L13 逐字（計畫握在誰手上） | ✅ 官方六條 prompt＋8–12 行最小 script＋存放與呼叫法 | ✅ 並行上限／4,096 項／不能等輸入／開不了 teams |
| Agent teams | ✅ V:L14 分界句＋勸退句 | ✅ 四類場景＋兩條 prompt＋開關環境變數 | ✅ 實驗性、`/resume`、不可巢狀、`-p` |
| Cross-session messaging | ✅ V:L15 逐字 | ✅ 四類用法＋三條 prompt＋平台版本 | ✅ 只傳純文字、無依賴語意、#24798 剩一項無對應 |
| Agent view | ✅ V:L16 逐字（使用時機即存在理由） | ✅ 官方三列場景＋`claude --bg`／`claude agents`＋worktree 隔離 | ✅ 研究預覽；官方未寫它能排先後或彙整 |
| Managed Agents | ✅ V:L17 逐字 | 🟡 **半格**：六條時機＋beta header 齊全，但**沒有可貼上就跑的 CLI 指令**——它是平台 API，不是 CLI | ✅ beta、零件狀態、細節指子頁 |
| Self-hosted runner | ✅ V:L18 逐字 | ✅ 三個換來的東西＋場景＋`claude self-hosted-runner` | ✅ public beta、Team／Enterprise、預設關閉 |

**無法填 0 格，半格 1 格**（Managed Agents 的最小指令）。處理方式：該卡明寫「它不是 CLI 指令而是平台 API：帳號預設可用，請求帶 `managed-agents-2026-04-01` beta header 即可開始」——說出它為什麼沒有指令，而不是留白或拿常識補。

## 4. 每題怎麼被解掉（對照冷讀者四題）

| 題 | 現行結果 | 新版怎麼答 |
|---|---|---|
| Q1 workflows 為什麼出 | ✅（靠 L83 的 issue 編號） | 卡三第一欄升級為官方逐字「計畫握在誰手上」＋context 只留最終答案；issue 證據保留在卡五並更正為已關閉、84 則 |
| Q2 subagent 加 workflows 跑什麼 | 🟡 半拿到（唯一缺件：沒有一行 script） | 卡三補官方六條 prompt＋一支 8–12 行 script（存 `.claude/workflows/`、`/<name>` 叫、`/workflows` 看）；「加」字由新節「這八塊怎麼疊」四條正面回答 |
| Q3 teams＋傳訊 vs subagent | ✅ 但「多做什麼」弱 | 拆成卡四、卡五兩張獨立卡（不再共擠一層半句）；官方分界句＋勸退句進卡四；`--name` 長駐專家場景從選型細節第 5 條搬進卡二；補開關 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` |
| Q4 三頁分不分得出 | 🟡 母子頁計費裂成三處 | 計費整組搬回子頁，母頁兩處都只留一句 wikilink；「子頁怎麼分」表新增「本頁」一列；摘要補一句反指 guide（原本單邊） |

## 5. 宣稱「X 會看守」——逐條附腳本行號

| 宣稱 | 真的有嗎 | 出處 |
|---|---|---|
| 儲存格 >120／條列 >200 會被擋 | ✅ 已驗紅 | `scripts/check_cell_limits.py`：`TABLE_LIMIT` L50、`LIST_LIMIT` L51、`_table_cells()` L141、`scan()` L157、`main()` L230；掛 `run_tests.py` |
| 內部用語外洩會被擋 | ✅ 已驗紅 | `scripts/check_reader_language.py`：`TERMS` L51 起、`scan()` L272、`main()` L338 |
| code fence 內的 prompt／script 不受條列上限拘束 | ✅ | `check_cell_limits.py` `body_lines()` L89（`in_fence` 分支直接 `continue`）；同邏輯 `check_reader_language.py` L199 |
| 懸置標記數不會靜默減少 | ✅ 安全（本波不引入也不刪除） | 本頁 `pending_count: 0`（frontmatter L18）、V 第三節同；`check_pending_markers.py` 基線不動 |
| 改節名不會打斷別頁錨點 | ✅ 安全 | `grep -rn "anthropic-agent-stack#" wiki/ weekly/ .claude/ scripts/` ＝ **0 筆**；被改名的 `這些積木能組出什麼架構` 在 `scripts/`／`src/tests/` 零命中 |
| 附錄速查表第 5 欄每週會跟著 radar 走 | ✅ 條文在，但**只證明規則存在、不證明有人做** | `scripts/table_census.py` `_mechanism()` L50＋`MECH_RE` L34（須含「覆寫」等詞）；稿規則-2 刻意維持單行且同時含新節名、`覆寫`、`anthropic-agent-stack`，否則機制欄會由「有」掉回「無」 |
| 八卡三欄格式會被機器看守 | ❌ **無機械看守** | 純人工：`.claude/reporter-rules/wiki-ingest-features.md`「多標三件事」節（稿規則-1）。每日更新時漏欄不會紅，只會在下次頁面健檢被抓到 |

## 6. 自檢（兩支閘直接量本稿要寫進 wiki 的正文）

暫存檔 `scratchpad/wave13-body.md`（234 行，非 wiki 路徑）；兩支 CLI 只吃 wiki 路徑，故以 `scan([Path])` 直接呼叫（`scratchpad/gate.py`）。

```
=== 字元上限閘 === OK: 無命中（0 筆）
=== 讀者語言閘 === OK: 無命中（0 筆）
```

**過程中被擋下並已修 4 處（綠不是一開始就綠）：** 卡二「官方多給了什麼」231 字元（官方續用兩句移進 code block）、卡二「還做不到什麼」208 字元、卡三「還做不到什麼」224 與 214 字元（續跑語意移到 fence 後的散文行）、卡六「派工與看板」命中讀者語言禁詞 `派工`（改「丟工作出去與看板」）。

**驗紅（不只看綠）：** 同一份稿注入一行含 `ingest`／`記者`／`覆寫` 的 213 字元條列＋一格 130 字元儲存格 → 字元上限閘命中 2 筆（`list_item 213/200`、`table_cell 130/120`）、讀者語言閘命中 3 筆（`ingest`、`記者`、`覆寫`，皆 @L236）；移除注入回到 0。**兩支閘確實在量這份稿。**

## 7. 實作後的驗證清單（依序跑，附預期值）

1. `check_reader_language.py` → exit 0｜2. `check_cell_limits.py` → exit 0（本頁零新增命中；注意子頁新增的計費兩條是逐字搬入，指紋若落在 `anthropic-agent-stack` 既有基線內，改頁後會判為 `managed-agents` 的新增——實測若紅，確認其為 <200 字元後即非命中）
3. `check_pending_markers.py` → 本頁標記數維持 0｜4. `table_census.py topics/anthropic-agent-stack` → 3 張表（決策樹是條列不入表）；`附錄：五種形態速查表` 機制欄應為「有（wiki-ingest-features.md）」
5. `check_rules.py` → 綠（本波未動 `.claude/review-registry.json`）｜6. `gen_wiki_frontmatter.py` → `run_tests.py` exit 0
7. `build_web.py` → 錨點 WARN 不增（本頁錨點入邊 0）｜8. `wiki_graph.py explain topics/anthropic-agent-stack` → 出邊 14 → 15（新增 `entities/pricing`）

## 8. 需使用者裁決一格（不自行擴大）

`wiki/index.md` **L102** 摘要「五種形態怎麼挑……編排缺口已由 dynamic workflows 補上大半」在八卡上線後失準，且「補上大半」正是冷讀者判定撐不起的句子的第二份副本。本波授權只及 index L30，故**本稿不動 L102**，列為裁決點：要不要一併改成「八塊官方積木各自為什麼出、讓你多做出什麼」。
