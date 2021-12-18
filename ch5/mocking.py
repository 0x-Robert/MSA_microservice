'''
동기식 호출 모방

다음 테스트에서는 session.mount()에 새로운 requests_mock.Adapter()인스턴스를 전달해서 
requests_mock 어댑터를 세션에 마운트한다.

'''

import json
import unittest 
from flask_session import setup_connector, get_connector
from flask_webtest import TestApp
import requests_mock
import sys

sys.path.append('../ch2')

class TestAPI(unittest.TestCase):
    def setUp(self):
        from flask_basic import app as _app
        self.app = TestApp(_app)
        setup_connector(_app)

        #요청을 모방한다.
        session=get_connector(_app)
        self.adapter = requests_mock.Adapter()
        session.mount('http://', self.adapter)

    def test_api(self):
        mocked_value=json.dumps({'Hello':'World!'})
        self.adapter.register_uri('GET','http://127.0.0.1:5000/api',text=mocked_value)
        res=self.app.get('/api')
        self.assertEqual(res.json['Hello'],'World!')

if __name__ == '__main__':
    unittest.main()