"""Loopback HTTP adapter. Endpoint is a registered command argument.

Command: [python, runtime_http.py, http://127.0.0.1:PORT/work, REQUEST].
Service must deduplicate execute by requestId and implement query/cancel.
No redirects, proxy, authentication, implicit retry or arbitrary remote URL.
"""
import http.client
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

url = urlsplit(sys.argv[-2])
if url.scheme != 'http' or url.hostname not in ('127.0.0.1', '::1') or url.username or url.password or url.fragment or url.query:
    raise ValueError('Select an explicit loopback HTTP endpoint')
raw = Path(sys.argv[-1]).read_bytes()
if len(raw) > 65536:
    raise ValueError('request too large')
r = json.loads(raw)
if r['schema'] != 'calf.runtime.v1' or r['operation'] not in ('execute', 'query', 'cancel'):
    raise ValueError('unsupported request')
c = http.client.HTTPConnection(url.hostname, url.port, timeout=5)
try:
    c.request('POST', url.path or '/', body=raw, headers={'Content-Type': 'application/json'})
    response = c.getresponse()
    body = response.read(65537)
    if response.status != 200 or len(body) > 65536:
        raise ValueError('incomplete service response; reconcile by requestId')
    value = json.loads(body)
    if value.get('schema') != 'calf.runtime.v1' or value.get('requestId') != r['requestId']:
        raise ValueError('service response identity mismatch')
    print(json.dumps(value))
finally:
    c.close()
