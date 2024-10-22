'''
Example 1:

Input: str1 = "ABCABC", str2 = "ABCABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        commonstr = ""
        for s1,s2 in zip(str1,str2):
            if s1 == s2 :
                if s1 not in commonstr:
                    commonstr = commonstr + s1
        print(commonstr)


str1 = "ABCABC"
str2 = "ABCABC"

sol = Solution()
output = sol.gcdOfStrings(str1, str2)
print(output)


# print(str1.find(str2))
