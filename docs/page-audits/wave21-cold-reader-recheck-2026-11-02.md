# 第 21 波冷讀者複驗（2026-11-02）

> 聲明：系統自動把專案根目錄 `CLAUDE.md` 載入了 context（內容提到 `wiki/CLAUDE.md` 與搜尋策略）。我沒有照它的搜尋策略做，也沒讀 `wiki/` 以外的檔案；全程從 `wiki/index.md` 出發點 wikilink，單頁內只用列標題與頁內找字。行號都是原始 .md 的行號。

## 1. 四題結果

### Q1 額度掉得快／莫名被扣費：官方認了沒？有沒有繞法？
- **路徑**：index:55 → `entities/pricing`（#事故現在還在發生嗎）→ pricing:318 → `topics/code-quality-decline`；回 index:28 → `topics/community-tech-tools`；回 index:50 → `entities/claude-code-known-issues`（💰 組）
- **跳數**：走了 4 頁；回頭看最短路徑是 index → known-issues:49 → pricing#事故，2 跳
- **結果**：**拿到**（答案是「官方沒認」；繞法只有監看工具和一支社群腳本）
- **答案在哪**：
  - 官方沒認：pricing:301-308（表上 6 列，5 列 🔴 未解，1 列 ⚖️ 司法中）、pricing:339-341（10-27「8 倍」只是單一 Reddit 貼文，未查證）、code-quality-decline:42、:58（token 異常官方沒有專文，#65687 還開著）
  - 繞法：known-issues:95-96（背景 agent 每 30 秒重送整段對話，社群腳本 `no-agent-summary.js` 可關掉）、pricing:308（關掉用不到的工具／connector）、code-quality-decline:67-73（自己量 session log）、community-tech-tools:54-55（監看工具）
- **卡住的原句**：
  - pricing:343 `%% 未列入總表：表滿載… %%`：最新的 10-27 事故被擠出總表，只看總表的讀者看不到「這幾天」的事。
  - known-issues:95 的 10-29 HN 527 分、附可用繞法，是這幾天最強的一則訊號，卻不在 pricing 總表，也不在 code-quality-decline:91-102 的訊號表。冷讀者先進 pricing，會錯過它。
  - index:28 把「帳單爆」帶去社群工具決策表，給的只有看帳工具，回答不了「官方認了沒」。

### Q2 最近兩週的版本、會影響設定的預設值改變、stable 還是 latest
- **路徑**：index:32 → `entities/claude-code-releases`（#現在該跟哪條）→ releases:51 → `feature-radar`（#⚠️ 升級前要知道的預設值與破壞性變更）
- **跳數**：2
- **結果**：**拿到，但有缺口**
- **答案在哪**：
  - 版本表：releases:70-88（v2.1.304–v2.1.316）
  - 該跟哪條：releases:48-50（stable 2.1.309、latest 2.1.316；沒用 Opus 4.8 fast mode 的人 stable 就夠）、releases:42（fast mode 11-30 移除）
  - 預設值改變：feature-radar:32-33（2.1.304 tool search 預設開啟；2.1.302 `-p` 的權限模式與 fork subagent 預設改變，附關閉方法）
- **卡住的原句**：
  - feature-radar:26「核對到 v2.1.304，2026-10-22」：v2.1.305–316 這段破壞性變更沒有核對過，兩週內一半的版本沒有把關。
  - releases:49 已經寫了 2.1.309「bypass 模式改直接拒絕危險 rm」這個行為改變，⚠️ 表裡卻沒有這一列。
  - feature-radar:7-8 的「這禮拜動了什麼」停在 2026-10-22，已經 11 天沒動。

### Q3 hooks 能不能當安全防線、什麼時候會失效
- **路徑**：index:33 → `entities/claude-code-features#hooks：事件、失效模式與能不能當防線`；另從 index:128 進 `topics/ai-agent-safety` 交叉比對
- **跳數**：1（交叉比對再加 1）
- **結果**：**拿到**
- **答案在哪**：features:154-164（失效模式表）、features:166-173（結論：觸發了就是硬擋，但不保證會觸發）、features:47（摘要）
- **卡住的原句**：
  - features:170「要保證一定擋，用 deny 規則或沙箱」，和 ai-agent-safety:44、:77、:91「deny-list 也不是安全邊界，要擋就用 allow-list 或沙箱」直接衝突。hooks 節沒有連到 ai-agent-safety，讀者只讀 features 會照著用 deny-list。
  - releases:70 v2.1.316「修 PowerShell hook exit 2 沒擋」是一條 hook 失效模式，失效表 features:156-164 沒收。
  - 失效表 features:145-152 的「去哪看」欄寫「已知問題 #6305」「版本表 v2.1.294」，都是純文字，點不過去。

### Q4 平行分派 subagent：有哪幾種型別、差在哪、我該選哪種
- **路徑**：index:31 → `topics/anthropic-agent-stack`（#二、內建 subagent、#你該用哪個）→ agent-stack:90 → `entities/claude-code-features#Subagent 型別差異對照`
- **跳數**：2
- **結果**：**拿到**
- **答案在哪**：features:177（平行分派選哪種：預設背景、20 路；要共用 cache 選 fork；要互派任務選 teammate）、features:179-238（四條軸線）、agent-stack:217-223（選型三問）
- **卡住的原句**：
  - index 沒有一列寫「subagent 型別／平行分派」。index:31 講的是「自己跑幾小時／過夜」，index:36 講的是多 agent 分工，兩列都要猜。
  - features:177「什麼都不設…subagent 就在背景跑」和 features:228「主對話需要結果才能繼續時是前景」，第一句沒帶這個例外。
  - features:179「四條獨立軸線」：讀者問的是「哪幾種型別」，頁面答的是四軸組合，第一次讀要轉一下才對得上。

