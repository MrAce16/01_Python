# 2 method add ab and method 2 c

# class addition:

#     def add_ab(self, a ,b):
#         return a+b
    
#     def add_c(self, a,b,c):
#         retur


# def divide(a,b):
#     try :

#         result = a/b
#         return result
#     except ZeroDivisionError:
#         return "error : division by zero is not allowed"
    
#     except ValueError:
#         return "error: both bad argument"
    
#     except Exception as e:
#         return f"unexpected error:{e}"
def second_highest(lst):
    # unique = list(set(lst))
    # print(unique[-2])
    highest = second_highest = 1

    for num in lst:
        if num > highest:
            second_highest = highest
            highest = num
            
        elif num > second_highest:
            second_highest = num
        
    return second_highest 
    
lst = [10,3,5,5,7,15,20,17]
result = second_highest(lst)
print(result) 

# def second_highest(lst):
#     unique = list(set(lst))  # Remove duplicates
    
#     highest = second_highest = float('-inf')  # Initialize to smallest possible values

#     for num in unique:
#         if num > highest:
#             second_highest = highest  # Update second_highest before changing highest
#             highest = num  # Update highest to the new highest number
#         elif num > second_highest and num < highest:
#             second_highest = num  # Update second_highest if it's between highest and second_highest
    
#     return second_highest if second_highest != float('-inf') else None

# lst = [10, 3, 5, 5, 7, 15, 20, 17]
# result = second_highest(lst)
# print(result)
