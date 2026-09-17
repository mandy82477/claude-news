# Wiki Ingest 記者派工循序圖（Markdown 版）

互動版見同目錄 `wiki-ingest-dispatch.html`（archify 產出，含 Guided Views 點擊亮路徑、hover 預覽、Path/Map/Lens 工具）。本檔是同一份 `wiki-ingest-dispatch.sequence.json` 規格的 Mermaid 對照版，供不方便開瀏覽器時快速查閱。

只涵蓋 `/news-pipeline` 的 Step2（Phase B）——抓新聞產日報是另一段背景 Phase A、收尾發布是背景 Phase C，兩者皆非「記者」角色，不在本圖範圍。

```mermaid
sequenceDiagram
    participant editor as 主編（主 Session）
    participant models as 模型記者
    participant features as 功能記者
    participant commercial as 商業記者
    participant safety as 安全政策記者
    participant community as 社群記者
    participant people as 人物記者
    participant review as 分類複核記者（新增）
    participant devpractice as 開發實務記者
    participant market as 投資分析記者

    Note over editor: 分類→寫帳本→對帳閘（獨立作業）

    par 同批派工（同一則訊息內一次送出，不是依序等待）
        editor->>models: 派工①
    and
        editor->>features: 派工②
    and
        editor->>commercial: 派工③
    and
        editor->>safety: 派工④
    and
        editor->>community: 派工⑤
    and
        editor->>people: 派工⑥
    and
        editor->>review: 派工⑦
    end

    par 記者回報
        models-->>editor: 回報①
    and
        features-->>editor: 回報②
    and
        commercial-->>editor: 回報③
    and
        safety-->>editor: 回報④
    and
        community-->>editor: 回報⑤
    and
        people-->>editor: 回報⑥
    and
        review-->>editor: 回報⑦（誤排除→分類回退）
    end

    Note over editor: 分類回退：同輪內按類別合併追加派工，不進轉知帳本

    Note over editor: 彙整共用檔 → 派沉澱／判讀（彙整後才派，非同批）

    editor->>devpractice: 沉澱派工
    editor->>market: 判讀派工
    devpractice-->>editor: 候選回報
    market-->>editor: 判讀回報

    Note over editor: 讀者版日報 daily/TARGET_DATE.md（獨立作業）
```

## 共用規則 vs 特殊規則

- **六類記者**（模型／功能／商業／安全政策／社群／人物）共用同一套分類路由：依日報條目類別派工，各有負責頁面。
- **分類複核記者／開發實務記者／投資分析記者**——三者角色檔皆明文「與六類記者不同，不在分類路由內」：
  - 分類複核記者：讀主編當天排除、未派給任何記者的條目清單，覆核有沒有誤排除
  - 開發實務記者：不吃日報條目，吃本輪 ingest 寫進 wiki 的 diff
  - 投資分析記者：不吃分類路由，吃當日日報本身換市場框架重讀

檔案結構（誰讀哪份規則檔）見同目錄 `reporter-rules-files.md`。
