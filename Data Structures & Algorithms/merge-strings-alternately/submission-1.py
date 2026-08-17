class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        new_str = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            new_str += word1[i] + word2[j]
            i, j = i + 1, j + 1
        
        if i < len(word1):
            new_str += word1[i:]
        if j < len(word2):
            new_str += word2[j:]
        
        return new_str
