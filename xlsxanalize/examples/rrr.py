import datetime
import re


class Date:
    def __init__(self, date=None):
        self._valid = None
        self.line = date
        try:
            self.date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
            self._valid = True
        except ValueError:
            self._valid = False
            self.date = None

    @property
    def valid(self):
        return self._valid

    def __str__(self):
        return str(self.date)

    def date_form(self, d, f):
        return


class Date_Pars:
    PAT_DATA = re.compile("\d{2}[-./,]\d{2}[-./,]\d{2,4}")
    PAT_TIME = re.compile("[\[(]\d{1,2}[)\]]|[\[(]\w+[)\]]")
    PAT_TIME_WORD = re.compile("\d{1,2}|\w+")
    DATA_DEL_PAT = "[-./,]"
    PAT_FORMAT_DATA = "%d.%m.%Y"

    def __init__(self):
        self.begin = None
        self.end = None
        self.time = None

    @staticmethod
    def del_space(line):
        return "".join(line.split())

    def data_pars(self, line):
        line = Date_Pars.del_space(line)
        res_data = re.findall(Date_Pars.PAT_DATA, line)
        if not res_data:
            return dict()
        else:
            res_data = [re.sub(Date_Pars.DATA_DEL_PAT, ".", d) for d in res_data]
            self.begin, self.end = (Date(res_data[0]), Date(res_data[1]))
            res_time = re.findall(Date_Pars.PAT_TIME, line)
            if res_time:
                self.time = re.findall(Date_Pars.PAT_TIME_WORD, res_time[0])[0]

    @staticmethod
    def valid_date(data_lst):
        r = []
        for d in data_lst:
            print(d)
            try:
                d = datetime.datetime.strptime(d,
                                               Date_Pars.PAT_FORMAT_DATA)
            except ValueError:
                r.append((d, False))
            else:
                r.append((d, True))
        return r


if __name__ == '__main__':
    s = "19.07.2017-30.07.2017  (24)"
    pd = Date_Pars()
    pd.data_pars(s)
    d = pd.end.date - pd.begin.date
    now = datetime.datetime.now()
    print(d == datetime.timedelta(days=1))
    print(now.date() == pd.begin.date)
    print(now.date() - pd.begin.date)






# d = datetime.datetime.strptime(data_lst[0], "%d.%m.%Y")
# print(d)
# print(datetime.datetime.strftime(d, "%d.%m.%Y"))
