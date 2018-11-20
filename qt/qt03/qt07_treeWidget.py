#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt07_treeWidget.py @time:2018/11/20.11:32
"""

import sys
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt06_plainTextEdit import Ui_Form

def getitem(item,column):
    #treeItem.clicked()的槽
    print(item.text(0),item.text(1))
    print(column)

app = QApplication(sys.argv)

t = QTreeWidget()
t.resize(700,600)
t.setColumnCount(2)
print('总列数：',t.columnCount())

#列表头
h = t.headerItem()
h.setText(0,"第1列")
h.setText(1,"第2列")

#或者：
t.setHeaderLabels(['第1列','第2列'])

print('表头第1列文本：',h.text(0))
print('表头第2列文本：',h.text(1))

#隐藏表头
t.setHeaderHidden(True)
t.setHeaderHidden(False)    #默认的


#设定列的宽度
t.setColumnWidth(0,400)
t.setColumnWidth(1,300)

#设置根结点
r = QTreeWidgetItem(t)
r.setIcon(0,QIcon('Warning.ico'))   #图标
r.setIcon(1,QIcon('Warning.ico'))   #图标
r.setText(0,'第1个根结点')
print('第1个根键：',r.text(0))

#设置根节点的背景颜色
brush_red=QBrush(Qt.red)
r.setBackground(0,brush_red)
brush_blue=QBrush(Qt.blue)
r.setBackground(1,brush_blue)

for i in range(4):
    item = QTreeWidgetItem(r)
    item.setText(0, '第{}行项目'.format(str(i)))
    item.setText(1, '第{}行列2'.format(str(i)))

r2 = QTreeWidgetItem(t)
r2.setText(0,'这是第2个根键')
i21 = QTreeWidgetItem(r2)
i21.setText(0,'这是根键2的1个子键')
i22 = QTreeWidgetItem(r2)
i22.setText(0,'这是根键2的2个子键')
i211 = QTreeWidgetItem(i21)
i211.setText(0,'这是根键2第1个子键的子键1')
i212 = QTreeWidgetItem(i21)
i212.setText(0,'这是根键2第1个子键的子键2')

#设置节点的状态
i21.setCheckState(0,Qt.Checked)
i21.setCheckState(1,Qt.Checked)


#节点全部展开
t.expandAll()

#设置激活的结点
#定位到第2个一级目录
t.setCurrentItem(t.topLevelItem(1))
#定位到三级目录：路径依次是第2个-第1个-第2个结点
t.setCurrentItem(t.topLevelItem(1).child(0).child(1))

#返回当前的item指针
pointer = t.currentItem()
print(pointer.text(0),pointer.text(1))

#当前item的列编号
col = t.currentColumn()
print(col)

# 增加的操作 -------------------
#增加顶层 addTopLevelItem
d = QTreeWidgetItem()
d.setText(0,'增加顶层1')
d.setText(1,'增加顶层2')
t.addTopLevelItem(d)

#添加子结点 addChild
a = QTreeWidgetItem()
a.setText(0,'增加的1')
a.setText(1,'增加的2')
t.topLevelItem(1).child(0).child(1).addChild(a)

# 增加子结点：批量操作 addChildren
b1 = QTreeWidgetItem()
b1.setText(0,'批量1')
b2 = QTreeWidgetItem()
b2.setText(0,'批量2')
b3 = QTreeWidgetItem()
b3.setText(0,'批量3')
b = [b1,b2,b3]
t.topLevelItem(0).child(1).addChildren(b)


#删除的操作=========================
#删除顶层结点的操作（将删除其下的所有节点）
x=QTreeWidgetItem()
x.setText(0,'这是供练习用的')
t.addTopLevelItem(x)  #设置一个结点以供后面练习删除
re = t.takeTopLevelItem(3)
# 现在我把它重新加上
re.setText(1,'删除又重新添加!!!')
t.addTopLevelItem(re)
del re

#删除节点（会把子节点一同删除）
t.setCurrentItem(t.topLevelItem(1).child(0).child(0))
root = t.invisibleRootItem()
for item in t.selectedItems():
    (item.parent() or root).removeChild(item)

#建立结点的单击信号槽
t.itemClicked.connect(getitem)

t.show()
sys.exit(app.exec_())

