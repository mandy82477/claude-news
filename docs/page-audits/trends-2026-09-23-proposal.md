# 第 17 波設計提案：topics/community-pattern-trends

使命句（主 session 代判，健檢卡 A）：**社群做法往哪幾個方向收斂、每個方向怎麼走到今天、你現有設計可以回頭檢查什麼。**
逐字稿 `trends-2026-09-23-draft.md`，逐行去向 `trends-2026-09-23-proposal-map.md`。官方事實只取 `trends-2026-09-23-verified.md` 已錨的句子；行號一律用檔案原始行號（健檢卡口徑）。scratchpad 產物：`build.py`（套稿）、`verify.py`（閘＋頁內契約）、`mkmap.py`（去向表覆蓋檢查）、`rungate.py`（對 wiki 副本跑閘的 `main()`）。

## 1. 推薦案（一個）

**演進時間軸不動，動它上下兩層：標題換成一把只量「方向」的尺加上「最近一次動靜」日期，🔥 照圖例重打、其餘標「估」；每段啟示改成「先看官方給了什麼、再回頭檢查什麼」，跟 LCW 重疊的指過去；判準、淡出、撈料條文搬回 weekly.md 並修到能跑。**

根因（健檢卡第 8 節、冷讀者 CR:80／:92）：讀者靠的是啟示段，但啟示段唯一能照做的一句（L85）寫反了，四／八／九零官方句，三處建議鄰居已撤回；標題層兩把尺各說各話，熱度層 1／13 對得上自己的圖例，淡出條文從沒跑過。九件事一起做：

1. **兩把尺（代判：明寫各量什麼）**：九條標題的狀態標統一為 `方向已收斂`（原「成形」「醞釀 → 成形」「新升格」三種寫法都已宣稱過門檻，L240／L279／L300），`## 成形趨勢` 改名 `## 已收斂的方向`；摘要新 L49 一句：「方向已收斂」量做法有沒有收斂成方向，採用量看 patterns 模式概覽表的成熟度，兩者可以不同（例：規格驅動已收斂、採用仍屬新興）。趨勢七／八因此不再與 patterns L64／L74 互斥。條文住 weekly.md B-1 首段（「本頁不另判採用量、不寫 ✅⚡⏳」）。
2. **熱度詞換成日期**：六種熱度詞（▬ 穩定延燒／成熟穩定／高檔穩定、📈 加溫中、↗ 醞釀中／新升格）沒有一種有機械定義（weekly.md:145 只有「📈 → stable」），換成「最近一次動靜 YYYY-MM-DD」＝該條最後節點日期（9/9 條與節點吻合，`verify.py` 實測）。趨勢五「醞釀 → 成形＋↗ 醞釀中」同標題兩狀態（健檢卡 7(2)#1）一併消失。
3. **🔥：照 L47 重打＋標判定日**（不選「改成收錄估計」）：14 個帶 HN 分數的節點依分數分級（Adrafinil 124、Merge Queue 42、machine0 83、Workweave 216 取 verified §二 L19–L22 即時值；其餘 10 個用頁面原記分數；新 Skillsync 59），判定日 2026-09-23；57 個無 HN 分數的節點一律標「（估）」。Fable 5 由 🔥🔥🔥🔥 降 🔥🔥🔥（估）（單平台轉載，健檢卡 7(1)）；ANMA HN 3 由 🔥🔥 降 🔥。
4. **exit code 照官方改**：L85 → 「Hook 怎麼擋」：exit 2 擋、exit 1 只算非阻擋錯誤、或 stdout 回 JSON `permissionDecision: "deny"`，直連官方 hooks 文件並指 guide（verified §一-1、§三 Q1）；L66、L68 同步（Stop hook exit 2「阻止停下、繼續對話」，verified §二 L18）；archive L279／L526 行尾各加註一句（不刪字）。庫內無家 → 轉知 C-1。
5. **官方對應一句**：趨勢四（`opusplan`＋`CLAUDE_CODE_SUBAGENT_MODEL`＋官方無自動難度路由，verified §一-3；直連 model-config、指 OCG；轉知 C-2）、趨勢八（遠端控制已確認可用，08-17 關閉 #29006，verified §一-5；指 claude-code）、趨勢九（auto memory 前 200 行／25KB，verified §三 Q3；指 LCW）。另依 B-1 第 5 步同一條規則，趨勢六轉述 OCG L60 的 Agent view 一句（庫內既有，不是新官方句）。L170 #56913 改 closed not_planned 09-15（verified §一-4）；L190「$100／$18」刪（verified §二 L25：無 token 假設），牌價的家是 `entities/pricing` L119／L122。
6. **淡出條文修到能跑，並當場跑一次**：B-1 第 4 步——最後節點逾 30 天 → 先看對照表類別在 patterns 模式概覽表的「最後動態」，30 天內有就打開那幾則，推進本方向的補進（屬漏收），不推進的在 `%%` 記一句；仍逾 30 天才標「↘ 淡出」。實跑：**趨勢七**補 spec-kit（09-12）後 11 天，不淡出；**趨勢四** patterns「模型使用策略」09-06 的 MaskShift（工具呼叫相容層，patterns L564）、magnitude（本地推論後端，L627）不推進路由 → 標「↘ 淡出・最近一次動靜 2026-08-14」，理由記頁尾 `%%`。趨勢一 07-02→08-15 那段 44 天空窗的舊「研判」段移進 `%%`。
7. **09-19 漏收補四則，不是五則**：spec-kit→趨勢七、hcom→趨勢二、Skillsync＋hister→趨勢九。**agent-channels 不補**：patterns 本體沒有它的節點，只在概覽表 L65 與類別細節 L86 列名，最早見 `news/2026-06-27.md:64`（附帶提及），不是那一窗漏收的料；理由記頁尾 `%%`。
8. **guide L287 撤回的三條**：讀取上限（L130）、已否決方案索引（L133）、本地小模型分流（L166）留在演進；啟示段各拿掉，趨勢三、趨勢四各一句分界指 guide。Fast Context 下架子條目（L167）補「接下來能拿什麼」：`CLAUDE_CODE_SUBAGENT_MODEL`（verified §三 Q4）、discussions L226 混合做法、tools L248 Dragoman。
9. **與 LCW 重疊的四段啟示（二／三／五／九）只留回頭檢查**，可執行零件與官方句一句指 LCW（連頁不連錨）。趨勢二「失敗場景」併入啟示問句、「怎麼修」移出（家：LCW L59／L61／L138）；趨勢三反模式表（2 欄鍵值，違反 `page-templates.md:119`）移出、直覺句併入；趨勢五「為什麼自我審查失效」併入啟示、Verity 延伸併入 L201 節點。表留三張（趨勢一 6×3、四 4×3、五 3×3）。

