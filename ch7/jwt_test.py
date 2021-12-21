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

이와 같은 클레임은 토큰을 일정 시간만큼만 유효한 상태로 유지할 수 있도록 하는 유연성을 제공한다.

마이크로 서비스의 성격에 따라 토큰의 TTL(Time To Live)를 매우짧게, 또는 무한하게 할 수 있다.
예를 들면 마이크로 서비스가 시스템 내의 다른 서비스와 연동된다면 매번 토큰을 생성할 필요 없이
일정 시간 동안 유지되도록 토큰을 만드는 것이 좋다.

반면에 토큰이 시스템 바깥의 여러 곳에 분산된다면 가능한 한 짧은 시간 동안만 유효하게 만드는 것이 좋다.

JWT 토큰의 마지막 부분은 서명이다. 서명은 헤더와 페이로드의 서명된 해시를 포함한다.
서명과 해시에는 여러 개의 알고리즘이 사용된다. 일부는 비밀 키를 기반으로 하며 일부는 공개 키와 비밀 키 쌍을  기반으로 한다.


"""



