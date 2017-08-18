import re

line = "17.08-18.08.17  (24)"
PAT_DATA = re.compile("\d{2}[-./,]\d{2}[-./,]\d{0,4}")
res_data = re.findall(PAT_DATA, line)

print(res_data)