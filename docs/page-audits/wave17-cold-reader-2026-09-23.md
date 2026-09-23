# 第 17 波冷讀者實測（2026-09-23）

**實際開過的頁（依序）：** index → topics/community-tech-patterns → topics/community-tech-patterns-archive → topics/coding-workflow-guide → topics/community-tech-tools → topics/community-pattern-trends → topics/model-comparison（頁內 Grep）→ entities/fable-5（頁內 Grep）→ topics/official-community-gap → topics/community-large-codebase-workflow → topics/community-tech-discussions（共 11 頁）

讀者設定：帶 6 個專案、模型分級寫死在 CLAUDE.md、CLAUDE.md 規則常被無視。只沿頁內連結走。

---

## Q1. CLAUDE.md 有 40 條規則常被無視：社群怎麼解？哪些搬去 hook？exit code 幾才真的攔住？

- **路徑：** index → community-tech-patterns（模式概覽「Hooks 與自動化」列）→ archive（06-23 核心條目）→ coding-workflow-guide（第 1 段「東西該放哪一層」）→ community-tech-tools（「CLAUDE.md 寫了它不聽」列）→ community-pattern-trends（趨勢一）
- **跳數：** 我實際走了 6 跳；事後看最短是 3 跳（index → patterns → trends 趨勢一）
- **結果：半拿到**：「該搬哪些」有單一答案、理由和做法；「exit code 幾」三頁給出三種說法，最明確的那句是錯的
- **拿到的答案原句：**
  - community-pattern-trends.md:72「你 CLAUDE.md 裡任何『必須 100% 遵守』的規則都放錯位置了……偏好留 CLAUDE.md，邊界搬 Hooks。」
  - community-pattern-trends.md:74「這條規則被遺漏一次，我會生氣嗎？生氣 → Hook，無所謂 → CLAUDE.md。」＋ :76-83 六列範例表（push --force、.env、prettier）：可直接照著做
  - coding-workflow-guide.md:190「你要某件事每次都發生 → 寫 hook」；:210「PreToolUse hook 最硬……回 deny 時連 bypassPermissions……都擋得住」
  - coding-workflow-guide.md:514 官方失敗模式「過度指定的 CLAUDE.md」→ 修法：沒這條也做得對就刪掉，或改成 hook（40 條規則的人最需要這句，卻埋在第 8 段）
- **卡住／誤導的原句：**
  - community-pattern-trends.md:85「Hook 的原理：exit 1 = 硬攔截」：全庫只有這句給了具體數字。我所知的官方 hooks 文件是 **exit 2** 才會阻擋，exit 1 屬非阻擋錯誤。照這句寫 hook，會寫出一個以為在擋、其實不擋的閘
  - community-tech-patterns-archive.md:279「偵測到 pattern 時，返回 non-zero exit code，強制 Claude 繼續」：沒說是幾號
  - community-tech-patterns-archive.md:526「PreToolUse 四種 exit code：Block、Allow、Modify、Error」：把「決策種類」寫成「exit code」，看完更不知道要回哪個數字
  - community-tech-tools.md:80 說「答案是機制不是工具，做法見 [[topics/community-tech-patterns]]」，但 patterns 主頁本身沒有做法（只在 :57 一格寫「CLAUDE.md 做偏好、Hooks 做邊界」），做法其實在 archive 和 trends。這個指路繞了一圈

## Q2. 依難度自動降階到便宜模型：社群走到哪、有沒有現成工具、風險、官方有沒有內建？

- **路徑：** index → community-tech-patterns（:60「模型使用策略」列）→ community-pattern-trends（趨勢四）→ entities/fable-5（查 46%／96% 出處）→ model-comparison（:135）→ official-community-gap（「想自己決定哪段用哪個模型」列）
- **跳數：** 走了 6 跳；最短 4 跳（index → patterns → trends → official-community-gap，patterns:143 有連結）
- **結果：拿到**：四個子題都有答案，但得拼兩頁，而且有兩處互相打架
- **拿到的答案原句：**
  - 走到哪／工具：community-pattern-trends.md:165「Workweave Router（6/27，HN 181）……嵌入式自動路由依請求難度選模型，無需手動規則」；community-tech-tools.md:222「實測成本降 40%+」
  - 怎麼分級：community-pattern-trends.md:183-188 Haiku／Sonnet／Opus 任務表，含「review migration SQL 安全性：Opus，不可降階」：可直接照抄進 CLAUDE.md
  - 風險：community-pattern-trends.md:192「黑盒路由……某些關鍵任務可能被靜默降階，你不知道為什麼結果不可靠。顯式規則路由更容易 debug」
  - 官方：official-community-gap.md:59「個人端有 `opusplan`：規劃時用 Opus、開始執行自動換 Sonnet……依成本或任務動態選模型的路由截至 2026-09-19 官方文件未見」
  - 補充：community-tech-patterns.md:910 hooks 強制後「改用較便宜的 Haiku 當 builder 也不再顯得冒險」：把 Q1 和 Q2 串起來的一句，很有用
