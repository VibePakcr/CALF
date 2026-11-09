"""On-demand Python text normalization adapter; standard library only.

Command: [physical-python, physical-runtime_text.py, REQUEST_FILE].
Input id 'source'; output id 'document'. Files are bounded to 1 MiB here.
"""
import json
from pathlib import Path
import sys
import unicodedata


def main():
    raw = Path(sys.argv[-1]).read_bytes()
    if len(raw) > 65536:
        raise ValueError('request too large')
    r = json.loads(raw)
    if r['schema'] != 'calf.runtime.v1' or r['operation'] != 'execute':
        raise ValueError('only synchronous execute is supported')
    source = next(x for x in r['inputs'] if x['id'] == 'source')
    with open(source['path'], 'rb') as f:
        text = f.read(1048577)
    if len(text) > 1048576:
        raise ValueError('text example accepts at most 1 MiB')
    lines = unicodedata.normalize('NFC', text.decode('utf-8')).splitlines()
    result = '\n'.join(line.rstrip() for line in lines).rstrip('\n') + '\n'
    out = next(x for x in r['outputs'] if x['id'] == 'document')
    root = Path(r['outputDirectory']).resolve(strict=True)
    target = root / out['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.resolve().is_relative_to(root):
        raise ValueError('output escaped candidate folder')
    with target.open('x', encoding='utf-8', newline='\n') as f:
        f.write(result)
    print(json.dumps({'schema': 'calf.runtime.v1', 'requestId': r['requestId'],
                      'state': 'succeeded', 'providerJobId': None, 'usage': None}))


if __name__ == '__main__':
    main()
