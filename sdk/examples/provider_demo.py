"""Synthetic adapter example: deliberately fail, repair, then review. No AI call."""
import sys
from calf_sdk import action, emit, plan, read_request, review

request = read_request(sys.argv[-1])
if request["phase"] == "review":
    file = next((f for f in request["files"] if f["path"] == "result.py"), {})
    verdict = "pass" if file.get("content") == "VALUE = 'expected'\n" else "unknown"
    emit(review(request, verdict, "Synthetic fixture: inspect the expected example content only."))
else:
    file = next(f for f in request["files"] if f["path"] == "result.py")
    value = "expected" if request["phase"] == "repair" else "trial"
    emit(plan(request, scope=["result.py", "test_result.py"],
              requirements=[{"id": "value", "text": "Return the expected fixture value", "checks": [c["id"] for c in request["registeredChecks"]]}],
              actions=[action("result.py", "VALUE = " + repr(value) + "\n", file["sha256"])]))
