
import paho.mqtt.client as mqtt
import json
from pc.client.algorithm import identify as it
from queue import Queue
class MQTT:
    def __init__(self):
        super().__init__()
        with open('./config/config.json') as f:
            setting = json.load(f)
            self.broker = setting['broker']
            self.port = setting['port']
            self.username = setting['client']
            self.password = setting['pwd']
            self.topic_publish = setting['topic_publish']
            self.topic_subscribe = setting['topic_subscribe']

        # MQTT设置
        client_id = '655cc02f46d44dc5b1a048e89a790ffe'
        self.client = mqtt.Client(client_id)
        self.connect_mqtt()
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.queue_rcv_msg = Queue(30)

    # 消息回调函数
    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = str(json.loads(msg.payload))
        print("主题：" + topic + "\n" + "消息：" + payload)
        if not self.queue_rcv_msg.full():
            self.queue_rcv_msg.put(payload)
            json_payload = json.loads(msg.payload)
            print(json_payload['Protocol30'])
        else:
            print("mqtt_client:queue_rcv_msg full!")
            self.queue_rcv_msg.queue.clear()

    # 订阅成功回
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("订阅成功: " + str(mid))


    # 取消订阅成功回调函数
    def on_unsubscribe(self, client, userdata, mid):
        print("取消订阅成功：" + str(mid))


    # 连接服务器函数
    def connect_mqtt(self):
        self.client.username_pw_set('', '')
        try:
            self.client.connect(self.broker)
            print('连接成功了')
        except Exception:
            print("连接出错，原因:{}".format(str(Exception)))
            return
        self.client.subscribe(self.topic_subscribe,qos=0)
        self.client.loop_start()

    # 断开服务器函数
    def disconnect_mqtt(self):
        self.client.loop_stop()
        self.client.disconnect()

    # 发布主题
    def pub(self):

        # payload = json.dumps(self.ui.textEdit_2.toPlainText())
        payload = json.dumps(

            {
                "To_XArm": {
                    "Control_XArm_Action": "Nod"
                }
            }

        )
        self.client.publish(self.topic_publish, payload)
        
    
    def publish(self, payload):
        self.client.publish(self.topic_publish, payload)

    def reset(self):
        payload = json.dumps({
            "To_XArm":{
                "Control_XArm_Action":"Reset"
            }
        })
        self.publish(payload)

    def only_see(self):
        payload = json.dumps(
            {
                "To_XArm":"Control_XArm_Position"
            }
        )
        self.publish(payload)

    def see(self):
        payload = json.dumps(
            {
                "To_XArm":"Control_XArm_Position"
            }
        )
        self.publish(payload)
        state = 0
        while True:
            if state == 1:
                break
            # 这里拿到他的位置 到位之后在后面获取排序
            state = 1
        return it.ans()
    
    def a2b(self, a, b):
        payload = json.dumps(
            {
                "To_XArm":{
                    "Control_XArm_Grab":{
                        "start": a,
                        "end":b
                    }
                }
            }
        )
        self.publish(payload)


        

