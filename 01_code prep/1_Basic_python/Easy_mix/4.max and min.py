l = [9, 11, 0, 370, 55, 40, 2]
max1 = l[0]
min1 = l[0]

for i in l:
    if max1 < i:
        max1 = i
    if min1 > i:
        min1 = i

print('min:', min1)
print('max:', max1)
