---
page: "topics/claude-code-experimental"
kind: "topic"
status: "ongoing"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-19"
last_news_update: "2026-09-19"
update_freq: "每日（有新版本才有新料；Claude Code 近期約一天一版）"
status_main: "ongoing"
days_since_news: 5
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 5
inbound_links: 3
attribution_count: 6
attribution_last: "2026-09-19"
top_source: "build-flags"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 實驗功能追蹤

**狀態：** ongoing
**開始日期：** 2026-09-15
**領域：** 🛠️ 工具/功能
**蒐集邊界：** 每個新版本出貨後，比對程式本體裡新增與消失的 `CLAUDE_CODE_*` 旗標名稱（每版一次）。只看得到名字，看不到行為；逾時、識別碼一類的設定旗標不列。官方態度靠 issue、文件、changelog 的既有監看；社群反應靠本站已抓進來的 HN、Reddit、issue 摘要對名字。名字本身不是承諾。
**更新頻率：** 每日（有新版本才有新料；Claude Code 近期約一天一版）
**最後更新：** 2026-09-24
**最後新聞更新：** 2026-09-24

> **本頁是什麼**（快照 2026-09-16）
> 出貨的 Claude Code 程式本體裡先出現、還沒有任何公告的功能旗標。旗標在這裡分四階：出現在 build、有人談論、官方承認、已出貨或已移除。**每往上一階都要證據連結**，沒證據就停在第一階，讀者一看就知道那只是名字。起因：`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` 在 09-04 的 build 就有了，官方 09-09 才在 issue 承諾出貨並更名 Claude Mods，changelog 到 09-14 仍未提——build 是實驗功能最早露臉的地方，changelog 是最晚的。

> **最新動態**（2026-09-24）
> 2.1.281 新增 9 個第一階旗標：`ARTIFACT_INHERITED_TYPE_GRANT`、`ARTIFACT_TEXT_VARIANT`、`CCR_EARLY_REMOTE_CONNECT`、`COMMIT_BETWEEN_KEYS`、`COORDINATOR_SKILL_GUIDANCE`、`DISABLE_STARTUP_WORK_GATE`、`DISABLE_SUBSTITUTION_RM_PROMPT`、`HOST_GATEWAY_LINEAGE`、`MCP_APPS_HOST`；對帳僅命中來源條目本身，非獨立社群提及，暫不升第二階。

---

## 摘要

- **2.1.281（09-24）新增 9 個第一階旗標**（名單見追蹤表）；另 1 個設定類旗標依蒐集邊界不列；對帳僅命中自身條目，暫不升第二階。
- **2.1.278（2026-09-19）新增 3 個第一階旗標**：`PER_TURN_TIMING`、`SESSION_START_ANNOUNCEMENTS_BEFORE_PROMPT`、代號旗標 `PARSED_WILLOW`；同批消失代號旗標 `DAPPER_LAGOON`；對帳僅命中自身條目，暫不升第二階。
- **2.1.276（2026-09-18）新增 2 個第一階旗標**：`DISABLE_ATTRIBUTION_CROSS_REPO`、`FORCE_TERMINAL_IMAGES`；同批消失 2 個：`HOLD_UNANSWERED_PARKED_PERMISSION`、`RETIRE_UNANSWERED_PARKED_PERMISSION`；對帳僅命中自身條目，暫不升第二階。
- **首批基線 2.1.272（2026-09-14）**：程式本體含 619 個 `CLAUDE_CODE_*` 旗標。09-04 的 2.1.261 到 09-14 的 2.1.272 之間新增 44 個、消失 4 個；新增裡 29 個像功能、15 個是設定類。
- **2.1.273（2026-09-16）新增 3 個第一階旗標**：`CLAUDE_CODE_BRIDGE_CHILD_MACHINE_SETTINGS`、`CLAUDE_CODE_GATEWAY_HINT_HEADERS`、`CLAUDE_CODE_OCHRE_KITE`；對帳僅命中來源條目本身與日報鏡像，非獨立社群提及，暫不升第二階。
- **2.1.274（2026-09-17）新增 6 個第一階旗標**（名單見下方追蹤表）；同批另有 1 個設定類旗標依蒐集邊界不列；對帳僅命中來源條目本身與日報鏡像，暫不升第二階。
- **已確認的一個**：`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`（第 3 階）——官方在 issue #91870 承諾數週內出貨，產品名 Claude Mods，細節與已知問題在 [[entities/claude-code]]。
- **其餘全在第一階**：只有名字。下表的「官方態度」「社群反應」兩欄空白代表本站來源裡還沒有證據，不代表沒有。

