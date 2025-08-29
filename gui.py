import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QWidget, QVBoxLayout, QToolButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("steamtl")
        self.setGeometry(700, 300, 0, 0)
        self.initUI()
        self.setWindowIcon(QIcon('./img/steamtl'))

    def initUI(self):

        central__widgit = QWidget()
        self.setCentralWidget(central__widgit)

        button1 = QToolButton()
        button2 = QToolButton()
        button1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        button1.setStyleSheet('font-size: 30px;')
        button1.setIcon(QIcon('./img/limbus'))
        button1.setIconSize(QSize(250, 250))
        button1.setText('Limbus')
        button1.clicked.connect(lambda: self.on_click('limbus_company'))

        button2.setStyleSheet('font-size: 30px;')
        button2.setIcon(QIcon('./img/zomboid'))
        button2.setIconSize(QSize(250, 250))
        button2.setText('Zomboid')
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
