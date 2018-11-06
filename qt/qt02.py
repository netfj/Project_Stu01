#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt02.py @time:2018/11/4.16:33
"""

from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget();
window.show()
sys.exit(app.exec_())
