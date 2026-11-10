"""Explicit, local Claude hook installation for the qualified macOS Claude Code adapter.

Codex and Antigravity use the native install command. This tool neither edits
their settings nor grants trust, command permissions, or a model connection.
"""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess
import sys
import tempfile
import uuid

EVENTS=('SessionStart','UserPromptSubmit','PreToolUse','PostToolUse','PostToolUseFailure','PostToolBatch','Stop','StopFailure','SessionEnd')

def physical(value,directory=False):
    p=Path(value)
    if not p.is_absolute() or p.is_symlink() or p.resolve(strict=True)!=p:raise ValueError('physical_absolute_path_required')
    if not (p.is_dir() if directory else p.is_file()):raise ValueError('regular_path_required')
    return p

def sha(path):
    h=hashlib.sha256()
    with physical(path).open('rb') as f:
        for block in iter(lambda:f.read(32768),b''):h.update(block)
    return h.hexdigest()

def unique(rows):
    out={}
    for k,v in rows:
        if k in out:raise ValueError('duplicate_json_key')
        out[k]=v
    return out

def read(path):
    p=physical(path)
    if p.stat().st_size>1048576:raise ValueError('settings_size_limit')
    return json.loads(p.read_bytes(),object_pairs_hook=unique)

def encoded(value):return (json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()

def write_new(path,value):
    with path.open('xb') as f:os.fchmod(f.fileno(),0o600);f.write(encoded(value));f.flush();os.fsync(f.fileno())

def replace(path,raw):
    fd,name=tempfile.mkstemp(prefix='.calf-host-',dir=path.parent)
    with os.fdopen(fd,'wb') as f:os.fchmod(f.fileno(),0o600);f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(name,path)
    folder=os.open(path.parent,os.O_RDONLY)
    try:os.fsync(folder)
    finally:os.close(folder)

@contextmanager
def locked(root):
    import fcntl
    with (root/'.mutex').open('a') as f:
        fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        try:yield
        finally:fcntl.flock(f,fcntl.LOCK_UN)

def store(path):
    root=physical(path,True)
    if read(root/'store.json')!={'schema':'calf.host-kit.v1'}:raise ValueError('host_store_required')
    return root

def prepare(root,revision,core,config,python):
    if sys.platform!='darwin':raise ValueError('claude_host_not_qualified_on_this_platform')
    if not re.fullmatch(r'[0-9A-Za-z.-]{1,64}',revision) or revision in ('.','..'):raise ValueError('revision_required')
    core=physical(core);config=physical(config);python=physical(python)
    info=subprocess.run([str(core),'--version'],capture_output=True,timeout=10,check=True)
    core_version=json.loads(info.stdout).get('version')
    if core_version not in ('1.8.7','1.8.8','1.8.9','1.8.10','1.8.11','1.8.12','1.9.6','1.9.7','1.9.8'):raise ValueError('qualified_core_required')
    cfg=read(config)
    if cfg.get('version')!=1 or not isinstance(cfg.get('bindings'),list) or not isinstance(cfg.get('stateDir'),str):raise ValueError('native_hook_config_required')
    root=Path(root)
    if not root.is_absolute() or '..' in root.parts or root.resolve()!=root:raise ValueError('physical_absolute_path_required')
    if not root.exists():
        root.mkdir(parents=True,mode=0o700);physical(root,True)
        write_new(root/'store.json',{'schema':'calf.host-kit.v1'});(root/'versions').mkdir();(root/'operations').mkdir()
    root=store(root)
    with locked(root):
        dest=root/'versions'/revision;dest.mkdir(mode=0o700)
        source=Path(__file__).resolve().parent/'claude/adapter.py'
        with (dest/'adapter.py').open('xb') as f:f.write(source.read_bytes())
        state=root/'state';state.mkdir(mode=0o700,exist_ok=True)
        write_new(dest/'adapter.json',{'schema':1,'core':str(core),'coreSha256':sha(core),'coreVersion':core_version,'nativeConfig':str(config),'adapterState':str(state)})
        hooks={}
        for event in EVENTS:
            row={'hooks':[{'type':'command','command':shlex.join([str(python),'-B',str(dest/'adapter.py'),event,str(dest/'adapter.json')]),'timeout':20}]}
            if event in ('PreToolUse','PostToolUse','PostToolUseFailure'):row['matcher']='*'
            hooks[event]=[row]
        release={'revision':revision,'hooks':hooks,'pins':{str(p):sha(p) for p in [core,python,dest/'adapter.py',dest/'adapter.json']}}
        write_new(dest/'release.json',release)
        return {'status':'PREPARED','revision':revision,'coreVersion':core_version,'hooks':len(hooks),'settingsWritten':False}

def release(root,revision):
    if not re.fullmatch(r'[0-9A-Za-z.-]{1,64}',revision) or revision in ('.','..'):raise ValueError('revision_required')
    result=read(root/'versions'/revision/'release.json')
    if result['revision']!=revision or any(sha(p)!=h for p,h in result['pins'].items()):raise ValueError('release_identity_changed')
    return result

def apply(root,settings,revision,expected):
    root=store(root);settings=physical(settings)
    with locked(root):
        unresolved=[p.name for p in (root/'operations').iterdir() if not (p/'result.json').exists()]
        if unresolved:raise ValueError('reconcile_pending_operations_first')
        if sha(settings)!=expected:raise ValueError('settings_changed')
        before=settings.read_bytes();value=read(settings)
        if not isinstance(value,dict):raise ValueError('settings_object_required')
        hooks=value.setdefault('hooks',{})
        if not isinstance(hooks,dict):raise ValueError('hooks_object_required')
        active=read(root/'active.json') if (root/'active.json').exists() else None
        if active is None:
            commands=[item.get('command','') for rows in hooks.values() if isinstance(rows,list) for row in rows if isinstance(row,dict) for item in row.get('hooks',[]) if isinstance(item,dict)]
            if any('calf' in command.lower() for command in commands if isinstance(command,str)):raise ValueError('existing_calf_route_requires_explicit_migration')
        if active:
            if active['settings']!=str(settings):raise ValueError('active_settings_path_changed')
            old=release(root,active['revision'])
            for event,rows in old['hooks'].items():
                present=hooks.get(event,[])
                if not isinstance(present,list):raise ValueError('hook_array_required')
                for row in rows:
                    if present.count(row)!=1:raise ValueError('managed_hook_edited_reconcile_first')
                    present.remove(row)
        new=release(root,revision)
        for event,rows in new['hooks'].items():
            present=hooks.setdefault(event,[])
            if not isinstance(present,list) or any(row in present for row in rows):raise ValueError('duplicate_or_invalid_hook')
            present.extend(rows)
        raw=encoded(value);after=hashlib.sha256(raw).hexdigest();op=root/'operations'/uuid.uuid4().hex;op.mkdir(mode=0o700)
        with (op/'before.private.json').open('xb') as f:os.fchmod(f.fileno(),0o600);f.write(before);f.flush();os.fsync(f.fileno())
        target={'revision':revision,'settings':str(settings)}
        write_new(op/'intent.json',{'settings':str(settings),'beforeSha256':expected,'afterSha256':after,'activeBefore':active,'activeAfter':target})
        if sha(settings)!=expected:raise ValueError('settings_changed')
        replace(settings,raw);replace(root/'active.json',encoded(target));write_new(op/'result.json',{'status':'APPLIED','afterSha256':after})
        return {'status':'APPLIED','revision':revision,'operation':op.name,'settingsSha256':after,'permissionsChanged':False,'hostRestartRequired':True}

def recover(root,acknowledge=None):
    root=store(root)
    with locked(root):
        pending=[]
        for op in (root/'operations').iterdir():
            if (op/'result.json').exists():continue
            intent=read(op/'intent.json');current=sha(intent['settings'])
            state='COMMITTED_UNACKNOWLEDGED' if current==intent['afterSha256'] else 'NOT_APPLIED' if current==intent['beforeSha256'] else 'UNKNOWN'
            pending.append({'operation':op.name,'status':state})
            if acknowledge==op.name:
                if state=='UNKNOWN':raise ValueError('settings_drift_reconcile_manually')
                target=intent['activeAfter'] if state=='COMMITTED_UNACKNOWLEDGED' else intent['activeBefore']
                if target is not None:replace(root/'active.json',encoded(target))
                write_new(op/'result.json',{'status':state,'reconciled':True})
        if acknowledge and acknowledge not in [p['operation'] for p in pending]:raise ValueError('pending_operation_not_found')
        return {'pending':pending,'settingsWritten':False,'acknowledged':acknowledge}

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    p=sub.add_parser('prepare')
    for key in ['root','core','config','python']:p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--revision',required=True)
    p=sub.add_parser('apply')
    for key in ['root','settings']:p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--revision',required=True);p.add_argument('--expected-sha256',required=True)
    p=sub.add_parser('recover');p.add_argument('--root',type=Path,required=True);p.add_argument('--acknowledge')
    p=sub.add_parser('inspect');p.add_argument('--settings',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.action=='prepare':result=prepare(args.root,args.revision,args.core,args.config,args.python)
        elif args.action=='apply':result=apply(args.root,args.settings,args.revision,args.expected_sha256)
        elif args.action=='recover':result=recover(args.root,args.acknowledge)
        else:read(args.settings);result={'settingsSha256':sha(args.settings),'settingsWritten':False}
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (OSError,ValueError,KeyError,subprocess.SubprocessError) as error:
        print(json.dumps({'status':'UNKNOWN','error':type(error).__name__,'message':str(error)[:300]},ensure_ascii=False),file=sys.stderr);return 1

if __name__=='__main__':raise SystemExit(main())
