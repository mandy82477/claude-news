// 角色帽子＋全部動作的圖鑑，畫格由 mod 實際的 lib.ts／actions.ts 算出。
// 跑法（Node 22+）：node --experimental-strip-types demo/make-gallery.mts → demo/gallery.html
import { writeFileSync } from 'node:fs'
import { actionPixels, VERB } from '../hooks/actions.ts'
import type { Action } from '../hooks/actions.ts'
import { EDITOR, reporterOf, toRows } from '../hooks/lib.ts'
import type { Who } from '../hooks/lib.ts'

const cats = ['功能', '模型', '商業', '安全政策', '社群', '人物', '投資分析', '開發實務', '分類複核']
const cast: Who[] = [EDITOR, ...cats.map((c) => reporterOf(`你是 CLAUDE_NEWS wiki 的「${c}」記者`) as Who)]
const HATNAME: Record<string, string> = {
  fedora: '紳士帽', hardhat: '工地安全帽', antenna: '機器人天線', tophat: '高禮帽', police: '警帽＋徽章',
  cap: '反戴棒球帽', newsboy: '報童帽＋記者證', visor: '會計遮陽帽', beanie: '毛帽＋毛球', deerstalker: '偵探帽',
}
const WHEN: Record<Action, string> = {
  write: 'Edit／Write wiki 頁', read: 'Read', search: 'Grep／Glob／wiki_search', log: 'Edit wiki/log.md',
  shelf: 'Edit wiki/index.md', radar: 'Edit feature-radar.md', press: 'Write news/、build_web', phone: 'WebFetch／WebSearch',
  whistle: '呼叫 Agent', check: 'run_tests／ingest_gate／check_*', thumbs: '檢查腳本綠燈', red: '檢查腳本紅燈',
  sweat: '被 hook 擋下或出錯', stamp: 'git commit', plane: 'git push', sweep: 'lint 腳本', busy: '其他 shell 指令',
}
const FR = 8
const castFrames = cast.map((w) => ({ name: w.badge + ' ' + w.name, hat: HATNAME[w.hat], f: [...Array(FR)].map((_, t) => toRows(actionPixels(w, 'write', t))) }))
const acts = (Object.keys(VERB) as Action[])
const actFrames = acts.map((a, i) => ({ verb: VERB[a], when: WHEN[a], f: [...Array(FR)].map((_, t) => toRows(actionPixels(cast[i % cast.length], a, t))) }))

const html = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>小編輯部圖鑑</title>
<style>:root{--bg:#faf9f5;--fg:#1f1e1d;--mut:#73726c;--line:#e0ded6;--card:#f3f1ea}@media (prefers-color-scheme:dark){:root{--bg:#1f1e1d;--fg:#f0eee6;--mut:#a3a199;--line:#3d3c38;--card:#2a2927}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:system-ui,"Noto Sans TC",sans-serif;padding:24px 16px}main{max-width:980px;margin:0 auto}
h1{font-size:20px;font-weight:500;margin:0 0 4px}h2{font-size:16px;font-weight:500;margin:24px 0 8px}p{color:var(--mut);font-size:14px;margin:0 0 12px}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px}.c{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}
.px{font-family:ui-monospace,Consolas,monospace;white-space:pre;font-size:16px;line-height:1}.px span{display:inline-block;height:1em;line-height:1em;vertical-align:top}.t{font-size:13px;font-weight:600;margin-top:8px}.d{font-size:12px;color:var(--mut)}</style>
<main><h1>小編輯部圖鑑</h1><p>每格由 mod 實際的 lib.ts／actions.ts 算出；終端機裡每格字是上下兩個像素，這裡放大顯示。</p>
<h2>角色與帽子</h2><div class="g" id="cast"></div><h2>動作與道具</h2><div class="g" id="acts"></div></main>
<script>const C=${JSON.stringify(castFrames)},A=${JSON.stringify(actFrames)};
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const row=segs=>segs.map(s=>{let st='';if(s.color)st+='color:'+s.color+';';if(s.backgroundColor)st+='background:'+s.backgroundColor+';';return st?'<span style="'+st+'">'+esc(s.text)+'</span>':esc(s.text)}).join('');
cast.innerHTML=C.map((c,i)=>'<div class="c"><div class="px" id="c'+i+'"></div><div class="t">'+esc(c.name)+'</div><div class="d">'+esc(c.hat)+'</div></div>').join('');
acts.innerHTML=A.map((a,i)=>'<div class="c"><div class="px" id="a'+i+'"></div><div class="t">'+esc(a.verb)+'</div><div class="d">'+esc(a.when)+'</div></div>').join('');
let t=0;function draw(){C.forEach((c,i)=>document.getElementById('c'+i).innerHTML=c.f[t%c.f.length].map(row).join('\\n'));A.forEach((a,i)=>document.getElementById('a'+i).innerHTML=a.f[t%a.f.length].map(row).join('\\n'));t++}draw();setInterval(draw,340);</script>`
writeFileSync(new URL('./gallery.html', import.meta.url), html)
console.log(`OK: demo/gallery.html（${cast.length} 個角色、${acts.length} 種動作）`)
