class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        def dfs(r, c, prev, sea):
            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in sea or
                prev > heights[r][c]
            ):
                return

            sea.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], sea)
        
        pacific, atlantic = set(), set()
        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows-1][c], atlantic)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
        
        