另：判準 L320–L328 降為一句讀者語言（`## 怎樣算「方向已收斂」`）；補 `## 目前結論`（你的選項／接下來看什麼，原則 4）；分工句三處同口徑——本頁摘要新 L47、patterns L44、discussions L43，index L103 主編自理；callout 改三條讀者語言。

## 2. 不選的方向（各一行）

- **狀態標改引用 patterns 成熟度**：九條對上 13 列、趨勢一／二／三／七各對兩列（健檢卡第 3 節），一條趨勢會同時掛 ✅ 與 ⏳；趨勢六根本沒有專屬列。
- **L47 改成「收錄當時估計」**：14 個節點頁面上寫著 HN 分數，圖例不給分級等於留著 13 筆自相矛盾的標記。
- **保留熱度詞、只補淡出**：熱度詞無機械定義，每週都要人判；日期是從條列算得出的事實。
- **淡出的趨勢移到新節「已淡出」**：LCW L74「趨勢六」、llm-wiki L69「趨勢九」按編號引用，搬動會斷；淡出只是標記，整條移除屬使用者裁決。
- **趨勢四因官方 09-15 標 #56913 不做而不淡出**：淡出量的是社群做法有沒有再進來，官方動作寫在官方句與「接下來看什麼」。
- **把 09-20～09-22 的 Chief of Staff、aoci-code、Foremerge、pstack-claude 也補進**：下次週更的正常料，混進來讓 callout 同時講兩件事（第 16 波同判）。
- **四段重疊啟示整段刪、只留指路**：刪掉「回頭檢查」就沒有使命句後半；冷讀者判啟示是本頁最值錢的一層（CR:92）。
- **趨勢七補官方句**：庫內沒有規格驅動的官方家，B-1 第 5 步只轉述庫內已寫的，不另找官方。

## 3. 可行性前提（一行）

