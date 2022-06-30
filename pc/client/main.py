import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.v0_0_2 import *
from mqtt_client.mqtt import MQTT

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form('192.168.43.97', '8087', MQTT())
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.btn5.clicked.connect(ui.muti_thread_show_pic)
    ui.btn6.clicked.connect(ui.show_gray)
    ui.btn7.clicked.connect(ui.show_two_val)
    ui.btn8.clicked.connect(ui.stop_video)

    ui.btn1.clicked.connect(ui.reset)
    ui.btn2.clicked.connect(ui.muti_thread_get_max)
    ui.btn3.clicked.connect(ui.see)
    # ui.btn3.clicked.connect(ui.get_min)
    # ui.btn4.clicked.connect(ui.sort)

    

    sys.exit(app.exec_())
    ui.mqtt.disconnect_mqtt()