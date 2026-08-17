class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visit):

            if(
                c not in range(cols) or
                r not in range(rows) or
                grid[r][c] == 0
            ):
                return 1
            
            if(
                (r, c) in visit
            ):
                return 0
            
            cnt = 0
            visit.add((r, c))
            for dr, dc in directions:
                cnt += dfs(r + dr, c + dc, visit)
            return cnt
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c, set())
        