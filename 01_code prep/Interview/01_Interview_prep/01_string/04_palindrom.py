#  Python program to check string is palindrome or not

def palindrom(str1):
    # if str1[::-1] == str1:
    #     print("palindrom")
    # else :
    #     print("Not a palindrom")
    
    # str2 = reversed(str1)
    # if str2 == str1:
    #     print("palindrom")
    # else :
    #     print("Not a palindrom")


    left = 0
    right = len(str1)-1

    while left < right :
        if str1[left] != str1[right]:
            return False
        
        left +=1
        right -=1
    
    return True
          
    
str1 = "madam1"
if palindrom(str1):
    print("palindrom")
else :
    print("Not a palindrom")