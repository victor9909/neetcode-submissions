class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        atl, pac = set(), set()

        def dfs(r, c, prev_height, visit):
            
            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                prev_height > heights[r][c]
            ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visit)

            return
        
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)

        res = []
        print(atl, pac)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r,c])
        return res
