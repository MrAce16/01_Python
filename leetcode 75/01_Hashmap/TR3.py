str1 = "my name is raghunath jha"
# reverse = str1[::-1]
# words = reverse.split()
# capital_word = [words.capitalize() for word in words]
# print(capital_word)
# word = [reverse.capitalize() for i in reverse]
# print(word)

# words = str1.split()
# reverse_capitalize = [word[::-1].capitalize() for word in words]  # made mistake in capitalize "()""
# output = " ".join(reverse_capitalize)
# print(output)

# words = str1.split()
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
#     result = [word for word in words if word_count[word] == 1]
#     print(result)
#     output = " ".join(result)
# print(output)


def output(str1,character_remove):
    return "".join(char for char in str1 if char!=character_remove)

str1 = "my name is raghunath jha"
character_remove = "a"
result= output(str1,character_remove)
print(result)

