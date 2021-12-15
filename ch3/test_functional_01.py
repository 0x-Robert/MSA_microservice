"""
마이크로서비스에서 기능 테스트란 게시된 API에 HTTP요청을 보내서 응답을 검증하는 모든 테스트를 말한다.
이 정의는 애플리케이션을 호출하는 모든 테스트, 예를 들면 퍼징(Fuzzing) 테스트부터 침투(Penetration)테스트, 또는 그 외의 것들을 포함할만큼
광범위하다. 여기서 퍼징 테스트는 고의로 유효하지 않은 무작위 데이터를 보내서 애플리케이션의 이상 여부를 검증하며, 침투 테스트는 보안 취약점을 찾는다.

기능 테스트는 다음 2가지를 중요하게 다뤄야한다.
1. 애플리케이션 기능이 의도대로 동작하는지 확인하는 테스트
2. 잘못된 동작을 수정한 후 더이상 해당 동작이 발생하지 않는지 확인하는 테스트

보통은 테스트 클래스에서 애플리케이션의 인스턴스를 생성해 연동한다.

실제 네트워크 호출은 일어나지 않으며, 테스트가 직접 애플리케이션을 호출하는 방식으로 동작한다.

테스트가 제대로 되려면 애플리케이션 내부에서 발생하는 모든 네트워크 호출 부분을 모방해야 한다.

test_client()함수를 사용하면 app객체에서 곧바로 FlaskClient 인스턴스를 만들 수 있따. FlaskClient는 요청을 보내기 위해 사용된다.



FlaskClient클래스는 예제에서 사용된 get()처럼 http 메소드에 대응하는 함수를 갖고 있다. 이 함수들은 Response 객체를 반환해서 결과를 검증한다.
"""

import unittest 
import json
import sys 
sys.path.append('../ch2')
from flask_basic import app as _app


#테스트에 성공하면 .이 찍힌다. 1개 통과하면 1개 찍힘

class TestApp(unittest.TestCase):
    def test_help(self):
        #app과 연동하기 위해 FlaskClient 인스턴스를 생성한다.
        app = _app.test_client()

        #/api 엔드포인트를  호출한다.
        hello=app.get('/api')

        #응답을 검사한다.
        body = json.loads(str(hello.data,'utf8'))
        print(body)
        #body['Hello'] 밸류와 World가 같은지 체크,     ,를 사이에두고 양옆에 값이 같은지 테스트 

        #self.assertEqual(custom_function(self.file_name), 3) 구문은 custom_function(file_name) 을 수행하고 결과가 3이면 테스트를 통과합니다.
        self.assertEqual(body['Hello'], 'World!')

if __name__ == "__main__":
    unittest.main()
