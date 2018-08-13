import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from chat_window import *


class mMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.label_background.hide()

        #self.thing.setText("查看明天上午的行程")
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    chat_win = mMainWindow()
    chat_win.setWindowFlags(Qt.FramelessWindowHint)
    chat_win.show()
    sys.exit(app.exec_())
    pass
