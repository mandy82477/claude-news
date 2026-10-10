---
page: "topics/claude-code-experimental"
kind: "topic"
status: "ongoing"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-10"
last_news_update: "2026-10-10"
update_freq: "每日（有新版本才有新料；Claude Code 近期約一天一版）"
status_main: "ongoing"
days_since_news: 0
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 0
inbound_links: 21
attribution_count: 22
attribution_last: "2026-10-10"
top_source: "build-flags"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Code 實驗功能追蹤

**狀態：** ongoing
**開始日期：** 2026-09-15
**領域：** 🛠️ 工具/功能
**更新頻率：** 每日（有新版本才有新料；Claude Code 近期約一天一版）
**最後更新：** 2026-10-10
**最後新聞更新：** 2026-10-10
**蒐集邊界：** 每個新版本出貨後，比對程式本體裡新增與消失的 `CLAUDE_CODE_*` 旗標名稱（每版一次）。只看得到名字，看不到行為；逾時、識別碼一類的設定旗標不列。官方態度靠 issue、文件、changelog 的既有監看；社群反應靠本站已抓進來的 HN、Reddit、issue 摘要對名字。名字本身不是承諾。

> **本頁是什麼**（快照 2026-09-16）
> 出貨的 Claude Code 程式本體裡先出現、還沒有任何公告的功能旗標。旗標在這裡分四階：出現在 build、有人談論、官方承認、已出貨或已移除。**每往上一階都要證據連結**，沒證據就停在第一階，讀者一看就知道那只是名字。起因：`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` 在 09-04 的 build 就有了，官方 09-09 才在 issue 承諾出貨並更名 Claude Mods，changelog 到 09-14 仍未提——build 是實驗功能最早露臉的地方，changelog 是最晚的。

> **最新動態**（2026-10-10）
> 2.1.296 新增 4 個候選旗標：3 個進追蹤表（`AGENT_PROGRESS_SUMMARIES`、`WEBSEARCH_CITATIONS_DECLARED`、`WORKFLOW_SUBAGENT_MODEL`），代號旗標 `SNAPPY_PELICAN` 1 個；`CLAUDE_CODE_ARTIFACT_TEXT_VARIANT` 消失升列第 4 階；對帳僅命中來源條目與日報鏡像，暫不升第二階。

---

## 摘要

