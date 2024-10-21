def power_factory(exp):
    def power(base):
        return base ** exp
    return power


square = power_factory(2)
cube = power_factory(3)
print(square(4))  # Outputs: 16
print(cube(3))    # Outputs: 27
