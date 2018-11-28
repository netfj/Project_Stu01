#coding:utf-8
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Exampl(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500, 600)

        lable = QLabel('Start: 这是标签', self)
        lable.setGeometry(1,1,200,30)

        pushButton = QPushButton('Start: 这是按钮', self)
        pushButton.setGeometry(5,40,200,40)

        TextBr = QTextBrowser(self)
        TextBr.setGeometry(10, 80, 200, 100)
        TextBr.append('QTextBrowser')

        Frame = QFrame(self)
        Frame.setGeometry(1,200,200,200)

        # self.setStyleSheet('QMainWindow{background-color:rgb(0,0,0)}'
        #                    'QPushButton{background-color:rgb(255,0,0)}'
        #                    'QFrame{background-color:rgb(0,255,0)}'
        #                    'QTextBrowser{background-color:rgb(0,0,255)}')

        with open('qss1.txt') as f:
            s = f.read()
        str = ''.join(s).strip('\n')
        self.setStyleSheet(str)

app = QApplication(sys.argv)
w = Exampl()
w.show()
sys.exit(app.exec_())