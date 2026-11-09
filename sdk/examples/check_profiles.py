"""Print locally discovered profiles; does not submit work or run tests."""
import argparse
import json
from pathlib import Path
from calf_sdk import CalfClient, Check

parser = argparse.ArgumentParser()
parser.add_argument("--calf", type=Path, required=True)
parser.add_argument("--home", type=Path, required=True)
parser.add_argument("workspace", type=Path)
args = parser.parse_args()
client = CalfClient(args.calf, args.home)
checks = [Check.from_discovered(c) for c in client.discover_checks(args.workspace)]
print(json.dumps([c.to_dict() for c in checks], ensure_ascii=False, indent=2))
