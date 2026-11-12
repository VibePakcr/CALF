import unittest
from calf_sdk import CalfClient


class Client(CalfClient):
    def __init__(self):
        self.calls = []

    def call(self, op, **fields):
        self.calls.append((op, fields))
        return fields


class PersonalEntry(unittest.TestCase):
    def test_handoff_is_preview_only_unless_explicitly_confirmed(self):
        client = Client()
        preview = client.handoff("task")
        self.assertEqual(preview["action"], "preview")
        self.assertFalse(preview["includeRequest"])
        with self.assertRaises(ValueError):
            client.handoff("task", confirm=True)
        self.assertEqual(len(client.calls), 1)
        exported = client.handoff("task", digest="a" * 64, confirm=True)
        self.assertEqual(exported["action"], "export")
        self.assertEqual(exported["digest"], "a" * 64)

    def test_templates_cannot_override_transport_or_dispatch_work(self):
        client = Client()
        for fields in [{"home": "/other"}, {"op": "submit"}, {"workspace": "/other"}]:
            with self.assertRaises(ValueError):
                client.request_templates(**fields)
        self.assertEqual(client.calls, [])
        client.request_templates()
        self.assertEqual(client.calls, [("request_templates", {"action": "list"})])
