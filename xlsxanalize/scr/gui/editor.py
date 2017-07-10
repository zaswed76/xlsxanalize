import os
import sys
from PyQt5 import QtWidgets

from scr.text import mess


class Widget(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)


if __name__ == '__main__':
    from xlsxanalize.scr.text import mess, xlsx_data
    from xlsxanalize.scr.pars import xlsx_parser

    xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
                      'bar_income', 'change_money', 'change_money_expenses',
                      'expenses_mess', 'salary_mess', 'total_in_safe',
                      'total_income', 'z_report']

    DATA_DIR = "../data"
    file_name = 'калькулятор бара отчет.xlsx'
    file_path = os.path.join(DATA_DIR, file_name)

    parser = xlsx_parser.Parser(file_path)
    xlsxData = xlsx_data.XlxsDada(parser)
    ms = mess.Message("./", "mess.html", xlsxData)
    ms.register_xlsx_data(*xlsx_data_list)
    ms_text = ms.text()
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Widget()
    main.setHtml(ms_text)
    main.show()
    sys.exit(app.exec_())