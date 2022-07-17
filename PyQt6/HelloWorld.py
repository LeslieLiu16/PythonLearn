import sys
from PyQt5.QtWidgets import QAction, qApp, QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from boto import BUCKET_NAME_RE
from PyQt5.QtCore import QCoreApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(0, 50, 960, 800)
        self.center()
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)       
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.statusBar().showMessage('准备就绪')
        self.setWindowTitle('Hello World')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        self.setWindowIcon(QIcon('Web.png'))
        QToolTip.setFont(QFont('SansSerif', 10))
        btn = QPushButton('确定', self)
        btn.setToolTip('This is a button')
        self.setToolTip('This is a simple example')
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(500,500)
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self,'Message','确定要退出吗？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

