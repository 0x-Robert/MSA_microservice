"""

현재 서버 시간으로 ETag 값을 생성해서 user 캐시에 사용한다.
ETag 값은 밀리초로 표시하는 epoch 시간이며, user의 modified 필드에 저장된다.

get_user()함수는 _USERS에서 정보를 읽어 반환하고, response.set_etag로 Etag값을 설정한다. 
뷰가 호출되면 If-None-Match 헤더에 설정된 값이 modified 값과 동일한지 검사해서 동일하다면 304 응답을 반환한다.

change_user()함수는 클라이언트가 보낸 POST 요청으로 user 정보를 수정할 때 사용한다.
다음은 etag.py를 실행하고 클라이언트에서 요청을  보냈을 떄의 결과이다.

먼저 1번 user 정보를 얻는다.
다시 POST 요청을 보내 1번 user의 나이벙보를 추가한다.
다시 1번 user 정보를 요청해서 나이 정보가 추가됐는지 확인한다.
마지막 요청을 보낼때는 If-None-Match 헤더에 modified 값을 설정해서 보낸다. 서버의 modified 값과 동일한 값을 설정했으므로 
서버의 응답 코드는 304 NOT MODIFIED다.


curl http://127.0.0.1:5000/api/user/1

{
    "modified":"1639730918679","name":"Tarek"
}

curl -H "Content-Type: application/json" -X POST -d "{\"name\":\"Tarek\",\"age\":40}" http://127.0.0.1:5000/api/user/1
{
    "age":40,"modified":"1639731122972","name":"Tarek"
}



curl http://127.0.0.1:5000/api/user/1
{
    "age":40,"modified":"1639731122972","name":"Tarek"
}


curl -v -H "If-None-Match: 1639731122972" http://127.0.0.1:5000/api/user/1


*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /api/user/1 HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.55.1
> Accept: */*
> If-None-Match: 1639731122972
>
* HTTP 1.0, assume close after body
< HTTP/1.0 304 NOT MODIFIED
< Server: Werkzeug/0.16.0 Python/3.7.4
< Date: Fri, 17 Dec 2021 08:53:49 GMT
<
* Closing connection 0


"""


import json
import time
from flask import Flask,jsonify,request,Response,abort

app = Flask(__name__)

def _time2etag(stamp=None):
    if stamp is None:
        stamp = time.time()
    return str(int(stamp * 1000))

_USERS={'1' : {'name': 'Tarek', 'modified': _time2etag()}}


@app.route('/api/user/<user_id>',methods=['POST'])
def change_user(user_id):
    print(request)

    user=request.json

    #새 타임스탬프 설정
    user['modified'] = _time2etag()
    _USERS[user_id] = user 
    resp = jsonify(user)
    resp.set_etag(user['modified'])
    return resp 


@app.route('/api/user/<user_id>')
def get_user(user_id):
    if user_id not in _USERS:
        return abort(404)
    user = _USERS[user_id]

    #if_none_match와 modified 값이 동일하면 304반환
    if user['modified'] in request.if_none_match:
        return Response(status=304)

    resp = jsonify(user)

    #ETag 설정
    resp.set_etag(user['modified'])
    return resp 

if __name__ == '__main__':
    app.run()
