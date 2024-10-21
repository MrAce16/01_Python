s = 'abhlnaoffiefffsjfljdsds'
ch = {}
for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
max_char = max(ch, key=ch.get)
print(max_char)
