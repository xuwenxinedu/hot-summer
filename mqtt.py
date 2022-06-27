import paho.mqtt.client as mqtt
import json

# one line explanation

class MQTT:
    def __init__(self):
        super().__init__()
        with open('config.json') as f:
            setting = json.load(f)
            self.broker = setting['broker']
            self.port = setting['port']
            self.username = setting['client']
            self.password = setting['pwd']
            self.topic = setting['topic']
 
        #MQTT设置
        # client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        client_id = 'c3410e79476e4e6e8733b7c0489d0c82'
        self.client = mqtt.Client(client_id)
        # self.client.on_message = self.on_message
        # self.client.on_subscribe = self.on_subscribe
        # self.client.on_unsubscribe = self.on_unsubscribe

        self.connect_mqtt()
 
       

    #连接服务器函数
    def connect_mqtt(self):
        self.client.username_pw_set('', '')
        try:
            self.client.connect(self.broker)
            print('连接成功了')
        except Exception:
            print("连接出错，原因:{}".format(str(Exception)))
            return
        self.client.loop_start()
        
 
    #断开服务器函数
    def disconnect_mqtt(self):
        self.client.loop_stop()
        self.client.disconnect()

    #发布主题
    def pub(self):
        
        # payload = json.dumps(self.ui.textEdit_2.toPlainText())
        payload = json.dumps(
            
            {
                "To_XArm":{
                    "Control_XArm_Action":"Nod"
                }
            }
            
        )
        self.client.publish(self.topic, payload)
 
    # #消息回调函数
    # def on_message(self, client, userdata, msg):
    #     topic = msg.topic
    #     payload = str(json.loads(msg.payload))
    #     self.ui.textEdit.append("主题："+topic+"\n"+"消息："+payload)
 
    # #订阅成功回
    # def on_subscribe(self,client, userdata, mid, granted_qos):
    #     self.ui.textEdit.append("订阅成功: " + str(mid) )
 
    # #取消订阅成功回调函数
    # def on_unsubscribe(self,client, userdata, mid):
    #     self.ui.textEdit.append("取消订阅成功：" + str(mid))
 
    # #各个发布主题按钮设置
    # #控制设备
    # def dev1(self):
    #     data = str({"data1":"hello1","data2":"hello2"})
    #     self.ui.lineEdit_3.setText("/V1/ID/device/response")
    #     self.ui.textEdit_2.setPlainText(data)
 
    # #数据上报
    # def dev2(self):
    #     data = str({"data1":"P","data2":"Y","data3":"T","data4":"H"})
    #     self.ui.lineEdit_3.setText("/V1/ID/device/data")
    #     self.ui.textEdit_2.setPlainText(data)
 
if __name__ == "__main__":
    t = MQTT()
    t.pub()