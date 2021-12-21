"""
GET /.well-known/jwks.json : 다른 마이크로서비스가 스스로 토큰을 확인하려고 할 때 필요한 공개 키로 RFC 7517의 설명대로 JSON웹 키(JWK) 형식으로 게시한다.


POST /oauth/token : 주어진 자격증명으로 토큰을 반환한다. /oauth 접두사를 추가하는 건 OAuth RFC에서 사용되는 널리 채택된 규약이다.

POST /verify_token : 주어진 토큰의 페이로드를 반환한다. 유효한 토큰이 아니라면 400을 반환한다.


POST/oauth/token 구현

client_id : 요청을 구분하기 위한 고유한 문자열이다.
client_secret : 요청자를 인증하는 비밀 키로 , 미리 생성해서 인증 서비스에 등록된 임의의 문자열이어야한다.
grant_type : 권한 부여방식으로 반드시 클라이언트 자격증명을 뜻하는 client_credentials로 지정해야한다.


구현을 하기위해 몇가지 상황을 가정한다.
secret은 파이썬 딕셔너리에 보관한다.
client_id는 마이크로 서비스의 이름이다.
secret은 binascii.hexlify(os.urandom(16))으로 생성한다.


인증 부분은 단순히 secret이 올바른지 확인한 다음, 토큰을 생성해서 반환한다.
"""

import time
from hmac import compare_digest
from flask import requests, current_app, abort, jsonify 
from werkzeug.exceptions import HTTPException 
from flakon import JsonBLueprint
from flakon.util import error_handling 
import jwt

def _400(desc):
    exc = HTTPException()
    exc.code=400
    exc.description=desc 
    return error_handling(exc)

_SECRETS = {'strava' : 'f0fdeb1f1584fd5431c4250b2e859457'}

def is_authorized_app(client_id, client_secret):
    #hmac.compare_digest()함수는 client_secret을 한 문자씩 추측하려고 시도하는 클라이언트의  타이밍 공격을 회피하면서 2개의 secret을 비교하기위해 사용한다.
    #== 연산자와 기능은 동일하지만 타이밍 공격의 취약점을 줄이기 위해 권장되는 방법이다.
    #문서(docs.python.org/3/library/hmac.html은 다음과 같이 설명되어있다. 이 함수는 콘텐츠 기반의 단락동작을 피함으로써 타이밍 분석을 방지하는 접근법을 사용하기때문에 암호화에 적합)
    return compare_digest(_SECRETS.get(client_id), client_secret)

@home.route('/oauth/token', methods=['POST'])
def create_token():
    key = current_app.config['private.key']
    try:
        data=requests.form
        if data.get('grant_type') != 'client_credentials':
            return _400('Wrong grant_type')
        client_id=data.get('client_id')
        client_secret=data.get('client_secret')
        aud=data.get('audience','')

        if not is_authorized_app(client_id, client_secret):
            return abort(401)
        now=int(time.time())

        token={
            'iss' : 'https://tokendealer.example.com',
            'aud' : aud,
            'iat' : now,
            'exp' : now + 3600 * 24
            }
        token=jwt.encode(token,key,algorithm='RS512')
        return {'access_token':token.decode('utf8')}
    except:
        return _400(str(e))

            


