"""產品 × 功能對照表的解析（scripts/build_web.py parse_product_matrix／build_matrix_tracking）。

為什麼要有：2026-10-23 起網站 🛠️ 分頁整個改渲染這張矩陣，資料只來自
`wiki/topics/anthropic-product-matrix.md`。頁面格式一漂（少一欄、狀態拼錯、某產品漏一格），
矩陣會缺格或整頁空白，而 build 照樣綠——所以結構錯誤必須 raise、進 build() 的致命集合。

釘的情境：
- 合法頁解析出 5 欄產品、功能列、專屬功能、專用版，方案縮寫正確；
- 狀態不在六態、某產品缺格、缺必要章節、專用版用到的功能對不上名 → ValueError；
- 追蹤頁區：以標頭「對照角色：追蹤頁」為準，與「index 🛠️ − 矩陣出處」不一致時回 WARN；
- 真實的對照頁本身要解析得過（守住 wiki 端格式不漂）；
- gen_wiki_frontmatter 只投影對照角色的主詞。

夾具全在暫存目錄生成、不含絕對路徑，故不需 `__REPO_ROOT__` 佔位符。
"""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

bw = load_script_module("build_web")
fm = load_script_module("gen_wiki_frontmatter")

PRODUCTS = ["Claude app", "Claude Code", "Claude Tag", "Claude Platform", "Claude Duet"]
URL = "[來源](https://support.claude.com/en/articles/1)"


def cell_lines(statuses=None, plans="Free／Pro／Max／Team／Enterprise"):
    statuses = statuses or ["available", "beta", "vague", "unknown", "preview"]
    return "\n".join(f"- **{p}：** {s}｜{plans}｜說明｜{URL}｜2026-10-23｜official" for p, s in zip(PRODUCTS, statuses))


def page(matrix_body=None, drop_section=None, spec_uses="Claude Code、Skills"):
    if matrix_body is None:
        matrix_body = f"### Skills\n\n- **分組：** Capabilities\n{cell_lines()}\n- **出處：** [[entities/claude-skills]]\n\n" \
                      f"### 語音\n\n- **分組：** 其他\n{cell_lines()}\n- **出處：** —\n"
    secs = {
        "官方自己的分法": "| 官方分組 | 成員 |\n|---|---|\n| Products | Claude、Claude Code |\n",
        "產品": "| 產品 | 入口 | 誰起手 | 一句話 | 出處 |\n|---|---|---|---|---|\n"
               "| Claude app（網頁／桌面／手機） | 網頁 | 你下令 | 對話 | [[entities/cowork]] |\n"
               "| Claude Code | 終端機 | 你每句下令 | 寫程式 | [[entities/claude-code]] |\n"
               "| Claude Tag | Slack | 你每句下令 | Slack | [[entities/claude-tag]] |\n"
               "| Claude Platform | API | 你的程式呼叫 | API | [[entities/managed-agents]] |\n"
               "| Claude Duet | app | 它自己判斷 | 主動 | [[entities/claude-duet]] |\n\n"
               "- **Claude app 的 Cowork**：已併入（[來源](https://support.claude.com/en/articles/15520349)）。\n",
        "對照表": matrix_body,
        "只在一個產品裡": "| 產品 | 功能 | 狀態 | 方案 | 出處 |\n|---|---|---|---|---|\n"
                     "| Claude Code | Claude Mods | available | Pro／Max／Team／Enterprise | [[entities/claude-mods]] |\n\n"
                     "**細節**\n\n- **Claude Mods**：預設開｜[來源](https://code.claude.com/docs/en/plugins/mods/overview)｜2026-10-23｜official\n",
        "專用版": "| 專用版 | 官方分組 | 建在哪 | 模型 | 用到的功能 | 誰能用 | 出處 |\n|---|---|---|---|---|---|---|\n"
               f"| Claude Security | Specialized | 網頁 app | Mythos | {spec_uses} | Enterprise | [[entities/claude-security]] |\n"
               "| Claude for Legal | 官方不列為產品（Solutions 頁） | 解決方案頁 | 官方未說 | Claude Mods | 官方未說 | — |\n",
    }
    out = "# 對照表\n\n一句話。\n\n**狀態：** ongoing\n**最後更新：** 2026-10-23\n\n---\n\n"
    for k, v in secs.items():
        if k == drop_section:
            continue
        out += f"## {k}\n\n{v}\n"
    return out


class _Tmp(unittest.TestCase):
    def write(self, text: str) -> Path:
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        f = Path(d.name) / "anthropic-product-matrix.md"
        f.write_text(text, encoding="utf-8")
        return f


