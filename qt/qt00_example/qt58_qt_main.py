# coding:utf-8
'''
这里模拟Qt设计好的文件，转换成py文件后，模拟引入的示例。
类Ui_Form，相当于是Qt设置的原始模板；被myForm继承后，以写入自己的业务逻辑。
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle('Qt Designer!')
        #还有很多…(略)

#from Qt_Designer.py import Ui_Form
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
