
import os

from scr.pars import data_pars


def report(directory):
    os.path.isdir(directory)
    file_lst = []
    dp_file_lst = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            dp = data_pars.Date_Pars()
            fullname = os.path.join(root, name)
            dp.data_pars(fullname)
            dp_file_lst.append(dp)
            file_lst.append((os.path.getctime(fullname), fullname))
    try:
        file = max(file_lst)[1]
    except ValueError:
        file = ""

    try:
        s = max(dp_file_lst)
    except:
        return None
    else:
        return s.line

import os
import shutil
import tempfile



def open_file(source):
    ext = os.path.splitext(source)[1]
    temp_xlsx = tempfile.mkstemp()[1] + ext
    shutil.copy2(source, temp_xlsx)
    os.startfile(temp_xlsx)


if __name__ == '__main__':
    print(report(r"C:\Users\Cassa\Desktop\Отчёты"))