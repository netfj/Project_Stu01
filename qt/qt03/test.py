#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test.py @time:2018/11/18.23:57
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
a= QWidget()
a.resize(400,300)
calendar = QCalendarWidget(a)
calendar.setGeometry(QtCore.QRect(0, 0, 400, 300))
a.show()
sys.exit(app.exec_())

def calendar_selectionChanged():
    data = calendar.selectedDate().toString("yyyy-MM-dd dddd")
    print(data)
app = QApplication(sys.argv)
calendar = QCalendarWidget()
calendar.setGeometry(QtCore.QRect(0, 0, 400, 300))
calendar.selectionChanged.connect(calendar_selectionChanged)
calendar.show()
sys.exit(app.exec_())