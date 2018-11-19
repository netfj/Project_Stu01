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
        self.rb1.toggled.connect(self.rb_toggled)

    def pushButton_clicked(self):
        print('---')
        print(self.rb1.isChecked())
        print(self.rb2.isChecked())
        print(self.rb3.isChecked())
        print(self.rb_hc1.isChecked())
        print(self.rb_hc2.isChecked())
        print(self.rb_hc3.isChecked())

    def rb_toggled(self):
        print('===============')





app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())