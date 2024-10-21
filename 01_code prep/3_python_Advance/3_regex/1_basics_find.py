# Q1. To Find the character in the string

import datetime
import re
str1 = "The lazy dog run over the intelligent fox"
pat = r'.a'
match = re.findall(pat, str1)
print(match)


# Q2. To find the date and time in regex


str1 = "999-1-1-9867,01/36/2024 is 07/08/2024"
patter = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
dates = re.findall(patter, str1)
print(dates)
