from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QWidget, QVBoxLayout, QToolButton, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import os
import sys
import json
from datetime import datetime


def img_path(name):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'img', name)
    else:
        return os.path.join(sys.path[0], 'img', name)


def cmd_path(cmd_name):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'cmd', f'{cmd_name}.cmd')
    else:
        return os.path.join(sys.path[0], 'cmd', f'{cmd_name}.cmd')


def data_path(name):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'data', name)
    else:
        return os.path.join(sys.path[0], 'data', name)


def get_time():
    with open(f'{data_path('tracker')}.json', 'r') as json_data:
        trackerhis = (json.load(json_data))
    if datetime.now().date() == datetime.strptime(trackerhis[0]["Current_date"], '%Y-%m-%d').date():
        return f'Time left : {trackerhis[0]["Time_left"]}'
    else:
        return "Timer not started yet"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(img_path('steamtl'))
        self.setGeometry(700, 300, 0, 0)
        self.initUI()
        self.setWindowIcon(QIcon('./img/steamtl'))

    def initUI(self):

        central__widgit = QWidget()
        self.setCentralWidget(central__widgit)

        label = QLabel()
        button1 = QToolButton()
        button2 = QToolButton()
        button1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        label.setText(get_time())
        button1.setStyleSheet('font-size: 30px;')
        button1.setIcon(QIcon(img_path('limbus')))
        button1.setIconSize(QSize(250, 250))
        button1.setText('Limbus')
        button1.clicked.connect(lambda: self.on_click('limbus_company'))

        button2.setStyleSheet('font-size: 30px;')
        button2.setIcon(QIcon(img_path('zomboid')))
        button2.setIconSize(QSize(250, 250))
        button2.setText('Zomboid')
        button2.clicked.connect(lambda: self.on_click('project_zomboid'))

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(button1)
        vbox.addWidget(button2)

        central__widgit.setLayout(vbox)

    def on_click(self, cmd_name):
        os.system(cmd_path(cmd_name))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
