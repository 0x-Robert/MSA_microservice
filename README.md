# MSA_microservice
# 파이썬 마이크로 서비스 스터디

## microservice는 마이크로서비스 기본 구조
일반적인 어플리케이션이며, 순환구조를 구현해서, 마이크로서비스개발의 시작점으로 사용가능

## Flakon은 또 다른 샘플프로젝트를 사용함
Flakon은 INI와 JSON을 사용해서 플라스크 애플리케이션의 구성과 초기화를 담당함


### micro service의 기본 구조는 다음과 같다.

* setup.py : Distuil의 설정 파일로 프로젝트를 설치하고, 릴리스하는 데 사용
* Makefile : 프로젝트를 만들고 빌드하고 실행하기 위해 필요한 명령을 포함
* setting.ini : 애플리케이션 기본 설정이 들어있는 INI파일
* requirement.txt : pip형식을 따르는 프로젝트 의존성이 들어있음
* myservice/:
    * __init__.py 
    * app.py : app모듈
    * views/: 블루프린트를 구성하는 뷰를 포함한 디렉토리
        * __init__.py
        * home.py 루트 엔드포인트를 처리하는 home 블루프린트
* tests : 모든 테스트를 포함하는 디렉토리
    * __init__.py
    * test_home.py : home 블루프린트 뷰를 위한 테스트

app.py파일의 다음 코드는 Flakon의 create_app 헬퍼를 사용해서 
플라스크 app을 초기화 한다. create_app은 등록하려는 블루프린트 목록 같은 몇 개의 옵션을 인수로 받는다.

****

import os
from flakon import create_app
from myservice.views import blueprints

_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

app = create_app(blueprints=blueprints,settings=_SETTINGS)

****

home.py 뷰는 Flakon의 JsonBlueprint 클래스를 사용한다. JsonBlueprint는 앞절에서
살펴봤던 에러 처리를 구현했다. 또한 Bottle프레임워크가 하는 것처럼 뷰가 반환하는 
객체가 딕셔너리라면 자동으로 jsonify()를 호출한다.

from flakon import JsonBlueprint
home = JsonBlueprint('home',__name__)

@home.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping
    """

    return {}

이 애플리케이션은 패키지 이름을 사용해서 플라스크의 기본명령으로 실행가능
FLASK_APP=myservice flask run

이로써 마이크로서비스에 대한 JSON 뷰를 빌드하는 것은 microservice/view에 필요한 모듈을 추가하고 관련된 테스트를 만드는 것으로 구성함



****


플라스크 마이크로서비스 요약


1. 플라스크는 WSGI 프로토콜로 단순한 요청/응답 메커니즘을 감싸고 있다. 
이렇게 해서 거의 표준 라이브러리만 사용해 애플리케이션을 개발할 수 있게 한다.

2. 플라스크는 쉽게 확장가능
3. 플라스크는 블루프린트,전역,시그널,템플릿 엔진,에러 핸들러, 디버거 같은 기능제공
4. microservice 플라스크의 기본 구조를 구현한 프로젝트로 설정파일로 INI파일을 사용하며, JSON으로 응답객체를 생성해 반환하는 단순한 앱이다.