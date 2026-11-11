// Seals the tutor/admin data for the claude.ai build so it is not readable in the page source.
// Usage: node scripts/seal.cjs <code> <salt> <json-file>   -> prints base64
// This keeps casual readers out. A 4-digit code can still be guessed by trying every value.
const fs = require('fs');
function cyrb53(str){var h1=0xdeadbeef,h2=0x41c6ce57;for(var i=0,ch;i<str.length;i++){ch=str.charCodeAt(i);h1=Math.imul(h1^ch,2654435761);h2=Math.imul(h2^ch,1597334677)}h1=Math.imul(h1^(h1>>>16),2246822507)^Math.imul(h2^(h2>>>13),3266489909);h2=Math.imul(h2^(h2>>>16),2246822507)^Math.imul(h1^(h1>>>13),3266489909);return 4294967296*(2097151&h2)+(h1>>>0)}
function tnCrypt(bytes,code,salt){var h=cyrb53('tn:'+salt+':'+code),g=cyrb53(code+'|'+salt),a=h>>>0,b=Math.floor(h/4294967296)>>>0,c=g>>>0,d=Math.floor(g/4294967296)>>>0;function r(){a|=0;b|=0;c|=0;d|=0;var t=(a+b|0)+d|0;d=d+1|0;a=b^b>>>9;b=c+(c<<3)|0;c=c<<21|c>>>11;c=c+t|0;return t>>>0}for(var i=0;i<24;i++)r();var out=new Uint8Array(bytes.length),w=0;for(i=0;i<bytes.length;i++){if(i%4===0)w=r();out[i]=bytes[i]^(w>>>(i%4*8)&255)}return out}
const [code, salt, file] = process.argv.slice(2);
const plain = Buffer.concat([Buffer.from('TNZ1'), fs.readFileSync(file)]);
process.stdout.write(Buffer.from(tnCrypt(plain, code, salt)).toString('base64'));
