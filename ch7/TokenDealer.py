import requests

"""
토큰  딜러 사용

인증은 다음과 같은 4단계이다.

1. TokenDealer는 스트라바 워커를 위해 client_id와 client_secret 짝을 보관하고 스트라바 워커 개발자와 공유한다.
2. 스트라바 워커는 client_id와 client_secret을 사용해서 TokenDealer에 토큰을 요청한다.
3. 스트라바 워커는 데이터 서비스에 보내는 모든 요청에 토큰을 추가한다. 
4. 데이터 서비스는 TokenDealer를 호출해 토큰을 검증하거나 로컬에서 직접 토큰을 검증한다.

call_data_service() 함수는 데이터 서비스를 호출했을 때 응답 코드가 401이면 새로운 토큰을 요청한다.

"""
server = 'http://localhost:5000'
secret = 'f0fdeb1f1584fd5431c4250b2e859457'


data=[

    ('client_id', 'strava'),
    ('client_secret', secret),
    ('audience', 'runnerly.io'),
    ('grant_type','client_credentials')

]

def get_token():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url=server + '/oauth/token'
    resp = requests.post(url, data=data , headers=headers)
    return resp.json()['access_token']

    #원래 표준구현은 /oauth/token이 JSON형식이 아닌 인코딩된 데이터를 받는다는 걸 알아두자
_TOKEN =None 

def get_auth_header(new=False):
    global _TOKEN 
    if _TOKEN is None or new:
        _TOKEN = get_token()
    return 'Bearer ' + _TOKEN

_dataservice = 'http://localhost:5001'


def _call_service(endpoint, token):
    #읽기를 단순히 하기 위해 세션 등은 사용하지 않는다. 
    return requests.get(_dataservice + '/' + endpoint, headers={'Authorization':token})

def call_data_service(endpoint):
    token=get_auth_header()
    resp=_call_service(endpoint,token)
    if resp.status_code==401:
        #토큰이 취소될 수 있으므로, 새로운 토큰으로 시도한다.
        token = get_auth_header(new=True)
        resp = _call_service(endpoint,token)
    return resp 

