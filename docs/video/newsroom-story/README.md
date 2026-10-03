# 小編輯部介紹動畫（newsroom-story）

`newsroom-story.html`：約 2 分半、1920×1080 的單檔 HTML 動畫，雙擊即可播放（空白鍵播放／暫停，左右鍵跳 5 秒，下方章節鈕可跳幕）。主角是本機 mod `newsroom-pets` 的同一批角色：像素由 `.claude/mods/newsroom-pets/hooks/lib.ts`、`actions.ts` 算出，mod 改了角色或道具，重跑產生器就跟著變。

重新產生：

```
node --experimental-strip-types docs/video/newsroom-story/make-story.mts
```

劇本與場景在 `story-runtime.js`。舊的資料流動畫（`docs/video/daily-archive-motion.html`）保留不動。

## 字級

畫布 1920 寬：字幕標題 52px、副標 36px、標籤與名牌 ≥30px、片名 96px。縮到 1280 寬播放時最小字約 20px。產出後跑過自動檢查（攔截每次寫字、每 0.5 秒取樣）：最小字 30px、沒有文字超出畫布或擠進字幕帶（唯一例外是第 5 幕派工單由右側畫外滑入，屬刻意進場）。

## 分鏡與出處

| 幕 | 時間 | 劇情 | 規則出處 |
|---|---|---|---|
| 開場 | 0:00 | 全員睡覺，鬧鐘響 | — |
| 01 抓料 | 0:08 | 三路來源→小幫手印日報；延遲 26–30 小時是設計 | `CLAUDE.md`「本站目標」、`.claude/skills/news-gather`、`news-digest` |
| 02 派工 | 0:20 | 主編戴眼鏡讀日報、吹哨，九類記者點名 | `.claude/skills/wiki-ingest/SKILL.md` 步驟 3、`references/dispatch.md` |
| 03 寫 wiki | 0:35 | 記者寫負責頁，主編寫日誌、整理索引 | `wiki/CLAUDE.md`（每個事實一個家、log 只能 append） |
| 04 查證① | 0:50 | 記者電話被鎖（無 web 工具），貼「⚠️ 需主編查證」 | `.claude/reporter-rules/commercial/daily.md` 等「無 web 工具」；`guard_roles.py` H7 |
| 04 查證② | 1:00 | ❓ 懸置標記；兩個探針命中日報→蓋「訊」；逾期分 Lane A／B | `.claude/reporter-rules/page-templates.md` 懸置標記；`shared.md` 待查證命中處置；`wiki-lint-sweeps/references/sweeps.md` 5c |
| 04 查證③ | 1:11 | 主編照優先序查一手來源：事實／🔎 查無官方／媒體稱 | `sweeps.md` 5c 查證優先序 |
| 04 查證④ | 1:23 | 每週擲骰抽題，每題帶回證據行 | `wiki-lint-reader-acceptance/SKILL.md` 7b |
| 05 退案① | 1:28 | 複核記者翻排除區，「誤排除」改派；一則最多回退一次 | `.claude/agents/wiki-reporter-classify-review.md`；`wiki-ingest/SKILL.md` 3b |
| 05 退案② | 1:37 | 規則檔擋住派工單：派工與規則牴觸 | `.claude/reporter-rules/shared.md`「規則檔優先於派工訊息」 |
| 05 退案③ | 1:44 | 主編抽驗回報，不符蓋「退回補做」，重做通過 | `wiki-lint-reporters/SKILL.md` 收報核對 |
| 05 退案④ | 1:52 | 內容閘紅：修復迴圈至多 2 輪、hook 擋改閘；轉綠才 commit，否則停泊分支 | `.claude/skills/web-publish/SKILL.md` Step 3／4；`gate_wiki_commit.py`、`guard_roles.py` H6 |
| 06 上線 | 2:04 | 測試全綠、建網站、一次 push；雲端每天三班 | `web-publish/SKILL.md` Step 5；`docs/cloud-runbooks/triggers/daily-news-pipeline-cloud.json` |
| 收尾 | 2:16 | 散會，主編睡回去 | — |
