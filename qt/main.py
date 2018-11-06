#coding:utf-8
"""
@info: 调用窗口，直接调用
@author:NetFj @software:PyCharm @file:main.py @time:2018/11/4.18:34
"""
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    from qt03 import *

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.setWindowIcon(QIcon('warning.ico'))  #增加icon图标，如果没有图片可以没有这句
    form.show()
    sys.exit(app.exec_())

