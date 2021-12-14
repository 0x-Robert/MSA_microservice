from flask import Flask 
import yaml #PyYAML 필요함.

"""
응답 : jsonify()는 뷰가 반환하는 매핑에서 Response 객체를 생성한다.
기술적으로 Response객체는 직접 사용할 수 있는 표준 WSGI 애플리케이션이다. Response는 플라스크에 감싸져 웹 서버로부터 받는 WSGI environ 딕셔너리 및 start_response 함수와 함께 호출된다.

플라스크가 URL 매퍼를 통해 호출할 뷰를 선택하면 environ 사전과 start_response인수를 받을 수 있는 호출 가능한 객체가 반환되기를 기대한다.

반환된 값이 호출될 수 없는 경우 다음중 하나에 해당하면 flask가 response객체로 바꾸려고 시도한다.
str: 데이터는 UTF-8로 인코딩되고 HTTP 응답의 바디로 사용된다.
bytes/bytesarray:바디로 사용된다.
(response, status,headers)튜플: response는 Response객체나 앞의 타입(str,bytes)중 하나가 될 수 있다. status는 정수 타입의 응답 코드이고, header는 딕셔너리 타입의 응답 헤더다.
(response,status)튜플 : header가 없는 것외에는 앞과 동일하다.
(response,header)튜플 : 앞과 동일하지만 추가로 header가 있다.


일반적으로 마이크로 서비스를 개발할 때는 jsonify()함수를 사용한다. 하지만 다른 타입을 반환해야 할 때는 생성된 데이터를 Response클래스로 변환하는 함수를
쉽게 만들어 쓸 수 있다. YAML 타입을 반환하는 코드를 보자

Yamlify()반환하는 (response, status, headers)튜플은 플라스크에 의해 적절한 Response 객체로 변환된다.


"""
app = Flask(__name__)

def yamlify(data,status=200,headers=None):
    _headers={'Content-Type': 'application/x-yaml'}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers 

@app.route('/api')
def my_microservice():
    return yamlify(['Hello', 'YAML', 'World!'])

if __name__ == '__main__':
    app.run()







