#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt0702_treeWidget_single_slot.py @time:2018/11/21.16:15
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class myForm(QWidget):
    def __init__(self):
        super().__init__()
        self.Ui()
        self.widget_setup()         #建立部件
        self.data_init()              #数据初始化
        self.single_slot_setup()    #信息与槽初始化

    def Ui(self):
        self = QWidget()

    def widget_setup(self):
        # 建立部件
        # treeWidget
        self.treeWidget = QTreeWidget(self)                 #创建 树 部件
        self.treeWidget.resize(500,400)                     #宽高
        self.treeWidget.setColumnCount(2)                   #列数
        self.treeWidget.setHeaderLabels(['第1列','第2列'])  #列名称
        self.treeWidget.setColumnWidth(0,200)               #列宽
        self.treeWidget.setColumnWidth(1,200)
        self.treeWidget.setSelectionMode(3)                 #选择模式：Ctrl+多选

        # textBrowser : 用于显示执行结果，或提示
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(0,410,800,300)
        self.textBrowser.setText('【textBrowser Display】')

        # pushButton
        self.pb1 = QPushButton(self)
        self.pb2 = QPushButton(self)
        self.pb3 = QPushButton(self)
        self.pb4 = QPushButton(self)
        self.pb5 = QPushButton(self)
        self.pb6 = QPushButton(self)
        self.pb7 = QPushButton(self)

        self.pb1.setGeometry(510,  0,200,35)
        self.pb2.setGeometry(510, 40,200,35)
        self.pb3.setGeometry(510, 80,200,35)
        self.pb4.setGeometry(510,120,200,35)
        self.pb5.setGeometry(510,160,200,35)
        self.pb6.setGeometry(510,200,200,35)
        self.pb7.setGeometry(510,240,200,35)

    def data_init(self):

        self.setWindowTitle('PyQt TreeWidget 示例: 初始化以2列为例')

        #添加树的数据: 增加节点
        r_list = []                                 #一级节点
        for n in range(5):
            r = QTreeWidgetItem()
            r.setText(0,'一级{}(列1)'.format(n+1))
            r.setText(1,'一级{}(列2)'.format(n+1))
            r.setIcon(0,QIcon('../../ico/1a.ico'))
            r.setIcon(1,QIcon('../../ico/1b.ico'))
            brush = QBrush(Qt.yellow)   #背景色
            r.setBackground(0, brush)
            r.setBackground(1, brush)

            rr_list = []                            #二级节点
            for m in range(3):
                rr = QTreeWidgetItem(r)
                rr.setText(0,'一级{}'.format(n+1)+'.二级{}(列1)'.format(m+1))
                rr.setText(1,'一级{}'.format(n+1)+'.二级{}(列2)'.format(m+1))
                rr.setIcon(0, QIcon('../../ico/2a.ico'))
                rr.setIcon(1, QIcon('../../ico/2b.ico'))

                rrr_list = []                       #三级节点
                for p in range(2):
                    rrr = QTreeWidgetItem(rr)
                    rrr.setText(0,'{}.{}.{}_列1'.format(n+1,m+1,p+1))
                    rrr.setText(1,'{}.{}.{}_列2'.format(n+1,m+1,p+1))
                rr_list.append(rrr)

            r_list.append(r)

        self.treeWidget.addTopLevelItems(r_list)

        self.treeWidget.expandAll()  # 展开所有节点

    def single_slot_setup(self):
        self.pb1.setText('&1.当前所有选中节点的信息')
        self.pb2.setText('&2.当前激活的节点信息')
        self.pb3.setText('&3.遍历')
        self.pb4.setText('&4.增')
        self.pb5.setText('&5.删')
        self.pb6.setText('&6.改')
        self.pb7.setText('&7.查')

        self.pb1.clicked.connect(self.solt_pb1_clicked)
        self.pb2.clicked.connect(self.solt_pb2_clicked)
        self.pb3.clicked.connect(self.solt_pb3_clicked)

        self.treeWidget.itemClicked.connect(self.slot_treeWidget_itemClicked)


    def solt_pb1_clicked(self):
        self.p('\nsolt_pb1_clicked: 1.当前所有选中节点的信息')

        info1 = '总列数：' + str(self.treeWidget.columnCount())

        info2 = '列名：' \
                + self.treeWidget.headerItem().text(0) \
                +' | '+ self.treeWidget.headerItem().text(1)

        info3 = '选中的节点: \n'
        items = self.treeWidget.selectedItems()
        if len(items)>0:
            for x in items:
                info3 +='  '+ x.text(0)+'|'+x.text(1) + '\n'
        else:
            info3 += '  无（没有选中的节点）'

        self.p(info1)
        self.p(info2)
        self.p(info3)

    def solt_pb2_clicked(self):
        self.p('\nsolt_pb2_clicked 2.当前节点(激活)的信息:')

        info0 = '(1)self.treeWidget.currentItem():'

        item = self.treeWidget.currentItem()
        info1 = '    节点名称:' + item.text(0) + '|' + item.text(1)

        info2 = '    父节点信息: '
        if not item.parent() == None:
            info2 += item.parent().text(0) + '|' + item.parent().text(1)
        else:
            info2 += '无(本身是一级节点)'

        info3 = '    子节点数:'
        n_childCount = item.childCount()
        info3 += str(n_childCount)

        if n_childCount>0:
            info3 += '\n    子节点名录:'
            for i in range(n_childCount):
                info3 +='\n      ' + item.child(i).text(0)+'|'+item.child(i).text(1)

        self.p(info0)
        self.p(info1)
        self.p(info2)
        self.p(info3)


        info10 = '(2)self.treeWidget.currentIndex():'

        index = self.treeWidget.currentIndex()

        info11 = '  当前节点在兄弟节点中排序是：第{}位'.format(index.row()+1)

        info12 = '  当前节点激活的列是：第{}列'.format(index.column()+1)

        index_parent = index.parent()
        n = index_parent.row()
        if n>=0:
            info13 = '  父节点在其兄弟节点中的排序是：第{}位'.format(index.row()+1)
        else:
            info13 = '  父节点：无（它本身是一级节点）'

        # 通过 index 定位 ：依次求出其父节点的排序（直至顶层一级），形成定位序列
        index = self.treeWidget.currentIndex()
        position = []
        while 1:
            if index.row()>=0:
                position.insert(0,index.row())
                index = index.parent()
            else:
                break
        info14 = '  定位序列（在各级节点中的排序；第1项从0开始）：' + '-'.join([str(x) for x in position])

        # 通过定位序列，求出 节点对象
        info15 = '  当前节点的文本：'
        if len(position)>0:
            x = position.pop(0)
            item = self.treeWidget.topLevelItem(x)
            for x in position:
                item = item.child(x)
            info15 += item.text(0)+'|'+item.text(1)

        self.p(info10)
        self.p(info11)
        self.p(info12)
        self.p(info13)
        self.p(info14)
        self.p(info15)

    def solt_pb3_clicked(self):
        self.p('\nsolt_pb3_clicked 3.遍历:')
        n = self.treeWidget.topLevelItemCount()
        for i in range(n):
            item = self.treeWidget.topLevelItem(i)
            self.recursive_item_child(str(i+1),item)     #调用递归函数把子节点求出

    def recursive_item_child(self,lead,item):
        #本递归函数用于求出一级节点以下的所有子、孙节点
        self.p('['+lead+']'+item.text(0) + '|' + item.text(1))
        n = item.childCount()
        if n>0:
            for m in range(n):
                self.recursive_item_child(lead+'.'+str(m+1),item.child(m))

    def slot_treeWidget_itemClicked(self,item,column_int):
        self.p('\nslot_treeWidget_itemClicked:')
        self.p('点击的节点：{}'.format(item.text(column_int)))

    def p(self,*list):
        if len(list)>0:
            for x in list:
                self.textBrowser.append(str(x))

app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())



