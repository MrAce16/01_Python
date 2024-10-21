list1 = [8,7,2,5,3,1]
k = 10
n = len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]+ list1[j] == k:
            print(f"number are {list1[i]} and {list1[j]}")