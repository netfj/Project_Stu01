# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt16_QLayout_grid.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        # Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 351, 241))

        # self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)

        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)


