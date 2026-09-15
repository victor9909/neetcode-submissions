class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = 0
            cnt = 0
            for dr, dc in directions:
                cnt += dfs(r + dr, c + dc)
            return cnt + 1
        
        def bfs(r, c):

            q = deque([(r, c)])
            area = 1
            grid[r][c] = 0
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] == 0 
                    ):
                        continue
                    
                    area += 1
                    q.append((row, col))
                    grid[row][col] = 0

            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(res, area)
        return res
