# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt10.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 26))
        self.menubar.setObjectName("menubar")
        self.menuOne = QtWidgets.QMenu(self.menubar)
        self.menuOne.setObjectName("menuOne")
        self.menu1_2 = QtWidgets.QMenu(self.menuOne)
        self.menu1_2.setObjectName("menu1_2")
        self.menuTwo = QtWidgets.QMenu(self.menubar)
        self.menuTwo.setObjectName("menuTwo")
        self.menuaddAction_tr_Help_this_SLOT_helpToolBarShow = QtWidgets.QMenu(self.menubar)
        self.menuaddAction_tr_Help_this_SLOT_helpToolBarShow.setObjectName("menuaddAction_tr_Help_this_SLOT_helpToolBarShow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileopen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/q/Warning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileopen.setIcon(icon)
        self.fileopen.setProperty("msg000001", "")
        self.fileopen.setObjectName("fileopen")
        self.test_info = QtWidgets.QAction(MainWindow)
        self.test_info.setObjectName("test_info")
        self.action1_2_1 = QtWidgets.QAction(MainWindow)
        self.action1_2_1.setObjectName("action1_2_1")
        self.action1_2_2 = QtWidgets.QAction(MainWindow)
        self.action1_2_2.setObjectName("action1_2_2")
        self.action2_1 = QtWidgets.QAction(MainWindow)
        self.action2_1.setObjectName("action2_1")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action2_3 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Warning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action2_3.setIcon(icon1)
        self.action2_3.setObjectName("action2_3")
        self.actionTest = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Warning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTest.setIcon(icon2)
        self.actionTest.setObjectName("actionTest")
        self.menu1_2.addAction(self.action1_2_1)
        self.menu1_2.addAction(self.action1_2_2)
        self.menuOne.addAction(self.fileopen)
        self.menuOne.addAction(self.menu1_2.menuAction())
        self.menuOne.addAction(self.test_info)
        self.menuTwo.addAction(self.action2_1)
        self.menuTwo.addAction(self.action2_2)
        self.menuTwo.addAction(self.action2_3)
        self.menuTwo.addAction(self.actionTest)
        self.menubar.addAction(self.menuOne.menuAction())
        self.menubar.addAction(self.menuTwo.menuAction())
        self.menubar.addAction(self.menuaddAction_tr_Help_this_SLOT_helpToolBarShow.menuAction())
        self.toolBar.addAction(self.fileopen)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.mymsg)
        self.test_info.triggered.connect(MainWindow.test_info)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuOne.setTitle(_translate("MainWindow", "One"))
        self.menu1_2.setTitle(_translate("MainWindow", "1-2"))
        self.menuTwo.setTitle(_translate("MainWindow", "Two"))
        self.menuaddAction_tr_Help_this_SLOT_helpToolBarShow.setTitle(_translate("MainWindow", "123"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.fileopen.setText(_translate("MainWindow", "1-1:fileopen"))
        self.fileopen.setShortcut(_translate("MainWindow", "Ctrl+F3"))
        self.test_info.setText(_translate("MainWindow", "1-3:test_info"))
        self.action1_2_1.setText(_translate("MainWindow", "1-2-1"))
        self.action1_2_2.setText(_translate("MainWindow", "1-2-2"))
        self.action2_1.setText(_translate("MainWindow", "2-1"))
        self.action2_2.setText(_translate("MainWindow", "2-2"))
        self.action2_3.setText(_translate("MainWindow", "2-3"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionTest.setToolTip(_translate("MainWindow", "This is a test"))
        self.actionTest.setShortcut(_translate("MainWindow", "F5"))

import qrc001_rc