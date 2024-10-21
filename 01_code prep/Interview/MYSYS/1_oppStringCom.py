#Input = a2b4c6
#output = aabbbbcccccc

str1 = "a2b4c6"
output = ""

for i in range(0, len(str1), 2):
    char = str1[i]
    count = int(str1[i+1])
    output += char*count
print(output)
