
import os


def report(directory):
    file_lst = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            fullname = os.path.join(root, name)
            file_lst.append((os.path.getctime(fullname), fullname))
    return max(file_lst)[1]
if __name__ == '__main__':
    print(report(r"C:\Users\Cassa\Desktop\Отчёты"))