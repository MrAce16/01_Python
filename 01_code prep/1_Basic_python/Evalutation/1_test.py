# Q1 add 2 list
# list1 = ['my', 'name']
# list2 = ['is', 'john']
# # list1.extend(list2)
# # print(' '.join(list1))

# list3 = list1 + list2
# print(' '.join(list3))

# Q2. combine to list and convert to dictionary
# list1 = ['my', 'name', 'is']
# list2 = [1, 2, 3]

# # dict1 = dict(zip(list1, list2))
# # print(dict1)
# dict2 = {list1(i): list2(i) for i in range(len(list1))}
# print(dict2)

# Q3. find the pair with given number in A list

list1 = [8, 7, 2, 5, 3, 1]
n = len(list1)
K = 10
for i in range(n):
    for j in range(i+1, n):
        if list1[i] + list1[j] == K:
            print(list1[i], list1[j])
