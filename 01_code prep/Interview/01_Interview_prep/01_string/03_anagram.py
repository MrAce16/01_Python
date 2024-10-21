# 3. Python program in to check string is anagrams or not

def anagram(str1,str2):
    
    if len(str1) == len(str2) :
        if sorted(str1) == sorted(str2):
            print("anagram")
        else :
            print("Not an anagram")
    else :
        print("Not an anagram")
        
    # for i in str1:
    #     for j in str2 :
    #         if i ==j and len(str1) == len(str2):
    #             print("anagram")

    #         else : 





str1 = "rat5"
str2 = "tar5"
result = anagram(str1,str2)
print(result)