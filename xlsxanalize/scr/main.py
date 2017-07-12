import os

from xlsxanalize.scr.text import mess, xlsx_data
from xlsxanalize.scr.pars import xlsx_parser
from xlsxanalize.scr import mailpy

xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
             'bar_income', 'change_money', 'change_money_expenses',
             'expenses_mess', 'salary_mess', 'total_in_safe',
             'total_income', 'z_report']

mymail = "zaswed76@gmail.com"
tomail = "sergitland@gmail.com"
subj = "тема"

DATA_DIR = "./data"
file_name = 'калькулятор бара отчет.xlsx'
file_path = os.path.join(DATA_DIR, file_name)

report_path_name = "12.07-13.07.2017 (сутки) отчет Бар лесной .xlsx"
bar_report_path = os.path.join(DATA_DIR, report_path_name)

parser = xlsx_parser.Parser(file_path, bar_report_path)
xlsxData = xlsx_data.XlxsDada(parser)

ms =  mess.Message("./text", "mess.html", xlsxData)
ms.register_xlsx_data(*xlsx_data_list)
ms_text = ms.text()
theme = ms.theme()

psw = "5422717fasad"

mailpy.run_mail(mymail, [tomail], theme, ms_text, psw)