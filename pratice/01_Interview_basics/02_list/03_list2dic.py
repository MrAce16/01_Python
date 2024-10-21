list1 = ['a','b','c','d']
list2 = [1,2,3,4]
dict1 = dict(zip(list1,list2))
print(dict1)

#using dict comphreshion

dict2 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict2)