lst = ['india','is','my','country']
lst1 = []
str1 = ''.join(lst)


for i in str1:
    if str1.count(i) > 1 and i not in lst1 :
        lst1.append(i)
print(i)

