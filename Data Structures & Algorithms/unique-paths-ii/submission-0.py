class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * (cols) for _ in range(rows)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                obstacleGrid[r][c] == 1
            ):
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]

            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]
        
        def dp():
            
            prev_row = [0] * (cols + 1)
            print(prev_row)
            prev_row[cols - 1] = 1

            for r in range(rows - 1, -1, -1):
                for c in range(cols - 1, -1, -1):
                    if obstacleGrid[r][c]:
                        prev_row[c] = 0
                    else:
                        prev_row[c] += prev_row[c + 1]
                print(prev_row)
            return prev_row[0]

        return dp()
