a = 'xyz'
b = 'abc'

c = a[:2] + b[2]
d = b[:2] + a[2]
print(c, d)


'''    Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 

Sample String : 'abc' 
Expected Result : 'abcing' 
Sample String : 'string' 
Expected Result : 'stringly'  '''

a = 'abc'
b = 'ing'
print(a + b)
