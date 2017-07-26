#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from functools import partial

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QFile

icon_dir = '../resource/icons'

class Status(QtWidgets.QStatusBar):
    def __init__(self, parent, height):
        super().__init__(parent)
        self.setFixedHeight(height)


class Action(QtWidgets.QAction):
    def __init__(self, icon, name, parent):
        super().__init__(icon, name, parent)


class Spacer(QtWidgets.QWidget):
    def __init__(self, w, h):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        box.addSpacerItem(QtWidgets.QSpacerItem(w, h,
                                                QtWidgets.QSizePolicy.Expanding))


class Tool(QtWidgets.QToolBar):
    SPACER = 'SPACER'

    def __init__(self, parent, height, actions):
        super().__init__(parent)
        self.setFixedHeight(height)
        self.setIconSize(QtCore.QSize(height, height))
        self.init_actions(actions)

    def init_actions(self, actions):
        for item in actions:
            if isinstance(item, Action):
                self.addAction(item)
            elif isinstance(item, Spacer):
                self.addWidget(item)


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtWidgets.QFrame()
        self.center.setObjectName('center_frame')
        self.setCentralWidget(self.center)
        self.center_box = QtWidgets.QVBoxLayout(self.center)
        self.center_box.setSpacing(0)
        self.center_box.setContentsMargins(0, 0, 0, 0)

    def action_method(self, name_action):
        try:
            getattr(self, name_action)()
        except Exception as er:
            print(er)



    def add_gui_sea(self, model_sea):
        self.center_box.addWidget(model_sea)

    def init_tool_bar(self, tool_bar):
        self.addToolBar(QtCore.Qt.BottomToolBarArea, tool_bar)

    def init_status(self, status):
        self.setStatusBar(status)

    def tool_actions(self, names):
        actions = []
        for name in names:
            if name == Tool.SPACER:
                spacer = Spacer(0, 0)
                actions.append(spacer)
            else:
                name_not_ext = os.path.splitext(name)[0]
                icon = QtGui.QIcon(os.path.join(icon_dir, name))
                act = Action(icon, name_not_ext, self)
                act.triggered.connect(
                    partial(self.action_method, name_not_ext))
                actions.append(act)
        return actions

    def load_style_sheet(self, sheetName):
        file_name = sheetName + '.css'
        file = QFile('../style/css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)


class AttachFile(QtWidgets.QFrame):
    def __init__(self, parent, file_name):
        super().__init__()
        self.parent = parent
        self.setMinimumHeight(38)
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setSpacing(15)
        self.box.setContentsMargins(0, 0, 0, 0)

        self.file_butn = QtWidgets.QPushButton()
        self.file_butn.setObjectName("file_btn")
        self.file_butn.setCursor(QtCore.Qt.PointingHandCursor)

        self.del_file = QtWidgets.QPushButton()
        self.del_file.setIcon(QtGui.QIcon("../resource/icons/del_file.png"))
        self.del_file.setIconSize(QtCore.QSize(15, 15))
        self.del_file.setObjectName("del_file")

        self.del_file.clicked.connect(self.close_file)


        self.box.addWidget(self.file_butn, stretch=1)

        self.box.addWidget(self.del_file)
        self.file_butn.setText(file_name)

    def close_file(self):
        self.close()


class AttachWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.attach = {}
        self.setMinimumHeight(41)
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)

    def add_file(self, file_name):
        name_text = os.path.basename(file_name)
        self.attach[file_name] = (AttachFile(self, name_text))
        self.box.addWidget(self.attach[file_name])
        return self.attach[file_name].file_butn




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
