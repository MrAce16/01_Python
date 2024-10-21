 

Code : 

 

#1 Reverse a string 

# str1 = "hello" 

# print(str1[::-1]) 

#2 Count the string : 

 

# str1= "abcdefgabc" 

# dict1 = {} 

 

# for i in str1: 

#     if i in dict1: 

#         dict1[i] +=1 

#     else: 

#         dict1[i] = 1 

# print(dict1) 

'''Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class''' 

# class Person: 

#     def get_gender(self): 

#         return "None" 

 

# class Male(Person): 

#     def get_gender(self): 

#         return "Male" 

 

# class Female(Person): 

#     def get_gender(self): 

#         return "female" 

 

# male = Male() 

# female = Female() 

 

# print(male.get_gender()) 

# print(female.get_gender()) 

 

# Original alphabet:      abcdefghijklmnopqrstuvwxyz 

# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc 

 

# def encrypt(input_text): 

#     result = "" 

     

#     for char in input_text: 

#         if char.isalpha(): 

#             if char.lower(): 

#                 result+=(char((ord(char))-ord('a')+3)%26 + ord('a')) 

#     return ''.join(result) 

                 

             

# input_text = "abc" 

# encrypted_text = encrypt(input_text) 

# print(encrypted_text) 

 

# balance bracket 

# def is_balance(bracket): 

#     bracket1 = {')':'(','}':'{',']':'['} 

     

#     list1 =[] 

     

#     for char in bracket: 

#         if char in "({[": 

#             list1.append(char) 

#         elif char in ")}]": 

#             if not list1 or list[-1]!= bracket1[i]: 

                 

#                 return "Not balanced" 

 

 

# print(is_balance("(")) 