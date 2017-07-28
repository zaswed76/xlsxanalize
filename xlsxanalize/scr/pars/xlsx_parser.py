import os
import re

import pandas as pd

from scr.pars import data_pars


# todo дата не совпадает с темой

def path_to_theme(pth):
    base = os.path.splitext(os.path.basename(pth))[0]
    return base


class Parser:
    Z_REPORT = ("Приход", 1)
    BAR_INCOME = ("Приход", 0)
    ADD_INCOME_MESS = ("Приход", 2)
    ADMIN_INCOME = ("Приход", 3)
    CHANGE_MONEY = ("Приход", 7)
    CHANGE_MONEY_EXPENSES = ("Расход", 7)
    TOTAL_INCOME = ("Приход", 8)
    ALL_EXPENSES = ("Расход", 8)
    TOTAL_IN_SAFE = ("имя расхода", 8)
    THEME = (0, 1)

    fields = {
        "z_report": Z_REPORT,
        "bar_income": BAR_INCOME,
        "add_income_mess": ADD_INCOME_MESS,
        "admin_income": ADMIN_INCOME,
        "change_money": CHANGE_MONEY,
        "total_income": TOTAL_INCOME,
        "change_money_expenses": CHANGE_MONEY_EXPENSES,
        "all_expenses": ALL_EXPENSES,
        "total_in_safe": TOTAL_IN_SAFE

    }
    SALARY_PAT = re.compile(r"аванс|зарплата|зп.",
                            flags=re.IGNORECASE)

    def __init__(self, file_path, bar_report_path):
        if os.path.isfile(file_path):
            self._file_path = file_path
        else:
            raise FileNotFoundError(
                "файл - \n{}\n не найден".format(file_path))

        if os.path.isfile(bar_report_path):
            self.bar_report_path = bar_report_path
        else:
            self.bar_report_path = ""
            raise FileNotFoundError(
                "файл - \n{}\n не найден".format(bar_report_path))

        self.df1 = self.load_file(self.file_path)

        self.report_df = self.load_file(self.bar_report_path)

    def load_file(self, file):
        try:
            self.xl = pd.ExcelFile(file)
        except FileNotFoundError:
            return None
        self.sheet_1 = self.xl.sheet_names[0]
        return self.xl.parse(self.sheet_1)

    def by_name(self, name):
        return self.df1[name[0]][name[1]]

    def expense(self) -> dict:
        """
        :rtype: dict < list
        """
        lst = []
        salary_lst = []
        for n, name in enumerate(self.df1["имя расхода"].values):
            if n > 6:
                break
            if not pd.isnull(name):
                if re.search(Parser.SALARY_PAT, name) is not None:
                    salary_lst.append((name, self.df1["Расход"][n]))
                else:
                    lst.append((name, self.df1["Расход"][n]))
        return {"expense": lst, "salary": salary_lst}

    def parse(self, line):
        dp = data_pars.Date_Pars()
        dp.data_pars(line)
        return dp

    def theme(self):
        path_line = path_to_theme(self.bar_report_path)
        report_parser = self.parse(path_line)

        d = dict()
        theme = self.report_df.iloc[self.THEME[0]][self.THEME[1]]
        theme_parser = self.parse(theme)
        d["begin_date"] = theme_parser.begin.text
        d["end_date"] = theme_parser.end.text
        d["time"] = theme_parser.time

        if theme_parser. \
                dates_valid_flag:
            d["begin_valid"] = theme_parser.begin.valid
            d["end_valid"] = theme_parser.end.valid
        else:
            d["begin_valid"] = False
            d["end_valid"] = False
        d["time_valid"] = True
        d["valid_report_theme"] = report_parser == theme_parser
        return d

    @property
    def file_path(self):
        return self._file_path

    @property
    def report_file(self):
        return self.bar_report_path



if __name__ == '__main__':
    pass
    # DATA_DIR = "../data"
    # file_name = 'калькулятор бара отчет.xlsx'
    # file_path = os.path.join(DATA_DIR, file_name)
    #
    # report_path_name = "12.07-13.07.2017 (сутки) отчет Бар лесной .xlsx"
    # bar_report_path = os.path.join(DATA_DIR, report_path_name)
    #
    # pars = Parser(file_path, bar_report_path)
    # pars.theme()
    #
    # s = r"C:\Users\Cassa\Desktop\Serg\project\xlsxanalize\xlsxanalize\scr\data\reports"