- **卡住／誤導的原句：**
  - community-tech-tools.md:63 把 Workweave Router 放在症狀「不想被單一供應商綁死」底下。我要找的是「省錢／降階」，決策表裡沒有這個症狀，差點以為它是換供應商的工具
  - official-community-gap.md:187「社群工具……填補的是後者，官方目前無對應方向」和同頁 :59 的 opusplan「自動換 Sonnet」打架
  - community-pattern-trends.md:177「可直接在 Claude Code 現行設定中使用」：沒說怎麼設（哪個設定、哪個指令）
  - community-pattern-trends.md:190「全走 Opus ≈ $100；……≈ $18」沒寫用哪一代的價格、每次多少 token 算的，不敢拿來估

## Q3. 「跨 session 記憶」近三個月變了什麼、現在看哪頁？趨勢觀察和技術模式差在哪？

- **路徑：** index（:32「大型 codebase……記憶」）→ community-large-codebase-workflow（第 3 線）→ community-pattern-trends（趨勢九）→ official-community-gap（「新開一個 session 它就忘光」列＋⟨G-05⟩）；patterns:59 的「記憶與知識管理」列是順路看到的
- **跳數：** 最短 4 跳（實際也差不多）
- **結果：半拿到**：「現在該看哪頁」有答案（large-codebase-workflow 第 3 線），「三個月變了什麼」沒有任何一頁直接回答，得自己從三頁拼時間軸
- **拿到的答案原句：**
  - 現況：community-large-codebase-workflow.md:111「官方已給：auto memory……每個 session 載入前 200 行或 25KB；官方明說它是 context 不是強制設定」
  - 官方這三個月動了什麼：official-community-gap.md:171「#47023 已於 2026-08-17 CLOSED／COMPLETED，官方答四個 hook（PreCompact／PostCompact／SessionStart／SessionEnd）今天都有」；:107「SessionStart 可回傳 additionalContext 把記憶注回來」
  - 社群三個月的節點：community-pattern-trends.md:292-298（6/28 OKF → 7/22 CodeAlmanac → 8/21 OzBrain → 8/24 手動 Obsidian → 8/25 brain.md → 8/31 否決紀錄 → 9/6 gentle-ai／cpr）；:310 結論「要嘛把記憶外化成你自己能讀的格式，要嘛乾脆整套換成手動策展」
  - 要裝什麼：community-tech-tools.md:59「每開新 session 都要重講一遍 → brain.md」
- **卡住／誤導的原句：**
  - community-pattern-trends.md:310「社群過去 105 天」和 :300「跨 121 天」同一節自己打架
  - community-pattern-trends.md:316「跨 Session 記憶層……已於本次升格為趨勢九」：「本次」是哪次？頁頂日期是 09-19，看不出是這三個月內哪天升的
  - auto memory 什麼時候上線、這三個月有沒有變：四頁都沒寫日期，official-community-gap.md:169 只說「還有已知毛病（見 [[entities/claude-code]]）」
  - 同一件事有兩個狀態：community-tech-patterns.md:59「記憶與知識管理 ⚡ 活躍」vs community-pattern-trends.md:288「趨勢九 成形／📈 加溫中」

## Q4. Fast Context Task Router 已下架，本地小模型分流還能拿什麼做？

- **路徑：** index → community-pattern-trends（:166-167）→ community-tech-patterns（:1565-1571）→ community-tech-discussions（:582-588、:226）→ community-tech-tools（:63、:256）→ coding-workflow-guide（:287）
- **跳數：** 5 跳
- **結果：沒拿到**：頁面誠實說了「沒了」，卻沒給可以裝的替代；唯一點名的替代品 claudely 頁面自己也說找不到 repo
- **拿到的原句：**
  - community-pattern-trends.md:167「想法被後續模式繼承，但這個專案已不可取得，要實作得自己找替代品」：誠實，但到此為止
  - community-tech-discussions.md:226「規劃用 Claude Code、實作交給本地模型」混合工作流（MCP 分擔給本地 Qwen3.8-27B、XDA 報導）：最接近替代的**做法**，但只是現象，沒有可裝的東西或設定步驟
  - community-tech-tools.md:63「只想改用本地模型、不動主配置 → claudely」，同頁 :82「claudely 到 09-22 都找不到公開 repo」
