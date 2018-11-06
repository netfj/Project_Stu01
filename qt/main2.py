#coding:utf-8
"""
:param 调用窗口，加写代码，实现代码与窗口分离
"""

from qt04 import Ui_MainWindow    # 导入生成form.py里生成的类
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()    #执行父类
        self.new = Ui_MainWindow()
        self.new.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())