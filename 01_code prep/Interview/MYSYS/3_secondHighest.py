list1 = [2, 4, 5, 23, 45, 34, 56, 78, 52, 67]
# list2 = sorted(list1)
# print("Second largest number in the list:", list2[-2]) # - -> method 1 using sorted function


# -- To Find max this logic is applicable
# max_num = list1[0]

# for i in list1:
#     if i > max_num:
#         max_num = i
# print(max_num)


# Second Largest number
largest = list1[0]
second_largest = list1[0]
for i in list1:
    if i > largest:
        largest = i
for j in list1:
    if j > second_largest and j != largest:
        second_largest = j
print(second_largest)
