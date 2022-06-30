from time import sleep
import paho.mqtt.client as ph_mqtt_clt
from paho.mqtt.client import *
from queue import Queue
import os
import json
import algorithm.identify as it


class HQYJ_Mqtt_Client():

    def __init__(self, ip_broker = '192.168.43.97', port_broker = 1883,
                 topic_subscribe = 'Gateway_HQYJ/Upload', 
                 topic_publish = 'Gateway_HQYJ/Issue',
                 time_out_seconds = 50, max_size_rcv_msg = 30):
        self.hqyj_mqtt_clt = ph_mqtt_clt.Client()
        self.hqyj_mqtt_clt.on_message = self.on_message # 0.设置接收回调
        self.topic_subscribe = topic_subscribe
        self.topic_publish = topic_publish
        self.queue_rcv_msg = Queue(max_size_rcv_msg)
        try:
            self.hqyj_mqtt_clt.connect(ip_broker, port_broker, time_out_seconds)    # 1.连接Mqtt Broker
            self.hqyj_mqtt_clt.subscribe(self.topic_subscribe, qos=0)   # 2. 订阅相关的topic
            self.hqyj_mqtt_clt.loop_start() # 3.开启接收循环
        except Exception as e:
            print("HQYJ_Mqtt_Client init failed!error:", str(e))
            os._exit(0)

    def __del__(self):
        self.queue_rcv_msg.queue.clear()
        self.hqyj_mqtt_clt.loop_stop()
        self.hqyj_mqtt_clt.disconnect()

    def on_message(self, client, userdata, message):
        msg = json.loads(message.payload.decode())
        if not self.queue_rcv_msg.full():
            self.queue_rcv_msg.put(msg)
            print(msg)
        else:
            print("mqtt_hqyj:queue_rcv_msg full!")
            self.queue_rcv_msg.queue.clear()

    def send_json_data(self, msg: str) -> bool:
        msg_inf: MQTTMessageInfo = self.hqyj_mqtt_clt.publish(self.topic_publish, payload="{}".format(msg))
        return msg_inf.rc == MQTT_ERR_SUCCESS

    def upload_mcu_json_data(self, obj_upload) -> bool:
        return self.send_json_data(json.dumps(obj_upload))

    def publish(self, msg):
        self.send_json_data(msg)

    def reset(self):
        payload = json.dumps({
            "To_XArm":{
                "Control_XArm_Action":"Reset"
            }
        })
        self.publish(payload)
        print('mqtt reset')

    def only_see(self):
        print('thread only see')
        payload = json.dumps(
            {
                "To_XArm":"Control_XArm_Position"
            }
        )
        self.publish(payload)

    def see(self):
        self.only_see()
        print('mqtt see')        
        while True:
            # 这里拿到他的位置 到位之后在后面获取排序
            if not self.queue_rcv_msg.empty():
                msg = self.queue_rcv_msg.get()
                if msg.get('Protocol30'):
                    if 'In_Storage_No1' == msg.get('Protocol30').get('XArm_Position_Upload'):
                        break
        time.sleep(5)
        a = it.ans()
        print(a)
        return a
    
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
        print(f'mtqq {a} to {b}')

    def wait_finished(self):
        while True:
            if not self.queue_rcv_msg.empty():
                msg = self.queue_rcv_msg.get()
                if msg.get('Protocol30'):
                    if 'Finished' == msg.get('Protocol30').get('XArm_Grab_Finished_Upload'):
                        break

    def sort(self, infor):
        self.a2b(infor[0][0] + 1, 1)
        self.wait_finished()
        self.a2b(infor[1][0] + 1, 2)
        self.wait_finished()
        self.a2b(infor[2][0] + 1, 3)
        self.wait_finished()
        self.a2b(infor[3][0] + 1, 4)


    
