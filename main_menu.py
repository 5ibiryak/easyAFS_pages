from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setSizeIncrement(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 251, 71))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ЦР-русский_-полный-_web_.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
    
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(355, 260, 489, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton1.setFont(font)
        self.pushButton1.setMouseTracking(True)
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 151, 216);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton1.setAutoRepeat(False)
        self.pushButton1.setObjectName("pushButton1")
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(355, 365, 489, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton2.setFont(font)
        self.pushButton2.setMouseTracking(True)
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 151, 216);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton2.setAutoRepeat(False)
        self.pushButton2.setObjectName("pushButton2")
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(355, 470, 489, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton3.setFont(font)
        self.pushButton3.setMouseTracking(True)
        self.pushButton3.setAutoFillBackground(False)
        self.pushButton3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 151, 216);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton3.setAutoRepeat(False)
        self.pushButton3.setObjectName("pushButton3")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flight Docs"))
        self.pushButton1.setText(_translate("MainWindow", "Исходные данные"))
        self.pushButton2.setText(_translate("MainWindow", "Паспорта АФС"))
        self.pushButton3.setText(_translate("MainWindow", "Журнал полётов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
