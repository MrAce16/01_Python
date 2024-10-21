# #shallow copy
# s= 5
# b = s
# b = 2
# print(s)

# # deep copy

# s= 5
# nw_obj = copy.deepcopy(s)

#decorator

# def animal(func):
#     def wrapper():
#         print("this is animal")
#         func()
#         print("this is animal1")
# @animal
# def dog(a):
#     print("vow vow")

# dog()

# import pandas as pd

# df = pd.Dataframe(columns=['id','name','values'])
# print(df)

# class Person:
#     s = "human"

#     def __init__(self, name, age):
#         self.name = name

    
#     def display(self):
#         return f"name"{self.name}
    
#     @classmethod


# Input: s = "helilo"
# Output: "holile"


def reverse_vowls(input_str):
    vowels = "aeiouAEIOU"
    s = list(input_str)
    i =0
    j=len(input_str) -1
    while i < j:
        if s[i] not in vowels:
            i +=1
        elif s[j] not in vowels:
            j -=1
        else:
            s[i] ,s[j] = s[j], s[i]

            i +=1
            j -=1
    
    return ''.join(s)

input_str = "helilo"
output_str = reverse_vowls(input_str)
print(output_str)

lst = list(map(int, input().split()))  # This takes user input correctly
# Example: input = [10, 20, 30, 40, 50, 60]
lst[0], lst[-1] = lst[-1], lst[0]  # Swap first and last elements
print(lst)