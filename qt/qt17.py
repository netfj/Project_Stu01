#coding:utf-8
"""
@info: 信号机制，多对多演示
@author:NetFj @software:PyCharm @file:qt17.py @time:2018/11/7.12:07
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SinClass(QObject):
    sin1 = pyqtSignal()
    sin2 = pyqtSignal(int)

    def __init__(self):
        super(SinClass,self).__init__()

    def sin1Call(self,val=0):
        print('sin1 emit !')
    def sin2Call(self,val=0):
        print('sin2 emit: ',val)

    def a_sin1_to_Call12_and_sin2_to_sin1Call(self):
        self.sin1.connect(self.sin1Call)
        self.sin1.connect(self.sin2Call)
        self.sin2.connect(self.sin1)

    def a_emit(self):
        self.sin1.emit()
        self.sin2.emit(1)

sin = SinClass()
sin.a_sin1_to_Call12_and_sin2_to_sin1Call()
sin.a_emit()


