# Write a Python program to create a class. 
# * write method to merge two arrays, remove the duplicates, sort and return 3rd largest number.

# * Find the words matching the pattern "he**o" (only characters not numericals) in the Sentence "Hello World, 
# Helllo will also be matched, not hel2o" 

# * Write Unittest for the methods, validate the result

# 1. write method to merge two arrays, remove the duplicates, sort and return 3rd largest number.

def find_third_largest(arr1,arr2):
    '''
    merged two arrays, remove the duplicates sort and return 3rd largest number
    '''
    merge_array = arr1 + arr2  # merged array

    unique_arr = list(set(merge_array)) # unique character

    unique_arr.sort(reverse=True) # sort array in descending order

    if len(unique_arr) >= 3:
        return unique_arr[2]
    
    else:
        return None

arr1 = [3,5,7,9]
arr2 = [2,3,5,8,10]
third_largest = find_third_largest(arr1,arr2)
print(f"The third largest number : {third_largest}")


# Find the words matching the pattern "he**o" (only characters not numericals) in the Sentence "Hello World, 
# Helllo will also be matched, not hel2o" 

# import re 

# def find_word_matching(word:str)->list[str]:
    
#     pattern = r'\bhe[a-zA-Z]{2}o\b'

#     matches = re.findall(pattern, word)
#  TestFindWord(unittest.TestCase):

#     def test_find_wopected_result )
        

        