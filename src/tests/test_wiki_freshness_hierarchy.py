"""設計者四案改寫為帶 item_url＋評審加第 5 案（新子頁漏報歸因、上層天天有歸因 → 仍紅）。"""
import importlib.util, io, json, os, tempfile, unittest
from pathlib import Path
SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "check_wiki_freshness.py"

def _page(title, last_news, parent=None, body=""):
    up = f"**上層：** [[{parent}]]\n" if parent else ""
    return f"# {title}\n\n**狀態：** ongoing\n**領域：** 🌐 社群\n{up}**最後更新：** {last_news}\n**最後新聞更新：** {last_news}\n\n{body}\n"

class FreshnessHierarchy(unittest.TestCase):
    def _run(self, pages, atts, today):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for sub in ("entities", "topics"):
                (root / "wiki" / sub).mkdir(parents=True)
            for slug, text in pages.items():
                (root / "wiki" / f"{slug}.md").write_text(text, encoding="utf-8")
            (root / "data").mkdir()
            with open(root / "data" / "source_attribution.jsonl", "w", encoding="utf-8") as fh:
                for page, day, url in atts:
                    fh.write(json.dumps({"date": day, "page": page, "item_url": url}, ensure_ascii=False) + "\n")
            spec = importlib.util.spec_from_file_location("cwf_under_test", SCRIPT)
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            m.REPO_ROOT, m.WIKI_DIR, m.ATTRIBUTION = root, root / "wiki", root / "data" / "source_attribution.jsonl"
            buf = io.StringIO(); m._stdout = lambda: buf
            rc = m.main(["x", today]); return rc, buf.getvalue()

    def test_1_拆頁當天子頁零歸因不紅(self):
        rc, out = self._run({"topics/hub": _page("母", "2026-10-07"),
                             "topics/kid": _page("子", "2026-10-06", "topics/hub", "[a](https://x/a)")},
                            [("topics/hub", "2026-10-06", "https://x/a"), ("topics/hub", "2026-10-07", "https://x/b")], "2026-10-09")
        self.assertEqual(rc, 0, out)

    def test_2_子頁宣稱日晚於母頁歸因仍紅(self):
        rc, out = self._run({"topics/hub": _page("母", "2026-10-07"),
                             "topics/kid": _page("子", "2026-10-08", "topics/hub", "[a](https://x/a)")},
                            [("topics/hub", "2026-10-07", "https://x/a")], "2026-10-09")
        self.assertEqual(rc, 1); self.assertIn("topics/kid", out)

    def test_3_子頁進新聞母頁不動不判漏更(self):
        rc, out = self._run({"topics/hub": _page("母", "2026-10-07"),
                             "topics/kid": _page("子", "2026-10-10", "topics/hub")},
                            [("topics/hub", "2026-10-07", "u1"), ("topics/kid", "2026-10-10", "u2")], "2026-10-10")
        self.assertEqual(rc, 0, out)

    def test_4_無上層零歸因仍紅(self):
        rc, out = self._run({"topics/solo": _page("獨", "2026-10-08")}, [], "2026-10-09")
        self.assertEqual(rc, 1); self.assertIn("topics/solo", out)

    def test_5_新子頁漏報歸因上層天天有歸因仍紅(self):
        rc, out = self._run({"entities/hub": _page("母", "2026-10-12"),
                             "entities/kid": _page("子", "2026-10-12", "entities/hub", "[n](https://x/new)")},
                            [("entities/hub", "2026-10-12", "https://x/parent-own")], "2026-10-12")
        self.assertEqual(rc, 1); self.assertIn("entities/kid", out)

if __name__ == "__main__":
    unittest.main()
