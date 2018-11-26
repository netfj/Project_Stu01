#coding:utf-8
"""
info:    一个箱式布局
author: NetFj@sina.com
file:   qt17_layout.py 
time:   2018/11/27.0:41
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QtWidgets.QGridLayout(self)

        self.pb1=QtWidgets.QPushButton('pb1')
        self.gridLayout.addWidget(self.pb1,0,0,1,1)

        self.pb2=QtWidgets.QPushButton('pb2')
        self.gridLayout.addWidget(self.pb1,0,1,1,1)

        self.pb3=QtWidgets.QPushButton('pb3')
        self.gridLayout.addWidget(self.pb1,1,0,1,1)

        self.pb4=QtWidgets.QPushButton('pb4')
        self.gridLayout.addWidget(self.pb1,1,1,1,1)

        self.resize(800,800)



app=QtWidgets.QApplication(sys.argv)
w = Form()
w.show()
sys.exit(app.exec_())
