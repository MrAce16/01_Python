# Function returning multiple values

# Problem : Create a function that returns both the area and circumference of a circle give its radius.
import math


def circum_status(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


print(area,)
