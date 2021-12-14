from flask import Flask, jsonify,request 
import json 

"""
다음예제에서 미들웨어는 X-Forwarded-For 헤더를 사용해서 플라스크앱이 nginx같은 프록시 뒤에 있다고 속인다.
이렇게 하면 테스트환경에서 유용한 미들웨어를 만든다.

"""

class XFFMiddleware(object):
    def __init__(self,app,real_ip='10.1.1.1'):
        self.app = app 
        self.real_ip = real_ip 

    #wsgi 앱은 실제 응답본문을 돌려주기 전에 start_response함수가 응답상태코드,헤더와 함께 호출된다. 
    #다른 WSGI프레임워크를 사용해야하는 기능이 아니라면 WSGI 미들웨어로 앱을확장할 필요는 없다.
    def __call__(self,environ,start_response):
        if 'HTTP_X_FORWARDED_FOR' not in environ:
            values = '%s, 10.3.4.5, 127.0.0.1' % self.real_ip
            environ['HTTP_X_FORWARDED_FOR'] = values 
        return self.app(environ,start_response)

app=Flask(__name__)
app.wsgi_app =XFFMiddleware(app.wsgi_app)

@app.route('/api')
def my_microservice():
    if "X-Forwarded-For" in request.headers:
        ips = [ip.strip() for ip in request.headers['X-Forwarded-For'].split(',')]
        ip=ips[0]
    else:
        ip=request.remote_addr
    return jsonify({'Hello':ip})

if __name__ == "__main__":
    app.run()
