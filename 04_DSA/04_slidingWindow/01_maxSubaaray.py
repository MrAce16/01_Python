#Find the maximum value in every window of size k in a given array

# Given an array arr[] of size N and an integer K, the task is to find the maximum element in every sub-array of size K.

# Examples:
# code this
# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
# Output: 3 5 6
# Explanation:
# The sub-array of size 3 are {1, 2, 3} => Max = 3
# {2, 3, 1} => Max = 3
# {3, 1, 4} => Max = 4
# {1, 4, 5} => Max = 5
# {4, 5, 2} => Max = 5
# {5, 2, 3} => Max = 5
# {2, 3, 6} => Max = 6

# write code for this in python
arr = [1, 2, 3, 1, 5,4, 2, 3, 6] 
K = 3
output = [3, 5, 6]
def maxSubarray(arr, K):
    n = len(arr)
    for i in range(n - K + 1):
        print(max(arr[i : i + K]), end = " ")