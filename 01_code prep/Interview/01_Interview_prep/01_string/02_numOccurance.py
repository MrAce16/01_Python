# 2. Python Program to count occurrence of characters in string

def str_count(str):
    dict1 = {}
    max_count = 0
    max_char = ""
    for i in str:
        if i in dict1:
            dict1[i] += 1
        else :
            dict1[i] = 1
    for i,j in dict1.items():
        if j > max_count:
            max_count = j
            max_char = i
    return(f"{max_char} : {max_count}") 
        
str = "hello world!"
output = str_count(str)
print(output)

#print(str.count('l'))
