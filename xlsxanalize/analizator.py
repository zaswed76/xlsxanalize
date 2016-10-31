# -*- coding: utf-8 -*-

import os
import re
from openpyxl import load_workbook

PATTERN = re.compile(r'\D')
EXT = '.xlsx'


class File:
    def __init__(self, pat, root='', name='', ext=''):
        self._date_parse_flag = True
        self.ext = ext
        self.name = name
        self.root = root
        self.full_path = os.path.join(self.root, self.name) + ext
        try:
            self.day_month, self.month, _, _, self.year, self.time = File.pars_line(
                self.name, pat)
        except ValueError:
            self.day_month, self.month, _, _, self.year, self.time = '?' * 6
            self._date_parse_flag = False

    def __repr__(self):
        return '{} - {}.{}.{}'.format(File.__name__, self.day_month, self.month, self.year)

    @property
    def date_parse_flag(self):
        return self._date_parse_flag

    @date_parse_flag.setter
    def date_parse_flag(self, flag):
        self._date_parse_flag = flag



    @staticmethod
    def pars_line(line, pat):
        """

        :param line: str
        :param pat: re
        :return: [date, month, date, month, year, time]
        """
        result = re.split(pat, line)
        return [x for x in result if x]


def get_files(dir, default_ext='.xlsx'):
    paths_dict = dict()
    for root, dirs, files in os.walk(dir):
        for name in files:
            name, ext = os.path.splitext(name)
            if ext == default_ext:
                paths_dict[name] = File(PATTERN, root, name, ext)
    return paths_dict


class XlsxFile:
    def __init__(self, file_object):
        self.file_object = file_object
        wb = load_workbook(self.file_object.full_path)
        sheet = wb.active
        print(sheet['D1'].value)



if __name__ == '__main__':
    files = get_files(
        r'D:\0SYNC\python_projects\xlsxanalize\xlsxanalize\data\Отчёты по Принтеру')
    d = {}
    for i in files.items():
        d[i[0]] = XlsxFile(i[1])
    print(len(d))





