# list1 = [1,2,3,3,4,5,5,5]
# frequency = {item:list1.count(item) for item in set(list1)}
# print(frequency)


# list1 = [1,5,3,4,2]
# d = 2

# output = [(x,x-d) for x in list1 if (x-d) in list1 ]
# print(output)

# def interger(func):
#     def wrapper(a,b):
#         if not isinstance(a,int) or not isinstance(b,int):
#             raise TypeError("Both parameter be interger only")
#         return func(a,b)
#     return(wrapper)

# @interger
# def add(a,b):
#     return a+b

# print(add(10, 'abc'))


reverse_string = lambda r : r[::-1]

result = reverse_string("hello")
print(result)


