# The Next greater Element for an element x is the first greater element on the right side of x in the array.
#  Elements for which no greater element exist, consider the next greater element as -1.
# Input: arr[] = [ 4 , 5 , 2 , 25 ]
# Output:        4      –>   5
#                5      –>   25
#                2      –>   25
#                25     –>   -1
# Explanation: except 25 every element has an element greater than them present on the right side


def next_greater(arr):
    s = []
    result = [-1] * len(arr)

    for i in range(len(arr)-1, -1,-1):
        while s and s[-1] <= arr[i]:
            s.pop()
            if s:
                result[i] = s[-1]
                s.append(arr[i])
    for i 





arr = [ 4 , 5 , 2 , 25 ]
next_greater(arr)