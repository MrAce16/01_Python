# Q1 Write a program to find common letter between 2 strings.
#M1
# str1 = "NAINA"
# str2 = "REENE"
# dub = []
# for i in str1:
#     if i in str2:
#         dub.append(i)
# print(set(dub))

# #M2
# s1,s2 = set(str1),set(str2)
# result = s1 & s2
# print(result)

str4 = "naina is a good girl"
str5 = "reena is a bad girl"
#naina reena good bad
l1 = len(str4.split())

for i in range(l1):
        # print(str4.split()[i])
    if str4.split()[i] not in str5.split()[i]:
         print(str4.split()[i],str5.split()[i] , end = " ")

# lst = []

# for i in str4.split():
#     if i in str5.split():
#         print(i)

# for i in str4.split():
#     for j in str5.split():
#         if i ==j:
#             lst.append(i)
# print(lst)


# s4 = str4.split()
# s5 = str5.split()
# print(s4)

# result = list(result.append(s4 & s5))

# print(result)