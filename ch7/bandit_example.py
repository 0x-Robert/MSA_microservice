"""

OpenStack 커뮤니티는 안전하지 않은 코드를 찾아주는 Bandit이라는 멋진 보안 린터를 만들었다.

이 도구는 ast모듈을 사용해서 Flake8이나 다른 정적 도구처럼 코드를 분석하며, 보안 문제가 발생할 수 있는 코드를 검색한다.
pip install bandit 으로 설치하고  bandit 명령으로 파이썬 모듈을 검사할 수 있다.

여기에는 64개의 보안 검사가 포함돼있으며, 자신만의 코드 검사 루틴을 만들어 확장하는 것도 가능하다.

"""



import subprocess 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml 

def read_file(filename):
    with open(filename) as f:
        data=yaml.load(f.read())

def run_command(cmd):
    return subprocess.check_call(cmd, shell=True)

db=create_engine('sqlite:///somedatabase')
Session=sessionmaker(bind=db)

def get_user(uid):
    session=Session()
    query = "select * from user where id='%s'" %uid
    return session.execute(query)