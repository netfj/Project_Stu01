#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:qt56_label.py @time:2018/11/19.10:22
"""


import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

t = '''
<html>
<body>
<p><span style=" text-decoration: underline;">富文本测试</span></p>
<p><span style=" font-weight:600;">字体粗</span></p>
<p><span style=" font-size:16pt; font-style:italic;">字体大斜</span></p>
</body>
</html>
'''

app = QApplication(sys.argv)
a = QWidget()
a.resize(500,300)

label1 = QLabel(a)
label1.resize(200,200)
label1.setText(t)

label2 = QLabel(a)
label2.setGeometry(QtCore.QRect(210,0,280,300))
label2.setScaledContents(True)
movie = QMovie("timg.gif")
label2.setMovie(movie)
movie.start()

a.show()
sys.exit(app.exec_())