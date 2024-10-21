# armstrong number  
def armstrong_num(num):

    digits = [int(d) for d in str(num)]
    power = len(digits)
    sum1 = sum([d ** power for d in digits])

    return num == sum1

count = 0
num = 100
second_armstrong = None
while count < 2 :
    if armstrong_num(num):
        count +=1
        if count ==2:
            second_armstrong = num
    num +=1 
print(f"the second armstrong number :{second_armstrong}")

