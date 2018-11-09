#coding:utf-8
"""
@info: 多线程信号槽通信
@author:NetFj @software:PyCharm @file:qt18.py @time:2018/11/7.19:04
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main(QWidget):
    def __init__(self):
        super(Main,self).__init__()

        #创建一个线程实例，并设置名称、变量、信号槽
        self.thread = MyThread()
        self.thread.setIdentity("thread1")
        self.thread.sinOut.connect(self.outText)
        self.thread.setVal(6)

    def outText(self,text):
        print(text)


class MyThread(QThread):

    sinOut = pyqtSignal(str)

    def __init__(self):
        super(MyThread,self).__init__()
        self.identity = None

    def setIdentity(self,text):
        self.identity = text

    def setVal(self,val):
        self.times = int(val)
        self.start()    # start run

    def run(self):
        while self.times>0 and self.identity:
            ## sent a signal
            self.sinOut.emit(self.identity+":"+str(self.times))
            self.times -= 1

app = QApplication([])
main = Main()
main.show()
app.exec_()

