"""Claude Code hooks -> pinned CALF native compatibility transport.

The existing native `codex` wire port is reused in an isolated Claude-owned
state directory. It is not a second model and never grants host permissions.
No transcript parsing, dependency installation, daemon or prompt storage.
"""
from pathlib import Path
import fcntl,hashlib,json,os,re,subprocess,sys,tempfile,time,uuid

EVENTS={'SessionStart','UserPromptSubmit','PreToolUse','PostToolUse','PostToolUseFailure','PostToolBatch','Stop','StopFailure','SessionEnd'}
LIMIT=4*1024*1024

def unique(rows):
    out={}
    for key,value in rows:
        if key in out:raise ValueError('duplicate_json_key')
        out[key]=value
    return out

def read_json(path):
    path=Path(path)
    if path.is_symlink() or path.stat().st_size>LIMIT:raise ValueError('unsafe_json_file')
    return json.loads(path.read_text(),object_pairs_hook=unique)

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(32768),b''):h.update(b)
    return h.hexdigest()

def physical(path):
    path=Path(path)
    if not path.is_absolute() or path.resolve()!=path:raise ValueError('physical_absolute_path_required')
    return path

def atomic(path,value):
    fd,name=tempfile.mkstemp(prefix='.claude-calf-',dir=path.parent)
    try:
        with os.fdopen(fd,'w') as f:os.fchmod(f.fileno(),0o600);json.dump(value,f,ensure_ascii=False);f.flush();os.fsync(f.fileno())
        os.replace(name,path)
    finally:
        if os.path.exists(name):os.unlink(name)

