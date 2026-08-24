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
        
        return dfs(0, 0)
            
