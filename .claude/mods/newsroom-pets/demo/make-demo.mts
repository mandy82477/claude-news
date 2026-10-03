// 用 mod 實際的 actions.ts／lib.ts 模擬一輪 /news-pipeline，把每格畫面算好寫成可播放的 HTML。
// 跑法（Node 22+）：node --experimental-strip-types demo/make-demo.mts
// 產出：demo/pipeline-demo.html（純靜態，雙擊即可開）

import { writeFileSync } from 'node:fs'
import { actionOf, actionPixels, outcomeOf, thinkingPixels, VERB } from '../hooks/actions.ts'
import { EDITOR, HELPER, reporterOf, sleepingPixels, toRows } from '../hooks/lib.ts'
import type { Who } from '../hooks/lib.ts'

const R = (cat: string) => reporterOf(`你是 CLAUDE_NEWS wiki 的「${cat}」記者。`) as Who
const FEATURES = R('功能'), MODELS = R('模型'), COMMUNITY = R('社群'), COMMERCIAL = R('商業')

type Ev = { who: Who; tool: string; input: any; rel?: string; result?: any; note: string }
// 一輪 pipeline 的典型工具呼叫（取自 news-pipeline／wiki-ingest／web-publish 的實際步驟）
const PHASES: { title: string; events: Ev[][] }[] = [
  { title: 'Phase A　抓料、寫日報（背景 pipeline agent）', events: [
    [{ who: HELPER, tool: 'Bash', input: { command: 'python -m news_aggregator.main --gather-only' }, note: '抓今天的新聞' }],
    [{ who: HELPER, tool: 'Write', input: {}, rel: 'news/2026-10-03.md', note: '寫日報' }],
    [{ who: HELPER, tool: 'Bash', input: { command: 'git commit -m "news: daily digest"' }, note: '日報 commit' }],
  ] },
  { title: 'Phase B　分類、派記者寫 wiki', events: [
    [{ who: EDITOR, tool: 'Read', input: {}, rel: 'news/2026-10-03.md', note: '主編讀日報' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'python scripts/build_ingest_packets.py' }, note: '分類、產派工包' }],
    [{ who: EDITOR, tool: 'Agent', input: { description: '六位記者' }, note: '吹哨派工' }],
    [
      { who: FEATURES, tool: 'Read', input: {}, rel: 'wiki/entities/claude-code.md', note: '' },
      { who: MODELS, tool: 'Grep', input: { pattern: 'Opus 5.5' }, note: '' },
      { who: COMMUNITY, tool: 'Read', input: {}, rel: 'wiki/topics/community-tech-tools.md', note: '記者們先翻閱、搜尋' },
    ],
    [
      { who: FEATURES, tool: 'Edit', input: {}, rel: 'wiki/entities/claude-code.md', note: '' },
      { who: MODELS, tool: 'Edit', input: {}, rel: 'wiki/entities/opus-5-5.md', note: '' },
      { who: COMMUNITY, tool: 'Edit', input: {}, rel: 'wiki/topics/community-tech-tools.md', note: '' },
      { who: COMMERCIAL, tool: 'Edit', input: {}, rel: 'wiki/entities/pricing.md', note: '四位記者同時寫' },
    ],
    [{ who: FEATURES, tool: 'WebFetch', input: { url: 'https://code.claude.com/docs' }, result: { deny: '記者無 web 工具' }, note: '記者想上網查 → 被 hook 擋，冒汗' }],
    [{ who: FEATURES, tool: 'Edit', input: {}, rel: 'wiki/feature-radar.md', note: '雷達掃描' }],
    [{ who: EDITOR, tool: 'Edit', input: {}, rel: 'wiki/index.md', note: '主編整理書架' }],
    [{ who: EDITOR, tool: 'Edit', input: {}, rel: 'wiki/log.md', note: '主編寫日誌' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'python scripts/ingest_gate.py --date 2026-10-03' }, result: { stdout: '❌ ingest_gate：1 道內容閘紅' }, note: '內容閘紅 → 冒汗' }],
    [{ who: EDITOR, tool: 'Edit', input: {}, rel: 'wiki/topics/market-signals.md', note: '修好紅燈' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'python scripts/ingest_gate.py --date 2026-10-03' }, result: { stdout: '✅ ingest_gate：9 道內容閘全綠' }, note: '重跑 → 全綠比讚' }],
  ] },
  { title: 'Phase C　收尾上線', events: [
    [{ who: EDITOR, tool: 'Bash', input: { command: 'git add wiki/ && git commit -m "wiki: auto-ingest"' }, note: 'wiki 蓋章' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'python scripts/run_tests.py > /tmp/rt.txt' }, result: { stdout: 'OK: 1162 個測試案例全數通過' }, note: '全套測試' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'python scripts/build_web.py' }, note: '印網站' }],
    [{ who: EDITOR, tool: 'Bash', input: { command: 'git push' }, note: '射紙飛機上線' }],
  ] },
]

type Seg = { text: string; color?: string; backgroundColor?: string }
type Card = { name: string; verb: string; rows: Seg[][] }
type Frame = { phase: string; note: string; cards: Card[]; nap?: { label: string; rows: Seg[][] } }

const frames: Frame[] = []
let tick = 0
const card = (who: Who, action: any, label: string): Card =>
  ({ name: who.badge + ' ' + who.name, verb: VERB[action as keyof typeof VERB] + (label ? ' ' + label : ''), rows: toRows(actionPixels(who, action, tick)) })

