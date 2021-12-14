#변수와 컨버터
#라우팅 시스템은 변수라는 기능을 제공함
#<변수_이름>구문을 이용해서 변수를 사용할 수 있음, 이 표기법은 거의 표준처럼 사용되고 있고, 엔드포인트를 동저으로 표현할 수 있음


#고유한 사용자 ID를 N으로 표현한다고 해보자 /person/N에 대한 요청을 처리하는 함수를 만들려면
# route에 /person/<person_id>를 인수로 넘겨주면된다. 아래는 예시다.
# curl localhost:5000/api/person/1007  요청방식 예시
# 여러개의 라우트가 동일 URL에 연결돼 있다면 특정 규칙에 따라 어떤 것을 호출할지 결정한다. 다음규칙은 Werkzeug의 라우팅 모듈에서 가져온 구현 설명이다.
# 1.성능을 위해 인수가 없는 라우트가 먼저 실행된다.
# 더 복잡한 규칙이 우선하므로 두 번째 인수는 가중치의 음수 길이다.
# 마지막으로, 실제 가중치에 따라 호출한다.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello':person_id})
    return response

if __name__ == '__main__':
    app.run()