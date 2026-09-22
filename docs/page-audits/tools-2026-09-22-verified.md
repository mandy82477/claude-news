# 第 15 波主編官方查證：topics/community-tech-tools

查證日 2026-09-22。工具：`gh api repos/<owner>/<repo>`（星數／forks／最後 push／archived／issue 數，皆為當日即時值）、`gh api repos/anthropics/claude-code/issues/<n>`、WebFetch 官網、WebSearch（只用於找候選 repo，再以 gh 核）。行號＝對象頁檔案原始行號（含 frontmatter）。「頁面寫什麼」逐字抄自頁面。

## 一、結論（五行）

1. **決策表九個首選裡有三個的 repo 已改名或換家，頁面連結全靠 GitHub 轉址撐著**：Harness（L57 首選、L286 ✅）已改名 **ness-dev/ness**（自述「An IDE for coding with agents」，99★）；Omar（L59 首選、L274 ✅「TUI 儀表板統一管理 100 個 agent」）官網 omar.tech 轉址 omar.rs，repo **omar-os/omar 僅 48★**、自述改為「deterministic, formally specified orchestration」；Cockpit（L208）已改名 **episko**（respeak-io/episko，v0.30.0）。
2. **兩個 ✅／首選的規模證據撐不起「廣泛採用」**：Harness 99★、Omar 48★、Groundtruth（L59 首選、L291 ⚡）**7★、0 forks、最後 push 07-20**，README 自標「claude code v2.1.119 verified」（現行 v2.1.277）。頁面沒有任何一句讓讀者看出這三個判斷分別是 04-27／04-29／05-02 下的、且此後無新證據。
3. **pxpipe 與 Graft 的數字對得上一手**：pxpipe README 逐字「≈25k tokens as text, ≈2.7k image tokens」「~59–70% lower end-to-end bill」（L66 一致）；Graft 已從 NanoNets 轉手 **trailhq/Graft**（8,994★），README 仍宣稱「Token savings +42%」、無第三方覆核，L202 ⚠️ 仍成立。
4. **「額度快用完想收提醒」（第 14 波複驗 Q2 未答完）官方與社群兩側都查到了**：官方 CLI 沒有主動告警——#13585「Add Quota Information Access to Claude Code CLI」**仍 OPEN**（2025-12-10 起，27 則、👍 124），#72718 被判重複於 #65292 且 #65292 **NOT_PLANNED（07-08）**；官方只有被動可見（`/usage` 用量條、狀態列 `rate_limits.*.used_percentage`，見第 14 波查證檔 L44–45）。社群有 ≥3 個做「門檻告警」的工具，本頁一個都沒進決策表（見第四節）。
5. **L238「Claude Usage Widget」✅ 無連結且無法辨識**：GitHub 至少 6 個同名專案（sefaguntepe／rishi-banerjee1／bozdemir／dependentsign／niccolo-sabato／SlavomirDurej），描述各異，頁面那句「讀取速率限制 API 標頭、每 5 秒更新、Windows + macOS」對不上任何一個的自述；它同時是 L54 的次選。

## 二、決策表九列 vs 官方（`gh api`，2026-09-22）

