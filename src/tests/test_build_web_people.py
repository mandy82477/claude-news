"""人物頁欄位解析測試（身分／與 Anthropic／職能／為何追蹤）。

契約見實作規格 §1、§2：
- META_RE 新增 identity / anthropicRel / func / why
- VALID_ANTHROPIC_RELS、VALID_PERSON_FUNCS 兩個列舉常數
- identity_from_index_desc(desc) 純函式（index.md 描述欄第一子句 fallback）
- parse_wiki() 在人物頁輸出 identity / identitySource / anthropicRel / func / why；
  列舉外的值 -> None 並印 WARN（不 fail）
夾具一律用 tmp 目錄的最小 markdown，不依賴 wiki/ 真實頁面。
"""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from tests._helpers import load_script_module

build_web = load_script_module("build_web")

ANTHROPIC_RELS = ["創辦團隊", "治理", "現任", "前員工", "投資人", "同業", "外部觀察者"]
PERSON_FUNCS = ["經營者", "研究者", "工程產品", "政策治理", "投資人", "評論媒體", "其他"]
PERSON_KEYS = ("identity", "anthropicRel", "func", "why")


def _page(entity_type="person", identity="Nvidia 執行長", rel="投資人",
          func="經營者", why="財報電話會議稱對投資 Anthropic 唯一後悔是投得不夠多",
          colon="：", extra_header=None) -> str:
    """組一頁最小人物 markdown。欄位傳 None 代表該行不寫。"""
    head = [
        "# 測試人物", "",
        f"**類型{colon}** {entity_type}",
        f"**狀態{colon}** active",
        f"**領域{colon}** 👤 人物",
    ]
    if identity is not None:
        head.append(f"**身分{colon}** {identity}")
    if rel is not None:
        head.append(f"**與 Anthropic{colon}** {rel}")
    if func is not None:
        head.append(f"**職能{colon}** {func}")
    if why is not None:
        head.append(f"**為何追蹤{colon}** {why}")
    head += extra_header or []
    head += [
        f"**首次出現{colon}** 2026-01-01",
        f"**最後更新{colon}** 2026-01-02",
        f"**最後新聞更新{colon}** 2026-01-02",
        "", "## 現況", "", "測試內容。", "",
    ]
    return "\n".join(head)


class _Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def parse(self, content: str, name="test-person.md"):
        p = Path(self.tmp.name) / name
        p.write_text(content, encoding="utf-8")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            meta = build_web.parse_wiki(p, "entity")
        return meta, buf.getvalue()


class TestApiSurface(unittest.TestCase):
    """實作端承諾的名稱必須存在；缺什麼在這裡清楚 FAIL。"""

    def test_meta_re_has_person_keys(self):
        for k in PERSON_KEYS:
            self.assertIn(k, build_web.META_RE, f"build_web.META_RE 缺少鍵 {k!r}")

    def test_enum_constants(self):
        self.assertTrue(hasattr(build_web, "VALID_ANTHROPIC_RELS"),
                        "缺 build_web.VALID_ANTHROPIC_RELS")
        self.assertTrue(hasattr(build_web, "VALID_PERSON_FUNCS"),
                        "缺 build_web.VALID_PERSON_FUNCS")
        self.assertEqual(set(build_web.VALID_ANTHROPIC_RELS), set(ANTHROPIC_RELS))
        self.assertEqual(set(build_web.VALID_PERSON_FUNCS), set(PERSON_FUNCS))

    def test_identity_fn_exists(self):
        self.assertTrue(callable(getattr(build_web, "identity_from_index_desc", None)),
                        "缺 build_web.identity_from_index_desc")


class TestPersonFieldsParsed(_Base):
    def test_all_four_fields_valid(self):
        meta, _ = self.parse(_page())
        self.assertEqual(meta["identity"], "Nvidia 執行長")
        self.assertEqual(meta["identitySource"], "page")
        self.assertEqual(meta["anthropicRel"], "投資人")
        self.assertEqual(meta["func"], "經營者")
        self.assertEqual(meta["why"], "財報電話會議稱對投資 Anthropic 唯一後悔是投得不夠多")

    def test_every_valid_rel_and_func_roundtrip(self):
        for rel in ANTHROPIC_RELS:
            meta, _ = self.parse(_page(rel=rel))
            self.assertEqual(meta["anthropicRel"], rel)
        for fn in PERSON_FUNCS:
            meta, _ = self.parse(_page(func=fn))
            self.assertEqual(meta["func"], fn)

    def test_halfwidth_colon(self):
        meta, _ = self.parse(_page(colon=":"))
        self.assertEqual(meta["identity"], "Nvidia 執行長")
        self.assertEqual(meta["identitySource"], "page")
        self.assertEqual(meta["anthropicRel"], "投資人")
        self.assertEqual(meta["func"], "經營者")
        self.assertIsNotNone(meta["why"])

    def test_values_stripped(self):
        meta, _ = self.parse(_page(identity="   Nvidia 執行長   ", rel="  投資人  ",
                                   func="\t經營者 ", why="  某原因  "))
        self.assertEqual(meta["identity"], "Nvidia 執行長")
        self.assertEqual(meta["anthropicRel"], "投資人")
        self.assertEqual(meta["func"], "經營者")
        self.assertEqual(meta["why"], "某原因")

    def test_crlf_values_clean(self):
        p = Path(self.tmp.name) / "crlf-person.md"
        p.write_bytes(_page().replace("\n", "\r\n").encode("utf-8"))
        with contextlib.redirect_stdout(io.StringIO()):
            meta = build_web.parse_wiki(p, "entity")
        for k in ("identity", "anthropicRel", "func", "why"):
            self.assertNotIn("\r", meta[k])
        self.assertEqual(meta["anthropicRel"], "投資人")


