# Write a Python program to find the longest word in a sentence.

str1 = 'hello jonny the sins of mahrashtra'
count = 0
max_word = ''
max_count = 0
for char in str1.split():
    count = len(char)
    if count > max_count:
        max_count = count
        max_word = char
print(max_word, max_count)
