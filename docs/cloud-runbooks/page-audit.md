# 雲端 routine：每日頁面健檢（daily-page-audit-cloud）

`[建立: 2026-09-22]`

**先讀 `docs/cloud-runbooks/_shared.md`**（環境覆寫、收尾閉迴路、無人值守原則），再照本檔執行。

你執行的是 `/page-audit-review`（`.claude/skills/page-audit-review/SKILL.md`）**一波**：廣度優先隊列的下一頁，走完健檢卡 → 冷讀者 → 主編查證 → 設計 → 評審 → 實作 → 複核＋複驗 → 定稿 → ledger。流程、角色、派工順序、邊界全部在該 skill，本檔只承載雲端環境差異，不重複步驟。

---

## 執行原則

**模型：** 主 session 為 `claude-opus-5`（主編查證與裁決代判是判斷最深的地方）。派工時照 skill 角色表帶 `model`（健檢卡／冷讀者／設計者／評審 `opus`，實作者 `sonnet`）；若該環境的 Agent 工具不接受 model 覆寫，照預設派並在 ledger 該波列註明「模型未依角色表」。

**一天一頁，一波一次：** 每次執行只做隊列下一頁；不批次、不擴規模（規模改變要使用者批准，見 skill 原則 8）。

## 隊列：這次審哪一頁

1. 讀 `docs/page-audits/ledger.md`「總帳」表最後一列與最新一節「回訪要查什麼」的「第 1 層下一頁」項。
2. 該項若指名了頁面，審那一頁；若寫「依入邊重算」，用 `python3 scripts/wiki_graph.py explain <slug>` 對它列出的候選逐一取入邊數，取最高者。
3. 候選頁若已在總帳出現過（已審），跳到下一候選；全部已審則把第 1 層走完的事實寫進 ledger，改取第 2 層（已審頁出邊指到、尚未審的頁，同樣依入邊排序）。
4. 開工前 `git log --oneline -5 -- wiki/<那一頁>.md`：若最近 24 小時內有其他 session 的健檢 commit（訊息含「第 N 波」），改取下一候選，避免同頁重審。

## 裁決點：沒有使用者可問

skill 邊界節列的裁決點（拆頁／砍整節／改使命句／砍整頁／併頁／新增頁）在雲端一律**照保守預設**（不拆、不砍、不併、不新增；使命句由主 session 代判取健檢卡推薦案），並：

- ledger 該波列標「主 session 代判」，「使用者裁決紀錄」節置頂加一條 `⏳ 待裁決｜<日期>｜<裁決點>`，列出選項與逐字稿位置；
- `wiki/log.md` 該波 Query 條目歸因句寫明「裁決點屬使用者、尚未裁決，代判保守預設」。

前一波若留有 ⏳ 待裁決且本波對象頁正是它的當事頁，仍照保守預設做本波，不替使用者決定。

## 官方查證（主編親做）

skill 的「主編查證」角色需要 GitHub 與官方站：

- 先跑 `python3 scripts/cloud_egress_check.py --group github`：印 `EGRESS: github OK` 才用 `gh api`／`gh issue view`；`PARTIAL`／`BLOCKED` 時改用 WebFetch（由 Anthropic 端執行，不經沙盒 egress）抓 `https://github.com/<owner>/<repo>` 與 `https://api.github.com/repos/<owner>/<repo>`，抓不到的項目在 `-verified.md` 標「雲端不可達，留待本機」，不猜。
- 官方文件與部落格走 WebFetch；社群平台（Reddit／X）不嘗試抓取，標二手不可達。

## 派工

- 派工用 Agent 工具；`SendMessage` 續用（先 `ToolSearch select:SendMessage`）。該環境若無 `SendMessage`，續用步驟改為重新派同角色並在 prompt 附上前一份交件路徑，ledger 註明。
- 冷讀者仍只准從 `wiki/index.md` 沿連結走，禁止 Glob／全庫 grep／讀 `docs/`——雲端與本機相同。

## 收尾

- 每份交件即 commit（指名路徑），最後定稿照 skill 第 8 步：`python3 scripts/run_tests.py` exit 0 才 commit（`&&` 串住）。
- 隨附的 `gen_wiki_frontmatter.py`／`build_web.py` 產物另開一筆 `chore:` commit。
- **單一 push** 走 `_shared.md` 收尾閉迴路；push 被拒時照 `.claude/skills/web-publish/SKILL.md` `Step 5` 重試。
- 全程只 `git add` 指名路徑，禁止 `git add -A`／`git add .`。

## 完成後輸出摘要

- 審了哪一頁、使命句、定稿改了什麼（五行內）
- 冷讀者原題與複驗的「跳數／結果」對照
- 留了哪些 `⏳ 待裁決`
- 測試／build／push 結果
- 若 skill 步驟表或角色表與本檔不同步，附上 `⚠️` 那一行
