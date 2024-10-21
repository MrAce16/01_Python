# You are given a base class Vehicle with attributes make and model and a method start_engine() that prints "Engine started."
# Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
# Additionally, override the start_engine() method to print "Car engine started."

class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine():
        print("Engine started.")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model) #Super method is used to call ---> Base class constructer 
        self.doors = num_doors

    def start_engine(self):
        print("Car engine started.")


# Example usage:
my_car = Car("Toyota", "Camry", 4)
my_car.start_engine()  # Output: Car engine started.
