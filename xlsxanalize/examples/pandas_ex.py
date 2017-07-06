

import os
import pandas as pd
from xlsxanalize.examples import tab_cfg

DATA_DIR = "../data"

# Assign spreadsheet filename to `file`
file_name = 'калькулятор бара отчет.xlsx'
# file_name = 'test_pd.xlsx'
file_path = os.path.join(DATA_DIR, file_name)

# Load spreadsheet
xl = pd.ExcelFile(file_path)

# Print the sheet names
# print(xl.sheet_names[0])

sheet_1 = xl.sheet_names[0]
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse(sheet_1)

# expense_name = df1.keys()[2]
#
def data_tabs(key, value):
    expense_names = [x for x in df1[key].values if not pd.isnull(x)]
    expense_values = [x for x in df1[value].values if not pd.isnull(x)]
    return expense_names, expense_values

def check_sum(data):
    return sum(data[0:-1]) == data[-1]

print(data_tabs("имя прихода", "Приход"))
incoming = data_tabs("имя прихода", "Приход")
print(check_sum(incoming[1]))





