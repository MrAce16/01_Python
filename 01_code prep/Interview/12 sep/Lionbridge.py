# data = {
#    'Name': ['Alice', 'Bob', 'Charlie'],
#    'Age': [25, 30, 35],
#    'City': ['New York', 'Los Angeles', 'Chicago']
# }
 
# #Filtering out people who are above the age of 30

# # filter_data = {key:value for key,value in data.items() if  key['Age'] <= 30}
# # print(filter_data)

# filter_data = {key:[] for key in data}

# for i in range(len(data['Age'])):
#     if data['Age'][i] <= 30:
#         for key in data:
#             filter_data[key].append(data[key][i])

# print(filter_data)

array= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]

lst = []

for i in array:
    if i not in lst:
        lst.append(i)

print(lst)


[11:08 AM] Gundekar, Sandesh
data = {
   'Name': ['Alice', 'Bob', 'Charlie'],
   'Age': [25, 30, 35],
   'City': ['New York', 'Los Angeles', 'Chicago']
}
 
Filtering out people who are above the age of 30
[11:20 AM] Gundekar, Sandesh
 array= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]
[11:25 AM] Gundekar, Sandesh
try:
 print("Hello")
except:
 print("Something went wrong")
else:
 print("Nothing went wrong")
finally:
 print("From Finally")
[11:26 AM] Gundekar, Sandesh
try:
   print("Hello")
finally:
   print("From Finally")
[11:27 AM] Gundekar, Sandesh
a=123
print(a)
a="xyz"
print(a)
[11:28 AM] Gundekar, Sandesh
x=123
y="abc"
z=x+y
print(z)