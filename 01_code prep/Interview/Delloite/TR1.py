#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longest_consecutive(nums):
    longest = 0
    num_set = set(nums)

    for num in num_set:
        if num -1 not in num_set:
            current = num 
            consective = 1

            while current + 1 in num_set:
                current +=1
                consective +=1
            longest = max(longest,consective)
    return longest


nums = [100,4,200,1,3,2]
output = longest_consecutive(nums)
print(output)

#M2 Time complexity is O(n) space complexity is O(n)
def longest_consecutive(nums):
    longest = 0
    numSet = set(nums)

    for i in numSet:
        if (i-1) not in numSet:
            length = 1
            while (i+length) in numSet:
                length +=1
            longest=max(longest, length)
    return longest


nums = [100,4,200,1,3,2,5]
result = longest_consecutive(nums)
print(result)

