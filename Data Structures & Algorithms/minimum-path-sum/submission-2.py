class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}

        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if i >= rows or j >= cols:
                return float("inf")
            
            if i == rows - 1 and j == cols - 1:
                return grid[i][j]
            
            memo[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
            return memo[(i, j)]
        
        #return dfs(0, 0)

        dp = [[float("inf")] * (cols + 1) for _ in range((rows + 1))]
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        
        return dp[0][0]


            
