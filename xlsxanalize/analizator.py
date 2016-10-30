# -*- coding: utf-8 -*-

import os
import re
from openpyxl import load_workbook

PATTERN = re.compile(r'\D')
EXT = '.xlsx'


class File:
    def __init__(self, root='', name='', ext='', pat=''):
        self._date_parse_flag = True
        # self.ext = ext
        self.name = name
        self.root = root
        self.fullname = os.path.join(self.root, self.name)
        try:
            self.day_month, self.month, _, _, self.year, self.time = File.pars_line(
                self.name, pat)
        except ValueError:
            self.day_month, self.month, _, _, self.year, self.time = '?' * 6
            self._date_parse_flag = False

    def __repr__(self):
        return self.name

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


def read_dir(dir, default_ext='.xlsx'):
    path_lst = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            name, ext = os.path.splitext(name)
            if ext == default_ext:
                path_lst.append(File(root, name, ext, PATTERN))
    return path_lst


if __name__ == '__main__':
    # m = read_dir(
    #     r'D:\0SYNC\python_projects\xlsxanalize\xlsxanalize\data\Отчёты по Принтеру')
    # print(m[0].name)
    # print(m[0].day_month)
    # print(m[0].year)
    # print(m[0].time)
    # print(m[0].date_parse_flag)
    p = File(ext=EXT, name='30.01-31.01.2016(24).xlsx', pat=PATTERN)
    print(p.name)
    print(p.fullname)
    print(p.day_month)
    print(p.date_parse_flag)
