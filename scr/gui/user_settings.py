
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from scr.gui import widgets

INVALID_ADDRESS_STYLE = "border: 1px solid #ED2007"
VALID_ADDRESS_STYLE = "border: 1px solid #52E02D"

PWD_VERIFY_PAT = re.compile("^[^а-яё]+$")

ADDRESS_VERIFY_PAT = re.compile(
    """^[_a-z0-9-]+
           (\.[_a-z0-9-]+)*
           @
           [a-z0-9-]+
           (\.[a-z0-9-]+)*
           (\.[a-z]{2,4})$
       """, re.VERBOSE)

def pwd_verify(line):
    return re.match(PWD_VERIFY_PAT, line)

def address_verify(addr):
    return re.match(ADDRESS_VERIFY_PAT, addr)


class AddUserWindow(QtWidgets.QFrame):
    def __init__(self, pwd_us):
        super().__init__()
        self.pwd_us = pwd_us
        self.setWindowTitle("добавить нового пользователя")
        base_box = widgets.Box(widgets.Box.horizontal, self)
        box = widgets.Box(widgets.Box.vertical)
        base_box.addLayout(box)
        self.user_line = QtWidgets.QLineEdit()
        self.user_line.setStyleSheet(INVALID_ADDRESS_STYLE)
        self.user_line.setObjectName("new_user")
        self.user_line.setPlaceholderText("mail нового пользователя")
        self.user_line.textEdited.connect(
            self.mail_edit_verify)

        self.user_pasw = QtWidgets.QLineEdit()
        self.user_pasw.setStyleSheet(INVALID_ADDRESS_STYLE)
        self.user_pasw.setObjectName("new_user_pasw")
        self.user_pasw.setPlaceholderText("пароль от почтового ящика")
        self.user_pasw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_pasw.textEdited.connect(
            self.pwd_edit_verify)

        self.master = QtWidgets.QLineEdit()
        self.master.setObjectName("master")
        self.master.setPlaceholderText("мастер пароль")
        self.master.setEchoMode(QtWidgets.QLineEdit.Password)

        self.master_2 = QtWidgets.QLineEdit()
        self.master_2.setObjectName("master_2")
        self.master_2.setPlaceholderText("подтвердить мастер пароль")
        self.master_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.check_pwd = QtWidgets.QCheckBox("показывать пароль")
        self.check_pwd.setObjectName("check_pwd")
        self.check_pwd.stateChanged.connect(self.change_pwd_visible)

        self.save_user_btn = QtWidgets.QPushButton("сохранить")
        self.save_user_btn.clicked.connect(
            self.save_user)

        box.addWidget(self.user_line)
        box.addWidget(self.user_pasw)
        box.addWidget(self.master)
        box.addWidget(self.master_2)
        box.addWidget(self.check_pwd)
        base_box.addWidget(self.save_user_btn)

    def mail_edit_verify(self, line):
        if address_verify(line):
            self.user_line.setStyleSheet(VALID_ADDRESS_STYLE)
        else:
            self.user_line.setStyleSheet(INVALID_ADDRESS_STYLE)

    def pwd_edit_verify(self, line):
        if pwd_verify(line):
            self.user_pasw.setStyleSheet(VALID_ADDRESS_STYLE)
        else:
            self.user_pasw.setStyleSheet(INVALID_ADDRESS_STYLE)

    def save_user(self):
        mail_user = self.user_line.text()





    def change_pwd_visible(self, state):
        if state:
            self.user_pasw.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.master.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.master_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.user_pasw.setEchoMode(QtWidgets.QLineEdit.Password)
            self.master.setEchoMode(QtWidgets.QLineEdit.Password)
            self.master_2.setEchoMode(QtWidgets.QLineEdit.Password)