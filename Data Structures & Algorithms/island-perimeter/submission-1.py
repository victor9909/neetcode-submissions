class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            
            if (r, c) in visit:
                return 0
            
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            
            count = 0
            visit.add((r, c))
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            
            return count
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    res += dfs(r, c)
        return res
