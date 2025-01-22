#input ==> "my name is Raghunath" output ==> "ym eman si htanuhgaR

# def reverse_words(input_str):
#     words = input_str.split(" ")
#     reversed_words = [word[::-1] for word in words]
#     return " ".join(reversed_words)

# input_str = "my name is Raghunath"
# output = reverse_words(input_str)
# print(output)

#input ==> a5b3d2 output==>aaaaabbbdd

# def multiple_string(input_str):
#     result = ""
#     i = 0
#     while i < len(input_str):
#         char = input_str[i]
#         if i + 1 < len(input_str) and input_str[i].isdigit():
#             count = int(input_str[i +1])
#             result += char * count
#             i += 2
#         else:
#             i += 1
#     return result
        
# input_str = "a5b3d2"
# output = multiple_string(input_str)
# print(output)

# select  DISTINCT salary
# from employee
# order by salary desc
# limit 1 offset 2;/


#input ==> a5b3d2 output==>aaaaabbbdd

# def expand_string(input):
#     result = ""
#     i = 0
#     while i < len(input):
#         char = input[i]
#         if i + 1 < len(input) and input[i + 1].isdigit():
#             count = int(input[i + 1])
#             result += char * count
#             i += 2
#         else:
#             i += 1
#     return result

# input = "a5b3d2"
# output = expand_string(input)
# print(output) #aaaaabbbdd



# input 