#coding:utf-8
"""
@info: 色彩与字体选择框
@author:NetFj @software:PyCharm @file:qt09_main.py @time:2018/11/5.15:22
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QColorDialog,QFontDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from qt09 import Ui_Form

class myform(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myform,self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)

    def msg1(self):
        color = QColorDialog.getColor(Qt.blue,self,'选择颜色')
        if color.isValid():     #检查对象变量是否已经实例化，即实例变量的值是否是个有效的对象句柄。
            print(color.name(),color)
            self.new.bt1.setPalette(QPalette(color))
            self.new.bt1.setAutoFillBackground(True)
            self.new.bt1.setText('改色成功')

    def msg2(self):
        font,ok = QFontDialog.getFont()
        if ok:
            print(font.key)
            self.new.bt2.setFont(font)

    def msg3(self):
        pass
    def msg4(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myform()
    myshow.show()
    sys.exit(app.exec())


