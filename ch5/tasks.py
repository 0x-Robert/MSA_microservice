from celery import shared_task
import unittest


'''
Celery가 레디스를 사용하게 설정하고 테스트를 지정해서 테스트 픽스처를 만들 수 있다.
첫 번째 단계는 tests 디렉토리에 Celery 테스크를 포함하는 tasks.py를 만드는 것이다. 다음은 그런 파일의 예로 
Celery 인스턴스를 만드는 대신 @shared_task 데코레이터를 사용해서 함수를 Celery 태스크로 표시한다.

echo란 이름으로 celery 태스크를 구현한 이 모듈은 문자열을 그대로 돌려준다.
pytest가 사용할 수 있게 설정하려면  celery_config와 celery_includes 픽스처를 구현해야한다.

'''
@shared_task(bind=True, name='echo')
def echo(app,msg):
    return msg

import pytest

@pytest.fixture(scope='session')
def celery_config():
    return {
        'broken_url ': 'redis://localhost:6379',
        'result_backend' : 'redis://localhost:6379'

    }

@pytest.fixture(scope='session')
def celery_includes():
    return ['myproject.tasks.tasks']

