from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Pasport_AFS import *

from PyQt5 import QtCore, QtGui, QtWidgets



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())