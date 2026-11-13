// Read-only example: node engineering_knowledge.mjs CALF_ABSOLUTE DATA_HOME_ABSOLUTE
import {CalfClient} from '../node/index.mjs';
const client=new CalfClient(process.argv[2],process.argv[3]);
const view=await client.knowledge('resolve',{query:'데이터베이스 쿼리 성능',byteBudget:8192});
if(view.executionAuthority!==false||view.currentCompletion!=='NOT_EVALUATED')throw Error('Unexpected reference contract');
console.log(JSON.stringify(view,null,2));
