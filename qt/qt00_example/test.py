#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test.py @time:2018/11/19.9:44
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
a = QWidget()
a.resize(500,300)

label1 = QLabel(a)
label1.resize(200,200)
label1.setWordWrap(True)
label1.setText('label 测试1\n第二行自动换行了自动换行了自动换行了自动换行了')
label1.setFrameStyle(QFrame.Panel | QFrame.Sunken)

label2 = QLabel(a)
label2.setGeometry(QtCore.QRect(210,0,200,100))
label2.setStyleSheet("border: 2px solid red")   #边框
label2.setText('label 测试2')
#插入一图
pix = QPixmap('Warning.ico')
label2.setPixmap(pix)

label3 = QLabel(a)
label3.setGeometry(QtCore.QRect(210,110,200,100))
label3.setStyleSheet("border: 2px solid red")
#插入一图
pix = QPixmap('Warning.ico')
label3.setPixmap(pix)
#修饰图片: 扩展到边界
label3.setScaledContents(True)

a.show()
sys.exit(app.exec_())
