#coding:utf-8
# @Info: radioButton
# @Author:Netfj@sina.com @File:qt26_main.py @Time:2018/11/17 16:12

import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app=QApplication(sys.argv)#所有的PyQt5应用必须创建一个应用（Application）对象
widgets=QWidget()         #Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
widgets.resize(300,300)   #设置这个Widget的界面大小
widgets.move(200,200)     #设置显示的位置
widgets.setWindowTitle('Example')#窗体的标题

QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))

widgets.show()
sys.exit(app.exec())