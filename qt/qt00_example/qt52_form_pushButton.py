#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt52_form_pushButton.py @time:2018/11/19.0:04
"""


import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
a= QWidget()
a.resize(400,300)
pushButton = QPushButton('Start',a)
a.show()
sys.exit(app.exec_())
