# Class and objects basic that need to understand.
class Abc():

    def __init__(self):  # special functio constructor
        print("company name", f"HYundi")

    def display(self, carname):                            # normal function
        print("hello, my car model", carname)


creata = Abc()
creata.display("Creata")
verna = Abc()
verna.display("Verana")

# Inheritance


class Xyz(Abc):  # Xyz is child class and Abc is parent class
    pass


obj2 = Xyz()
obj2.display('i20')

# Functions and arguments


def add(s):  # parameter   #function definition
    print(s)  # body.


add("hello")  # function call  argumnet
