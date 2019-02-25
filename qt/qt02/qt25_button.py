# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt25_button.ui'
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
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(140, 10, 231, 31))
        self.toolButton.setObjectName("toolButton")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.radioButton.setObjectName("radioButton")
        self.cb1 = QtWidgets.QCheckBox(Form)
        self.cb1.setGeometry(QtCore.QRect(10, 110, 61, 31))
        self.cb1.setObjectName("cb1")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 160, 167, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(10, 246, 166, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 110, 61, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.cb3 = QtWidgets.QCheckBox(Form)
        self.cb3.setGeometry(QtCore.QRect(150, 110, 61, 31))
        self.cb3.setObjectName("cb3")
        self.cb4 = QtWidgets.QCheckBox(Form)
        self.cb4.setGeometry(QtCore.QRect(220, 110, 61, 31))
        self.cb4.setObjectName("cb4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.toolButton.setText(_translate("Form", "..."))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.cb1.setText(_translate("Form", "CheckBox"))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.cb3.setText(_translate("Form", "CheckBox"))
        self.cb4.setText(_translate("Form", "CheckBox"))

