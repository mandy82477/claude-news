# 第 16 波冷讀者實測：大型 codebase × Claude Code（2026-09-23）

開過的頁（依序，共 10 跳）：index → topics/community-large-codebase-workflow → topics/community-tech-tools → entities/claude-code → topics/coding-workflow-guide → topics/community-tech-patterns → topics/community-tech-discussions → topics/code-quality-decline → topics/anthropic-agent-stack → topics/skill-interest-watch

讀者設定：Claude Code 熟手、十年 monorepo 老手，第一次拿 Claude Code 帶 200 萬行 monorepo。只沿頁內連結走。

---

## Q1. 開 10 個 agent 同時改 monorepo：官方隔離、社群做法、崩在哪、裝什麼

- **路徑**：index → community-large-codebase-workflow → community-tech-tools → entities/claude-code → anthropic-agent-stack
- **跳數**：5（最短可行是 index → large-codebase → anthropic-agent-stack 共 3 跳，外加 tools 共 4 跳；但 agent-stack 我是在 large-codebase 頁底「相關實體」才找到，照頁面指示先走 claude-code 等於白走一跳）
- **結果**：拿到
- **拿到的答案原句**：
  - 社群共識：`community-large-codebase-workflow.md:59`「每個 agent 一個 git worktree（或等價的檔案系統隔離）——沒有獨立工作空間，並行必崩」
  - 崩在哪：`community-large-codebase-workflow.md:70`「4→20 崩潰主因：git lock／DB 連線競爭、context 洩漏、無協調層」
  - 規模建議：`community-large-codebase-workflow.md:60`「先從 10–20 個 agent 驗證協調機制；每次倍增規模重新驗證」
  - 官方隔離：`anthropic-agent-stack.md:213`「它們會不會碰到同一批檔案？會 → 用 worktree 隔離（背景 session 會自動搬進 `.claude/worktrees/`）」；指令在 `anthropic-agent-stack.md:168-173`（`claude --bg` ＋ `claude agents`）
  - monorepo 專用設定：`coding-workflow-guide.md:253`「`worktree.sparsePaths` ＋ `symlinkDirectories` —— worktree 只 checkout 需要的目錄」（這條對 200 萬行 repo 最值錢，但 Q1 路線上沒有任何頁指過來，是查 Q3 時順手撞到的）
  - 裝什麼：`community-tech-tools.md:59` 首選 ness；「已經用 worktree 隔離、只差 commit 落地不打架 → Claude Code Merge Queue」
- **卡住或誤導的原句**：
  - `community-large-codebase-workflow.md:43`「官方機制以 [[entities/claude-code]]、[[entities/managed-agents]] 為準」——照做去開 claude-code，得到 866 行的版本流水帳，worktree 只散在版本表（`claude-code.md:502`、`:515`、`:592`），沒有「怎麼開」的一句。真正的官方答案在 agent-stack，這頁沒在線 1 指過去。
  - `community-large-codebase-workflow.md:65`「官方 20 路並行」——對照 `anthropic-agent-stack.md:121`「上限 16 路並行（v2.1.269 起可用 `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` 提到 256）」，分不出「官方上限」到底是 16、20 還是 256（20 路原來是 Managed Agents，不是 CLI）。
  - `community-tech-tools.md:59` ness 與 worktree 是什麼關係沒講：它是用 worktree 做隔離，還是取代 worktree？我已經準備自己開 worktree，還要不要裝 ness，讀不出來。

## Q2. 跑三四小時後變笨：context 撐爆還是模型退步？怎麼量、量完裁哪裡

