lst = [1,2,3,1,3,6,5]
lst1 =[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
    elif i in lst1:
        print(i, end =" ")
    