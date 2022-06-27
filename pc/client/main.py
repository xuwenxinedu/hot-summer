import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.v0_0_1 import *



  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form('192.168.43.97', '8087')
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.btn1.clicked.connect(ui.muti_thread_show_pic)
    sys.exit(app.exec_())