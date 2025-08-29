import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QWidget, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("steamtl")
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        self.setWindowIcon(QIcon('./img/steamtl'))

    def initUI(self):
        central__widgit = QWidget()
        self.setCentralWidget(central__widgit)

        button1 = QPushButton('Limbus', self)
        button2 = QPushButton('Zomboid', self)

        button1.setStyleSheet('font-size: 30px;')
        button1.setIcon(QIcon('./img/limbus'))
        button1.setIconSize(QSize(500, 250))
        button1.setFixedSize(500, 250)
        button1.clicked.connect(lambda: self.on_click('limbus_company'))
        button2.setStyleSheet('font-size: 30px;')
        button2.setIcon(QIcon('./img/limbus'))
        button2.setIconSize(QSize(500, 250))
        button2.setFixedSize(500, 250)
        button2.clicked.connect(lambda: self.on_click('project_zomboid'))

        vbox = QVBoxLayout()

        vbox.addWidget(button1)
        vbox.addWidget(button2)

        central__widgit.setLayout(vbox)

    def on_click(self, cmd_name):
        os.system(f'{cmd_name}.cmd')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
