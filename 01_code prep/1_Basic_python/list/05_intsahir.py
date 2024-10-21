# Q1. Count number of element in list
lst1 = [2, 5, 6, 7, 9, 23, 45, 4]
count1 = 0
# print(len(lst1))

for i in lst1:
    count1 += 1
print('lenghtof list:', count1)

# M2 Count number of element in list
data = [1, 2, 3, 4, 5]
count = sum([1 for _ in data])  # list comprehension
print("Length of the list:", count)

# Q2. Count the frequency of the list

data = [1, 2, 2, 3, 4, 4, 4, 5]
count1 = {}
for i in data:
    if i in count1:
        count1[i] += 1
    else:
        count1[i] = 1
print(count1)

# M2 using count

# Q3. merge two list
list1 = [1, 4, 5, 6, 3]
list2 = [3, 5, 6]

# lst = (list1 + list2)   # M1
# print(lst)
list1.extend(list2)  # M2
print(list1)

# Q4. common find out in list

# Method 1 :

data1 = [1, 2, 2, 3, 4, 4, 4, 5]
data2 = [1, 2, 3, 3]
common = []
for i in data1:
    for j in data2:
        if i == j:
            common.append(i)
print(set(common))

# Method 2 :
data1 = [1, 2, 2, 3, 4, 4, 4, 5]
data2 = [1, 2, 3, 3]
commond = []
for i in data1:
    if i in data2:
        if i not in commond:
            commond.append(i)
print("The common of two list is :", commond)

# Q5. Dublicate of in list

data1 = [1, 2, 2, 3, 4, 4, 4, 5]
dublicate_1 = []

#     if data1[i] == i+1:
#         dublicate_1.append(i)
# print(dublicate_1)
for i in data1:
    if data1.count(i) > 1:
        if i not in dublicate_1:
            dublicate_1.append(i)
print(dublicate_1)


# Q6. JOIn in list Q
# data1 = [1, 2, 2, 3, 4, 4, 4, 5]
# str1 = ("".join(data1))
# print(str1)


data1 = [1, 2, 2, 3, 4, 4, 4, 5]
print(''.join(map(str, data1)))
