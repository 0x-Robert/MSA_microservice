# Session 객체는 앱이 보내는 모든 요청에 공통적으로 설정해야하는 인증 정보와 기본 헤더 값을 갖고있다. 
# 예를 들어 다음 코드에서 Session 객체는 Content-Type 헤더와 인증 정보를 자동으로 생성한다.

from requests import Session 

s = Session()
s.headers['Content-Type'] = 'application/json'
s.auth = 'tarek','password'

#호출이 일어날 때 헤더와 인증 정보가 모두 설정된다.
s.get('http://localhost:5000/api').json()
s.get('http://localhost:5000/api2').json()

