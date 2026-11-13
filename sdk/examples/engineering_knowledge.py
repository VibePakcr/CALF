"""Read-only example: python engineering_knowledge.py CALF_ABSOLUTE DATA_HOME_ABSOLUTE"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from calf_sdk import CalfClient

client = CalfClient(sys.argv[1], sys.argv[2])
view = client.knowledge("resolve", query="database query performance", byteBudget=8192)
assert view["executionAuthority"] is False
assert view["currentCompletion"] == "NOT_EVALUATED"
print(json.dumps(view, ensure_ascii=False, indent=2))