- **路徑**：index → community-large-codebase-workflow（線 2）→ community-tech-tools → community-tech-patterns → community-tech-discussions → code-quality-decline
- **跳數**：6
- **結果**：半拿到——「是 context 不是模型」有結論有理由、「裁哪裡」有五法；但「怎麼量 context 組成」沒有可執行步驟
- **拿到的答案原句**：
  - 判斷：`community-tech-discussions.md:77`「長 session 性能退化是使用者頻繁回報的現象。社群已確認根因不在模型退步，而在 context 品質管理」
  - 裁哪裡：`community-tech-discussions.md:715`「① 裁剪 tool output ② 壓縮對話歷史 ③ 分 session 隔離任務 ④ 重置前保存關鍵摘要 ⑤ …裁剪現有 context」
  - 固定成本清單：`community-large-codebase-workflow.md:84`「MCP 工具清單、CLAUDE.md、headless 冷啟動都是可量的固定成本」；`community-large-codebase-workflow.md:94`「9 個 server ≈ 每輪 38k token 冷啟動」
  - 官方動作：`coding-workflow-guide.md:283`「任務之間執行 `/clear`」
- **卡住或誤導的原句**（死路在哪）：
  - `community-large-codebase-workflow.md:84`「『變笨』先量 context 組成再怪工具」——沒說用什麼量，往下指到 tools 頁。
  - `community-tech-tools.md:56`「還不確定是誰在撐爆 → 先跑 PrismoDev 診斷」——只有名字，推薦細節沒有它，也沒有證據等級。
  - `community-tech-patterns.md:1503`「提供『先測量、再歸咎工具』的可複用診斷流程」——**我在這句放棄**：節點宣稱有流程，但沒寫步驟、沒寫最後找到的「真正原因」是什麼，來源 `:1505` 只有標題沒有連結。
  - `code-quality-decline.md:68`「量什麼：`~/.claude/projects/` 下每個專案的 JSONL session log」——量的是 token 用量與模型，不是 context 組成；答的是「模型有沒有變差」，不是我問的「context 被誰吃掉」。
  - 官方的 `/context` 指令只在 `coding-workflow-guide.md:508` 以「`/context` 的 Skills 列」一筆帶過，沒有任何頁說「變笨時先打 `/context` 看各塊佔多少」。

## Q3. 架構決策（含已否決方案）怎麼讓 agent 跨 session 記得？auto memory 夠不夠？裝什麼

- **路徑**：index → community-large-codebase-workflow（線 3）→ community-tech-tools → coding-workflow-guide → entities/claude-code
- **跳數**：5
- **結果**：半拿到——有做法（決策外化到 CLAUDE.md／spec／ADR）和工具（brain.md），但「auto memory 夠不夠」沒有任何一頁正面回答，且「已否決方案要不要記」兩頁互相否定
- **拿到的答案原句**：
  - `community-large-codebase-workflow.md:109`「repo 才是記憶體、模型只是工作者：已確定的架構決策外化到 CLAUDE.md、spec、ADR，不靠模型跨 session 記住」
  - `community-tech-tools.md:58`「每開新 session 都要重講一遍 → brain.md｜要團隊共享而非單機 → OzBrain（付費服務）」；`:81`「單機選檔案式，跨人選共享式」
  - auto memory 的容量：`coding-workflow-guide.md:204`「auto memory｜`MEMORY.md` 前 200 行／25KB｜Claude 自寫」
  - auto memory 的缺陷（只能自己拼）：`claude-code.md:221`「session 無法得知 auto-memory 索引完整載入、截斷還是未載入」；`claude-code.md:261`「跨 session 持久記憶（#14227）…官方標記 NOT_PLANNED」
- **卡住或誤導的原句**：
  - `community-large-codebase-workflow.md:111`「『什麼不該再做』也要記——已否決方案沒進 agent 可讀的知識源，agent 會重做一次」 vs `coding-workflow-guide.md:287`「『已否決方案索引』（對應官方 issue 已關閉、0 reactions）…本頁不再推薦」——一頁叫我記、一頁說不推薦，沒有一頁說「否決紀錄該放 CLAUDE.md 還是 ADR」。
  - 「auto memory 是 Claude 自寫」（`coding-workflow-guide.md:204`）對團隊決策意味什麼（個人機器、不進 git、同事看不到）——沒寫，得靠我自己的經驗推。

