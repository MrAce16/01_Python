def factorial(num):
    if num<= 1:
        return 1
    else: 
        return num * factorial(num -1)

num = 6
print(factorial(num))


