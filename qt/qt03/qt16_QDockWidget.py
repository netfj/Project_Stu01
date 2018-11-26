#coding:utf-8
"""
info:    
author: NetFj@sina.com
file:   qt16_QDockWidget.py 
time:   2018/11/26.17:44
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        hlayout = QHBoxLayout()     #必须使用布局
        self.setLayout(hlayout)

        self.tt = QTextEdit()
        self.setCentralWidget(self.tt)      #在中央放入一个部件

        self.dockWidget = QtWidgets.QDockWidget('我是一个QdockWidget',self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)

        self.dockWidget.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable
            | QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(
            QtCore.Qt.LeftDockWidgetArea
            | QtCore.Qt.RightDockWidgetArea
            | QtCore.Qt.TopDockWidgetArea)

        self.pb = QPushButton('我是DOC内的一个按钮')
        self.dockWidget.setWidget(self.pb)   #加入DOC（这是关键）

        self.pb.clicked.connect(self.pb_clicked)

    def pb_clicked(self):
        self.tt.append('You press me !')
        print('You press me!')

app = QtWidgets.QApplication(sys.argv)
myshow = Window()
myshow.show()
sys.exit(app.exec_())

