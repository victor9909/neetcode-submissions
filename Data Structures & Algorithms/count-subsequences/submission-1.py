class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}

        def dfs(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]

            if len(t) <= j:
                return 1
            
            res = 0
            for idx in range(i, len(s)):
                if s[idx] == t[j]:
                    res += dfs(idx + 1, j + 1)
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
