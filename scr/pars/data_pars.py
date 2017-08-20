import datetime
import re


class Date:
    def __init__(self, date=None):
        self._valid = None
        self.text = date

        try:
            self.date = datetime.datetime.strptime(date,
                                                   "%d.%m.%Y").date()
            self._valid = True
        except ValueError:
            try:
                self.date = datetime.datetime.strptime(date,
                                                       "%d.%m.%y").date()
                self._valid = True
            except ValueError:
                self._valid = False
                self.date = None

    @property
    def valid(self):
        return self._valid

    def __repr__(self):
        return str(self.date)

    def __sub__(self, other):
        if (isinstance(self.date, datetime.date) and
                isinstance(other.date, datetime.date)):
            return self.date - other.date

    def __gt__(self, other):
        if (isinstance(self.date, datetime.date) and
                isinstance(other.date, datetime.date)):
            return self.date > other.date

class Time:
    time_str_12 = ["день", "ночь"]
    time_str_24 = ["сутки"]

    def __init__(self, time):
        self._valid = True

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

    def __repr__(self):
        return str(self.time)

    def __eq__(self, other):
        return self.num == other.num

def re_data(line):
    pat_data = re.compile("""
                     (\d{2}[./,]\d{2})
                     ([./,]?)(\d{0,4})
                     ([-./,])
                     (\d{2}[./,]\d{2})
                     ([./,]?)(\d{0,4})
                     """, re.VERBOSE)

    res = re.search(pat_data, line)
    if res :
        dates = res.group(1, 5)
        years = res.group(3, 7)
        if years[0] and years[1]:
            y = (int(x) for x in years)
        elif years[0] or years[1]:
            _y = int([x for x in years if x][0])
            y = (_y, _y)
        else:
            _y = datetime.date.today().year
            y = (_y, _y)
        r = tuple(["{}.{}".format(d, y) for d, y in zip(dates, y)])
        return r
    else:
        return (None, None)

class Date_Pars:
    PAT_DATA = re.compile("\d{2}[-./,]\d{2}[-./,]\d{0,4}")
    PAT_TIME = re.compile("[\[(]\d{1,2}[)\]]|[\[(]\w+[)\]]")
    PAT_TIME_WORD = re.compile("\d{1,2}|\w+")
    DATA_DEL_PAT = "[-./,]"
    PAT_FORMAT_DATA = "%d.%m.%Y"
    time_valid_12 = ["ночь", "день", 12]
    time_valid_24 = ["сутки", 24]

    def __init__(self):
        self.counter = 0
        self.begin = None
        self.end = None
        self.time = None
        self._line = None
        self._dates_valid_flag = True

    def __eq__(self, other):
        beg = self.begin.date == other.begin.date
        end = self.end.date == other.end.date
        time = self.time.num == other.time.num
        return all([beg, end, time])

    @property
    def dates_valid_flag(self):
        """
        проверяет соответствует ли части даты друг другу и времени
        :return: bool
        """
        d = self.end - self.begin
        if (d == datetime.timedelta(days=1) and self.time.num == 24):
            r1 = True
        elif (d == datetime.timedelta(days=0) and self.time.num < 24):
            r1 = True
        else:
            r1 = False
        r2 = self.end.date == datetime.datetime.now().date()
        return all([r1, r2])

    @staticmethod
    def del_space(line):
        return "".join(line.split())


    def regeexp_data(self, line):
        begin, end = None, None
        line = Date_Pars.del_space(line)
        res_data = re.findall(Date_Pars.PAT_DATA, line)
        if not res_data:
            return []
        else:
            res_data = [re.sub(Date_Pars.DATA_DEL_PAT, ".", d) for d
                        in res_data]
        if res_data:
            begin = Date(res_data[0])
        if len(res_data) == 2:
            end = Date(res_data[1])
        return begin, end



    def data_pars(self, line):
        if not isinstance(line, str):
            return
        self._source_line = line

        _begin, _end = re_data(line)

        if _begin is None or _end is None:
            pass
        else:
            self.begin = Date(_begin)
            self.end = Date(_end)

        res_time = re.findall(Date_Pars.PAT_TIME, line)
        if res_time:
            time = \
            re.findall(Date_Pars.PAT_TIME_WORD, res_time[0])[0]
            self.time = Time(time)
        else:
            self.time = Time(None)

    @property
    def source_line(self):
        return self._source_line

    def __str__(self):
        return str((self.begin, self.end, self.time))

    def __gt__(self, other):
        if isinstance(self.end, Date) and isinstance(other.end, Date):
           r =  self.end > other.end
           return r


if __name__ == '__main__':
    # s = "12.07.18"
    s = "17.08-18.08.17  (24)"

    pd = Date_Pars()
    pd.data_pars(s)

    print(pd)











# d = datetime.datetime.strptime(data_lst[0], "%d.%m.%Y")
# print(d)
# print(datetime.datetime.strftime(d, "%d.%m.%Y"))
