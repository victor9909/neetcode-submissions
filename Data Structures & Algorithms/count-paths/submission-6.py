class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dfs(r, c):
            if r not in range(m) or c not in range(n):
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]

            if r == m - 1 and c == n - 1:
                return 1
            
            memo[(r, c)] = dfs(r, c + 1) + dfs(r + 1, c)
            return memo[(r, c)]
        
        #return dfs(0, 0)

        dp = [[0] * (n+1) for _ in range(m + 1)]
        dp[m-1][n-1] = 1

        print(dp)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
        return dp[0][0]

