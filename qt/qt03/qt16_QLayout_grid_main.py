# coding:utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from qt16_QLayout_grid import Ui_Form
class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print('这是我的业务内容.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = myForm()
    mainwindow.show()
    sys.exit(app.exec_())