
def reverse_string(str1):

    if len(str1)<= 1:
        return str1
    
    return str1[-1] + reverse_string(str1[:-1])

# def reverse_string(s):
#     reverse = ""
#     for i in s:
#         reverse = i + reverse
#     return reverse

str1 = "myworld"
reverse_str = reverse_string(str1)
print(reverse_str)


# class Singleton1:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Singleton1,cls)

    
#     def __init__(self, value = None):
#         if not hasattr(self, initialize):
#             self.value = value
#             self.initialize = True
    

# obj1 = Singleton1("First Instance")
# print(obj1)

# obj2 = Singleton1("second Instance")
# print(obj2)
        





    