// 開場：睡覺 → 收到 prompt 醒著想
for (let i = 0; i < 6; i++, tick++) frames.push({ phase: '平常', note: '沒事時主編縮在右下角睡覺（2 行）', cards: [], nap: { label: '主編 zZ', rows: toRows(sleepingPixels(EDITOR, tick)) } })
for (let i = 0; i < 4; i++, tick++) frames.push({ phase: '收到 /news-pipeline', note: 'Claude 在想、還沒用工具：醒著坐在角落', cards: [], nap: { label: '主編 …', rows: toRows(thinkingPixels(EDITOR, tick)) } })

for (const ph of PHASES) {
  for (const group of ph.events) {
    const starts = group.map((ev) => ({ ev, ...actionOf(ev.tool, ev.input, ev.rel ?? null) }))
    const note = group.map((g) => g.note).filter(Boolean).join('；')
    // 動作進行中 6 格
    for (let i = 0; i < 6; i++, tick++) frames.push({ phase: ph.title, note, cards: starts.map((s) => card(s.ev.who, s.action, s.label)) })
    // 有結果動作的（被擋、閘紅綠）再演 5 格
    const outs = starts.map((s) => ({ ...s, out: outcomeOf(s.action, s.ev.result ?? null) }))
    if (outs.some((o) => o.out)) {
      for (let i = 0; i < 5; i++, tick++) frames.push({ phase: ph.title, note, cards: outs.map((o) => card(o.ev.who, o.out ?? o.action, o.label)) })
    }
  }
}
for (let i = 0; i < 8; i++, tick++) frames.push({ phase: '收工', note: '大家散會，主編回去睡', cards: [], nap: { label: '主編 zZ', rows: toRows(sleepingPixels(EDITOR, tick)) } })

const html = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>小編輯部 demo</title>
<style>
:root{--bg:#faf9f5;--fg:#1f1e1d;--mut:#73726c;--line:#e0ded6;--term:#f3f1ea}
@media (prefers-color-scheme:dark){:root{--bg:#1f1e1d;--fg:#f0eee6;--mut:#a3a199;--line:#3d3c38;--term:#2a2927}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:system-ui,"Noto Sans TC",sans-serif;padding:24px 16px}
main{max-width:860px;margin:0 auto}
h1{font-size:20px;font-weight:500;margin:0 0 4px}
p.sub{color:var(--mut);font-size:14px;margin:0 0 16px}
.term{background:var(--term);border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-family:ui-monospace,Consolas,monospace}
.band{display:flex;gap:16px;min-height:96px;align-items:flex-end;flex-wrap:wrap}
.band.nap{justify-content:flex-end}
.px{white-space:pre;font-size:18px;line-height:1}
.nm{font-size:12px;margin-top:4px;font-weight:600}
.vb{font-size:11px;color:var(--mut);max-width:150px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.prompt{border-top:1px solid var(--line);margin-top:12px;padding-top:8px;color:var(--mut);font-size:13px}
.ctl{display:flex;gap:8px;align-items:center;margin:14px 0;flex-wrap:wrap}
button{font:inherit;font-size:14px;padding:6px 12px;border-radius:8px;border:1px solid var(--line);background:transparent;color:var(--fg);cursor:pointer}
input[type=range]{flex:1;min-width:160px}
.phase{font-size:15px;font-weight:500;margin:0}
.note{font-size:14px;color:var(--mut);margin:4px 0 0;min-height:20px}
</style>
<main>
<h1>小編輯部：一輪 /news-pipeline 會看到什麼</h1>
<p class="sub">畫面由 mod 實際的 actions.ts 算出（${frames.length} 格），終端機裡長這樣，只是放大了。</p>
<p class="phase" id="ph"></p><p class="note" id="nt"></p>
<div class="term"><div class="band" id="band"></div><div class="prompt">&gt; </div></div>
<div class="ctl"><button id="pp">暫停</button><input type="range" id="sl" min="0" max="${frames.length - 1}" value="0"><span id="ix" style="font-size:12px;color:var(--mut)"></span></div>
</main>
<script>
const F=${JSON.stringify(frames)};
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const row=segs=>segs.map(s=>{let st='';if(s.color)st+='color:'+s.color+';';if(s.backgroundColor)st+='background:'+s.backgroundColor+';';return st?'<span style="'+st+'">'+esc(s.text)+'</span>':esc(s.text)}).join('');
const art=rows=>'<div class="px">'+rows.map(row).join('\\n')+'</div>';
let i=0,play=true;
function draw(){const f=F[i];ph.textContent=f.phase;nt.textContent=f.note;sl.value=i;ix.textContent=(i+1)+' / '+F.length;
 if(f.nap){band.className='band nap';band.innerHTML='<div style="display:flex;gap:8px;align-items:flex-end"><span class="vb">'+esc(f.nap.label)+'</span>'+art(f.nap.rows)+'</div>'}
 else{band.className='band';band.innerHTML=f.cards.map(c=>'<div>'+art(c.rows)+'<div class="nm">'+esc(c.name)+'</div><div class="vb">'+esc(c.verb)+'</div></div>').join('')}}
pp.onclick=()=>{play=!play;pp.textContent=play?'暫停':'播放'};
sl.oninput=()=>{i=+sl.value;draw()};
setInterval(()=>{if(play){i=(i+1)%F.length;draw()}},320);draw();
</script>`
writeFileSync(new URL('./pipeline-demo.html', import.meta.url), html)
console.log(`OK: demo/pipeline-demo.html（${frames.length} 格）`)
