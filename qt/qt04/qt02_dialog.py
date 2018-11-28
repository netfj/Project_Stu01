#coding:utf-8
"""
info:   对话框 全示例
author: NetFj@sina.com
file:   qt02_dialog.py 
time:   2018/11/27.19:49
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

class Form(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
myshow = Form()
myshow.show()
sys.exit(app.exec_())
