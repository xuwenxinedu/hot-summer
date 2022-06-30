from sre_parse import State
import paho.mqtt.client as mqtt
import json
from algorithm import identify as it

class MQTT:
    def __init__(self):
        super().__init__()
        with open('./config/config.json') as f:
            setting = json.load(f)
            self.broker = setting['broker']
            self.port = setting['port']
            self.username = setting['client']
            self.password = setting['pwd']
            self.topic = setting['topic']

        # MQTT设置
        client_id = '655cc02f46d44dc5b1a048e89a790ffe'
        self.client = mqtt.Client(client_id)
        self.connect_mqtt()



    # 连接服务器函数
    def connect_mqtt(self):
        self.client.username_pw_set('', '')
        try:
            self.client.connect(self.broker)
            print('连接成功了')
        except Exception:
            print("连接出错，原因:{}".format(str(Exception)))
            return
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
        self.client.publish(self.topic, payload)
        
    
    def publish(self, payload):
        self.client.publish(self.topic, payload)

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
        