## 2. 入口
| 題 | index 哪一列 | 直覺嗎 |
|---|---|---|
| Q1 | :55 pricing「還在發生的計費事故」（:28「帳單爆」會帶錯方向） | 半直覺：開發實務入口沒有「額度掉得快，官方認了沒」這一列，而 known-issues:49 正好就是這句 |
| Q2 | :32 | 直覺，一列直達兩頁 |
| Q3 | :33 | 直覺，錨點直達 |
| Q4 | :31（猜的） | 不直覺：沒有一列點名 subagent 型別 |

## 3. 分不出差別的兩頁
- `entities/pricing#事故與爭議` 和 `entities/claude-code-known-issues` 的 💰 組：同一批 issue（#16157、#38335、#79773、#37394）兩邊都逐條寫。known-issues:49 說「官方認了沒去 pricing」，但 pricing:301 的總表又會漏掉 known-issues 裡比較新的條目。
- 次要的一組：`topics/anthropic-agent-stack` 和 `topics/community-multi-agent`（index:31 和 :36）。從 index 的鉤子分不出 Q4 該進哪一頁。

## 4. 百科還是雷達
| 頁 | 判定 |
|---|---|
| entities/claude-code-features | 百科 |
| topics/anthropic-agent-stack | 百科 |
| topics/ai-agent-safety | 百科（入口）＋雷達（時段總結） |
| entities/pricing | 前 290 行是百科，後 600 行是雷達事件流，雷達佔大頭（頁內 :35 自己也判了要拆） |
| topics/code-quality-decline | 雷達（頂部的三條線表偏百科） |
| entities/claude-code-releases | 雷達（頂部「現在該跟哪條」是百科） |
| feature-radar | 雷達 |
| entities/claude-code-known-issues | 雷達 |
| topics/community-tech-tools | 雷達／目錄 |
| entities/claude-code（母頁） | 雷達＋路由 |

## 5. 內部用語外洩（10 處）
1. pricing:295「本表上限 6 列，滿載時較新的活躍事故會暫時列在下方事件流（標『未列入總表』）」：把維運規則講給讀者聽
2. pricing:335「🔎 查無官方（標…｜查…｜複 2026-11-24）…08-29 `訊` 為探針假命中，已移除」
3. releases:81「❓ 待查證（標 2026-10-21｜查 vertex-sdk-v1.0.0、取樣參數）」
4. feature-radar:26「不是本庫的報導覆蓋率」
5. feature-radar:52「因上限 12 列移出的較舊門檻」
6. feature-radar:28「本站報導過的新功能（來源日報）」
7. community-tech-tools:54「🟡（判 08-27｜查 09-22，287★）」：判／查記號沒有圖例
8. claude-code:57「上限 8 列」
9. features:141「本節只彙整與導覽，細節留在原處：版本頁…已知問題頁各組」
10. features:255「逾 90 天未回訪時在此標明」

（另有 releases:38、features:38、claude-code:44 的 `%%…第 21 波…%%`。如果網站版會濾掉 `%%` 就不算外洩，原始 md 上看得到。）

## 6. 撐不起的句子
- features:170「要保證一定擋，用 deny 規則」：和 ai-agent-safety:91（deny-list 不是安全邊界）衝突。
- releases:49「沒用 Opus 4.8 fast mode，stable 已夠」：feature-radar:26 自承 2.1.305 之後沒核對，這句的前提沒有被驗證；2.1.316 的 PowerShell hook 修正也只在 latest。
- releases:48「差 7 個版號」：中間實際發布的只有 310、311、312、314、316 五版（313 不存在，見 releases:66），「7 個」會讓人以為有 7 版。
- code-quality-decline:121「與既有十一則一致」，和同節 :89「表上 10 則」數字對不上。
- pricing:339 標題「稱 Anthropic 已證實服務端錯誤一樣消耗付費額度」：標題就寫「已證實」，括號裡才說未查證，掃標題的讀者會當成官方認了。
- features:177「什麼都不設就在背景跑」：沒帶 features:228 的前景例外。

## 7. 最想改的三件事
1. **features 的 hooks 結論和 ai-agent-safety 對齊**：features:170 改成「allow-list 或沙箱」，加連到 ai-agent-safety#官方現在擋到哪；失效表補上 2.1.316 PowerShell exit 2；「去哪看」欄改成可點的連結。
2. **補齊 ⚠️ 預設值表到 v2.1.316**：至少補 2.1.309 bypass 拒絕 rm、2.1.316 fast mode 移除。releases:49 的「stable 已夠」等核對完再下。
3. **Q1 收一個家**：index 開發實務入口加一列「額度掉得快／被扣費，官方認了沒」，直接指到 pricing#事故現在還在發生嗎。總表放寬，或在表下加一行「最近 7 天新增」（10-27 8 倍、10-29 背景 agent 重送），讓「這幾天」的事進得了第一屏。
