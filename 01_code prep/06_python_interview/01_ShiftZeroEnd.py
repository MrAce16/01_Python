lst = [1,0,3,5,7,80,9,0,0,8]

# M1 complexity is o(n square)
for i in lst:
    if i ==0:
        lst.remove(i)
        lst.append(0)
print(lst)

#M2 Time complexity is O(n)
new_lst = []
count = 0
for i in lst:
    if i == 0:
        count += 1
    else:
        new_lst.append(i)

new_lst.extend([0]* count)
print(new_lst)






