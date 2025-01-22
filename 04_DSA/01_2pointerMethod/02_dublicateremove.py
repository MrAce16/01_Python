# def remove_dublicate(nums):
#     left,right = 0, len(nums)-1

#     for i in nums:






# nums = [1,1,2,2,4,4,4,5,6,7,8,1]
# print(remove_dublicate(nums))

nums = [1,1,2,2,4,4,4,5,6,7,8,1]
non_dublicate = []

for i in nums:
    if not non_dublicate or nums[i]!=non_dublicate[-1] :
        non_dublicate.append(i)
print(non_dublicate)