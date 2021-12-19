from celery.execute import send_task


'''
테스트에서  echo 태스크를 사용할 수 있으며 실제로 호출되는 워커를 만들 수 있다.
'''

class TestCelery(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def init_worker(self,celery_worker):
        self.worker=celery_worker

    def test_api(self):
        async_result=send_task('echo', ['yeah'], {})
        self.assertEqual(async_result.get(),'yeah')
        
    