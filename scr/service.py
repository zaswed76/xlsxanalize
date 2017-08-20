
import os

from scr.pars import data_pars


def report(directory):
    file_lst = []
    dp_file_lst = []
    for root, dirs, files in os.walk(directory):

        for name in files:

            dp = data_pars.Date_Pars()
            fullname = os.path.join(root, name)
            print(fullname)
            if os.path.splitext(name)[1] == ".xlsx":
                dp.data_pars(fullname)


                dp_file_lst.append(dp)
                file_lst.append((os.path.getctime(fullname), fullname))

    try:

        s = max(dp_file_lst)


    except:

        pass
    else:
        l = s.source_line


        return l

import os
import shutil
import tempfile



def open_file(source):
    ext = os.path.splitext(source)[1]
    temp_xlsx = tempfile.mkstemp()[1] + ext
    shutil.copy2(source, temp_xlsx)
    os.startfile(temp_xlsx)


a = "C:/Users/Cassa/Desktop/Отчёты/Август\01.08-02.08.2017 (сутки) отчет Бар лесной.xlsx"

b = "C:/Users/Cassa/Desktop/Serg/project/xlsxanalize/scr/data/reports\28.07.17-29.07.17 (сутки) отчет Бар лесной.xlsx"

if __name__ == '__main__':
    print(report(r"C:\Users\Cassa\Desktop\Отчёты"))