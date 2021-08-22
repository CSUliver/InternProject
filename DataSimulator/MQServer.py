import time
import stomp
import json
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)


class MyListener(stomp.ConnectionListener):

    def on_message(self, message):
        # header 消息头信息，可以通过header 判断那个topic的数据
        # {'message-id': 'ID:jtcsOTMS-db-47634-1552380859117-1:1:1:1:7249045', 'destination': '/queue/test_topic', 'timestamp': '15529}
        print('actvemq-data:', message)  # 获取到的队列信息


class MyActiveMq():
    def __init__(self, queue_host, queue_port, queue_username, queue_password) -> None:
        self.queue_host = queue_host
        self.queue_port = queue_port
        self.queue_username = queue_username
        self.queue_password = queue_password

    def mq_conn(self):  # 连接mq
        self.conn = stomp.Connection10([(self.queue_host, self.queue_port)])
        self.conn.connect(username=self.queue_username, passcode=self.queue_password)

    def send_data(self, queue_name, data):
        '''
        queue_name:消息队列名称
        data:发送的数据
        '''
        self.conn.send("/topic/"+queue_name, json.dumps(data, cls=DateEncoder))  # 数据存入 Topic 话题
        # self.conn.send(queue_name, f"message:{json.dumps(data)}")  # 数据存入消息队列

    def read_data(self, queue_name):
        '''
        queue_name:消息队列名称
        '''
        self.conn.set_listener('data_sim', MyListener())
        self.conn.subscribe(destination=queue_name, ack='auto')



if __name__ == '__main__':
    mq_host = "47.98.214.197"
    mq_port = 8161
    mq_username = "admin"
    mq_passwd = "admin"
    ms = MyActiveMq(mq_host, mq_port, mq_username, mq_passwd)
    ms.mq_conn()
    ms.read_data("Temper")
    ms.send_data("Temper", "36")
    ms.send_data("Temper", "37")
    ms.send_data("Temper", "38")

    while True:
        pass