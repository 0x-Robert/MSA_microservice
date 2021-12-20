import base64

def decode(data):
    
    pad = len(data) % 4
    if pad > 0:
        data += '=' * ( 4 - pad)
    return  base64.urlsafe_b64decode(data)

print(decode('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'))  #헤더
print(decode('eyJ1c2VyIjoidGFyZWsifQ')) #페이로드
print(decode('OeMWz6ahNsf-TKg8LQNdNMnFHNtReb0x3NMs0eY64WA'))  #서명

"""
서명을 제외하면 JWT 토큰의 각 부분은 JSON 맵으로 이뤄졌다. 헤더는 보통 typ와 alg 키를 포함하는데, typ 키의 값으로 
JWT 토큰이란 걸 알 수 있으며, alg 키는 사용된 해시 알고리즘을 나타낸다.

페이로드는 필요한 어떤 내용도 포함할 수 있다. RFC7519에서는 정보의 각 필드를 JWT 클레임(Claim)이라고 부른다.

RFC는 등록된 클레임 이름(Registered Claim Name)이라고 부르는 , 토큰이 포함될 수 있는 클레임 항목을 미리 정의하고 있다.이들 중 일부를 정리하면 다음과 같다.

* iss: 토큰을 생성한 엔티티(entity)의 이름, 즉 토큰(발급자, issue)를 나타낸다. 보통 호스트 이름이기 때문에 클라이언트는 /.well-known/jwks.json을 요청해서 공개 키를 알아낼 수 있다.
* exp: 토큰 만료 시간(Expiration Time)을 의미한다.
* nbt: 토큰이 유효해지는 시간(Not Before Time)을 나타낸다.
* aud: 토큰이 누구에게 발급됐는지, 수신자(Audience)를 나타낸다. 
* iat: 토큰이 언제 발급 됐는지(Issued At)를 나타낸다.

다음의 예제 페이로드에는 몇 개의 타임스탬프와 함께 사용자 정의 클레임인 user_id가 들어있다.
이 토큰은 2018년 2월 6일 화요일 오후 6:20:15부터 24시간 동안 사용가능하다.

{

    "iss" : "https://tokendealer.example.com",
    "aud" : "runnerly.io",
    "iat" : 1517822415, // 2018년 2월 5일 월요일 오후 6:20:15
    "nbt" : 1517908815, // 2018년 2월 6일 화요일 오후 6:20:15
    "exp" : 1517995215, // 2018년 2월 7일 수요일 오후 6:20:15
    "user_id" : 1234


}

"""



