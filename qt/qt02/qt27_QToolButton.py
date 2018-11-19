#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt27_QToolButton.py @time:2018/11/18.19:50
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def initUI(self):
        # 鼠标移到工具按钮上才会呈现出来，而且有图标和文字信息
        tb = QToolButton(self)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tb.setArrowType(Qt.DownArrow)
        tb.setToolTip('选择适合你的支付方式')
        tb.setPopupMode(QToolButton.MenuButtonPopup)
        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        tb.setAutoRaise(True)   #自动浮现

        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'), '支付宝支付', self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'), '微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'), 'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'), '万事达卡支付', self)

        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)

        tb.setMenu(menu)
        self.show()

        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)

    def on_click(self):
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))

app = QApplication(sys.argv)
myshow = Example()
myshow.initUI()
sys.exit(app.exec_())