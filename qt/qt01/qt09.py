# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt09.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.bt1 = QtWidgets.QPushButton(Form)
        self.bt1.setGeometry(QtCore.QRect(20, 17, 261, 61))
        self.bt1.setObjectName("bt1")
        self.bt2 = QtWidgets.QPushButton(Form)
        self.bt2.setGeometry(QtCore.QRect(20, 90, 261, 91))
        self.bt2.setObjectName("bt2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        self.bt1.clicked.connect(Form.msg1)
        self.bt2.clicked.connect(Form.msg2)
        self.pushButton_3.clicked.connect(Form.msg3)
        self.pushButton_4.clicked.connect(Form.msg4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "色彩与字体选择框"))
        self.bt1.setText(_translate("Form", "色彩"))
        self.bt2.setText(_translate("Form", "字体"))
        self.pushButton_3.setText(_translate("Form", "--"))
        self.pushButton_4.setText(_translate("Form", "--"))

