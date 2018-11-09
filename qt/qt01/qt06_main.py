#coding:utf-8
"""
@info: 基本输入框 QInputDialog
@author:NetFj @software:PyCharm @file:qt06_main.py @time:2018/11/5.13:45
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit,QInputDialog
import sys
from qt06 import Ui_Form

class myWidget(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWidget,self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)

    def msg(self):
        doubleNum,ok1 = QInputDialog.getDouble(self,'标题','计数',37.56,-10000,10000,2)
        print(doubleNum,ok1)

        intNum, ok2 = QInputDialog.getInt(self, '标题', '计数', 0, -10000, 10000, 2)
        print(intNum, ok2)

        stringNum, ok3 = QInputDialog.getText(self, '标题', '姓名', QLineEdit.Normal, '张三丰')
        print(stringNum, ok3)

        items = ['Spring','Summer','Fall','Winter']
        item, ok4 = QInputDialog.getItem(self, '标题', '季节',items,1,True)
        print(item, ok4)

        text,ok5 = QInputDialog.getMultiLineText(self,'标题','地址','青城街1号')
        print(text,ok5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWidget()
    myshow.show()
    sys.exit(app.exec())

