"""
플라스크는 시그널 라이브러리인 Blinker를 통합한다.
이 라이브러리는 특정 이벤트를 구독 했다가 이벤트가 발생했을 때 필요한 함수를 실행한다.


이벤트란 고유한 이름표 label을 가지고  blinker.signal 클래스를 통해 
생성된 인스턴스다. 플라스크 0.12는 요청을 처리하던 중 중요한 순간마다 총 10개의 시그널을 발생시킨다.
전체목록은 http://flask.pocoo.org/docs/latest/api/#core-signals-list를 참고하자.

시그널 connect 함수를 사용해서 특정이벤트 등록가능
시그널은 코드가 시그널의 send 함수를 호출하면 트리거됨
send 함수는 추가적인 인수를 받아서 모든 등록된 함수에 데이터를 전달함

다음예제에서 request_finished 시그널에 finished 함수를 등록한다. 
이 함수는 응답 객체를 받는다.
"""

from flask import Flask, jsonify,g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")

app = Flask(__name__)

def finished(sender, response, **extra):
    print('About to send a Response')
    print(response)

request_finished.connect(finished)


@app.route('/api')
def my_microservice():
    return jsonify({'Hello':'World'})

if __name__ == '__main__':
    app.run()


#요청객체가 만들어지고, 처리되고 소멸되는 과정에서 발생하는 시그널들은 로그를 남길때 유용하다.
#코드와 분리된 채로 이벤트를 사용해서 어떤 기능을 처리하고 싶다면 어플리케이션에 사용자 정의 시그널을 구현할 수도 있다.

#예를 들어 pdf 보고서를 생성하고 보고서에 암호화된 서명을 하고 싶다면 report_ready 시그널을 만들어 필요한 함수를 등록할 수 있다.

