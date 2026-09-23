# 第 16 波冷讀者複驗（2026-09-23）

依序開過的頁（共 7 跳）：`wiki/index.md` → `topics/community-large-codebase-workflow` → `topics/community-tech-tools` → `topics/community-tech-discussions`（讀到第 196 行，其餘用頁內 Grep）→ `topics/code-quality-decline` → `topics/coding-workflow-guide`（跳讀第 27–346、413–542 行，加頁內 Grep）→ `topics/anthropic-agent-stack`（第 26–225 行）

讀者設定：Claude Code 熟手、monorepo 老手，剛接手 200 萬行 monorepo。全程只沿頁面內的連結走。

---

## Q1. 10 個 agent 同時改 monorepo：官方有沒有隔離、社群怎麼做、崩在哪、裝什麼

- **路徑**：index:32 →（第 2 跳）community-large-codebase-workflow 線 1 →（第 3 跳）community-tech-tools「我卡在這裡」。另外補查：第 6 跳 coding-workflow-guide 2a 看 monorepo 的 worktree 設定，第 7 跳 anthropic-agent-stack 看「何時該隔離」。
- **跳數**：3（最短路徑）；補查後共 7
- **結果**：**拿到**
- **拿到的答案原句**：
  - 官方：「`claude --worktree <名字>` 開隔離 session，subagent 設 `isolation: worktree` 各拿暫時 worktree」（community-large-codebase-workflow.md:59）
  - 崩在哪：「4→20 崩潰主因：git lock／DB 連線競爭、context 洩漏、無協調層」（community-large-codebase-workflow.md:71）；「先在 10–20 個 agent 驗證協調機制，每倍增一次重驗」（community-large-codebase-workflow.md:61）
  - 裝什麼：「已經用 worktree 隔離、只差 commit 落地不打架 → 🧩 Claude Code Merge Queue」（community-tech-tools.md:59）；監看用 Omar／HUD（community-tech-tools.md:60）
  - 對 200 萬行很關鍵：「`worktree.sparsePaths` ＋ `symlinkDirectories` —— worktree 只 checkout 需要的目錄」（coding-workflow-guide.md:253）
- **卡住或誤導我的原句**：
  - 「首選 ness，原名 Harness」（community-large-codebase-workflow.md:64、community-tech-tools.md:59）：官方已內建 worktree，ness 比 `claude --worktree` 多做了什麼，頁面沒講。community-tech-tools.md:73 只交代「為什麼不換首選」，沒交代「為什麼要在官方之外另裝它」。
  - 「官方的 20 是上限（Claude Code 一個 session 預設同時 20 個 subagent」（community-large-codebase-workflow.md:66），但 anthropic-agent-stack.md:121 寫 workflow「上限 16 路並行」。兩個上限對應不同積木，頁面沒放在一起講，我一開始以為兩頁互相矛盾。
  - 「《Why 20 Instances Break Down》」（community-large-codebase-workflow.md:71）：這份崩潰分析是整條線最重要的依據，但沒有附連結。

## Q2. 跑三四小時後變笨：是 context 撐爆還是模型退步？怎麼量、量完裁哪裡

- **路徑**：index:32 →（第 2 跳）community-large-codebase-workflow 線 2 →（第 4 跳）community-tech-discussions →（第 5 跳）code-quality-decline「怎麼自己量一次」→（第 3 跳，回頭查）community-tech-tools 的 PrismoDev →（第 6 跳）coding-workflow-guide 2a／第 8 段
- **跳數**：5（拼出答案至少要 5 跳，途中還繞了一圈）
- **結果**：**半拿到**。「為什麼」和「裁哪裡」拿到了，「怎麼量」沒拿到可以照做的步驟。
- **拿到的答案原句**：
  - 為什麼：「『Claude 越用越笨』是模型退步還是 context 腐蝕——……多則實測收斂為 context 腐蝕」（community-tech-discussions.md:67）；「工具輸出直接塞進 context → 早期約束被稀釋 → 模型『越用越笨』。修復法：裁剪 tool output、壓縮歷史、分 session 隔離任務」（community-tech-discussions.md:79）
  - 裁哪裡：「9 個 server ≈ 每輪 38k token 冷啟動」（community-large-codebase-workflow.md:96）；CLAUDE.md「目標 200 行以內」（coding-workflow-guide.md:177）；「任務之間執行 `/clear`」（coding-workflow-guide.md:283）；「/compact 後模型遺忘的不是程式碼而是設計決策的『理由』」（community-tech-discussions.md:80）
  - 最接近「怎麼量」的一句：「還不確定是誰在撐爆 → 先跑 ⌨️ PrismoDev 診斷」（community-tech-tools.md:56）
