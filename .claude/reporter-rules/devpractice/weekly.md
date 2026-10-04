# Wiki Ingest — 開發實務（devpractice）週彙整指南（lint 層）

`/wiki-lint` 步驟 5f 由主編派 devpractice 記者執行（週彙整的明文觸發邊）。每日 ingest 不讀此檔。

**執行順序前提：** 5f 在六記者 lint 收報**之後**跑——社群記者的 tools 策展與 patterns 更新已完成，你讀到的是本週最終狀態。手冊整頁只有你寫，不會互踩。

---

## 每週兩件事

### 1. 手冊週更

照 `.claude/reporter-rules/devpractice/pages.md`「週更動作」七步執行。候選從 `python scripts/devpractice_diff.py pending` 讀，不看日期——哪一週沒跑，這週會一起看到。**並讀 [[topics/skill-interest-watch]] 各類「本週竄升」欄**：竄升者是值得知道的第一手線索，但星數是規模不是品質，寫進正文須另有一句為什麼。

**連續 2 週正文零改動** → 回報標「⚠️ 連續 2 週手冊正文零改動，建議檢討收錄判準是否過嚴」轉知主編。coding 是本庫大宗，連續空手更可能是判準太嚴或每日沉澱失靈。

### 2. coding 跨頁對帳

檢查三處引用是否失步（引用方 vs 事實的家）：

| 引用方 | 事實的家 | 對什麼 |
|---|---|---|
| guide 導航表「社群側見…」行 | `community-tech-tools` 🧩 Skills 速查 | 節名還在嗎 |
| `community-large-codebase-workflow` 各線 🧰 行 | tools「我卡在這裡」決策表 | 症狀句與首選還對得上嗎（機械層已有 `scripts/check_tools_page.py`，此處看語意） |
| `wiki/index.md` 💻 開發實務入口表 | 各目標頁 | 路由描述還成立嗎；本週有新 coding 頁值得入表嗎 |

失步屬手冊的直接改；屬他人頁面（tools、large-codebase、index）→ 回報「⚠️ 需主編轉知」。

## 欄位與回報

- 寫過頁就跑 `.claude/reporter-rules/shared.md` 的機械自查
- 回報格式：

  ```
  ## 開發實務 記者回報（weekly 彙整）
  候選：待處理 N 筆 → 落地 a 筆（哪幾段）／不寫 b 筆
  技能清冊：增 x／減 y／無異動
  社群面補段：第 X 段——已補／零證據（已查範圍）
  本週亮點：N 條（or 無）
  跨頁對帳：✅ 一致 ／ ⚠️ 失步 M 處（已改 a／需轉知 b）
  同步自查：[✅ / ⚠️ 需主編轉知（說明）]
  ```
