''' Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. 
    Sample String : 'w3resource' 
    Expected Result : 'w3ce' 
    Sample String : 'w3' 
    Expected Result : 'w3w3' 
    Sample String : ' w' 
    Expected Result : Empty String '''

str1 = input("Enter the string :")
if len(str1) > 2:
    print(str1[:2] + str1[-2:])
elif len(str1) == 2:
    print(str1) + print(str1)
else:
    len(str1) < 2
    print(f'Empty string')
