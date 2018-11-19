#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test.py @time:2018/11/18.23:57
"""

import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys
app = QtWidgets.QApplication (sys.argv)
window = QtWidgets.QWidget ()
window.setWindowTitle ("QToolBox")
window.resize (200, 100)
toolBox = QtWidgets.QToolBox ()
toolBox.addItem (QtWidgets.QPushButton ("Tab Content 1"), "Tab &1")
toolBox.addItem (QtWidgets.QLabel ("Tab Content 2"), "Tab &2")
toolBox.addItem (QtWidgets.QLabel ("Tab Content 3"),QtGui.QIcon('editcut.png'), "Tab &3")
toolBox.setCurrentIndex (0)
vbox = QtWidgets.QVBoxLayout ()
vbox.addWidget (toolBox)
window.setLayout (vbox)
window.show ()
sys.exit (app.exec_ ())
