

from xlsxanalize.scr import mess

xlsx_data = ['add_income_mess', 'admin_income', 'all_expenses',
             'bar_income', 'change_money', 'change_money_expenses',
             'expenses_mess', 'salary_mess', 'total_in_safe',
             'total_income', 'z_report']

message =  mess.Message()
message.register_xlsx_data(*xlsx_data)