'''Write a Python script that takes input from the user and 
displays that input back in upper and lower cases '''


def lower_upper(str1):
    print(str1.lower())
    print(str1.upper())


str1 = input("Enter the string in mixed form")
lower_upper(str1)
