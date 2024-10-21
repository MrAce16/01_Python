# data = [{"sshUserName":"admin",
#          "groupName":"vpc","switchName":"SW_95","switchDbID":"1020","ipAddress":"10.1.228.95"},
#          {"sshUserName":"admin","groupName":"vpc","switchName":"SW_146","switchDbID":"1070","ipAddress":"10.1.228.146"},
#          {"sshUserName":"admin","groupName":"Policy","switchName":"SW_192","switchDbID":"5480","ipAddress":"10.1.228.192"}]

# # print dictionary with switch name as key and its ip address as value.
# # eg: {'SW_95':'10.1.228.95','SW_146':'10.1.228.146', ...}
# list1 =[]
# list2 =[]
# for i in data:
#     for j,v in i.items():
#         if j == "switchName":
#             list1.append(v)
#         elif j == "ipAddress":
#             list2.append(v)
# dict1 = dict(zip(list1,list2))
# print(dict1)

# op = '''
# Software
# BIOS: version 07.69
# NXOS: version 9.3(11)
# BIOS compile time:  04/08/2021
# NXOS image file is: bootflash:///nxos.9.3.11.bin
# '''

#use regular expression to find BIOS version and NXOS version.

import re 

text = ''' Software
BIOS: version 07.69
NXOS: version 9.3(11)
BIOS compile time:  04/08/2021
NXOS image file is: bootflash:///nxos.9.3.11.bin'''

bios_pattern = r"BIOS\s+version\s*:\s*([])"

bios_match = re.serach(bios_pattern,text)

if bios_match:
    print("bios version",bios_match.group(1))

Question1: Need to find whether the input string is valid IPv4 Address or not.

Hint:

IPV4: contains 4 octets ranging from 0-255

Constraints:

Should not use Regular Expression in the code.

Must use Class and Object oriented approach.

Code must utilize low Memory and CPU during execution.

Must write the Logical functions for IPv4.

Below are Sample Inputs and code must provide the exact output.

Input1:
ip_address="*.1.1.1"
Not Valid

Input2:
ip_address="35.2.123.1"
Valid