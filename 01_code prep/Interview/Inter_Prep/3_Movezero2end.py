# Move zero or any element at the end of the list.
list1 = [1, 2, 3, 0, 0, 8, 2, 2, 6, 8, 0, 1]

for i in list1:
    if i == 0:
        list1.remove(i)
        list1.append(i)

print(list1)
