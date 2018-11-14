#coding:utf-8
"""
@info: listWidget 控件的练习
@author:NetFj @software:PyCharm @file:qt23_main.py @time:2018/11/14.19:11
"""

import sys,time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt23_listWidget import Ui_Form

class myWin(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)

    def start(self):
        print('增加项目')
        self.listWidget.addItem('1.Test One')
        self.listWidget.addItem('2.Test Two')
        self.listWidget.addItems(['3.aaa','4.bbb','5.ccc'])


        # 第1个项目设为焦点
        self.listWidget.setCurrentRow(0)

        print('排序')
        # self.listWidget.sortItems()

        print('#在第二行之后插入一项')
        self.listWidget.insertItem(2, '《2》*****《3》')  #在第二行之后插入一项

        # 设置选择模式
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        '''
        选择模式有:  ExtendedSelection    按住ctrl多选,
                    SingleSelection      单选
                    MultiSelection       点击多选
                    ContiguousSelection  鼠标拖拉多选
        '''

    def add(self):
        t = self.lineEdit.text()
        if len(t)>0:
            self.listWidget.addItem(t)
        print(t)

    def delete(self):
        msg = '过程名：delete(self)\n'
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        msg += '删除的项目为：' + item.text()
        self.tb_run.setText(msg)
        del item

        # self.listWidget.insertItem(4, item)   # 删除的项目可以用以重新添加到listWidget

    def info(self):
        msg = '过程名：info(self) 【当前项目信息 按钮的槽】\n'

        n = self.listWidget.count()  # 得到子项总数
        msg += '项目总数（self.listWidget.count()）：'+str(n)+'\n'

        n = self.listWidget.currentRow()
        msg += '\n当前行号（控件获取）【 n=self.listWidget.currentRow() 】：' + str(n) + '\n'

        t = self.listWidget.item(n).text()
        msg += '\n当前行号所在的项目名称（self.listWidget.item(n).text()）：' + t + '\n'

        # print('-- info() -----------')
        # lt = self.listWidget.selectedItems()  # 返回一个 包含item对象 的list 对象
        # print(lt)
        # print(lt[0])
        # print(lt[0].text())
        # print('-------------')
        msg += '\n当前选中的项目(用listWidget.selectedItems()获取):\n'
        msg += '返回列表, 内容为项目相关信息, 名称依次为:\n  '
        lt = self.listWidget.selectedItems()
        t_list = [i.text() for i in lt]
        msg += "\n  ".join(t_list)
        self.tb_info.setText(msg)

    def clear_all(self):
        pass

    def list_text_changed(self,QString):
        # print(QString)
        pass

    def list_row_changed(self,Qint):
        msg = '过程名：list_row_changed(self,Qint)\n'
        msg += '传入参数Qint(当前行号)：' + str(Qint) + '\n'
        self.tb_r.setText(msg)

    def list_clicked(self,QModeIndex):
        print('\nlist_clicked(self,QModeIndex)',end=' --> ')
        print(QModeIndex)
        pass

    def list_item_clicked(self,*QListWidgetItem):
        # print(QListWidgetItem)
        # print(QListWidgetItem[0])
        # print(QListWidgetItem[0].text())

        msg = '过程名：list_item_clicked(self,*QListWidgetItem) \n'
        msg += '返回值是个元组\n'
        msg += '元素个数:'+str(len(QListWidgetItem))+'\n'
        msg += '项目名称依次为(用QListWidgetItem[n].text()方法获得):\n'
        for x in QListWidgetItem:
            msg += x.text()+'\n'
        self.tb_item_clicked.setText(msg)

        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWin()
    myshow.show()
    sys.exit(app.exec())

