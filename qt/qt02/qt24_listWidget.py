#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt24_listWidget.py @time:2018/11/15.15:54
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# print('\n'.join(dir(QListWidget)))


app=QApplication(sys.argv)  #所有的PyQt5应用必须创建一个应用（Application）对象
widgets=QListWidget()       #实例化一个(itembase)的列表
widgets.resize(500,500)     #设置窗体大小
widgets.setWindowTitle('QListWidget Example')   #标题


#添加数据
widgets.addItem('1.test')
widgets.addItems(['2.test','3.test'])

#添加图标
item = QtWidgets.QListWidgetItem(QtGui.QIcon('python.png'),'新建项目一')
widgets.addItem(item)
item = QtWidgets.QListWidgetItem(QtGui.QIcon('Warning.ico'),'新建项目二')
widgets.addItem(item)

#设置图片大小
widgets.setIconSize(QSize(125, 125));

widgets.show()
sys.exit(app.exec_())