#abort.mapping 딕셔너리를 통해 에러목록을 얻을 수 있다.
# 다음 예제에서 app.register_error_handler를 사용해 모든 에러에 대해 error_handling 함수를 등록한다.
#JsonApp함수는 플라스크 app인스턴스를 감싼 뒤에 발생 가능한 모든 4xx, 50x에러에 대해
#사용자 정의 JSON 에러 핸들러를 설정한다.
from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions, _aborter

def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {'code': error.code, 'description': error.description,
                        'message': str(error.code) +" " + error.name}
        else:
            description = _aborter.mapping[500].description
            result = {'code': 500, 'description': description,
                        'message': str(error)}
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)
    return app

app = JsonApp(Flask(__name__))

@app.route('/api')
def my_microservice():
    raise TypeError("Some Exception")

if __name__ == '__main__':
    #디버그 모드 실행하면 내장된 디버그를 통해 에러확인 가능
    #디버그 모드는 운영중에 사용하면 보안위험이 있고 해킹된 사례가 있음, 디버거는 원격코드를 실행하기 때문
    
    app.run(debug=True)
