class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):

            if(i not in range(rows) or j not in range(cols) or (i, j) in visit):
                    return 0
            
            if grid[i][j] == 0:
                return 0

            visit.add((i, j))
            curr_area = 0
            for r, c in directions:
                curr_area += dfs(i + r, j + c)
            
            return curr_area + 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    res = max(dfs(i, j), res)
        
        return res
