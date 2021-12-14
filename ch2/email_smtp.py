"""
이메일 템플릿을 사용해서  RFC 822표준에 맞는 메시지를 생성하고 SMTP를 통해 보내는 파이썬 스크립트다.
"""

from datetime import datetime 
from jinja2 import Template
from email.utils import format_datetime 

def render_email(**data):
    with open('email_template.eml') as f:
        template = Template(f.read())
    return template.render(**data)

data={'date':format_datetime(datetime.now()),
      'to': 'bob@example.com',
      'from':'tarek@ziade.org',
      'subject':"Your Tarek's Burger order",
      'name':'Bob',
      'items' : [
          {'name':'Cheeseburger', 'price':4.5},
          {'name':'Fries','price':2.},
          {'name':'Root beer','price':3}]}

print(render_email(**data))


