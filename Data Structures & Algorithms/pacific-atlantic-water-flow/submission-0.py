class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()


        def dfs(prev_heigh, visit, r, c):

            if (
                r not in range(rows) or
                c not in range(cols) or
                prev_heigh > heights[r][c] or
                (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            dfs(heights[r][c], visit, r + 1, c)
            dfs(heights[r][c], visit, r, c + 1)
            dfs(heights[r][c], visit, r - 1, c)
            dfs(heights[r][c], visit, r, c - 1)
        
        for c in range(cols):
            dfs(heights[0][c], pac, 0, c)
            dfs(heights[rows - 1][c], atl, rows - 1, c)
        
        for r in range(rows):
            dfs(heights[r][0], pac, r, 0)
            dfs(heights[r][cols-1], atl, r, cols-1)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
        


