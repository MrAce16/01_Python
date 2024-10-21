# Case1 : Input : A3G4B2
# output: ADGKBD
str1 = "A3G4B2"
str2 = ""
for ch in str1:
    if ch.isalpha():
        str2 = str2 + ch
        temp = ch
    else:
        str2 = str2+chr(ord(temp) + int(ch))
print(str2)

# Program fails for case 2 :
# Case1 : Input : A3X4Z3
# output: ADXBZC

str1 = "A3X4Z3"
str2 = ""
for ch in str1:
    if ch.isalpha():
        str2 = str2 + ch
        temp = ch
    else:
        if (ord(temp)+int(ch)) > 90:
            str2 = str2+chr(64+(int(ch)-(90-ord(temp))))
        else:
            str2 = str2+chr(ord(temp) + int(ch))
print(str2)
