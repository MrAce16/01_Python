# Write a Python program to remove all duplicates from a string and return the result.

str1 = 'Hello world'
remove_dublicate = ''
for i in str1:
    if i not in remove_dublicate:
        remove_dublicate += i
print(remove_dublicate)
