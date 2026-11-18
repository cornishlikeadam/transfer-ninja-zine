const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('vercel/public/index.html','utf8'),gated=JSON.parse(fs.readFileSync('vercel/gated.json'));
let script=html.match(/<script>([\s\S]*?)<\/script>/)[1].replace('setGateUI();renderAll();entryStoreInit();libInit();','window.test={S,SY,save,saveLocal,stamp,payload,syncApply,syncKeys,syncValue,saveEntry,queueEntry,deleteEntry,sprintDocuments,writingDeskHTML,writingBackup,setData:function(){DATA=fixture;LENS=fixture.lens;UNLOCKED=true;ENT=S.ent||(S.ent={});SY.ready=true;stamp();SY.mode="local"}};').replace('syncBoot();','');
function client(storage={}){
 const elements={};function el(k){return elements[k]||(elements[k]={innerHTML:'',textContent:'',value:'',hidden:false,dataset:{},querySelector:()=>null,querySelectorAll:()=>[]})}
 const c={console,fixture:gated,window:{},document:{querySelector:el,querySelectorAll:()=>[],addEventListener:()=>{}},location:{hostname:'test'},localStorage:{getItem:k=>storage[k]||null,setItem:(k,v)=>storage[k]=v},sessionStorage:{getItem:()=>null},setTimeout:()=>1,clearTimeout:()=>{},Date,URL,Blob};vm.runInNewContext(script,c);c.window.test.setData();return {t:c.window.test,storage};
}
const a=client();a.t.queueEntry('ca-essay',{text:'A real scene. 中文 🙂',status:'draft'});
let stored=JSON.parse(a.storage['transfer-ninja-zine.v1']);assert.equal(stored.ent['ca-essay'].text,'A real scene. 中文 🙂');assert(stored._t['ent:ca-essay']>0,'revision timestamp must be saved with text, immediately');
assert.equal(client(a.storage).t.S.ent['ca-essay'].text,stored.ent['ca-essay'].text,'reload before debounce keeps final characters');
a.t.S.notes['profile-Life story in order']='My own correction';a.t.save();stored=JSON.parse(a.storage['transfer-ninja-zine.v1']);assert(stored._t['notes:profile-Life%20story%20in%20order']);
const b=client();b.t.queueEntry('q-cornell-another',{text:'A different essay'});const both=Object.assign({},JSON.parse(JSON.stringify(a.t.payload())),JSON.parse(JSON.stringify(b.t.payload())));a.t.syncApply(both);b.t.syncApply(both);
assert.equal(a.t.S.ent['q-cornell-another'].text,'A different essay');assert.equal(b.t.S.ent['ca-essay'].text,'A real scene. 中文 🙂','different essays from two devices survive');
a.t.deleteEntry('ca-essay');const deletion=a.t.payload()['ent:ca-essay'];assert.equal(deletion.v,null);b.t.syncApply({'ent:ca-essay':{v:null,t:deletion.t+1}});assert(!b.t.S.ent['ca-essay'],'deletion tombstone propagates');
b.t.syncApply({notes:{v:{legacy:'Old note'},t:10},ent:{v:{'old-draft':{text:'Prior version writing'}},t:10}});assert.equal(b.t.S.notes.legacy,'Old note');assert.equal(b.t.S.ent['old-draft'].text,'Prior version writing','legacy data migrates without reset');
assert(a.t.writingDeskHTML().includes('Story bank'));assert(a.t.sprintDocuments().some(d=>d.school==='cornell'));assert(a.t.writingBackup().state.notes['profile-Life story in order']);
console.log('PASS writing persistence: immediate keystroke save, timestamp reload, Unicode, independent drafts across devices, deletion, legacy migration, profile notes and backup.');
