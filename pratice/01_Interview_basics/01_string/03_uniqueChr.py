str1 = 'test'
lst1 = []
for i in str1:
    if i not in lst1 and str1.count(i) ==1 :
        lst1.append(i)
print(lst1)
print(' '.join(lst1))