def execute(config,event,payload):
    cfg=read_json(config)
    if cfg.get('schema')!=1:raise ValueError('adapter_configuration_invalid')
    core_version=cfg.get('coreVersion','1.8.7')
    if core_version not in ('1.8.7','1.8.8','1.8.9','1.8.10','1.8.11','1.8.12','1.9.6','1.9.7','1.9.8'):raise ValueError('unqualified_core_version')
    core=physical(cfg['core']);native_config=physical(cfg['nativeConfig']);state=physical(cfg['adapterState'])
    if digest(core)!=cfg['coreSha256']:raise ValueError('native_binary_changed')
    if event not in EVENTS or payload.get('hook_event_name')!=event:raise ValueError('hook_event_mismatch')
    workspace=str(physical(payload['cwd']));session=payload['session_id']
    if not isinstance(session,str) or not 1<=len(session)<=256:raise ValueError('invalid_session_identity')
    if payload.get('agent_id'):raise ValueError('subagent_hooks_not_supported')
    key=hashlib.sha256((workspace+'\0'+session).encode()).hexdigest()
    state.mkdir(parents=True,exist_ok=True,mode=0o700);physical(state)
    folder=state/key;folder.mkdir(mode=0o700,exist_ok=True);physical(folder)
    lock=folder/'session.lock'
    if lock.is_symlink():raise ValueError('linked_session_lock')
    with lock.open('a') as locked:
        fcntl.flock(locked,fcntl.LOCK_EX|fcntl.LOCK_NB)
        path=folder/'session.json'
        current=read_json(path) if path.exists() else {'schema':1,'turn':'startup','open':False,'tools':{}}
        if current.get('schema')!=1 or not isinstance(current.get('tools'),dict):raise ValueError('adapter_state_invalid')
        def invoke(native_event,extra=None,turn=None):
            p={'cwd':workspace,'session_id':session,'turn_id':turn or current['turn']}
            if extra:p.update(extra)
            r=subprocess.run([str(core),'hook','codex',native_event,str(native_config)],input=json.dumps(p),capture_output=True,text=True,timeout=12)
            if r.returncode or len(r.stdout)>LIMIT:raise ValueError('native_hook_failed')
            response=json.loads(r.stdout,object_pairs_hook=unique)
            if response.get('error') or 'CALF 기록/판정 확인 불가:' in json.dumps(response,ensure_ascii=False):raise ValueError('native_evidence_unavailable')
            return response
        def interrupt():
            invoke('Interrupt')
            # Native interrupt collection is deliberately deferred to a regular
            # event; this observation drains it without executing user work.
            invoke('UserPromptSubmit')
            current['open']=False
        def close_unstarted(current_turn_only=False):
            # Claude can reject a command after PreToolUse without emitting a
            # PostToolUseFailure. Read the pinned port's per-session index;
            # never edit it or infer termination of an already claimed ticket.
            native_cfg=read_json(native_config)
            port=physical(Path(native_cfg['stateDir'])/'codex')
            transport=port/key[:32]/'transport.json'
            if not transport.exists():return []
            observed=read_json(transport)
            if observed.get('version')!=1 or not isinstance(observed.get('calls'),dict):raise ValueError('native_transport_invalid')
            closed=[]
            for attempt,call in observed['calls'].items():
                if not call.get('ticket') or call.get('results'):continue
                turn=call.get('turn')
                if current_turn_only and turn!=current['turn']:continue
                if not re.fullmatch(r'cx-[0-9a-f]{40}',attempt):raise ValueError('owned_attempt_invalid')
                file=physical(call['ticket'])
                if file!=port/'tickets'/(attempt+'.json'):raise ValueError('owned_ticket_location')
                terminal=file.with_suffix('.terminal.json')
                # A claim may represent a live process. Leave it UNKNOWN.
                if terminal.exists() or file.with_suffix('.claimed').exists():continue
                ticket=read_json(file);ticket_hash=digest(file)
                expected_key=hashlib.sha256((workspace+'\0'+session+'\0'+str(turn)).encode()).hexdigest()
                if ticket_hash!=call.get('ticketHash') or ticket.get('schema')!=1 or ticket.get('attempt')!=attempt or ticket.get('workspace')!=workspace or ticket.get('session')!=session or ticket.get('turn')!=turn or ticket.get('turnKey')!=expected_key or ticket.get('state')!=str(port) or ticket.get('commandHash')!=call.get('commandHash'):raise ValueError('owned_ticket_identity')
                if len(closed)>=8:raise ValueError('owned_reconciliation_limit')
                invoke('Interrupt',turn=turn)
                marker=port/'cancellations'/(expected_key+'.json')
                expected={'hook_event_name':'Interrupt','cwd':workspace,'session_id':session,'turn_id':turn}
                if read_json(marker)!=expected:raise ValueError('owned_cancellation_missing')
                # With the verified cancellation marker, pinned 1.8.7 execute
                # writes its own cancelled terminal without launching argv.
                result=subprocess.run([str(core),'execute',str(file),ticket_hash],capture_output=True,timeout=12)
                receipt=read_json(terminal)
                if result.returncode!=130 or result.stdout or result.stderr or receipt.get('ticketHash')!=ticket_hash or receipt.get('attempt')!=attempt or receipt.get('session')!=session or receipt.get('turn')!=turn or receipt.get('workspace')!=workspace or receipt.get('cancelled') is not True or receipt.get('exitCode') is not None or receipt.get('childReaped') is not True or receipt.get('groupAbsent') is not True:raise ValueError('owned_cancellation_unconfirmed')
                invoke('UserPromptSubmit',turn=turn)
                closed.append({'attempt':attempt,'turn':turn,'ticketSha256':ticket_hash,'terminalSha256':digest(terminal)})
            return closed
        reconciled=[];batch_resolutions=[]
        output={}
        if event=='SessionStart':
            native=invoke('SessionStart')
            text=native.get('hookSpecificOutput',{}).get('additionalContext','')
            output={'hookSpecificOutput':{'hookEventName':event,'additionalContext':'CALF '+core_version+' · Claude Code. Only registered checks establish completion. '+text}}
        elif event=='UserPromptSubmit':
            reconciled=close_unstarted()
            if current['open']:interrupt()
            current.update(turn='claude-'+uuid.uuid4().hex,open=True,tools={})
            invoke('UserPromptSubmit')
            if reconciled:
                binding=next((b for b in read_json(native_config).get('bindings',[]) if b.get('workspace')==workspace),None)
                if binding:
                    result=subprocess.run([str(core),'status',workspace,binding['task']],capture_output=True,text=True,timeout=12)
                    if result.returncode:raise ValueError('native_reconciled_status_unavailable')
                    verdict=json.loads(result.stdout,object_pairs_hook=unique)
                    output={'hookSpecificOutput':{'hookEventName':event,'additionalContext':'CALF reconciled '+str(len(reconciled))+' never-started owned checks as cancelled, without launching the check commands. Existing current registered-task verdict: '+str(verdict.get('outcome','UNKNOWN'))+'. This does not authorize another check run.'}}
        elif event in {'PreToolUse','PostToolUse','PostToolUseFailure'}:
            if not current['open']:raise ValueError('no_active_user_turn')
            tool=payload.get('tool_name');identity=payload.get('tool_use_id');value=payload.get('tool_input')
            if not isinstance(identity,str) or not identity or not isinstance(tool,str) or not isinstance(value,dict):raise ValueError('tool_identity_missing')
            mapped='apply_patch' if tool in {'Write','Edit','MultiEdit','NotebookEdit'} else tool
            extra={'tool_name':mapped,'tool_use_id':identity,'tool_input':value}
            if event=='PreToolUse':
                if len(current['tools'])>=128 and identity not in current['tools']:raise ValueError('turn_tool_limit')
                native=invoke('PreToolUse',extra)
                hook=native.get('hookSpecificOutput',{})
                # In particular, never forward native permissionDecision=allow.
                # Claude's own deny/ask/default permission flow stays in charge.
                if hook.get('permissionDecision')=='deny':
                    output={'hookSpecificOutput':{'hookEventName':event,'permissionDecision':'deny','permissionDecisionReason':hook.get('permissionDecisionReason','CALF evidence unavailable')}}
                elif 'updatedInput' in hook:
                    output={'hookSpecificOutput':{'hookEventName':event,'updatedInput':hook['updatedInput']}}
                current['tools'][identity]={'tool':mapped,'inputSha256':hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
            else:
                if identity not in current['tools']:raise ValueError('tool_result_without_start')
                if current['tools'][identity]['tool']!=mapped:raise ValueError('tool_identity_changed')
                response=payload.get('tool_response',{})
                # Do not guess exit 0 from a tool's textual success claim. The
                # native owned ticket is authoritative for registered checks.
                if not isinstance(response,dict):response={'result':response}
                extra['tool_response']=response
                if event=='PostToolUseFailure':
                    interrupt();extra['tool_response']={'error':True,'interrupted':payload.get('is_interrupt') is True}
                invoke('PostToolUse',extra)
        elif event=='PostToolBatch':
            # A permission denial resolves a tool call without PostToolUse or
            # PostToolUseFailure. Use the host's complete batch, not transcript
            # text, timeouts or a missing process, to close an observed call.
            calls=payload.get('tool_calls')
            if not current['open'] or not isinstance(calls,list) or len(calls)>128:raise ValueError('batch_shape_invalid')
            native_cfg=read_json(native_config)
            transport=physical(Path(native_cfg['stateDir'])/'codex')/key[:32]/'transport.json'
            observed=read_json(transport) if transport.exists() else {'calls':{}}
            if not isinstance(observed.get('calls'),dict):raise ValueError('native_transport_invalid')
            pending=[];seen=set()
            # Validate the entire batch before writing any terminal observation.
            for call in calls:
                if not isinstance(call,dict):raise ValueError('batch_call_invalid')
                identity=call.get('tool_use_id');tool=call.get('tool_name');value=call.get('tool_input')
                if not isinstance(identity,str) or not identity or identity in seen or not isinstance(tool,str) or not isinstance(value,dict) or 'tool_response' not in call:raise ValueError('batch_call_invalid')
                seen.add(identity)
                prior=current['tools'].get(identity)
                if prior is None:continue  # Rejected before PreToolUse: no start to close.
                mapped='apply_patch' if tool in {'Write','Edit','MultiEdit','NotebookEdit'} else tool
                matches=[v for v in observed['calls'].values() if v.get('toolId')==identity and v.get('turn')==current['turn']]
                if len(matches)>1:raise ValueError('batch_identity_ambiguous')
                if not matches:continue
                native_call=matches[0]
                # An owned check can finish only through its real native terminal.
                # Its rewritten tool input is therefore not used as batch proof.
                if native_call.get('ticket') or native_call.get('criterion') is not None or native_call.get('results'):continue
                input_hash=hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                if prior['tool']!=mapped or prior['inputSha256']!=input_hash:raise ValueError('batch_tool_identity_changed')
                result_hash=hashlib.sha256(json.dumps(call['tool_response'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                pending.append({'tool_name':mapped,'tool_use_id':identity,'tool_input':value,'tool_response':{'calfResolutionEvent':'PostToolBatch','resultSha256':result_hash,'executionConfirmed':False}})
            for extra in pending:
                invoke('PostToolUse',extra)
                batch_resolutions.append({'toolUseId':extra['tool_use_id'],'resultSha256':extra['tool_response']['resultSha256'],'executionConfirmed':False})
            if pending:
                output={'hookSpecificOutput':{'hookEventName':event,'additionalContext':'CALF observed '+str(len(pending))+' resolved non-check tool calls from this host batch. This records resolution only, not successful execution or a passing check. Registered checks still require their native receipts.'}}
        elif event=='Stop':
            reconciled=close_unstarted(current_turn_only=True)
            text=payload.get('last_assistant_message')
            if not isinstance(text,str):text='CALF_TURN_OUTCOME: BLOCKED'
            if payload.get('background_tasks') or reconciled:text+='\nCALF_TURN_OUTCOME: BLOCKED'
            output=invoke('Stop',{'last_assistant_message':text,'stop_hook_active':payload.get('stop_hook_active') is True})
            if output.get('decision')!='block':current['open']=False
        elif event in {'StopFailure','SessionEnd'}:
            reconciled=close_unstarted()
            if current['open']:interrupt()
        atomic(path,current)
        audit={'host':'claude','nativeWirePort':'codex','engineVersion':core_version,'event':event,'session':session,'turn':current['turn'],'workspace':workspace,'tool':payload.get('tool_name'),'toolUseId':payload.get('tool_use_id'),'at':time.time(),'nativeBinarySha256':cfg['coreSha256']}
        if reconciled:audit['reconciledUnstartedChecks']=reconciled
        if batch_resolutions:audit['resolvedBatchCalls']=batch_resolutions
        with (folder/'events.jsonl').open('a') as f:os.fchmod(f.fileno(),0o600);f.write(json.dumps(audit,ensure_ascii=False)+'\n')
        return output

def main():
    event=sys.argv[1] if len(sys.argv)>1 else ''
    try:
        if len(sys.argv)!=3:raise ValueError('adapter_arguments')
        raw=sys.stdin.buffer.read(LIMIT+1)
        if len(raw)>LIMIT:raise ValueError('payload_limit')
        value=json.loads(raw,object_pairs_hook=unique)
        result=execute(sys.argv[2],event,value)
    except Exception as error:
        print('CALF Claude adapter: '+type(error).__name__+': '+str(error)[:256],file=sys.stderr)
        reason='CALF Claude record/check unavailable: '+type(error).__name__+'. Completion UNKNOWN.'
        if event=='PreToolUse':result={'hookSpecificOutput':{'hookEventName':event,'permissionDecision':'deny','permissionDecisionReason':reason}}
        elif event=='Stop':result={'continue':False,'stopReason':reason,'systemMessage':reason}
        elif event=='UserPromptSubmit':result={'decision':'block','reason':reason}
        else:result={'systemMessage':reason}
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
