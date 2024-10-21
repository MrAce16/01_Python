import pandas as pd

df = pd.read_csv(r"C:\Users\ragjha\Downloads\employees.csv")
print(df.iloc[4])
print(df.head)      # to print first 5 rows
print(df.tail)      # to print first 5 columns
print(df.shape)     # to print number of Rows and columns
print(df.iloc[4])   # to print forth 3th row
print(df.iloc[:, 4])  # to print forth 4th column
print(df.iloc[0, 4])  # 0 --> Row and 4 --> column
