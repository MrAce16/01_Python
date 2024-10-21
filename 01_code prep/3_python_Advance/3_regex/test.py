import re
x = "raghuAnD$#@"

pattern = re.compile(r'[^a-z A-Z 0-9]')
match = pattern.search(x)
if match:
    print("special character : ", match.group())
else:
    print("No special character")




# import pandas as pd

# df = pd.read_csv("C:\Users\ragjha\OneDrive - Cisco\Desktop\learning")
# print(df.iloc[4])