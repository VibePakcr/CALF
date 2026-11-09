import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import subprocess

from calf_sdk import CalfClient, CalfError, CalfTransportError, Check, ProviderConfig, action, is_satisfied, read_request


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="calf-sdk-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = CalfClient(Path(sys.executable).absolute(), self.root, timeout=5)

    def test_unicode_roundtrip(self):
        result = self.client._invoke(["-c", "import json,sys;print(json.dumps(json.load(sys.stdin)))"], {"text": "한국어 中文 日本語"})
        self.assertEqual(result, {"text": "한국어 中文 日本語"})

    def test_exit_zero_is_not_completion(self):
        for response in ({}, {"requested": True}, {"outcome": "UNKNOWN"}, {"outcome": "FAIL"}):
            self.assertFalse(is_satisfied(response))
        self.assertTrue(is_satisfied({"outcome": "SATISFIED"}))

    def test_errors_remain_errors(self):
        for code in ("print('{\"error\":\"refused\"}')", "import sys;print('{}');sys.exit(2)"):
            with self.assertRaises(CalfError):
                self.client._invoke(["-c", code])

    def test_incomplete_or_ambiguous_response_is_unknown(self):
        for raw in ("", "[]", '{"outcome":', '{"outcome":"SATISFIED","outcome":"UNKNOWN"}', '{"x":NaN}'):
            with self.assertRaises(CalfTransportError):
                self.client._invoke(["-c", "print(" + repr(raw) + ")"])

    def test_bounded_output_and_timeout(self):
        small = CalfClient(Path(sys.executable).absolute(), self.root, timeout=0.5, max_response_bytes=1024)
        with self.assertRaisesRegex(CalfTransportError, "limit"):
            small._invoke(["-c", "print('x'*2048)"])
        children = []
        launch = subprocess.Popen
        def capture(*args, **kwargs):
            child = launch(*args, **kwargs)
            children.append(child)
            return child
        with patch("calf_sdk.client.subprocess.Popen", side_effect=capture):
            with self.assertRaisesRegex(CalfTransportError, "timed out"):
                small._invoke(["-c", "import time;time.sleep(10)"])
        self.assertEqual(len(children), 1)
        self.assertIsNotNone(children[0].poll(), "timed-out API child must be reaped")

    def test_input_rejected_before_launch(self):
        with self.assertRaises(ValueError):
            self.client._invoke([], {"text": "한" * 22000})
        with self.assertRaises(ValueError):
            self.client._invoke([], {"value": float("nan")})
        with self.assertRaises(ValueError):
            CalfClient(Path(sys.executable).absolute(), "relative")
        with self.assertRaises(ValueError):
            self.client.call("list", home=str(self.root / "another-home"))

    def test_config_never_overwrites(self):
        check = Check("unit", [sys.executable, "-m", "unittest"], ["test_result.py"])
        config = ProviderConfig([sys.executable, "adapter.py"], [check])
        target = self.root / "provider.json"
        config.write_new(target)
        before = target.read_bytes()
        with self.assertRaises(FileExistsError):
            config.write_new(target)
        self.assertEqual(target.read_bytes(), before)
        config.max_attempts = 0
        with self.assertRaises(ValueError):
            config.to_dict()
        config.max_attempts = 4
        config.command = "/not-an-argv-array"
        with self.assertRaises(ValueError):
            config.to_dict()

    def test_discovered_profile_is_preserved_and_detached(self):
        raw = {"id": "pytest-tests", "command": [sys.executable, "check-profile", "pinned"],
               "inputs": ["test_result.py"], "envKeys": [], "class": "light",
               "profile": {"schema": 2, "kind": "pytest", "targets": ["test_result.py"]}}
        check = Check.from_discovered(raw)
        self.assertEqual(check.to_dict(), raw)
        raw["profile"]["targets"].append("other.py")
        output = check.to_dict()
        self.assertNotEqual(output, raw)
        output["profile"]["targets"].clear()
        self.assertEqual(check.to_dict()["profile"]["targets"], ["test_result.py"])
        with self.assertRaises(ValueError):
            Check.from_discovered({"id": "incomplete"})
        check.profile = {"schema": 3, "kind": "node-test", "nodeVersion": "v24.1.0", "targets": ["example.test.ts"]}
        self.assertEqual(check.to_dict()["profile"], check.profile)
        check.profile = {"schema": 99}
        with self.assertRaises(ValueError):
            check.to_dict()

    def test_provider_identity_and_create_only(self):
        request = self.root / "request.json"
        request.write_text(json.dumps({"schema": 1, "phase": "plan", "requestHash": "0" * 64}))
        self.assertEqual(read_request(request)["phase"], "plan")
        request.write_text('{"schema":1,"phase":"plan","requestHash":"missing"}')
        with self.assertRaises(ValueError):
            read_request(request)
        self.assertIsNone(action("new.py", "new", None)["expectedSha"])
        with self.assertRaises(ValueError):
            action("new.py", "x" * 32769, None)


if __name__ == "__main__":
    unittest.main()
