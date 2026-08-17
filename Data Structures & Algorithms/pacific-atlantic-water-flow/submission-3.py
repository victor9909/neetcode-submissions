class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def dfs(r, c, visit, par):

            if(
                r not in range(rows) or
                c not in range(cols) or 
                heights[r][c] < par or
                (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res




