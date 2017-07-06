

from xlsxanalize.scr import mess, mailpy

xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
             'bar_income', 'change_money', 'change_money_expenses',
             'expenses_mess', 'salary_mess', 'total_in_safe',
             'total_income', 'z_report']

mymail = "zaswed76@gmail.com"
tomail = "sergitland@gmail.com"
subj = "тема"

ms =  mess.Message("../templates", "mess.html")
ms.register_xlsx_data(*xlsx_data_list)
ms_text = ms.text()
psw = "5422717fasad"

mailpy.run_mail(mymail, [tomail], subj, ms_text, psw)