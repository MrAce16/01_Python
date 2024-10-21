'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
Sample String : 'restart' 
Expected Result : 'resta$t'''

str1 = "this is the world tour, it will be beautiful"
str_new = str1[0]
h = str_new
for i in range(1, len(str1)):
    if str1[i] == h:
        str_new += '$'
    else:
        str_new += str1[i]
print(str_new)
