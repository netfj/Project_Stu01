#coding:utf-8
"""
@info:  PYQT5 +python3打造文本编辑器
    https://blog.csdn.net/thindi/article/details/81294314
@author:NetFj @software:PyCharm @file:qt21_edit_main.py @time:2018/11/9.11:55
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt21_edit import Ui_Form

class MyEdit(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyEdit, self).__init__()
        # self.new = Ui_Form()
        self.setupUi(self)

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self,
                                               '打开本地文件')
        if filename[0]:
            # print(filename[0])
            with open(filename[0],mode='r',encoding='utf-8',errors='ignore') as f:
                # print(f.read())
                self.textEdit.setText(f.read())
    def open_files(self):
        filenames = QFileDialog.getOpenFileNames(self,'打开多个文件')
        print(filenames)
        if filenames[0]:
            for file in filenames[0]:
                with open(file,mode='r',encoding='utf-8',errors='ingnore') as f:
                    self.textEdit.append('【File】'+ file)
                    self.textEdit.append(f.read())
                    self.textEdit.append('\n')
    def change_font(self):
        fo,b = QFontDialog.getFont()
        if b:
            self.textEdit.setFont(fo)
    def change_color(self):
        col1 = QColorDialog.getColor(title='选择字体颜色')
        if col1.isValid():
            self.textEdit.setStyleSheet("QTextEdit{color:%s}" % col1.name())
        col2 = QColorDialog.getColor(title='选择背景色')
        if col2.isValid():
            self.textEdit.setStyleSheet("QTextEdit{background-color:%s}" % col2.name())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyEdit()
    myshow.show()
    sys.exit(app.exec())
