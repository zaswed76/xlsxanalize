import os
import sys
from PyQt5 import QtCore

from PyQt5 import QtWidgets

from scr.text import mess
from xlsxanalize.scr.gui import tool

class Editor(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()

class ThemeEditor(QtWidgets.QLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setTextMargins(15, 0, 0, 0)



class MainEditor(QtWidgets.QMainWindow):
    def __init__(self, editor, theme_editor):
        super().__init__()
        self.theme_editor = theme_editor
        self.central_widget = QtWidgets.QFrame()
        self.setCentralWidget(self.central_widget)
        self.editor = editor
        self.resize(600, 500)
        box = QtWidgets.QVBoxLayout(self.central_widget)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(0)

        box.addWidget(self.theme_editor)
        box.addWidget(self.editor)

    def set_tool(self, tool):
        self.tool = tool
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.tool)



if __name__ == '__main__':
    from xlsxanalize.scr.text import mess, xlsx_data
    from xlsxanalize.scr.pars import xlsx_parser

    xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
                      'bar_income', 'change_money', 'change_money_expenses',
                      'expenses_mess', 'salary_mess', 'total_in_safe',
                      'total_income', 'z_report', "theme"]

    DATA_DIR = "../data"
    file_name = 'калькулятор бара отчет.xlsx'
    file_path = os.path.join(DATA_DIR, file_name)

    report_path_name = "12.07-13.07.2017 (сутки) отчет Бар лесной .xlsx"
    bar_report_path = os.path.join(DATA_DIR, report_path_name)

    parser = xlsx_parser.Parser(file_path, bar_report_path)
    xlsxData = xlsx_data.XlxsDada(parser)
    ms = mess.Message("./", "mess.html", xlsxData)
    ms.register_xlsx_data(*xlsx_data_list)
    ms_text = ms.text()
    theme = ms.theme()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../style/css/base.css', "r").read())
    theme_editor = ThemeEditor()
    theme_editor.setText(theme)
    editor = Editor()
    main = MainEditor(editor, theme_editor)
    tool_bar = tool.Tool()
    main.set_tool(tool_bar)
    editor.setHtml(ms_text)
    main.show()
    sys.exit(app.exec_())
