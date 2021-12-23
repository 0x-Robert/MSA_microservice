"""
스트라바 토큰 얻기
스트라바는 전형적인 3자 인증 OAuth2 방식을 구현하며, Stravalib을 사용해서 처리할 수 있다.
OAuth2를 구현하려면 사용자를 리다이렉션한 후 사용자가 스트라바 접근을 승인했을 때 다시 리다이렉트할 엔드포인트를 노출하면 된다.

스트라바 계정에서 얻어야 할 것은 사용자 정보와 엑세스 토큰이다. 이 정보를 플라스크 세션에 저장해서 로그인 처리에 사용할 수 있다.
그리고 이메일과 토큰 값을 데이터 서비스에 전달해서 Celery 스트라바 워커가 토큰을 사용할 수 있게 한다.

"""

from stravalib.client import Client
def get_strava_url():
    client=Client()
    cid=app.config['STRAVA_CLIENT_ID']
    redirect=app.config['STRAVA_REDIRECT']
    url=client.authorization_url(client_id=cid, redirect_uri=redirect)
    return url
    
