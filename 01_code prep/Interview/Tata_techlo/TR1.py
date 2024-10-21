
def greeting(func):
    # print("Hello")
    func()
    print("Hello Raghunath")
    
@greeting
def raghu():
    pass



def car(func):
	print("This is F1 car")
	func()
	print("Modify the car")
					
@car
def green_car():
    print("This is green car")

# 



# class Animals():
#     def speak():
#         print("animal speak")

# class Dog():
#     def speak():
#         print("Vow vow")

# class Cat(Animals, Dog):
#     def sound():
#         print("mew mew")

# cat = Cat()
# Cat.speak()

# l = [1,2,3,4,5,6]

# d = {x:'odd' if x % 2 !=0 else 'even' for x in l}
# print(d)