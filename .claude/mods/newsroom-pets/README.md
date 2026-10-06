# newsroom-pets（本機 mod）

prompt 上方的提示列裡住著一間小編輯部：主編（主 session）與記者（先依 agent 類型 `wiki-reporter-<slug>` 認、認不出再看派工 prompt 開頭句的子 agent）每做一種 wiki 操作，就做對應的彩色像素小動作。只觀察、不干預——`agent.spawn` 與 `tool.call` 一律回傳 `next(e)` 的結果。只在 CLAUDE_NEWS 樹上作用。

## 角色與帽子（住 `hooks/lib.ts` 的 CAST 與 HATS）

每個角色寬 10 格（2 列帽子＋身體），右邊 8 格是道具區，共 18×8 像素：終端機畫成 4 行半格方塊字，桌面版等沒有等寬字格的介面畫成一張 SVG（方塊字在那裡會一列列錯開）。

| 角色 | 帽子 |
|---|---|
| 🖋️ 主編 | 深色紳士帽 |
| 🛠️ 功能記者 | 黃色工地安全帽 |
| 🤖 模型記者 | 機器人天線 |
| 💼 商業記者 | 高禮帽 |
| 🏛️ 安全政策記者 | 警帽＋金徽章 |
| 🌐 社群記者 | 反戴棒球帽 |
| 👤 人物記者 | 報童帽＋記者證 |
| 💰 投資分析記者 | 會計遮陽帽 |
| 📓 開發實務記者 | 毛帽＋紅毛球 |
| 🔍 分類複核記者 | 偵探帽 |
| 🧰 小幫手（不是記者類型、prompt 也沒有範本開頭句的子 agent） | 頭帶 |

## 動作對照（判斷邏輯住 `hooks/actions.ts`）

| 動作 | 名牌下方 | 什麼時候 |
|---|---|---|
| 打字 | ✎ 檔名 | Edit／Write wiki 頁 |
| 寫日誌 | 寫日誌 log.md | Edit `wiki/log.md` |
| 整理書架 | 整理書架 index.md | Edit `wiki/index.md` |
| 雷達掃描 | 雷達掃描 feature-radar | Edit `wiki/feature-radar.md` |
| 印報 | 印報 … | Write `news/*.md`、跑 `build_web.py`／`news_aggregator` 等 |
| 翻閱（戴眼鏡） | 翻閱 檔名 | Read |
| 搜尋（戴眼鏡） | 搜尋 … | Grep／Glob／`wiki_search.py` |
| 打電話查證 | 打電話查證 網域 | WebFetch／WebSearch |
| 吹哨派工 | 派工 … | 呼叫 Agent |
| 檢查打勾 | 檢查中 腳本 | `run_tests.py`／`ingest_gate.py`／`check_*.py`／`gate_web_build.py` |
| 全綠比讚 | 全綠 腳本 | 檢查腳本輸出看得出綠燈 |
| 閘紅冒汗 | 閘紅 腳本 | 檢查腳本輸出看得出紅燈 |
| 被擋冒汗 | 被擋了 … | 任何呼叫被 hook 擋下或出錯 |
| 蓋章 | 蓋章 git commit | `git commit` |
| 射紙飛機 | 送上線 git push | `git push` |
| 掃地 | 掃地 … | `lint_health.py` 等 lint |
| 忙 | 忙 指令 | 其他 shell 指令 |
| 想事情（2 行、靠右） | 主編 … | Claude 在工作但沒有角色在台上 |
| 睡覺（2 行、靠右） | 主編 zZ | 平常 |

結束後停留 3.5 秒；同時在台上的角色並排，放不下顯示「…還有 N 位」。提示列被收合（Ctrl+X Ctrl+A 或 `[-]`）時 mod 看不到也無法展開，再按一次即可。

## Demo

`node --experimental-strip-types demo/make-gallery.mts` 產出 `demo/gallery.html`：全部角色帽子與動作道具的圖鑑。

`node --experimental-strip-types demo/make-demo.mts` 用本 mod 實際的 `actions.ts` 模擬一輪 `/news-pipeline`，產出 `demo/pipeline-demo.html`（雙擊開啟）。

## 驗證

`claude plugin test`（本目錄）；`python scripts/run_tests.py` 的 `check_mods.py` 會一起跑。mod 的遠端開關（`tengu_plugin_hooks_modules`）是關的時候，plugin test 跑不起來，閘會印 WARN 跳過。
