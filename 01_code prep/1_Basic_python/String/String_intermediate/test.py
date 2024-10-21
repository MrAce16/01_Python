
# square_dict = {num: num**2 for num in range(1, 11)}
# print(square_dict)

# squares = {}
# for i in range(1, 11):
#     squares[i] = i ** 2
# print("squares using loop :", squares)


# import re

# ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


# def is_ipv4_address(ip):
#     return re.match(ipv4_pattern, ip) is not None


# # Example usage
# print(is_ipv4_address("192.168.1.1"))  # True
# print(is_ipv4_address("255.255.255.255"))  # True
# print(is_ipv4_address("256.100.50.25"))  # False
# print(is_ipv4_address("192.168.1.300"))  # False


# lambda function for even and odd

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda function to check if a number is even

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Find odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
