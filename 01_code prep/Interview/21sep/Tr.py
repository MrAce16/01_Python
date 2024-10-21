
#  Mr=[(1,2),(2,3),(3,4),(4,5),(1,3),(2,4)]
#    output=[(1,2),(2,3),(3,4),(4,5)]

# def non_overlap(Mr):
#     lst = []
#     for i in range(len(Mr)):
#         first , second = Mr[i]
#         if i == len(Mr)-1:
#             new_tup = (second, second+1)
#         else:
#             new_tup = Mr[i]
#         lst.append(new_tup)
#     return lst

# Mr=[(1,2),(2,3),(3,4),(4,5),(1,3),(2,4)]
# output = non_overlap(Mr)
# print(output)

Mr=[(1,2),(2,3),(3,4),(4,5),(1,3),(2,4)]
output = []

for i in range(len(Mr)):
    first , second = Mr[i]
    if i == len(Mr)-1:
        new_tup = (second, second+1)
    else:
        new_tup = Mr[i]
    output.append(new_tup)
print(output)
    









# list1=[{"a":1,"b":2,"c":3}]
# list2=[{"a":4,"b":5,"c":6}]
# list3=[{"a":7,"b":8,"c":9}]
 
# #out={"a":[1,4,7],"b":[2,5,8],"c":[3,6,9]}
# output = list1+list2+list3
# result_dict ={key:1 for key in output}
# print(result_dict)


# find . -type f -name "<file_name>" mv "oldfile" "new_file"

# chmod 777
# chmod 444 <filename>
