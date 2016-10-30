#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


line = '_31.12(18.00)-02.01.2016(09.00)'

pat = re.compile(r'\D')

print()

def pars_line(line, pat):
    """

    :param line: str
    :param pat: re
    :return: [date, month, date, month, year, time]
    """
    result = re.split(pat, line)
    return [x for x in result if x]


# day_month, month, _, _, year, time = pars_line(line, pat)
print(pars_line(line, pat))
# print(day_month, month, year, time)
