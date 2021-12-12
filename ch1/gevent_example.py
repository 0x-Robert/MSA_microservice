from gevent import monkey; monkey.patch_all()

#아래 한줄추가로 표준동기코드가 소켓을 사용할때마다 마술처럼 비동기가 된다.
from gevent import monkey; monkey.patch_all()

def application(environ,start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    #소켓으로 필요한 작업을 한다.
    return result

    