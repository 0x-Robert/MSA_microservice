import time 
import json
from twisted.web import server, resource
from twisted.internet import reactor, endpoints


#동시요청의 수가 증가하고 이를 처리하는 것이 중요하다면 WSGI 표준을 포기하고 토네이도나 트위스티드 같은 비동기 프레임워크를 사용하고싶은 유혹이 들 수 있다.
# 트위스티드는 매우 정교하고 효과적인 프레임워크지만 HTTP 마이크로 서비스로 사용하는데는 다음과 같은 문제가 있다.
# Resource 클래스를 상속받는 클래스로 각 마이크로 서비스의 endpoint를 구현해야하며, 필요한 함수도 구현해야한다.
# 몇개의 단순한 API를 만들기위해 많은 장황한 코드가 추가된다.
# 트위스티드 코드는 비동기적인 성질때문에  이해하기 어렵고 디버그가 힘들다.
# 트리거를 연달아 발생시키기 위해 너무 많은 함수를 연결하면 콜백지옥에 빠지기 쉽다.
# 제대로 테스트하기 어렵다 

class Simple(resource.Resource):
    isLeaf=True
    def render_GET(self,request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        return bytes(json.dumps({'time':time.time()}), 'utf8')

site=server.Site(Simple())
endpoint=endpoints.TCP4ServerEndpoint(reactor,8080)
endpoint.listen(site)
reactor.run()
