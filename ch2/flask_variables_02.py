#변수를 특정타입으로 변환해주는 컨버터가 있다. 예를 들어 정수타입의 변수를 사용한다면 <int:변수_이름>으로 표현한다. 앞의 예제코드와 비교하면
# /person/<int:person_id>로 표시할 수 있다.

#기본적으로 제공하는 컨버터로 string(유니코드가 기본), int,float,path,any,uuid가 있다.
# path 컨버터는 / 를 포함한다. 이는 [^/].*? 정규표현식과 비슷하다.
# any컨버터는 여러개의 값을 조합할 수 있게 하며, 드물게 사용된다. uuid 컨버터는 UUID 스트링을 매칭한다.

#사용자 정의 컨버터도 만들수 있다. 사용자 id와 이름을 매칭하고 싶다면 저장된 데이터에서 ID에 해당하는 이름을 찾아 변환해주는 컨버터를 만들면된다.
# BAsicConverter 클래스를 상속하는 클래스가 필요하고, 이 클래스는 두개의 함수를 구현하는데, to_python()은 URL 경로를 파이썬 객체로 변환해서 뷰에서 쓸 수 있게 하며
# to_url()은 주어진 인수에 해당하는 URL을 만들기 위해 url_for()에서 사용한다. 




from flask import Flask, jsonify, request 
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1':'Tarek', '2':'Freya'}
#items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
_IDS = {val:id for id, val in _USERS.items()}



class RegisteredUser(BaseConverter):
    def to_python(self,value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self,value):
        print("_IDS",_IDS)
        return _IDS[value]



app =Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello hey':name})
    return response 

if __name__ == '__main__':
    app.run()