class TestParse(_Tmp):
    def test_valid_page(self):
        pm = bw.parse_product_matrix(self.write(page()))
        self.assertEqual([p["id"] for p in pm["products"]], ["claude-app", "claude-code", "tag", "platform", "duet"])
        self.assertEqual([f["name"] for f in pm["features"]], ["Skills", "語音"])
        c = pm["features"][0]["cells"]
        self.assertEqual(c["tag"]["status"], "vague")
        self.assertEqual(c["claude-app"]["abbr"], "全")
        self.assertEqual(c["claude-app"]["source"], "https://support.claude.com/en/articles/1")
        self.assertIsNone(pm["features"][1]["page"])  # 出處「—」
        self.assertEqual(pm["exclusive"][0]["product"], "claude-code")
        self.assertEqual(pm["exclusive"][0]["source"], "https://code.claude.com/docs/en/plugins/mods/overview")
        sec = pm["specialized"][0]
        self.assertEqual([u["kind"] for u in sec["uses"]], ["product", "feature"])
        self.assertTrue(sec["isProduct"])
        self.assertFalse(pm["specialized"][1]["isProduct"])
        self.assertEqual(pm["products"][0]["extra"][0]["sources"], ["https://support.claude.com/en/articles/15520349"])
        self.assertEqual(pm["checked"], "2026-10-23")

    def test_bad_status_raises(self):
        body = f"### Skills\n\n- **分組：** Capabilities\n{cell_lines(['available', 'maybe', 'beta', 'beta', 'beta'])}\n"
        with self.assertRaisesRegex(ValueError, "maybe"):
            bw.parse_product_matrix(self.write(page(body)))

    def test_missing_product_cell_raises(self):
        lines = cell_lines().splitlines()[:-1]  # 拿掉 Duet
        body = "### Skills\n\n- **分組：** Capabilities\n" + "\n".join(lines) + "\n"
        with self.assertRaisesRegex(ValueError, "Claude Duet"):
            bw.parse_product_matrix(self.write(page(body)))

    def test_missing_section_raises(self):
        with self.assertRaisesRegex(ValueError, "專用版"):
            bw.parse_product_matrix(self.write(page(drop_section="專用版")))

    def test_unknown_spec_feature_raises(self):
        with self.assertRaisesRegex(ValueError, "不存在的功能"):
            bw.parse_product_matrix(self.write(page(spec_uses="不存在的功能")))

    def test_cell_without_source_raises(self):
        body = "### Skills\n\n- **分組：** Capabilities\n" + cell_lines().replace(URL, "沒有連結", 1) + "\n"
        with self.assertRaisesRegex(ValueError, "來源"):
            bw.parse_product_matrix(self.write(page(body)))

    def test_real_page_parses(self):
        pm = bw.parse_product_matrix(bw.PRODUCT_MATRIX_PAGE)
        self.assertEqual(len(pm["products"]), 5)
        self.assertEqual(len(pm["features"]), 15)
        for f in pm["features"]:
            self.assertEqual(set(f["cells"]), {"claude-app", "claude-code", "tag", "platform", "duet"}, f["name"])


class TestHelpers(unittest.TestCase):
    def test_plan_abbr(self):
        cases = {"Free／Pro／Max／Team／Enterprise": "全", "Pro／Max／Team／Enterprise（Team／Enterprise 雲端 beta）": "付費",
                 "Team／Enterprise": "T/E", "Pro／Max": "P/M", "API（按量計費）": "API", "美國 Pro／Max（候補名單）": "美 P/M",
                 "": "", "—": "", "奇怪的方案": ""}
        for k, v in cases.items():
            self.assertEqual(bw.plan_abbr(k), v, k)

    def test_matrix_role_main(self):
        self.assertEqual(bw.matrix_role_main("功能（產出物；含 Dashboards、Motion）"), "功能")
        self.assertEqual(bw.matrix_role_main("追蹤頁"), "追蹤頁")
        self.assertEqual(bw.matrix_role_main("其他東西（x）"), "")

    def test_frontmatter_projects_main_word_only(self):
        self.assertEqual(fm.matrix_role_of("**領域：** 🛠️ 工具/功能\n**對照角色：** 專用版（獨立桌面 app）\n"), "專用版")
        self.assertIsNone(fm.matrix_role_of("**領域：** 🤖 模型\n"))
        self.assertIsNone(fm.matrix_role_of("**對照角色：** 亂寫\n"))


