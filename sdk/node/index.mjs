// Dependency-free Node client. All state transitions and verification stay native.
import {spawn} from 'node:child_process';
import {isAbsolute} from 'node:path';
export class CalfClient {
  constructor(executable, home, {timeoutMs=35000,maxBytes=1024*1024}={}) {
    if(!isAbsolute(executable)||!isAbsolute(home)||!Number.isSafeInteger(timeoutMs)||timeoutMs<=0||!Number.isSafeInteger(maxBytes)||maxBytes<1024||maxBytes>8*1024*1024)throw Error('Invalid CALF client options');
    Object.assign(this,{executable,home,timeoutMs,maxBytes});
  }
  work(action,fields={}) {
    if(!['register','adapters','submit','list','inspect','step','cancel','retry','recheck','adopt'].includes(action)||['op','home','action'].some(k=>Object.hasOwn(fields,k)))return Promise.reject(Error('Invalid work request'));
    const input=JSON.stringify({...fields,op:'work',home:this.home,action});
    if(Buffer.byteLength(input)>65536)return Promise.reject(Error('Request exceeds 64 KiB'));
    return new Promise((resolve,reject)=>{
      const child=spawn(this.executable,['api'],{shell:false,windowsHide:true,stdio:['pipe','pipe','pipe']});
      let chunks=[],bytes=0,errBytes=0,failure=null,killTimer;
      const stop=message=>{
        if(failure)return;failure=Error(message+'; inspect before retrying');chunks=[];
        if(['step','recheck'].includes(action)&&fields.work){
          const cancel=spawn(this.executable,['api'],{shell:false,windowsHide:true,stdio:['pipe','ignore','ignore']});
          const cancelTimer=setTimeout(()=>cancel.kill(),2000);
          cancel.once('error',()=>clearTimeout(cancelTimer));cancel.once('close',()=>clearTimeout(cancelTimer));cancel.stdin.on('error',()=>{});
          cancel.stdin.end(JSON.stringify({op:'work',home:this.home,action:'cancel',work:fields.work}));
        }else child.kill('SIGTERM');
        killTimer=setTimeout(()=>child.kill('SIGKILL'),5000);
      };
      const timer=setTimeout(()=>stop('CALF transport timed out; completion unknown'),this.timeoutMs);
      child.stdout.on('data',b=>{bytes+=b.length;if(bytes>this.maxBytes)stop('Response limit exceeded');else if(!failure)chunks.push(b);});
      child.stderr.on('data',b=>{errBytes+=b.length;if(errBytes>65536)stop('Diagnostic limit exceeded');});
      child.stdin.on('error',()=>{});
      child.once('error',e=>{clearTimeout(timer);clearTimeout(killTimer);reject(e);});
      child.once('close',code=>{clearTimeout(timer);clearTimeout(killTimer);if(failure)return reject(failure);try{const v=JSON.parse(Buffer.concat(chunks).toString('utf8'));if(code!==0||v.error)throw Error(v.error||'CALF failed');resolve(v);}catch(e){reject(e);}});
      child.stdin.end(input);
    });
  }
  workMcpServer({control=false}={}) {return {command:this.executable,args:['work-mcp',this.home,...(control?['--control']:[])]};}
  repositoryMcpServer(registry,workspace) {
    if([registry,workspace].some(p=>typeof p!=='string'||!isAbsolute(p)||p.includes('\0')||p.split(/[\\/]/).includes('..')))throw Error('Explicit absolute registry and workspace paths are required');
    return {command:this.executable,args:['repository-mcp',registry,workspace]};
  }
  toolMcpServer(policy,policySha256,{control=false}={}) {
    if(typeof policy!=='string'||!isAbsolute(policy)||policy.includes('\0')||policy.split(/[\\/]/).includes('..')||typeof policySha256!=='string'||!/^[0-9a-f]{64}$/.test(policySha256)||typeof control!=='boolean')throw Error('An absolute policy path, exact policy SHA-256 and boolean control are required');
    return {command:this.executable,args:['tool-mcp',policy,policySha256,...(control?['--control']:[])]};
  }
}
export const isSatisfied = result => result?.verified===true && result?.outcome==='SATISFIED';
