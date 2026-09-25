# .claude/reporter-rules/

wiki 記者 subagent 與 ingest／lint 主編**明文 Read** 的規則檔。**沒有自動載入**——放在這裡就不會佔用每個 session 的開場預算，要用的人自己讀。不帶 `paths:`（那裡沒有自動載入機制，帶了只是裝飾）。

## 記者 × 檔案

| 記者 | daily | weekly | pages | 負責頁數 |
|---|---|---|---|---|
| features（🛠️ 工具/功能） | ✅ | —（週更動作寫在 pages.md 的 coding-workflow-guide 節） | ✅ 7 節 | 12 |
| community（🌐 社群） | ✅ | ✅ | ✅ 3 節 | 6 |
| commercial（💼 商業） | ✅ | ✅（主編層：pricing 通路與乘數） | ✅ 6 節 | 6 |
| models（🤖 模型） | ✅ | — | ✅ 3 節 | 7 |
| market（投資分析，不在分類路由內） | ✅ | ✅（主編層：回顧結算＋教材頁） | ✅ 1 節 | 1 |
| people（👤 人物） | ✅ | — | —（無結論表） | 4 |
| safety-policy（🏛️ 政策/安全） | ✅ | — | ✅ 2 節 | 3 |
| devpractice（開發實務，不在分類路由內） | ✅ | ✅ | —（每日不寫頁） | 0（週更寫 guide 一節） |

「負責頁數」是 `daily.md`「負責頁面」表的明列頁數；每位記者實際認領的是 `wiki/index.md` 中領域等於自己那一組的所有頁面（含子頁與日後新增）。

三份跨記者共用檔：

| 檔 | 答什麼 |
|---|---|
| `shared.md` | 邊界限制、讀取策略、書寫紀律、回報契約（八欄骨架的單一家） |
| `page-templates.md` | 建頁與格式：決策框架、蒐集邊界欄位、entities／topics 模板、呈現品質標準（含頂部 callout）、懸置標記語法、命名與分類 |
| `page-lifecycle.md` | 頁面活著以後：節名凍結、頁面拆分與階層、時段蒸餾與封存、警示觸發重構 |

## 誰讀哪裡

記者由 `.claude/agents/wiki-reporter-*.md` 的「開始前必讀」清單指名（`shared.md` ＋自己資料夾的 `daily.md`／`pages.md`／`weekly.md`，建頁時另加 `page-templates.md`；`pages.md` 一頁一節，只讀本次要動的頁的那幾節，不整檔讀）；ingest／lint 主編由 `.claude/skills/wiki-ingest/SKILL.md`、`.claude/skills/wiki-lint*/SKILL.md`、`.claude/commands/wiki-backfill.md` 等 command／skill 內文指名（分類與派工正典住 `.claude/skills/wiki-ingest/references/classification.md`，不在本資料夾）。教訓敘事一律住 `docs/rules-changelog/reporter-*.md`，不進 agent 讀取範圍。

與 `.claude/rules/` 的分工：那裡放**主 session 自己會用到**、由 `paths:` frontmatter 觸發載入的規則（`claude-md-edit.md`、`web-reader-design.md`、`collection-scope.md`）。

改動這裡的檔案後照樣跑 `/review-commands`——`scripts/check_rules.py` 與 `.claude/review-registry.json` 的 glob（`.claude/reporter-rules/**/*.md`）已涵蓋本資料夾與子資料夾。
