#coding:utf-8
"""
info:    
author: NetFj@sina.com
file:   qt15_contianer.py 
time:   2018/11/26.10:16
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *

class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.setup_groupBox()
        self.setup_tabWidget()
        self.setup_stackedWidget()

        self.setGeometry(50,100,1000,700)

    def setup_stackedWidget(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(660,30,300,200)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)

        self.page1 = QtWidgets.QWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.page3)

        self.pb1_in_page1 =  QtWidgets.QPushButton(self.page1)
        self.pb1_in_page1.setText('pb1_in_page1 in Stacked page1')

        self.rb1_in_page2 = QtWidgets.QRadioButton(self.page2)
        self.rb1_in_page2.setText('rb1_in_page2 in Stacked page2')

        #设第2页激活
        self.stackedWidget.setCurrentIndex(1)


    def setup_tabWidget(self):
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(350,30,300,200)

        self.tab1 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab1,'Tab1')

        self.tab2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab2,'Tab2')

        self.tab3 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab3,'Tab3')

        lable1 = QtWidgets.QLabel(self.tab1)
        lable2 = QtWidgets.QLabel(self.tab1)
        lable3 = QtWidgets.QLabel(self.tab1)
        lable1.setText('lable 1 Test!')
        lable2.setText('lable 2 Test!')
        lable3.setText('lable 3 Test!')
        lable1.setGeometry(10,10,100,20)
        lable2.setGeometry(10,40,100,20)
        lable3.setGeometry(10,70,100,20)

        pb1 = QtWidgets.QPushButton(self.tab2)
        pb2 = QtWidgets.QPushButton(self.tab2)
        pb1.setText('tab2 pb 1')
        pb2.setText('tab2 pb 2')
        pb1.setGeometry(10,10,100,35)
        pb2.setGeometry(10,50,100,35)


    def setup_groupBox(self):
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(30,30,300,200)
        self.groupBox.setTitle('Test groupBox')
        rb1 = QtWidgets.QRadioButton(self.groupBox)
        rb2 = QtWidgets.QRadioButton(self.groupBox)
        rb3 = QtWidgets.QRadioButton(self.groupBox)
        rb1.setGeometry(10, 20,200,35)
        rb2.setGeometry(10, 60,200,35)
        rb3.setGeometry(10,100,200,35)
        rb1.setText('select item 1')
        rb2.setText('select item 2')
        rb3.setText('select item 3')



    def setupUi(self):
        self = QtWidgets.QWidget()


app = QtWidgets.QApplication(sys.argv)
myshow=Form()
myshow.show()
sys.exit(app.exec_())