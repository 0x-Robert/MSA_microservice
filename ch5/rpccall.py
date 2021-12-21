import pika

from pika import BlockingConnection, BasicProperties

def on_message(channel, method_frame,header_frame, body):
    race_id = method_frame.rougin_key.split('.')[-1]
    print('---새 메시지---')
    print('race id:',race_id)
    print('body: ',body.decode('utf-8'))

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    #on_change 함수에서 rabbitmq에 ack를 보내 메시지를 받았다는 걸 알린다.
    #rabbitmq가 이 ack를 수신하면 큐에서 메시지를 안전하게 제거한다.
    

print("race 메시지 수신 대기 중...\n")

connection = pika.BlockingConnection()
channel= connection.channel()
channel.basic_consume(on_message,queue='race')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
