"""Preview a task summary locally. This example does not export or upload it."""
import argparse
import json
from calf_sdk import CalfClient

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("executable")
parser.add_argument("home")
parser.add_argument("task")
args = parser.parse_args()
client = CalfClient(args.executable, args.home)
preview = client.handoff(args.task)
validation = client.validate_handoff(preview)
assert validation["currentVerdict"] == "NOT_EVALUATED"
assert validation["executionAuthority"] is False
print(json.dumps({"preview": preview, "validation": validation}, ensure_ascii=False, indent=2))
