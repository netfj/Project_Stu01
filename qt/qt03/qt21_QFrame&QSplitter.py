#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   qt21_QFrame&QSplitter.py 
time:   2018/11/27.17:20
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Form(QWidget):
    def __init__(self):
        super().__init__()

        frameLeft = QFrame()
        frameRight = QFrame()
        frameLeft.setFrameShape(QFrame.StyledPanel)
        frameRight.setFrameShape(QFrame.StyledPanel)
        pb1 = QPushButton('frameLeft',frameLeft)
        pb2 = QPushButton('frameRight',frameRight)

        sp1 = QSplitter(Qt.Horizontal)
        sp1.addWidget(frameLeft)
        sp1.addWidget(frameRight)

        frameBottom = QFrame()
        frameBottom.setFrameShape(QFrame.Box)
        pb3 = QPushButton('frameBottom',frameBottom)

        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(frameBottom)

        hbox = QHBoxLayout()
        hbox.addWidget(sp2)
        self.setLayout(hbox)

        self.resize(300,300)


app=QApplication(sys.argv)
myshow=Form()
myshow.show()
sys.exit(app.exec_())

