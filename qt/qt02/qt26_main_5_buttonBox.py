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
        self.buttonBox.clicked.connect(self.buttonBox_clicked)



    def pushButton_clicked(self):
        print('---')

    def buttonBox_clicked(self):
        print('=====')
        # print(dir(self.sender()))
        print(self.sender().Yes)
        print(self.sender().Ok)
        print(self.sender().No)




app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())