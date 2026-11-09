"""Small protocol helpers for runtime and validator adapters. No execution engine."""
import hashlib
import json
from pathlib import Path
from .client import _json

def read_work_request(path):
    with open(path,'rb') as f: raw=f.read(65537)
    if len(raw)>65536: raise ValueError('Work request exceeds 64 KiB')
    r=_json(raw)
    if r.get('schema')!='calf.runtime.v1' or r.get('operation') not in ('execute','query','cancel','validate') or not isinstance(r.get('requestId'),str):
        raise ValueError('Unsupported runtime request')
    return r

def runtime_result(request, state, *, provider_job_id=None, usage=None):
    if state not in ('running','succeeded','failed','cancelled','unknown','not_found'):
        raise ValueError('Unsupported runtime state')
    return {'schema':'calf.runtime.v1','requestId':request['requestId'],'state':state,'providerJobId':provider_job_id,'usage':usage}

def validation_result(request, outcome, reason):
    if request['operation']!='validate' or outcome not in ('SATISFIED','VIOLATED','UNKNOWN') or not isinstance(reason,str) or len(reason)>2048:
        raise ValueError('Invalid validation result')
    return {'schema':'calf.runtime.v1','requestId':request['requestId'],'checkId':request['extra']['check']['id'],
            'manifestDigest':request['extra']['manifest']['digest'],'outcome':outcome,'reason':reason}

def input_reference(path, identifier, media_type):
    path=Path(path).resolve(strict=True);h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(32768),b''):h.update(b)
    return {'id':identifier,'path':str(path),'sha256':h.hexdigest(),'mediaType':media_type}

def adapter_descriptor(identifier, command, files, *, role='executor', asynchronous=False, query=False, cancel=False, resource_class='light'):
    return {'schema':1,'id':identifier,'role':role,'command':list(command),'files':list(map(str,files)),
            'capabilities':{'asynchronous':asynchronous,'query':query,'cancel':cancel},'class':resource_class}

def emit_work(response):
    raw=json.dumps(response,ensure_ascii=False,allow_nan=False)
    if len(raw.encode())>65536:raise ValueError('Runtime response exceeds 64 KiB')
    print(raw,flush=True)
