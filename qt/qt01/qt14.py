#coding:utf-8
"""
@info: 一个简短的消息框
@author:NetFj @software:PyCharm @file:qt14.py @time:2018/11/7.10:53
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def sinTest():
    print(btn.text())
    btn.setText("按钮文本改变")

app = QApplication([])

main = QWidget()
main.resize(200, 100)
btn = QPushButton("按钮文本", main)
btn.clicked.connect(sinTest)    # 按钮btn的内置信号连接名为sinTest的槽
main.show()
app.exec_()
