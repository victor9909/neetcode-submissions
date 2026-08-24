class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m or j >= n:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]
        
        #return dfs(0, 0)

        prev = [0] * (n + 1)
        for i in range(m-1, -1, -1):
            curr = [0] * (n + 1)
            curr[n-1] = 1
            for j in range(n - 2, -1, -1):
                curr[j] = curr[j + 1] + prev[j]
            prev = curr

        return prev[0]
