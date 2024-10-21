def add(no1,no2):
    return no1 + no2

def sub(no1,no2):
    return no1 - no2

def mult(no1,no2):
    return no1 * no2

def expo(no1,no2):
    return no1 ** no2

#__name__ IMP line is 14 and 15
print(__name__)
if __name__ == "main":
    no1 = int(input("Enter No1 : "))
    no2 = int(input("Enter No2 : "))
    print("sum", add(no1,no2))
    print("sub", sub(no1,no2))
    print("mult", mult(no1,no2))
    print("expo", expo(no1,no2))

