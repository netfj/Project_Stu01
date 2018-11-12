# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt21_edit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 505)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb1 = QtWidgets.QPushButton(Form)
        self.pb1.setObjectName("pb1")
        self.verticalLayout.addWidget(self.pb1)
        self.pb2 = QtWidgets.QPushButton(Form)
        self.pb2.setObjectName("pb2")
        self.verticalLayout.addWidget(self.pb2)
        self.pb3 = QtWidgets.QPushButton(Form)
        self.pb3.setObjectName("pb3")
        self.verticalLayout.addWidget(self.pb3)
        self.pb4 = QtWidgets.QPushButton(Form)
        self.pb4.setObjectName("pb4")
        self.verticalLayout.addWidget(self.pb4)
        self.pb5 = QtWidgets.QPushButton(Form)
        self.pb5.setObjectName("pb5")
        self.verticalLayout.addWidget(self.pb5)
        self.pb6 = QtWidgets.QPushButton(Form)
        self.pb6.setObjectName("pb6")
        self.verticalLayout.addWidget(self.pb6)
        self.pb7 = QtWidgets.QPushButton(Form)
        self.pb7.setObjectName("pb7")
        self.verticalLayout.addWidget(self.pb7)
        self.pb8 = QtWidgets.QPushButton(Form)
        self.pb8.setObjectName("pb8")
        self.verticalLayout.addWidget(self.pb8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.pb1.clicked.connect(Form.open_file)
        self.pb2.clicked.connect(Form.open_files)
        self.pb3.clicked.connect(Form.change_font)
        self.pb4.clicked.connect(Form.change_color)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文本编辑器"))
        self.pb1.setText(_translate("Form", "打开文件（&F）"))
        self.pb2.setText(_translate("Form", "打开多文本"))
        self.pb3.setText(_translate("Form", "修改字体"))
        self.pb4.setText(_translate("Form", "修改颜色"))
        self.pb5.setText(_translate("Form", "保存文件"))
        self.pb6.setText(_translate("Form", "页面设置"))
        self.pb7.setText(_translate("Form", "文本打印"))
        self.pb8.setText(_translate("Form", "清除文件"))

