list = [8, 7, 2, 5, 3]
n = len(list)
k = 10
for i in range(n):
    for j in range(i+1, n):
        if (list[i]+list[j] == k):
            print(list[i], list[j])

str = 'india'
