#1. Python program to remove character from string

def str_remove_ch(str,ch_remove):
    str2 = str.replace(ch_remove,'')
    return str2


str = "hello"
ch_remove = "l"
output = str_remove_ch(str,ch_remove)
print(output)
