#coding:utf-8
"""
info:   QMidArea
author: NetFj@sina.com
file:   qt19_QMidArea.py 
time:   2018/11/27.11:57
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1500,800)
        self.n = 1  #用于标识当前有多少个子容器

        #创建 QMidArea ，并作为中央部件实例化
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #创建菜单
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu('&File')

        # 创建子菜单
        self.file.addAction('&New')
        self.file.addAction('&Cascade(瀑布)')
        self.file.addAction('&Tiled（平铺）')
        self.file.addAction('Test')

        # 设定菜单的槽，传递参数 QAction
        self.file.triggered.connect(self.menu_action)

    def menu_action(self,qaction):
        if qaction.text()=='&New':
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle(str(self.n))
            sub.setObjectName('sub'+str(self.n))

            if self.n==1:
                sub1 = sub

            self.mdi.addSubWindow(sub)
            sub.show()
            self.n += 1

        if qaction.text()=='&Cascade(瀑布)':
            # 级联显示
            self.mdi.cascadeSubWindows()

        if qaction.text()=='&Tiled（平铺）':
            # 平铺显示
            self.mdi.tileSubWindows()

        if qaction.text()=='Test':
            win = self.mdi.currentSubWindow()
            self.mdi.setActiveSubWindow(sub1)



app = QApplication(sys.argv)
myshow = Window()
myshow.show()
sys.exit(app.exec_())
