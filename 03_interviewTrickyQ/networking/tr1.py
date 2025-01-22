# decorator

# def my_decorator(func):
#     def wrapper():
#         print("Hi this decorator 1")
#         func()
#         print("Hi this decorator 2")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# def moves_zeros_to_end(nums):
#     non_zero = 0

#     for i in range(len(nums)):
#         if nums[i] !=0 :
#             nums[non_zero] = nums[i]
#             non_zero +=1

#     while non_zero < len(nums):
#             nums[non_zero] = 0
#             non_zero +=1
#     return nums

# def moves_zeros_to_end(nums):
#     non_zero = 0


#     for i in range(len(nums)):
#         if nums[i] !=0:
#             nums[non_zero] = nums[i]
#             non_zero +=1
#         while






# nums = [0]
# output = moves_zeros_to_end(nums)
# print(output)




# Input: nums = [5,4,-1,7,8]
# Output: 23


def max_subaaray_sum(nums):
    

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):
        current_sum = max(nums[i], current_sum+ nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


nums = [1]
output = max_subaaray_sum(nums)
print(output)