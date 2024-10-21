# Input : Hi i am raghu 
 
# Output : uh g ar maiiH

def reverse_string(input):

    words = input.split()
    result1 = []

    for i in words :
        if len(i)>1:
            first_letter = i[0]
            last_letter = i[-1]
            middle_letter = i[1:-1]
            result= last_letter + middle_letter + first_letter
        else :
            result1= i
            result1.append(result)
    return " ".join(result1)
    # reverse_str = input[::-1]
    # reverse_str1 = reverse_str.split()
    # result = ' '.join(reverse_str1[::-1])
    # return result


input = "Hi i am raghu "
output = reverse_string(input)
print(output)
 