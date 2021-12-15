import unittest 
import sys
sys.path.append('../ch2')
from flask_basic import app as _app

"""

WebTest는 FlaskTest처럼 WSGI 애플리케이션에 대한 호출을 감싸서 연동할 수 있게 한다.
또한 JSON 처리에 관한 추가적인 유틸리티와 비 WSGI 애플리케이션을 호출하기위한 기능도 제공한다.


"""
class TestMyApp(unittest.TestCase):
    def setUp(self):
        from webtest import TestApp
        #app과 연동하기 위한 클라이언트를 생성한다.
        self.app = TestApp(_app)

    def test_help(self):
        #/api 엔드포인트를 호출한다.
        hello=self.app.get('/api')

        #응답을 검사한다.
        self.assertEqual(hello.json['Hello'], 'World!')

if __name__ == "__main__":
    unittest.main()
