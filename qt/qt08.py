# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt08.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.msg1)
        self.pushButton_2.clicked.connect(Form.msg2)
        self.pushButton_3.clicked.connect(Form.msg3)
        self.pushButton_4.clicked.connect(Form.msg4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "标准文件打开、保存框测试"))
        self.pushButton.setText(_translate("Form", "选取文件夹"))
        self.pushButton_2.setText(_translate("Form", "选取文件"))
        self.pushButton_3.setText(_translate("Form", "多文件选择"))
        self.pushButton_4.setText(_translate("Form", "文件保存"))

