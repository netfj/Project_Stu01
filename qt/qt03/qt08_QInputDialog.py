#coding:utf-8
"""
info:   标准输入对话框
author: NetFj@sina.com
file:   qt08_QInputDialog.py 
time:   2018/11/23.9:20
"""
import sys
from PyQt5.QtWidgets import (QWidget,QInputDialog,QApplication)

app = QApplication(sys.argv)
w = QWidget()
w.show()

sender = ''
sex = ['男','女']

text, ok = QInputDialog.getText(w,'修改姓名', '请输入姓名：')
if ok:
    print(text)

text, ok = QInputDialog.getInt(w,'修改年龄', '请输入年龄：', min = 1)
if ok:
    print(str(text))

text, ok = QInputDialog.getItem(w,'修改性别', '请选择性别：',sex)
if ok:
    print(text)

text, ok = QInputDialog.getDouble(w,'修改身高', '请输入身高：', min = 1.0)
if ok:
    print(str(text))

text, ok = QInputDialog.getMultiLineText(w,'修改信息', '请输入个人信息：')
if ok:
    print(text)

sys.exit(app.exec_())