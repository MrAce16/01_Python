# "Cheese, Milk! 12345? cutter 3456" how many alpha numeric word count -->o/p count=3

str1 = "Cheese, Milk! 12345? cutter 3456"
list1 = []
count = 0
for i in str1.replace(',',' ').split():
    print(i)
    if i.isalnum():
        list1.append(i)
        count += 1
print(count, list1)


#count = Bank1,Bank2,Bank3,Bank4,Bank1,Bank2,Bank5,Bank6,Bank7,Bank8,Bank1,Bank2,Bank9,Bank10,Bank11,Bank1,Bank2,Bank12,Bank1

str2= "Bank1,Bank2,Bank3,Bank4,Bank1,Bank2,Bank5,Bank6,Bank7,Bank8,Bank1,Bank2,Bank9,Bank10,Bank11,Bank1,Bank2,Bank12,Bank1"
bank = str2.split(',')
print(bank)
bank_count = {}

for i in bank:
    if i in bank_count:
        bank_count[i] += 1
    else:
        bank_count[i] =1

max_count = max(bank_count.values())
print(max_count)



# using count 
str = "Bank1,Bank2,Bank3,Bank4,Bank1,Bank2,Bank5,Bank6,Bank7,Bank8,Bank1,Bank2,Bank9,Bank10,Bank11,Bank1,Bank2,Bank12,Bank1"
bank_1 = str.split(',')
max_count = 0
most_frequent_bank = 0

for i in set(bank_1):
    count1 = bank_1.count(i)
    if max_count < count1:
        max_count = count1
        most_frequent_bank = i
print(f"{most_frequent_bank} count is {max_count} times")


