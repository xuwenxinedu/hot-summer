import paho.mqtt.client as mqtt
import json

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
        self.connect_mqtt()
        self.client.publish(self.topic, payload)
        self.disconnect_mqtt()
