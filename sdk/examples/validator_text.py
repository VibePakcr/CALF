"""Independent exact-content validator; separate process from the producer.

The frozen check's parameters.expected is authoritative. This intentionally
does not import or repeat the producer's normalization implementation.
"""
import hashlib
import json
from pathlib import Path
import sys

raw = Path(sys.argv[-1]).read_bytes()
if len(raw) > 65536:
    raise ValueError('request too large')
r = json.loads(raw)
if r['schema'] != 'calf.runtime.v1' or r['operation'] != 'validate':
    raise ValueError('only validate is supported')
check, manifest = r['extra']['check'], r['extra']['manifest']
artifact = next(a for a in manifest['artifacts']['files'] if a['id'] == check['artifact'])
root = Path(r['outputDirectory']).resolve(strict=True)
target = (root / artifact['path']).resolve(strict=True)
if not target.is_relative_to(root):
    raise ValueError('candidate path escape')
with target.open('rb') as f:
    actual = f.read(1048577)
if len(actual) > 1048576:
    raise ValueError('validator limit exceeded')
matched = hashlib.sha256(actual).hexdigest() == artifact['sha256']
passed = matched and actual == check['rule']['parameters']['expected'].encode('utf-8')
print(json.dumps({'schema': 'calf.runtime.v1', 'requestId': r['requestId'],
                  'checkId': check['id'], 'manifestDigest': manifest['digest'],
                  'outcome': 'SATISFIED' if passed else 'VIOLATED',
                  'reason': 'Exact UTF-8 content and candidate hash compared independently.'}))
