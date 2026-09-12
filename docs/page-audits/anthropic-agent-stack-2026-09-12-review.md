# 評審：topics/anthropic-agent-stack 第 13 波提案（2026-09-12）

評審：主 session 親做（減交棒版）。對象：`-proposal.md`（83 行）、`-proposal-map.md`（74 行）、`-draft.md`（314 行）。上游：健檢卡（含第 8 節預測對照）、冷讀者、verified（含第五節補查）。

## 結論

推薦案採納：換軸不重寫關係軸，八卡＋怎麼疊＋三問決策樹，選型表與六層降附錄。去向表抽驗 6 段全數對上（L47–48 條文搬規則檔、L68–69 搬子頁、L70–71 進附錄細節區、L83 拆進卡四卡五、L61 硬錯改指官方專頁、L114–116 一字不動）。兩處 🔴 都在「宣稱逐字卻不是逐字」，修法可直接貼上；🟡 七條。修完放行實作。

## 四視角

### 明天的維護者

- 🔴 **R1 最小 script 形狀與官方不符**（稿 L85–97）。官方 workflows 頁的 script 是頂層 `await`、四原語為注入的全域函式，沒有 `export default async function ({ agent, … })` 這層包裝；`parallel()` 收的是 agent 任務集合而非已呼叫的 promise 陣列（官方例只示範 `agent()`＋`pipeline()`）。稿裡這支存進 `.claude/workflows/` 會跑不起來或行為不明。**修法：整段換成官方 `audit-routes` 例的形狀，一字對照官方頁，不用 `parallel()`：**

  ```js
  export const meta = {
    name: 'audit-routes',
    description: 'Audit every route handler for missing auth checks',
  }

  const found = await agent('List every .ts file under src/routes/.', {
    schema: { type: 'object', required: ['files'], properties: { files: { type: 'array', items: { type: 'string' } } } },
  })

  const audits = await pipeline(found.files, file =>
    agent(`Audit ${file} for missing authentication checks.`, { label: file }),
  )

  return audits.filter(Boolean)
  ```

  其後說明句改為：「`agent()` 派一個，`pipeline()` 逐項流水，`parallel()` 齊發等全收，`phase()` 在進度畫面分組；四者是 script 裡直接可用的全域函式，不用 import。被停掉或 API 錯的 agent 回 `null`，所以最後 `.filter(Boolean)`。」（官方 workflows 頁「What the saved script looks like」節，2026-09-12 查證）
- 🟡 **R2 規則-1 換掉三點後，同節「為什麼落點」段仍寫「積木架構節回答它們之間怎麼講話」**（規則檔 L290）。修法：該段首句改「該頁八張積木卡答每塊為什麼出、讓你多做出什麼；附錄六層答它們之間怎麼講話」，其餘不動。
- 🟡 **R3 規則-2 是句內取代不是整行取代**。規則檔 L300 是單一長行，含「每次 /wiki-lint」整段；實作者只能替換「母頁 [[topics/anthropic-agent-stack]] 的 `## 你該用哪個` 表……不得留舊值」這一子句，行數不變。取代後跑 `python scripts/table_census.py`，確認母頁「附錄：五種形態速查表」那列機制欄為「有（wiki-ingest-features.md）」（`_mechanism()` 要求命中行含 slug，該行有 `[[topics/anthropic-agent-stack]]`，可過）。

### 機器

- 🟡 **R4 callout 日期語意**（稿 L24）：「最近一次積木層級變動（2026-09-10）」把查證日當變動日。修法：「（2026-09-10 查證時已生效）」。
- 🟡 **R5 頁尾 `## 子頁怎麼分` 新增「本頁」列**：`check_hierarchy.py` 若把該表當子頁清單解析，「本頁」不是 wikilink 可能報錯。實作者跑閘後若報，改把「本頁」列拿掉、改成表上方一句「本頁答：八塊積木各自為什麼出、讓你多做出什麼、怎麼疊、怎麼挑」。
- 閘：設計者自檢 `check_cell_limits.py`／`check_reader_language.py` 各 0 筆並驗紅，採信；懸置標記本頁 0，稿內無 ⟨Q-xx⟩，不引入。`build_web.py` 錨點 WARN 數以實作前為基線。

### 冷讀者

