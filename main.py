from ishodnie_dannye import *
from main_menu import *
from PyQt5 import QtWidgets
import json
import sys


def getDirectory_logs():
    dirlist = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder.setPlainText(format(dirlist))

def getDirectory_path_document():
    dirlist = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder_4.setPlainText(format(dirlist))

def btn_click():
    # СЧИТЫВАНИЕ ДАННЫХ
    folder_with_logs = ui.plainTextEdit_folder.toPlainText() # папка с логами
    operator = ui.plainTextEdit_folder_2.toPlainText() # ФИО оператора 
    object_name = ui.plainTextEdit_folder_3.toPlainText() # наименование объекта
    path_for_document = ui.plainTextEdit_folder_4.toPlainText() # путь до создоваемого файла
    file_name = ui.plainTextEdit_folder_5.toPlainText() # название excel файла
    
    pasport_ishodnie_dannye = {
    "folder_with_logs" : folder_with_logs,
    "operator" : operator,
    "object_name" : object_name,
    "path_for_document" : path_for_document,
    "file_name" : file_name,
    }
    with open("data.json","w") as write_file: 
        json.dump(pasport_ishodnie_dannye,write_file) 
    change()


def change():
    MainWindow.close()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ishodnie_dannye()
ui.setupUi(MainWindow)



with open("data.json", "r") as read_file:
    data = json.load(read_file)
print(data['file_name'])
ui.plainTextEdit_folder.setPlainText(data["folder_with_logs"])
ui.plainTextEdit_folder_2.setPlainText(data["operator"])
ui.plainTextEdit_folder_3.setPlainText(data["object_name"])
ui.plainTextEdit_folder_4.setPlainText(data["path_for_document"])
ui.plainTextEdit_folder_5.setPlainText(data["file_name"])

ui.pushButton_folder.clicked.connect(getDirectory_logs)
# ui.pushButton_folder.clicked.connect(change)
ui.pushButton_folder_2.clicked.connect(getDirectory_path_document)
ui.pushButton.clicked.connect(btn_click)



MainWindow.show()
sys.exit(app.exec_())