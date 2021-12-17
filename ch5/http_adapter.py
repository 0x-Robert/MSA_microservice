"""
세션레벨에 기본 값을 설정하는 방법도 있다.
이를 위해 requests 라이브러리의 전송 어댑터 기능을 사용한다. 
이 기능을 사용하면 세션이 호출하는 특정 호스트에 대한 동작을 정의할 수 있는데, 타임아웃을 설정하거나 서비스가 응답하지 않을 때의 
재시도 횟수를 retires 옵션으로 지정가능하다.

어댑터에 timeout과 retires 옵션을 추가해 모든 요청에 기본 값으로 사용되게 아래 코드를 작성했다.
"""

from requests import adapters
from requests.adapters import HTTPAdapter
from requests import Session

class HTTPTimeoutAdapter(HTTPAdapter):
    def __init__(self, *args , **kw):
        self.timeout = kw.pop('timeout',30.)
        print('self.timeout=', self.timeout)
        super().__init__(*args, **kw)
    
    def send(self,request,**kw):
        timeout = kw.get('timeout')
        if timeout is None:
            kw['timeout'] = self.timeout
        return super().send(request,**kw)

def setup_connector(app,name='default',**options):
    if not hasattr(app,'extensions'):
        app.extensions={}
    if 'connector' not in app.extensions:
        app.extensions['connectors'] = {}
    session=Session()

    if 'auth' in options:
        session.auth = options['auth']

    headers=options.get('headers',{})

    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    session.headers.update(headers)

    retries=options.get('retries',3)

    #timeout은 아래 두가지 중 하나의 방법으로 설정한다. 
    #1) 하나의 float 값으로 connect/read timeout을 동일하게 설정
    #2) 하나의 float 튜플로 connect/read timeout을 다르게 설정
    timeout=options.get('timeout',(5.0,3.0)) #2) 방법 사용

    adapters = HTTPTimeoutAdapter(max_retries=retries,timeout=timeout)
    #session.mount()함수는 이제부터 모든 HTTP 서비스를 호출할 때 requests 라이브러리가 HTTPTimeoutAdapter를 사용하게 한다.
    # host 인수로 사용된 http://은 모든 HTTP 호출을 뜻한다.
    """
    mount()함수의 뛰어난 점은 애플리케이션 로직에 따라 각 서비스별로 세션의 동작을 조정할 수 있다는 것이다. 
    예를 들어 특정 서비스에 대해서는 재시도 횟수와 타임아웃값을 다르게 설정하고 싶다면 어댑터 인스턴스를 새로 만들어 연결할 수 있다.
    adapter2 = HTTPTimeoutAdapter(max_retries=1, timeout=1.)
    session.mount('http://myspecial.service',adapter2)
    이 기능 덕분에  하나의 요청 Session 객체를 애플리케이션에 저장해두고 여러개의 HTTP 서비스와 연동하는 데 사용할 수 있다.
    
    """
    session.mount('http://',adapter)
    app.extensions['connectors'][name] = session
    return session

def get_connector(app, name='default'):
    return app.extensions['connectors'][name]



