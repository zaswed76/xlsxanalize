import datetime
import re

PAT_DATA = re.compile("\d{2}[-./,]\d{2}[-./,]\d{2,4}")
PAT_TIME = re.compile("[\[(]\d{1,2}[)\]]|[\[(]\w+[)\]]")

class Date_Pars:


    def __init__(self):
        pass


    @staticmethod
    def del_space(line):
        return "".join(line.split())

    @staticmethod
    def data_pars(line):
        line = Date_Pars.del_space(line)

        res_data = re.findall(PAT_DATA, line)
        if not res_data:
            return []
        else:
            res_data = [re.sub("[-./,]", ".", d) for d in res_data]
            res_time = re.findall(PAT_TIME, line)
            if res_time:
                res_data.append(res_time[0])
            return res_data
    @staticmethod
    def valid_date(data_lst):
        pass


if __name__ == '__main__':
    s = "19.07.2017-20.07.2017 (24)"
    pd = Date_Pars()
    print(pd.data_pars(s))






# d = datetime.datetime.strptime(data_lst[0], "%d.%m.%Y")
# print(d)
# print(datetime.datetime.strftime(d, "%d.%m.%Y"))

