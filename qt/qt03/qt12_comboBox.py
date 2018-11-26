#coding:utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class myForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setupWidgets()
        self.setup_signal_slot()

        self.setGeometry(100, 200, 500, 600)

    def setupUi(self):
        self = QWidget()

    def setupWidgets(self):
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(10,10,400,80)
        self.comboBox.addItem(QIcon('../../ico/1a.ico'),'1.第1项有图标')
        self.comboBox.addItems(['2.批量加','3.批量加'])
        self.comboBox.setFont(QFont('song',18))

    def setup_signal_slot(self):
        # 指定参数的不同类型
        self.comboBox.currentIndexChanged['int'].connect(self.slot_comboBox_1)
        self.comboBox.currentIndexChanged['QString'].connect(self.slot_comboBox_2)

    def slot_comboBox_1(self,int):
        print('传入的参数是: ',int)

    def slot_comboBox_2(self, str):
        print('传入的参数是: ', str)

app = QApplication(sys.argv)
myshow = myForm()
myshow.show()
sys.exit(app.exec_())