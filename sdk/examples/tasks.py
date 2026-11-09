"""Read records by default. Submission requires an explicit request argument."""
import argparse
import json
from calf_sdk import CalfClient

parser = argparse.ArgumentParser()
parser.add_argument("--calf", required=True, help="Absolute path to the released calf / calf.exe")
parser.add_argument("--home", required=True, help="Existing Workbench records home")
parser.add_argument("--workspace")
parser.add_argument("--request")
args = parser.parse_args()
client = CalfClient(args.calf, args.home)
if args.request is not None:
    if args.workspace is None:
        parser.error("--request requires --workspace")
    result = client.submit(args.workspace, args.request)
else:
    result = client.tasks()
print(json.dumps(result, ensure_ascii=False, indent=2))
