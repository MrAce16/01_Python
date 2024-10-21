# def grocery_store(list1):
#     for i in list1:
#         print(i)


# list1 = ['Apple', '3kg', 250, 'vmart']
# obje1 = grocery_store(list1)
# print(obje1)

def reverse(str1):
    for i in str1[::-1]:
        print(i, end=' ')


str1 = input(str("Enter the string to be reverse :"))
reverse(str1)