## Q4. 多 agent PR 誰把關？「71.6%→89.7%」出處、原始連結

- **路徑**：index → community-large-codebase-workflow（線 4，`:136`）→ community-tech-patterns（`:91`、`:1167-1173`）
- **跳數**：3（另在 coding-workflow-guide `:438` 也拿到同一連結）
- **結果**：拿到——論文連結拿得到；Reddit 原帖拿不到連結
- **拿到的答案原句**：
  - `community-tech-patterns.md:1172`「來源：『Claude reviewing Codex's code lifted the pass rate from 71.6% to 89.7%』— Reddit r/ClaudeAI…；[arXiv 2607.21656](https://arxiv.org/abs/2607.21656)（2026-08-13 查證）」
  - 方法論：`coding-workflow-guide.md:438`「116 則 LiveCodeBench 中／難題、六種條件對照，reviewer 僅見題目與 writer 草稿、不能執行測試。方向不對稱：反向（Codex 審 Claude）反而使通過率由 91.4% 降至 82.8%」
  - 把關做法：`community-large-codebase-workflow.md:135`「審查者 agent 不掛編輯工具、只能輸出意見」
- **卡住或誤導的原句**：
  - `community-large-codebase-workflow.md:136` 引數字但不附出處，只在 `:43` 總說出處在 community-tech-patterns——要在 1,710 行的頁裡自己 grep。
  - Reddit 原帖（`community-tech-patterns.md:1172`）**只有標題沒有 URL**，我在這句放棄找 Reddit 原文。
  - 數字是 LiveCodeBench 解題、reviewer 不能跑測試（`coding-workflow-guide.md:438`），不是 PR review；large-codebase 把它放在「多 agent 產出誰把關」的答案裡，套用到我的 PR 流程前得自己打折。

---

## 分不出差別的兩頁

**`topics/code-quality-decline` vs `topics/community-tech-discussions`（「Context 管理生命週期」段）**

兩頁都回答「Claude 越用越笨是怎麼回事」。discussions 說已吵出共識是 context 腐蝕（`community-tech-discussions.md:67`、`:77`）；decline 說三種解釋（含「你這端的配置」）都排除不掉（`code-quality-decline.md:113-118`）。decline 在 `:157` 試圖切開：「這條線和『context 腐蝕』那場爭論不是同一件事」——但沒說**差在哪**。讀到這句我仍分不清：我的症狀是「長 session 變笨」，該信「已確認是 context」還是「三種都排除不掉」？只能自己歸納出：decline 管「同樣任務跨版本變差／變貴」，discussions 管「同一個 session 內越跑越差」——但這個分界兩頁都沒寫出來。

次要：`topics/community-tech-tools` vs `topics/skill-interest-watch`。index `:27` 把「我卡住了」導去 skill-interest-watch，large-codebase 全部導去 community-tech-tools，兩張決策表逐字相同。讀到 `skill-interest-watch.md:40`「完整證據、推薦細節…在 community-tech-tools」才懂一個是副本加星數榜——能分，但多開了一頁。

## 雷達還是百科

- **index**：百科（路由目錄）
- **community-large-codebase-workflow**：想當百科（「現在的答案」），但「還沒解決」與子問題表的證據日期讓它半雷達；社群做法最完整，官方那一半缺
- **community-tech-tools**：百科（決策表＝答案），頂部 callout 是雷達
- **entities/claude-code**：雷達（版本流水與 issue 清單），不適合回答「怎麼做」
- **coding-workflow-guide**：百科，全站最能直接照做的一頁
- **community-tech-patterns**：雷達（逐則收錄的流水帳），只適合當出處庫
- **community-tech-discussions**：雷達（爭論狀態），「Context 管理生命週期」一段是百科
- **code-quality-decline**：雷達（官方回應追蹤），「怎麼自己量一次」是百科
- **anthropic-agent-stack**：百科，官方並行／隔離的最佳答案在這
- **skill-interest-watch**：雷達（每日星數榜）

## 內部用語外洩

