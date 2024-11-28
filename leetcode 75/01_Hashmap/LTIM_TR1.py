def second_largest(numbers):

    # unique = list(set(numbers))
    # if len(unique) < 2:
    #     return None
    
    # unique.sort(reverse=True)
    # return unique[1]

    if len(numbers) < 2 :
        return None
    
    largest = second = 0

    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        
        elif i > second and i!=  largest:
            second = i
    
    return second 

    
 
numbers = [-10,-20,-30,-40,-4,-5,-45,-9,-98,-5]
print(second_largest(numbers))





class Student:
    stream = 'abc'
    def __init__(self, name, email):
        self.name = name
        self.email = email
a = Student('Test1', 'Test1@gmail.com')
b = Student('Test2', 'Test2@gmail.com')

print(a.stream)   # 'abc'  
print(b.stream)   # 'abc'
a.stream = 'xyz'

print(a.stream)  # 'xyz'
print(b.stream)  # 'abc'
Student.stream = 'pqr'
print(a.stream)   # 'xyz'
print(b.stream)  # 'pqr'

# output = 