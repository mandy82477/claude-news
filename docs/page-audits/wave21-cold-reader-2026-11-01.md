# Wave 21 冷讀者實測（2026-11-01）

> **聲明**：開工時系統自動把專案根目錄 `CLAUDE.md` 載進 context（本站目標、架構、三個動作的說明）。我沒有主動讀它，也沒有讀 `wiki/CLAUDE.md`、`wiki/log.md` 或 `wiki/` 以外的任何檔，但它的內容可能讓我對「日報／記者／主編」這類用語比真正的冷讀者熟一點。
> 讀者設定：把 Claude Code 接進日常開發的工程師。從 `wiki/index.md` 出發，只沿 wikilink 走；單頁內只用「列標題」和 Ctrl-F。行號都是原始 .md 的行號。

---

## 1. 四題結果

### Q1 額度掉得特別快／莫名被扣費，官方認了沒？有沒有繞法？

- **路徑**：index（:53 pricing 列）→ `entities/pricing`「事故現在還在發生嗎」→ pricing:318 → `topics/code-quality-decline`「Token 消耗異常訊號群」→ 回 index（:120 子故事）→ `topics/community-cost`「用量窗口與配額守門」；旁支 index:28 → `topics/community-tech-tools`「我卡在這裡」
- **跳數**：4（含一次回 index）
- **結果**：半拿到
- **答案在哪**
  - 官方沒認：
    - pricing:307–308：#38335、#16157 都是 🔴 未解。
    - pricing:399：官方只新增了一份說明文件，沒有回應 issue 本身。
    - code-quality-decline:58、139：token 異常官方沒有專文，#65687 仍開著。
  - 繞法（散在多頁）：
    - pricing:308：關掉不需要的工具／連接器，查 `Settings > Usage`。
    - pricing:49：把重活挪進 5 小時窗。
    - code-quality-decline:67–73：用 `~/.claude/projects/` 的 JSONL 自己量。
    - community-tech-tools:54–55：監看工具。
    - community-cost:66–96：六類補救。
  - 「這幾天」最貼近的具體原因：community-cost:137–144，背景 agent 面板每 30 秒重傳逐字稿（HN 527 分，附停用腳本）。
- **卡住的原句**
  - pricing:295「本表上限 6 列，滿載時較新的活躍事故會暫時列在下方事件流（標「未列入總表」），一併掃一次才完整」：最近的 #79337（10-24）、#37394 都不在總表，讀者得把 300 行事件流掃完。
  - community-cost:137 那則「隱藏重傳成本」是這幾天最像答案的一則，卻只在技術彙整的逐則條目裡。pricing:318 和 code-quality-decline 的訊號表（:91–102）都沒有連過去。
  - index:28 把「帳單爆」導到社群工具目錄，那裡只回答「裝什麼看帳單」，不回答「官方認了沒」。

### Q2 最近兩週出了哪幾版？有沒有改預設值？值不值得升、stable 還是 latest？

- **路徑**：index（:15 feature-radar）→ `feature-radar`「⚠️ 升級前要知道的預設值與破壞性變更」→ feature-radar:28 → `entities/claude-code#版本更新`
- **跳數**：2
- **結果**：半拿到
- **答案在哪**
  - 版本：claude-code:712–730，10-18～10-31 共 10 版：2.1.303／304／306／308／309／310／311／312／314／316。
  - 預設值：feature-radar:32–34（v2.1.300／302／304）；claude-code:68（v2.1.302 的 `-p` 權限模式與 fork subagent）。
  - 通道：claude-code:695–704。
- **卡住的原句**
  - feature-radar:26「核對到 v2.1.304，2026-10-22；v2.1.289–v2.1.294、v2.1.296–v2.1.299、v2.1.301、v2.1.303 區間尚未逐版核對」：這兩週一半的版本沒核對過。v2.1.309 把 bypass 模式下危險 `rm` 從追問改成直接拒絕（claude-code:57），v2.1.310 在關 telemetry 時攔下長時間 sleep（claude-code:55；coding-workflow-guide:470 也提到）。兩者都是行為改變，表上都沒有。
  - feature-radar:50「上表你都對不上號，版本面就沒有東西擋著你升級」：這句跟 :26 自承的缺口互相打架。
  - claude-code:697「stable 缺的權限修正與切換建議見 2026-W40 週報開發實務專文」：沒有 wikilink，冷讀者找不到這份「建議」，所以「該裝 stable 還是 latest」沒有結論。
  - claude-code:708「破壞性變更與預設值改變見 [[feature-radar]]「從你現在的版本升上去，會遇到什麼」」：feature-radar 沒有這個標題，實際標題是 :24「⚠️ 升級前要知道的預設值與破壞性變更」。錨點斷了。
  - claude-code 現況清單（:48–108）漏了 v2.1.312、v2.1.303，下方版本表（:714、:729）卻有。同一頁兩處版本清單不一致。

### Q3 用 hooks 擋 rm -rf，能當安全防線嗎？哪些情況會失效？

