
def missing_no(input):
    sum1 = sum(input)
    x = len(input)+1
    y = (x*(x+1)//2)
    return y-sum1
        

input = [1,2,4,5,6,7]
output = missing_no(input)
print(output)