
import os
from openpyxl import load_workbook
from openpyxl import Workbook

xls_dir = '../data'
file = os.path.join(xls_dir, '01.10.16 - 02.10.2016 (24).xlsx')

print(os.path.isfile(file))
wb = load_workbook(file)
sheet = wb.active
print(sheet['C1'].value)
