#coding:utf-8
# @Info: radioButton
# @Author:Netfj@sina.com @File:qt26_main.py @Time:2018/11/17 16:12

import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt26_buttons import Ui_Form

class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myForm,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_clicked)


        # 设置 toolButton
        # 弹出样式：文本显示在图标旁边
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton.setText('支付方式')
        self.toolButton.setIcon(QIcon('icon/bank.ico'))

        #构建menu
        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'),'支付宝支付',self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'),'微信支付',self)
        menu.addAction(self.alipayAct)
        menu.addSeparator()
        menu.addAction(self.wechatAct)
        self.toolButton.setMenu(menu)

        #设置菜单响应
        self.alipayAct.triggered.connect(self.on_clicked)
        self.wechatAct.triggered.connect(self.on_clicked)

    def on_clicked(self):
        print('Your chioce: ',self.sender().text())
        if self.sender() == self.alipayAct:
            print('alipay')
        elif self.sender() == self.wechatAct:
            print('wechat')


    def pushButton_clicked(self):
        print('---')




app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())