#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   qt03_color.py 
time:   2018/11/28.17:35
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class myForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel('这是label',self)
        label2 = QLabel('这是label',self)
        label3 = QLabel('这是label',self)
        label4 = QLabel('这是label',self)
        label5 = QLabel('这是label',self)
        label6 = QLabel('这是label',self)

        label2.move(0,30)
        label3.move(0,60)
        label4.move(0,90)
        label5.move(0,120)
        label6.move(0,150)

        label1.setStyleSheet('QLabel{background-color:rgb(110,255,0)}')
        label2.setStyleSheet("color:red")
        label3.setStyleSheet("color:rgb(20,200,200)")
        label4.setStyleSheet('color:red')
        label5.setStyleSheet('font: 18pt "楷体"')
        label6.setStyleSheet('font: 30pt "黑体"')

        print(label1.styleSheet())
        print(label2.styleSheet())
        print(label3.styleSheet())
        print(label4.styleSheet())

        col = QColorDialog.getColor(title='选择字体颜色')
        if col.isValid():
            label5.setStyleSheet("color:%s" % col.name())

        label6.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        label6.setPalette(palette)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = myForm()
    win.show()
    sys.exit(app.exec_())