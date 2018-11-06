#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt10_main.py @time:2018/11/5.16:10
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from qt10 import Ui_MainWindow

class myMainWin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myMainWin,self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)
        self.new.fileopen.triggered.connect(self.msg)

    def msg(self):
        file,ok=QFileDialog.getOpenFileName(
            self,'Open','d:/','*.txt')
        self.new.statusbar.showMessage('[这是状态栏] 你选择了这个文件:  '+file)
        print(file,ok)

    def test_info(self):
        print('==================================')

    def mymsg(self):
        print('~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myMainWin()
    myshow.show()
    sys.exit(app.exec())

