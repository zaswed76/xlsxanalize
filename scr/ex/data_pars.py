import re

line = "17.08.2017-18.08  (24)"
PAT_DATA_START = re.compile("\d{2}[./,]\d{2}")
PAT_DATA_END = re.compile("(?:\d{2}[-./,]\d{2}[-./,])(\d{2}[-./,]\d{2}[-./,]\d{0,4})")
PAT_DATA = re.compile("""
                     (\d{2}[./,]\d{2}[./,]?\d{0,4})
                     ([-./,])
                     (\d{2}[./,]\d{2})
                     """, re.VERBOSE)


PAT_DATA_YEAR = re.compile("\d{2}[./,]\d{2}[./,]\d{0,4}")

res_data = re.search(PAT_DATA, line)
res_data_years = re.search(PAT_DATA_YEAR, line)
# res_data_year = re.findall(PAT_DATA_YEAR, line)


# print(res_data_start.group())
# print(res_data_end.group(1))
# print()
# print(res_data_years.group())


import datetime
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


line = "17.08.17-17.08.17"
print(re_data(line))
import webbrowser
webbrowser.open('http://python.org')