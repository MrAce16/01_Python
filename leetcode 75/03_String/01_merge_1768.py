'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r 

'''
class Solution():

    def mergeAlternately(self,word1: str, word2: str) -> str:

        w1_len, w2_len =len(word1), len(word2)
        min_len = min(w1_len,w2_len) #3
        merged = ""
        for i in range(min_len):
            merged = merged + word1[i] + word2[i]
        if w1_len > w2_len:
            merged = merged + word1[min_len::]
        else :
            merged = merged + word2[min_len::]

        return merged

word1 = "abcdefg"
word2 = "pqr23457"

sol = Solution()
output = sol.mergeAlternately(word1, word2)
print(output)




