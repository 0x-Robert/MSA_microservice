import jwt

"""
인증서로서 Let's Encrypt를 사용하는것도 훌륭하다 이 프로젝트는 웹 보안을 목표로 하지만
도메인 이름을 소유하고 있다면 확장을 사용해 마이크로 서비스를 보호하는데 사용할 수도 있다.

커맨드
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 Generating a 4096 bit RSA private key

openssl x509 -pubkey -noout -in cert.pem > pubkey.pem

openssl rsa -in key.pem -out privkey.pem

rsa는 3명의 저자인 리베스트,샤미르,아들만의 앞글자에서 가져왔다. RSA 암호화 알고리즘은 최대 4096바이트의 암호화키를 생성하며 안전한 알고리즘으로 평가받고 있다.

cert.pem 파일은 인증서를 갖고 있다.
pubkey.pem 파일은 인증서에서 추출한 공개 키를 갖고 있다.
key.pem 파일은 암호화된 RSA 개인 키를 갖고 있다.
privkey.pem은 평문의 RSA 개인 키를 갖고있다.
"""

with open('public.key') as f:
    PUBKEY = f.read()

with open('private.key') as f:
    PRIVKEY = f.read()

def create_token(**data):
    return jwt.encode(data,PRIVKEY, algorithm='RS512')

def read_token(token):
    return jwt.decode(token,PUBKEY)

token=create_token(some='data',inthe='token')
print(token)

read=read_token(token)
print(read)


