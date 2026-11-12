// Read-only preview and native validation. No export or network call.
import {CalfClient} from '../node/index.mjs';
const [executable,home,task]=process.argv.slice(2);
if(!task)throw Error('Usage: task_handoff.mjs CALF HOME TASK');
const client=new CalfClient(executable,home);
const preview=await client.handoff(task),validation=await client.validateHandoff(preview);
if(validation.currentVerdict!=='NOT_EVALUATED'||validation.executionAuthority!==false)throw Error('Unexpected authority claim');
console.log(JSON.stringify({preview,validation}));
