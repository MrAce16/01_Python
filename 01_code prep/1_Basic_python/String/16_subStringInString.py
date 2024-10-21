

string = "hello ' welcome in world of string python don't  welcome in world of python"
c = 0
n = len(string.split())
# print(n)
for x in range(n):
    if string.find("python"):
        c = string.count("python")


print(c)
