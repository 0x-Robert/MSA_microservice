"""
파이썬의 PyJWT 라이브러리는 JWT 토큰을 생성하고 읽을 수 있는 방법을 제공한다.
encode()함수로 토큰을 생성한다.
decode()함수로 토큰을 읽을 수 있다.

encode , 인코딩이란 정보를 부호화/암호화한다는 뜻
decode , 디코딩이란 그 부호화/암호화를 해제한다는 뜻


jwt.exceptions.DecodeError: It is required that you pass in a value for the "algorithms" argument when calling decode().  
위 에러발생시

pip install pyjwt=1.7.1 로 조치


아래 코드를 실행하면 압축된 형식의 토큰과 압축되지 않은 토큰이 함께 출력된다.

미리 정의된 등록 클레임 중 하나를 사용하면 PyJWT가 해당 클레임을 인식해서 제어한다.
예를들어 exp 클레임을 추가했고, 이 토큰이 만료됐다면 jwt.decode() 호출시에 라이브러리에서 자동으로 에러를 발생시킨다.

아래 코드같이 하나의 secret만 사용해서 전체시스템에 적용하면 보안에 문제가 생긴다.
그러므로 공개키와 개인 키로 구성된 비대칭 키를 사용하는 것이 좋다.
개인 키는 토큰 발급자가 토큰을 서명할 때 사용하며, 공개 키는 토큰을 검증할 필요가 있는 누구라도 사용할 수있다.

물론 공격자가 개인키에 접근할 수 있거나, 위조된 공개키로 클라이언트를 속일 수 있따면 여전히 문제의 소지가 있찌만, 공개 키/ 개인 키 쌍을 사용하면 인증 프로세스의 공격 가능 범위를 상당히 좁힐 수 있다.

"""


import jwt 


def create_token(alg='HS256', secret='secret', **data):
    print("data",data)
    return jwt.encode(data, secret, algorithm=alg)

def read_token(token, secret='secret'):
    print("token read",token)
    print("secret read",secret)
    return jwt.decode(token,secret)

token=create_token(some='data', inthe='token')
print("token", token)

read = read_token(token)
print("read",read)


