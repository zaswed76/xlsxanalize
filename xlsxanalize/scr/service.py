
import os


def report(directory):
    file_lst = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            fullname = os.path.join(root, name)
            file_lst.append((os.path.getctime(fullname), fullname))
    try:
        file = max(file_lst)[1]
    except ValueError:
        file = ""
    print(file)
    return file

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