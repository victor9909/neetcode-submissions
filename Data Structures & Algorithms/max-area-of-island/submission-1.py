class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        visit = set()

        def dfs(i, j):
            if(
                i not in range(rows) or
                j not in range(cols) or
                (i, j) in visit or
                grid[i][j] == 0
            ):
                return 0
            
            count = 1
            visit.add((i, j))
            for dr, dc in directions:
                count += dfs(i + dr, j + dc)
            
            return count
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(dfs(r, c), res)

        return res 
            
            

