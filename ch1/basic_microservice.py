import json
import time

#파이썬 커뮤니티는 웹 서버 게이트웨이 인터페이스(WSGI)라는 표준을 만들었다.
#WSGI는 CGI의 영향을 받았으며, 파이썬 어플리케이션이 HTTP요청을 쉽게 처리할 수 있게 한다.
#WSGI의 가장 큰 문제는 동기방식인데 
#아래 APPLICATION함수는 요청이 들어올때마다 호출되고 함수가 종료될  떄 응답을 반환한다. 
def application(environ,start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK',headers)
    return [bytes(json.dumps({'time': time.time()}), 'utf8')]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    srv = make_server('localhost',8080,application)
    srv.serve_forever()
