

import arrow

import arrow

# s = "29.07.2017"
s2 = "29.07.2017-30.07.2017,444  (24)"
obj = arrow.get(s2, 'DD.MM.YYYY')
print(obj.format('DD.MM.YYYY'))
# print(arrow.Arrow(2013, 5, 5, 12, 30, 45))