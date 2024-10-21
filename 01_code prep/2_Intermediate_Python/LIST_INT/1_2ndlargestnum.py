lst1 = [2, 4, 5, 6, 3, 8, 9]
# lst2 = sorted(lst1)   --> M1
# print(lst2[-2])
larg = 0
secnd_larg = 0

for i in lst1:
    if lst1[i] > lst1[i+1]:
        larg += i
print(larg)
