#coding:utf-8
"""
info:    
author: NetFj@sina.com
file:   qt10_QTableWidget_01.py 
time:   2018/11/23.10:25
"""


import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def slot_pb1_clicked():
    font = tw.item(0,0).font()
    font.setBold(True)
    tw.item(0,0).setFont(font)



app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(0,0,1010,800)

tw = QTableWidget(10,4,w)
tw.setGeometry(0,0,800,700)

# 表格外无边框
tw.setFrameShape(QFrame.Box)
tw.setFrameShape(QFrame.NoFrame)
tw.setFrameShape(QFrame.HLine)
tw.setFrameShape(QFrame.VLine)

# tw.setColumnCount(4)
# tw.setRowCount(10)

pb1 = QPushButton(w)
pb2 = QPushButton(w)
pb3 = QPushButton(w)
pb4 = QPushButton(w)
pb1.setGeometry(810,0,200,35)
pb2.setGeometry(810,40,200,35)
pb3.setGeometry(810,80,200,35)
pb4.setGeometry(810,120,200,35)

pb1.setText('set Font')
pb1.clicked.connect(slot_pb1_clicked)

# 表格编辑激活方式
tw.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)

# 选择行为
tw.setSelectionBehavior(QAbstractItemView.SelectRows)
# tw.setSelectionBehavior(QAbstractItemView.SelectColumns)

#选择模式
tw.setSelectionMode(QTableWidget.ExtendedSelection)

'''
选项	描述
QTableWidget.NoSelection	不能选择
QTableWidget.SingleSelection	选中单个目标
QTableWidget.MultiSelection	选中多个目标
QTableWidget.ExtendedSelection	shift键的连续选择
QTableWidget.ContiguousSelection	ctrl键的不连续的多个选择
'''
#水平标签
tw.setHorizontalHeaderLabels(['ID','姓名','性别','收入'])

#垂直标签
tw.setVerticalHeaderLabels(['L1','L2','L3','L4'])
print(tw.verticalHeaderItem(0).text())
print(tw.verticalHeaderItem(1))

# 表格线
tw.setShowGrid(False)
tw.setShowGrid(True)
# tw.setGridStyle(Qt.DashDotDotLine)

for index in range(tw.columnCount()):
    headItem = tw.horizontalHeaderItem(index)
    headItem.setFont(QFont("song", 16, QFont.Bold))
    headItem.setForeground(QBrush(Qt.red))
    headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

# 表头 处理
# tw.horizontalHeader().setVisible(False)     #上横
# tw.verticalHeader().setVisible(False)       #左竖

# 表头 对齐方式
tw.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
tw.horizontalHeaderItem(1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
tw.horizontalHeaderItem(2).setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
tw.horizontalHeaderItem(3).setTextAlignment(Qt.AlignJustify | Qt.AlignBaseline)


# 单元格宽度/高度
tw.setColumnWidth(0,50)  #将第2列的单元格，设置成50宽度
tw.setRowHeight(0,160)      #将第2行的单元格，设置成60的高度
tw.setRowHeight(1,160)      #将第2行的单元格，设置成60的高度

# 在单元格内放置控件
comBox = QComboBox()
comBox.addItems(['男','女'])
comBox.addItem('未知')
# comBox.setStyleSheet('QComboBox{margin:3px}')
tw.setCellWidget(0,2,comBox)

# 添加数据
# 1------
newItem1 = QTableWidgetItem('001')
newItem2 = QTableWidgetItem('张三')
newItem4 = QTableWidgetItem('123456789.99')

tw.setItem(0,0,newItem1)
tw.setItem(0,1,newItem2)
tw.setItem(0,3,newItem4)

tw.item(0,0).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
tw.item(0,1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
tw.item(0,3).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)


# 2-------
newItem1 = QTableWidgetItem('002')
newItem2 = QTableWidgetItem('李四')
newItem3 = QTableWidgetItem('男')
newItem4 = QTableWidgetItem('123456789.99')

newItem1.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
newItem2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
newItem3.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
newItem4.setTextAlignment(Qt.AlignJustify | Qt.AlignBaseline)

tw.setItem(1,0,newItem1)
tw.setItem(1,1,newItem2)
tw.setItem(1,2,newItem3)
tw.setItem(1,3,newItem4)


# 合并
tw.setSpan(3,1,2,3)

a = tw.item(1,1)
a.setFont(QFont("kaiti", 20, QFont.Bold))
a.setText('这是新的名字')
print(a.text())
a.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

tw.item(1,0).setBackground(QBrush(QColor(255, 255, 0)))
tw.item(1,0).setForeground(QBrush(QColor(255,0,0)))

tw.item(1,3).setBackground(QBrush(Qt.red))
tw.item(1,3).setForeground(QBrush(Qt.green))

# 自动行高、列宽
tw.resizeColumnsToContents()
tw.resizeRowsToContents()

# 写数据
for i in range(5,tw.rowCount()):
    item = QTableWidgetItem('第%s行' % (i+1))
    tw.setItem(i,1,item)

# 设置默认的行高列宽
tw.horizontalHeader().setDefaultSectionSize(100)
tw.verticalHeader().setDefaultSectionSize(30)

#设置第一列的宽度
tw.horizontalHeader().resizeSection(0,300)



#设置第一行的高度
tw.verticalHeader().resizeSection(0,200)

#字体加粗
font=tw.horizontalHeader().font()
font.setBold(False)
tw.horizontalHeader().setFont(font)


# 设置横向表头第一个元素的字体加粗
font=QFont()
font.setBold(False)
tw.horizontalHeaderItem(0).setFont(font)
tw.horizontalHeaderItem(1).setFont(font)


# 表头不塌陷
tw.horizontalHeader().setHighlightSections(False)


item=tw.horizontalHeaderItem(1)
item.setText('=--==')
item.setForeground(QColor("blue"))   #设置横向表头第二个元素的颜色


# 插入行列
tw.insertRow(tw.rowCount())
tw.insertColumn(0)


w.show()


sys.exit(app.exec_())