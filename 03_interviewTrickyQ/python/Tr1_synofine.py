# def fibonnacci_gen():
#     a,b = 0, 1

#     while b <=30:
#         yield b
#         a,b = b, a+b

# fibo_sum = sum (fibonnacci_gen())
# print(f"the sum of fibbo series 1 to 30 : {fibo_sum}")




# input_data = [1,1,2,3,5,8,13,21,5,8] #o/p = unique and 

# unique_data = set (input_data)

# element_count = {num : input_data.count(num) for num in unique_data}

# print(f"unique element : {unique_data}")
# print(f"count of each element : {element_count}")


############pandas

#AB,ABC,ABC,ABB,AB 

# import pandas as pd

# data = ['AB','ABC','ABC','ABB','AB']

# df = pd.DataFrame(data, columns=['category'])
# group_count = df.groupby('category').size()
# print(group_count)






