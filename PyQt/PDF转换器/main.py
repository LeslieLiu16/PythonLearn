import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QFileDialog
from PyQt5 import QtCore
from Ui_window import Ui_MainWindows

class MainWindows(QMainWindow,Ui_MainWindows):
    '''
    窗体类
    '''
    def __init__(self):
        super(MainWindows,self).__init__()
        self.setupUi(self)