from collections import Counter

# username = "<your_username>"
# password = "<password>"


# try :

#     driver.get("https://abc.com/login")

#     driver.maximize_window()

#     username_field = driver.find_element(ID, "username")

#     password_field = driver.find_element(ID, "password")

#     login_button = driver.find_element(ID,"loginButton")
#     login_button.click()

# except Exception as e:
#     print("Login failed")

# Program1 Sort dictionary in descending order

# dict1 = {'a':1, 'b':2, 'c':3}

# sort_values = sorted(dict1.values(), reverse = True)
# print(sort_values)

# sort_items= sorted (dict1.items(), key = lambada x : x[1], reverse= True)

# for key,values in sorted_items:
#     print(f"{key}:{values}")

list1 = [1,2,2,3,4]

occurances = Counter(list1)
print(occurances)

# occurances = {}
# for element in list1:
#     if element in occurances:
#         occurances[element] +=1
#     else:
#         occurances[element] = 1
# print(occurances)

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
dict1.update(dict2)
print(dict1)
    
    
    
    
    
    
    
    
    
    
    
    
