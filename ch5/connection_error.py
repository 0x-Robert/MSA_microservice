"""
연결이 끊기거나 서버에 접속할 수 없다면 또 다른 에러가 발생한다. 이 경우는 요청이 여러번 시도된 뒤에
ConnectionError가 발생한다. 다음 코드는 ConnectionError가 발생했을 때 request_timeout.py와 동일하게 비어있는 응답을 반환한다.
"""


from flask import Flask ,jsonify
from requests.exceptions import ConnectionError
from flask_session import setup_connector,get_connector

app=Flask(__name__)
setup_connector(app)

@app.route('/api',methods=['GET','POST'])
def my_microservice():
    with get_connector(app) as conn:
        try:
            result=conn.get('http://localhost:5000/api',timeout=2.0).json()
        except ConnectionError:
            result={}
    return jsonify({'result':result, 'Hello':'World!'})

if __name__ == '__main__':
    app.run(port=5001)