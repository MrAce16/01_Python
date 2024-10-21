# Q1 Function with paramenters

def person(name, age):
    print("Name :", name)
    print("age :", age)


obj = person(age=30, name="Rahul")    # Order doesn't matter


# Q2 Function without parameter and with return.

def get_five():
    return 5


result = get_five()
print(result)

# eg:2


def dog():
    return 'bark'


obj1 = dog()
print(obj1)

# Q3. Function with paramenter and return


def add(a, b):
    sum = a + b
    return sum


results = add(4, 5)
print(results)

# eg:2


def multi(a, b):
    multiply = a*b
    sum1 = a + b
    return multiply, sum1


result = multi(9, 5)
print(result)

# Q4. 