# 1Question: How would you find the longest common prefix among an array of strings?

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix


# Example usage
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""


# Q2 .How would you find the most frequent character in a string?

def most_frequent_char(s):
    char_count = {}
    max_char = ''
    max_count = 0
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char


# Example usage
print(most_frequent_char("aabbbcccc"))  # Output: "c"


# M2

str1 = "aabbcccdddd"
d = {}
c = {}
max_char = ''
max_count = 0

for i in str1:
    c = str1.count(i)
print(max(c))
