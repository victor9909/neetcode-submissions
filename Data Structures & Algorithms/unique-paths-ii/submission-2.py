class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if(
                i not in range(n) or
                j not in range(m) or
                obstacleGrid[i][j] == 1
            ):
                return 0
            
            if i == n - 1 and j == m - 1:
                return 1
            
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]
        
        #return dfs(0, 0)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                
                if i == n - 1 and j == m - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                
        return dp[0][0]



