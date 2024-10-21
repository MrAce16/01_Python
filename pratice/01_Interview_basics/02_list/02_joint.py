list1 = ['my', 'name']
list2 = ['is','john']

#M1
list3 = list1 + list2
print(' '.join(list3))
#M2
list1.extend(list2)
print(' '.join(list1))