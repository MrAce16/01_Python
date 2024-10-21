str = "This is the woooorld"
output = {}
total = 0

for s in str:
    n = str.count(s)
    if total < n:
        k = s
        total = n
output[k] = total
print(output)
