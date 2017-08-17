import os
from PyQt5 import QtWidgets, QtCore, uic

from scr.gui.widgets import Box

ui_dir = "../gui/ui"


class Recipients(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.users= {}
        self.box = Box(Box.horizontal, self)
        self.recipients_box = Box(Box.horizontal)
        self.box.addLayout(self.recipients_box)
        self.add_rec = QtWidgets.QPushButton("+")
        self.add_rec.clicked.connect(self.add_user)
        self.box.addWidget(self.add_rec)


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