# str1 = 'madam'
# if str1 == str1[::-1]:
#     print('string is palindrome')
# else:
#     print("string is not palindrome")

import re
number1 = [1, 2, 3, 4]
number2 = [6, 7, 8, 9]
multiple_num1_num2 = list(map(lambda x, y: x*y, number1, number2))
print(multiple_num1_num2)

with open('ip.txt', r) as file:
    content = file.read()

# rgergeg7468', '192.68.3.4'))
ipv4_patter = r'^ (("192.168.1.1 a@3455667hfhgnsg", '192.168.2.1 b


def is_ip_address(ip):
    return re.match(is_ip_address, ip) is not None


print(is_ip_address("192.168.1.1"))
print(is_ip_address("192.168.1.2"))
