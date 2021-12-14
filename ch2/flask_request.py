from flask import Flask, request 

app = Flask(__name__)


""""
핵심은 뷰가 request 객체 속성을 사용해서 간단히 클라이언트로부터의 요청을 검토 할  수 잇다는 점이다.
플라스크가 처리하는 이 작업은 꽤 고수준의 작업이다. 

예를 들어 승인과 관련된 정보가 요청에 포함돼 있다면 자동으로 Authorization헤더가 검색돼 분리된다.

코드를 통해 알아보자 , 다음예제에서 클라이언트가 보내는 HTTP 기본 인증은 서버로 보내질 때 Basic 접두사 + base64 형태로 변환된다.
플라스크가 Basic 접두사를 감지하고 request.authorization 내의 username과 password 필드로 파싱된다.

요청예제 
curl localhost:5000 -u tarek:password

응답
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
The raw Authorization header
Basic dGFyZWs6cGFzc3dvcmQ=
Flask's Authorization header
{'username': 'tarek', 'password': 'password'}
127.0.0.1 - - [14/Dec/2021 10:05:44] "GET / HTTP/1.1" 200 -

"""

@app.route("/")
def auth():
    print("The raw Authorization header")
    print(request.environ["HTTP_AUTHORIZATION"])
    print("Flask's Authorization header")
    print(request.authorization)
    return ""

if __name__ == "__main__":
    app.run()
