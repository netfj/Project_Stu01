#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt55_lcdNumber.py @time:2018/11/19.9:14
"""

import sys,time
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def refresh():
    t1 = QDate.currentDate()
    t2 = QTime.currentTime()
    intervals = t1.toString(Qt.ISODate) + ' ' + t2.toString()
    lcd.display(intervals)

app = QApplication(sys.argv)
a= QWidget()
a.resize(500,100)
a.setWindowTitle('当前时间')

lcd = QLCDNumber(a)
lcd.setGeometry(QtCore.QRect(0, 0, 500, 100))
lcd.setDigitCount(20)
lcd.setStyleSheet("border: 2px solid black; color: red; background: silver;")

time = QTimer(a)
time.setInterval(1000)
time.timeout.connect(refresh)
time.start()

a.show()
sys.exit(app.exec_())