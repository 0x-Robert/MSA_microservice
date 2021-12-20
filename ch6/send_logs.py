# -*- coding: utf-8 -*- 
import logging 
import graypy 
import json
from flask import Flask , jsonify, abort ,session
from werkzeug.exceptions import HTTPException, _aborter 

app=Flask(__name__)


def error_handling(error):
  if isinstance(error, HTTPException):
      result = {'code': error.code, 'description': error.description}
  else:
      description = _aborter.mapping[500].description
      result={'code':500, 'description':description}

  app.logger.exceptions('예외발생! ' +str(error), extra=result)
  result['message']=str(error)
  resp=jsonify(result)
  resp.status_code=result['code']
  return resp

for code in _aborter.mapping:
    app.register_error_handler(code,error_handling)

@app.route('/api',methods=['GET','POST'])
def my_microservice():
    app.logger.info("Graylog에 info 로그 기록")
    resp = jsonify({'result':'OK', 'Hello':'World!'})

    #고의로 예외를 발생시켜서 Graylog에 exception 로그 기록
    raise Exception('BAHM')
    return resp


class InfoFillter(logging.Filter):
  def filter(self,record):
    record.username=session.get('username','Anoymous')
    return True 


if __name__ == '__main__':
    handler = graypy.GELFTCPHandler('localhost',12201)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    #app.logger.addFilter(InfoFilter())
    app.run()