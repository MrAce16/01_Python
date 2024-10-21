#Q2. count number of times words are appearing.

str = "sheena loves eating apple and mango. Her sister also loves eating apple and mango"
# lst =[]
# count = 1
# for i in str.split(' '):
#     if i not in lst and str.count(i)> 1:
#         lst.append(i)
#         count +=1
# print(f"{lst}:{count}")


dict = {}
for i in str.split():
    i.remove('.')
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
print(dict)
        
