# Write a Python program to count the number of vowels in a string

str1 = 'this is the camel'
vow = 'a', 'e', 'i', 'o', 'u'
c = 0
for i in str1:
    if i in vow:
        c += 1
print(c)


# str1 = 'this is the camel'
# c = 0
# for i in str1:
#     if i in 'a' or 'e' or 'i' or 'o' or 'u':
#         c += 1
# print(c)
