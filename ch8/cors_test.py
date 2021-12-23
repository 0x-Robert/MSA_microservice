"""
플라스크에서는 Flakon의 crossdomain()데코레이터를 써서 CORS 지원을 추가할 수 있다. 
"""

from flask import Flask, json, jsonify
from flakon import crossdomain

app=Flask(__name__)

@app.route('/api/runs.json')
@crossdomain()
def _runs():
    runs1={'title':'Endurance', 'type':'training'}
    runs2={'title':'10K de chalon', 'type':'race'}
    _data=[runs1,runs2]
    return jsonify(_data)

if __name__ == '__main__':
    app.run(port=5002)