| 列 | 工具 | 頁面寫什麼 | gh 查到什麼 | 判定 |
|---|---|---|---|---|
| L54 帳單爆了 | tare（首選） | L196「Show HN score 84」、⏳、🟡（08-27） | kelviq/tare 287★／13 forks／push 08-28／created 08-12 | 成立，但 08-28 後零 push（25 天） |
| L54 | Claude Usage Widget（次選） | L238 ✅、無連結 | 6 個同名專案，無法對應 | **不可辨識**；見第五節候選 |
| L54 | Frugal Tokens（次選） | L201 連 demo.frugaltokens.com | demo 站只剩標題；主站 301 → dpclark4/frugal-tokens **23★**、push 09-20 | 連結該換 repo；23★ 當次選偏弱 |
| L55 context 撐爆 | pxpipe（首選） | L66「25,000→2,700、帳單降 59–70%（08-05）、forks 8.5%」 | teamchong/pxpipe 7,426★／647 forks（8.7%）／push 09-16／65 issues；README 逐字同數字 | 成立 |
| L55 | Graft（次選） | L202 ⚠️「宣稱 42%、HN 質疑」、連 NanoNets/Graft | 轉手 **trailhq/Graft** 8,994★／820 forks／push 09-22／194 issues；README「Token savings +42%」 | ⚠️ 成立；連結靠轉址 |
| L55 | PrismoDev（次選） | L232 ⚡ | shanirsh/prismodev **20★／push 07-02** | 「⚡ 小圈子」撐不起 |
| L56 大 repo | graphify（首選） | L96「08-31 訊號 11.3 萬星」；L275「40k stars」 | Graphify-Labs/graphify **120,410★**／11,626 forks／push 09-20／1,447 issues | 成立；同頁兩個星數（見第六節） |
| L56 | Understand-Anything／archify／codegraph | L97–99「81,325★／43,378★／69,253★（09-02）」 | 83,707★／**69,632★**／71,801★ | archify 20 天漲 60%（43k→69k）；三者皆活躍 |
| L57 重講一遍 | brain.md（首選） | L74「08-25，504 星」 | mindmuxai/brain.md 552★／push 09-11／0 issues | 成立 |
| L57 | OzBrain（次選） | L199「Show HN 69」、L74「團隊共享」 | 官網活躍：Free 50 篇／Pro $20／Max $99；列 Claude Code 為支援平台；無 GitHub | 成立；**付費 SaaS** 頁面未標 |
| L58 互相覆蓋 | **Harness**（首選） | L286 ✅「多 Git worktree 並行管理」、🟢（04-29 起多來源）；L69 同名提醒 | frenchie4111/harness → **ness-dev/ness** 99★／13 forks／push 09-06／created 04-09；自述「An IDE for coding with agents」；README「Run ten Claudes at once」 | **改名＋定位變**：頁面名字、連結文字、✅ 三者都過期 |
| L58 | Claude Code Merge Queue（次選） | L210 ⏳ | funador/claude-code-merge-queue 125★／push 08-24 | 成立 |
| L58 | omnigent（次選） | L71「9,080 星、forks 14.7%、⚪」 | 10,150★／1,609 forks（15.9%）／push 09-22／**1,420 open issues** | 成立 |
| L59 看不到誰卡住 | **Omar**（首選） | L274 ✅「TUI 儀表板統一管理 100 個 Claude Code Agent」、🟢（05-02 起多來源）、連 omar.tech | omar.tech → omar.rs；repo **omar-os/omar 48★**／8 forks／push 09-18／created 01-24；自述「deterministic, formally specified orchestration」、README 無「100 agents」 | **✅ 撐不起**；「100 個」出處只剩頁面自己 |
| L59 | HUD（次選） | L207 ⏳「走官方 JSON event stream」 | adrida/hud-mode **28★／0 forks／push 08-05** | 成立但極小 |
| L59 | Cockpit（次選） | L208 連 episko.dev | 已改名 **episko**（respeak-io/episko，MIT，v0.30.0，created 07-16） | 頁面名字過期 |
| L60 說做完了沒做 | **Groundtruth**（首選） | L107 🟡（04-27）；L291 ⚡ | vnmoorthy/groundtruth **7★／0 forks／push 07-20**／README「claude code v2.1.119 verified」 | 🟡 成立（單一作者自測），但 ⚡ 撐不起；驗證版本落後 158 版 |
| L60 | Proof Loop（次選） | L223 ⚡ | LeoStehlik/proof-loop 11★／push 09-01 | ⚡ 撐不起 |
| L61 CLAUDE.md 不聽 | —（Writ／Caliber 次選） | L242／L279 皆 Reddit 或無連結 | 無 GitHub 可查；Reddit 不可自動抓取 | 二手不可達，維持 |
| L62 供應商綁死 | Workweave Router（首選） | L213 ⚡、連 workweave/router | → **weave-os/router** 4,735★／128 forks／push 09-22／129 issues；自述「Cut costs 40-70%」 | 成立；連結靠轉址 |
| L62 | claudely／clarp | L270 無連結／L228 Reddit | 無法查 | 二手不可達 |

## 三、改名／轉手／換域名清單（頁面連結現況）

| 行號 | 頁面名／連結 | 現在 | 意義 |
|---|---|---|---|
| L57、L69、L286 | Harness／frenchie4111/harness | ness-dev/ness（Slack 仍叫 harness-chat） | 讀者搜「Harness」找不到；L69「同名提醒」比較的對象已不存在 |
| L59、L274 | Omar／omar.tech | omar.rs／omar-os/omar | 域名與 repo 都換，頁面文字描述（TUI、100 個）與現版自述不符 |
| L208、patterns L1199 | Cockpit／episko.dev | episko（respeak-io/episko） | 名字過期 |
| L55、L202 | Graft／NanoNets/Graft | trailhq/Graft | 轉手；⚠️ 判定不變 |
| L62、L213 | Workweave Router／workweave/router | weave-os/router | 轉址 |
| L201 | Frugal Tokens／demo.frugaltokens.com | dpclark4/frugal-tokens | demo 站已空 |

## 四、考題的官方錨句

