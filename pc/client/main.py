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
    ui.btn1.clicked.connect(ui.nod)
    sys.exit(app.exec_())