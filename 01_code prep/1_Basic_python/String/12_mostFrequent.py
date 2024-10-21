# Write a Python program to find the most frequent character in a string

# str1 = 'life is beautiful'
# count1 = 0
# for i in str1:
#     if i


# Using dictionary
string = "hello world welcome in world of string python"
dic = {}


max_count = 0
max_char = ''
for x in string:
    if x != ' ':
        count_char = string.count(x)
        # dic[x]=count_char
        if count_char > max_count:
            max_count = count_char
            max_char = x
print(f'{max_char}:{max_count}')
