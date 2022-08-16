import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Ui_Learn import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    '''窗体类'''

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.print_height)
        self.pushButton_2.setShortcut('enter')

    def print_height(self):
        '''输出身高'''
        QMessageBox.information(self, 'info', "你的身高为："+str(self.lineEdit.text())).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
