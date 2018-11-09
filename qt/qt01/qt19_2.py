#coding:utf-8
"""
@info: pyqt多线程编程
@author:NetFj @software:PyCharm @file:qt19.py @time:2018/11/7.20:17
"""

# 不成功，待进一步测试

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time

global sec
sec = 0

class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(10**8):
            pass
        self.trigger.emit()

def countTime():
    global sec
    sec += 1
    lcdNumber.display(sec)

def work():
    timer.start(1000)
    workThread.start()
    workThread.trigger.connect(timeStop)

def timeStop():
    timer.stop()
    print('run over',lcdNumber.value())
    global sec
    sec = 0

app = QApplication([])
top = QWidget()
layout = QHBoxLayout(top)
lcdNumber=QLCDNumber()
layout.addWidget(lcdNumber)
button =  QPushButton('Test')
layout.addWidget(button)

timer=QTimer()
workThread = WorkThread()

button.clicked.connect(work)
timer.timeout.connect(countTime)

top.show()
app.exec()

'''
流程: 
'''