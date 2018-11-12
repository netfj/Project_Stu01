#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt08_main_PushButton.py @time:2018/11/5.14:55
"""

import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QFileDialog
from qt08 import Ui_Form

class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myForm,self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)

    def msg1(self):
        dir1 = QFileDialog.getExistingDirectory(
            self,'选取文件夹','C:\\')
        print(dir1)

    def msg2(self):
        filename1,filetype = QFileDialog.getOpenFileName(
            self,'选取文件','C:\\','All File(*);;text(*.txt);py(*.py)')
        print(filename1,filetype)

    def msg3(self):
        files,ok1 = QFileDialog.getOpenFileNames(
            self,'多选文件','C:\\','All(*)')
        print(files,ok1)

    def msg4(self):
        filename2,ok2=QFileDialog.getSaveFileName(
            self,'文件保存','C:\\','')
        print(filename2,ok2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myForm()
    myshow.show()
    sys.exit(app.exec())
