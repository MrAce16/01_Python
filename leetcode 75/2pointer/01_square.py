# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def square_asc(nums):

    list1 = [i*i for i in nums  ]
    rev = []
    print(list(sorted(list1)))
    # print(rev)


nums = [-4,-1,0,3,10]
output = square_asc(nums)
print(output)