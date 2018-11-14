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
    db=''
    tb=''
    record=0
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
        print(filename[0])
        if filename[0]:
            self.dbt = Dbt()
            suc = self.dbt.database_connect(filename[0])
            if suc == True:
                tables_all = self.dbt.tables_all_get()
                if len(tables_all)>0:
                    for x in tables_all:
                        self.listWidget.addItem(x[0])
                    self.listWidget.setCurrentRow(0)
                    # self.list_text_changed()

    def list_double_click(self,item):
        print(type(item))

    def list_text_changed(self,t):
        print(t)
        value = self.dbt.query_table(t)
        struct = self.dbt.table_structure_get(t)
        self.table_set(value,struct)

    def dis_conn_data(self):
        pass
    def table_create(self):
        pass
    def table_delete(self):
        pass
    def value_insert(self):
        self.dbt.value_insert('t1',"('name','age')","('Tom',20),('Kite',21)")

    def value_delete(self):
        pass

    def table_set(self,value,struct):
        # print(value)
        # print(struct)

        n = len(value)
        if n == 0:
            return
        m = len(value[0])

        self.tableWidget.setColumnCount(m)
        self.tableWidget.setRowCount(n)


        for x in range(n):
            for y in range(m):
                v = str(value[x][y])  # 内容
                self.tableWidget.setItem(x, y, QTableWidgetItem(v))

        # 设置高度
        for x in range(n):
            self.tableWidget.setRowHeight(x, 30)
        # 设置宽度
        for y in range(m):
            self.tableWidget.setColumnWidth(y, 80)

        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直表头
        # self.tableWidget.horizontalHeader().setVisible(False)#隐藏水平表头

        #设置表头
        print(struct)
        st = []
        for x in struct:
            st.append(x[1])
        print(st)
        self.tableWidget.setHorizontalHeaderLabels(st)

        # 设置水平方向表格为自适应的伸缩模式
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 将行与列的高度设置为所显示的内容的宽度高度匹配
        QTableWidget.resizeColumnsToContents(self.tableWidget)
        QTableWidget.resizeRowsToContents(self.tableWidget)

        # 表格整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWin()
    myshow.show()
    sys.exit(app.exec())