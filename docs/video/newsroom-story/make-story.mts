// 「小編輯部」介紹動畫的產生器：角色、帽子、道具的像素由 mod 實際的 lib.ts／actions.ts 算出，
// 劇本與場景在 story-runtime.js。跑法（Node 22+）：
//   node --experimental-strip-types docs/video/newsroom-story/make-story.mts
// 產出：newsroom-story.html（完整版約 2 分半）與 newsroom-story-1min.html（精簡版約 1 分鐘），單檔、雙擊即可播放

import { readFileSync, writeFileSync } from 'node:fs'
import { actionPixels, VERB } from '../../../.claude/mods/newsroom-pets/hooks/actions.ts'
import type { Action } from '../../../.claude/mods/newsroom-pets/hooks/actions.ts'
import { bodyPixels, EDITOR, HELPER, reporterOf, sleepingPixels } from '../../../.claude/mods/newsroom-pets/hooks/lib.ts'
import type { Who } from '../../../.claude/mods/newsroom-pets/hooks/lib.ts'

const CATS = ['功能', '模型', '商業', '安全政策', '社群', '人物', '投資分析', '開發實務', '分類複核']
const KEYS = ['features', 'models', 'commercial', 'policy', 'community', 'people', 'market', 'devpractice', 'classify']
const cast: Record<string, Who> = { editor: EDITOR, helper: HELPER }
CATS.forEach((c, i) => { cast[KEYS[i]] = reporterOf(`你是 CLAUDE_NEWS wiki 的「${c}」記者`) as Who })

// 調色盤壓縮：每種顏色一個字元，'.' 透明
const palette: string[] = []
const code = (c: string | null) => {
  if (!c) return '.'
  let i = palette.indexOf(c)
  if (i < 0) { palette.push(c); i = palette.length - 1 }
  return String.fromCharCode(65 + i) // A, B, C…（色數遠少於 26）
}
const pack = (g: (string | null)[][]) => g.map((row) => row.map(code).join(''))

const FR = 8
const chars: Record<string, any> = {}
for (const [key, who] of Object.entries(cast)) {
  chars[key] = {
    name: who.name, badge: who.badge,
    wave: [...Array(FR)].map((_, t) => pack(bodyPixels(who, t, true))),
    still: [...Array(FR)].map((_, t) => pack(bodyPixels(who, t, false))),
    glasses: [...Array(FR)].map((_, t) => pack(bodyPixels(who, t, false, false, true))),
    sleep: [...Array(6)].map((_, t) => pack(sleepingPixels(who, t))),
  }
}
const props: Record<string, string[][]> = {}
for (const a of Object.keys(VERB) as Action[]) {
  props[a] = [...Array(FR)].map((_, t) => pack(actionPixels(EDITOR, a, t).map((row) => row.slice(10))))
}

const runtime = readFileSync(new URL('./story-runtime.js', import.meta.url), 'utf8')
const page = (short: boolean) => `<!doctype html>
<html lang="zh-Hant">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Claude News 小編輯部${short ? '（1 分鐘版）' : ''}</title>
<style>
:root{--bg:#f4f1e8;--fg:#1f1e1d;--mut:#5f5e5a;--line:#d8d4c8;--btn:#ffffff}
@media (prefers-color-scheme:dark){:root{--bg:#1c1b19;--fg:#f0eee6;--mut:#b4b2a9;--line:#3d3c38;--btn:#2a2927}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:"Noto Sans TC","Microsoft JhengHei",system-ui,sans-serif}
main{max-width:1600px;margin:0 auto;padding:20px 16px 32px}
h1{font-size:24px;font-weight:600;margin:0 0 6px}
p.lead{font-size:17px;color:var(--mut);margin:0 0 16px;line-height:1.6}
.stage{position:relative;width:100%;aspect-ratio:16/9;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#f7f3e8}
canvas{width:100%;height:100%;display:block}
.bar{display:flex;gap:10px;align-items:center;margin:14px 0 10px;flex-wrap:wrap}
button{font:inherit;font-size:17px;padding:8px 16px;border-radius:10px;border:1px solid var(--line);background:var(--btn);color:var(--fg);cursor:pointer}
button.on{outline:2px solid #D85A30}
input[type=range]{flex:1;min-width:220px;accent-color:#D85A30}
#clock{font-size:16px;color:var(--mut);font-variant-numeric:tabular-nums;min-width:96px}
.chapters{display:flex;gap:8px;flex-wrap:wrap}
.chapters button{font-size:16px;padding:6px 12px}
</style>
<main>
<h1>Claude News 小編輯部：一份日報怎麼變成會查證的知識庫</h1>
<p class="lead">${short ? '約 1 分鐘精簡版' : '約 2 分半完整版'}。主角是本機 mod「newsroom-pets」裡的同一批角色。空白鍵播放／暫停，左右鍵跳 5 秒。</p>
<div class="stage"><canvas id="cv" width="1920" height="1080" aria-label="小編輯部介紹動畫"></canvas></div>
<div class="bar"><button id="pp">⏸ 暫停</button><input type="range" id="sl" min="0" max="1000" value="0" aria-label="進度"><span id="clock"></span></div>
<div class="chapters" id="ch"></div>
</main>
<script>
const SHORT=${short};
const PALETTE=${JSON.stringify(palette)};
const CHARS=${JSON.stringify(chars)};
const PROPS=${JSON.stringify(props)};
${runtime}
</script>
</html>
`
writeFileSync(new URL('./newsroom-story.html', import.meta.url), page(false))
writeFileSync(new URL('./newsroom-story-1min.html', import.meta.url), page(true))
console.log(`OK: newsroom-story.html＋newsroom-story-1min.html（${Object.keys(chars).length} 個角色、${Object.keys(props).length} 種道具、${palette.length} 色）`)
