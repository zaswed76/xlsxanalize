import os
import sys

from functools import partial
from PyQt5 import QtWidgets, uic, QtCore

actions_names = ["undo.png", "redo.png", "SPACER", "setting.png"]
from scr.text import mess
from xlsxanalize.scr.gui import widgets

ui_dir = "../gui/ui"


class Editor(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()


class ThemeEditor(QtWidgets.QLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setTextMargins(15, 0, 0, 0)


class MainEditor(widgets.MainWidget):
    def __init__(self, editor, theme_editor):
        super().__init__()
        self.resize(400, 600)
        self.theme_editor = theme_editor
        self.editor = editor

        self.load_style_sheet("base")
        self.tool = widgets.Tool(self, 26, self.tool_actions(actions_names))
        self.init_tool_bar(self.tool)

        self.center_box.addWidget(self.theme_editor)
        self.center_box.addWidget(self.editor)

        self.set_widg = uic.loadUi(
            os.path.join(ui_dir, "setting.ui"))

        self.set_widg.report_dir_btn.clicked.connect(
            self.report_chooce_dir)

        self.set_widg.calc_file_btn.clicked.connect(
            self.calc_choos_file)

    def report_chooce_dir(self):
        directory = self.choose_dir()

    def calc_choos_file(self):
        f = self.showDialog()

    def showDialog(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]

    def choose_dir(self):
        return str(QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory"))



    def undo(self):
        print("undo")

    def redo(self):
        print("redo")

    def setting(self):
        self.set_widg.show()




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

    editor.setHtml(ms_text)
    main.show()
    sys.exit(app.exec_())
