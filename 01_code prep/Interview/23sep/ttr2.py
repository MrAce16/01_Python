str1 = input("Enter a string: ")

char = []

for i in str1:
    if i.isalpha():
        char.append(i)


reversed1 = reversed(char)


result = []


for i in str1:
    if i.isalpha():
        result.append(next(reversed1))  
    else:
        result.append(i)  


reversed_string = ''.join(result)
print(reversed_string)
