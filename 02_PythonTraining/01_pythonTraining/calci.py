# add,sub
import Arithemtic
# 1 import Arithemtic as Arith  --> both file on same location
# 2 import Arithemtic import add,sub
# 3 import Arithemtic import *

print(__name__)
x = int(input("Enter x : "))
y = int(input("Enter y : "))

ch = input("Enter the choice (+/-) : ")

if ch == '+':
    print("Addition : ", Arithemtic.add(x,y))
    # 1 print("Addition : ", Arith.add(x,y))
    # 2 print("Addition : ", add(x,y))
elif ch =='-':
    print("Substraction : ", Arithemtic.sub(x,y))
    # 1 print("Substraction : ", Arith.sub(x,y))
    # 2 print("Substraction : ", sub(x,y))

