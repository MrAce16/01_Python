# Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'

# Count of number of string


def count_char(char1):
    count = {}
    for i in char1:
        count += 1
    print(count)


char1 = 'google.com'
count_char(char1)


# M2 :
char1 = 'google.com'
dict1 = {}
for i in char1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)
