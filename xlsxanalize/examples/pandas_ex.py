

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

# print(df1.keys())
for k, v in df1["Приход"].items():
    if not pd.isnull(v):
        print(k, v, sep=" = ")
