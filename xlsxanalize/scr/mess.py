
from jinja2 import Environment, FileSystemLoader
from xlsxanalize.scr import xlsx_data



class Message:
    def __init__(self, templates_dir, template_file):
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.template = self.env.get_template(template_file)
        self.xlsx_data = dict()

    def register_xlsx_data(self, *data_meth):
        for line in data_meth:
            mess = getattr(xlsx_data, line)()
            self.xlsx_data[line] = mess

    def text(self):
        return self.template.render(self.xlsx_data)

if __name__ == '__main__':
    xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
             'bar_income', 'change_money', 'change_money_expenses',
             'expenses_mess', 'salary_mess', 'total_in_safe',
             'total_income', 'z_report']

    ms = Message("../templates", "mess.html")
    ms.register_xlsx_data(*xlsx_data_list)
    print(ms.text())