- **2.1.296（10-10 比對）新增 4 個候選旗標**：3 個第一階（`AGENT_PROGRESS_SUMMARIES`、`WEBSEARCH_CITATIONS_DECLARED`、`WORKFLOW_SUBAGENT_MODEL`）＋代號旗標 `SNAPPY_PELICAN`；`ARTIFACT_TEXT_VARIANT` 消失升第 4 階；另 3 個設定類旗標不列；暫不升第二階。
- **2.1.295（10-09 比對）新增 5 個候選旗標**（名單見追蹤表），皆第一階；另 2 個設定類旗標依蒐集邊界不列。`ARTIFACT_FIVE_CLASS_ASKS`（首見 2.1.262–2.1.272）消失升列第 4 階，`INTRO_FRAME` 同批消失但首見早於追蹤範圍；對帳僅命中來源條目與日報鏡像，暫不升第二階。
- **2.1.294（10-08 比對）新增 1 個候選旗標**：`CLAUDE_CODE_DESKTOP_SKILL_SWITCHES`，第一階；對帳僅命中來源條目與日報鏡像，暫不升第二階。
- **2.1.292（10-07 比對）新增 4 個候選旗標**（名單見追蹤表），皆第一階；對帳僅命中來源條目與日報鏡像，暫不升第二階。
- **2.1.289–2.1.291（10-06 比對）累積新增 18 個候選旗標**：5 個代號旗標（見代號旗標表）＋13 個一般候選（見追蹤表）；對帳僅命中來源條目與日報鏡像，暫不升第二階。
- **2.1.288（10-03 比對）新增 7 個候選旗標**：`DISABLE_STRUCTURED_OUTPUTS` 依[官方 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) 升第 4 階已出貨，其餘 6 個仍第一階（名單見追蹤表）；對帳僅命中自身條目，暫不升第二階。
- **2.1.287（10-02 比對）新增 7 個第一階候選旗標**（名單見追蹤表）；`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`（第 3 階，≤09-04 即在 build 裡）升第 4 階——官方 v2.1.287 Release 正式出貨為「Claude Mods」，同輪已回報 [[feature-radar]] 新增。
- **2.1.286（10-01 比對）新增 8 個第一階候選旗標**（名單見追蹤表）；另 2 個設定類旗標依蒐集邊界不列。`CLAUDE_CODE_AUTO_MODE_CANDIDATE_WORDING`（首見 2.1.284）消失，依消失清單升列第 4 階；對帳僅命中自身條目（來源文章），不算獨立佐證，暫不升第二階。
- **2.1.285（09-30 比對）新增 9 個第一階候選旗標**，`CLAUDE_CODE_DISABLE_WEB_FETCH` 依官方 Release 已出貨升列第 4 階，其餘 8 個仍第一階；另 1 個設定類旗標依蒐集邊界不列。同版消失 7 個（`DIR_SYNC` 家族 6＋代號旗標 `PARCHMENT_FERN`），皆早於本頁追蹤範圍；對帳僅命中自身條目，暫不升第二階。
- **2.1.284（09-28）新增 4 個第一階旗標＋1 個代號旗標**（`WHIMSICAL_ELEPHANT`）；`COMMIT_BETWEEN_KEYS`（首見 2.1.281）依消失清單升列 4 階，`ENABLE_NARRATION` 同批消失但首見早於本頁基線；對帳僅命中自身條目，暫不升第二階。
- **2.1.282（09-25）新增 8 個第一階旗標＋2 個代號旗標**（`ELEGANT_MEADOW`、`SQUISHY_NEWT`，名單見追蹤表）；`CLAUDE_CODE_OCHRE_KITE`（首見 2.1.273）從程式本體消失，依來源條目消失清單升列 4 階已移除；對帳僅命中自身條目，暫不升第二階。
- **2.1.281（09-24）新增 9 個第一階旗標**（名單見追蹤表）；另 1 個設定類旗標依蒐集邊界不列；對帳僅命中自身條目，暫不升第二階。
- **2.1.278（2026-09-19）新增 3 個第一階旗標**：`PER_TURN_TIMING`、`SESSION_START_ANNOUNCEMENTS_BEFORE_PROMPT`、代號旗標 `PARSED_WILLOW`；同批消失代號旗標 `DAPPER_LAGOON`；對帳僅命中自身條目，暫不升第二階。
- **2.1.276（2026-09-18）新增 2 個第一階旗標**：`DISABLE_ATTRIBUTION_CROSS_REPO`、`FORCE_TERMINAL_IMAGES`；同批消失 2 個：`HOLD_UNANSWERED_PARKED_PERMISSION`、`RETIRE_UNANSWERED_PARKED_PERMISSION`；對帳僅命中自身條目，暫不升第二階。
- **首批基線 2.1.272（2026-09-14）**：程式本體含 619 個 `CLAUDE_CODE_*` 旗標。09-04 的 2.1.261 到 09-14 的 2.1.272 之間新增 44 個、消失 4 個；新增裡 29 個像功能、15 個是設定類。
- **2.1.273（2026-09-16）新增 3 個第一階旗標**：`CLAUDE_CODE_BRIDGE_CHILD_MACHINE_SETTINGS`、`CLAUDE_CODE_GATEWAY_HINT_HEADERS`、`CLAUDE_CODE_OCHRE_KITE`；對帳僅命中來源條目本身與日報鏡像，非獨立社群提及，暫不升第二階。
- **2.1.274（2026-09-17）新增 6 個第一階旗標**（名單見下方追蹤表）；同批另有 1 個設定類旗標依蒐集邊界不列；對帳僅命中來源條目本身與日報鏡像，暫不升第二階。
- **已出貨的一個**：`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`（第 4 階）——v2.1.287 正式出貨，產品名 Claude Mods，細節與已知問題在 [[entities/claude-code]]。
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
| `CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES` | 2.1.296（10-10） | 1 | — | — | 2.1.296 仍在（比對日 10-10） |
| `CLAUDE_CODE_WEBSEARCH_CITATIONS_DECLARED` | 2.1.296（10-10） | 1 | — | — | 2.1.296 仍在（比對日 10-10） |
| `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` | 2.1.296（10-10） | 1 | — | — | 2.1.296 仍在（比對日 10-10） |
| `CLAUDE_CODE_AUTOUPDATER_DISABLED_BY_HOST` | 2.1.295（10-09） | 1 | — | — | 2.1.295 仍在（比對日 10-09） |
| `CLAUDE_CODE_RESTRICT_PERSONAL_CONFIG` | 2.1.295（10-09） | 1 | — | — | 2.1.295 仍在（比對日 10-09） |
| `CLAUDE_CODE_SLEEP_COMPACT` | 2.1.295（10-09） | 1 | — | — | 2.1.295 仍在（比對日 10-09） |
| `CLAUDE_CODE_SUBAGENT_CONFIG_WARNING` | 2.1.295（10-09） | 1 | — | — | 2.1.295 仍在（比對日 10-09） |
| `CLAUDE_CODE_WEBSEARCH_CITATIONS` | 2.1.295（10-09） | 1 | — | — | 2.1.295 仍在（比對日 10-09） |
| `CLAUDE_CODE_DESKTOP_SKILL_SWITCHES` | 2.1.294（10-08） | 1 | — | — | 2.1.294 仍在（比對日 10-08） |
| `CLAUDE_CODE_ARTIFACT_PREVIEW_EMULATOR` | 2.1.292（10-07） | 1 | — | — | 2.1.292 仍在（比對日 10-07） |
| `CLAUDE_CODE_ARTIFACT_VERSIONS` | 2.1.292（10-07） | 1 | — | — | 2.1.292 仍在（比對日 10-07） |
| `CLAUDE_CODE_HOST_SKILL_CATALOG` | 2.1.292（10-07） | 1 | — | — | 2.1.292 仍在（比對日 10-07） |
| `CLAUDE_CODE_MANAGED_CONFIG_PREFETCH` | 2.1.292（10-07） | 1 | — | — | 2.1.292 仍在（比對日 10-07） |
| `CLAUDE_CODE_DISABLE_PROACTIVITY` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_HOSTED_DESKTOP` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_RELAUNCH_PROACTIVITY_BASELINE` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_RELAUNCH_PROACTIVITY_DECIDED` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_RELAUNCH_PROACTIVITY_EVER_ON` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_RELAUNCH_PROACTIVITY_LEVEL` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_REMOTE_TOOLS_HOST_ALLOWS_UNATTENDED` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_REMOVE_PROMPT_STRINGS` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_RESUME_TOLERATES_CONTEXT_SEEDS` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_STREAMED_BUMBLEBEE_TEXT` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06，與代號旗標 `STREAMED_BUMBLEBEE` 同批） |
| `CLAUDE_CODE_SUBAGENT_PROMPT_SNAPSHOT` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` | 2.1.289–2.1.291（跨版回填） | 1 | — | — | 2.1.291 仍在（比對日 10-06） |
| `CLAUDE_CODE_CONFIG_WATCH_EVENTS` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_GROWTHBOOK_KICK_ON_WARM_CACHE` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_GZIP_DATADOG_LOGS` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_HOST_WORKTREE` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_HOST_WORKTREE_FENCE` | 2.1.288（10-03） | 1 | — | — | 2.1.288 仍在（比對日 10-03） |
| `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` | 2.1.288（10-03） | 4 | 已出貨：[官方 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) 明列新增此環境變數關閉 structured outputs | — | 2.1.288（10-02）官方 Release 確認已出貨 |
| `CLAUDE_CODE_CCR_EARLY_SKILLS_SYNC` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_CCR_FOLD_FIRST_TURN_RESCAN` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_CCR_SKIP_FRESH_MIGRATIONS` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_GROWTHBOOK_KICK_FROM_INIT` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_GZIP_REQUEST_BODY_BLOCKS` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_MCP_SERVE_TOOL_OUTPUT` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_POLL_EVENT_DECLARATIONS` | 2.1.287（10-02） | 1 | — | — | 2.1.287 仍在（比對日 10-02） |
| `CLAUDE_CODE_ARTIFACT_SHARE` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_AUTO_MODE_HEARTH_MEMBER_RELAY_ROWS` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_AUTO_MODE_TIER` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_CCR_EARLY_PLUGINS_SYNC` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_CONFIG_PROBE` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_MCP_PREWAIT_SERVERS` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG` | 2.1.286（10-01） | 1 | — | — | 2.1.286 仍在（比對日 10-01） |
| `CLAUDE_CODE_DISABLE_WEB_FETCH` | 2.1.285（09-29） | 4 | 已出貨：[官方 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) 明列新增此環境變數關閉 WebFetch 工具 | — | 2.1.285（09-29）官方 Release 確認已出貨 |
| `CLAUDE_CODE_3P_PROBE_WROTE_HAIKU_DEFAULT` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_3P_SEEDED_OPUS_DEFAULT` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_3P_SEEDED_SONNET_DEFAULT` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_HOST_PROMPT_SUPERSEDES_RECORD` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_MCP_SERVE_SETTINGS` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_RESULT_NONCE` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY` | 2.1.285（09-30） | 1 | — | — | 2.1.285 仍在（比對日 09-30） |
| `CLAUDE_CODE_APPEND_PROMPT_HEAD` | 2.1.284（09-28） | 1 | — | — | 2.1.284 仍在（比對日 09-28） |
| `CLAUDE_CODE_AUTO_MODE_CANDIDATE_WORDING` | 2.1.284（09-28） | 4 | — | — | 2.1.286（10-01）消失（來源條目消失清單） |
| `CLAUDE_CODE_RELAUNCH_HOME_TRUST` | 2.1.284（09-28） | 1 | — | — | 2.1.284 仍在（比對日 09-28） |
| `CLAUDE_CODE_SDK_READS_SESSION_STATE` | 2.1.284（09-28） | 1 | — | — | 2.1.284 仍在（比對日 09-28） |
| `CLAUDE_CODE_ARTIFACT_INHERITED_TYPE_GRANT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_ARTIFACT_TEXT_VARIANT` | 2.1.281（09-24） | 4 | — | — | 2.1.296（10-10）消失（來源條目消失清單） |
| `CLAUDE_CODE_CCR_EARLY_REMOTE_CONNECT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_COMMIT_BETWEEN_KEYS` | 2.1.281（09-24） | 4 | — | — | 2.1.284（09-28）消失（來源條目消失清單） |
| `CLAUDE_CODE_COORDINATOR_SKILL_GUIDANCE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_DISABLE_STARTUP_WORK_GATE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_HOST_GATEWAY_LINEAGE` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_MCP_APPS_HOST` | 2.1.281（09-24） | 1 | — | — | 2.1.281 仍在（比對日 09-24） |
| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | ≤2.1.261（09-04） | 4 | 已出貨：[v2.1.287 Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) 正式更名「Claude Mods」上線，內建示範 mod「You should know」 | [issue #91870](https://github.com/anthropics/claude-code/issues/91870) 追蹤串：出貨當日累積 233 則留言、218 個讚 | 2.1.287（10-01）官方 Release 確認已出貨 |
| `CLAUDE_CODE_PER_TURN_TIMING` | 2.1.278（09-19） | 1 | — | — | 2.1.278 仍在（比對日 09-19） |
| `CLAUDE_CODE_SESSION_START_ANNOUNCEMENTS_BEFORE_PROMPT` | 2.1.278（09-19） | 1 | — | — | 2.1.278 仍在（比對日 09-19） |
| `CLAUDE_CODE_DISABLE_ATTRIBUTION_CROSS_REPO` | 2.1.276（09-18） | 1 | — | — | 2.1.276 仍在（比對日 09-18） |
| `CLAUDE_CODE_FORCE_TERMINAL_IMAGES` | 2.1.276（09-18） | 1 | — | — | 2.1.276 仍在（比對日 09-18） |
| `CLAUDE_CODE_ARTIFACT_DB_STR_REPLACE` | 2.1.262–2.1.272（跨版回填） | 1 | — | — | 2.1.272 仍在（比對日 09-14） |
| `CLAUDE_CODE_ARTIFACT_FRESH_READ` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_OPENING_PREFETCH` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_START_KIT` | 2.1.274（09-17） | 1 | — | — | 2.1.274 仍在（比對日 09-17） |
| `CLAUDE_CODE_ARTIFACT_FIVE_CLASS_ASKS` | 2.1.262–2.1.272（跨版回填） | 4 | — | — | 2.1.295（10-09）消失（來源條目消失清單） |
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
| `CLAUDE_CODE_OCHRE_KITE` | 2.1.273（09-16） | 4 | — | — | 2.1.282（09-25）消失（來源條目消失清單） |
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
| `CLAUDE_CODE_DISABLE_ATTRIBUTION_BASELINE_REUSE` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_DISABLE_REFUSAL_RETRY` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_GZIP_REQUEST_BODY_LEVEL` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_PARKED_RUN_BEFORE_CLEAR` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_PROJECTS_SESSION` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_REMOTE_TOOLS_SPECULATIVE_CLASSIFIER` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_WEBSEARCH_CCR_PROXY_FAST` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |
| `CLAUDE_CODE_WEB_SEARCH_FAST_ARG` | 2.1.282（09-25） | 1 | — | — | 2.1.282 仍在（比對日 09-25） |

## 代號旗標

兩個字拼成的名字，像內部實驗代號，看得出有東西、看不出是什麼。只記出現與消失，不解讀。

| 旗標 | 動靜 |
|---|---|
| `CLAUDE_CODE_SNAPPY_PELICAN` | 2.1.296（10-10）出現 |
| `CLAUDE_CODE_CALM_MOCHI` | 2.1.289–2.1.291（跨版回填）出現 |
| `CLAUDE_CODE_CURRIED_TRINKET` | 2.1.289–2.1.291（跨版回填）出現 |
| `CLAUDE_CODE_HARMONIC_RIDDLE` | 2.1.289–2.1.291（跨版回填）出現 |
| `CLAUDE_CODE_RIPPLING_TULIP` | 2.1.289–2.1.291（跨版回填）出現 |
| `CLAUDE_CODE_STREAMED_BUMBLEBEE` | 2.1.289–2.1.291（跨版回填）出現 |
| `CLAUDE_CODE_WHIMSICAL_ELEPHANT` | 2.1.284（09-28）出現 |
| `CLAUDE_CODE_ELEGANT_MEADOW` | 2.1.282（09-25）出現 |
| `CLAUDE_CODE_SQUISHY_NEWT` | 2.1.282（09-25）出現 |
| `CLAUDE_CODE_PARSED_WILLOW` | 2.1.278（09-19）出現 |
| `CLAUDE_CODE_POLISHED_DEWDROP` | 2.1.262–2.1.272 之間出現 |
| `CLAUDE_CODE_SLEEPY_SNOWFLAKE` | 2.1.262–2.1.272 之間出現 |
| `CLAUDE_CODE_CARVED_SLATE` | 2.1.262–2.1.272 之間消失 |
| `CLAUDE_CODE_DAPPER_LAGOON` | 2.1.276–2.1.278 之間消失 |
| `CLAUDE_CODE_GAULT_KESTREL` | 2.1.262–2.1.272 之間消失 |
| `CLAUDE_CODE_WALNUT_SPIRE` | 2.1.262–2.1.272 之間消失 |
| `CLAUDE_CODE_PARCHMENT_FERN` | 2.1.284–2.1.285 之間消失（首見版本早於本頁追蹤範圍，未曾單獨列於追蹤表） |

## 已消失

- `CLAUDE_CODE_INTRO_FRAME`（2.1.294–2.1.295 之間消失，首見版本早於本頁追蹤範圍，未曾單獨列於追蹤表）
- `CLAUDE_CODE_DIR_SYNC_DISABLE_ANCHORING`、`CLAUDE_CODE_DIR_SYNC_ENGINE`、`CLAUDE_CODE_DIR_SYNC_FFWD`（2.1.284–2.1.285 之間消失，首見版本早於本頁追蹤範圍，未曾單獨列於追蹤表）
- `CLAUDE_CODE_DIR_SYNC_GIT`、`CLAUDE_CODE_DIR_SYNC_STREAM`、`CLAUDE_CODE_DISABLE_DIR_SYNC`（同批消失，同屬 `DIR_SYNC` 家族，首見版本早於本頁追蹤範圍）
- `CLAUDE_CODE_ENABLE_NARRATION`（2.1.283–2.1.284 之間，首見版本早於本頁基線，未曾單獨列於追蹤表）
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
| 2026-10-10 | 2.1.296 新增 4 候選旗標：3 第一階（名單見追蹤表）＋代號旗標 `SNAPPY_PELICAN`；`ARTIFACT_TEXT_VARIANT`（首見 2.1.281）消失，列 4 階；對帳僅命中來源條目與日報鏡像，不算獨立佐證 |
| 2026-10-09 | 2.1.295 新增 5 個候選旗標（見追蹤表）；`ARTIFACT_FIVE_CLASS_ASKS` 消失列 4 階、`INTRO_FRAME` 同批消失；對帳僅命中自身條目，不算獨立佐證 |
| 2026-10-08 | 2.1.294 新增 1 個第一階候選旗標 `CLAUDE_CODE_DESKTOP_SKILL_SWITCHES`；`build_flags_mentions.py` 對帳 2 筆，命中僅來源條目與日報鏡像，不算獨立佐證 |
| 2026-10-07 | 2.1.292 新增 4 個第一階候選旗標（名單見追蹤表）；`build_flags_mentions.py` 對帳 4 個，命中僅來源條目與日報鏡像，不算獨立佐證 |
| 2026-10-06 | 2.1.289–2.1.291（跨版回填比對）累積新增 18 個旗標（5 代號＋13 一般候選，名單見追蹤表）；`build_flags_mentions.py` 對帳 18 個，命中僅來源條目與日報鏡像，不算獨立佐證 |
| 2026-10-03 | 2.1.288 新增 7 個旗標；`DISABLE_STRUCTURED_OUTPUTS` 升第 4 階已出貨；其餘 6 個第一階（名單見追蹤表）；對帳僅命中自身條目，不算獨立佐證 |
| 2026-10-02 | `ENABLE_FUNCTION_HOOKS` 升第 4 階：v2.1.287 出貨為「Claude Mods」，已回報 [[feature-radar]] 新增；同版新增 7 個第一階候選旗標（名單見追蹤表） |
| 2026-10-01 | 2.1.286 新增 8 個第一階候選旗標（名單見追蹤表）；另 2 個設定類旗標依蒐集邊界不列；`AUTO_MODE_CANDIDATE_WORDING`（首見 2.1.284）消失，列 4 階；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-30 | 2.1.285 新增 9 候選旗標，`DISABLE_WEB_FETCH` 升 4 階已出貨；消失 7 個（`DIR_SYNC` 家族 6＋代號旗標），皆早於追蹤範圍 |
| 2026-09-28 | 2.1.284 新增 4 個第一階旗標＋代號旗標 `WHIMSICAL_ELEPHANT`（名單見追蹤表）；`COMMIT_BETWEEN_KEYS` 列 4 階、`ENABLE_NARRATION` 消失；不算獨立佐證 |
| 2026-09-25 | 2.1.282 新增 8 個第一階旗標＋2 個代號旗標（`ELEGANT_MEADOW`、`SQUISHY_NEWT`）；`OCHRE_KITE`（首見 2.1.273）消失，依來源條目消失清單列 4 階；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-24 | 2.1.281 新增 9 個第一階旗標（名單見追蹤表）；同批 1 個設定類旗標依蒐集邊界不列；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-15 | 建頁。基線 2.1.272；回填 2.1.261→2.1.272 十日差；`ENABLE_FUNCTION_HOOKS` 以 issue #91870 為證據列第 3 階 |
| 2026-09-16 | review 後修正：黏字清理（原「已消失」誤列 `GOAL_CHECKIN_MINUTES0`，實為位元組黏字）、過濾改 token 式、第 3 階列補連結與提及人數 |
| 2026-09-16 | 2.1.273 新增 3 個第一階旗標：`BRIDGE_CHILD_MACHINE_SETTINGS`、`GATEWAY_HINT_HEADERS`、`OCHRE_KITE`；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
| 2026-09-17 | 2.1.274 新增 6 個第一階旗標（名單見追蹤表）；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
| 2026-09-18 | 2.1.276 新增 2 旗標，消失 2 個；對帳僅命中自身條目，不算獨立佐證 |
| 2026-09-19 | 2.1.278 新增 3 第一階旗標（含代號旗標 `PARSED_WILLOW`），代號旗標 `DAPPER_LAGOON` 消失；對帳僅命中自身條目與日報鏡像，不算獨立佐證 |
