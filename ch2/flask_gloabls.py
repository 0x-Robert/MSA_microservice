"""
플라스크에서 @app.before_request 데코레이터는 요청이 만들어지고 뷰에 전달하기 직전에 호출할 함수가 있을 때 사용

before_request를 사용하는 일반적인 경우는 전역 공간에 값을 저장할 때다.
이렇게 하면 요청 컨텍스트 안에서 호출되는 모든 함수는 g변수를 사용해서 데이터를 얻을 수 있다.

다음예제에서 HTTP 기본인증을 처리할 때 요청 컨텍스트의 username을 g변수의 user 속성에 저장한다.
 
"""


from flask import Flask , jsonify, g,request 

app = Flask(__name__)

@app.before_request 
def authenticate():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'

@app.route('/api')
def my_microservice():
    return jsonify({'Hello':g.user})

if __name__ == '__main__':
    app.run()

#클라이언트가 /api 엔드포인트를 호출하면 제공된 헤더 정보에 맞는 g.user 값이 authenticate()함수에서 설정된다.
