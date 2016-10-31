#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


# noinspection PyArgumentList
class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())



