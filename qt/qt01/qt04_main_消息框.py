#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt04_main_消息框.py @time:2018/11/4.21:23
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from qt04 import Ui_MainWindow

class win4(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(win4, self).__init__()  # 执行父类
        self.new = Ui_MainWindow()
        self.new.setupUi(self)

    def mytest(self):
        print('mytest is runing ... ')
        self.new.tb.setText(" ")
        self.new.tb.append("正在打印，请稍候...")

    def testQMessageBox(self):
        QMessageBox.about(self, "关于", "信息在此信息在此信息在此！   ")
        QMessageBox.question(self,'问答框','是否同意?')
        QMessageBox.warning(self,'警告框','信息: 无反馈')
        QMessageBox.warning(self,'警告框','信息：有反馈', QMessageBox.Yes | QMessageBox.No)
        QMessageBox.information(self, "信息框1", "消息: 有反馈", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.information(self, "信息框2", "消息：无反馈")

        #反馈解析
        reply = QMessageBox.information(self, "反馈解析", "消息: 有反馈", QMessageBox.Yes | QMessageBox.No)
        if reply==QMessageBox.Yes:
            print("Yes")
        if reply==QMessageBox.No:
            print('No')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = win4()
    myshow.show()
    sys.exit(app.exec())

