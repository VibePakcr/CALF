import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from calf_sdk import CalfClient
from calf_sdk.work import read_work_request, runtime_result, validation_result, input_reference


class WorkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='calf-work-sdk-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = CalfClient(Path(sys.executable).absolute(), self.root)

    def test_dispatch_is_native_and_not_direct_journal_write(self):
        with patch.object(self.client, '_invoke', return_value={'outcome':'UNKNOWN'}) as call:
            self.client.work('submit', spec={'key':'abc'})
            self.assertEqual(call.call_args.args, (['api'], {'op':'work','home':str(self.root),'action':'submit','spec':{'key':'abc'}}))
        self.assertEqual(list(self.root.iterdir()), [])

    def test_endpoint_default_read_only_and_control_explicit(self):
        self.assertEqual(self.client.work_mcp_server()['args'], ['work-mcp',str(self.root)])
        self.assertEqual(self.client.work_mcp_server(control=True)['args'][-1], '--control')

    def test_no_unknown_action_or_home_override(self):
        with self.assertRaises(ValueError):self.client.work('exec',command='anything')
        with self.assertRaises(ValueError):self.client.work('list',home='/different')

    def test_duplicate_keys_and_invalid_protocol_rejected(self):
        p=self.root/'request.json'
        for raw in ['{"schema":"a","schema":"calf.runtime.v1"}', '{"schema":"other"}', '[]']:
            p.write_text(raw)
            with self.assertRaises(ValueError):read_work_request(p)

    def test_reference_is_exact_utf8_identity(self):
        p=self.root/'한국어.txt';p.write_bytes('한글 中文 日本語'.encode())
        value=input_reference(p,'source','text/plain')
        self.assertEqual(value['sha256'],hashlib.sha256(p.read_bytes()).hexdigest())
        self.assertEqual(value['path'],str(p.resolve()))

    def test_validator_binds_exact_manifest_and_check(self):
        r={'schema':'calf.runtime.v1','requestId':'w:1','operation':'validate','extra':{'check':{'id':'quality'},'manifest':{'digest':'a'*64}}}
        v=validation_result(r,'UNKNOWN','Unavailable')
        self.assertEqual((v['requestId'],v['checkId'],v['manifestDigest']),('w:1','quality','a'*64))
        with self.assertRaises(ValueError):validation_result(r,'PASS','not a verdict')
        with self.assertRaises(ValueError):runtime_result(r,'complete')

    def test_protocol_input_bound(self):
        p=self.root/'request.json';p.write_bytes(b' ' * 65537)
        with self.assertRaises(ValueError):read_work_request(p)


if __name__=='__main__':unittest.main()
