# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pasport_AFS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 800))
        self.frame.setMaximumSize(QtCore.QSize(400, 800))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(228, 232, 235);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(40, 150, 341, 51))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 220, 341, 51))
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 290, 361, 81))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_5.setGeometry(QtCore.QRect(40, 430, 381, 51))
        self.textBrowser_5.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 40, 251, 71))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Стили/ЦР-русский_-полный-_web_.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(390, 0, 16, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 800))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_6.setGeometry(QtCore.QRect(40, 360, 331, 51))
        self.textBrowser_6.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_7.setGeometry(QtCore.QRect(40, 500, 231, 51))
        self.textBrowser_7.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 0, 800, 800))
        self.frame_2.setMinimumSize(QtCore.QSize(800, 800))
        self.frame_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.plainTextEdit_folder_2 = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_folder_2.setGeometry(QtCore.QRect(60, 220, 571, 31))
        self.plainTextEdit_folder_2.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}")
        self.plainTextEdit_folder_2.setObjectName("plainTextEdit_folder_2")
        self.plainTextEdit_folder_3 = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_folder_3.setGeometry(QtCore.QRect(60, 290, 571, 31))
        self.plainTextEdit_folder_3.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}")
        self.plainTextEdit_folder_3.setObjectName("plainTextEdit_folder_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(120, 620, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 151, 216);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(60, 150, 581, 31))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::down-button{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 360, 581, 31))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::down-button{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 430, 581, 31))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("QComboBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::down-button{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setCurrentText("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(60, 500, 581, 31))
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet("QComboBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::down-button{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setCurrentText("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(250, 60, 141, 51))
        self.textBrowser_4.setStyleSheet("QTextBrowser{\n"
"    \n"
"    border: 0px\n"
"}")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 620, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 151, 216);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Номер полетного задания</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Дата полета</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Время полета</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Вид АФС</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Тип АФС</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Название БВС</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Паспорт АФС</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Далее"))


