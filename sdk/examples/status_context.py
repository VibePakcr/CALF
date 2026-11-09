"""Read saved/current status. No check execution, AI call or environment edits."""
import argparse
import json
from pathlib import Path
from calf_sdk import CalfClient, is_satisfied

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("executable", type=Path)
parser.add_argument("home", type=Path)
parser.add_argument("workspace", type=Path)
parser.add_argument("task")
args = parser.parse_args()
client = CalfClient(args.executable, args.home)
status = client.registered_status(args.workspace, args.task)
print(json.dumps({"currentOutcome": status.get("outcome"),
                  "currentSatisfied": is_satisfied(status),
                  "diagnostics": status.get("statusView")}, ensure_ascii=False, indent=2))
