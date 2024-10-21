list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2 = [0, 4, 5]
j = 1
for i in range(0, len(list1)-j):
    if i in list2:
        list1.pop(i)
        j += 1
print(list1)

# list1.pop(0)
# list1.pop(4)
