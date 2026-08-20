class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return 0
            
            visit.add((r, c))
            res = 1
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res