from flask import Flask,jsonify,request

#WSGI Web Server Gateway Interface
#파이썬 웹커뮤니티는 WSGI라는 표준을 만들었고, CGI(Common Gateway Interface)의 영향을 받았으며, 파이썬 어플리케이션이 HTTP 요청을 쉽게 처리할 수 있게 한다.
#이표준에 따라 개발딘 애플리케이션은 uwsgi나 mod_wsgi같은 WSGI확장을 사용해 아파치,nginx 등의 웹서버에서 실행할 수 있다.

#플라스크는 WSGI 프로토콜을 사용해 HTTP 요청을 처리하는 Werkzeug WSGI툴킷과 기타 라우팅 시스템과같은 다양한 도구들을 기반으로 2010년부터 배포되기 시작했다.


#플라스크 앱이 실행되고 요청이 들어와서 응답을 반환할때 다음 과정을 거친다.
# 라우팅 : 플라스크가 Map 클래스를 생성한다.
# 요청: 플라스크가 Request 객체를 뷰에 전달한다.
# 응답: Response 객체에 필요한 내용을 채워서 응답을 보낸다. 

#라우팅
#라우팅은 Werkzeug Map 클래스의 인스턴스인 app.url_map에서 일어남, 이 클래스는 정규표현식을 사용해 클라이언트에서 호출한 엔드포인트와 일치하는
# @app.route로 데코레이트된 함수를 찾는다.
# 기본적으로 라우팅은  HTTP 메소드 중 HEAD, GET , OPTIONS만 받아들인다.
#지원하지 않는 HTTP 메소드를 사용하면 405가 반환됨

app=Flask(__name__)

#다른 HTTP 메소드도 라우팅하고 싶다면 route 데코레이터에 전달되는 method 인수에 필요한 http 메소드를 추가하면된다.
@app.route('/api', methods=['POST','DELETE','GET'])
def my_microservice():
    print(request)
    print(request.environ)
    response=jsonify({'Hello':'World!'})
    print(response)
    print(response.data)
    return response 

if __name__ == '__main__':
    print(app.url_map)
    app.run()
