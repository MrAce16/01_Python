#Lambada

list1 = [2,4,5,6,7,8,9]
result= list(map(lambda x:x**2,list1))
print(result)

#multiplication

a = [10]
b = [15]
multi= list(map(lambda x,y : x*y ,a,b))
print(multi)

a = [10]
b = [15]
add = list(filter(lambda x,y:x+y,a,b))
print(add)

# addition