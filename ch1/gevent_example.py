from gevent import monkey; monkey.patch_all()

#아래 한줄추가로 표준동기코드가 소켓을 사용할때마다 마술처럼 비동기가 된다.
from gevent import monkey; monkey.patch_all()

def application(environ,start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    #소켓으로 필요한 작업을 한다.
    return result


#이암시적인 마술에는 대가가 있다.  Gevent가 잘 동작하려면 모든 기본코드가 Gevent 패치와호환되야한다. 특히 C확장을 사용하거나, Gevent가 패치한 일부 기능을 우회하는 경우
#다른 패키지 일부가 계속 차단돼 예상치 못한 결과가 발생할 수 있다.
# 이 코드는 파이어폭스 동기 서비스를 확장하기 위해 이 라이브러리를 사용하기도 했다.

