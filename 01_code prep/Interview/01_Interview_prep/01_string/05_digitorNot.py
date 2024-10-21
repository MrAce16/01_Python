#Python code to check given character is digit or not



def digit(str):

    # ch = [i for i in range(0,10)]
    # for i in str:
    #     if i == ch :
    #         print("character have digit")
    #     else :
    #         print("character not have digit")
    ch = [i for i in str if i in "123456789"]
    if ch :
        print("Digit found")
    else :
        print("Digit not found")


str = "hello python 5"
result = digit(str)
print(result)

