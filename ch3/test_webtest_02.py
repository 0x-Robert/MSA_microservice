"""
통합테스트는 로컬 WSGI의 인스턴스 대신 실제 배포된 서버를 호출한다는 것만 제외하면 기능 테스트와 유사하다. 
WebTest는 파이썬 앱에 대한 호출을 실제 http애플리케이션에 대한 http 요청으로 변환해주는 WSGIProxy2 라이브러리를 사용하는데,
이 기능을 활용하면 약간의 변경으로 통합테스트와 기능 테스트를 모듈 하나에 작성할 수 있다.

다음예제는 앞의01 코드를 약간 수정했는데 HTTP_SERVER 환경변수를 설정했다면 통합 테스트로 실행된다.


HTTP_SERVER=http://myservice/ 로 환경 변수를 설정하고 테스트를 실행했다면 모든 호출을 http://myservice/로 보낸다.
이 방법은 두 개의 분리된 테스트를 만들지 않고도 기능테스트를 쉽게 통합테스트로 전환할 수 있게 해준다. 

"""

import unittest
import os
import sys 
sys.path.append('../ch2')

class TestMyApp(unittest.TestCase):

    def setUp(self):
        #HTTP_SERVER 환경 변수가 설정됐다면
        # 그 값을 엔드포인트로 사용한다.(통합 테스트)
        http_app = os.environ.get('HTTP_SERVER')
        if http_app is not None:
            from webtest import TestApp 
            self.app = TestApp(http_app)

        else:
            #WSGI 애플리케이션을 호출한다. (기능 테스트).
            from flask_basic import app
            from flask_webtest import TestApp 
            self.app = TestApp(app)

    def test_help(self):
        #/api 엔드포인트를 호출한다. 
        hello = self.app.get('/api')

        #응답을 검사한다.
        self.assertEqual(hello.json['Hello'], 'World!')

if __name__ == "__main__":
    unittest.main()