class TestInvalidEnumsBecomeNull(_Base):
    def test_rel_outside_enum_is_null_and_warns(self):
        # 規格待決：括號補充說明要不要剝掉。此處依「不合法 -> null」測。
        for bad in ("治理／董事", "前員工（2024）", "投資人（個人）", "隨便"):
            meta, out = self.parse(_page(rel=bad))
            self.assertIsNone(meta["anthropicRel"], f"{bad!r} 應為 null")
            self.assertIn("WARN", out, f"{bad!r} 應印 WARN")
            # 其他欄位不受影響
            self.assertEqual(meta["func"], "經營者")

    def test_func_outside_enum_is_null_and_warns(self):
        for bad in ("CEO", "經營者／投資人", "經營者（前）"):
            meta, out = self.parse(_page(func=bad))
            self.assertIsNone(meta["func"], f"{bad!r} 應為 null")
            self.assertIn("WARN", out)
            self.assertEqual(meta["anthropicRel"], "投資人")

    def test_missing_rel_and_func_are_null(self):
        meta, _ = self.parse(_page(rel=None, func=None))
        self.assertIsNone(meta["anthropicRel"])
        self.assertIsNone(meta["func"])

    def test_missing_why_is_null(self):
        meta, _ = self.parse(_page(why=None))
        self.assertIsNone(meta["why"])


class TestIdentityFallbackOnParse(_Base):
    def test_missing_identity_not_marked_page(self):
        # parse_wiki 看不到 index.md；缺欄位時不得宣稱 source=page，
        # 且不得把別的欄位值（如為何追蹤）誤當身分。
        meta, _ = self.parse(_page(identity=None))
        self.assertNotEqual(meta.get("identitySource"), "page")
        self.assertFalse(meta.get("identity"))


class TestIdentityFromIndexDesc(unittest.TestCase):
    def setUp(self):
        self.fn = build_web.identity_from_index_desc

    def test_cases(self):
        cases = [
            ("Nvidia 執行長；2026-08-26 財報…", "Nvidia 執行長"),
            ("Claude Code 創始人，「Loops 是未來」設計哲學", "Claude Code 創始人"),
            ("前聯準會主席，2026-07-09 加入…", "前聯準會主席"),
            ("AI「教父」、Meta 前首席 AI 科學家；2026-10-01…",
             "AI「教父」、Meta 前首席 AI 科學家"),
            ("Anthropic「Claude for Legal」負責人（2026-08-07 任命…）",
             "Anthropic「Claude for Legal」負責人"),
            ("Anthropic「Claude for Legal」負責人(2026-08-07 appointed)",
             "Anthropic「Claude for Legal」負責人"),
            ("某某教授。其餘", "某某教授"),
        ]
        for desc, want in cases:
            with self.subTest(desc=desc):
                self.assertEqual(self.fn(desc), want)

    def test_wikilink_stripped(self):
        out = self.fn("[[entities/dario-amodei]] 的共同創辦人，其餘描述")
        self.assertNotIn("[[", out)
        self.assertNotIn("]]", out)
        self.assertIn("共同創辦人", out)

    def test_wikilink_with_alias_stripped(self):
        out = self.fn("[[entities/dario-amodei|Dario]] 的共同創辦人，其餘")
        self.assertNotIn("[[", out)
        self.assertNotIn("]]", out)
        self.assertNotIn("entities/", out)

    def test_result_is_stripped_str(self):
        out = self.fn("  Nvidia 執行長 ；其餘")
        self.assertIsInstance(out, str)
        self.assertEqual(out, out.strip())


class TestNonPersonPages(_Base):
    """非人物頁：欄位不輸出或為 null（兩種皆可，但 feature／model 之間要一致）。"""

    def _absent_or_null(self, meta):
        return {k: (meta.get(k) is None or meta.get(k) == "") for k in PERSON_KEYS}

    def test_feature_and_model_no_person_fields(self):
        results = {}
        for et in ("feature", "model"):
            meta, _ = self.parse(
                _page(entity_type=et, identity=None, rel=None, func=None, why=None),
                name=f"{et}-page.md")
            self.assertEqual(meta["entityType"], et)
            flags = self._absent_or_null(meta)
            self.assertTrue(all(flags.values()), f"{et} 頁不應有人物欄位值：{flags}")
            self.assertNotEqual(meta.get("identitySource"), "page")
            results[et] = (all(k in meta for k in PERSON_KEYS))
        self.assertEqual(results["feature"], results["model"],
                         "feature／model 頁型輸出人物欄位的方式要一致（皆輸出或皆不輸出）")

    def test_feature_page_with_person_lines_ignored(self):
        # 非人物頁即使誤寫了欄位行，也不當人物資料輸出
        meta, _ = self.parse(_page(entity_type="feature"), name="feature-with-lines.md")
        self.assertTrue(all(self._absent_or_null(meta).values()),
                        "非人物頁不應輸出人物欄位值")


if __name__ == "__main__":
    unittest.main()
