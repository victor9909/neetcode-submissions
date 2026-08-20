class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0
            ):
                return 1
            
            if((r, c) in visit):
                return 0
            
            visit.add((r, c))
            res = 0
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)

            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    per = dfs(r, c)
                    return per


