#kth greatest element from list

#M1 : Time complexity is O(nlogn) space complexity is O(1)
def  kth_greatest(lst,k):
    lst.sort(reverse=True)
    return lst[k-1]

lst = [1,3,5,2,6,8]
k = 1
output = kth_greatest(lst,k)
print(output)

#M2 Time complexity is O(n) space complexity is O(n)




#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4

def longest_consecutive(nums):
    longest = 0
    numSet = set(nums)

    for i in numSet:
        if i-1 not in numSet:
            length = 1
            while i+length in numSet:
                length +=1
            longest=max(longest,length)
    return longest


nums = [100,4,200,1,3,2,5]
result = longest_consecutive(nums)
print(result)