# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v0_0_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import cv2
import numpy as np
import requests

class Ui_Form(object):

    def __init__(self, str_ip_camera_server, port_camera_server) -> None:
        self.str_ip_camera_server = str_ip_camera_server
        self.port_camera_server = port_camera_server

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 550)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 230, 251, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 1, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 40, 391, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.btn5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn5.setObjectName("btn5")
        self.verticalLayout.addWidget(self.btn5)
        self.btn6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn6.setObjectName("btn6")
        self.verticalLayout.addWidget(self.btn6)
        self.btn7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn7.setObjectName("btn7")
        self.verticalLayout.addWidget(self.btn7)
        self.btn8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn8.setObjectName("btn8")
        self.verticalLayout.addWidget(self.btn8)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 320, 251, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl6.setObjectName("lbl6")
        self.gridLayout_2.addWidget(self.lbl6, 0, 2, 1, 1)
        self.lbl7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl7.setObjectName("lbl7")
        self.gridLayout_2.addWidget(self.lbl7, 1, 0, 1, 1)
        self.lbl8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl8.setObjectName("lbl8")
        self.gridLayout_2.addWidget(self.lbl8, 1, 2, 1, 1)
        self.lbl5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl5.setObjectName("lbl5")
        self.gridLayout_2.addWidget(self.lbl5, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(70, 40, 251, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbl2.setObjectName("lbl2")
        self.gridLayout_3.addWidget(self.lbl2, 0, 1, 1, 1)
        self.lbl1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbl1.setObjectName("lbl1")
        self.gridLayout_3.addWidget(self.lbl1, 0, 0, 1, 1)
        self.lbl3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbl3.setObjectName("lbl3")
        self.gridLayout_3.addWidget(self.lbl3, 1, 0, 1, 1)
        self.lbl4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbl4.setObjectName("lbl4")
        self.gridLayout_3.addWidget(self.lbl4, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "复位"))
        self.btn3.setText(_translate("Form", "抓取最小值"))
        self.btn2.setText(_translate("Form", "抓取最大值"))
        self.btn4.setText(_translate("Form", "排序"))
        self.lbl.setText(_translate("Form", "video"))
        self.btn5.setText(_translate("Form", "显示彩色图"))
        self.btn6.setText(_translate("Form", "显示灰度图"))
        self.btn7.setText(_translate("Form", "显示二值图"))
        self.btn8.setText(_translate("Form", "停止显示图像"))
        self.lbl6.setText(_translate("Form", "2"))
        self.lbl7.setText(_translate("Form", "3"))
        self.lbl8.setText(_translate("Form", "4"))
        self.lbl5.setText(_translate("Form", "1"))
        self.lbl2.setText(_translate("Form", "2"))
        self.lbl1.setText(_translate("Form", "1"))
        self.lbl3.setText(_translate("Form", "3"))
        self.lbl4.setText(_translate("Form", "4"))



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