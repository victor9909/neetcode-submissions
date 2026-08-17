class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        
        def dfs(i, j):

            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)
            insert = dfs(i, j + 1)
            return min(delete, replace, insert) + 1
        
        return dfs(0,0)
