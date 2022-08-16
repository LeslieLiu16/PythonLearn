import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from Ui_game import Ui_MainWindow
from random import randint



class MainWindows(QMainWindow, Ui_MainWindow):
    '''窗体类'''
    num = 0
    randnum = 0
    a = 0
    b = 100

    def __init__(self):
        super(MainWindows, self).__init__()
        self.setupUi(self)
        self.pushButton.setShortcut('enter')
        self.pushButton.clicked.connect(self.get_num)
        self.pushButton_2.clicked.connect(self.rand_randnum)
        self.pushButton_2.clicked.connect(self.re_game)
    
    def rand_randnum(self):
        '''获取一个随机数'''
        self.randnum = randint(1, 99)

    def get_num(self):
        '''基本逻辑'''
        input_ =int(self.lineEdit.text())
        if(input_ <= self.a or input_ >= self.b):
            QMessageBox.warning(self, '警告', '输入错误！')
            self.lineEdit.setText("")
        elif(self.randnum == input_):
            QMessageBox.information(self, '提示', '你输了！数字炸弹为：'+str(self.randnum))
            self.lineEdit.setText("")
        elif(self.randnum < input_):
            self.b = input_
            self.lineEdit.setText("")
        elif(self.randnum > input_):
            self.a = input_
            self.lineEdit.setText("")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "请输入"+str(self.a)+"~"+str(self.b)+"的数字"))

    def re_game(self):
        '''重新启动游戏'''
        self.a = 0
        self.b = 100
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "请输入"+str(self.a)+"~"+str(self.b)+"的数字"))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWin = MainWindows()
    MyWin.show()
    sys.exit(app.exec_())
