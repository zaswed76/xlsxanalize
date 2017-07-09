import re

pat = re.compile(r"аванс|зарплата", flags=re.IGNORECASE)

line = "Лукьяненко зарПлата"

print(re.search(pat, line))