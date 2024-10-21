# str = input("Enter the string :")
# print(str)
str = 'hello'
# str1 = str[3:]
print(str[3:])
# o/p -- lo


#############################
# sclicing [start : stop : steps]

str = 'my name is hello'
print(str[1:-1:2])    #ynm shl

# Reverse a string  M1

rev = 'john'
print(rev[::-1]) # nhoj


# Reverse a string  M2
rev = 'raghu'
rev1 = reversed(rev)
print(''.join(rev1))  # uhgar

# Reverse a string  M2

# my_string = 'hello world'
# reverse_string = ''
# for char in my_string([::-1]):


def reverse_string_loop(string):
    reversed_string = ""
    for char in string[::-1]:
        reversed_string += char
    return reversed_string


my_string = "hello world"
reversed_string = reverse_string_loop(my_string)
print(reversed_string)  # Output: dlrow olleh
