"""根層頁必須有頁面產物——防「index 連得到、網站點不開」。

死因（2026-09-12 lint 渲染層驗收抓到）：`wiki/overview.md` 每週被重寫，
`wiki/index.md` 概覽區第一列把它列為讀者入口，graph.json 也把它當節點，
但 `build_web.py` 從來沒有產出 `overview.json`——讀者在網站上點進去是死路。
build 綠燈、測試全綠、markdown 完全正確，壞的只有「讀者看到的東西」。

本測試看守的不是 overview 這一頁，而是那條規則：**`wiki/index.md` 用
wikilink 連到的每個根層頁（`wiki/*.md`，非 entities/ topics/），都必須有
對應的 `web_reader/data/wiki/<slug>.json`。**
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX_MD = ROOT / "wiki" / "index.md"
OUT_WIKI_DIR = ROOT / "web_reader" / "data" / "wiki"

# 這些根層頁刻意不上站（封存頁由母頁錨點承接，log 過長且只有維護者讀）
EXEMPT = {"log"}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def root_pages_linked_from_index() -> set[str]:
    if not INDEX_MD.exists():
        return set()
    text = INDEX_MD.read_text(encoding="utf-8-sig")
    out = set()
    for target in WIKILINK_RE.findall(text):
        target = target.strip()
        if "/" in target:          # entities/ topics/ news/ 都不是根層頁
            continue
        if target in EXEMPT:
            continue
        if (ROOT / "wiki" / f"{target}.md").exists():
            out.add(target)
    return out


class TestRootPagesHaveProducts(unittest.TestCase):
    def test_every_root_page_linked_from_index_has_a_json_product(self):
        linked = root_pages_linked_from_index()
        self.assertTrue(linked, "index.md 應至少連到一個根層頁；抓不到代表解析壞了")
        missing = sorted(p for p in linked if not (OUT_WIKI_DIR / f"{p}.json").exists())
        self.assertEqual(
            missing, [],
            f"index.md 連到這些根層頁但網站沒有對應產物，讀者點進去是死路：{missing}。"
            f"修法二選一：(a) 在 build_web.py 產出該頁的 wiki/<slug>.json；"
            f"(b) 確認刻意不上站，則自 index.md 移除該列並加進本測試的 EXEMPT"
        )

    def test_overview_product_is_openable_shaped(self):
        """產物光存在還不夠——它得帶得動前端的開頁流程。"""
        f = OUT_WIKI_DIR / "overview.json"
        if not f.exists():
            self.skipTest("overview.json 尚未建置（build_web 未跑過）")
        data = json.loads(f.read_text(encoding="utf-8"))
        for key in ("id", "pageType", "name", "markdown"):
            self.assertIn(key, data, f"overview.json 缺 {key}，前端 openWikiPage 會渲染出空殼")
        self.assertEqual(data["id"], "overview")
        self.assertTrue(data["markdown"].strip(), "overview.json 的 markdown 是空的")


if __name__ == "__main__":
    unittest.main()
