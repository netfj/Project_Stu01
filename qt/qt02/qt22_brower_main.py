#coding:utf-8
"""
@info: Qt与数据库、表的操作配合；主要练习 list / table 部件
@author:NetFj @software:PyCharm @file:qt22_brower_main.py @time:2018/11/12.18:26
"""
import sys, time, logging
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from suport.logging_set import log_config
log_config('qt22_brower_runinfo.log')

from suport.SQLiteClass import Dbt

from qt22_brower import Ui_Form

#新建一个类，继承QT设计的界面，实现业务与界面的分离
class myWin(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)

    def database_create(self):
        filename = QFileDialog.getSaveFileName(self,'指定SQLite数据库文件名','','*.db')
        if filename[0]:
            dbt = Dbt()
            suc = dbt.database_connect(filename[0])
            if suc == True:
                QMessageBox.information(self,'信息','建立成功：'+filename[0])
            else:
                QMessageBox.information(self,'信息','建立失败！')


    def conn_data(self):
        filename = QFileDialog.getOpenFileName(self,'指定SQLite数据库文件','','*.db')
        print(filename)
        if filename[0]:
            dbt = Dbt()
            suc = dbt.database_connect(filename[0])
            if suc :
                tables_all = dbt.tables_all()

                print(tables_all)

    def dis_conn_data(self):
        pass
    def table_create(self):
        pass
    def table_delete(self):
        pass
    def value_insert(self):
        pass
    def value_delete(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWin()
    myshow.show()
    sys.exit(app.exec())