#coding:utf-8
"""
@info:
@author:NetFj @software:PyCharm @file:qt05_lineEdit_regex.py @time:2018/11/19.22:24
"""

import sys
from PyQt5.QtWidgets import QWidget,QLineEdit,QLabel,QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class myForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

        t = '输入限制：\n' \
            '  1.长度不能超过15位；\n' \
            '  2.字母开头；\n' \
            '  3.后面跟着的字符只能是字母或者数字。'
        self.lable = QLabel(self)
        self.lable.setText(t)

        self.resize(500,300)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10,110)

        #正则表达式
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.lineEdit)
        self.lineEdit.setValidator(validator)

    def setupUi(self):
        self = QWidget()

app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())