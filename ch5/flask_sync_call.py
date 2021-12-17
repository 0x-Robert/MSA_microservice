"""
다음 코드는 플라스크 앱에서 5001 포트에서 요청을 기다린다. 그리고 요청이 들어오면 응답을 만들기 위해 
5000포트에서 실행되고 있는 또 다른 마이크로 서비스를 동기식으로 호출한다.
"""

from flask import Flask, jsonify 
# flask_Session.py를 import 해서 하기의 함수들을 쓴다.
# 저장된 세션을 이용하기 위함
from flask_session import setup_connector, get_connector 

app = Flask(__name__)
setup_connector(app)

@app.route('/api', methods=['GET','POST'])
def my_microservice():
    with get_connector(app) as conn:
        sub_result = conn.get('http://localhost:5000/api').json()
    return jsonify({'result': sub_result, 'Hello':'World!'})
if __name__ == "__main__":
    app.run(port=5001)


"""
위 코드의 문제점은 모든것이 기대한대로 동작할 것이라는 안이한 생각을 하는 것이다.
마이크로서비스 호출에 지연이 발생해서 응답 반환에 30초가 걸린다면 어떻게 될까?

기본적으로 요청은 응답이 준비될 때까지 행(hang)이 걸리므로  마이크로서비스를 호출할 때는 이런 상황을 피해야한다.


"""