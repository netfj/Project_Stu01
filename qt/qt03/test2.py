#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test2.py @time:2018/11/19.16:32
"""
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyQQ(QTabWidget):
    def __init__(self, parent=None):
        super(MyQQ, self).__init__(parent)

        toolButton1 = QToolButton()
        toolButton1.setText(self.tr("gavin"))
        toolButton1.setIcon(QIcon("Warning.ico"))
        toolButton1.setIconSize(QSize(60, 60))
        toolButton1.setAutoRaise(True)
        toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        toolButton2 = QToolButton()
        toolButton2.setText(self.tr("问题的方法"))
        toolButton2.setIcon(QIcon("Warning.ico"))
        toolButton2.setIconSize(QSize(60, 60))
        toolButton2.setAutoRaise(True)
        toolButton2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        toolButton3 = QToolButton()
        toolButton3.setText(self.tr("为什么"))
        toolButton3.setIcon(QIcon("Warning.ico"))
        toolButton3.setIconSize(QSize(60, 60))
        toolButton3.setAutoRaise(True)
        toolButton3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        groupbox1 = QGroupBox()
        vlayout1 = QVBoxLayout(groupbox1)
        vlayout1.setAlignment(Qt.AlignCenter)
        vlayout1.addWidget(toolButton1)
        vlayout1.addWidget(toolButton2)
        vlayout1.addStretch()

        groupbox2 = QGroupBox()
        vlayout2 = QVBoxLayout(groupbox2)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton3)
        vlayout2.addStretch()

        groupbox3 = QGroupBox()

        toolbox1 = QToolBox()
        toolbox1.addItem(groupbox1, self.tr("我的好友"))
        toolbox1.addItem(groupbox2, self.tr("同事"))
        toolbox1.addItem(groupbox3, "黑名单")

        toolbox2 = QToolBox()

        self.addTab(toolbox1, "联系人")
        self.addTab(toolbox2, "群/讨论组")


app = QApplication(sys.argv)
myqq = MyQQ()
myqq.setWindowTitle("QQ2012")
myqq.show()
app.exec_()