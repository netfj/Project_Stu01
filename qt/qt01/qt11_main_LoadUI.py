#coding:utf-8
"""
@info: 直接调用 UI 文件
@author:NetFj @software:PyCharm @file:qt11_main_LoadUI.py @time:2018/11/5.20:18
"""


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        loadUi('qt11.ui',self)
        self.setFixedSize(self.sizeHint())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

#  不成功, 待进一步测试 ......