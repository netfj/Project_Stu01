#coding:utf-8
# @Info: 
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

    def pushButton_clicked(self):
        print('=====\nself.cb3.setTristate(False):')
        self.cb3.setTristate(False)
        self.cb3.setChecked(True)
        self.cb3.setCheckState(1)
        self.cb4.setCheckState(Qt.PartiallyChecked)

        print(Qt.Unchecked)
        print(Qt.PartiallyChecked)
        print(Qt.Checked)

        print('self.cb4.setTristate(True):')
        self.cb4.setTristate(True)


        # self.cb4.checkStateSet(1)

    def cb1_change(self,n_int):

        print('====>')
        print(self.cb2.isTristate())
        print(self.cb3.isTristate())
        print(self.cb4.isTristate())

        print(n_int,'--->')
        print('self.cb2.isChecked()',self.cb2.isChecked())

        print('=====\n'
              'self.cb3.setTristate(False):')
        print('self.cb3.isChecked()', self.cb3.isChecked())
        print('self.cb3.checkState()', self.cb3.checkState())

        print('\n'
              'self.cb4.setTristate(True):')
        print('self.cb4.isChecked()', self.cb4.isChecked())
        print('self.cb4.checkState()', self.cb4.checkState())

        # print(dir(QCheckBox))



app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())