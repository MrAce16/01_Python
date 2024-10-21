#print subb arrays
arr = [1,2,3,4]
total = 0
# n = len(arr)

# for i in range(n):
#     sum1 = arr[i] * (i+1) *(n-i)
#     total += sum1
# print(total)


# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         subarray = arr[i:j+1]
#         total += sum (subarray)
#         print(total)
       

# A = [1, 2, 3, 4]
# B = 2
# B = B % len(A)
# A[:] = A[B:] + A[:B]
# print(A)


# str = "p@ay#t%h$en"
# str1 = ""

def reverse_string_with_special_chars(mystr):
    # Step 1: Extract only the alphabetic characters
    letters = [ch for ch in mystr if ch.isalpha()]
    
    # Step 2: Reverse the alphabetic characters
    letters.reverse()
    
    # Step 3: Rebuild the string while preserving special characters
    result = []
    letter_idx = 0
    
    for ch in mystr:
        if ch.isalpha():
            result.append(letters[letter_idx])
            letter_idx += 1
        else:
            result.append(ch)
    
    # Join the list into a string
    return ''.join(result)

# Example usage
mystr = "P#aay@t%on"
output = reverse_string_with_special_chars(mystr)
print(output)  # Output: "n#o@t%yp"









#o/p = "n@eh#t%a$yp"



# for al in str:
#     if al.isalpha():
#         str1 = al + str1  #p
#     else: 
#         str1 =  al + str1 
# print(str1)