import sys
from PyQt5 import QtWidgets

from xlsxanalize.scr.gui import widgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = widgets.Recipients()
    main.show()
    sys.exit(app.exec_())