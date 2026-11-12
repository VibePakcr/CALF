"""Inspect first; create a new note only with explicit --create-note.

Usage / 사용법: python managed_artifact.py --help
The task must already be registered in the selected journal.
선택한 저널에 이미 등록된 작업을 사용합니다. 기존 파일은 변경하지 않습니다.
"""
import argparse
import json
from pathlib import Path
from calf_sdk import CalfClient

parser = argparse.ArgumentParser(description=__doc__)
for name in ("binary", "home", "workspace", "state"):
    parser.add_argument("--" + name, type=Path, required=True)
parser.add_argument("--task")
parser.add_argument("--request-id")
parser.add_argument("--create-note", help="Create this new disposable text; never reads an existing file")
args = parser.parse_args()
client = CalfClient(args.binary, args.home)
if args.create_note is None:
    result = client.artifacts(args.workspace, operation="plan", state=args.state)
else:
    if not args.task or not args.request_id:
        parser.error("--create-note requires --task and a stable --request-id")
    result = client.artifacts(args.workspace, operation="create", state=args.state, task=args.task,
                              requestId=args.request_id, role="temporary", label="Example note",
                              content=args.create_note, retentionSeconds=86400, confirm=True)
print(json.dumps(result, ensure_ascii=False, indent=2))
