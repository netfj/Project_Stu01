#coding:utf-8
# @Info: radioButton
# @Author:Netfj@sina.com @File:qt26_main.py @Time:2018/11/17 16:12

import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt26_buttons import Ui_Form

class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myForm,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.commandLinkButton.clicked.connect(self.cc)

    def pushButton_clicked(self):
        print('---')
        self.pushButton.setText('新文字')
        self.pushButton.setIcon(QIcon('warning.ico'))


    def cc(self,c=0):
        print('===',self.sender().text())
        print('===',self.sender().description())
        QDesktopServices.openUrl(QUrl(self.sender().description()))


app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())