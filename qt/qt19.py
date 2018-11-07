#coding:utf-8
"""
@info: pyqt多线程编程
@author:NetFj @software:PyCharm @file:qt19.py @time:2018/11/7.20:17
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time

global sec
sec = 0
def setTime():
    global sec
    sec+=1
    lcdNumber.display(sec)

def work():
    timer.start(1000)
    for i in range(10**8):
        pass
    timer.stop()

app = QApplication([])
top = QWidget()
layout = QHBoxLayout(top)   # 垂直部局类 QVBoxLayout
lcdNumber = QLCDNumber()
layout.addWidget(lcdNumber)
button = QPushButton('测试')
layout.addWidget(button)

timer=QTimer()
timer.timeout.connect(setTime)
button.clicked.connect(work)

top.show()
app.exec()
