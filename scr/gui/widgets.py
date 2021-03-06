#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from functools import partial

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QFile

icon_dir = '../resource/icons'

_box_margin = (0, 0, 0, 0)
_box_spacing = 0


class Box(QtWidgets.QBoxLayout):
    horizontal = QtWidgets.QBoxLayout.LeftToRight = 0
    vertical = QtWidgets.QBoxLayout.TopToBottom = 2

    def __init__(self, direction, parent=None,
                 margin=_box_margin, spacing=_box_spacing):
        """
        :param direction: Box._horizontal \ Box._vertical
        :param QWidget_parent: QWidget
        :param margin: поле вокруг
        :param spacing: интервал (шаг) между виджетами
        """
        super().__init__(direction, parent)
        self.setDirection(direction)
        self.setContentsMargins(*margin)
        self.setSpacing(spacing)

    def addWidget(self, QWidget, stretch=0, Qt_Alignment=None,
                  Qt_AlignmentFlag=None, *args, **kwargs):
        if self.direction() == Box.horizontal:
            super().addWidget(QWidget, alignment=QtCore.Qt.AlignLeft)
        elif self.direction() == Box.vertical:
            super().addWidget(QWidget,
                              alignment=QtCore.Qt.AlignCenter |
                                        QtCore.Qt.AlignTop)



class AddUserBtn(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()


class Users(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)


class UserProfile(QtWidgets.QFrame):
    def __init__(self, users: list):
        super().__init__()

        self.icon_size = QtCore.QSize(20, 20)
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)
        self.users = Users()
        self.box.addWidget(self.users, stretch=1)
        self.users.addItems(users)

        self.add_user_btn = AddUserBtn()
        self.add_user_btn.setObjectName("adduser")
        self.add_user_btn.setIcon(
            QtGui.QIcon("../resource/icons/useradd.png"))
        self.add_user_btn.setIconSize(self.icon_size)

        self.del_user_btn = AddUserBtn()
        self.del_user_btn.setObjectName("del_user_btn")
        self.del_user_btn.setIcon(
            QtGui.QIcon("../resource/icons/del_user.png"))
        self.del_user_btn.setIconSize(self.icon_size)

        self.box.addWidget(self.add_user_btn)
        self.box.addWidget(self.del_user_btn)

    @property
    def current_user(self):
        return self.users.currentText()

    def del_current_user(self):
        self.users.removeItem(self.users.currentIndex())

    def add_user(self, user):
        self.users.addItem(user)


class AddressLabel(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()


class Editor(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()


class ThemeEditor(QtWidgets.QTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)

    def add_error_mess(self, text=""):
        if text:
            text = "тема не соответствует имени файла"
            lb = QtWidgets.QLabel()
            lb.setObjectName('error_path_theme_label')
            lb.setText(text)
            self.box.addWidget(lb,
                               alignment=QtCore.Qt.AlignBottom
                                         | QtCore.Qt.AlignCenter)


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
        self.del_file.setIcon(
            QtGui.QIcon("../resource/icons/del_file.png"))
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
