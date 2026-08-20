class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        color_c = image[sr][sc]
        visit = set()
        
        def dfs(r, c):
            nonlocal color_c
            if(
                r not in range(rows) or
                c not in range(cols) or
                image[r][c] != color_c or
                (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image