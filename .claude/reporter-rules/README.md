# .claude/reporter-rules/

改本目錄或 `.claude/agents/` 任何檔前，先 Read `.claude/rules/claude-md-edit.md` 與 `.claude/rules/dev-done.md`（這兩處不會自動載入它們）。

wiki 記者 subagent 與 ingest／lint 主編**明文 Read** 的規則檔。**沒有自動載入**——放在這裡就不會佔用每個 session 的開場預算，要用的人自己讀。不帶 `paths:`（那裡沒有自動載入機制，帶了只是裝飾）。

## 記者 × 檔案

| 記者 | daily | weekly | pages |
|---|---|---|---|
| features（🛠️ 工具/功能） | ✅ | — | ✅ |
| community（🌐 社群） | ✅ | ✅ | ✅ |
| commercial（💼 商業） | ✅ | ✅（主編層：pricing 通路與乘數） | ✅ |
| models（🤖 模型） | ✅ | — | ✅ |
| market（投資分析，不在分類路由內） | ✅ | ✅（主編層：回顧結算＋教材頁） | ✅ |
| people（👤 人物） | ✅ | — | —（無結論表） |
| safety-policy（🏛️ 政策/安全） | ✅ | — | ✅ |
| devpractice（開發實務，只收官方使用指南一種條目） | ✅ | ✅ | ✅ |

**頁數不寫在這裡**（拆頁波次每改一次就全錯一輪）：
- 明列頁數 → 讀該記者 `daily.md` 的「負責頁面」表（market 的在 `daily.md` 開頭的「負責頁面：」一句，不是表）
- 實際認領頁數 → `python scripts/reporter_pages.py --all`（依頁面 `domain` ＋ `pending_handoffs.OWNER_OVERRIDES`，含子頁，是唯一權威口徑）
- `pages.md` 的節數 → `grep -c '^## ' .claude/reporter-rules/<類別>/pages.md`

「明列」與「概括覆蓋」的差別很重要：`wiki/CLAUDE.md`「搜尋策略」第 5 路規定，只被「領域＝X 的所有頁面歸本記者」概括條款覆蓋的頁，不算證實會被更新。

六份跨記者共用檔：

| 檔 | 答什麼 |
|---|---|
| `shared.md` | 邊界限制、書寫紀律、回報契約（九欄骨架＋呈現品質審查列＋機械自查列的單一家；欄名與順序由 `scripts/collect_reporter_reports.py` 的 `CORE_FIELDS` 消費，改欄必須同批改該常數與 `.claude/review-registry.json`） |
| `daily-contracts.md` | 每日派工必讀的兩份契約：呈現品質標準（含頂部 callout）、懸置標記語法 |
| `shared-when.md` | 碰到才讀：大型頁面讀取策略、事實更正必回掃、待查證命中處置、轉知接手處置 |
| `page-templates.md` | 建頁與格式：決策框架、蒐集邊界欄位、entities／topics 模板、命名與分類 |
| `page-lifecycle.md` | 頁面活著以後：節名凍結、頁面拆分與階層、時段蒸餾與封存、警示觸發重構 |
| `batch-edit.md` | 批次修改（`scripts/apply_edits.py`）的步驟與禁令。選用：目前只有功能記者在每日派工被要求讀（觸發條件在 `.claude/agents/wiki-reporter-features.md`「開始前必讀」第 5 項：本輪跨頁合計 ≥ 3 處）。試點已結案、不推其他記者，量測與結論在 `docs/workaround-register.md`「已收斂」段 |

## 誰讀哪裡

記者由 `.claude/agents/wiki-reporter-*.md` 的「開始前必讀」清單指名（`shared.md` ＋ `daily-contracts.md` ＋自己資料夾的 `daily.md`／`pages.md`／`weekly.md`，建頁時另加 `page-templates.md`，本輪改動 ≥ 3 處時另加 `batch-edit.md`；`pages.md` 一頁一節，只讀本次要動的頁的那幾節，不整檔讀）；ingest／lint 主編由 `.claude/skills/wiki-ingest/SKILL.md`、`.claude/skills/wiki-lint*/SKILL.md`、`.claude/commands/wiki-backfill.md` 等 command／skill 內文指名（分類與派工正典住 `.claude/skills/wiki-ingest/references/classification.md`，不在本資料夾）。教訓敘事一律住 `docs/rules-changelog/reporter-*.md`，不進 agent 讀取範圍。

與 `.claude/rules/` 的分工：那裡放**主 session 自己會用到**、由 `paths:` frontmatter 觸發載入的規則（`claude-md-edit.md`、`web-reader-design.md`、`collection-scope.md`）。

改動這裡的檔案後照樣跑 `/review-commands`——`scripts/check_rules.py` 與 `.claude/review-registry.json` 的 glob（`.claude/reporter-rules/**/*.md`）已涵蓋本資料夾與子資料夾。
