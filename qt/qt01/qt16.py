#coding:utf-8
"""
@info: 信号机制，带参数的演示
@author:NetFj @software:PyCharm @file:qt16.py @time:2018/11/7.11:28
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SinClass(QObject):

    sin1 = pyqtSignal()
    sin2 = pyqtSignal(int)
    sin3 = pyqtSignal(int,str)
    sin4 = pyqtSignal(list)
    sin5 = pyqtSignal(dict)
    sin6 = pyqtSignal([int,str],[str])

    def __init__(self):
        super(SinClass,self).__init__()
        self.sin1.connect(self.sin1Call)
        self.sin2.connect(self.sin2Call)
        self.sin3.connect(self.sin3Call)
        self.sin4.connect(self.sin4Call)
        self.sin5.connect(self.sin5Call)
        self.sin6[int,str].connect(self.sin6Call)
        self.sin6[str].connect(self.sin6OverCall)

    def em(self):
        self.sin1.emit()
        self.sin2.emit(100)
        self.sin3.emit(1,'text')
        self.sin4.emit([1,2,3,4])
        self.sin5.emit({1:'code','age':12})
        self.sin6[int,str].emit(6,'text')
        self.sin6[str].emit('text')

    def sin1Call(self):
        print('sin1 emit')
    def sin2Call(self,val):
        print('sin2Call',val)
    def sin3Call(self,val,text):
        print('sin3Call',val,text)
    def sin4Call(self,lt):
        print('sin4Call',lt)
    def sin5Call(self,val):
        print('sin5Call',val)
    def sin6Call(self,val,text):
        print('sin6Call',val,text)
    def sin6OverCall(self,val):
        print('sin60OverCall:',val)

sin = SinClass()
sin.em()