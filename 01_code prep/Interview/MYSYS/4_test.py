str1 = 'aaaabbbcdddcc'
output = ""
count1 = 0
char = str1[0]

for i in str1:
    if char == i :
        count1 +=1
        #print(count)
    else:

        output = output + count1 * char
        char = i
        count = 1
output = output + int(count1) * char
print(output)