- **卡住／誤導的原句：**
  - community-pattern-trends.md:179「本地小模型分流（如純程式碼探索工作）是另一條降本路徑」仍當作建議，但 coding-workflow-guide.md:287 寫「本地小模型分流省 50–60% context……本頁不再推薦（生態只驗證成本不驗證 context）」。兩頁結論相反，互不指路
  - community-tech-patterns.md:1570「下架爭議與機制本身的社群反思見 [[topics/community-tech-discussions]]」：過去只看到 :588「尚無共識」，沒有下一步
  - 相關的 magnitude（本地推論伺服器，patterns:626）、Dragoman（可路由到 Ollama，tools:248）其實都有，但沒有一頁把它們放在「Fast Context 沒了之後」這個脈絡下

---

## 分不出差別的兩頁

**community-pattern-trends（社群趨勢觀察）vs community-tech-patterns（社群技術模式）**

- 為什麼分不出：兩頁都按「類別」組織，類別名稱大量重疊（Hooks／多 agent／context／模型路由／記憶／規格驅動），各自還有一套成熟度詞彙：patterns 用 ✅成熟／⚡活躍／⏳新興（:76），trends 用「成形／醞釀」＋熱度箭頭（:320-328）。同一主題在兩頁的狀態不一樣（記憶：⚡ vs 成形）。兩頁也都有「怎麼做」的內容（trends 的啟示表 vs patterns 的「類別細節」）
- 讀到哪一句才弄懂：community-pattern-trends.md:43「從 community-tech-patterns 的具體模式中，萃取出宏觀趨勢……對現有設計的啟示」＋ community-tech-patterns.md:44「想知道哪個方向在加溫……見 community-pattern-trends」。到這裡才懂 **patterns 是逐則型錄（1710 行、按月份流水帳），trends 是給結論和做法的**
- 我的決定：**想要「我該怎麼改設定」→ trends；想要「某個工具／做法的原始證據」→ patterns**。但這個分法和兩頁的頁名、index 的鉤子（index:101 vs :103）都對不上：真正給我行動建議的，是頁名聽起來最「觀察」的那頁
- 第三頁也在搶：community-large-codebase-workflow 也是「每條線先給現在的答案」，記憶題它比 trends 更好用。三頁的分工從 index 看不出來

## 雷達還是百科（各頁一句）

| 頁 | 判定 | 一句 |
|---|---|---|
| index | 地圖 | 路由表好用，但「社群」四頁的鉤子分不出誰給答案 |
| community-tech-patterns | 雷達（外面包了一層百科） | 頂部 21 類概覽像百科，正文 1500 行是按月流水帳，找做法得靠 Grep |
| community-tech-patterns-archive | 百科（封存） | Q1 最關鍵的「搬去 hook」核心條目住在封存頁，冷讀者不會想到要來這裡 |
| coding-workflow-guide | 百科 | 官方層級表和「什麼徵狀往哪層搬」是全庫最可執行的答案 |
| community-tech-tools | 百科（決策表）＋雷達（目錄） | 決策表好用，但症狀分類缺「想省錢降階」 |
| community-pattern-trends | 頁名是雷達，實際是百科 | 熱度箭頭是雷達，但真正值錢的是「對現有設計的啟示」表，那是百科 |
| official-community-gap | 百科（上表）＋雷達（下方沿革） | 「官方補了沒」表一格一答很好，下方技術彙整的舊敘述和上表打架 |
| community-large-codebase-workflow | 百科 | 「現在的答案」先給官方零件，記憶題最好的入口 |
| community-tech-discussions | 雷達 | 爭論狀態表清楚，但對「我該怎麼做」幫助小 |

## 內部用語外洩表