## 怎麼讀這一頁

| 階 | 意思 | 升到這一階要什麼證據 |
|---|---|---|
| 1 出現在 build | 程式本體裡有這個名字 | 每版比對自動寫入，不需證據 |
| 2 有人談論 | 社群或 issue 留言提到它 | 至少一個連結（HN、Reddit、issue 留言），由對帳腳本找到 |
| 3 官方承認 | Anthropic 員工或官方文件說了它是什麼 | issue 本文、官方文件頁或 changelog 的連結 |
| 4 已出貨／已移除 | 功能正式上線，或旗標從 build 消失 | changelog 條目，或比對顯示消失的版本 |

## 旗標追蹤表

| 旗標 | 首見 | 階 | 官方態度（證據） | 社群反應（證據） | 最後動靜 |
|---|---|---|---|---|---|
| `CLAUDE_CODE_ARTIFACT_INHERITED_TYPE_GRANT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_ARTIFACT_TEXT_VARIANT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_CCR_EARLY_REMOTE_CONNECT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_COMMIT_BETWEEN_KEYS` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_COORDINATOR_SKILL_GUIDANCE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_DISABLE_STARTUP_WORK_GATE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_HOST_GATEWAY_LINEAGE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_MCP_APPS_HOST` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | ≤2.1.261（09-04） | 3 | 已承認：[issue #91870 本文](https://github.com/anthropics/claude-code/issues/91870) 09-09 改寫「數週內出貨、更名 Claude Mods」，並寫明可用此旗標試玩 | [issue 留言](https://github.com/anthropics/claude-code/issues/91870)：09-04 起 14 人、09-09 官方改寫後 5 人回報用此旗標試玩（2026-09-16 數） | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_PER_TURN_TIMING` | 2.1.278（09-19） | 1 | — | — | 2.1.278 仍在（比對日 09-19） |
| `CLAUDE_CODE_SESSION_START_ANNOUNCEMENTS_BEFORE_PROMPT` | 2.1.278（09-19） | 1 | — | — | 2.1.278 仍在（比對日 09-19） |
| `CLAUDE_CODE_DISABLE_ATTRIBUTION_CROSS_REPO` | 2.1.276（09-18） | 1 | — | — | 2.1.276 仍在（比對日 09-18） |
| `CLAUDE_CODE_FORCE_TERMINAL_IMAGES` | 2.1.276（09-18） | 1 | — | — | 2.1.276 仍在（比對日 09-18） |
| `CLAUDE_CODE_ARTIFACT_DB_STR_REPLACE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_FRESH_READ` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_OPENING_PREFETCH` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_START_KIT` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_FIVE_CLASS_ASKS` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_HOT` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_PATH_PIN` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_QUICKSTART` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_REPL` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ATTRIBUTION_ANNOUNCEMENT` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_AUTO_MODE_SERVER` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_BASH_EDIT_DIFF` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_BRIDGE_CHILD_ARTIFACT` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_BRIDGE_CHILD_AUTO_DEFAULT` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_BRIDGE_CHILD_MACHINE_SETTINGS` | 2.1.273（09-16） | 1 | — | — | 2.1.273 仍在（比對日 09-16） |
| `CLAUDE_CODE_DISABLE_AWAITING_USER_IDLE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_DISABLE_TURN_HANDOFF` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_DISABLE_WINDOWS_SHELL_LAUNCHER` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_EMIT_STARTUP_TIMING` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_FOOTER_INDICATOR` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_GATEWAY_HINT_HEADERS` | 2.1.273（09-16） | 1 | — | — | 2.1.273 仍在（比對日 09-16） |
| `CLAUDE_CODE_MODEL_CAPABILITIES` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_OCHRE_KITE` | 2.1.273（09-16） | 1 | — | — | 2.1.273 仍在（比對日 09-16） |
| `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_POST_TURN_MEMORY` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_POST_TURN_MEMORY_CONFIG` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_POST_TURN_MEMORY_SYNC` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_QUESTION_OPTIONAL_DESCRIPTIONS` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_REMOTE_TOOLS_ADOPT_MCP` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_RESUME_REASON` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_SENDMESSAGE_HANDBACK` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_SESSION_ATTENDED` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_STARTUP_FAILURE_RESULTS` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_TETHER_LIVE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |

