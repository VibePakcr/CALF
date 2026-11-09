"""Run a local text work contract through the native core. No AI required.

python universal_work.py /absolute/calf /absolute/records /absolute/input.txt
Uses a deterministic key; repeated identical submissions inspect the same work.
"""
from pathlib import Path
import hashlib
import sys
from calf_sdk import CalfClient
from calf_sdk.work import adapter_descriptor, input_reference

core, home, source = map(Path, sys.argv[1:4])
client = CalfClient(core, home, timeout=35)
script = Path(__file__).resolve().with_name('runtime_text.py')
adapter_id = 'text-' + hashlib.sha256(script.read_bytes()).hexdigest()[:16]
client.work('register', adapter=adapter_descriptor(adapter_id,
    [str(Path(sys.executable).resolve()), str(script)], [script]))
input_file = input_reference(source, 'source', 'text/plain')
spec = {'schema':'calf.work.v1', 'key':'text-normalize:'+input_file['sha256']+':'+adapter_id,
        'title':'Normalize text', 'adapter':adapter_id, 'parameters':{}, 'inputs':[input_file],
        'outputs':[{'id':'document','path':'document.txt','mediaType':'text/plain','minBytes':1,'maxBytes':1048576}],
        # Select a real, task-specific requirement. Here the output must contain
        # a newline; this does NOT establish semantic quality of the document.
        'checks':[{'id':'newline','artifact':'document','kind':'text-contains','rule':{'text':'\n'}}],
        'budget':{'maxAttempts':1,'timeoutMs':10000,'maxOutputBytes':1048576},'adoption':'manual'}
accepted = client.work('submit', spec=spec)
result = client.work('step', work=accepted['work'])
print({'work':result['work'],'phase':result['phase'],'outcome':result['outcome'],
       'manifest':result['manifest'],'adopted':result['adopted']})
# Adoption is separate: after review, use client.work('adopt', work=..., digest=...).
