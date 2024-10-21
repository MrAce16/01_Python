# Write a Python program to get the largest, smallest number and sort from a list. without using inbuilt function

list1 = [4, 5, 6, -9, 5, 8, 34, 87]
for i in range(len(list1)):
    for j in range(len(list1)-1-x):
        if list1[j] > list1[i]:
            list1[j], list1[i] = list1[i]

print(sort1)


# ========solution=====
# list1=[8,4,6,7,1,3,-9,6,-5,99]


# for x in range(len(list1)):
#     for j in range(len(list1)-1-x):
#         if list1[j]> list1[j+1]:
#             list1[j], list1[j+1]=list1[j+1],list1[j]
# print(list1)
# print(f'the mi ninimum of list1 is {list1[0]}')
# print(f'the mi max of list1 is {list1[len(list1)-1]}')
# print(list1[:-4:-1])


# for x in range(10):
#     print(x)
