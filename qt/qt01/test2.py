#coding:utf-8
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import  sys
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(0,0,600,600)
w.show()

QMessageBox.about(w,"关于", "信息在此信息在此信息在此！   ")
QMessageBox.question(w ,'问答框' ,'是否同意?')
QMessageBox.warning(w ,'警告框' ,'信息: 无反馈')
QMessageBox.warning(w ,'警告框' ,'信息：有反馈', QMessageBox.Yes | QMessageBox.No)
QMessageBox.information(w, "信息框1", "消息: 有反馈", QMessageBox.Yes | QMessageBox.No)
QMessageBox.information(w, "信息框2", "消息：无反馈")

# 反馈解析
reply = QMessageBox.information(w, "反馈解析", "消息: 有反馈", QMessageBox.Yes | QMessageBox.No)
if reply==QMessageBox.Yes:
    print("Yes")
if reply==QMessageBox.No:
    print('No')

sys.exit(app.exit_())