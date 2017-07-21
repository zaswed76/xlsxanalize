import datetime
import re


class Date:
    def __init__(self, date=None):
        self._valid = None
        self.text = date
        try:
            self.date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
            self._valid = True
        except ValueError:
            self._valid = False
            self.date = None

    @property
    def valid(self):
        return self._valid

    def __repr__(self):
        return str(self.date)


class Time:
    time_str_12 = ["день", "ночь"]
    time_str_24 = ["сутки"]

    def __init__(self, time):
        self._valid = True
        print(time)
        if time is not None:
            time = time.lower()
            if time.isdigit() and 49 > int(time) > 0:
                self.time = time
                self.text = Time.digit_to_text(time)
                self.num = int(time)
            elif time in Time.time_str_12 or time in Time.time_str_24:
                self.time = time
                self.text = str(time)
                self.num = Time.text_to_digit(time)
            else:
                self._valid = False
                self.time = "время?"
        else:
            self.time = None
            self.text = None
            self.num = None

    @property
    def valid(self):
        return self._valid

    @staticmethod
    def digit_to_text(digit):
        digit = int(digit)
        if digit <= 12:
            return ("день", "ночь")
        elif digit == 24:
            return "сутки"
        else:
            return None

    @staticmethod
    def text_to_digit(text):
        if text in Time.time_str_24:
            return 24
        elif text in Time.time_str_12:
            return 12
        else:
            return None

    def __str__(self):
        return str(self.time)


class Date_Pars:
    PAT_DATA = re.compile("\d{2}[-./,]\d{2}[-./,]\d{2,4}")
    PAT_TIME = re.compile("[\[(]\d{1,2}[)\]]|[\[(]\w+[)\]]")
    PAT_TIME_WORD = re.compile("\d{1,2}|\w+")
    DATA_DEL_PAT = "[-./,]"
    PAT_FORMAT_DATA = "%d.%m.%Y"
    time_valid_12 = ["ночь", "день", 12]
    time_valid_24 = ["сутки", 24]

    def __init__(self):
        self.begin = None
        self.end = None
        self.time = None
        self._dates_valid_flag = True

    @property
    def dates_valid_flag(self):
        d = self.end.date - self.begin.date
        r1 = (d == datetime.timedelta(days=1) and self.time.num == 24)
        print(r1, 1)
        r2 = self.end.date == datetime.datetime.now()
        print(r2)

        return self._dates_valid_flag

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
            print(res_data)
            self.begin, self.end = (Date(res_data[0]), Date(res_data[1]))
            res_time = re.findall(Date_Pars.PAT_TIME, line)
            if res_time:
                time = re.findall(Date_Pars.PAT_TIME_WORD, res_time[0])[0]
                self.time = Time(time)
            else:
                self.time = Time(None)

    def __str__(self):
        return str((self.begin, self.end, self.time))


if __name__ == '__main__':
    s = "20.07.2017-21.07.2017  (Сутки)"
    q ="28.02.17-01.03.17 (сутки)"
    pd = Date_Pars()
    pd.data_pars(q)
    print(pd.begin)









# d = datetime.datetime.strptime(data_lst[0], "%d.%m.%Y")
# print(d)
# print(datetime.datetime.strftime(d, "%d.%m.%Y"))
