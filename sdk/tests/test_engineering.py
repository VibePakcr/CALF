import unittest
from calf_sdk import CalfClient, is_satisfied


class Client(CalfClient):
    def __init__(self):
        self.calls = []

    def call(self, op, **fields):
        self.calls.append((op, fields))
        return fields


class Engineering(unittest.TestCase):
    def test_read_only_transport_preserves_cjk_and_exact_source_digest(self):
        client = Client()
        client.knowledge("resolve", query="데이터베이스 쿼리 성능", byteBudget=8192)
        self.assertEqual(client.calls, [("knowledge", {"request": {
            "action": "resolve", "query": "데이터베이스 쿼리 성능", "byteBudget": 8192,
        }})])
        client.knowledge("read", id="doc:0", sha256="a" * 64)
        self.assertEqual(client.calls[-1][1]["request"]["sha256"], "a" * 64)
        self.assertFalse(is_satisfied({"currentCompletion": "NOT_EVALUATED"}))

    def test_no_execution_import_or_transport_override(self):
        client = Client()
        for action in ["import", "execute", "delete"]:
            with self.assertRaises(ValueError):
                client.knowledge(action)
        for fields in [{"home": "/other"}, {"op": "submit"}, {"workspace": "/other"}]:
            with self.assertRaises(ValueError):
                client.knowledge(**fields)
        self.assertEqual(client.calls, [])
