# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt17_QToolBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 575)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 20, 141, 321))
        self.toolBox.setObjectName("toolBox")

        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 141, 261))
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.toolBox.addItem(self.page, "")

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 141, 261))
        self.page_2.setObjectName("page_2")
        self.radioButton = QtWidgets.QRadioButton(self.page_2)
        self.radioButton.setGeometry(QtCore.QRect(0, 10, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_2)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 40, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.toolBox.addItem(self.page_2, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Page 1"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Page 2"))



class myForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print('这是我的业务内容.')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = myForm()
    mainwindow.show()
    sys.exit(app.exec_())