九條 `### 趨勢N` 的編號與順序不動（LCW L74、llm-wiki L69 按編號引用）；全庫無 `[[topics/community-pattern-trends#…]]` 錨點、`scripts/`／`web_reader/assets/`／`src/tests/` 無人 grep 本頁節名（`page-lifecycle.md:16` 查法實跑）、`review-registry.json` 對本頁只有 `bare_name_search_dirs`（L91）——節名與標題可改；weekly.md 的「每日 ingest 不」（`review-registry.json:250–258`）在 L3，B-1 不碰。

## 4. 新骨架

| 節 | 一句用途 | 行數（原→新） |
|---|---|---|
| 標頭＋callout | 三條：exit 2 更正、三條官方對應、四則新做法 | 12 → 14（L27–L38 → L27–L40） |
| `## 摘要` | delta-first 一段＋分工兩條＋兩把尺＋最近一次動靜＋🔥 圖例 | 10 → 12 |
| 趨勢一 | 演進＋代表模式＋啟示＋表＋「Hook 怎麼擋」 | 36 → 34 |
| 趨勢二 | ＋hcom；啟示三問、指 LCW；失敗場景／怎麼修收掉 | 35 → 27 |
| 趨勢三 | 啟示回頭檢查＋分界句；反模式表移出 | 36 → 29 |
| 趨勢四 | ↘ 淡出；官方句首；表留；$100 刪；黑盒補模型釘選 | 36 → 34 |
| 趨勢五 | 啟示兩問＋表；自審失效／Verity 併入 | 33 → 28 |
| 趨勢六 | 官方句首（Agent view）；計數段移出 | 24 → 21 |
| 趨勢七 | ＋spec-kit（節點＋代表模式） | 17 → 19 |
| 趨勢八 | 官方句首（遠端控制）；計數段移出 | 18 → 16 |
| 趨勢九 | ＋Skillsync、hister；官方句首（auto memory）；計數段移出 | 26 → 26 |
| 還在醞釀／目前結論／怎樣算 | 「目前沒有」／選項＋接下來看什麼／一句門檻 | 18 → 19 |
| 相關實體 | ＋LCW、guide、OCG、tools；`%%` 水位與健檢備忘 | 7 → 13 |

**338 → 322 行**（scratchpad 實測）。

## 5. 誰看守什麼（附行號；沒有腳本的寫「無看守」）

| 契約 | 看守 |
|---|---|
| 條列 ≤200、表格格 ≤120 字元 | **有**：`check_cell_limits.py:50–51`（上限）、`:176–197`（`scan`）、`:266`／`:289`（FAIL、exit 1）；本頁改後 0 命中 |
| 維運禁詞（轉知、記者、門檻、callout 整理語…） | **有**：`check_reader_language.py:51`（TERMS）、`:88`（門檻）、`:162`（callout 整理語）、`:276`（scan） |
| 懸置標記與舊字樣不增加 | **有**：`pending_markers.py:46–48`（SHORT_RE）、`:60–61`（LEGACY_RE）；`check_pending_markers.py:313`（`check`） |
| 規則檔不得有裸露的那個檔名 | **有**：`check_rules.py:102–157`；B-1 對照表第一列因此不寫出該類別全名（實測寫出即紅，第 6 節） |
| wikilink 目標存在 | **有**：`build_web.py`（實作單第 10 步）；新增 13 個連結目標 scratchpad 逐一 `-f` 驗過 |
| 標題日期＝最後節點日期、HN 分級、無 HN 必標「估」、淡出檢查 | **無看守**（本波 `verify.py` 自驗 9/9、14/14、57/57；不進 `run_tests.py`） |
| 「節點」「本輪」「本線」「GitHub Search」不上正文 | **無看守**：不在 TERMS（第 16 波已記同一缺口），B-1 第 2、8 步只是條文 |
| 啟示第一句先寫官方、四段指 LCW | **無看守** |

## 6. 閘：我自己跑過的結果

**現行基線（動手前，對象頁）**：`check_cell_limits` 基線內 5 筆（L98、L99、L203、L238、L259）、無新增；`check_reader_language` 0；`check_pending_markers` 119 筆（基線 106）、舊字樣 40（基線 42）；`check_rules` 全綠。

**draft 套進 scratchpad wiki 副本後**（wiki 本體未動；A-1 round-trip 與副本逐字相同）：

