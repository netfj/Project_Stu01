#coding:utf-8
"""
@info: progressBar
@author:NetFj @software:PyCharm @file:qt01_main.py @time:2018/11/18.23:18
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pb_clicked)

    def setupUi(self, Form):
        self.resize(400, 300)
        self.pushButton = QPushButton('Start',self)

    def pb_clicked(self):
        num = 100000
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")

app = QApplication(sys.argv)
myshow = Example()
myshow.show()
sys.exit(app.exec_())

