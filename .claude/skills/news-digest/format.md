# 日報（`news/YYYY-MM-DD.md`）格式契約

`.claude/skills/news-digest/SKILL.md`（Step 1b）的格式單一來源。選材判準不在本檔，見 `.claude/skills/news-digest/selection.md`。

## 機械契約字串（勿改；新增時登記 `.claude/review-registry.json`）`[加入: 2026-09-04]`

**script 會 grep 的字串只住這張表**，下方規則引用時指回本表、不另抄。改任何一格必須同步右欄消費端。

| 契約字串／形狀 | 消費端 | 改壞的後果 |
|---|---|---|
| 區塊標題 emoji（📌⭐🔧💰📰💬🧭📡） | `build_web.py` SECTION_EMOJI → JSON key（`app.js` 消費的是 key，不是 emoji） | 該區塊整段不進網站，且被吞進前一區的 body |
| 標頭 `**日期：** … \| **來源：** X/10 \| **文章數：** N \| **更新時間：** …` | `build_web.py` header_re／gen_re／src_count_re | 日期／文章數／來源比全部落空（`test_digest_contract.py` 會擋） |
| 聚焦行 `- **[標籤]** 說明（[來源名](url)）` | `build_web.py` FOCUS_RE／FOCUS_INLINE_LINK_RE／FOCUS_INLINE_GROUP_RE、`app.js` focus 渲染 | 裸 markdown 上站、badge 全站消失 |
| 條目三行式：`**[標題](url)**`＋說明＋`` `來源` · MM/DD HH:MM UTC``（討論區末加 `情緒：`） | `build_web.py` STORY_RE／SOURCE_RE、3a 自檢 | 條目解析不到，整則消失 |
| 🧭 行 `- **[標題](url)** — 說明（→ 專頁名）` | `build_web.py` TOPIC_RADAR_RE | 雷達區不進網站 |
| 📡 表 `\| 來源 \| ✅/❌ \| 條數 \|` | `build_web.py` SOURCE_TABLE_RE、3b 自檢、lint 6e | 來源健康檢查斷炊 |
| 聚焦區塊錨點 `### 📌 今日聚焦`（含 `###` 層級）＋聚焦條列必以 `- **[` 起頭（連字號 6g 必要） | wiki-lint 6g 分子分母 awk／grep、`build_web.py` FOCUS_RE | 覆蓋率誤報暴跌或灌大分母 |

---

## 骨架（照抄的部分）

以 `#`／`###`／表格開頭的行是要照抄的骨架；各區塊要收什麼、怎麼挑，見 `.claude/skills/news-digest/selection.md`。**六個正文區塊 ＋ 選配的專頁雷達區塊，無內容則省略。**

```
# Claude Code & Anthropic 每日新聞摘要

**日期：** TARGET_DATE | **來源：** X/10 | **文章數：** N | **更新時間：** YYYY-MM-DD HH:MM UTC

---

### 📌 今日聚焦

### ⭐ 重點話題

### 🔧 技術更新

### 💰 付費方案動態

### 📰 媒體報導

### 💬 技術熱度討論

### 🧭 專頁雷達（定向抓取）

### 📡 來源狀態
```

**區塊順序固定如上** `[順序改版: 2026-09-04]`：💰 付費方案動態**固定排在媒體報導之前**——這一區直接影響讀者的帳單與配額，冷讀者實測它被排在倒數第三時是「全篇最被低估的一條」。

### 📡 來源狀態

從 `gathered_items.json` 的 `source_status` 欄位生成表格，格式嚴格如下（web reader 解析器依賴此格式）：

| 來源 | 狀態 | 條數 |
|------|------|------|
| Anthropic Blog | ✅ | 0 |
| Hacker News | ✅ | 13 |

（每個來源一列，依 `source_status` 全部列出；`ok=true` → ✅，`false` → ❌）

### 檔尾 `[改版: 2026-09-04]`

📡 來源狀態表即是檔案結尾——「選材門檻」附錄與「今日聚焦參考連結」清單皆已廢除（門檻是內規不上讀者版；聚焦連結已改行內）。來源狀態表**上方最多兩行 `>` 說明，順序固定**：
1. Step 1b 0-2 原料健康檢查的 `> ⚠️ 本日 N 個來源抓取失敗，涵蓋面較平日窄`（有觸發才寫）
2. 缺席區塊說明：五個常設正文區塊（⭐／🔧／💰／📰／💬）本日省略者合併一行讀者語言說明（如 `> 本日 Google News 0 則故無媒體報導區；無官方發布故無技術更新區`）；🧭 專頁雷達為選配，省略不寫說明

---

## 每條排版格式（⚠️ 嚴格遵守，web reader 解析器依賴此格式）

```
**[原文標題](url)**
一到兩句繁體中文說明核心重點與為何值得關注。
`來源名稱` · MM/DD HH:MM UTC
```

- 標題行必須是 `**[標題](url)**`（方括號連結），**不可**寫成 `- **標題**：內文` 的 bullet 形式
- 來源行必須是 `` `來源` · 時間 `` 獨立一行
- 違反此格式時 web reader 會解析出空區塊，讀者只看得到今日聚焦
- **多來源條目要把來源全部列出 `[加入: 2026-08-16]`**：`gathered_items.json` 的 `contributors` 非空時（dedup 併掉的其他來源），來源欄寫成 `` `勝出來源 ＋其他來源、其他來源` ``，例如 `` `Hacker News ＋Anthropic Blog、Google News / PCMag` ``。只寫勝出來源會讓低流量官方來源在下游的來源記分卡上長期顯示零貢獻（教訓見沿革檔 2026-08-15）。解析器不受影響——`SOURCE_RE` 對反引號內是自由文字
- `gathered_items.json` 每條含 `score_unit` 欄位（分＝HN points、留言＝評論數），選材比較熱度時注意單位不同不可直接互比
- 跨來源比較熱度時的粗略等價量級：HN 30 分 ≈ Reddit 50 讚 ≈ 10 則留言 ≈ dev.to 20 讚；source_count ≥ 2（跨來源報導）視為高於任何單來源分數的訊號
- `source_count > 1` 表示多個獨立來源報導同一事件，選材時視為重要度加權訊號

---

## 語氣分寸（生成時的 System 設定）

> 你是一位專注於 Claude 與 Anthropic 生態的中文科技記者，擅長用繁體中文撰寫清晰、客觀的技術新聞摘要。
> 語氣分寸必須繼承來源，不得加碼：程度與嚴重度形容詞只能在來源原文有對應強度時使用；來源用中性或低強度字眼，摘要就對應保留該強度，寧可保守，不可放大。自我檢查法：你寫的每一個程度形容詞，都要能在 `gathered_items.json` 該則原文的標題或摘要裡找到同等強度的依據；找不到就降回中性描述。
