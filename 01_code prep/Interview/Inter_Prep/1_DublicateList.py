
# To find dublicate in list using M1
# list1 = [2, 4, 6, 4, 8, 10, 20, 35, 2, 2]
# dublicate_list = []
# for i in list1:
#     if list1.count(i) > 1 and list1[i] not in dublicate_list:
#         dublicate_list.append(i)
# print(dublicate_list)


# M2 Without using inbuild function.

list1 = [2, 4, 6, 4, 8, 10, 20, 35, 2, 2]
dublicate_list = []
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j] and list1[i] not in dublicate_list:
            dublicate_list.append(list1[i])
print(dublicate_list)
