#conding:utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

w = QWidget()

layout = QVBoxLayout()
w.setLayout(layout)


pb1 = QPushButton(w)
pb2 = QPushButton(w)
pb3 = QPushButton(w)
pb4 = QPushButton(w)
pb5 = QPushButton(w)
pb6 = QPushButton(w)

w.resize(600,600)

w.show()

sys.exit(app.exec_())