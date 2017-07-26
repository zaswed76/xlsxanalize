
import os
import shutil
import tempfile



def open_file(source):
    temp_xlsx = tempfile.mkstemp()[1] + ".xlsx"
    shutil.copy2(source, temp_xlsx)
    os.startfile(temp_xlsx)

