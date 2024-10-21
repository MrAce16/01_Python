# Write a Python program to capitalize the first letter of each word in a sentence

str1 = 'hello world, john sins'

for char in str1.split():
    print(char.capitalize(), end=' ')
