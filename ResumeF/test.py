# def form_palindrome(s):
#     count1 = {}
#     for char in s:
#         if char in count1:
#             count1[char] +=1
#         else:
#             count1[char] =1
    
#     odd = 0
#     for count in count1.values():
#         if count % 2 != 0:
#             odd +=1
    
#     return odd <=1
   


# s="hello"
# print(form_palindrome(s))

# input 2,3,4,5,6.8.9,12,13,16
 
# output 5,6,12,13
import math

def is_power(n):
    if n<= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        exp = math.log(n, i)
        if abs(round(exp)-exp) < 1e-10:
            return True
    return False

def remove_power(input):
    return[num for num in input if not is_power (num)]


input = [2,3,4,5,6,8,9,12,13,16]
output = remove_power(input)
print(output)