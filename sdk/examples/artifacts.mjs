// Read-only / 읽기 전용. No scan, move, model call or direct record write.
import {CalfClient} from '../node/index.mjs';
const [binary,home,workspace,state]=process.argv.slice(2);
if(!binary||!home||!workspace)throw new Error('Usage: node artifacts.mjs ABS_BINARY ABS_HOME ABS_WORKSPACE [ABS_JOURNAL_STATE]');
const client=new CalfClient(binary,home);
console.log(JSON.stringify(await client.artifacts(workspace,{operation:'plan',...(state?{state}:{})}),null,2));
