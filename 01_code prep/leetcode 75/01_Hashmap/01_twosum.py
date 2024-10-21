# arr = [1,5,4,9,2]

#M1
# target = 9

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i,j)

def two_sum(list_array,target):

    dict1 ={}
    for i,num in enumerate(list_array):
        diff = target-num
        if diff in dict1:
            return[dict1[diff],num[i]]
        dict1[i] = 1
    return None

list_array=[3,5,7,9,1]
target= 4
sum1= two_sum(list_array, target)
print(sum1)


