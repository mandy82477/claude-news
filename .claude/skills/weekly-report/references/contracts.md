# 週報機械契約字串（勿改；新增時登記 `.claude/review-registry.json`）`[加入: 2026-09-04]`

**script 會 grep 的字串只住這張表**，`.claude/skills/weekly-report/` 其餘檔案的條文引用時指回本表、不另抄一份。改任何一格必須同步右欄消費端（`check_rules.py` 依 registry 看守）。

| 契約字串 | 消費端 | 改壞的後果 |
|---|---|---|
| 頭條標題 `## 一、頭條敘事：<一句話>`（`頭條敘事` 四字不可省——`build_web.py` 以 `"頭條" in title` 認節；冒號後為標題本體） | `check_weekly_ledger.py` HEADLINE_DECK_RE（硬擋，W36 起）、`build_web.py` 節切分、`app.js` `weeklyHeadlineDeck()` 渲染副標 | 缺冒號後半 → 硬擋；`頭條敘事` 被拿掉 → 整節不進 JSON |
| ~~`> **本週一句話**：`~~（**2026-09-06 退場**，併入上一列） | `build_web.py` WEEKLY_LEDE_RE 仍在（W30–W34 已凍結期數要渲染） | 新期不再寫；程式不刪，刪了舊期副標會消失 |
| 節標題 `## 一、…`／`## 四、本週數字`（編號＋字面） | `check_weekly_ledger.py` HEADLINE_SECTION_RE、NUMBERS_HEADING_RE | 頭條十條規則與數字檢查**靜默跳過**（不報錯） |
| 討論段子標題 `### 本週版本`／`### 討論綜述`／`### 深挖：主題` | `build_web.py` 討論子段切分（h3）、`check_weekly_ledger.py` check_deepdive | versionNote／roundup／deepDive 變 None，內容被併進整段 body |
| 新開表頭 `\| 類型 \| 預告 \| 判準 \|` | `build_web.py` WEEKLY_FORECAST_HEADER_RE、`check_weekly_ledger.py` FORECAST_HEADER_RE | 新開表整張不進 JSON，條數與查證線索檢查全部落空 |
| 新開小標 `### 下週值得關注：新開 N 條` | `check_weekly_ledger.py` 導言檢查（`build_web` 不認此小標） | 導言缺漏檢查失效（⚠️ 級） |
| 回收小標 `### 上週的線怎麼了（YYYY-Wnn）`（須逐字等於實際上一期檔名）＋表頭 `\| 上週預告 \| 判準 \| 本週結果 \|` | `build_web.py` WEEKLY_RECAP_HEADING_RE／WEEKLY_RECAP_HEADER_RE、`check_weekly_ledger.py` RECAP_HEADING_RE／RECAP_HEADER_RE、`scan_open_forecasts.py` RECAP_HEADER_RE（表頭） | 回收表消失／帳目對不上硬擋 |
| 回收結果欄狀態符號 ✅❌⏰（結案）／⏳🟡（續盯，含「續盯」二字） | `check_weekly_ledger.py` CLOSED_MARKS／OPEN_MARKS | 結案與殭屍規則判錯，未結案條目靜默漏收 |
| 判準欄尾 `｜查證：關鍵字1、關鍵字2` | `scan_open_forecasts.py` PROBE_RE、`check_weekly_ledger.py` 查證線索硬擋 | 預告失去日報偵測，且每條新開判準被判缺線索而報錯 |
| 新開條數 3–6 | `check_weekly_ledger.py` MIN_FORECASTS／MAX_FORECASTS | 規格與程式各說一套，硬擋門檻不等於規格 |
| 檔尾 `---` 分隔線＋下一行 `**素材涵蓋窗**` 起頭、位於全檔最末 | `build_web.py` WEEKLY_FOOTER_RE | 檔尾不上站並污染「本週數字」 |
| 檔尾數字 `- **值**——說明`（全形破折號條列） | `build_web.py` WEEKLY_STAT_RE、`check_weekly_ledger.py` STAT_BULLET_RE | 數字節網站空殼 |