- **路徑**：index（:126 ai-agent-safety）→ `topics/ai-agent-safety`（死路：全頁 hook 只出現在供應鏈與 Groundtruth，沒有連到 hooks 節）→ 回 index（:26）→ `topics/coding-workflow-guide`（Ctrl-F「hook」）→ coding-workflow-guide:393 → `entities/claude-code#hooks：事件、失效模式與能不能當防線`；旁支 coding-workflow-guide:397 → `topics/community-guardrails`
- **跳數**：4（含一次回 index）
- **結果**：拿到，但兩頁講法互相衝突
- **答案在哪**
  - claude-code:991–1007：失效模式表，結論「hook 是保險絲不是門鎖，硬擋用權限系統」。
  - coding-workflow-guide:199：只有 `exit 2` 才會硬擋。
  - coding-workflow-guide:393–397：`onFailure: "block"`、`blockWritesOutsideWorkingDirectories`，以及 deny 換個寫法就漏。
  - community-guardrails:78–87：守衛本身會靜默失效。
  - rm 專屬的部分：claude-code:57（v2.1.309）、claude-code:88（v2.1.288）、claude-code:703。
- **卡住的原句**
  - coding-workflow-guide:197「`PreToolUse` hook 最硬——它先於任何權限模式檢查，回 `deny` 時連 `bypassPermissions` 和 `--dangerously-skip-permissions` 都擋得住」，對上 claude-code:1007「hook 是保險絲不是門鎖，硬擋用權限系統」。一頁叫你靠 hook，一頁叫你別靠，讀者不知道該信哪頁。coding-workflow-guide:393「強制性要落在 hook 而不是措辭」也站在前一邊。
  - ai-agent-safety:78「把 DROP、DELETE、`rm -rf` 設成要顯式確認才放行」：沒說用 hook 還是 permissions，也沒連到 claude-code#hooks。
  - index 的「💻 開發實務入口」沒有任何一列寫 hooks／擋危險指令。index:48 claude-code 的鉤子是「功能、已知問題、社群工具」，看不出裡面有 hooks 防線專節。

### Q4 平行分派工作，subagent 有哪幾種型別、差在哪、該選哪種？

- **路徑**：index（:31）→ `topics/anthropic-agent-stack`「你該用哪個」＋「二、內建 subagent」→ 頁內沒有連到型別對照 → 回 index（:48）→ `entities/claude-code`（列標題）→ `#Subagent 型別差異對照`
- **跳數**：3（含一次回 index）
- **結果**：半拿到
- **答案在哪**
  - 選 subagent 還是別的積木：anthropic-agent-stack:216–224、:237。
  - 內建 subagent 的限制：anthropic-agent-stack:89；平行上限 20 路：:91。
  - 型別四軸線（內建／自訂／plugin、fork、background、teammate）：claude-code:1009–1065。
  - 角色檔陷阱：claude-code:1067–1078。
- **卡住的原句**
  - anthropic-agent-stack:89「Explore 與 Plan 唯讀……要來回追問改用 `general-purpose`」：這裡只點到三個內建型別，fork、background、teammate 一字未提，也沒連到 claude-code:1009。
  - claude-code:1011「派 subagent 前先看四條獨立軸線，可疊加」：四軸講清楚了「差在哪」，但沒有一句「平行分派選哪種」的建議。讀者得自己從 :1042（fork 共用 cache 較便宜）、:1056（預設依序）拼出答案。
  - claude-code:1056 預設選擇那一句用斜線串了五個條件，讀不出來。

---

## 2. 入口

| 題 | index 哪一列帶我進去 | 直覺嗎 |
|---|---|---|
| Q1 | :53 pricing（「還在發生的計費事故」）；:28 是陷阱 | 半直覺。:28「帳單爆」字面最像，但只導到工具；官方立場在 :53，token 異常又在 :116，三列分散 |
| Q2 | :15 feature-radar | 不直覺。index 沒有「升級／版本／stable」任何一列，只能猜雷達 |
| Q3 | :126 ai-agent-safety（死路）→ :26 coding-workflow-guide | 不直覺。開發實務入口缺 hooks 一列；真答案在 claude-code，index 鉤子沒提 |
| Q4 | :31 anthropic-agent-stack | 直覺，括號裡就寫了 subagent。但型別細節在別頁、沒有連結 |

## 3. 分不出差別的兩頁

- **`entities/pricing`「事故現在還在發生嗎」 vs `topics/code-quality-decline`「Token 消耗異常訊號群」**
  - 同一個 #38335 兩邊都在追：pricing:307 記 855 留言，code-quality-decline:96 記 791 留言，數字不同步。
  - 讀者問的是「額度掉得快」，分不出該看「計費事故」還是「token 異常」。
  - code-quality-decline:46 只說「帳單變多不一定等於模型變差」，pricing:318 反向指回來，兩頁互推，沒有一頁給分界判準。
- **`topics/ai-agent-safety` vs `topics/community-guardrails`**：都在答「怎麼防它亂來」。前者給「沙箱才是邊界」，後者給「搬到 hook」，兩頁的結論方向不同，也沒有互相交代分工。

