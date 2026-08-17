class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        idx1 = 0
        idx2 = 0
        res = "" 
        while idx1 < len(word1) and idx2 < len(word2):
            res += word1[idx1]
            idx1 += 1
            res += word2[idx2]
            idx2 += 1
        
        if idx1 < len(word1):
            res += word1[idx1:]
        
        if idx2 < len(word2):
            res += word2[idx2:]
        
        return res
