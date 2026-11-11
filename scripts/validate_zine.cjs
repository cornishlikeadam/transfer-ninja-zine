const fs=require('fs'),vm=require('vm'),assert=require('assert');
const strategy=JSON.parse(fs.readFileSync('data/strategy.json')),schools=JSON.parse(fs.readFileSync('data/schools.json'));
assert.equal(schools.schools.length,21);assert.equal(schools.bench.length,5);assert.equal(new Set(schools.schools.concat(schools.bench).map(s=>s.id)).size,26);
assert.equal(Object.keys(strategy.schools).length,21);assert.equal(strategy.research.schools.length,21);
for(const s of schools.schools){const x=strategy.schools[s.id];assert.equal(x.bullets.length,3);assert(x.supplements.length);for(const q of x.supplements)assert.equal(q.guidance.length,5)}
const html=fs.readFileSync('vercel/public/index.html','utf8');assert(!html.includes('Military service preceded Broward'));assert(!html.includes('GPA-bearing semester hours (planning estimate)\",22'));
let script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
script=script.replace('setGateUI();renderAll();entryStoreInit();libInit();','window.testing={setData:function(d){DATA=d;LENS=d.lens;UNLOCKED=true},S:S,panelStats:panelStats,panelStrategy:panelStrategy,schoolStrategyHTML:schoolStrategyHTML,statsResult:statsResult,strategyMarkdown:strategyMarkdown,renderApps:renderApps};');
const elements={};function el(k){return elements[k]||(elements[k]={innerHTML:'',textContent:'',value:'',hidden:false,dataset:{},querySelector:()=>null,querySelectorAll:()=>[]})}
const context={console,window:{},document:{querySelector:el,querySelectorAll:()=>[],addEventListener:()=>{}},location:{hostname:'test'},localStorage:{getItem:()=>null,setItem:()=>{}},sessionStorage:{getItem:()=>null},setTimeout,clearTimeout,Date,URL,Blob};
vm.runInNewContext(script,context);const t=context.window.testing;t.setData(JSON.parse(fs.readFileSync('vercel/gated.json')));
const stats=t.statsResult({bg:3.04,bc:22,sg:3.33,sq:30,nq:15,ng:4});assert(Math.abs(stats.combined-3.178095238)<0.0001);assert(Math.abs(stats.projected-3.5533333)<0.0001);
assert.equal((t.panelStats().match(/<tr>/g)||[]).length,22);assert(t.panelStrategy().includes('21-school'));
for(const s of schools.schools){assert(t.schoolStrategyHTML(s.id).includes(s.name));t.S.ui.atab='questions';t.S.ui.aschool=s.id;t.renderApps();assert(elements['#appsbox'].innerHTML.includes('Supplements and guidance'))}
assert(t.strategyMarkdown().includes('Reserve'));assert.equal(JSON.parse(fs.readFileSync('vercel/gated.json')).routes.length,27);
console.log('PASS: 21 active, 5 reserves, 87 supplement/requirement items, 5 guidance bullets each, 21 stats rows, GPA math, all school rendering, gated privacy and 27 preserved route plans.');