## 代號旗標

兩個字拼成的名字，像內部實驗代號，看得出有東西、看不出是什麼。只記出現與消失，不解讀。

| 旗標 | 動靜 |
|---|---|
| `CLAUDE_CODE_PARSED_WILLOW` | 2.1.278（09-19）出現 |
| `CLAUDE_CODE_POLISHED_DEWDROP` | 2.1.262–2.1.272 之間出現 |
| `CLAUDE_CODE_SLEEPY_SNOWFLAKE` | 2.1.262–2.1.272 之間出現 |
| `CLAUDE_CODE_CARVED_SLATE` | 2.1.262–2.1.272 之間消失 |
| `CLAUDE_CODE_DAPPER_LAGOON` | 2.1.276–2.1.278 之間消失 |
| `CLAUDE_CODE_GAULT_KESTREL` | 2.1.262–2.1.272 之間消失 |
| `CLAUDE_CODE_WALNUT_SPIRE` | 2.1.262–2.1.272 之間消失 |

## 已消失

- `CLAUDE_CODE_CCR_LAZY_SUBAGENT_HYDRATE`（2.1.262–2.1.272 之間）
- `CLAUDE_CODE_HOLD_UNANSWERED_PARKED_PERMISSION`（2.1.274–2.1.276 之間，首見版本早於本頁基線，未曾單獨列於追蹤表）
- `CLAUDE_CODE_RETIRE_UNANSWERED_PARKED_PERMISSION`（2.1.274–2.1.276 之間，首見版本早於本頁基線，未曾單獨列於追蹤表）

## 靜默表

第一階超過 30 天沒有任何提及的旗標會摺到這裡，不刪、不進日報。

- 目前無（本頁 2026-09-15 起算）

## 相關實體

- [[entities/claude-code]]：Claude Mods／Function Hooks 的已知問題與版本紀錄住那裡
- [[feature-radar]]：升到第 4 階出貨的功能會進雷達

## 時序

| 日期 | 事件 |
|---|---|
| 2026-09-24 | 2.1.281 新增 9 個第一階旗標（名單見追蹤表）；同批 1 個設定類旗標依蒐集邊界不列；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-15 | 建頁。基線 2.1.272；回填 2.1.261→2.1.272 十日差；`ENABLE_FUNCTION_HOOKS` 以 issue #91870 為證據列第 3 階 |
| 2026-09-16 | review 後修正：黏字清理（原「已消失」誤列 `GOAL_CHECKIN_MINUTES0`，實為位元組黏字）、過濾改 token 式、第 3 階列補連結與提及人數 |
| 2026-09-16 | 2.1.273 新增 3 個第一階旗標：`BRIDGE_CHILD_MACHINE_SETTINGS`、`GATEWAY_HINT_HEADERS`、`OCHRE_KITE`；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
| 2026-09-17 | 2.1.274 新增 6 個第一階旗標（名單見追蹤表）；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
| 2026-09-18 | 2.1.276 新增 2 旗標，消失 2 個；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-19 | 2.1.278 新增 3 第一階旗標（含代號旗標 `PARSED_WILLOW`），代號旗標 `DAPPER_LAGOON` 消失；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
