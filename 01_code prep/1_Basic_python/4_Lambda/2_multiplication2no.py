def swap_first_last(s):
    return s[-1] + s[1:-1] + s[0]


str1 = 'abcderdwertfdgtysw'
# a and w
swapped_string = swap_first_last(str1)
print(swapped_string)
