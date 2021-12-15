import requests
import bugzilla


"""
단위테스트는 가장 단순한 테스트이다.
파이썬에서 개별 테스트를 만드는건 특정 인수를 갖고 클래스나 함수 호출에 대한 인스턴스를 만들어서 기대한 결과가 나오는지 검증하는 것이다.
  모방하기를 통해 격리된환경에서 해당호출을 흉내낼 수 있다. 실제로 어떤처리는 하지 않고 모의객체로 실제 동작을 흉내내는것을 말한다.

  모방하기는 다음과 같은 3가지경우에 사용하는것이 좋다.

   1. I/O연산 : 코드가 서드파티 서비스를 호출하거나, 소켓,파일 등의 리소스를 사용하고 있는데 테스트에서는 이 작업을 수행할 수 없을 때
   2. CPU 연산 : 테스트를 느리게 만드는 계산이 있을 때
   3. 특정상황 재연 : 네트워크 에러나 날짜/시간 변경처럼 특정 상황에서 코드를 시험하기 위한 테스트를 작성할 때 

   다음코드는 requests를 활용해서 버그질라 REST API를 호출해 버그 목록을 가져온다.


"""

class MyBugzilla:
    def __init__(self,account,server='https://bugzilla.mozilla.org'):
        self.account=account 
        self.server=server
        self.session=requests.Session()

    #격리된 환경에서 테스트를 처리하는 bug_link함수
    def bug_link(self,bug_id):
        return '%s/show_bug.cgi?id=%s' %(self.server,bug_id)

    # 실제 버그질라 서버로 요청을 보내는 get_new_bugs() 함수
    def get_new_bugs(self):
        call = self.server +'/rest/bug'
        params={'assigned_to':self.account , 'status':'NEW', 'limit':10}

        try:
            res=self.session.get(call,params=params).json()
        except requests.exceptions.ConnectionError:
            res={'bugs':[]}
        
        def _add_link(bug):
            bug['link'] = self.bug_link(bug['id'])
            return bug

        for bug in res['bugs']:
            yield _add_link(bug)

            