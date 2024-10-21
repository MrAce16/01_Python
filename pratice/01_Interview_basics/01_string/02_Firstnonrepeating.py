#To remove dublicate from string
str1 = "swiss"
lst = []
for i in str1:
    if i not in lst:
        lst.append(i)
print(lst)

# Find the First Non-Repeating Character

count = 0
for char in str1:
    if str1.count(char) == 1:
        print(char)
        break

x = [[]]
x = x*5    
x[0].append(2)
print(x)


