#coding:utf-8

import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt25_button import Ui_Form

class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myForm,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(myForm.pushButton_clieked)
        self.pushButton.clicked.connect(myForm.pushButton_clieked)

    def pushButton_clieked(self):
        print('---')

    def cb1_change(self,n_int):
        print(n_int)


app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())


