# first question
b = [1, 2, 2] * -2
print(b) 


# second question

a = [1, 2, 3, 4, 5]
a.extend([6, 7])  # [1,2,3,4,5,6,7]
print(a[::-1]) #[7,6,5,4,3,2,1]

# 3rd question

from collections import deque

myqueue = deque([i for i in range(10)]) # [0,1,2,3,...9]
myqueue.append(0) #[0,1,2,3....9,0]
myqueue.pop() # [0,1,2,3....,9]
myqueue.appendleft(10)#[10,0,1,2,3,..,9]
myqueue.popleft() #[0,1,2....,9]
print(myqueue) 

# 4th question decorator

def color_decorator(func):
    def inside(*args, **kwargs):
        return "Yellow" 
    return inside


@color_decorator
def Painter(color):  #Red
    return f"The color is {color}"

print(Painter("Red"))



# 5th nested list

def get_list(nested_list):
     return [item for sublist in nested_list for item in sublist]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = get_list(nested_list)
print(result)

# 6 Time complexity O(n)

def linear_search(list1, target):
    for item in list1:
        if item == target:
            return True
    return False


