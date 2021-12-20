import functools
import logging 
import graypy
import json
import time
import random

from collections import defaultdict, deque
from flask import Flask, jsonify,g

app=Flask(__name__)

"""
성능측정 코드는 운영환경에서 서비스에 영향을 줄 수있기 때문에
추가하는것에 신중을 기해야한다.

다음 코드에서 @timeit 데코레이터는 fast_stuff()와 some_slow_stuff()함수의
실행 시간을 수집하고, 요청이 끝나면 각 호출에 걸린 시간을 Graylog로 전송한다.

# @functools.wraps() 데코레이터 함수는 signature 를 잘 보존하고
      # docstring 을 보존해 다른 개발자와의 협업에 유리한 면이 있기 때문에
      # decorator 함수를 만들때는 항상 사용해야 할 것 같습니다
"""
class Encoder(json.JSONEncoder):
    def default(self,obj):
      base = super(Encoder, self).default
      #시간 측정을 위한 인코더
      if isinstance(obj, deque):
        calls = list(obj)
        return {'num_calls': len(calls),'min':min(calls), 'max':max(calls), 'values':calls}
        return base(obj)
      
def timeit(func):
  @functools.wraps(func)
  def _timeit(*args,**kw):
    start = time.time()
    try:
      return func(*args, **kw)
    finally:
      if 'timers' not in g:
        g.timers = defaultdict(functools.partial(deque, maxlen=5))
      g.timers[func.__name__].append(time.time() - start)
  return _timeit 

@timeit 
def fast_stuff():
  time.sleep(.001)

@timeit 
def some_slow_stuff():
  time.sleep(random.randint(1,100) / 100.)

def set_view_metrics(view_func):
  @functools.wraps(view_func)
  def _set_view_metrics(*args, **kw):
      try:
          return view_func(*args, **kw)
      finally:
          app.logger.info(json.dumps(dict(g.timers), cls=Encoder))
  return _set_view_metrics

def set_app_metrics(app):
    for endpoint, func in app.view_functions.items():
      app.view_functions[endpoint] = set_view_metrics(func)
  
@app.route('/api', methods=['GET','POST'])
def my_microservice():
  some_slow_stuff()
  for i in range(12):
    fast_stuff()
    resp = jsonify({'result' : 'OK', 'Hello':'World!'})
    fast_stuff()
  return resp
  

if __name__ == '__main__':
    handler = graypy.GELFTCPHandler('localhost',12201)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    set_app_metrics(app)
    app.run()
