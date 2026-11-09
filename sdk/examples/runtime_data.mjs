// On-demand Node data aggregation; no packages, shell, service or model.
// Input id rows: JSON array of {category:string, amount:integer}.
import fs from 'node:fs';
import path from 'node:path';
const raw=fs.readFileSync(process.argv.at(-1));
if(raw.length>65536)throw Error('Request too large');
const r=JSON.parse(raw);
if(r.schema!=='calf.runtime.v1'||r.operation!=='execute')throw Error('Only execute is supported');
const input=r.inputs.find(x=>x.id==='rows');
if(fs.statSync(input.path).size>1048576)throw Error('Example input limit: 1 MiB');
const rows=JSON.parse(fs.readFileSync(input.path,'utf8'));
if(!Array.isArray(rows)||rows.length>10000)throw Error('Invalid rows');
const groups=new Map();let total=0;
for(const row of rows){
  if(typeof row.category!=='string'||!Number.isSafeInteger(row.amount))throw Error('Invalid row');
  const n=(groups.get(row.category)||0)+row.amount;total+=row.amount;
  if(!Number.isSafeInteger(n)||!Number.isSafeInteger(total))throw Error('Integer overflow');
  groups.set(row.category,n);
}
const result={count:rows.length,total,groups:Object.fromEntries([...groups].sort((a,b)=>a[0].localeCompare(b[0])))};
const root=fs.realpathSync(r.outputDirectory),target=path.resolve(root,r.outputs.find(x=>x.id==='summary').path);
if(path.relative(root,target).startsWith('..')||path.isAbsolute(path.relative(root,target)))throw Error('Output escaped candidate folder');
fs.mkdirSync(path.dirname(target),{recursive:true});
fs.writeFileSync(target,JSON.stringify(result)+'\n',{flag:'wx'});
process.stdout.write(JSON.stringify({schema:'calf.runtime.v1',requestId:r.requestId,state:'succeeded',providerJobId:null,usage:null})+'\n');
