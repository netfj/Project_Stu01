#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt04_main.py @time:2018/11/19.19:10
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt04_lineEdit import Ui_Form

class myForm(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        action = QAction(self)
        action.setIcon(QIcon('Warning.ico'))
        action.triggered.connect(self.Check)
        self.lineEdit.addAction(action, QLineEdit.TrailingPosition)

        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.lineEdit_4)
        self.lineEdit_4.setValidator(validator)


    def Check(self):
        print('你输入了：',self.lineEdit.text())


app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())