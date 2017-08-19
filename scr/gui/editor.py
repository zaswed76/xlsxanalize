import os
import sys

from functools import partial

import yaml
from PyQt5 import QtWidgets, uic, QtCore

from scr.mail import mailpy, pwd

from scr import service
from scr.pars import xlsx_parser
from scr.text import xlsx_data, mess
import sys
from PyQt5 import QtWidgets
from scr.gui import widgets, user_settings, recipients

actions_names = ["undo.png", "redo.png", "attach_file",
                 "SPACER", "send2.png", "show_setting_wind.png"]
ui_dir = "../gui/ui"
config_path = "../etc/config.yaml"
pwd_path = "../etc/pwd.pkl"

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
        self.data_pwd = pwd.Pwd.load(pwd_path)
        if self.data_pwd is None:
            users = []
        else:
            users = list(self.data_pwd.keys())

        self.usr_profile = widgets.UserProfile(users)
        self.recipients = recipients.Recipients(self)

        self.theme_editor = theme_editor
        self.theme_editor.setMinimumHeight(60)
        self.editor = editor
        self.attach_widget = widgets.AttachWidget()

        self.load_style_sheet("base")
        self.tool = widgets.Tool(self, 26,
                                 self.tool_actions(actions_names))
        self.init_tool_bar(self.tool)

        self.center_box.addWidget(self.usr_profile, stretch=0)
        self.center_box.addWidget(self.recipients, stretch=0)
        self.center_box.addWidget(self.theme_editor, stretch=4)
        self.center_box.addWidget(self.editor, stretch=21)
        self.center_box.addWidget(self.attach_widget, stretch=1)

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

        self.usr_profile.add_user_btn.clicked.connect(
            self.add_user)

        self.usr_profile.del_user_btn.clicked.connect(
            self.del_user)

        self.attach_objects = {}



    def del_user(self):
        current_user = self.usr_profile.current_user
        if current_user:
            del(self.data_pwd[self.usr_profile.current_user])
            self.usr_profile.del_current_user()
            pwd.Pwd.update(pwd_path, self.data_pwd)
            print("del_user")

    def add_user(self):
        rect_base_w = self.geometry()
        self.add_user_window = user_settings.AddUserWindow()
        self.add_user_window.save_user_btn.clicked.connect(
            self.save_user)
        self.add_user_window.setWindowModality(
            QtCore.Qt.ApplicationModal)
        self.add_user_window.move(rect_base_w.left(), rect_base_w.top())
        self.add_user_window.setMinimumWidth(rect_base_w.width()-8)
        self.add_user_window.show()

    def save_user(self):
        pwd_us = pwd.Pwd()
        valid = self.add_user_window.all_valid_flags()
        if valid:
            mail = self.add_user_window.user_line.text()
            password = self.add_user_window.user_pasw.text()
            master = self.add_user_window.master.text()
            encode_data = pwd_us.encrypt(password, master)
            pwd_us.save(mail, pwd_path, encode_data)
            self.data_pwd.update({mail: encode_data})
            self.usr_profile.add_user(mail)
            self.add_user_window.close()
            print("сохранено")


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
        if not bar_report_path:
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
        user = self.usr_profile.current_user
        print("current", user)
        user_pwd_data = self.data_pwd[user]


        dialog = QtWidgets.QInputDialog(self)

        result = dialog.exec()
        if result == QtWidgets.QDialog.Accepted:
            master = dialog.textValue()
            decode_pwd_data = pwd.Pwd.decrypt(user_pwd_data, master)
        else:
            return
        print(decode_pwd_data)

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

            text = service.report(directory)
            self.set_widg.report_file.setText(text)


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
        self.set_widg.show()

    def setting_set_conf(self):
        self.set_widg.calc_file_btn.setText(self.cfg["calc_file"])
        self.set_widg.report_dir_btn.setText(self.cfg["reports_dir"])
        text = service.report(self.cfg["reports_dir"])
        self.set_widg.report_file.setText(text)

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

