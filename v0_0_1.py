# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v0_0_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import requests
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QObject, Qt

from paho.mqtt import client as mqtt_client

client_id = '2943f6c1736d450190e9abf84be97b76'
username = ''
password = ''
broker = '192.168.43.97'
port = '1883'
topic = 'Gateway_HQYJ/Issue'


class Ui_Form(object):

    def __init__(self, str_ip_camera_server, port_camera_server) -> None:
        self.str_ip_camera_server = str_ip_camera_server
        self.port_camera_server = port_camera_server

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 543)
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setGeometry(QtCore.QRect(350, 310, 181, 71))
        self.btn1.setObjectName("btn1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 260, 151, 131))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "btn_1_最小"))
        self.label.setText(_translate("Form", "不知道放啥"))

    def show_pic(self):
        while True:
            response = requests.get("http://" + self.str_ip_camera_server + ":" + str(self.port_camera_server) + "/video_feed_api")
            image_array = np.frombuffer(response.content, dtype=np.uint8)
            np_image = cv2.imdecode(image_array, 1)

            np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
            
            q_img = QtGui.QImage(np_image, np_image.shape[1], 
                                np_image.shape[0], 
                                np_image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap(q_img).scaled(self.label.width(), 
                                            self.label.height())
            self.label.setPixmap(pix)
    
    def muti_thread_show_pic(self):
        t = Thread(target=self.show_pic)
        t.start()
        
           

