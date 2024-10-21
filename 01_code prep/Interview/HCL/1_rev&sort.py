# Reverse string using for loop
# str1 = "Hello world"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print(str2)


# sort the given list inside tuple with number

# tu = [("xyz", 20), ("qwe", 5), ("asd", 10), ("uio", 15)]

# list1 = tu(sorted(l) for l in tu)
# print(list1)

# Sort the list of tuples based on the second element (the number)

tu = [("xyz", 20), ("qwe", 5), ("asd", 10), ("uio", 15)]
n = len(tu)
for i in range(0, n):
    for j in range(0, n-i-1):
        if tu[j][1] > tu[j+1][1]:
            tu[j], tu[j+1] = tu[j+1], tu[j]
print(tu)


# Bubble sort
my_list = ["banana", "apple", "mango", "zebra", "cherry"]

for i in range(0, len(my_list)):
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)
