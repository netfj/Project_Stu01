#coding:utf-8
"""
info:   QtTreeWidget 综合练习示例
soft:   Python X64 ver 3.7, PyQt5
author: NetFj@sina.com 
file:   qt0702_treeWidget_single_slot.py
time:   2018/11/21.16:15
"""

import sys
from PyQt5 import QtCore
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
        self.treeWidget.setColumnWidth(0,300)               #列宽
        self.treeWidget.setColumnWidth(1,100)
        self.treeWidget.setSelectionMode(3)                 #选择模式：Ctrl+多选

        # textBrowser : 用于显示执行结果，或提示
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(0,410,920,300)
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

        # checkBox
        self.checkBox1 = QCheckBox(self)
        self.checkBox2 = QCheckBox(self)
        self.checkBox3 = QCheckBox(self)
        self.checkBox4 = QCheckBox(self)
        self.checkBox5 = QCheckBox(self)
        self.checkBox6 = QCheckBox(self)
        self.checkBox7 = QCheckBox(self)
        self.checkBox8 = QCheckBox(self)
        self.checkBox1.setGeometry(720,  0,200,25)
        self.checkBox2.setGeometry(720, 30,200,25)
        self.checkBox3.setGeometry(720, 60,200,25)
        self.checkBox4.setGeometry(720, 90,200,25)
        self.checkBox5.setGeometry(720,120,200,25)
        self.checkBox6.setGeometry(720,150,200,25)
        self.checkBox7.setGeometry(720,180,200,25)
        self.checkBox8.setGeometry(720,240,200,25)


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
        # pb按钮
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
        self.pb4.clicked.connect(self.solt_pb4_clicked)
        self.pb5.clicked.connect(self.solt_pb5_clicked)
        self.pb6.clicked.connect(self.solt_pb6_clicked)
        self.pb7.clicked.connect(self.solt_pb7_clicked)

        # 复选框
        self.checkBox1.setText('可选择')
        self.checkBox2.setText('可编辑')
        self.checkBox3.setText('可被拖拉')
        self.checkBox4.setText('可拖放目标（接受）')
        self.checkBox5.setText('用户可检查')
        self.checkBox6.setText('可用')
        self.checkBox7.setText('拥有第三选择状态（半选）')
        self.checkBox8.setText('选择框状态')
        self.checkBox1.toggled.connect(self.slot_checkBox1_toggled)
        self.checkBox2.toggled.connect(self.slot_checkBox2_toggled)
        self.checkBox3.toggled.connect(self.slot_checkBox3_toggled)
        self.checkBox4.toggled.connect(self.slot_checkBox4_toggled)
        self.checkBox5.toggled.connect(self.slot_checkBox5_toggled)
        self.checkBox6.toggled.connect(self.slot_checkBox6_toggled)
        self.checkBox7.toggled.connect(self.slot_checkBox7_toggled)
        self.checkBox8.toggled.connect(self.slot_checkBox8_toggled)

        # 树对象 的 信号与槽
        self.treeWidget.itemClicked.connect(self.slot_treeWidget_itemClicked)



    def slot_checkBox1_toggled(self,b):
        self.p('\nslot_checkBox1_toggled: 可被选择')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsSelectable)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable)

    def slot_checkBox2_toggled(self,b):
        self.p('\nslot_checkBox2_toggled: 可编辑')
        # 设置文本是否可编辑
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

        # 检验是否可编辑
        flags = item.flags()
        if flags & QtCore.Qt.ItemIsEditable:
            self.p("当前节点文本是可编辑的(ItemIsEditable)")
        else:
            self.p("当前节点文本是不可编辑的(NOT ItemIsEditable)")

    def slot_checkBox3_toggled(self, b):
        self.p('\nslot_checkBox3_toggled: 可被拖拉')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsDragEnabled)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsDragEnabled)

    def slot_checkBox4_toggled(self, b):
        self.p('\nslot_checkBox4_toggled: 可拖放目标（接受）')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsDropEnabled)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsDropEnabled)

    def slot_checkBox5_toggled(self, b):
        self.p('\nslot_checkBox5_toggled: 用户可检查')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsUserCheckable)

    def slot_checkBox6_toggled(self, b):
        self.p('\nslot_checkBox6_toggled: 可用')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)

    def slot_checkBox7_toggled(self, b):
        self.p('\nslot_checkBox7_toggled: 拥有第三选中状态（半选中）')
        item = self.treeWidget.currentItem()
        if b:
            item.setFlags(item.flags() | QtCore.Qt.ItemIsTristate)
        else:
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsTristate)

    def slot_checkBox8_toggled(self, b):
        self.p('\nslot_checkBox8_toggled: 选择框')
        if b:
            self.treeWidget.currentItem().setCheckState(0, Qt.Checked)
        else:
            self.treeWidget.currentItem().setCheckState(0, Qt.Unchecked)


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

        self.check_refresh()

        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex()
        if (item==None or index.row()<0):
            self.p('  当前节点总数为0, 没有节点被选取!')
            return

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

    def solt_pb4_clicked(self):
        self.p('\nsolt_pb4_clicked 4.增:')
        item_current = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex()

        if (item_current==None or index.row()<0):
            self.p('  当前节点总数为0, 或没有节点被激活选中!')
            self.p('    增加顶层节点1个: 顶1')
            item = QTreeWidgetItem()
            item.setText(0, '| 添加1个顶层节点：顶1')
            self.treeWidget.addTopLevelItem(item)
            return

        self.p('当前节点是：' + item_current.text(0) +'|'+ item_current.text(1))

        self.p('  1-->添加2个子节点：子1、子2')
        item1 = QTreeWidgetItem()
        item2 = QTreeWidgetItem()
        item1.setText(0,'-->添加1个节点：子1')
        item2.setText(0,'-->添加1个节点：子2')
        item_list = [item1,item2]
        item_current.addChildren(item_list)

        self.p('  2<--添加2个同级节点：同1、同2')
        item_add1 = QTreeWidgetItem()
        item_add2 = QTreeWidgetItem()
        item_add1.setText(0,'<--添加1个同级节点：同1')
        item_add2.setText(0,'<--添加1个同级节点：同2')
        if index.parent().row()>0:  # 判断是否是顶层节点
            item_current.parent().addChild(item_add1)
            item_current.parent().addChild(item_add2)
        else:
            self.treeWidget.addTopLevelItem(item_add1)
            self.treeWidget.addTopLevelItem(item_add2)

    def solt_pb5_clicked(self):
        self.p('\nsolt_pb5_clicked 5.删:')

        item_current = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex()

        if (item_current == None or index.row()<0):
            self.p('  当前没有节点可供删除, 或没有节点被选中激活!')
            return

        self.p('使用 removeChild() 实现')
        self.p('  删除一个节点，注意其子结点将一同被删除！')
        self.p('    当前节点是：' + item_current.text(0) + '|' + item_current.text(1))
        self.p('      删除...（结果可能滞后)...')
        root = self.treeWidget.invisibleRootItem()
        (item_current.parent() or root).removeChild(item_current)
        self.p('      删除...（结果可能滞后)...OK!')

    def solt_pb6_clicked(self):
        self.p('\nsolt_pb6_clicked 6.改:')
        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex()

        if (item == None or index.row()<0):
            self.p('  当前没有节点可供操作, 或没有节点被选中激活!')
            return

        self.p('当前节点：'+item.text(0)+'|'+item.text(1))
        self.p('  先删除然后再建立重建它（放入中转站）,相当于移动')
        if item.parent()==None or index.parent().row()<0:
            self.p('    当前节点是一级节点,使用takeTopLevelItem、addTopLevelItem命令')
            item_take = self.treeWidget.takeTopLevelItem(index.row())
        else:
            self.p('    当前节点是子结点，使用 takeChild')
            item_take = item.parent().takeChild(index.row())

        # 建中转站
        items = self.treeWidget.findItems("【中转站】", Qt.MatchExactly, 0)
        if len(items)>0:
            item_zzz = items[0]
        else:
            item_zzz = QTreeWidgetItem()
            item_zzz.setText(0,'【中转站】')
            self.treeWidget.addTopLevelItem(item_zzz)

        item_zzz.addChild(item_take)


    def solt_pb7_clicked(self):
        self.p('\nsolt_pb6_clicked 7.查:')
        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex()


        items = self.treeWidget.findItems("中转站", Qt.MatchContains,0)
        print(items)

        if len(items) > 0:

            for item in items:
                # print(self.listWidgetName.row(item))

                print(item.text(0))


    def recursive_item_child(self,lead,item):
        #本递归函数用于求出一级节点以下的所有子、孙节点
        self.p('['+lead+']'+item.text(0) + '|' + item.text(1))
        n = item.childCount()
        if n>0:
            for m in range(n):
                self.recursive_item_child(lead+'.'+str(m+1),item.child(m))

    def check_refresh(self):     #选择的节点改变时
        self.p('\nslot_treeWidget_itemSelectionChanged:')

        # 检验是否可选择[1], 并更新 checkBox1
        self.checkBox1.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsSelectable)
        self.p('  可选择：'+str(self.checkBox1.isChecked()))

        # 检验是否可编辑[2], 并更新 checkBox2 （这是个完整样本，语句较细）
        item = self.treeWidget.currentItem()
        flags = item.flags()
        if flags & QtCore.Qt.ItemIsEditable:
            self.p("  当前节点文本是可编辑的(ItemIsEditable)")
            self.checkBox2.setChecked(True)
        else:
            self.p("  当前节点文本是不可编辑的(NOT ItemIsEditable)")
            self.checkBox2.setChecked(False)
        self.p('  可编辑：'+str(self.checkBox2.isChecked()))

        # 检验是否可被拖位[4], 并更新 checkBox3
        self.checkBox3.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsDragEnabled)
        self.p('  可被拖：'+str(self.checkBox3.isChecked()))

        # 检验是否可成为拖放目标（接受）[8], 并更新 checkBox4
        self.checkBox4.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsDropEnabled)
        self.p('  可接受拖放：'+str(self.checkBox4.isChecked()))

        # 检验是否 用户可检查[16], 并更新 checkBox5
        self.checkBox5.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsUserCheckable)
        self.p('  用户可检查：'+str(self.checkBox5.isChecked()))

        # 检验是否可用[32], 并更新 checkBox6
        self.checkBox6.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsEnabled)
        self.p('  可用：'+str(self.checkBox6.isChecked()))

        # 检验是否 有第三状态（半选）[64], 并更新 checkBox7
        self.checkBox7.setChecked(
            self.treeWidget.currentItem().flags()
            & QtCore.Qt.ItemIsTristate)
        self.p('  是否有第三选择状态：'+str(self.checkBox7.isChecked()))

        # 选择框, 并更新 checkBox8
        if self.treeWidget.currentItem().checkState(0)==Qt.Checked:
            self.checkBox8.setChecked(True)
        else:
            self.checkBox8.setChecked(False)
        self.p('  选择：'+str(self.checkBox8.isChecked()))

    def slot_treeWidget_itemClicked(self,item,column_int):
        self.p('\nslot_treeWidget_itemClicked:')
        self.p('点击的节点：{}'.format(item.text(column_int)))
        self.check_refresh()

    def p(self,*list):
        if len(list)>0:
            for x in list:
                self.textBrowser.append(str(x))

app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())



