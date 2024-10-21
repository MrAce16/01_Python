import pandas as pd
# #hybrid inheritence : 

# class A :
#     def m_a(self):
#         print("print A")

# class B(A):
#     def m_b(self):
#         print("print B")

# class C(A):
#     def m_c(self):
#         print("print c")

# class D(B,C):
#     def m_d(self):
#         print("print D")

# d = D()

# df = pd.read_csv('C:\Users\ACER\Downloads/customers-100.csv','encoading'= utf-8)

# print(df.head())


def concat(a,b,c,d,e):
    print(a+str(b)+str(c)+str(d)+e)


c = concat(1,'rahul','mohan','rupam',5)
print(c)