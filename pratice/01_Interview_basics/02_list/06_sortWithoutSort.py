lst1 = [41,23,41,12,6,7,8,9,21,45,45]
lst2 = list(set(lst1))
n = len(lst2)
for i in range(n):
    for j in range(i+1,n):
        if lst2[i] > lst2 [j]:
            lst2[i],lst2[j] = lst2[j],lst2[i]
print(lst2)