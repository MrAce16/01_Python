# Q1. N of input from user and sort the value.
# n = int(input("How many state you want to enter"))
# i = 1
# list1 = []
# while n > 0:
#     str1 = input("Enter the name of the state")
#     list1.append(str1)
#     n -= 1
# print(sorted(list1))

# Q2. Find the unique character

# Remove dublicate character.

# dublicate_char = "aabbccdef"
# c1 = []
# for i in dublicate_char:
#     if i not in c1:
#         c1.append(i)
# print(c1)


# unique character.
unique_char = "aabbccdef"
unk = []
for i in unique_char:
    if unique_char.count(i) == 1:
        unk.append(i)
print(unk)

# Q3. Count frequency of string
unique_char = "aabbccdefffghj"
for i in unique_char:
    print(unique_char.count(i))
