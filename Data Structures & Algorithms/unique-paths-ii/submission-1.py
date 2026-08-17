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
        
        return dfs(0, 0)