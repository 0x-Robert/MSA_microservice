import json 
from molotov import scenario

@scenario(5)
async def scenario_one(session):
    res = await session.get('http://localhost:5000/api').json()
    assert res['Hello'] == 'World'

@scenario(30)
async def scenario_two(session):
    somedata = json.dumps({'OK':1})
    res = await session.post('http://localhost:5000/api', data=somedata)
    assert res.status_code == 200

"""
boom과 molotov는 지표를 몇 개보여주는데 실행환경의 네트워크나 CPU등에 따라 결과는 다르게 나타난다. 
부하테스트를 돌릴 때는 서버측에서 지표를 측정하는 것이 더 좋다. 플라스크에는 flask-profiler도구가 있다. 각 요청을 처리하는 데 걸린 시간을 수집해서 
대시보드로 보여준다.

엔드투 엔드 테스트 작성은 셀레니움 웹드라이버 테스트 자동화 책을 참고하면 된다.
"""