### 額度快用完想收提醒（第 14 波複驗 Q2、本波 Q2）
- 官方 CLI **沒有**主動告警：#13585「Add Quota Information Access to Claude Code CLI」OPEN（2025-12-10，27 則留言、👍 124，2026-09-22 仍開）；#32796（03-10）被 luvidal 判「Duplicate of #13585」關閉；#72718（07-01）被 bot 判重複於 #65292，而 #65292「Real-time cost/token usage display and warnings」**closed / not_planned（2026-07-08）**。
- 官方有的只是被動可見（第 14 波查證檔 L44–45 已錨）：`/usage` 方案用量條；狀態列 `rate_limits.five_hour.used_percentage`／`seven_day`／`resets_at`；VS Code 警示橫幅；手機推播。
- 社群「門檻告警」候選（gh 2026-09-22）：jens-duttke/usage-monitor-for-claude **293★**／53 forks／push 09-13（Windows 托盤，門檻告警）；Maciek-roboblog/Claude-Code-Usage-Monitor **8,713★**／push **07-05**（「predictions and warnings」，2025-06 出生）；bozdemir/claude-usage-widget 53★／push 09-21（跨平台，burn alerts）；wavever/CCLimitPing 45★／push 09-14（已在 patterns L1569，自動 continue 型）；AThevon/TokenEater 502★／push 09-08（已在目錄 L186 前後，⏳ 09-16，監控型非告警）；Shendhan-E-Ravi/Claude-Usage-Notifier 0★、arturl95/claude-usage-monitor 0★（09-16／09-20 新生，不達門檻）。
- 判定：**症狀存在（官方 issue 兩條線、冷讀者兩波）、社群解存在、本頁沒列**——是否開列屬設計者／使用者；開列門檻（weekly.md 第 5 條「≥2 筆獨立需求證據」）以 #13585＋#65292 已達。

### 多 agent 互相覆蓋（Q1）
- 首選 repo 的一手自述已變（見第二節 L58）。官方側：Claude Code 自 v2.1.224 起 session 可互傳訊息、agent teams 可命名 subagent 定義（第 14 波查證檔 #24798／#24316 Boris 留言）——「互相覆蓋」的官方緩解是 worktree 隔離（`EnterWorktree`／`isolation: worktree`），頁面 L58 沒指官方對應。

### 把 codebase 畫成架構圖交付（Q3）
- tt-a1i/archify 69,632★／push 09-22／148 issues，活躍；L99 安裝指令 `npx skills add tt-a1i/archify -g` 與 README 一致（未逐字核 README，推論自 skills 慣例）。

## 五、需設計者處理但主編查不到的

- L238 Claude Usage Widget 身分（6 候選）：頁面描述最接近 sefaguntepe（Windows、5h／weekly、閾值告警）或 rishi-banerjee1（macOS、單檔 Swift）；「Windows + macOS」兩者都不符。建議：不猜，改成有連結的具體 repo，或降為「—」。
- L242 Writ、L219 VIR、L228 clarp、L270 claudely、L279 Caliber：只有 Reddit 或無連結，無法查活性；決策表 L61／L62 三個次選全在此列。
- Omar「100 個 agent」（L274）出處不在現版 README／官網；05-02 收錄時的來源在日報，設計者若保留數字須帶「05-02 當時宣稱」。

## 六、同頁數字不一致（主編順手抓到，健檢卡自洽掃描應涵蓋）

| 工具 | 一處 | 另一處 | gh 今日 |
|---|---|---|---|
| graphify | L96「11.3 萬星（08-31）」 | L275「40k stars」（05-02） | 120,410 |
| Groundtruth | L107 🟡（04-27） | L291 ⚡ | 7★ |
| Harness | L57 ⌨️ CLI | L286「多 Git worktree 並行管理」；現版是桌面 IDE | — |
| omnigent | L71「9,080 星、forks 14.7%」 | L205（目錄列，未核） | 10,150／15.9% |

## 七、給設計者三句

1. 決策表的「證據」欄該加一個讀者看得到的「判定日距今多久／首選 repo 現況」訊號：三個首選（Harness／Omar／Groundtruth）四個多月沒回訪，其中兩個已改名、一個 7★——weekly.md「首選只在新證據時更換」在沒人回訪時等於永不更換。
2. 目錄 152 列的「採用」欄有 14 個 ✅，本波抽到的 Harness、Omar、Claude Usage Widget 三個 ✅ 都撐不起（99★／48★／不可辨識）；✅ 的定義（weekly.md 第 3 條「廣泛採用才給」）沒有任何量化門檻與看守。
3. 「額度快用完提醒」是全站唯一有官方 issue、有社群工具、有兩波冷讀者、卻沒有家的症狀；開不開列是裁決點，但「這頁誠實說沒有並指向 patterns L1569」是最低限度。