- **卡住或誤導我的原句**：
  - 「『變笨』先量 context 組成再怪工具」（community-large-codebase-workflow.md:86）：叫我先量，但沒說用什麼量，隨後把我導去 community-tech-discussions 和 code-quality-decline。
  - 「🧰 現在就能下的解：先量 context 組成再怪工具（[[topics/community-large-codebase-workflow]] 線 2）；社群工具目錄的決策表目前沒有對應『感覺變笨、想先量測歸因』的列」（code-quality-decline.md:78）：這句又把我送回出發頁，**形成迴圈**。而且它說決策表沒有對應列，可是 community-tech-tools.md:56 明明有 PrismoDev 診斷這個分支。
  - 「怎麼自己量一次」（code-quality-decline.md:66–76）量的是跨週的 token／模型漂移，不是單一 session 裡的 context 組成，答的不是我問的那件事。
  - 官方的 `/context` 指令全站只出現一次，寫成「`/context` 的 Skills 列」（coding-workflow-guide.md:508），用途是檢查設定有沒有生效，不是拿來量 context 組成。**死路就在這一句**：我知道官方有 `/context`，但 wiki 從沒說過可以用它量 context 被什麼占掉。

## Q3. 已否決的架構決策怎麼讓 agent 下次還記得？auto memory 夠不夠？裝什麼

- **路徑**：index:32 →（第 2 跳）community-large-codebase-workflow 線 3 →（第 3 跳）community-tech-tools brain.md 列 →（第 6 跳）coding-workflow-guide 第 1 段「東西該放哪一層」
- **跳數**：3（拿到做法）；要弄清 auto memory 的定位得走到第 6 跳
- **結果**：**半拿到**。「外化到 repo」的做法和理由拿到了，工具也有指名；但「auto memory 對團隊夠不夠」沒有正面回答，「已否決方案」本身被兩頁用互相打架的說法處理。
- **拿到的答案原句**：
  - 「repo 才是記憶體、模型只是工作者：已確定的架構決策外化到 CLAUDE.md、spec、ADR，不靠模型跨 session 記住」（community-large-codebase-workflow.md:112）
  - 官方也支持寫進 CLAUDE.md：「該放：……專案特有的架構決策」（coding-workflow-guide.md:147）
  - auto memory 的定位：「官方明說它是 context 不是強制設定，要硬擋得用 PreToolUse hook」（community-large-codebase-workflow.md:111）；「auto memory｜`MEMORY.md` 前 200 行／25KB｜Claude 自寫」（coding-workflow-guide.md:204）
  - 裝什麼：「⌨️ brain.md｜要團隊共享而非單機 → 🖥️ OzBrain（付費服務）」（community-tech-tools.md:58）
  - 頁面誠實承認的缺口：「『已否決方案要不要記』仍停在問題點名，沒有工具實作」（community-large-codebase-workflow.md:117）
- **卡住或誤導我的原句**：
  - auto memory 會不會進 git、團隊能不能共用，兩頁都沒寫。「Claude 自寫」（coding-workflow-guide.md:204）講不出它能不能當團隊記憶，而我的問題核心正是「團隊」。
  - 「『已否決方案索引』（對應官方 issue 已關閉、0 reactions）」被列在「已被官方機制取代或證據不足，本頁不再推薦」底下（coding-workflow-guide.md:287）。我讀成「官方已有替代品」，但 issue 被關掉不等於官方有替代機制。community-large-codebase-workflow.md:163 解釋了兩頁的分工，我還是不知道該不該做否決紀錄。
  - ADR 寫好之後怎麼讓 agent 讀到（例如在 CLAUDE.md 用 `@docs/adr/...` import，或放進 `.claude/rules/`），沒有一句可以照做。

## Q4. 多 agent 產出的 PR 誰把關？「71.6%→89.7%」出處拿得到嗎

