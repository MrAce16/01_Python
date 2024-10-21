#String manupulation
str1 = "hello World"
print(str1.replace(" ",""))
print(str1[1::3])
print(str1.replace(" ",""),str1.lower(),str1[1::3])

#reverse a string :
print(str1[::-1])

#Palinrome
if str1 == str1[::-1]:
    print("given str is palindrome")
else:
    print("given str is not a palindrome")




