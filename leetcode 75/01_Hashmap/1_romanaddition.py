class Solution(object):
    def romanToInt(self, s):
        symbols = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for x in s:
            if x in symbols:
                total += symbols[x]
        print(total)


obj = Solution()
obj.romanToInt('MCMXC')



