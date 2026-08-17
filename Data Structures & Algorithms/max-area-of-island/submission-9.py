class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = 0
            res = 1
            for dr, dc in directions:
                res += dfs(dr + r, dc + c)
            
            return res
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res