## 4. 每頁判定

| 頁 | 判 | 理由 |
|---|---|---|
| index | 路由 | — |
| entities/pricing | 上半百科（:41–292）、下半雷達（:326–937） | 一頁兩種讀法，頁頂 :35 自己也判「拆」 |
| topics/code-quality-decline | 雷達為主 | 「怎麼自己量一次」:67 是百科段 |
| topics/community-tech-tools | 百科（決策表 :48）＋雷達（工具目錄 :158） | — |
| topics/community-cost | 雷達 | 「目前結論」只 4 行，其餘是逐則彙整 |
| entities/claude-code | 混合 | 版本與已知問題是雷達；hooks／subagent 節（:976–1082）是百科，埋在 1,231 行的頁裡 |
| feature-radar | 雷達 | — |
| topics/ai-agent-safety | 百科（入口） | — |
| topics/coding-workflow-guide | 百科 | — |
| topics/community-guardrails | 雷達 | — |
| topics/anthropic-agent-stack | 百科 | — |

## 5. 內部用語外洩（10）

1. index:3、:6「見 `wiki/CLAUDE.md`「資訊架構哲學」」「`wiki/CLAUDE.md`「搜尋策略」」：讀者打不開。
2. index:5「盤點用 Grep」「→ `news/`」：維護者視角。
3. pricing:295「本表上限 6 列，滿載時……標「未列入總表」」：維護規則外露，讀者因此要自己掃事件流。
4. claude-code:52、:71「功能候選旗標」「第一階候選旗標＋代號旗標」：沒有定義，要點到 experimental 頁才懂。
5. claude-code:697「2026-W40 週報開發實務專文」：站內沒有連結。
6. claude-code:708「本表只收本庫日報報導過的版本」：「日報」對讀者沒有意義。
7. claude-code:723「❓ **待查證**（標 2026-10-21｜查 vertex-sdk-v1.0.0、取樣參數）」：工作佇列格式。
8. community-tech-tools:54–55「🟡（判 08-27｜查 09-22，287★）」：判／查兩個日期沒有圖例。
9. community-cost:121、:123、:132「**主線：** —」「主線填 —」：欄位填寫說明外露。
10. code-quality-decline:104「證據硬度五值（由來源決定……）」、feature-radar:26「不是本庫的報導覆蓋率」：方法論用語，讀者不需要。

## 6. 撐不起的句子

- **feature-radar:50**「上表你都對不上號，版本面就沒有東西擋著你升級。」
  - 同頁 :26 自承只核對到 v2.1.304，而且中間有多段沒核對。
  - v2.1.309／310 的行為改變不在表上。
- **claude-code:703**「stable 標籤已到 2.1.308……落差已追上」
  - 下一行 :704 就說 v2.1.309 不在 stable，latest 已到 v2.1.316（:712）。「追上」只對 rm 修正成立，不是對整條通道。
- **claude-code:1006**「上表五個 🔴 都是 hook 靜默不作用的路徑」
  - 其中 #9516（沒有中斷 hook）、#7075（profile 隔離）是功能請求，不是「靜默不作用」。
  - :1007 的結論因此建在被灌水的證據上。
- **coding-workflow-guide:197**「`PreToolUse` hook 最硬……連 `bypassPermissions` 都擋得住」
  - 這一行沒有附來源或查證日。
  - 和 claude-code:1005 的官方立場（「要硬性允許或拒絕請用權限系統」）衝突。
- **ai-agent-safety:44**「所以『等官方修到 0%』不會發生」：這是從官方定性推出來的修辭結論，沒有任何官方原句說過不會修。

## 7. 最想改的三件事

1. **index「💻 開發實務入口」補兩列**
   - 「升版前要知道什麼／stable 還是 latest」→ feature-radar#⚠️ 表＋claude-code#發布通道。
   - 「用 hooks／權限擋危險指令」→ claude-code#hooks。
   - 同時修好 claude-code:708 的斷錨點，並把 :697 的「W40 週報建議」寫進站內。
2. **hooks 能不能當防線只留一個家**
   - 把 coding-workflow-guide:197、:393 與 claude-code:1007 的結論對齊（hook 跟 permissions 誰是硬擋，各擋什麼）。
   - ai-agent-safety:78、:132 補連 claude-code#hooks。
   - anthropic-agent-stack:89 補連 claude-code#Subagent 型別差異對照，並在該節加一句「平行分派選哪種」。
3. **「額度掉得快」給一個總入口**
   - 在 pricing「事故現在還在發生嗎」表上方加一段，給三路分流：計費事故／token 消耗變多／自己的配置（背景 agent 面板重傳、subagent 佔 48%），各連 code-quality-decline 與 community-cost 對應條目。
   - 解除「上限 6 列」造成的漏讀，至少把 #79337 這類最近的事故放在讀者看得到的地方。
   - feature-radar 的預設值表補核 v2.1.305–316，或拿掉 :50 那句「沒有東西擋著你」。
