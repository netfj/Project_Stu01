#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt02_main.py @time:2018/11/19.6:28
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt02_Slider import Ui_Form

class myWin(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)

        self.calendarWidget.selectionChanged.connect(self.cw)
    def cw(self,):
        print('--========\n',self.calendarWidget.selectedDate())
        data = self.calendarWidget.selectedDate().toString("yyyy-MM-dd dddd")
        print('==> ',data)
        print(self.calendarWidget.monthShown(),self.calendarWidget.yearShown())

    def vc(self,v):
        # print('---',v)
        # print(self.horizontalSlider.value())
        # print(self.verticalSlider.value())
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWin()
    myshow.show()
    sys.exit(app.exec())