| 閘 | 改後 | 說明 |
|---|---|---|
| 本頁 `check_cell_limits.main()` | **0 筆** | 5 筆基線內的全改到 ≤200（最長 198）；5 個舊指紋成孤兒，不轉紅 |
| 本頁 `check_reader_language.main()` | **0 筆** | |
| 鄰居 `--page topics/community-tech`／`topics/community-` | 無新增 | 基線內 120／4 筆與改前同 |
| `check_pending_markers.check()` | 119（基線 106）、舊字樣 40（基線 42） | 本頁改前改後皆 0 |
| `check_rules.py`（repo 副本，新 weekly.md＋新頁） | 失敗集合與改前副本相同 | 副本缺 `web_reader`／`news`，改前改後同為 7 行環境性失敗；首版對照表寫出規則檔名 → 多出「檢查 1 裸露引用」，已改寫後消失 |
| 頁內契約（`verify.py`） | 標題 9、日期吻合 9/9、HN 分級 14/14、估 57、HN 與估重疊 0 | |

**驗紅**：`verify.py --inject-red` 把 hcom 節點加長到 263 字元、在「還在醞釀的方向」寫進「已轉知功能記者」→ cell 閘 `NEW 104 list_item 263`：紅在 `check_cell_limits.py:193`（`len(visible) > LIST_LIMIT`）→ `:194` append → `split_hits` 不在基線 → `main()` `:266` 印 FAIL、`:289` exit 1；reader 閘命中「記者」（`check_reader_language.py:61`）與「轉知」（`:100`）兩筆 → `:296` 比對 → `:380` FAIL、`:400` exit 1。

最後一行（原樣抄，三支閘對現行 wiki，依序 `check_cell_limits --page topics/community-pattern-trends` → `check_reader_language --page …` → `check_pending_markers`；`check_rules` 另跑）：
```
OK: 字元上限機械閘 — 無新增超限
OK: 讀者語言閘 — 無新增命中
狀態：✅ 懸置標記語法檢查通過
狀態：✅ 全部確定性檢查通過
```

## 7. 規則檔與轉知

**進規則檔（draft B-1，weekly.md L135–L157 整段換，23 → 34 行）**：門檻第二條改「最早與最晚節點相隔 ≥14 天」（取頁面 L325 嚴格版）；趨勢↔patterns 類別對照表；撈料改 patterns 關係行＋`%%`「週更已收至」水位（前 3 天起算）；節點格式改成頁面實際的條列＋四級 🔥＋「（估）」；標題格式；淡出檢查；啟示先官方、四段指 LCW、撤回的只留演進；表的存在條件與改寫時機；演進 >12 節點回報；callout／目前結論；水位回寫。09-19 漏收的根因：舊第 1 步讀「近 14 天 news」而不是 patterns 節點、也沒有水位（推論——log 無那一輪的撈料紀錄可證）。

**轉知 3 筆**（完整參數見 draft C 區）：C-1 功能／guide L210 缺 exit code 語意；C-2 功能／OCG L59 缺 `CLAUDE_CODE_SUBAGENT_MODEL`、與 L187 互斥（CR:38）；C-3 模型／`entities/opus-5`：verified §四 提到官方文件寫預設模型「Opus 5.5」。guide L287 前兩條已由 H-c63724 在案，不重開。

**只記 log、同維護者下次處理**：tools L63 症狀歸類（CR:37）、patterns L1653 同題兩家、patterns L1655 vs discussions L54、pizza-bot／TokenEater 是否屬趨勢六。**主編自理**：index L103 新句（91 字元）、overview L118／L119 過期、Fable 5 日期 7/14 vs 07-08。

## 8. 仍需補查（本案沒有它也能上）

1. 10 個頁面原記的 HN 分數（L135、L204、L235–L237、L257、L275、L293、L294 等）未對即時值（健檢卡第 6 節「需查」）；分級以原記分數為準，判定日寫 2026-09-23。
2. hister 的「HN Repo Bridge 668 分」不確定是不是 HN 分數，本案當估計（🔥🔥🔥（估））。
3. Fast Context Task Router 下架原因（L167）仍是頁面自記 09-13 複查，未對一手。
4. 「節點／本輪」禁詞與四項頁內契約都無看守；最小方案是把前者加進 `check_reader_language.py` TERMS 走存量基線、後者寫成 `run_tests.py` 一支頁面契約測試——改 script 屬另一波。