- 🔴 **R6 agent teams 兩條 prompt 標「可以逐字抄」但是改寫**（稿 L109–110）。官方原文是多行，改寫後失去「Have them each review and report findings」「Update the findings doc with whatever consensus emerges」這些關鍵句。修法：換成官方逐字：

  ```
  Spawn three teammates to review PR #142:
  - One focused on security implications
  - One checking performance impact
  - One validating test coverage
  Have them each review and report findings.
  ```
  ```
  Users report the app exits after one message instead of staying connected.
  Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
  each other to try to disprove each other's theories, like a scientific debate.
  Update the findings doc with whatever consensus emerges.
  ```
- 🟡 **R7 workflows 六條 prompt 少了觸發前綴**（稿 L73–78）。官方每條以 `use a workflow to` 開頭，那正是觸發字；讀者照抄稿裡的版本不會開 workflow。修法：六條各補回 `use a workflow to `，第二條官方原文為 `use a workflow to run npx tsc --noEmit and keep fixing the reported errors until the type check passes or two rounds in a row make no progress`，照官方。
- 🟡 **R8 `/goal` 卡「沒有跨 session 記憶」**（稿 L50）與官方 goal 頁「Resume with an active goal」相左：resume 會帶回未完成的 goal，只重置回合數、計時與 token 基線。修法：該句改「跨 session 只帶條件不帶進度：resume 會還原未完成的 goal，但回合數、計時與 token 基線歸零」。
- 🟡 **R9 subagent 卡「以 Opus 為上限」歸屬**（稿 L65）：官方只對 Explore 寫 capped at Opus；general-purpose 走 `CLAUDE_CODE_SUBAGENT_MODEL` 或主對話模型。修法：「Explore 的模型繼承主對話、在 Claude API 上以 Opus 為上限」。
- 稿 L58 `claude --agent code-reviewer --name reviewer-1` 是官方兩個旗標的組合非官方單句，可留，句尾加「（`--name` 自取）」。

### 治理

- 🟡 **R10 index L102 摘要失準（設計者列為裁決點）**：主 session 代判**改**，理由是 index 只放路由、摘要句是入口句，屬「同維護者鄰居只改入口句」範圍；記 ledger。修法：L102 摘要欄改「官方 agent 積木總覽：八塊積木各自為什麼出、讓你多做出什麼、怎麼疊；選型表與六層架構收附錄　↳ 子故事：[[entities/managed-agents]]」，其餘欄不動。
- 使命句、不拆頁、不砍節、計費歸子頁、選型表與六層降附錄：皆在使用者已批範圍內。`coding-workflow-guide` 三處引用節名「你該用哪個」保留，不斷鏈。`overview.md` L24 留給週更。

## 照順序執行（＝實作單，交 Sonnet）

1. 讀本檔、`-draft.md`、`-verified.md`；不讀其他。基線：`PYTHONIOENCODING=utf-8 python scripts/build_web.py 2>&1 | grep -c WARN`、`python scripts/check_pending_markers.py` 的標記數，記下。
2. 把稿一（A）fence 內全文套用 R1、R4、R6、R7、R8、R9 與 L58 括號後，整段取代 `wiki/topics/anthropic-agent-stack.md` frontmatter 之後全部正文（L25–116）。
3. 子頁 `wiki/entities/managed-agents.md`：B-1 取代 L59 那句；B-2 在 `## 熱度與試用價值` 節末、`## 接下來看什麼` 之前插入 `## 怎麼計費` 兩條（逐字）。
4. `wiki/feature-radar.md` L227 只改第 5 欄（C-1）。
5. `wiki/index.md` L30 照 C-2；L102 照 R10。
6. `.claude/reporter-rules/wiki-ingest-features.md`：規則-1（取代「判定為 agent 相關時…」段＋三點）、R2（「為什麼落點」首句）、規則-2 照 R3 句內取代、規則-3 取代負責頁面列；`docs/rules-changelog/wiki-ingest-features.md` 補 2026-09-12 段（三句：換軸原因＝16 格 11 無是軸選錯；八卡三欄固定；社群案例只 wikilink）。
7. 跑 `python scripts/gen_wiki_frontmatter.py`（先 `--help` 看是否需帶頁名），讓母頁與子頁 frontmatter 更新。
8. 閘，全部帶 `PYTHONIOENCODING=utf-8`：`check_reader_language.py`、`check_cell_limits.py`、`check_pending_markers.py`（不低於基線）、`check_rules.py`、`check_hierarchy.py`（若 R5 報錯照 R5 修）、`table_census.py`（確認 R3）、`build_web.py`（WARN 不增）、`run_tests.py`（exit 0）。
9. 回報 ≤70 行：每步一行、每個閘最後一行原樣抄、偏離清單、改動檔案清單。**不 git、不改 run_tests.py、不碰上列以外的檔。**
