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





### 테스트
* 마이크로서비스에서는 다음과 같은 5개 테스트로 분류한다.

1. 단위 테스트(Unit Test): 격리된 환경에서 클래스나 함수가 예상대로 동작하는지 확인한다.
2. 기능 테스트(Functionall test): 마이크로서비스가 고객의 관점에서 기대한 대로 동작 하는지 살피고, 잘못된 요청에 대해서도 정확히 응답하는지 검증한다.
3. 통합 테스트(Integration test): 마이크로서비스가 다른 서비스와 제대로 연동되는지 확인한다.
4. 부하 테스트(Load test) : 마이크로서비스의 성능을 측정한다.
5. 엔드 투 엔드 테스트 : 전체 시스템이 제대로 동작하는지 확인한다.

 


####  통합테스트
통합테스트는 실제 환경에서 실행한다.
통합테스트는 보통 개발이나 스테이징 환경에서 실행한다. 

#### 부하테스트
부하테스트의 목적은 트래픽이 증가된 상황에서 서비스의 병목 현상을 파악하고 조기 최적화(premature optimization)가 아닌 앞으로의 계획을 세우는 데 있다.
부하테스트를 만들면 다음질문에 대한 답을 얻을 수 있다.

* 특정사양을 갖춘 머신에서 하나의 인스턴스는 얼마나 많은 사용자를 받아들 일 수 있는가?
* 10/100/1000개의 동시요청에 대한 평균 응답시간은 얼마인가?  더 많은 동시성을 처리할 수 있는가?
* 서비스에 부하가 걸린 상황일 때 RAM과 CPU 중 어느 것을 더 소비하는가?
* 해당 서비스의 인스턴스를 더 추가해서 수평으로 확장할 수 있는가?
* 다른 서비스를 호출할 때 커넥션 풀을 사용할 수 있는가?
* 서비스를 한번 실행하면 성능저하없이 며칠동안 실행될 수 있는가?
* 사용량이 최고점에 한 번 도달한 뒤에도 서비스가 올바르게 동작하는가?

RPS : request per second



#### 이번 절에서 배운 내용을 정리해보면 다음과 같다.

* 기능 테스트는 가장 중요한 테스트다. 플라스크에서는 테스트에 app의 인스턴스를 만들어 연동하는 방식으로 쉽게 만들 수 있다.
* 단위 테스트는 훌륭한 수단이지만 모방을 남용하지 않게 주의해야한다.
* 통합 테스트는 기능 테스트와 비슷하지만 , 실제 환경에서 돌려야한다.
* 부하 테스트는 마이크로서비스의 병목점을 파악해 다음 단계의 계획을 세우는 데 유용하다.
* 엔드 투 엔드 테스트는 클라이언트가 실제로 사용하는 UI와 동일한 것을 사용해야 한다. 


