---
paths:
  - "CLAUDE.md"
  - "wiki/CLAUDE.md"
  - ".claude/**/*.md"
  - ".claude/review-registry.json"
---
# CLAUDE.md 及規則檔修改規則

修改根目錄 `CLAUDE.md`、`wiki/CLAUDE.md`、`.claude/commands/*.md`、`.claude/rules/*.md`、`.claude/reporter-rules/**/*.md`、`.claude/agents/*.md`、`.claude/review-registry.json` 前必須讀取此檔案（與檔首 `paths:` 同範圍）。

---

## 修改前：確認影響範圍

**先執行反向查詢，找出所有引用方：**
```
grep -rn "被修改的檔名" .claude/ docs/rules-changelog/
```

範圍要含 `.claude/agents/`（所有記者角色檔都引用 reporter-rules；**不寫死檔數**——角色檔會增減，寫死的數字必然漂掉）、`.claude/review-registry.json`（registry 登記的檔名與 pattern）與沿革檔。逐一確認每個引用方在修改後仍能正確找到所需規則。若不確定影響範圍，寧可先查、再動手。

---

## 修改時：路徑引用原則

command / skill 中永遠使用明確路徑，**禁止裸露的 `CLAUDE.md`**：

| 寫法 | 判斷 |
|------|------|
| `` `wiki/CLAUDE.md` `` | ✅ 明確 |
| `` `.claude/reporter-rules/features/daily.md` `` | ✅ 明確 |
| `` `CLAUDE.md` ``（無路徑前綴） | ❌ 禁止 |
| `見 CLAUDE.md`（無路徑前綴） | ❌ 禁止 |

理由：裸露路徑在重構時無法靠 grep 追蹤，容易造成 skill 靜默失效。

---

## 修改時：不標日期、不指沿革

條文不掛 `[加入: 日期]`／`[改版: 日期]` 之類的版本戳（2026-09-13 廢除，全庫 342 個已清）。規則年齡由 git blame 算（`python scripts/lint_health.py age`，`/wiki-lint` 6d 的量測端）；來歷寫進 `docs/rules-changelog/` 對應檔的日期段，正文不留「起因見沿革檔」指路句。正文只留會改變執行者邊界判斷的那一句為什麼；事故經過、日期、量測進沿革檔。

---

## 修改時：CLAUDE.md 設計原則

**適合放進 CLAUDE.md 的內容：**
- 有明確觸發條件的操作規則（「執行 X 時必須做 Y」）
- 可用 grep 驗證的格式規範
- 邊界判斷（單一 yes/no 問題）
- 跨 skill 共用的限制（路徑、語言、唯讀）

**不適合放進 CLAUDE.md 的內容：**
- 快速上手、安裝說明（→ `README.md`）
- 格式模板／範本（→ 消費它的那份 rules 檔；跨 skill 共用且無單一消費者的，放共用載入點 `wiki/CLAUDE.md` 或 `.claude/reporter-rules/shared.md`，根目錄只留判準句＋指路）
- 面向人類的操作範例（→ `README.md`）
- 教訓敘事（→ 該檔的沿革檔，`docs/rules-changelog/`）：條文只留判準＋「沿革檔 日期」指路，不進 agent 讀取範圍

> 規則檔以「內容是否精簡、有無重複」為準，不設行數上限；長度非簡化理由（同 wiki 頁面「一頁一故事」哲學）。

---

## 修改時：機械契約字串住固定區

**任何會被 script grep／regex 消費的字串（小標、表頭、標籤、格式形狀），在規格檔裡只能住該規格檔的「機械契約字串」表**（現有：`weekly-report.md` 一張、`.claude/skills/news-digest/references/format.md` 與 `.claude/skills/reader-digest/references/format.md` 各一張），正文條文引用時指回該表，不另抄一份；新增契約字串時同步登記 `.claude/review-registry.json` 的 `sync_pairs`（規格端與消費端互相指認），讓 `check_rules.py` 看守。

> 立法依據見沿革檔 2026-09-04。

**判斷式：** 這個字串有沒有任何 script 在 grep？用指令答，不憑印象——

```
grep -rn "要改的字串" scripts/ web_reader/assets/ src/tests/
```

有命中 → 進契約表＋registry（登記時**規格端與消費端各一組 pattern**，避免 `all_contain` 全檔搜尋讓同檔第二份副本掩護漂移）；零命中 → 一般文案，自由改。本檔上方「修改前：確認影響範圍」的反向查詢只掃 `.claude/`，接不到程式端——兩個 grep 都要跑。

---

## rules 檔必須有 `paths:` 範圍

無 `paths:` 的規則檔會在**每個 session 無條件載入**（實測與搬遷經過見沿革檔 2026-09-12）。

- **新增規則檔必帶 `paths:`**，寫在檔首 frontmatter，`---` 後緊接 `# 標題`：

  ```
  ---
  paths:
    - "wiki/entities/**/*.md"
    - "wiki/topics/model-*.md"
  ---
  ```

- **範圍＝消費這份規則的場景會讀到的檔案**（負責頁面、看守腳本、資料帳本）。寧可略寬也不要漏——漏了會讓該場景失去規則。
- glob 相對專案根（`CLAUDE_NEWS/`），支援 `**` 與 `{a,b}`。
- **載入靠明文 Read，不靠自動載入**：記者由角色檔（`.claude/agents/wiki-reporter-*.md`）列規則清單、主編由 command 內文指名，`paths:` 只是縮小無條件載入量。
- **只給記者／主編明文 Read 的規則放 `.claude/reporter-rules/`，不放本資料夾**——那裡沒有自動載入機制，不需要也不應該帶 `paths:`（帶了只是裝飾）。本資料夾只留主 session 自己會用到的規則。
- 由 `src/tests/test_rules_frontmatter.py` 看守：缺 `paths:`、空清單、glob 在庫內零匹配、或 frontmatter 後未緊接 `# 標題` 皆 FAIL（只掃 `.claude/rules/*.md`）。

---

## 修改後：強制驗證

**修改完成後執行 `/review-commands`，直到零錯誤才可收工。**

規則一致性已納入測試套件（`scripts/check_rules.py`，讀取 `.claude/review-registry.json` 執行裸露引用、路徑存在性、錨點、同步配對、coupling hints、個人路徑外洩等機械檢查；**檢查項會增加，以該腳本輸出為準、不在此寫死類數**），`/review-commands` 只做失敗判讀與修復，不再手動 grep。新增同步配對或錨點時登記進 `.claude/review-registry.json`，不需另外維護紙本註冊表。

Stop hook `.claude/hooks/check_rules_on_stop.py` 會在收工時比對規則檔 mtime 與 `.claude/.last-rules-check`，改了規則卻沒跑 `check_rules.py` 全綠就會被擋下——這不是替代 `/review-commands`，只是兜底。

**判斷標準：**
> 所有引用這個檔案的 command / skill，在修改後還能正確找到所需的規則或格式嗎？若否，先修引用再收工。

> **沿革檔：** `docs/rules-changelog/claude-md-edit.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，）