class TestTracking(_Tmp):
    def _item(self, pid, kind, role="", domain="🛠️ 工具/功能"):
        return {"id": pid, "pageType": kind, "name": pid, "domain": domain, "matrixRole": role, "parent": "",
                "status": "ongoing", "pill": "active", "lastNewsUpdate": "2026-10-20", "latestHeadline": "頭條"}

    def _run(self, index_rows, items):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        (Path(d.name) / "index.md").write_text("\n".join(index_rows) + "\n", encoding="utf-8")
        old = bw.WIKI_DIR
        bw.WIKI_DIR = Path(d.name)
        self.addCleanup(setattr, bw, "WIKI_DIR", old)
        pm = bw.parse_product_matrix(self.write(page()))
        ents = [i for i in items if i["pageType"] == "entity"]
        tops = [i for i in items if i["pageType"] == "topic"]
        return bw.build_matrix_tracking(pm, ents, tops, None)

    def test_header_and_index_agree(self):
        rows, warns = self._run(
            ["| [[entities/claude-skills]] | feature | 🛠️ 工具/功能 | active | x |",
             "| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | 漏洞偵測 |",
             "| [[topics/long-context-1m]] | 🛠️ 工具/功能 | ongoing | 1M 計費　↳ 子故事：[[topics/a]] |"],
            [self._item("claude-skills", "entity", "功能（Capabilities）"),
             self._item("bugcrawl", "entity", "追蹤頁"), self._item("long-context-1m", "topic", "追蹤頁")])
        self.assertEqual(warns, [])
        self.assertEqual({r["id"] for r in rows}, {"bugcrawl", "long-context-1m"})
        self.assertEqual(next(r for r in rows if r["id"] == "long-context-1m")["hook"], "1M 計費")

    def test_missing_header_warns(self):
        rows, warns = self._run(
            ["| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | 漏洞偵測 |"],
            [self._item("bugcrawl", "entity", "")])  # 忘了加對照角色
        self.assertEqual(rows, [])
        self.assertEqual(len(warns), 1)
        self.assertIn("entities/bugcrawl", warns[0])

    def test_other_domain_ignored(self):
        rows, warns = self._run(["| [[topics/x]] | 🤖 模型 | ongoing | y |"],
                                [self._item("x", "topic", "追蹤頁", domain="🤖 模型")])
        self.assertEqual((rows, warns), ([], []))


class TestBuildFatal(unittest.TestCase):
    """index 有登記對照頁、檔卻解析不了 → build() 必須 exit 1（不可靜默退回列表）。"""

    def _build(self, page_text):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        root = Path(d.name)
        for sub in ("wiki/entities", "wiki/topics", "news", "web_reader/data"):
            (root / sub).mkdir(parents=True)
        (root / "wiki" / "index.md").write_text(
            "| [[topics/anthropic-product-matrix]] | 🛠️ 工具/功能 | ongoing | 對照表 |\n", encoding="utf-8")
        if page_text is not None:
            (root / "wiki" / "topics" / "anthropic-product-matrix.md").write_text(page_text, encoding="utf-8")
        patched = {"ROOT": root, "WIKI_DIR": root / "wiki", "WIKI_ENTITIES": root / "wiki" / "entities",
                   "WIKI_TOPICS": root / "wiki" / "topics", "WIKI_RADAR": root / "wiki" / "feature-radar.md",
                   "NEWS_DIR": root / "news", "DAILY_DIR": root / "daily", "WEEKLY_DIR": root / "weekly",
                   "OUT_JS": root / "web_reader" / "data" / "data.js",
                   "OUT_WIKI_DIR": root / "web_reader" / "data" / "wiki",
                   "OUT_DIGEST_DIR": root / "web_reader" / "data" / "digest",
                   "OUT_WEEKLY_DIR": root / "web_reader" / "data" / "weekly",
                   "OUT_SEARCH_INDEX": root / "web_reader" / "data" / "search-index.json"}
        orig = {k: getattr(bw, k) for k in patched}
        for k, v in patched.items():
            setattr(bw, k, v)
        self.addCleanup(lambda: [setattr(bw, k, v) for k, v in orig.items()])
        # 吞掉 build 的輸出：致命時印的「ERROR: 下列 wiki 頁面解析失敗…」會被 gate_web_build 的
        # 失敗行 regex 當成真的測試失敗（本測試要的正是那個致命路徑）
        with contextlib.redirect_stdout(io.StringIO()):
            bw.build()

    def test_listed_but_missing_is_fatal(self):
        with self.assertRaises(SystemExit):
            self._build(None)

    def test_listed_but_broken_is_fatal(self):
        with self.assertRaises(SystemExit):
            self._build(page(drop_section="對照表"))


if __name__ == "__main__":
    unittest.main()
