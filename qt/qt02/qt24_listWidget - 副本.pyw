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

a = dir(QListWidget)
# print(a)
for x in a:
    print(x,type(x))