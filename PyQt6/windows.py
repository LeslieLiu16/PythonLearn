from PyQt6.QtWidgets import QApplication, QWidget
import sys


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,200)
    w.move(300,300)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    