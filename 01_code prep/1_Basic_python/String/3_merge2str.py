'''str1 = "my name "
str2 = "is john"

o/p = my name is john

'''


str1 = "my name "
str2 = "is john"

print(str1 + str2)


################
# Find unique charter in str


str1 = 'test'
str_list = []
for char in str1:
    if str1.count(char) == 1:  # and char not in str_list:
        str_list.append(char)
print(str_list)
