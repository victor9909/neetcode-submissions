class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        cache = {}

        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)
            insert = dfs(i, j + 1)
            cache[(i, j)] = min(delete, replace, insert) + 1
            return cache[(i, j)]
        
        #return dfs(0,0)
    
        def dp():

            dp = {}
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == m:
                        dp[(i, j)] = n - j
                    if j == n:
                        dp[(i, j)] = m - i
            
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if word1[i] == word2[j]:
                        dp[(i, j)] = dp[(i + 1,  j + 1)]
                    else:
                        dp[(i, j)] = min(dp[(i+1, j)], dp[(i+1, j+1)], dp[(i, j+1)]) + 1
            
            return dp[(0, 0)]
        
        return dp()










