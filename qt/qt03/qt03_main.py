#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt03_main.py @time:2018/11/19.15:59
"""
import sys
from PyQt5.QtWidgets import QWidget,QToolButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt03_toolBox import Ui_Form

class myForm(QWidget,Ui_Form):
    def __init__(self):
        super(myForm,self).__init__()
        self.setupUi(self)

        toolButton1 = QToolButton()
        toolButton1.setText(self.tr("gavin"))
        toolButton1.setIcon(QIcon("Warning.ico"))
        toolButton1.setIconSize(QSize(60, 60))
        toolButton1.setAutoRaise(True)
        toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())
