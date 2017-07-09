
import os
import pandas as pd

class Parser:
    d = {
        "Z отчет": ("Приход", 1),
        "Бар": ("Приход", 0),
        "Доп. Доход": ("Приход", 2),
        "Печать": ("Приход", 3),
        "Разменка": ("Приход", 7)
    }
    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path
        else: raise FileNotFoundError("файл не найден")


        self.xl = pd.ExcelFile(file_path)
        self.sheet_1 = self.xl.sheet_names[0]
        self.df1 = self.xl.parse(self.sheet_1)


    def __call__(self, name):
        coll = self.d[name][0]
        line = self.d[name][1]
        return self.df1[coll][line]




if __name__ == '__main__':
    DATA_DIR = "../data"
    file_name = 'калькулятор бара отчет.xlsx'
    file_path = os.path.join(DATA_DIR, file_name)
    pars = Parser(file_path)
    print(pars("Разменка"))

