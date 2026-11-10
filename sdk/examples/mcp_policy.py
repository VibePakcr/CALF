"""Inspect or prepare an existing reviewed policy; never execute its tool."""
import argparse
import json
from calf_sdk import CalfClient

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--core', required=True)
parser.add_argument('--home', required=True)
parser.add_argument('--policy', required=True)
parser.add_argument('--sha256', required=True)
parser.add_argument('--request', help='JSON request file: prepare only; omitted means status')
args = parser.parse_args()
client = CalfClient(args.core, args.home)
if args.request:
    with open(args.request, encoding='utf-8') as stream:
        request = json.load(stream)
    result = client.prepare_tool(args.policy, args.sha256, request)
else:
    result = client.tool_status(args.policy, args.sha256)
print(json.dumps(result, ensure_ascii=False, indent=2))
