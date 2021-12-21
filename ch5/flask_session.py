"""
플라스크 app에서 세션 사용
플라스크 앱 객체의 extensions에는 애플리케이션의 특정 상태 등을 저장 할 수 있다. 
여기서는 Session 객체를 저장하는 용도로 사용한다.

"""


from requests import Session

def setup_connector(app,name='default',**options):
    if not hasattr(app, 'extensions'):
        app.extensions={}
    if 'connectors' not in app.extensions:
        app.extensions['connectors']={}
    session=Session()

    if 'auth' in options:
        session.auth = options['auth']
    headers=options.get('headers',{})

    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    session.headers.update(headers)

    app.extensions['connectors'][name] = session 
    return session 

def get_connector(app,name='default'):
    return app.extensions['connectors'][name]

"""
setup_connector()함수는 Session 객체를 생성해 앱의 extensions에 저장한다. 
생성된 Session의 Content-Type 헤더값은 application/json이 기본으로 지정되므로 JSON기반의 마이크로 서비스에 데이터를 보내는 데 쓸 수 있다.
세션이 앱에 저장되면 뷰에서는 get_connector 함수로 저장된 세션을 가져올 수 있다.

"""