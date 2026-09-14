"""Tests for scripts/check_css_overrides.py — CSS 靜默覆寫機械閘。

事故來源：2026-09-14 排版改版，同特異度靠源順序決勝的靜默覆寫在一輪內命中六次。
本閘要擋的就是那一類；測試的重點是**方向**——媒體查詢寫在基礎規則之後是正常做法，
寫在之前才是死碼，兩者長得幾乎一樣，不能一起報。

每個測試用假檔（TemporaryDirectory）餵 scan(files=...)，不碰真實 web_reader。
"""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import load_script_module

mod = load_script_module("check_css_overrides")


class _Case(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def css(self, text: str) -> list[Path]:
        p = self.dir / "t.css"
        p.write_text(text, encoding="utf-8")
        return [p]

    def dead(self, text: str) -> list[str]:
        return [d["text"] for d in mod.scan(self.css(text))["dead"]]

    def shorthand(self, text: str) -> list[str]:
        return mod.scan(self.css(text))["shorthand"]


class TestDeadMediaQuery(_Case):
    def test_媒體查詢寫在基礎規則之前是死碼(self):
        """這就是本輪踩六次的形態：改了媒體查詢完全沒反應。"""
        hits = self.dead(
            "@media (max-width: 640px) { .story { padding: 14px 0; } }\n"
            ".story { padding: 21px 0; }\n"
        )
        self.assertEqual(len(hits), 1)
        self.assertIn(".story", hits[0])
        self.assertIn("padding", hits[0])

    def test_媒體查詢寫在基礎規則之後是正常做法(self):
        """方向相反就不該報——否則整份 CSS 的響應式寫法都會被誤擋。"""
        self.assertEqual(
            self.dead(
                ".story { padding: 21px 0; }\n"
                "@media (max-width: 640px) { .story { padding: 14px 0; } }\n"
            ),
            [],
        )

    def test_修飾子在子集上覆寫基礎類別不算死碼(self):
        """@media .story 對 .story--star 元素不生效，但對一般 .story 生效——
        那是 BEM 的正常級聯，不是死碼。只認同一選擇器才不會誤擋整份 CSS。"""
        self.assertEqual(
            self.dead(
                "@media (max-width: 640px) { .story { margin: 0; } }\n"
                ".story--star { margin: 10px 0; }\n"
            ),
            [],
        )

    def test_同一選擇器的媒體覆寫寫在前面才算(self):
        """真正無歧義的形態：同一個選擇器，媒體覆寫排在自己的基礎規則之前。"""
        hits = self.dead(
            "@media (max-width: 640px) { .story--star { margin: 0; } }\n"
            ".story--star { margin: 10px 0; }\n"
        )
        self.assertEqual(len(hits), 1)

    def test_不同屬性不算衝突(self):
        self.assertEqual(
            self.dead(
                "@media (max-width: 640px) { .a { padding: 1px; } }\n"
                ".a { margin: 2px; }\n"
            ),
            [],
        )

    def test_後面那條特異度較高就不是死碼(self):
        """雙類別勝出與源順序無關，不該報。"""
        self.assertEqual(
            self.dead(
                "@media (max-width: 640px) { .a { padding: 1px; } }\n"
                ".a.b { padding: 2px; }\n"
            ),
            [],
        )

    def test_無法判定共同套用時不報(self):
        """保守原則：寧可漏報也不誤報，含後代組合子的選擇器不做推論。"""
        self.assertEqual(
            self.dead(
                "@media (max-width: 640px) { .wrap .a { padding: 1px; } }\n"
                ".box .a { padding: 2px; }\n"
            ),
            [],
        )

    def test_keyframes_不被當成規則(self):
        """@keyframes 裡的 0%/100% 不是選擇器，混進來會產生假命中。"""
        self.assertEqual(
            self.dead(
                "@keyframes pulse { 0% { padding: 1px; } 100% { padding: 2px; } }\n"
                ".a { padding: 3px; }\n"
            ),
            [],
        )

    def test_註解不影響行號(self):
        hits = self.dead(
            "/* 一段\n   跨行註解 */\n"
            "@media (max-width: 640px) { .a { padding: 1px; } }\n"
            ".a { padding: 2px; }\n"
        )
        self.assertEqual(len(hits), 1)
        self.assertIn(":3", hits[0])


class TestShorthandAxis(_Case):
    def test_簡寫覆寫會洗掉水平值(self):
        """本輪實例：.story 的 padding 簡寫把 .story--star 的 18px 水平內距歸零。"""
        hits = self.shorthand(
            ".story--star { padding: 21px 18px; }\n"
            "@media (max-width: 640px) { .story { padding: 14px 0; } }\n"
        )
        self.assertEqual(len(hits), 1)
        self.assertIn("padding-block", hits[0])

    def test_長寫不觸發(self):
        """padding-block 只寫上下，正是本閘要推廣的修法。"""
        self.assertEqual(
            self.shorthand(
                ".story--star { padding: 21px 18px; }\n"
                "@media (max-width: 640px) { .story { padding-block: 14px; } }\n"
            ),
            [],
        )

    def test_水平值相同不觸發(self):
        self.assertEqual(
            self.shorthand(
                ".story--star { padding: 21px 18px; }\n"
                ".story { padding: 14px 18px; }\n"
            ),
            [],
        )


class TestSpecificity(_Case):
    def test_特異度計算(self):
        self.assertEqual(mod.specificity(".a"), (0, 1, 0))
        self.assertEqual(mod.specificity(".a.b"), (0, 2, 0))
        self.assertEqual(mod.specificity("#x .a"), (1, 1, 0))
        self.assertEqual(mod.specificity(".a:hover"), (0, 2, 0))

    def test_共同套用判斷(self):
        self.assertTrue(mod.co_apply(".story", ".story--star"))
        self.assertTrue(mod.co_apply(".a.b", ".a"))
        self.assertFalse(mod.co_apply(".a", ".b"))
        self.assertFalse(mod.co_apply(".wrap .a", ".box .a"))


class TestBaseline(_Case):
    def test_基線內的不算新增(self):
        files = self.css(
            "@media (max-width: 640px) { .a { padding: 1px; } }\n"
            ".a { padding: 2px; }\n"
        )
        dead = mod.scan(files)["dead"]
        self.assertEqual(len(dead), 1)
        fp = dead[0]["fp"]
        # 指紋不含行號：在前面插入空行後仍相同，才不會一改版就整批變「新增」
        files[0].write_text(
            "\n\n@media (max-width: 640px) { .a { padding: 1px; } }\n.a { padding: 2px; }\n",
            encoding="utf-8",
        )
        self.assertEqual(mod.scan(files)["dead"][0]["fp"], fp)


if __name__ == "__main__":
    unittest.main()
