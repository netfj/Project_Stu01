# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt14_contianers.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 655)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 161, 171))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 115, 19))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 120, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(180, 20, 211, 171))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab2, "")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(440, 20, 171, 171))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.pushButton = QtWidgets.QPushButton(self.page1)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.page2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 30, 115, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.page2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 60, 115, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.stackedWidget.addWidget(self.page2)


        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(40, 270, 201, 171))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "选择地区"))
        self.radioButton.setText(_translate("Form", "安徽"))
        self.radioButton_2.setText(_translate("Form", "上海"))
        self.radioButton_3.setText(_translate("Form", "湖南"))
        self.radioButton_4.setText(_translate("Form", "北京"))
        self.label.setText(_translate("Form", "概况信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "概况"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">细节在此</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.baidu.com\"><span style=\" text-decoration: underline; color:#0000ff;\">继续</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "细节"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.radioButton_5.setText(_translate("Form", "RadioButton"))
        self.radioButton_6.setText(_translate("Form", "RadioButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

