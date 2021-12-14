from flask import Flask , jsonify

# 이 앱은 /api를 호출하면 응답으로 JSON데이터를 반환해주고 이외호출은 404에러를 반환한다.
# 단일 파이썬 모듈을 실행하면 __name__ 변수값은 애플리케이션 패키지 이름인 __main__이다. 플라스크가 새로운 로거 인스턴스를 생성하고
# 디스크에서 파일 위치를 찾을 때 이 이름을 사용한다. 플라스크는 앱 설정처럼 헬퍼를 위한 루트로서 이 디렉토리를 사용하며 static과 templates디렉토리의 기본위치를 결정한다.
# jsonify()함수는 Response 객체를 생성하고 매핑을 본문에 출력한다.
# 많은 웹프레임워크가 request객체를 코드로 전달하는 데 반해 , 플라스크는 암시적인 전역 request 변수를 사용한다. 
# 전역  request 변수는 내부적으로 HTTP 요청을 WSGI 환경 변수 딕셔너리로 파싱해서 만든 Request 객체를 가리키고 있다.


app = Flask(__name__)

@app.route('/api')
def my_microservice():
    return jsonify({'Hello':'World!'})

if __name__ == "__main__":
    app.run()
    