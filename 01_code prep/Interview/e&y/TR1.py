# Abstraction
import abc import ABC

class Animal(ABC):
    def sound (self):
        pass

# Even square and odd cube print
lst = [1,2,3,4,5,6,7,8,9]

result = [x**2 if x % 2 ==0 else x**3 for x in lst]
print(result)

#merge the dictionary
dic1 = {"name": "raghu", "age":32,"dep":"it"}
dic2 = {"add":"abc", "loc":"mum","cout":"india"}

# dic3 = dict(zip(dic1,dic2))
# print(dic3)
# dic1.update(dic2)
# print(dic1)


# merged_dict= {k:v for k,v  in zip(dic1,dic2)}
# print(merged_dict)