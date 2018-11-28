#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   qt01_main.py 
time:   2018/11/27.19:20
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.Qt import *
from PyQt5 import QtWidgets

from qt01_QFontCombobox import *

class myForm(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fontComboBox.currentFontChanged.connect(self.fc)
        self.pushButton.clicked.connect(self.pc)

    def fc(self,qf):
        self.pushButton.setFont(qf)

    def pc(self):
        qf = QFont('kaiti',16,QFont.Bold)
        self.pushButton.setFont(qf)


        qf = QFont()
        qf.setBold(True)
        qf.setFamily('黑体')
        qf.setPointSize(20)
        qf.setStretch(150)  #拉伸:150%
        self.pushButton2.setFont(qf)

        qf2 =  self.pushButton2.font()
        qf2.setStretch(50)
        self.pushButton3.setFont(qf2)

        print('字体：',qf2.family())
        print('粗体：',qf2.bold())
        print('大小：',qf2.pointSize())
        print('拉伸(%)：',qf2.stretch())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = myForm()
    win.show()
    sys.exit(app.exec_())

