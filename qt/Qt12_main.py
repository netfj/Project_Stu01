#coding:utf-8
"""
@info: 父窗体调用子窗体
@author:NetFj @software:PyCharm @file:Qt12_main.py @time:2018/11/6.9:14
"""


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Qt12_MainForm import Ui_MainWindow
from qt12_Children import Ui_Form


class MainForm(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        # self.new = Ui_MainWindow()
        self.setupUi(self)

        self.child = ChildrenForm()     #生成子窗口实例

    def childShow(self):
        print('---------')
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

class ChildrenForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec())



