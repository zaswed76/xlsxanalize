import os
from PyQt5 import QtWidgets, QtCore, QtGui, uic

from scr.gui.widgets import Box

ui_dir = "../gui/ui"

class RecipientLabel(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setScaledContents(True)
        self.setFixedHeight(25)


class RecipientBox(QtWidgets.QGridLayout):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setSpacing(4)
        self.setContentsMargins(0, 0, 0, 0)


class Recipients(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        #

        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.scrol_area = QtWidgets.QScrollArea(self)
        self.scrol_area.setMinimumHeight(40)
        self.box.addWidget(self.scrol_area)

        self.parent = parent
        self.users= {}
        self.fr = QtWidgets.QFrame()

        self.rec_box = QtWidgets.QGridLayout(self.fr)
        self.rec_box.setSpacing(2)
        self.rec_box.setContentsMargins(1, 1, 1, 1)

        r1 = RecipientLabel("zaswed76@gmail.com")
        self.rec_box.addWidget(r1, 0, 0)

        r2 = RecipientLabel("zaswed@ukr.net")
        self.rec_box.addWidget(r2, 0, 1)

        r3 = RecipientLabel("qwerty@bigmir.com")
        self.rec_box.addWidget(r3, 0, 2)

        r3 = RecipientLabel("serg@mail.ru")
        self.rec_box.addWidget(r3, 1, 0)

        self.rec_box.addWidget(self.recipient_btn(), 1, 1, alignment=QtCore.Qt.AlignLeft)


        self.scrol_area.setWidget(self.fr)

    def recipient_btn(self):
        add_recipient_btn = QtWidgets.QPushButton()
        add_recipient_btn.clicked.connect(self.add_user)
        add_recipient_btn.setObjectName("add_recipient_btn")
        add_recipient_btn.setIcon(
            QtGui.QIcon("../resource/icons/recipient_btn.png"))
        add_recipient_btn.setIconSize(QtCore.QSize(20, 20))
        return add_recipient_btn

    def add_user(self, user):
        rect_base_w = self.parent.geometry()
        self.recipients_edit = uic.loadUi(
            os.path.join(ui_dir, "recipients.ui"))
        self.recipients_edit.accept.clicked.connect(
            self.accept)
        self.recipients_edit.setWindowModality(
            QtCore.Qt.ApplicationModal)
        self.recipients_edit.move(rect_base_w.left(), rect_base_w.top())
        self.recipients_edit.setMinimumWidth(rect_base_w.width()-10)
        self.recipients_edit.show()

    def accept(self):
        print("accept")
        self.recipients_edit.close()