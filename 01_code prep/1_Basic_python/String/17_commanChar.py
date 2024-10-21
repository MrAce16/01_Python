# Write a Python program to find the common characters between two strings.
str1 = "abcdef"
str2 = "bcdef"


print(set(str1) & set(str2))
new_str = ""
for char in str1:
    if char in str2:
        new_str += char
print(new_str)
