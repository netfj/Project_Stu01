#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test.py @time:2018/11/18.23:57
"""

import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


#直接运行程序时的入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    #Window系统提供的模式
    model = QDirModel()
    #创建一个QtreeView部件
    tree = QTreeView()
    #为部件添加模式
    tree.setModel(model)
    tree.setWindowTitle(tree.tr("Dir View"))
    tree.resize(640, 480)
    tree.show()
    sys.exit(app.exec_())
