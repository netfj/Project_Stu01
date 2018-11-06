#coding:utf-8
"""
@info: 代码放入同文件,窗体展示测试
@author:NetFj @software:PyCharm @file:qt07_main.py @time:2018/11/5.14:12
"""

from PyQt5 import QtWidgets,QtCore
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 141, 71))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form窗口标题"))
        self.pushButton.setText(_translate("Form", "测试"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = QtWidgets.QWidget()
    ui = MyWindow()
    ui.setupUi(myshow)
    myshow.show()
    sys.exit(app.exec())
