a = list(range(10))
print(a[2 : -2])

def length(s):
    count = 1
    char = []
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count +=1
        
        else:
            char.append(f"{s[i-1]}{count}")
            count = 1
    char.append(f"{s[i-1]}{count}")

    return ''.join(char)
    
input = "aaaabbbccaaaaa"
output = length(input)
print(output)
# output = "a3b2a2"

