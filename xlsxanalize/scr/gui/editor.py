import os
import sys

from functools import partial

import yaml
from PyQt5 import QtWidgets, uic, QtCore

from scr.text import mess
from xlsxanalize.scr.gui import widgets
from xlsxanalize.scr import service

actions_names = ["undo.png", "redo.png", "SPACER", "send2.png", "setting.png"]
ui_dir = "../gui/ui"
config_path = "../etc/config.yaml"


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
        self.cfg = yaml.load(open(config_path))
        self.cfg_copy = self.cfg.copy()
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
        self.set_widg.setWindowModality(QtCore.Qt.ApplicationModal)

        self.set_widg.set_close.clicked.connect(
            self.close_set)

        self.set_widg.set_ok.clicked.connect(
            self.ok_set)

        self.set_widg.report_dir_btn.clicked.connect(
            self.report_chooce_dir)

        self.set_widg.calc_file_btn.clicked.connect(
            self.calc_choos_file)

        self.set_widg.report_file.clicked.connect(
            self.report_file)

    def get_message(self, file_path, bar_report_path):
        if not file_path or not bar_report_path:
            return "", ""

        parser = xlsx_parser.Parser(file_path, bar_report_path)
        xlsxData = xlsx_data.XlxsDada(parser)
        ms = mess.Message("./", "mess.html", xlsxData)
        ms.register_xlsx_data(*xlsx_data_list)
        ms_text = ms.text()
        theme = ms.theme()
        return ms_text, theme

    def show_text(self):
        file_path = self.cfg["calc_file"]
        bar_report_path = service.report(self.cfg["reports_dir"])

        try:
            ms_text, theme = self.get_message(file_path, bar_report_path)
        except:
            ms_text, theme = ("none", "none")
        theme_editor.setText(str(theme))
        editor.setHtml(ms_text)


    def setting_set_conf(self):
        self.set_widg.calc_file_btn.setText(self.cfg["calc_file"])
        self.set_widg.report_dir_btn.setText(self.cfg["reports_dir"])

    def close_set(self):
        self.cfg_copy.update(self.cfg)
        self.set_widg.close()

    def ok_set(self):
        self.cfg.update(self.cfg_copy)
        self.save_conf(self.cfg)
        self.show_text()
        self.set_widg.close()

    def report_file(self):
        f = self.showDialog()
        if f:
            self.cfg_copy["report_file"] = f
            self.set_widg.report_file.setText(f)

    def report_chooce_dir(self):
        directory = self.choose_dir()
        if directory:
            self.cfg_copy["reports_dir"] = directory
            self.set_widg.report_dir_btn.setText(directory)


    def calc_choos_file(self):
        f = self.showDialog()
        if f:
            self.cfg_copy["calc_file"] = f
            self.set_widg.calc_file_btn.setText(f)

    def showDialog(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]

    def choose_dir(self):
        return str(QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory"))

    def undo(self):
        print("undo")

    def redo(self):
        print("redo")

    def send2(self):
        print("send")

    def setting(self):
        self.setting_set_conf()
        self.set_widg.show()

    def save_conf(self, cfg):
        with open(config_path, 'w') as f:
            yaml.dump(cfg, f, default_flow_style=False)





if __name__ == '__main__':
    from xlsxanalize.scr.text import mess, xlsx_data
    from xlsxanalize.scr.pars import xlsx_parser

    xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
                      'bar_income', 'change_money', 'change_money_expenses',
                      'expenses_mess', 'salary_mess', 'total_in_safe',
                      'total_income', 'z_report', "theme"]




    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../style/css/base.css', "r").read())
    theme_editor = ThemeEditor()

    editor = Editor()
    main = MainEditor(editor, theme_editor)


    main.show()
    main.show_text()
    sys.exit(app.exec_())