- **路徑**：index:32 →（第 2 跳）community-large-codebase-workflow 線 4，第 139 行直接附 arXiv 連結。之後在第 6 跳 coding-workflow-guide 第 5 段看到方法論。
- **跳數**：2
- **結果**：**拿到**（原始連結在第 2 跳就拿到了）
- **拿到的答案原句**：
  - 「跨模型交叉審查（Claude 審 Codex）通過率 71.6%→89.7%、反向反而下降（[arXiv 2607.21656](https://arxiv.org/abs/2607.21656)，量的是解題草稿、審查者不能跑測試，不是 PR review）」（community-large-codebase-workflow.md:139）
  - 方法論：「116 則 LiveCodeBench 中／難題、六種條件對照，reviewer 僅見題目與 writer 草稿、不能執行測試……反向（Codex 審 Claude）反而使通過率由 91.4% 降至 82.8%」（coding-workflow-guide.md:438）
  - 誰把關：「審查者 agent 不掛編輯工具、只能輸出意見」（community-large-codebase-workflow.md:138）；「要真的擋住得靠 Stop hook 跑檢查」（community-large-codebase-workflow.md:137）
- **卡住或誤導我的原句**：
  - 這個數字被放在「多 agent 產出誰把關？」的「現在的答案」裡（community-large-codebase-workflow.md:50、139），同一句卻自己說「不是 PR review」。問題問的是 PR 把關，第一眼拿到的數字卻不是在量 PR。
  - 線 4 的「官方已給」只連到第 9 段（community-large-codebase-workflow.md:137）。官方六個 review 入口和價格在 coding-workflow-guide 第 5 段，我是從 index:31 才知道那一段存在，線 4 本身沒指過去。

---

## 分不出差別的兩頁

**第一組：`topics/community-tech-tools` 與 `topics/skill-interest-watch`**（後者我沒點進去，判斷根據是其他頁描述它的句子）
- index.md:22 寫「工具的判斷……每日同步進『興趣類別 skill 總覽』——讀者只需看總覽一頁」，叫我看 skill-interest-watch。
- community-tech-tools.md:44 卻寫「skill-interest-watch 是這張決策表的每日副本……判斷只寫在這一頁」，叫我看自己。
- community-large-codebase-workflow 的四個 🧰 行（:64、:89、:115、:142）全部指向 community-tech-tools。
- 兩頁到底哪頁為準，我**沒弄懂**。讀到 community-tech-tools.md:44 才知道兩頁有主從關係，但 index 叫我去的正好是「副本」那頁。

**第二組：`topics/community-large-codebase-workflow` 與 `topics/coding-workflow-guide`**
- index.md:26–32 把兩頁都排進「開發實務入口」，兩頁都有「官方已給＋社群補位」的結構。community-large-codebase-workflow.md:37 還說四條線的第一條都改成官方零件。
- 讀到 community-large-codebase-workflow.md:163「分界是那頁只收官方機制撐得起的做法、本頁記社群走到哪」才大致懂。可是本頁每條線的第一條也在講官方零件，這條分界讀起來是軟的。

---

## 雷達還是百科

- **index.md**：地圖，兩者都不是。「開發實務入口」表是這站最好用的一塊。
- **community-large-codebase-workflow**：百科。四條主線加「現在的答案」，但子問題表裡帶著日期（09-04、09-16），有一點雷達的殘留。
- **community-tech-tools**：上半「我卡在這裡」決策表是百科，下半工具目錄（:151–265）是雷達式的收錄流水帳。
- **community-tech-discussions**：雷達。「最近在討論什麼」表占掉大半頁，全頁 817 行，百科部分（:47–67）被淹沒。
- **code-quality-decline**：前半（三條線、怎麼量、模型釘選）是百科，後半時序和訊號表是雷達。
- **coding-workflow-guide**：百科，是最像手冊的一頁；頂部「本週 coding 亮點」是雷達插頁。
- **anthropic-agent-stack**：百科。每塊積木都答「為什麼、多做出什麼、還做不到什麼」，可以直接照抄。

---

## 內部用語外洩表

| 檔名:行號 | 原句 | 困惑 |
|---|---|---|
| index.md:3–6 | 「角色：地圖……哲學見 `wiki/CLAUDE.md`『資訊架構哲學』」「收：／不收：／讀法：」 | 讀者一進門先看到維護契約，指向的檔案也不是 wiki 連結，點不進去 |
| index.md:22 | 「工具的判斷……由社群工具目錄每週整理，每日同步進……」 | 這是編輯流程描述，讀者不需要知道誰每週、誰每日 |
| community-large-codebase-workflow.md:98 | 「『該裝什麼』『載入順序』兩篇」 | 用內部簡稱指兩篇文章，沒有連結，也沒寫作者和來源 |
| community-large-codebase-workflow.md:128 | 「兩則概念性觀察（8/7、8/31）」 | 只有日期沒有出處，讀者找不到原文 |
| community-large-codebase-workflow.md:191 | 「%% 週更撈料：patterns 節點以 `**主線：**` 欄位標記……規則：.claude/reporter-rules/community/daily.md %%」 | 讀原始 md 或在 Obsidian 會看到，「撈料」「主線 tag」是維運用語 |
| coding-workflow-guide.md:102 | 「標 `[已補：庫內證據]`，來自既有 `community-tech-patterns` 條目的萃取，非新一輪查證」 | 「庫內證據」「萃取」「新一輪查證」是編輯部流程詞，段標也掛著 `[社群面待補]` |
| coding-workflow-guide.md:100 | 「九段用同一把尺」 | 讀者不知道這是在對誰交代評分一致性 |
| code-quality-decline.md:52 | 「%% 維運備忘：上限 4 列……見 .claude/rules/wiki-ingest-community.md…… %%」 | 同上，讀原始 md 時會看到內部規則檔路徑 |
| code-quality-decline.md:148 | 「⟨Q-01⟩ **Sonar 第三方量化評測**」 | ⟨Q-01⟩ 是懸置標記，讀者不知道 Q 是什麼 |
| code-quality-decline.md:78 | 「%% —（決策表暫無對應列｜候選症狀：感覺變笨，想先量測歸因） %%」 | 維運待辦寫在讀者要找答案的那一行旁邊 |

---

## 撐不起的句子

1. **「社群已確認根因不在模型退步」**（community-tech-discussions.md:77，另見 :67「收斂為 context 腐蝕」）對上 code-quality-decline.md:116–118 三種解釋「都排除不掉」，以及 code-quality-decline.md:41「2026-04 那次是真的，官方認了也修了」。一頁說已確認，另一頁說排除不掉，而且確實有過一次官方承認的退步。
2. **「社群實測卻在 4→20 之間就崩」**（community-large-codebase-workflow.md:66）對上 :71「證據強度：單一深度分析」，而且那份分析沒附連結。「社群實測」說得比證據強。
3. **跨模型審查 71.6%→89.7% 被當成「多 agent 產出誰把關」的答案**（community-large-codebase-workflow.md:50、139）對上 coding-workflow-guide.md:438：LiveCodeBench 116 題、審查者不能跑測試。這份證據撐不起 PR 把關的結論。
4. **「已否決方案索引」被列為「已被官方機制取代或證據不足」**（coding-workflow-guide.md:287）對上 community-large-codebase-workflow.md:117「仍停在問題點名，沒有工具實作」。沒有任何官方機制取代它，被關掉的 issue 也不是反證。
5. **Opus 5 訊號則數對不上**：code-quality-decline.md:58「十四則裡十二則」、:132「18 則……十六則裡十四則」、:157「這 15 則」，同一頁出現三種數字。

---

## 最想改的三件事（讀者立場）

1. **把線 2「先量 context 組成」寫成可以照做的步驟，並打斷迴圈。** 在 community-large-codebase-workflow.md:86 直接寫出用什麼量（官方 `/context` 能看到什麼、PrismoDev 掃什麼），每一項都對應到「量完裁哪裡」。code-quality-decline.md:78 改指向 community-tech-tools 的 PrismoDev 分支，不要再送回出發頁。
2. **線 4「現在的答案」第一條改放官方 review 入口**（連到 coding-workflow-guide 第 5 段的六個入口和價格）。71.6%→89.7% 移到子問題表的「對抗式審查」列，不要當作 PR 把關的答案。
3. **線 3 正面回答「auto memory 夠不夠給團隊用」**：寫清楚它是不是只存在個人機器、會不會進版控。再給一行 ADR 怎麼接進 agent 的具體做法（CLAUDE.md 的 import 或 `.claude/rules/`）。同時統一兩頁對「否決紀錄」的說法。
