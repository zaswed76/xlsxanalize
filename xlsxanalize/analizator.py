# -*- coding: utf-8 -*-

import os
from openpyxl import load_workbook


def list_paths(direct):
    return [os.path.join(direct, x) for x in os.listdir(direct)]

def read_dir(dir):
    months = []
    for root, dirs, files in os.walk(
            dir):  # пройти по директории рекурсивно
        for name in files:
            fullname = os.path.join(root,
                                    name)  # получаем полное имя файла
            if dirs:
                months.extend(dirs)
    return months

            # os.path.getctime(fullname)  # делаем что-нибудь с ним

if __name__ == '__main__':
    m = read_dir(r'E:\SERG\programming\xlsxa\xlsxanalize\xlsxanalize\data\Отчёты по Принтеру')
    print(m[0])