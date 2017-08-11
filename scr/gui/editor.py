import os
import sys

from functools import partial

import yaml
from PyQt5 import QtWidgets, uic, QtCore

from scr.mail import mailpy
from scr.gui import widgets
from scr import service
from scr.pars import xlsx_parser
from scr.text import xlsx_data, mess
import sys
from PyQt5 import QtWidgets
from scr.gui import widgets

actions_names = ["undo.png", "redo.png", "attach_file",
                 "SPACER", "send2.png", "show_setting_wind.png"]
ui_dir = "../gui/ui"
config_path = "../etc/config.yaml"

xlsx_data_list = ['add_income_mess', 'admin_income',
                  'all_expenses',
                  'bar_income', 'change_money',
                  'change_money_expenses',
                  'expenses_mess', 'salary_mess', 'total_in_safe',
                  'total_income', 'z_report']


class MainEditor(widgets.MainWidget):
    def __init__(self, editor, theme_editor):
        super().__init__()
        self.cfg = yaml.load(open(config_path))
        if self.cfg:
            self.cfg_copy = self.cfg.copy()
        else:
            self.cfg = dict()
            self.cfg_copy = self.cfg.copy()
        self.resize(450, 600)
        self.usr_profile = widgets.UserProfile(self.cfg_copy["users"])
        self.theme_editor = theme_editor
        self.editor = editor
        self.attach_widget = widgets.AttachWidget()

        self.load_style_sheet("base")
        self.tool = widgets.Tool(self, 26,
                                 self.tool_actions(actions_names))
        self.init_tool_bar(self.tool)

        self.center_box.addWidget(self.usr_profile)
        self.center_box.addWidget(self.theme_editor)
        self.center_box.addWidget(self.editor)
        self.center_box.addWidget(self.attach_widget)

        self.set_widg = uic.loadUi(
            os.path.join(ui_dir, "setting.ui"))
        self.set_widg.setWindowModality(QtCore.Qt.ApplicationModal)

        self.set_widg.set_close.clicked.connect(
            self.close_set)

        self.set_widg.set_ok.clicked.connect(
            self.ok_set)

        self.set_widg.report_dir_btn.clicked.connect(
            self.report_choose_dir)

        self.set_widg.calc_file_btn.clicked.connect(
            self.calc_choos_file)

        self.attach_objects = {}

    def get_message(self, file_path, bar_report_path):

        parser = xlsx_parser.Parser(file_path, bar_report_path)

        xlsxData = xlsx_data.XlxsDada(parser)

        ms = mess.Message("../text",
                          "mess.html",
                          "theme.html",
                          xlsxData)
        ms.register_xlsx_data(*xlsx_data_list)
        ms.create_theme_data()
        ms_text = ms.text()
        theme = ms.theme()
        path = parser.report_file
        return ms_text, theme, path, parser.error_theme_path

    def show_text(self):
        file_path = self.cfg["calc_file"]
        if not os.path.isfile(file_path):
            self.ms_text = "калькулятор бара отсутствует"
            self.editor.setHtml(self.ms_text)
            return
        bar_report_path = service.report(self.cfg["reports_dir"])
        if not os.path.isfile(bar_report_path):
            theme = "отчёт отсутствует"
            theme_editor.setText(theme)
            return

        self.ms_text, self.theme, path, error_theme_path = self.get_message(
            file_path, bar_report_path)

        self.theme_editor.setHtml(self.theme)
        self.theme_editor.add_error_mess(error_theme_path)
        self.editor.setHtml(self.ms_text)
        self.add_attach(path)

    def send2(self):
        # psw = "5422717fasad
        # mymail = "zaswed76@gmail.com"
        # tomail = "sergitland@gmail.com"
        # theme = self.theme_editor.toPlainText()
        # ms_text = self.editor.toHtml()
        # mailpy.run_mail(mymail, [tomail], theme, ms_text, psw)
        print("send")

    def add_attach(self, file):
        self.attach_objects[file] = self.attach_widget.add_file(file)
        self.attach_objects[file].clicked.connect(partial(
            self.press_attach, file))

    def press_attach(self, file):
        service.open_file(file)

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

    def report_choose_dir(self):
        directory = self.choose_dir()
        if directory:
            self.cfg_copy["reports_dir"] = directory
            self.set_widg.report_dir_btn.setText(directory)
            self.set_widg.report_file.setText(
                service.report(directory))

    def calc_choos_file(self):
        f = self.showDialog()
        if f:
            self.cfg_copy["calc_file"] = f
            self.set_widg.calc_file_btn.setText(f)

    def showDialog(self):
        return \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[
                0]

    def choose_dir(self):
        return str(QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory"))

    def undo(self):
        print("undo")

    def redo(self):
        print("redo")

    def show_setting_wind(self):
        self.setting_set_conf()
        print(555)
        self.set_widg.show()

    def setting_set_conf(self):

        self.set_widg.calc_file_btn.setText(self.cfg["calc_file"])

        self.set_widg.report_dir_btn.setText(self.cfg["reports_dir"])
        self.set_widg.report_file.setText(
            service.report(self.cfg["reports_dir"]))

    def save_conf(self, cfg):
        with open(config_path, 'w') as f:
            yaml.dump(cfg, f, default_flow_style=False)

    def attach_file(self):
        f = self.showDialog()
        if f:
            self.cfg_copy[f] = f
            btn = self.attach_widget.add_file(os.path.basename(f))
            btn.clicked.connect(partial(self.press_attach, f))


if __name__ == '__main__':



    xlsx_data_list = ['add_income_mess', 'admin_income',
                      'all_expenses',
                      'bar_income', 'change_money',
                      'change_money_expenses',
                      'expenses_mess', 'salary_mess', 'total_in_safe',
                      'total_income', 'z_report']

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../style/css/base.css', "r").read())
    theme_editor = widgets.ThemeEditor()
    editor = widgets.Editor()
    main = MainEditor(editor, theme_editor)

    main.show()
    main.show_text()
    sys.exit(app.exec_())
