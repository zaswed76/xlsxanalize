

import sys
from PyQt5 import QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout(self)
        self.lab = QtWidgets.QPushButton()
        self.box.addWidget(self.lab)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    main.lab.setText("self.del_filezergaergergaewrgta123456789")
    sys.exit(app.exec_())