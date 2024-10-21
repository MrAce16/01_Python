# Reverse without using 2nd vriable
lst =  [1,2,3,4]
print(lst[::-1])

start = 0
end = len(lst)-1

while start < end:
    lst[start],lst[end] = lst[end], lst[start]
    start +=1
    end  -=1
    
print(lst)

# class , constructer, and print name

class human():
    def __init__(self,name):
        self.name = name

h = human('raghu')
print(h.name)





 