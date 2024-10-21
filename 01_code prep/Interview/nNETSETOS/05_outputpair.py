# sum in an array in python 

def sum_arr(arr,k):


    #M1 Time complexity is O(n^2) and space complexity is O(1)
    # n = len(arr)
    # for i in range(n):
    #     for j in range(1+i):
    #         if arr[i] + arr[j] == k:
    #             return (f"{arr[i],arr[j]}")
# M2 
    dict1 = {}
    
    for i,num in enumerate(arr) :
        diff = k - num
        if diff in dict1:
            print(f"{i} {arr[i]}")





arr = [5,7,11,32]
k = 18
output = sum_arr(arr,k)
print(output)
#o/p = (1,2)
