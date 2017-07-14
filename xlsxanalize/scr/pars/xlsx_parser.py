import os
import re

import pandas as pd


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
    SALARY_PAT = re.compile(r"аванс|зарплата", flags=re.IGNORECASE)

    def __init__(self, file_path, bar_report_path):

        if os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError("файл - \n{}\n не найден".format(file_path))

        if os.path.isfile(bar_report_path):
            self.bar_report_path = bar_report_path
        else:
            self.bar_report_path = ""
            raise FileNotFoundError(
                "файл - \n{}\n не найден".format(bar_report_path))

        self.df1 = self.load_file(self.file_path)
        print("--------------------------------")
        print(self.df1)

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

    def theme(self):
        return self.report_df.iloc[0][1]

    def _theme_test(self):
        return self.report_df.iloc[0][1]


if __name__ == '__main__':
    DATA_DIR = "../data"
    file_name = 'калькулятор бара отчет.xlsx'
    file_path = os.path.join(DATA_DIR, file_name)

    report_path_name = "12.07-13.07.2017 (сутки) отчет Бар лесной .xlsx"
    bar_report_path = os.path.join(DATA_DIR, report_path_name)

    pars = Parser(file_path, bar_report_path)
    print(pars._theme_test())
