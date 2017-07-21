import os

from jinja2 import Environment, FileSystemLoader
from xlsxanalize.scr.text import xlsx_data



class Message:
    def __init__(self, templates_dir, template_file,
                 template_file_theme, xlsxdata):
        self.xlsxdata = xlsxdata
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.template = self.env.get_template(template_file)

        self.env_theme = Environment(loader=FileSystemLoader(templates_dir))
        self.template_theme = self.env.get_template(template_file_theme)
        # print(self.template_theme)

        self.xlsx_data = dict()
        self.theme_data = dict()
        self._theme = None

    def register_xlsx_data(self, *data_meth):
        for line in data_meth:
            mess = getattr(self.xlsxdata, line)()
            self.xlsx_data[line] = mess

    def create_theme_data(self):
        self.theme_data = self.xlsxdata.theme()

    def text(self):
        return self.template.render(self.xlsx_data)

    def theme(self):
        return self.template_theme.render(self.theme_data)


if __name__ == '__main__':
    pass
    #
    # from xlsxanalize.scr.pars import xlsx_parser
    # xlsx_data_list = ['add_income_mess', 'admin_income', 'all_expenses',
    #          'bar_income', 'change_money', 'change_money_expenses',
    #          'expenses_mess', 'salary_mess', 'total_in_safe',
    #          'total_income', 'z_report']
    #
    # DATA_DIR = "../data"
    # file_name = 'калькулятор бара отчет.xlsx'
    # file_path = os.path.join(DATA_DIR, file_name)
    #
    # report_file = r"C:\Users\Cassa\Desktop\Serg\project\xlsxanalize\xlsxanalize\scr\data\reports\12.07-13.07.2017 (сутки) отчет Бар лесной .xlsx"
    #
    # parser = xlsx_parser.Parser(file_path, report_file)
    #
    # xlsxData = xlsx_data.XlxsDada(parser)
    # ms = Message("../text", "mess.html", "theme.html", xlsxData)
    # ms.register_xlsx_data(*xlsx_data_list)
    # print(ms.theme())

