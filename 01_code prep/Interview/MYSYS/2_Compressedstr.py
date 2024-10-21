str1 = 'aaaabbbcdddcc'
output = ''
char1 = str1[0]
counter = 0

for ch in str1:
    if ch == char1:
        counter += 1
    else:
        output = output + char1 + str(counter)
        counter = 1
        char1 = ch
output = output + char1 + str(counter)
print(output)
