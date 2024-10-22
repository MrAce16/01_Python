#count number of words repeated print max repeated word
sentence = "hello world welcome to the world of python hello python hello"
dic = {}

for i in sentence.split():
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
print(dic) 

max_value = max(dic, key = dic.get)
dic = dic[max_value]
print(dic)

