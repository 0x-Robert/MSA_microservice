import unittest
from unittest import mock
import requests
from requests.exceptions import ConnectionError

import requests_mock
from test_request_01 import MyBugzilla
"""

test_network_error()함수는 파이썬의 mock.patch 데코레이터를 사용해 네트워크 흉내 내는 두번째 테스트다. 이 테스트는 네트워크가 
좋지 않을 때도 클래스가 예상대로 동작하는지 검사한다.

단위테스트를 활용하면 클래스와 함수 대부분의 동작을 검사할 수 있다. 프로젝트가 성장하고 코드가 늘어나면서 이전에 없던 새로운 상황이 
발생하므로 가능한 많은 테스트를 만드는 것이 좋다.

마이크로서비스에서는 단위테스트는 우선순위가 높지 않고 기능테스트에 좀 더 집중하는 것이 좋다. 


"""

class TestBugzilla(unittest.TestCase):
    def test_bug_id(self):
        zilla = MyBugzilla('tarek@mozilla.com',server='http://yeah')
        link=zilla.bug_link(23)
        self.assertEqual(link,'http://yeah/show_bug.cgi?id=23')

    @requests_mock.mock()
    def test_get_new_bugs(self,mocker):
        #요청을 모방해서 2개의 버그 목록을 반환한다.
        bugs = [{'id':1184528} , {'id':1184524}]
        mocker.get(requests_mock.ANY,json={'bugs':bugs})

        zilla = MyBugzilla('tarek@mozilla.com',server='http://yeah')
        bugs=list(zilla.get_new_bugs())

        self.assertEqual(bugs[0]['link'], 'http://yeah/show_bug.cgi?id=1184528')


        @mock.patch.object(requests,'get',side_effect=ConnectionError('Nonetwork'))
        def test_network_error(self,mocked):
            #서버 다운 등의 네트워크 에러 테스트
            zilla = MyBugzilla('tarek@mozilla.com',server='http://yeah')
            bugs=list(zilla.get_new_bugs())
            self.assertEqual(len(bugs),0)
        

if __name__ == "__main__":
    unittest.main()

