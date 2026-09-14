"""Tests for scripts/wiki_search.py — wiki 全文檢索＋同義叢集＋圖擴散。

單元測試用假檔（`TemporaryDirectory`）餵 `Index.from_files(...)`；最後一組是真實
wiki 的回歸：2026-09-14 問「agent 視覺化」漏掉「可觀測性／協調地圖」兩頁，
修法是全文 BM25＋同義叢集，這組測試守住那次漏掉的兩頁不再漏。

假語料的角色（每個測試只動用其中幾頁）：
  topics/gap       字面命中頁——正文寫「多平行 agent 即時可觀測性／協調地圖」
  topics/patterns  字面命中頁——正文寫「視覺化」＋ 指向 trends 的正文 wikilink
  topics/trends    圖擴散目標——正文沒有任何查詢詞，但被 gap 與 patterns 正文指到
  topics/tpl       樣板區陷阱——只在「## 相關實體」樣板區指向 gap，不得靠圖被撈回
  topics/big       大頁陷阱——40 段都寫 agent 工具，段數多但每段都弱
  topics/other     亂問陷阱——含「量子」「麵包」零碎 bigram
  index            樞紐——含所有查詢詞且指向所有頁，必須被索引與圖同時排除
  log              樞紐——同 index，另一個必須排除的樞紐頁
gap 正文另含版號 v2.1.211，用來測整詞命中版號、不誤觸子字串叢集。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import REPO_ROOT, load_script_module

mod = load_script_module("wiki_search")

CLUSTERS = [["視覺化", "可觀測性", "儀表板", "live map"], ["subagent", "子 agent"]]


class TestTokenize(unittest.TestCase):
    def test_cjk_bigram_and_latin_word(self):
        self.assertEqual(mod.tokenize("可觀測性 v2.1.211"), ["可觀", "觀測", "測性", "v2.1.211"])

    def test_single_cjk_char_kept_and_hyphen_flag_kept_whole(self):
        self.assertEqual(mod.tokenize("多 --forward-subagent-text"), ["多", "forward-subagent-text"])


class TestExpandQuery(unittest.TestCase):
    def test_cluster_hit_adds_lower_weight_tokens_and_concept_map(self):
        weights, hits, concept = mod.expand_query("agent 視覺化", CLUSTERS)
        self.assertEqual(hits, ["視覺化"])
        self.assertEqual(weights["視覺"], 1.0)
        self.assertEqual(weights["可觀"], mod.ALIAS_WEIGHT)
        self.assertIn("可觀", concept["視覺"])

    def test_grammar_bigrams_dropped_from_query_side_only(self):
        weights, _, _ = mod.expand_query("視覺化工具有哪些", [])
        self.assertTrue({"視覺", "覺化", "化工", "工具"} <= set(weights))
        self.assertFalse({"有哪", "哪些", "具有"} & set(weights))
        self.assertEqual(mod.content_tokens(["的", "有哪"]), ["的", "有哪"])

    def test_content_tokens_filters_stopwords_when_content_present(self):
        # 混了實詞時，虛字 bigram 被剔掉，只留實詞——不是「全剔光才原樣回傳」那條分支。
        self.assertEqual(mod.content_tokens(["視覺", "有哪"]), ["視覺"])

    def test_found_rule_ratio_or_three_content_words(self):
        self.assertTrue(mod.is_found(0.1, 3))
        self.assertTrue(mod.is_found(0.3, 1))
        self.assertFalse(mod.is_found(0.29, 2))

    def test_is_found_uses_named_thresholds_not_just_literals(self):
        # 鎖住常數本身（MIN_COVERAGE / MIN_MATCHED），不是只鎖 0.3／3 這兩個數字。
        self.assertTrue(mod.is_found(mod.MIN_COVERAGE, 0))
        self.assertTrue(mod.is_found(0.0, mod.MIN_MATCHED))
        self.assertFalse(mod.is_found(mod.MIN_COVERAGE - 0.01, mod.MIN_MATCHED - 1))

    def test_latin_alias_needs_word_boundary(self):
        _, hits, _ = mod.expand_query("forward-subagent-text", CLUSTERS)
        self.assertEqual(hits, [])
        _, hits, _ = mod.expand_query("subagent 怎麼派", CLUSTERS)
        self.assertEqual(hits, ["subagent"])


class _Corpus(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        (self.dir / "topics").mkdir()
        self.write("topics/gap.md",
                   "---\nx: 1\n---\n# 缺口\n\n## 矩陣\n\n多平行 agent 即時可觀測性／協調地圖，官方無對應，"
                   "趨勢見 [[topics/trends]]。旗標 --forward-subagent-text 提供資料來源，版本 v2.1.211 起支援。\n")
        self.write("topics/patterns.md",
                   "# 模式\n\n## 地圖\n\n以視覺化地圖呈現多個平行 agent 的狀態，宏觀層見 [[topics/trends]]。\n")
        self.write("topics/trends.md",
                   "# 趨勢\n\n## 趨勢六\n\n六個實作殊途同歸，這條線已成形。\n")
        self.write("topics/tpl.md",
                   "# 樣板頁\n\n## 正文\n\n本頁談別的事。\n\n## 相關實體\n\n- [[topics/gap]]\n- [[topics/patterns]]\n")
        self.write("topics/big.md",
                   "# 大頁\n\n" + "".join(f"## 段{i}\n\nagent 工具 agent 工具 定價。\n\n" for i in range(40)))
        self.write("topics/other.md", "# 別頁\n\n## 節\n\n後量子密碼與麵包屑筆記。\n")
        self.write("index.md",
                   "# 目錄\n\n視覺化 可觀測性 協調地圖 agent [[topics/gap]] [[topics/trends]] [[topics/other]]\n")
        self.write("log.md",
                   "# 日誌\n\n視覺化 可觀測性 協調地圖 agent [[topics/gap]] [[topics/trends]] [[topics/other]]\n")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> Path:
        p = self.dir / rel
        p.write_text(text, encoding="utf-8")
        return p

    def index(self):
        return mod.Index.from_files(mod.iter_wiki_files(self.dir), self.dir)

    def pages(self, result):
        return [e["page"] for e in result["pages"]]


class TestIndexing(_Corpus):
    def test_hub_pages_excluded_from_index_and_graph(self):
        idx = self.index()
        pages_in_index = {s.page for s in idx.sections}
        for hub in ("index", "log"):
            self.assertNotIn(hub, pages_in_index)
            self.assertNotIn(hub, idx.adjacency)
            self.assertNotIn(hub, idx.adjacency.get("topics/gap", set()))

    def test_line_numbers_include_frontmatter_offset(self):
        idx = self.index()
        gap = [s for s in idx.sections if s.page == "topics/gap" and s.heading == "矩陣"][0]
        self.assertEqual(gap.line, 6)

    def test_template_zone_links_do_not_form_graph_edges(self):
        idx = self.index()
        self.assertNotIn("topics/tpl", idx.adjacency.get("topics/gap", set()))
        self.assertEqual(idx.adjacency["topics/trends"], {"topics/gap", "topics/patterns"})


class TestLexicalAndAlias(_Corpus):
    def test_literal_hit_is_tagged_and_points_to_section(self):
        r = mod.search("協調地圖", self.index(), [], top=3)
        top = r["pages"][0]
        self.assertEqual(top["page"], "topics/gap")
        self.assertEqual(top["source"], "字面命中")
        self.assertEqual(top["sections"][0]["heading"], "矩陣")
        self.assertTrue(r["found"])
        self.assertEqual(top["via"], [])

    def test_page_and_section_dicts_carry_found_and_matched_fields(self):
        r = mod.search("協調地圖", self.index(), [], top=3)
        top = r["pages"][0]
        self.assertIn("matched", top)
        self.assertIn("found", top)
        self.assertEqual(top["found"], mod.is_found(top["coverage"], top["matched"]))
        sec = top["sections"][0]
        self.assertIn("matched", sec)
        self.assertIn("found", sec)
        self.assertEqual(sec["found"], mod.is_found(sec["coverage"], sec["matched"]))

    def test_version_number_literal_hit_without_substring_cluster_noise(self):
        r = mod.search("v2.1.211", self.index(), CLUSTERS, top=3)
        self.assertEqual(r["alias_hits"], [])
        self.assertEqual(self.pages(r)[0], "topics/gap")
        self.assertEqual(r["pages"][0]["coverage"], 1.0)

    def test_alias_bridges_wording_gap(self):
        r = mod.search("agent 視覺化", self.index(), CLUSTERS, top=3)
        self.assertEqual(self.pages(r)[:2], ["topics/patterns", "topics/gap"])
        self.assertGreaterEqual(r["pages"][1]["coverage"], mod.MIN_COVERAGE)

    def test_no_alias_flag_drops_the_bridge(self):
        r = mod.search("agent 視覺化", self.index(), [], top=3)
        self.assertEqual(self.pages(r)[0], "topics/patterns")
        gap = [e for e in r["pages"] if e["page"] == "topics/gap"]
        self.assertTrue(not gap or gap[0]["coverage"] < 1.0)

    def test_latin_identifier_hits_whole_token_without_alias_noise(self):
        r = mod.search("forward-subagent-text", self.index(), CLUSTERS, top=3)
        self.assertEqual(r["alias_hits"], [])
        self.assertEqual(self.pages(r)[0], "topics/gap")
        self.assertEqual(r["pages"][0]["coverage"], 1.0)

    def test_big_page_does_not_win_by_section_count(self):
        r = mod.search("agent 可觀測性", self.index(), [], top=3)
        self.assertEqual(self.pages(r)[0], "topics/gap")

    def test_long_natural_language_query_still_finds_answer(self):
        q = "agent 相關的視覺化工具有哪些（多 agent 協作、執行狀態、輸出用視覺化呈現）"
        r = mod.search(q, self.index(), CLUSTERS, top=3)
        self.assertTrue({"topics/gap", "topics/patterns"} <= set(self.pages(r)))
        self.assertTrue(r["found"])

    def test_scattered_bigrams_are_zero_hit_and_hint_expand(self):
        r = mod.search("量子糾纏烤麵包", self.index(), [], top=3)
        self.assertFalse(r["found"])
        text = mod.render(r, False)
        self.assertIn("零命中", text)
        self.assertIn("--expand", text)


class TestGraphExpansion(_Corpus):
    def test_page_without_any_query_word_is_recovered_via_seeds(self):
        idx = self.index()
        plain = mod.search("agent 視覺化", idx, CLUSTERS, top=6)
        self.assertNotIn("topics/trends", self.pages(plain))
        r = mod.search("agent 視覺化", idx, CLUSTERS, top=6, expand=True)
        trends = [e for e in r["pages"] if e["page"] == "topics/trends"][0]
        self.assertEqual(trends["source"], "圖擴散")
        self.assertEqual(sorted(trends["via"]), ["topics/gap", "topics/patterns"])
        self.assertIn("種子", mod.render(r, False))

    def test_template_only_neighbour_is_not_recovered(self):
        r = mod.search("agent 視覺化", self.index(), CLUSTERS, top=6, expand=True)
        self.assertNotIn("topics/tpl", self.pages(r))

    def test_lexical_hits_keep_their_score_no_double_counting(self):
        idx = self.index()
        plain = mod.search("agent 視覺化", idx, CLUSTERS, top=6)
        exp = mod.search("agent 視覺化", idx, CLUSTERS, top=6, expand=True)
        for e in exp["pages"]:
            if e["source"] != "圖擴散":
                self.assertEqual(e["score"], [p for p in plain["pages"] if p["page"] == e["page"]][0]["score"])

    def test_expanded_pages_capped_at_half_of_top(self):
        r = mod.search("agent 視覺化", self.index(), CLUSTERS, top=2, expand=True)
        self.assertLessEqual(sum(e["source"] == "圖擴散" for e in r["pages"]), 1)

    def test_no_seeds_means_no_expansion(self):
        r = mod.search("量子糾纏烤麵包", self.index(), [], top=3, expand=True)
        self.assertFalse(r["found"])
        self.assertFalse(any(e["source"] == "圖擴散" for e in r["pages"]))
        self.assertNotIn("--expand", mod.render(r, False))

    def test_render_suggests_expand_when_candidates_are_thin(self):
        r = mod.search("協調地圖", self.index(), [], top=3)
        self.assertIn("--expand", mod.render(r, False))


@unittest.skipUnless((REPO_ROOT / "wiki" / "topics" / "official-community-gap.md").exists(), "real wiki absent")
class TestRealWikiRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx = mod.Index.from_files(mod.iter_wiki_files())
        cls.aliases = mod.load_aliases()

    def test_2026_09_14_agent_visualization_query_surfaces_both_pages(self):
        r = mod.search("多 agent 視覺化工具", self.idx, self.aliases, top=6)
        found = set(e["page"] for e in r["pages"])
        self.assertTrue({"topics/official-community-gap", "topics/community-pattern-trends"} <= found, found)

    def test_expand_on_real_graph_tags_sources_and_keeps_seeds_first(self):
        r = mod.search("多 agent 視覺化工具", self.idx, self.aliases, top=12, expand=True)
        self.assertEqual(r["pages"][0]["source"], "字面命中")
        for e in r["pages"]:
            if e["source"] == "圖擴散":
                self.assertTrue(e["via"])


if __name__ == "__main__":
    unittest.main()