| 檔名:行號 | 原句 | 讀起來的困惑 |
|---|---|---|
| community-large-codebase-workflow.md:70 | 「見下方懸置細節 ⟨Q-01⟩」 | 「懸置」是什麼狀態？Q-01 是題號還是 issue？ |
| community-large-codebase-workflow.md:31 | 「每週從 community-tech-patterns 沉澱一次」 | 「沉澱」是編輯流程，不是我要知道的 |
| community-large-codebase-workflow.md:43 | 「屬於這四個痛點的節點」 | 「節點」是什麼的節點？ |
| community-tech-patterns.md:170 | 「主線填並行規模」 | 「填」——這是給維護者的表單欄位說明 |
| community-tech-patterns.md:1171 | 「尚未到 🌊延燒認定所需的天數（3 天以上持續出現）」 | 「延燒認定」是內部規則，對我沒意義 |
| community-tech-discussions.md:709 | 「爭論表第 6 列『…』的最後一則證據」 | 爭論表現在只有 9 列，且依 `:67` 這場已移出表——第 6 列指什麼？ |
| code-quality-decline.md:78 | 「%% —（決策表暫無對應列｜候選症狀：感覺變笨，想先量測歸因） %%」 | 原始檔裡看得到的維護註解（網站會剝，Obsidian 原檔讀者看得到） |
| entities/claude-code.md:243 | 「🔎 **查無官方**（標 2026-08-09｜查 …｜複 2026-10-18）」 | 標／查／複三個日期各是什麼，頁內沒圖例 |
| coding-workflow-guide.md:390 | 「`[已補：庫內證據]`」 | 「庫內證據」＝本站自己的其他頁？比「已深查」弱多少？ |
| index.md:5 | 「快變事實（日期／熱度／近況→頁面標頭，盤點用 Grep）」 | 目錄頁頭在跟維護者講話 |

## 撐不起的句子

1. `community-large-codebase-workflow.md:111`「『什麼不該再做』也要記」 ⟷ `coding-workflow-guide.md:287`「『已否決方案索引』…本頁不再推薦」。兩頁對同一件事結論相反。
2. `community-tech-patterns.md:1170`、`:1173`「arXiv…重現此數字…非單一來源自陳數據」 ⟷ 同頁 `:1167` Reddit 貼文日期 2026-08-04，而論文編號 2607 是 2026-07 投稿、早於貼文——比較像 Reddit 轉述論文，不是獨立重現；`community-large-codebase-workflow.md:146`「學術重現」同樣撐不起。
3. `community-tech-discussions.md:77`「社群已確認根因不在模型退步」 ⟷ `code-quality-decline.md:113-118`、`:157`「三種解釋都排除不掉」。
4. `code-quality-decline.md:118`、`:124`「沒有任何一則『改完設定就恢復正常』的回報」 ⟷ `community-tech-discussions.md:716`「停止添加 context 改裁剪 tool output 後，3 小時任務不再中途失憶（dev.to/kenimo49）」——鄰頁就有一則緩解成功回報。
5. `entities/claude-code.md:502`「v2.1.233（2026-08-14）新增 `--worktree` 旗標」 ⟷ 同頁 `:821`「2026-05-08 v2.1.133：…讓使用者可控制 `--worktree`、`EnterWorktree`…」——五月就已經有 `--worktree`，八月不會是「新增」。

## 最想改三件

1. large-codebase 每條線的「現在的答案」旁直接放一行「官方怎麼做＋連結」（例如線 1 直接指 agent-stack 的 worktree 隔離與 `worktree.sparsePaths`），不要叫我去讀 866 行的 claude-code 流水帳。
2. 「變笨」只留一個家，寫出可照打的量法（先打哪個指令、看哪幾塊、各塊多少算異常），並講清楚「session 內變笨」與「跨版本變差」的分界。
3. 「已否決方案要不要記、記在哪」與「auto memory 夠不夠團隊用」給一個直接答案，兩頁不要互相否定。
