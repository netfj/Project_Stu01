#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt06_main.py @time:2018/11/19.23:33
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt06_plainTextEdit import Ui_Form

class myForm(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




app=QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())