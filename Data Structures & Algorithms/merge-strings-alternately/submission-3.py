class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            char1 = word1[i] if i < len(word1) else ""
            char2 = word2[j] if j < len(word2) else ""
            res += char1 + char2
            i += 1
            j += 1
        return res