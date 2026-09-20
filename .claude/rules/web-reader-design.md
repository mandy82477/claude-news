---
paths:
  - "web_reader/index.html"
  - "web_reader/**/*.css"
  - "web_reader/**/*.js"
  - "scripts/build_web.py"
---
# Web Reader 設計規範

修改 `web_reader/index.html`、`web_reader/assets/design.css`、`web_reader/assets/app.js` 前必須讀取此檔案。

---

## 設計語言

**風格：** paper/sumi editorial — 書卷氣排版，hairline 邊框，單一 ochre 強調色。

**三條核心原則：**
1. Hairline-first：邊框用 0.5–1px，不用粗框或填色背景（active 狀態改用 outline 或底線）
2. Sharp corners：`border-radius` ≤ 2px（特例：pill shape 用 `border-radius: 99px`，需有明確理由）
3. 單色強調：全站只有 ochre 一個品牌色，不引入第二強調色

---

## 色票 token（明暗雙模式自動切換）

| token | 用途 |
|-------|------|
| `--ochre-9` | 主強調色（文字、active 狀態、連結 hover） |
| `--ochre-7` | 次要強調（邊框 hover、icon） |
| `--ochre-5` | 輔助 hover（底線、淡色填充） |
| `--ochre-tint` | 背景淡染（active 狀態 bg） |
| `--ink-1` | 主文字 |
| `--ink-2` | 次要文字 |
| `--ink-3` | 輔助文字（placeholder、label） |
| `--ink-4` | 極淡文字（disabled、裝飾） |
| `--bg-0` | 頁面底色（paper 色） |
| `--bg-1` | hover 狀態背景 |
| `--border-2` | 標準邊框（hairline，半透明） |
| `--border-strong` | 強調邊框 |

---

## 字型使用原則

| 變數 | 字型 | 用途 |
|------|------|------|
| `--font-display` | Cormorant Garamond + Noto Serif | 標題、引言、summary 斜體 |
| `--font-sans` | Inter + Noto Sans TC | UI 元件（按鈕、label、chip、nav） |
| `--font-mono` | JetBrains Mono | code、slug、日期、meta 數值 |

**判斷原則：** UI 控制元件（按鈕、chip、filter）用 `--font-sans`；不可用 `--font-mono` 做 UI 控制元件。

---

## 元件慣例

### Tab / filter bar

實作類名是 `.domain-chips` / `.domain-chip`（**不是 `.tab-row` / `.tab`——那兩個類名全庫從未存在過**，照舊範例寫會加出一組沒人套用的死 CSS）：

```css
.domain-chips { display: flex; flex-wrap: nowrap; overflow-x: auto; gap: 0; border-bottom: 1px solid var(--border-2); }
.domain-chip {
  font-family: var(--font-sans); font-size: var(--fs-small);
  padding: 7px 14px; border: none; border-bottom: 2px solid transparent;
  background: transparent; color: var(--ink-3);
  margin-bottom: -1px;
}
.domain-chip:hover { color: var(--ink-2); border-bottom-color: var(--ochre-5); }
.domain-chip--active { color: var(--ochre-9); border-bottom-color: var(--ochre-9); }
```

### Pill（狀態標籤）
- border + 文字色，**無填色背景**
- `border-radius: var(--radius-2)`（約 3–4px）
- `.pill--active`：`color: var(--success); border-color: var(--success)`

### 圖示
- 優先使用 inline SVG（自繪，stroke 風格，`stroke-width: 1.8`）
- **不使用平台 emoji 作為 UI 圖示**（跨平台渲染不一致）
- emoji 只允許在 markdown 內文或 wiki 資料值中保留
- icon 尺寸：UI 行內 13px，裝飾性最大 18px

### 卡片（pinned）
- `border: 1px solid var(--border-2)`，`border-radius: 2px`
- hover：`background: var(--bg-1); border-color: var(--border-strong)`
- **無 box-shadow、無 gradient**
- 適用 `.radar-card` / `.gap-card` / `.pin-card`

> **entity 清單不是卡片**：2026-07-04 起改為表格列 `.entity-table` / `.entity-row`，`.entity-card` 全庫從未存在過。照舊標題把 entity 當卡片改，會改錯元件。

---

## 禁止清單

- ❌ **裝飾性漸層**（background 和 border 都不行）
  - 禁的是「看得出漸層」這個**效果**，不是 `linear-gradient()` 這個函式。用 `repeating-linear-gradient` 畫 **1px 虛線分隔線**（實 4px／空 4px 交替，等價於 `border-style: dashed`、只是 dash 長度可控）不在此限——它產生的是一條虛線，不是漸層。
  - 判斷式：**把它截圖給人看，他會說「這裡有漸層」嗎？** 不會 → 不是本條要擋的東西。
- ❌ box-shadow（除非是 focus ring）
 - 品牌 token 檔（`.claude/skills/claude-news-llm-wiki-design/colors_and_type.css`）定義的 `--shadow-1/--shadow-2`（"one whisper for elevated paper"）在本站**刻意不使用**——2026-07-26 美感 review 曾提議放寬給三處抬升容器，使用者裁決維持全面禁用。此為已裁決事項，後續 review 不需再提
 - **抬升要用本站自己的語彙做**：hairline 邊框＋底色對比＋（必要時）overlay 的 `backdrop-filter`，不用陰影。`.search-modal` 曾有一道 `0 24px 64px` 的抬升陰影（2026-05-15 寫入，早於上述裁決故漏網），2026-09-20 移除——該 modal 本來就有 `--bg-1` 底色、hairline 邊框與 overlay 模糊三重區隔，陰影是多的
- ❌ 平台 emoji 作為 UI 圖示
- ❌ `--font-mono` 用在 UI 控制元件
- ❌ 第二強調色（只有 ochre）
- ❌ `border-radius` > 99px（pill）或 > 2px（其他元件）
- ❌ `font-weight` > 500

---

## 週報：判準不上螢幕

週報「下週看什麼」的**判準欄不渲染到網站**。它是給 `scripts/check_weekly_ledger.py` 的凍結契約（尾端還掛著 `｜查證：` 探針關鍵字），不是給讀者的內容——使用者裁決「那感覺不是給人看的」。

- markdown 與 `web_reader/data/weekly/*.json` **照舊保留** criterion 欄位，凍結與逐條結算機制零改動；只是不上螢幕
- 螢幕上保留 `待回收 · Wnn` 一句——那是全站唯一告訴讀者「這條預告不是白說的、下週會回來結算」的東西，支撐本節「提醒下週值得關注」的目的
- 對應的 `.weekly-bet__criterion` / `.weekly-ledger__criterion` / `.weekly-bet__criterion-label` CSS 與 `weeklyCriterionText()` 已一併移除；`wikilinkButtonHtml` 的 `opts.short` 因此無呼叫端，要再用須同時補回 CSS

> 此為已裁決事項，後續 review 不需再提「判準欄可讀性」——它不在螢幕上。

---

## 版本號更新

每次修改 `design.css` 或 `app.js` 後，更新 `index.html` 中對應的 `?v=` 參數為當前 Unix timestamp，避免瀏覽器 cache 舊版本。

---

## 修改後必做

1. 確認 JS 中 class selector（如 `.domain-chip--active`、`data-domain`）與 HTML 一致
2. 若新增 CSS class，同步確認無與既有 class 命名衝突
