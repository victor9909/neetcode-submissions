class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        def dfs(visit, r, c, prev):

            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                heights[r][c] < prev
            ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(visit, r + dr, c + dc, heights[r][c])
        
        atl, pac = set(), set()
        for r in range(rows):
            dfs(pac, r, 0, heights[r][0])
            dfs(atl, r, cols - 1, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(pac, 0, c, heights[0][c])
            dfs(atl, rows - 1, c, heights[rows - 1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))
        return res
        
