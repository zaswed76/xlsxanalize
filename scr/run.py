
import sys
from PyQt5 import QtWidgets
from scr.gui import widgets
from scr.gui import editor as main_editor



xlsx_data_list = ['add_income_mess', 'admin_income',
                  'all_expenses',
                  'bar_income', 'change_money',
                  'change_money_expenses',
                  'expenses_mess', 'salary_mess', 'total_in_safe',
                  'total_income', 'z_report']

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(open('../scr/style/css/base.css', "r").read())
theme_editor = widgets.ThemeEditor()
editor = widgets.Editor()
main = main_editor.MainEditor(editor, theme_editor)

main.show()
main.show_text()
sys.exit(app.exec_())



