---
name: wiki-lint-sweeps
description: /wiki-lint B 段：主編親做／親查的十四個週更掃描（5a–5n），涵蓋熱度降溫、逾期待查證清算、結論表退場與投資訊號結算。
disable-model-invocation: true
---

# Wiki Lint — B 段：主編掃描（5a–5n）

由 `.claude/skills/wiki-lint/SKILL.md` 在 A 段（記者收報）之後帶起。**這十四步的觸發邊只有這裡**——它們吃的是外部榜單、官方文件、GitHub issue、圖譜訊號或帳本，類別路由接不到，記者也沒有 web 工具。

**每步的判準與回報格式住 `.claude/skills/wiki-lint-sweeps/references/sweeps.md`，執行該步之前逐字讀對應節**，本檔不重述。回報行原樣填進步驟 8 的 lint 紀錄。

## 十四步

| 步驟 | 做什麼 | 執行方式 |
|---|---|---|
| 5a | feature-radar 熱度降溫 ＋ ⏳ 逾期處置 | 主編親做 |
| 5b | 跨家任務榜單週更（`topics/model-task-leaderboard`） | 主編派 `general-purpose` ＋ `model: "haiku"` |
| 5c | 逾期待查證清算（Lane A／Lane B、結案回掃） | 主編親查 |
| 5d | 歸因忠實度抽查（近 60 天 5 筆） | 主編親做 |
| 5e | pricing「通路與乘數」複查 | 主編親查 |
| 5f | devpractice 週彙整 | 主編派 devpractice 記者（`model: "sonnet"`） |
| 5g | 高引用但停滯（frontmatter signal 消費端） | 主編親做，逐頁二選一時派對應記者 |
| 5h | 投資訊號回顧環（催化劑＋兩週方向結算） | 主編親查 |
| 5i | 安全政策兩頁結論表退場複查 | 主編親做 |
| 5j | 商業健康度四表退場複查 | 主編親做 |
| 5k | 社群三張結論表＋討論兩表退場複查 | 主編派社群記者 |
| 5l | 模型頁世代表複查（fable-5／opus-5） | 主編親做 |
| 5m | code-quality-decline 三條線 issue 狀態複查 | 主編親做 |
| 5n | official-community-gap「官方補了沒」表對官方一手 | 主編親做 |

## 順序與相依

- **5f 必須排在六記者收報之後**：功能記者的 guide 清冊週更、社群記者的 tools 策展先完成，寫入才不會互踩。
- **5e 與 5j 同批看 pricing 的「資料截至」**：5j 核對合作表快照日時以 5e 更新後的值為準。
- 5n 與 5a 同批看官方 CHANGELOG：5a 抓下來的全文可直接給 5n grep，不必抓兩次。
- 其餘各步互不相依，單步失敗只影響該步，其餘照跑。
- 雲端執行 5b／5c／5m／5n 前先跑 egress 探測（**不得未探測就跳過**）；5h 不需探測。5n 吃 GitHub，走 `--group github`，與 5m 同組。判斷表見 `.claude/skills/wiki-lint-sweeps/references/sweeps.md`「雲端 egress 探測」節。

## 邊界

- 由主編（本機主 session 或雲端頂層 session）執行；派工一律 foreground 且帶明確 `model`，記者不可再呼叫 Agent tool 委派。
- `news/` 唯讀、`log.md` 只能 append、繁體中文為主：見 `wiki/CLAUDE.md`「🚫 絕對限制」；wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下。
- 需使用者確認的項目（5a ⏳ 逾期以外的結構性改動、5g 連續 2 輪門檻調整、5k 滿載讓位）一律只回報、寫進步驟 8 的待使用者確認區。
- 驗證閘：十四行回報全部有值（跳過者寫明跳過理由）才算完。

> **沿革檔：** `docs/rules-changelog/wiki-lint.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍）
