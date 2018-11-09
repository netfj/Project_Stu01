#coding:utf-8
"""
@info: 测试信息和槽
@author:NetFj @software:PyCharm @file:qt05_main.py @time:2018/11/5.10:53
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from qt05 import Ui_Form

class myform(QtWidgets.QWidget,Ui_Form):
    _singnal = QtCore.pyqtSignal(str)    # 定义信息，参数为str型
    def __init__(self):
        super(myform,self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)
        self._singnal.connect(self.mySingnal)      #将信号连接到槽:函数 mySingle()

    def test_info(self):
        self.new.tb.setText('')
        self.new.tb.setText('正在打印，稍等....')
        self._singnal.emit('发送一个信息：你结束了吗，请回答！')

    def mySingnal(self,string):                 #这个函数相当于槽，响应绑定的信号
        self.new.tb.append('信息收到：')
        self.new.tb.append(string)
        self.new.tb.append('打印结束！')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myform()
    myshow.show()
    sys.exit(app.exec())
