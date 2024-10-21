# dict1 = {'chai': 2, 'masala': 1, 'cold_tea': 5, 'ginger': 4}
# # dict2 = {'masala': 1}

# # for i in dict1.values():
# #     if 5 == i:
# #         print(f'yes')
# #         break

# # method 2 :

# if 5 in dict1.values():
#     print('yes')
# else:
#     print('No')


# # 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# def square_num(n):
#     d = {}
#     for i in range(1, n):
#         d[i] = i*i
#     print(d)


# square_num(6)


# # 10. Write a Python program to sum all the items in a dictionary.

# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
#      9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# sum1 = 0
# # M1
# sum1 = sum(d.values())
# print(sum1)
# # M2
# for i in d.values():
#     sum1 += i
# print(sum1)

# # 12. Write a Python program to remove a key from a dictionary

# dict1 = {'chai': 2, 'masala': 1, 'cold_tea': 5, 'ginger': 4}

# dict1.pop['chai'] = 2
# print(dict1)


# How many element you want to add in a dictionary, if user = 10, then we need to add 10 items in dict.
# And which one element you want to delete and you need to check it out it is present in dictionary or not
# Add an element to existing dictionary  --> 1
# Find out all the names of employees
# Find out salary of an employees
# Sum of salary of all employees       --> Sum1
# number of employee present in dictionary.  --> count
# Find out the highest salary in all employee.  --> max_dict
# Find out the lowest salary in all employee.   --->
# Display all choices eg: 1 --> Add , 2 --> subract 3-->
dic1 = {'sahir': 1, 'punit': 4, 'rohit': 9, 'mohan': 16, 'ram': 25, 'rahim': 36, 'akbar': 49,
        'saktiman': 64, 'birbal': 81, 'love': 100, 'ishq': 121, 'peter': 144, 'engl': 169, 'dom': 196, 'iron': 225}
sum1 = 0
count = 0
max_dict = 0
min_dict = []
for i in dic1.values():
    sum1 += i
    count += 1
    if max_dict < i:
        max_dict = i


print(sum1, count, max_dict, )
print()