| 檔名:行號 | 原句 | 困惑 |
|---|---|---|
| community-tech-patterns.md:160 | ⟨Q-nn⟩ 標的是這一則還沒查實的地方 | 這套編號是給誰看的？我只想知道能不能信 |
| community-tech-patterns.md:150 | 見下方懸置細節 ⟨Q-07⟩ 已查證：未恢復 | 「懸置細節」＋編號＋「已查證」三層，讀者語言應是「官方沒恢復（查證日 09-20）」 |
| community-tech-patterns.md:177 | **主線：** — | 「主線」是什麼？破折號代表沒有還是未填？ |
| community-tech-patterns.md:859 | 非大型 codebase 特有痛點，暫不歸入主線 … 四條主線 | 這是編輯決策，不是給讀者的資訊 |
| community-tech-patterns.md:1010 | 無「週熱門」標記，score 不可信；……依內容判斷收錄 | 收錄理由寫在正文，讀者不需要知道收錄規則 |
| community-tech-patterns.md:1196 | 依 dev.to 內容判斷原則收錄 | 同上 |
| community-pattern-trends.md:326 | 至少 1 條代表模式達 A/B 層證據 | A 層、B 層沒定義（:300 也用「B 層證據」） |
| coding-workflow-guide.md:390 | `[已補：庫內證據]`（另 :234 `[已深查]`、:481 `[社群面待補]`） | 標題上的維護狀態標籤，讀者看不懂「庫內」指什麼 |
| official-community-gap.md:59 | ⟨G-13⟩ | 又一套編號（G-），和 Q- 是不是同一套？ |
| community-tech-discussions.md:587 | 07-12～08-07 news 查無跟進 | 「news」指的是本站日報，外人以為是新聞媒體 |

## 撐不起的句子

1. **Hook 攔截的 exit code 各說各話**：community-pattern-trends.md:85「exit 1 = 硬攔截」↔ community-tech-patterns-archive.md:279「non-zero exit code」↔ archive:526「四種 exit code：Block／Allow／Modify／Error」↔ coding-workflow-guide.md:210「回 deny」。沒有一句附官方出處；依官方 hooks 文件（讀者既有知識，未在庫內查到），exit 2 才阻擋，trends:85 很可能是錯的
2. **「CLAUDE.md 管理已定案」**：community-tech-patterns.md:1655「已經定案的四類（…CLAUDE.md 管理…）……近三個月沒出現反對意見」↔ community-tech-discussions.md:54「CLAUDE.md 與提示詞該寫多少｜還在吵｜2026-08-28」
3. **官方到底有沒有 CLAUDE.md 對應**：official-community-gap.md:44「13 個痛點裡，1 個官方目前沒有任何對應」↔ 同頁 :142「CLAUDE.md 規則失效｜無｜❌」、:144「AI 輔助開發副作用｜❌」（至少 3 個 ❌）；gap:80「官方對複雜 CLAUDE.md 幾乎沒有文件指引」↔ coding-workflow-guide.md:182-190、:514（官方 features-overview 有徵狀判準、官方明列「過度指定的 CLAUDE.md」失敗模式）
4. **官方模型路由**：official-community-gap.md:187「官方目前無對應方向」↔ 同頁 :59「opusplan……開始執行自動換 Sonnet」；community-tech-patterns.md:145「強拆分者勝過強執行者……已補」
5. **趨勢頁自己的數字**：community-pattern-trends.md:179「本頁 5 條趨勢」↔ 實際有九條（:288 趨勢九）↔ index.md:103「7 條成形趨勢」；trends:310「105 天」↔ :300「121 天」；trends:308「四種公開實作」↔ index.md:105「六種公開實作」

## 最想改三件（讀者立場）

1. **修正並統一 hook exit code**：trends:85 改成官方說法並附出處（哪個 exit code 阻擋、stderr 會不會回饋給模型、PreToolUse 用 JSON `deny` 的寫法），archive:279／:526 指向同一處。這是四題裡唯一一個照著做會出事的答案
2. **給「社群」四頁一句話分工，寫在 index 和各頁頂**：patterns＝原始證據型錄、trends＝該怎麼改設定、large-codebase＝四面牆的現在答案、tools＝該裝哪個。同時統一成熟度詞彙（⚡／成形二選一），同一主題不要在兩頁有兩個狀態
3. **「沒了」要附下一步，兩頁結論不要相反**：Fast Context 那條直接指向 discussions:226 的混合工作流和 Dragoman（可路由到 Ollama），並和 coding-workflow-guide:287「不再推薦」對齊；決策表加「想依難度降階省錢」症狀，把 Workweave＋opusplan＋trends 分級表放在同一格
