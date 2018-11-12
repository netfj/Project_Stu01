#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt21_main.py @time:2018/11/12.22:29
"""


import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt21_list import Ui_Form
class myWin(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)

    def start(self):
        self.listWidget.addItem('test1')
        self.listWidget.addItem('test2')
        self.listWidget.setCurrentRow(1)

        pass

    def test(self):
        pass

    def text_changed(self,aaa):
        print(aaa)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWin()
    myshow.show()
    sys.exit(app.exec())