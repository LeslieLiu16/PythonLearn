import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from Ui_grade_tool import Ui_MainWindow
import spider as sp



class GradeWindows(Ui_MainWindow, QMainWindow):
    '''窗体类'''

    data = {}

    def __init__(self):
        super(GradeWindows, self).__init__()
        self.setupUi(self)

        self.pushButton.setShortcut('enter')
        self.pushButton.clicked.connect(self.get_grades)
        

    def get_grades(self):
        '''获取成绩'''
        self.data[self.lineEdit.text()] = self.lineEdit_3.text()
        try:
            you_grade = sp.login_in(self.lineEdit.text(), self.lineEdit_3.text())
            QMessageBox.information(self, '提示', str(you_grade))
            _translate = QtCore.QCoreApplication.translate
            self.pushButton.setText(_translate("MainWindow", "登录"))
        except ValueError:
            QMessageBox.warning(self, '警告', '发生错误，请检查用户名和密码')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWin = GradeWindows()
    MyWin.show()
    sys.exit(app.exec_())
