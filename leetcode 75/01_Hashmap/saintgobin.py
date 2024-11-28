# list_values=[2,3,5,3,4,2,2,2,3,5,3,3,3,3,3]

 
# # {2:4,3:4}

# output = {}

# #min_frequency = 3

# for i in list_values:
#     if i in output:
#         output[i] +=1
#     else :
#         output [i] =1

# max_frequency = 4

# output = {key:value for key, value in output.items() if value > max_frequency}

# print(output)


# list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list_values=[2,3,5,3,4,2,2,2,3,5,3,3,3,3,3]

output = {}
max_key, max_value = 0,0

for i in list_values:
    n = i.count(list_values) 